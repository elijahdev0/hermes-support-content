---
title: "SigNoz | Dokploy"
source: "https://docs.dokploy.com/docs/templates/signoz"
category: dokploy-docs
created: "2026-06-25T17:21:59.113Z"
---

SigNoz | Dokploy

# SigNoz

Copy as Markdown

SigNoz is an open-source Datadog or New Relic alternative. Get APM, logs,traces, metrics, exceptions, & alerts in a single tool.

## Configuration

docker-compose.ymltemplate.toml

```
x-common: &common
  networks:
    - signoz-net
  restart: unless-stopped
  logging:
    options:
      max-size: 50m
      max-file: "3"
x-clickhouse-defaults: &clickhouse-defaults
  !!merge <<: *common
  image: clickhouse/clickhouse-server:25.5.6
  tty: true
  labels:
    signoz.io/scrape: "true"
    signoz.io/port: "9363"
    signoz.io/path: "/metrics"
  depends_on:
    init-clickhouse:
      condition: service_completed_successfully
    zookeeper-1:
      condition: service_healthy
  healthcheck:
    test:
      - CMD
      - wget
      - --spider
      - -q
      - 0.0.0.0:8123/ping
    interval: 30s
    timeout: 5s
    retries: 3
  ulimits:
    nproc: 65535
    nofile:
      soft: 262144
      hard: 262144
  environment:
    - CLICKHOUSE_SKIP_USER_SETUP=1
x-zookeeper-defaults: &zookeeper-defaults
  !!merge <<: *common
  image: signoz/zookeeper:3.7.1
  user: root
  labels:
    signoz.io/scrape: "true"
    signoz.io/port: "9141"
    signoz.io/path: "/metrics"
  healthcheck:
    test:
      - CMD-SHELL
      - curl -s -m 2 http://localhost:8080/commands/ruok | grep error | grep null
    interval: 30s
    timeout: 5s
    retries: 3
x-db-depend: &db-depend
  !!merge <<: *common
  depends_on:
    clickhouse:
      condition: service_healthy
    schema-migrator-sync:
      condition: service_completed_successfully
services:
  init-clickhouse:
    !!merge <<: *common
    image: clickhouse/clickhouse-server:25.5.6
    command:
      - bash
      - -c
      - |
        version="v0.0.1"
        node_os=$$(uname -s | tr '[:upper:]' '[:lower:]')
        node_arch=$$(uname -m | sed s/aarch64/arm64/ | sed s/x86_64/amd64/)
        echo "Fetching histogram-binary for $${node_os}/$${node_arch}"
        cd /tmp
        wget -O histogram-quantile.tar.gz "https://github.com/SigNoz/signoz/releases/download/histogram-quantile%2F$${version}/histogram-quantile_$${node_os}_$${node_arch}.tar.gz"
        tar -xvzf histogram-quantile.tar.gz
        mv histogram-quantile /var/lib/clickhouse/user_scripts/histogramQuantile
    restart: on-failure
    volumes:
      - ../files/clickhouse/user_scripts:/var/lib/clickhouse/user_scripts/
  zookeeper-1:
    !!merge <<: *zookeeper-defaults
    volumes:
      - zookeeper-1:/bitnami/zookeeper
    environment:
      - ZOO_SERVER_ID=1
      - ALLOW_ANONYMOUS_LOGIN=yes
      - ZOO_AUTOPURGE_INTERVAL=1
      - ZOO_ENABLE_PROMETHEUS_METRICS=yes
      - ZOO_PROMETHEUS_METRICS_PORT_NUMBER=9141
  clickhouse:
    !!merge <<: *clickhouse-defaults
    container_name: signoz-clickhouse
    volumes:
      - ../files/clickhouse/config.xml:/etc/clickhouse-server/config.xml
      - ../files/clickhouse/user_scripts:/var/lib/clickhouse/user_scripts/
      - ../files/clickhouse/cluster.xml:/etc/clickhouse-server/config.d/cluster.xml
      - clickhouse:/var/lib/clickhouse/
  signoz:
    !!merge <<: *db-depend
    image: signoz/signoz:v0.97.1
    command:
      - --config=/root/config/prometheus.yml
    ports:
      - "8080"
    volumes:
      - ../files/signoz/prometheus.yml:/root/config/prometheus.yml
      - sqlite:/var/lib/signoz/
    environment:
      - SIGNOZ_ALERTMANAGER_PROVIDER=signoz
      - SIGNOZ_TELEMETRYSTORE_CLICKHOUSE_DSN=tcp://clickhouse:9000
      - SIGNOZ_SQLSTORE_SQLITE_PATH=/var/lib/signoz/signoz.db
      - STORAGE=clickhouse
      - TELEMETRY_ENABLED=true
      - DEPLOYMENT_TYPE=docker-standalone-amd
      - DOT_METRICS_ENABLED=true
      - SIGNOZ_JWT_SECRET=${SIGNOZ_JWT_SECRET}
    healthcheck:
      test:
        - CMD
        - wget
        - --spider
        - -q
        - localhost:8080/api/v1/health
      interval: 30s
      timeout: 5s
      retries: 3
  otel-collector:
    !!merge <<: *db-depend
    image: signoz/signoz-otel-collector:v0.129.7
    command:
      - --config=/etc/otel-collector-config.yaml
    volumes:
      - ../files/collector/otel-collector-config.yaml:/etc/otel-collector-config.yaml
    ports:
      - "4317" # OTLP gRPC receiver
      - "4318" # OTLP HTTP receiver
    depends_on:
      signoz:
        condition: service_healthy
  schema-migrator-sync:
    !!merge <<: *common
    image: signoz/signoz-schema-migrator:v0.129.7
    command:
      - sync
      - --dsn=tcp://clickhouse:9000
      - --up=
    depends_on:
      clickhouse:
        condition: service_healthy
    restart: on-failure
  schema-migrator-async:
    !!merge <<: *db-depend
    image: signoz/signoz-schema-migrator:v0.129.7
    command:
      - async
      - --dsn=tcp://clickhouse:9000
      - --up=
    restart: on-failure
networks:
  signoz-net:
    name: signoz-net
volumes:
  clickhouse:
    name: signoz-clickhouse
  sqlite:
    name: signoz-sqlite
  zookeeper-1:
    name: signoz-zookeeper-1
```

```
[variables]
main_domain = "${domain}"
jwt_secret = "${password:64}"

[config]
[[config.domains]]
serviceName = "signoz"
port = 8080
host = "${main_domain}"
path = "/"

[[config.domains]]
serviceName = "otel-collector"
port = 4318
host = "${main_domain}"
path = "/"

[config.env]
SIGNOZ_JWT_SECRET = "${jwt_secret}"

[[config.mounts]]
filePath = "/clickhouse/config.xml"
content = """
<?xml version="1.0"?>
<!--
  NOTE: User and query level settings are set up in "users.xml" file.
  If you have accidentally specified user-level settings here, server won't start.
  You can either move the settings to the right place inside "users.xml" file
   or add <skip_check_for_incorrect_settings>1</skip_check_for_incorrect_settings> here.
-->
<clickhouse>
    <logger>
        <!-- Possible levels [1]:

          - none (turns off logging)
          - fatal
          - critical
          - error
          - warning
          - notice
          - information
          - debug
          - trace
          - test (not for production usage)

            [1]: https://github.com/pocoproject/poco/blob/poco-1.9.4-release/Foundation/include/Poco/Logger.h#L105-L114
        -->
        <level>information</level>
        <formatting>
            <type>json</type>
        </formatting>
        <log>/var/log/clickhouse-server/clickhouse-server.log</log>
        <errorlog>/var/log/clickhouse-server/clickhouse-server.err.log</errorlog>
        <!-- Rotation policy
             See https://github.com/pocoproject/poco/blob/poco-1.9.4-release/Foundation/include/Poco/FileChannel.h#L54-L85
          -->
        <size>1000M</size>
        <count>10</count>
        <!-- <console>1</console> --> <!-- Default behavior is autodetection (log to console if not daemon mode and is tty) -->

        <!-- Per level overrides (legacy):

        For example to suppress logging of the ConfigReloader you can use:
        NOTE: levels.logger is reserved, see below.
        -->
        <!--
        <levels>
          <ConfigReloader>none</ConfigReloader>
        </levels>
        -->

        <!-- Per level overrides:

        For example to suppress logging of the RBAC for default user you can use:
        (But please note that the logger name maybe changed from version to version, even after minor upgrade)
        -->
        <!--
        <levels>
          <logger>
            <name>ContextAccess (default)</name>
            <level>none</level>
          </logger>
          <logger>
            <name>DatabaseOrdinary (test)</name>
            <level>none</level>
          </logger>
        </levels>
        -->
    </logger>

    <!-- Add headers to response in options request. OPTIONS method is used in CORS preflight requests. -->
    <!-- It is off by default. Next headers are obligate for CORS.-->
    <!-- http_options_response>
        <header>
            <name>Access-Control-Allow-Origin</name>
            <value>*</value>
        </header>
        <header>
            <name>Access-Control-Allow-Headers</name>
            <value>origin, x-requested-with</value>
        </header>
        <header>
            <name>Access-Control-Allow-Methods</name>
            <value>POST, GET, OPTIONS</value>
        </header>
        <header>
            <name>Access-Control-Max-Age</name>
            <value>86400</value>
        </header>
    </http_options_response -->

    <!-- It is the name that will be shown in the clickhouse-client.
         By default, anything with "production" will be highlighted in red in query prompt.
    -->
    <!--display_name>production</display_name-->

    <!-- Port for HTTP API. See also 'https_port' for secure connections.
         This interface is also used by ODBC and JDBC drivers (DataGrip, Dbeaver, ...)
         and by most of web interfaces (embedded UI, Grafana, Redash, ...).
      -->
    <http_port>8123</http_port>

    <!-- Port for interaction by native protocol with:
         - clickhouse-client and other native ClickHouse tools (clickhouse-benchmark, clickhouse-copier);
         - clickhouse-server with other clickhouse-servers for distributed query processing;
         - ClickHouse drivers and applications supporting native protocol
         (this protocol is also informally called as "the TCP protocol");
         See also 'tcp_port_secure' for secure connections.
    -->
    <tcp_port>9000</tcp_port>

    <!-- Compatibility with MySQL protocol.
         ClickHouse will pretend to be MySQL for applications connecting to this port.
    -->
    <mysql_port>9004</mysql_port>

    <!-- Compatibility with PostgreSQL protocol.
         ClickHouse will pretend to be PostgreSQL for applications connecting to this port.
    -->
    <postgresql_port>9005</postgresql_port>

    <!-- HTTP API with TLS (HTTPS).
         You have to configure certificate to enable this interface.
         See the openSSL section below.
    -->
    <!-- <https_port>8443</https_port> -->

    <!-- Native interface with TLS.
         You have to configure certificate to enable this interface.
         See the openSSL section below.
    -->
    <!-- <tcp_port_secure>9440</tcp_port_secure> -->

    <!-- Native interface wrapped with PROXYv1 protocol
         PROXYv1 header sent for every connection.
         ClickHouse will extract information about proxy-forwarded client address from the header.
    -->
    <!-- <tcp_with_proxy_port>9011</tcp_with_proxy_port> -->

    <!-- Port for communication between replicas. Used for data exchange.
         It provides low-level data access between servers.
         This port should not be accessible from untrusted networks.
         See also 'interserver_http_credentials'.
         Data transferred over connections to this port should not go through untrusted networks.
         See also 'interserver_https_port'.
      -->
    <interserver_http_port>9009</interserver_http_port>

    <!-- Port for communication between replicas with TLS.
         You have to configure certificate to enable this interface.
         See the openSSL section below.
         See also 'interserver_http_credentials'.
      -->
    <!-- <interserver_https_port>9010</interserver_https_port> -->

    <!-- Hostname that is used by other replicas to request this server.
         If not specified, then it is determined analogous to 'hostname -f' command.
         This setting could be used to switch replication to another network interface
         (the server may be connected to multiple networks via multiple addresses)
      -->

    <!--
    <interserver_http_host>example.clickhouse.com</interserver_http_host>
    -->

    <!-- You can specify credentials for authenthication between replicas.
         This is required when interserver_https_port is accessible from untrusted networks,
         and also recommended to avoid SSRF attacks from possibly compromised services in your network.
      -->
    <!--<interserver_http_credentials>
        <user>interserver</user>
        <password></password>
    </interserver_http_credentials>-->

    <!-- Listen specified address.
         Use :: (wildcard IPv6 address), if you want to accept connections both with IPv4 and IPv6 from everywhere.
         Notes:
         If you open connections from wildcard address, make sure that at least one of the following measures applied:
         - server is protected by firewall and not accessible from untrusted networks;
         - all users are restricted to subset of network addresses (see users.xml);
         - all users have strong passwords, only secure (TLS) interfaces are accessible, or connections are only made via TLS interfaces.
         - users without password have readonly access.
         See also: https://www.shodan.io/search?query=clickhouse
      -->
    <!-- <listen_host>::</listen_host> -->

    <!-- Same for hosts without support for IPv6: -->
    <!-- <listen_host>0.0.0.0</listen_host> -->

    <!-- Default values - try listen localhost on IPv4 and IPv6. -->
    <!--
    <listen_host>::1</listen_host>
    <listen_host>127.0.0.1</listen_host>
    -->

    <!-- Don't exit if IPv6 or IPv4 networks are unavailable while trying to listen. -->
    <!-- <listen_try>0</listen_try> -->

    <!-- Allow multiple servers to listen on the same address:port. This is not recommended.
      -->
    <!-- <listen_reuse_port>0</listen_reuse_port> -->

    <!-- <listen_backlog>4096</listen_backlog> -->

    <max_connections>4096</max_connections>

    <!-- For 'Connection: keep-alive' in HTTP 1.1 -->
    <keep_alive_timeout>3</keep_alive_timeout>

    <!-- gRPC protocol (see src/Server/grpc_protos/clickhouse_grpc.proto for the API) -->
    <!-- <grpc_port>9100</grpc_port> -->
    <grpc>
        <enable_ssl>false</enable_ssl>

        <!-- The following two files are used only if enable_ssl=1 -->
        <ssl_cert_file>/path/to/ssl_cert_file</ssl_cert_file>
        <ssl_key_file>/path/to/ssl_key_file</ssl_key_file>

        <!-- Whether server will request client for a certificate -->
        <ssl_require_client_auth>false</ssl_require_client_auth>

        <!-- The following file is used only if ssl_require_client_auth=1 -->
        <ssl_ca_cert_file>/path/to/ssl_ca_cert_file</ssl_ca_cert_file>

        <!-- Default transport compression type (can be overridden by client, see the transport_compression_type field in QueryInfo).
             Supported algorithms: none, deflate, gzip, stream_gzip -->
        <transport_compression_type>none</transport_compression_type>

        <!-- Default transport compression level. Supported levels: 0..3 -->
        <transport_compression_level>0</transport_compression_level>

        <!-- Send/receive message size limits in bytes. -1 means unlimited -->
        <max_send_message_size>-1</max_send_message_size>
        <max_receive_message_size>-1</max_receive_message_size>

        <!-- Enable if you want very detailed logs -->
        <verbose_logs>false</verbose_logs>
    </grpc>

    <!-- Used with https_port and tcp_port_secure. Full ssl options list: https://github.com/ClickHouse-Extras/poco/blob/master/NetSSL_OpenSSL/include/Poco/Net/SSLManager.h#L71 -->
    <openSSL>
        <server> <!-- Used for https server AND secure tcp port -->
            <!-- openssl req -subj "/CN=localhost" -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout /etc/clickhouse-server/server.key -out /etc/clickhouse-server/server.crt -->
            <!-- <certificateFile>/etc/clickhouse-server/server.crt</certificateFile> -->
            <!-- <privateKeyFile>/etc/clickhouse-server/server.key</privateKeyFile> -->
            <!-- dhparams are optional. You can delete the <dhParamsFile> element.
                 To generate dhparams, use the following command:
                  openssl dhparam -out /etc/clickhouse-server/dhparam.pem 4096
                 Only file format with BEGIN DH PARAMETERS is supported.
              -->
            <!-- <dhParamsFile>/etc/clickhouse-server/dhparam.pem</dhParamsFile>-->
            <verificationMode>none</verificationMode>
            <loadDefaultCAFile>true</loadDefaultCAFile>
            <cacheSessions>true</cacheSessions>
            <disableProtocols>sslv2,sslv3</disableProtocols>
            <preferServerCiphers>true</preferServerCiphers>
        </server>

        <client> <!-- Used for connecting to https dictionary source and secured Zookeeper communication -->
            <loadDefaultCAFile>true</loadDefaultCAFile>
            <cacheSessions>true</cacheSessions>
            <disableProtocols>sslv2,sslv3</disableProtocols>
            <preferServerCiphers>true</preferServerCiphers>
            <!-- Use for self-signed: <verificationMode>none</verificationMode> -->
            <invalidCertificateHandler>
                <!-- Use for self-signed: <name>AcceptCertificateHandler</name> -->
                <name>RejectCertificateHandler</name>
            </invalidCertificateHandler>
        </client>
    </openSSL>

    <!-- Default root page on http[s] server. For example load UI from https://tabix.io/ when opening http://localhost:8123 -->
    <!--
    <http_server_default_response><![CDATA[<html ng-app="SMI2"><head><base href="http://ui.tabix.io/"></head><body><div ui-view="" class="content-ui"></div><script src="http://loader.tabix.io/master.js"></script></body></html>]]></http_server_default_response>
    -->

    <!-- Maximum number of concurrent queries. -->
    <max_concurrent_queries>100</max_concurrent_queries>

    <!-- Maximum memory usage (resident set size) for server process.
         Zero value or unset means default. Default is "max_server_memory_usage_to_ram_ratio" of available physical RAM.
         If the value is larger than "max_server_memory_usage_to_ram_ratio" of available physical RAM, it will be cut down.

         The constraint is checked on query execution time.
         If a query tries to allocate memory and the current memory usage plus allocation is greater
          than specified threshold, exception will be thrown.

         It is not practical to set this constraint to small values like just a few gigabytes,
          because memory allocator will keep this amount of memory in caches and the server will deny service of queries.
      -->
    <max_server_memory_usage>0</max_server_memory_usage>

    <!-- Maximum number of threads in the Global thread pool.
    This will default to a maximum of 10000 threads if not specified.
    This setting will be useful in scenarios where there are a large number
    of distributed queries that are running concurrently but are idling most
    of the time, in which case a higher number of threads might be required.
    -->

    <max_thread_pool_size>10000</max_thread_pool_size>

    <!-- Number of workers to recycle connections in background (see also drain_timeout).
         If the pool is full, connection will be drained synchronously. -->
    <!-- <max_threads_for_connection_collector>10</max_threads_for_connection_collector> -->

    <!-- On memory constrained environments you may have to set this to value larger than 1.
      -->
    <max_server_memory_usage_to_ram_ratio>0.9</max_server_memory_usage_to_ram_ratio>

    <!-- Simple server-wide memory profiler. Collect a stack trace at every peak allocation step (in bytes).
         Data will be stored in system.trace_log table with query_id = empty string.
         Zero means disabled.
      -->
    <total_memory_profiler_step>4194304</total_memory_profiler_step>

    <!-- Collect random allocations and deallocations and write them into system.trace_log with 'MemorySample' trace_type.
         The probability is for every alloc/free regardless to the size of the allocation.
         Note that sampling happens only when the amount of untracked memory exceeds the untracked memory limit,
          which is 4 MiB by default but can be lowered if 'total_memory_profiler_step' is lowered.
         You may want to set 'total_memory_profiler_step' to 1 for extra fine grained sampling.
      -->
    <total_memory_tracker_sample_probability>0</total_memory_tracker_sample_probability>

    <!-- Set limit on number of open files (default: maximum). This setting makes sense on Mac OS X because getrlimit() fails to retrieve
         correct maximum value. -->
    <!-- <max_open_files>262144</max_open_files> -->

    <!-- Size of cache of uncompressed blocks of data, used in tables of MergeTree family.
         In bytes. Cache is single for server. Memory is allocated only on demand.
         Cache is used when 'use_uncompressed_cache' user setting turned on (off by default).
         Uncompressed cache is advantageous only for very short queries and in rare cases.

         Note: uncompressed cache can be pointless for lz4, because memory bandwidth
         is slower than multi-core decompression on some server configurations.
         Enabling it can sometimes paradoxically make queries slower.
      -->
    <uncompressed_cache_size>8589934592</uncompressed_cache_size>

    <!-- Approximate size of mark cache, used in tables of MergeTree family.
         In bytes. Cache is single for server. Memory is allocated only on demand.
         You should not lower this value.
      -->
    <mark_cache_size>5368709120</mark_cache_size>

    <!-- If you enable the `min_bytes_to_use_mmap_io` setting,
         the data in MergeTree tables can be read with mmap to avoid copying from kernel to userspace.
         It makes sense only for large files and helps only if data reside in page cache.
         To avoid frequent open/mmap/munmap/close calls (which are very expensive due to consequent page faults)
         and to reuse mappings from several threads and queries,
         the cache of mapped files is maintained. Its size is the number of mapped regions (usually equal to the number of mapped files).
         The amount of data in mapped files can be monitored
         in system.metrics, system.metric_log by the MMappedFiles, MMappedFileBytes metrics
         and in system.asynchronous_metrics, system.asynchronous_metrics_log by the MMapCacheCells metric,
         and also in system.events, system.processes, system.query_log, system.query_thread_log, system.query_views_log by the
         CreatedReadBufferMMap, CreatedReadBufferMMapFailed, MMappedFileCacheHits, MMappedFileCacheMisses events.
         Note that the amount of data in mapped files does not consume memory directly and is not accounted
         in query or server memory usage - because this memory can be discarded similar to OS page cache.
         The cache is dropped (the files are closed) automatically on removal of old parts in MergeTree,
         also it can be dropped manually by the SYSTEM DROP MMAP CACHE query.
      -->
    <mmap_cache_size>1000</mmap_cache_size>

    <!-- Cache size in bytes for compiled expressions.-->
    <compiled_expression_cache_size>134217728</compiled_expression_cache_size>

    <!-- Cache size in elements for compiled expressions.-->
    <compiled_expression_cache_elements_size>10000</compiled_expression_cache_elements_size>

    <!-- Path to data directory, with trailing slash. -->
    <path>/var/lib/clickhouse/</path>

    <!-- Path to temporary data for processing hard queries. -->
    <tmp_path>/var/lib/clickhouse/tmp/</tmp_path>

    <!-- Disable AuthType plaintext_password and no_password for ACL. -->
    <!-- <allow_plaintext_password>0</allow_plaintext_password> -->
    <!-- <allow_no_password>0</allow_no_password> -->`

    <!-- Policy from the <storage_configuration> for the temporary files.
         If not set <tmp_path> is used, otherwise <tmp_path> is ignored.

         Notes:
         - move_factor              is ignored
         - keep_free_space_bytes    is ignored
         - max_data_part_size_bytes is ignored
         - you must have exactly one volume in that policy
    -->
    <!-- <tmp_policy>tmp</tmp_policy> -->

    <!-- Directory with user provided files that are accessible by 'file' table function. -->
    <user_files_path>/var/lib/clickhouse/user_files/</user_files_path>

    <!-- LDAP server definitions. -->
    <ldap_servers>
        <!-- List LDAP servers with their connection parameters here to later 1) use them as authenticators for dedicated local users,
              who have 'ldap' authentication mechanism specified instead of 'password', or to 2) use them as remote user directories.
             Parameters:
                host - LDAP server hostname or IP, this parameter is mandatory and cannot be empty.
                port - LDAP server port, default is 636 if enable_tls is set to true, 389 otherwise.
                bind_dn - template used to construct the DN to bind to.
                        The resulting DN will be constructed by replacing all '{user_name}' substrings of the template with the actual
                         user name during each authentication attempt.
                user_dn_detection - section with LDAP search parameters for detecting the actual user DN of the bound user.
                        This is mainly used in search filters for further role mapping when the server is Active Directory. The
                         resulting user DN will be used when replacing '{user_dn}' substrings wherever they are allowed. By default,
                         user DN is set equal to bind DN, but once search is performed, it will be updated with to the actual detected
                         user DN value.
                    base_dn - template used to construct the base DN for the LDAP search.
                            The resulting DN will be constructed by replacing all '{user_name}' and '{bind_dn}' substrings
                             of the template with the actual user name and bind DN during the LDAP search.
                    scope - scope of the LDAP search.
                            Accepted values are: 'base', 'one_level', 'children', 'subtree' (the default).
                    search_filter - template used to construct the search filter for the LDAP search.
                            The resulting filter will be constructed by replacing all '{user_name}', '{bind_dn}', and '{base_dn}'
                             substrings of the template with the actual user name, bind DN, and base DN during the LDAP search.
                            Note, that the special characters must be escaped properly in XML.
                verification_cooldown - a period of time, in seconds, after a successful bind attempt, during which a user will be assumed
                         to be successfully authenticated for all consecutive requests without contacting the LDAP server.
                        Specify 0 (the default) to disable caching and force contacting the LDAP server for each authentication request.
                enable_tls - flag to trigger use of secure connection to the LDAP server.
                        Specify 'no' for plain text (ldap://) protocol (not recommended).
                        Specify 'yes' for LDAP over SSL/TLS (ldaps://) protocol (recommended, the default).
                        Specify 'starttls' for legacy StartTLS protocol (plain text (ldap://) protocol, upgraded to TLS).
                tls_minimum_protocol_version - the minimum protocol version of SSL/TLS.
                        Accepted values are: 'ssl2', 'ssl3', 'tls1.0', 'tls1.1', 'tls1.2' (the default).
                tls_require_cert - SSL/TLS peer certificate verification behavior.
                        Accepted values are: 'never', 'allow', 'try', 'demand' (the default).
                tls_cert_file - path to certificate file.
                tls_key_file - path to certificate key file.
                tls_ca_cert_file - path to CA certificate file.
                tls_ca_cert_dir - path to the directory containing CA certificates.
                tls_cipher_suite - allowed cipher suite (in OpenSSL notation).
             Example:
                <my_ldap_server>
                    <host>localhost</host>
                    <port>636</port>
                    <bind_dn>uid={user_name},ou=users,dc=example,dc=com</bind_dn>
                    <verification_cooldown>300</verification_cooldown>
                    <enable_tls>yes</enable_tls>
                    <tls_minimum_protocol_version>tls1.2</tls_minimum_protocol_version>
                    <tls_require_cert>demand</tls_require_cert>
                    <tls_cert_file>/path/to/tls_cert_file</tls_cert_file>
                    <tls_key_file>/path/to/tls_key_file</tls_key_file>
                    <tls_ca_cert_file>/path/to/tls_ca_cert_file</tls_ca_cert_file>
                    <tls_ca_cert_dir>/path/to/tls_ca_cert_dir</tls_ca_cert_dir>
                    <tls_cipher_suite>ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:AES256-GCM-SHA384</tls_cipher_suite>
                </my_ldap_server>
             Example (typical Active Directory with configured user DN detection for further role mapping):
                <my_ad_server>
                    <host>localhost</host>
                    <port>389</port>
                    <bind_dn>EXAMPLE\{user_name}</bind_dn>
                    <user_dn_detection>
                        <base_dn>CN=Users,DC=example,DC=com</base_dn>
                        <search_filter>(&(objectClass=user)(sAMAccountName={user_name}))</search_filter>
                    </user_dn_detection>
                    <enable_tls>no</enable_tls>
                </my_ad_server>
        -->
    </ldap_servers>

    <!-- To enable Kerberos authentication support for HTTP requests (GSS-SPNEGO), for those users who are explicitly configured
          to authenticate via Kerberos, define a single 'kerberos' section here.
         Parameters:
            principal - canonical service principal name, that will be acquired and used when accepting security contexts.
                    This parameter is optional, if omitted, the default principal will be used.
                    This parameter cannot be specified together with 'realm' parameter.
            realm - a realm, that will be used to restrict authentication to only those requests whose initiator's realm matches it.
                    This parameter is optional, if omitted, no additional filtering by realm will be applied.
                    This parameter cannot be specified together with 'principal' parameter.
         Example:
            <kerberos />
         Example:
            <kerberos>
                <principal>HTTP/[email protected]</principal>
            </kerberos>
         Example:
            <kerberos>
                <realm>EXAMPLE.COM</realm>
            </kerberos>
    -->

    <!-- Sources to read users, roles, access rights, profiles of settings, quotas. -->
    <user_directories>
        <users_xml>
            <!-- Path to configuration file with predefined users. -->
            <path>users.xml</path>
        </users_xml>
        <local_directory>
            <!-- Path to folder where users created by SQL commands are stored. -->
            <path>/var/lib/clickhouse/access/</path>
        </local_directory>

        <!-- To add an LDAP server as a remote user directory of users that are not defined locally, define a single 'ldap' section
              with the following parameters:
                server - one of LDAP server names defined in 'ldap_servers' config section above.
                        This parameter is mandatory and cannot be empty.
                roles - section with a list of locally defined roles that will be assigned to each user retrieved from the LDAP server.
                        If no roles are specified here or assigned during role mapping (below), user will not be able to perform any
                         actions after authentication.
                role_mapping - section with LDAP search parameters and mapping rules.
                        When a user authenticates, while still bound to LDAP, an LDAP search is performed using search_filter and the
                         name of the logged in user. For each entry found during that search, the value of the specified attribute is
                         extracted. For each attribute value that has the specified prefix, the prefix is removed, and the rest of the
                         value becomes the name of a local role defined in ClickHouse, which is expected to be created beforehand by
                         CREATE ROLE command.
                        There can be multiple 'role_mapping' sections defined inside the same 'ldap' section. All of them will be
                         applied.
                    base_dn - template used to construct the base DN for the LDAP search.
                            The resulting DN will be constructed by replacing all '{user_name}', '{bind_dn}', and '{user_dn}'
                             substrings of the template with the actual user name, bind DN, and user DN during each LDAP search.
                    scope - scope of the LDAP search.
                            Accepted values are: 'base', 'one_level', 'children', 'subtree' (the default).
                    search_filter - template used to construct the search filter for the LDAP search.
                            The resulting filter will be constructed by replacing all '{user_name}', '{bind_dn}', '{user_dn}', and
                             '{base_dn}' substrings of the template with the actual user name, bind DN, user DN, and base DN during
                             each LDAP search.
                            Note, that the special characters must be escaped properly in XML.
                    attribute - attribute name whose values will be returned by the LDAP search. 'cn', by default.
                    prefix - prefix, that will be expected to be in front of each string in the original list of strings returned by
                             the LDAP search. Prefix will be removed from the original strings and resulting strings will be treated
                             as local role names. Empty, by default.
             Example:
                <ldap>
                    <server>my_ldap_server</server>
                    <roles>
                        <my_local_role1 />
                        <my_local_role2 />
                    </roles>
                    <role_mapping>
                        <base_dn>ou=groups,dc=example,dc=com</base_dn>
                        <scope>subtree</scope>
                        <search_filter>(&(objectClass=groupOfNames)(member={bind_dn}))</search_filter>
                        <attribute>cn</attribute>
                        <prefix>clickhouse_</prefix>
                    </role_mapping>
                </ldap>
             Example (typical Active Directory with role mapping that relies on the detected user DN):
                <ldap>
                    <server>my_ad_server</server>
                    <role_mapping>
                        <base_dn>CN=Users,DC=example,DC=com</base_dn>
                        <attribute>CN</attribute>
                        <scope>subtree</scope>
                        <search_filter>(&(objectClass=group)(member={user_dn}))</search_filter>
                        <prefix>clickhouse_</prefix>
                    </role_mapping>
                </ldap>
        -->
    </user_directories>

    <!-- Default profile of settings. -->
    <default_profile>default</default_profile>

    <!-- Comma-separated list of prefixes for user-defined settings. -->
    <custom_settings_prefixes></custom_settings_prefixes>

    <!-- System profile of settings. This settings are used by internal processes (Distributed DDL worker and so on). -->
    <!-- <system_profile>default</system_profile> -->

    <!-- Buffer profile of settings.
         This settings are used by Buffer storage to flush data to the underlying table.
         Default: used from system_profile directive.
    -->
    <!-- <buffer_profile>default</buffer_profile> -->

    <!-- Default database. -->
    <default_database>default</default_database>

    <!-- Server time zone could be set here.

         Time zone is used when converting between String and DateTime types,
          when printing DateTime in text formats and parsing DateTime from text,
          it is used in date and time related functions, if specific time zone was not passed as an argument.

         Time zone is specified as identifier from IANA time zone database, like UTC or Africa/Abidjan.
         If not specified, system time zone at server startup is used.

         Please note, that server could display time zone alias instead of specified name.
         Example: Zulu is an alias for UTC.
    -->
    <!-- <timezone>UTC</timezone> -->

    <!-- You can specify umask here (see "man umask"). Server will apply it on startup.
         Number is always parsed as octal. Default umask is 027 (other users cannot read logs, data files, etc; group can only read).
    -->
    <!-- <umask>022</umask> -->

    <!-- Perform mlockall after startup to lower first queries latency
          and to prevent clickhouse executable from being paged out under high IO load.
         Enabling this option is recommended but will lead to increased startup time for up to a few seconds.
    -->
    <mlock_executable>true</mlock_executable>

    <!-- Reallocate memory for machine code ("text") using huge pages. Highly experimental. -->
    <remap_executable>false</remap_executable>

    <![CDATA[
         Uncomment below in order to use JDBC table engine and function.

         To install and run JDBC bridge in background:
         * [Debian/Ubuntu]
           export MVN_URL=https://repo1.maven.org/maven2/ru/yandex/clickhouse/clickhouse-jdbc-bridge
           export PKG_VER=$(curl -sL $MVN_URL/maven-metadata.xml | grep '<release>' | sed -e 's|.*>\(.*\)<.*|\1|')
           wget https://github.com/ClickHouse/clickhouse-jdbc-bridge/releases/download/v$PKG_VER/clickhouse-jdbc-bridge_$PKG_VER-1_all.deb
           apt install --no-install-recommends -f ./clickhouse-jdbc-bridge_$PKG_VER-1_all.deb
           clickhouse-jdbc-bridge &

         * [CentOS/RHEL]
           export MVN_URL=https://repo1.maven.org/maven2/ru/yandex/clickhouse/clickhouse-jdbc-bridge
           export PKG_VER=$(curl -sL $MVN_URL/maven-metadata.xml | grep '<release>' | sed -e 's|.*>\(.*\)<.*|\1|')
           wget https://github.com/ClickHouse/clickhouse-jdbc-bridge/releases/download/v$PKG_VER/clickhouse-jdbc-bridge-$PKG_VER-1.noarch.rpm
           yum localinstall -y clickhouse-jdbc-bridge-$PKG_VER-1.noarch.rpm
           clickhouse-jdbc-bridge &

         Please refer to https://github.com/ClickHouse/clickhouse-jdbc-bridge#usage for more information.
    ]]>
    <!--
    <jdbc_bridge>
        <host>127.0.0.1</host>
        <port>9019</port>
    </jdbc_bridge>
    -->

    <!-- The list of hosts allowed to use in URL-related storage engines and table functions.
        If this section is not present in configuration, all hosts are allowed.
    -->
    <!--<remote_url_allow_hosts>-->
        <!-- Host should be specified exactly as in URL. The name is checked before DNS resolution.
            Example: "clickhouse.com", "clickhouse.com." and "www.clickhouse.com" are different hosts.
                    If port is explicitly specified in URL, the host:port is checked as a whole.
                    If host specified here without port, any port with this host allowed.
                    "clickhouse.com" -> "clickhouse.com:443", "clickhouse.com:80" etc. is allowed, but "clickhouse.com:80" -> only "clickhouse.com:80" is allowed.
            If the host is specified as IP address, it is checked as specified in URL. Example: "[2a02:6b8:a::a]".
            If there are redirects and support for redirects is enabled, every redirect (the Location field) is checked.
            Host should be specified using the host xml tag:
                    <host>clickhouse.com</host>
        -->

        <!-- Regular expression can be specified. RE2 engine is used for regexps.
            Regexps are not aligned: don't forget to add ^ and $. Also don't forget to escape dot (.) metacharacter
            (forgetting to do so is a common source of error).
        -->
    <!--</remote_url_allow_hosts>-->

    <!-- If element has 'incl' attribute, then for it's value will be used corresponding substitution from another file.
         By default, path to file with substitutions is /etc/metrika.xml. It could be changed in config in 'include_from' element.
         Values for substitutions are specified in /clickhouse/name_of_substitution elements in that file.
      -->

    <!-- Substitutions for parameters of replicated tables.
          Optional. If you don't use replicated tables, you could omit that.

         See https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/replication/#creating-replicated-tables
      -->

    <macros>
        <shard>01</shard>
        <replica>example01-01-1</replica>
    </macros>

    <!-- Reloading interval for embedded dictionaries, in seconds. Default: 3600. -->
    <builtin_dictionaries_reload_interval>3600</builtin_dictionaries_reload_interval>

    <!-- Maximum session timeout, in seconds. Default: 3600. -->
    <max_session_timeout>3600</max_session_timeout>

    <!-- Default session timeout, in seconds. Default: 60. -->
    <default_session_timeout>60</default_session_timeout>

    <!-- Sending data to Graphite for monitoring. Several sections can be defined. -->
    <!--
        interval - send every X second
        root_path - prefix for keys
        hostname_in_path - append hostname to root_path (default = true)
        metrics - send data from table system.metrics
        events - send data from table system.events
        asynchronous_metrics - send data from table system.asynchronous_metrics
    -->
    <!--
    <graphite>
        <host>localhost</host>
        <port>42000</port>
        <timeout>0.1</timeout>
        <interval>60</interval>
        <root_path>one_min</root_path>
        <hostname_in_path>true</hostname_in_path>

        <metrics>true</metrics>
        <events>true</events>
        <events_cumulative>false</events_cumulative>
        <asynchronous_metrics>true</asynchronous_metrics>
    </graphite>
    <graphite>
        <host>localhost</host>
        <port>42000</port>
        <timeout>0.1</timeout>
        <interval>1</interval>
        <root_path>one_sec</root_path>

        <metrics>true</metrics>
        <events>true</events>
        <events_cumulative>false</events_cumulative>
        <asynchronous_metrics>false</asynchronous_metrics>
    </graphite>
    -->

    <!-- Serve endpoint for Prometheus monitoring. -->
    <!--
        endpoint - mertics path (relative to root, statring with "/")
        port - port to setup server. If not defined or 0 than http_port used
        metrics - send data from table system.metrics
        events - send data from table system.events
        asynchronous_metrics - send data from table system.asynchronous_metrics
        status_info - send data from different component from CH, ex: Dictionaries status
    -->

    <prometheus>
        <endpoint>/metrics</endpoint>
        <port>9363</port>

        <metrics>true</metrics>
        <events>true</events>
        <asynchronous_metrics>true</asynchronous_metrics>
        <status_info>true</status_info>
    </prometheus>

    <!-- Query log. Used only for queries with setting log_queries = 1. -->
    <query_log>
        <!-- What table to insert data. If table is not exist, it will be created.
             When query log structure is changed after system update,
              then old table will be renamed and new table will be created automatically.
        -->
        <database>system</database>
        <table>query_log</table>
        <!--
            PARTITION BY expr: https://clickhouse.com/docs/en/table_engines/mergetree-family/custom_partitioning_key/
            Example:
                event_date
                toMonday(event_date)
                toYYYYMM(event_date)
                toStartOfHour(event_time)
        -->
        <partition_by>toYYYYMM(event_date)</partition_by>
        <!--
            Table TTL specification: https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/mergetree/#mergetree-table-ttl
            Example:
                event_date + INTERVAL 1 WEEK
                event_date + INTERVAL 7 DAY DELETE
                event_date + INTERVAL 2 WEEK TO DISK 'bbb'

        <ttl>event_date + INTERVAL 30 DAY DELETE</ttl>
        -->

        <!-- Instead of partition_by, you can provide full engine expression (starting with ENGINE = ) with parameters,
             Example: <engine>ENGINE = MergeTree PARTITION BY toYYYYMM(event_date) ORDER BY (event_date, event_time) SETTINGS index_granularity = 1024</engine>
          -->

        <!-- Interval of flushing data. -->
        <flush_interval_milliseconds>7500</flush_interval_milliseconds>
    </query_log>

    <!-- Trace log. Stores stack traces collected by query profilers.
         See query_profiler_real_time_period_ns and query_profiler_cpu_time_period_ns settings. -->
    <trace_log>
        <database>system</database>
        <table>trace_log</table>

        <partition_by>toYYYYMM(event_date)</partition_by>
        <flush_interval_milliseconds>7500</flush_interval_milliseconds>
    </trace_log>

    <!-- Query thread log. Has information about all threads participated in query execution.
         Used only for queries with setting log_query_threads = 1. -->
    <query_thread_log>
        <database>system</database>
        <table>query_thread_log</table>
        <partition_by>toYYYYMM(event_date)</partition_by>
        <flush_interval_milliseconds>7500</flush_interval_milliseconds>
    </query_thread_log>

    <!-- Query views log. Has information about all dependent views associated with a query.
         Used only for queries with setting log_query_views = 1. -->
    <query_views_log>
        <database>system</database>
        <table>query_views_log</table>
        <partition_by>toYYYYMM(event_date)</partition_by>
        <flush_interval_milliseconds>7500</flush_interval_milliseconds>
    </query_views_log>

    <!-- Uncomment if use part log.
         Part log contains information about all actions with parts in MergeTree tables (creation, deletion, merges, downloads).-->
    <part_log>
        <database>system</database>
        <table>part_log</table>
        <partition_by>toYYYYMM(event_date)</partition_by>
        <flush_interval_milliseconds>7500</flush_interval_milliseconds>
    </part_log>

    <!-- Uncomment to write text log into table.
         Text log contains all information from usual server log but stores it in structured and efficient way.
         The level of the messages that goes to the table can be limited (<level>), if not specified all messages will go to the table.
    <text_log>
        <database>system</database>
        <table>text_log</table>
        <flush_interval_milliseconds>7500</flush_interval_milliseconds>
        <level></level>
    </text_log>
    -->

    <!-- Metric log contains rows with current values of ProfileEvents, CurrentMetrics collected with "collect_interval_milliseconds" interval. -->
    <metric_log>
        <database>system</database>
        <table>metric_log</table>
        <flush_interval_milliseconds>7500</flush_interval_milliseconds>
        <collect_interval_milliseconds>1000</collect_interval_milliseconds>
    </metric_log>

    <!--
        Asynchronous metric log contains values of metrics from
        system.asynchronous_metrics.
    -->
    <asynchronous_metric_log>
        <database>system</database>
        <table>asynchronous_metric_log</table>
        <!--
            Asynchronous metrics are updated once a minute, so there is
            no need to flush more often.
        -->
        <flush_interval_milliseconds>7000</flush_interval_milliseconds>
    </asynchronous_metric_log>

    <!--
        OpenTelemetry log contains OpenTelemetry trace spans.
    -->
    <opentelemetry_span_log>
        <!--
            The default table creation code is insufficient, this <engine> spec
            is a workaround. There is no 'event_time' for this log, but two times,
            start and finish. It is sorted by finish time, to avoid inserting
            data too far away in the past (probably we can sometimes insert a span
            that is seconds earlier than the last span in the table, due to a race
            between several spans inserted in parallel). This gives the spans a
            global order that we can use to e.g. retry insertion into some external
            system.
        -->
        <engine>
            engine MergeTree
            partition by toYYYYMM(finish_date)
            order by (finish_date, finish_time_us, trace_id)
        </engine>
        <database>system</database>
        <table>opentelemetry_span_log</table>
        <flush_interval_milliseconds>7500</flush_interval_milliseconds>
    </opentelemetry_span_log>

    <!-- Crash log. Stores stack traces for fatal errors.
         This table is normally empty. -->
    <crash_log>
        <database>system</database>
        <table>crash_log</table>

        <partition_by />
        <flush_interval_milliseconds>1000</flush_interval_milliseconds>
    </crash_log>

    <!-- Session log. Stores user log in (successful or not) and log out events.

        Note: session log has known security issues and should not be used in production.
    -->
    <!-- <session_log>
        <database>system</database>
        <table>session_log</table>

        <partition_by>toYYYYMM(event_date)</partition_by>
        <flush_interval_milliseconds>7500</flush_interval_milliseconds>
    </session_log> -->

    <!-- Profiling on Processors level. -->
    <processors_profile_log>
        <database>system</database>
        <table>processors_profile_log</table>

        <partition_by>toYYYYMM(event_date)</partition_by>
        <flush_interval_milliseconds>7500</flush_interval_milliseconds>
    </processors_profile_log>

    <!-- <top_level_domains_path>/var/lib/clickhouse/top_level_domains/</top_level_domains_path> -->
    <!-- Custom TLD lists.
         Format: <name>/path/to/file</name>

         Changes will not be applied w/o server restart.
         Path to the list is under top_level_domains_path (see above).
    -->
    <top_level_domains_lists>
        <!--
        <public_suffix_list>/path/to/public_suffix_list.dat</public_suffix_list>
        -->
    </top_level_domains_lists>

    <!-- Configuration of external dictionaries. See:
         https://clickhouse.com/docs/en/sql-reference/dictionaries/external-dictionaries/external-dicts
    -->
    <dictionaries_config>*_dictionary.xml</dictionaries_config>

    <!-- Configuration of user defined executable functions -->
    <user_defined_executable_functions_config>*function.xml</user_defined_executable_functions_config>
    <user_scripts_path>/var/lib/clickhouse/user_scripts/</user_scripts_path>

    <!-- Uncomment if you want data to be compressed 30-100% better.
         Don't do that if you just started using ClickHouse.
      -->
    <!--
    <compression>
        <!- - Set of variants. Checked in order. Last matching case wins. If nothing matches, lz4 will be used. - ->
        <case>

            <!- - Conditions. All must be satisfied. Some conditions may be omitted. - ->
            <min_part_size>10000000000</min_part_size>        <!- - Min part size in bytes. - ->
            <min_part_size_ratio>0.01</min_part_size_ratio>   <!- - Min size of part relative to whole table size. - ->

            <!- - What compression method to use. - ->
            <method>zstd</method>
        </case>
    </compression>
    -->

    <!-- Configuration of encryption. The server executes a command to
         obtain an encryption key at startup if such a command is
         defined, or encryption codecs will be disabled otherwise. The
         command is executed through /bin/sh and is expected to write
         a Base64-encoded key to the stdout. -->
    <encryption_codecs>
        <!-- aes_128_gcm_siv -->
            <!-- Example of getting hex key from env -->
            <!-- the code should use this key and throw an exception if its length is not 16 bytes -->
            <!--key_hex from_env="..."></key_hex -->

            <!-- Example of multiple hex keys. They can be imported from env or be written down in config-->
            <!-- the code should use these keys and throw an exception if their length is not 16 bytes -->
            <!-- key_hex id="0">...</key_hex -->
            <!-- key_hex id="1" from_env=".."></key_hex -->
            <!-- key_hex id="2">...</key_hex -->
            <!-- current_key_id>2</current_key_id -->

            <!-- Example of getting hex key from config -->
            <!-- the code should use this key and throw an exception if its length is not 16 bytes -->
            <!-- key>...</key -->

            <!-- example of adding nonce -->
            <!-- nonce>...</nonce -->

        <!-- /aes_128_gcm_siv -->
    </encryption_codecs>

    <!-- Allow to execute distributed DDL queries (CREATE, DROP, ALTER, RENAME) on cluster.
         Works only if ZooKeeper is enabled. Comment it if such functionality isn't required. -->
    <distributed_ddl>
        <!-- Path in ZooKeeper to queue with DDL queries -->
        <path>/clickhouse/task_queue/ddl</path>

        <!-- Settings from this profile will be used to execute DDL queries -->
        <!-- <profile>default</profile> -->

        <!-- Controls how much ON CLUSTER queries can be run simultaneously. -->
        <!-- <pool_size>1</pool_size> -->

        <!--
             Cleanup settings (active tasks will not be removed)
        -->

        <!-- Controls task TTL (default 1 week) -->
        <!-- <task_max_lifetime>604800</task_max_lifetime> -->

        <!-- Controls how often cleanup should be performed (in seconds) -->
        <!-- <cleanup_delay_period>60</cleanup_delay_period> -->

        <!-- Controls how many tasks could be in the queue -->
        <!-- <max_tasks_in_queue>1000</max_tasks_in_queue> -->
    </distributed_ddl>

    <!-- Settings to fine tune MergeTree tables. See documentation in source code, in MergeTreeSettings.h -->
    <!--
    <merge_tree>
        <max_suspicious_broken_parts>5</max_suspicious_broken_parts>
    </merge_tree>
    -->

    <!-- Protection from accidental DROP.
         If size of a MergeTree table is greater than max_table_size_to_drop (in bytes) than table could not be dropped with any DROP query.
         If you want do delete one table and don't want to change clickhouse-server config, you could create special file <clickhouse-path>/flags/force_drop_table and make DROP once.
         By default max_table_size_to_drop is 50GB; max_table_size_to_drop=0 allows to DROP any tables.
         The same for max_partition_size_to_drop.
         Uncomment to disable protection.
    -->
    <!-- <max_table_size_to_drop>0</max_table_size_to_drop> -->
    <!-- <max_partition_size_to_drop>0</max_partition_size_to_drop> -->

    <!-- Example of parameters for GraphiteMergeTree table engine -->
    <graphite_rollup_example>
        <pattern>
            <regexp>click_cost</regexp>
            <function>any</function>
            <retention>
                <age>0</age>
                <precision>3600</precision>
            </retention>
            <retention>
                <age>86400</age>
                <precision>60</precision>
            </retention>
        </pattern>
        <default>
            <function>max</function>
            <retention>
                <age>0</age>
                <precision>60</precision>
            </retention>
            <retention>
                <age>3600</age>
                <precision>300</precision>
            </retention>
            <retention>
                <age>86400</age>
                <precision>3600</precision>
            </retention>
        </default>
    </graphite_rollup_example>

    <!-- Directory in <clickhouse-path> containing schema files for various input formats.
         The directory will be created if it doesn't exist.
      -->
    <format_schema_path>/var/lib/clickhouse/format_schemas/</format_schema_path>

    <!-- Default query masking rules, matching lines would be replaced with something else in the logs
        (both text logs and system.query_log).
        name - name for the rule (optional)
        regexp - RE2 compatible regular expression (mandatory)
        replace - substitution string for sensitive data (optional, by default - six asterisks)
    -->
    <query_masking_rules>
        <rule>
            <name>hide encrypt/decrypt arguments</name>
            <regexp>((?:aes_)?(?:encrypt|decrypt)(?:_mysql)?)\s*\(\s*(?:'(?:\\'|.)+'|.*?)\s*\)</regexp>
            <!-- or more secure, but also more invasive:
                (aes_\w+)\s*\(.*\)
            -->
            <replace>\1(???)</replace>
        </rule>
    </query_masking_rules>

    <!-- Uncomment to use custom http handlers.
        rules are checked from top to bottom, first match runs the handler
            url - to match request URL, you can use 'regex:' prefix to use regex match(optional)
            methods - to match request method, you can use commas to separate multiple method matches(optional)
            headers - to match request headers, match each child element(child element name is header name), you can use 'regex:' prefix to use regex match(optional)
        handler is request handler
            type - supported types: static, dynamic_query_handler, predefined_query_handler
            query - use with predefined_query_handler type, executes query when the handler is called
            query_param_name - use with dynamic_query_handler type, extracts and executes the value corresponding to the <query_param_name> value in HTTP request params
            status - use with static type, response status code
            content_type - use with static type, response content-type
            response_content - use with static type, Response content sent to client, when using the prefix 'file://' or 'config://', find the content from the file or configuration send to client.

    <http_handlers>
        <rule>
            <url>/</url>
            <methods>POST,GET</methods>
            <headers><pragma>no-cache</pragma></headers>
            <handler>
                <type>dynamic_query_handler</type>
                <query_param_name>query</query_param_name>
            </handler>
        </rule>

        <rule>
            <url>/predefined_query</url>
            <methods>POST,GET</methods>
            <handler>
                <type>predefined_query_handler</type>
                <query>SELECT * FROM system.settings</query>
            </handler>
        </rule>

        <rule>
            <handler>
                <type>static</type>
                <status>200</status>
                <content_type>text/plain; charset=UTF-8</content_type>
                <response_content>config://http_server_default_response</response_content>
            </handler>
        </rule>
    </http_handlers>
    -->

    <send_crash_reports>
        <!-- Changing <enabled> to true allows sending crash reports to -->
        <!-- the ClickHouse core developers team via Sentry https://sentry.io -->
        <!-- Doing so at least in pre-production environments is highly appreciated -->
        <enabled>false</enabled>
        <!-- Change <anonymize> to true if you don't feel comfortable attaching the server hostname to the crash report -->
        <anonymize>false</anonymize>
        <!-- Default endpoint should be changed to different Sentry DSN only if you have -->
        <!-- some in-house engineers or hired consultants who're going to debug ClickHouse issues for you -->
        <endpoint>https://[email protected]/5226277</endpoint>
    </send_crash_reports>

    <!-- Uncomment to disable ClickHouse internal DNS caching. -->
    <!-- <disable_internal_dns_cache>1</disable_internal_dns_cache> -->

    <!-- You can also configure rocksdb like this: -->
    <!--
    <rocksdb>
        <options>
            <max_background_jobs>8</max_background_jobs>
        </options>
        <column_family_options>
            <num_levels>2</num_levels>
        </column_family_options>
        <tables>
            <table>
                <name>TABLE</name>
                <options>
                    <max_background_jobs>8</max_background_jobs>
                </options>
                <column_family_options>
                    <num_levels>2</num_levels>
                </column_family_options>
            </table>
        </tables>
    </rocksdb>
    -->

    <!-- Uncomment if enable merge tree metadata cache -->
    <merge_tree_metadata_cache>
        <lru_cache_size>268435456</lru_cache_size>
        <continue_if_corrupted>true</continue_if_corrupted>
    </merge_tree_metadata_cache>
</clickhouse>
"""

[[config.mounts]]
filePath = "/clickhouse/cluster.xml"
content = """
<?xml version="1.0"?>
<clickhouse>
    <!-- ZooKeeper is used to store metadata about replicas, when using Replicated tables.
         Optional. If you don't use replicated tables, you could omit that.

         See https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/replication/
      -->
    <zookeeper>
        <node index="1">
            <host>zookeeper-1</host>
            <port>2181</port>
        </node>
        <!-- <node index="2">
            <host>zookeeper-2</host>
            <port>2181</port>
        </node>
        <node index="3">
            <host>zookeeper-3</host>
            <port>2181</port>
        </node> -->
    </zookeeper>

    <!-- Configuration of clusters that could be used in Distributed tables.
         https://clickhouse.com/docs/en/operations/table_engines/distributed/
      -->
    <remote_servers>
        <cluster>
            <!-- Inter-server per-cluster secret for Distributed queries
                 default: no secret (no authentication will be performed)

                 If set, then Distributed queries will be validated on shards, so at least:
                 - such cluster should exist on the shard,
                 - such cluster should have the same secret.

                 And also (and which is more important), the initial_user will
                 be used as current user for the query.

                 Right now the protocol is pretty simple and it only takes into account:
                 - cluster name
                 - query

                 Also it will be nice if the following will be implemented:
                 - source hostname (see interserver_http_host), but then it will depends from DNS,
                   it can use IP address instead, but then the you need to get correct on the initiator node.
                 - target hostname / ip address (same notes as for source hostname)
                 - time-based security tokens
            -->
            <!-- <secret></secret> -->
            <shard>
                <!-- Optional. Whether to write data to just one of the replicas. Default: false (write data to all replicas). -->
                <!-- <internal_replication>false</internal_replication> -->
                <!-- Optional. Shard weight when writing data. Default: 1. -->
                <!-- <weight>1</weight> -->
                <replica>
                    <host>clickhouse</host>
                    <port>9000</port>
                    <!-- Optional. Priority of the replica for load_balancing. Default: 1 (less value has more priority). -->
                    <!-- <priority>1</priority> -->
                </replica>
            </shard>
            <!-- <shard>
                <replica>
                    <host>clickhouse-2</host>
                    <port>9000</port>
                </replica>
            </shard>
            <shard>
                <replica>
                    <host>clickhouse-3</host>
                    <port>9000</port>
                </replica>
            </shard> -->
        </cluster>
    </remote_servers>
</clickhouse>
"""

[[config.mounts]]
filePath = "/signoz/prometheus.xml"
content = """
# my global config
global:
  scrape_interval:     5s # Set the scrape interval to every 15 seconds. Default is every 1 minute.
  evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.
  # scrape_timeout is set to the global default (10s).

# Alertmanager configuration
alerting:
  alertmanagers:
  - static_configs:
    - targets:
      - alertmanager:9093

# Load rules once and periodically evaluate them according to the global 'evaluation_interval'.
rule_files: []
  # - "first_rules.yml"
  # - "second_rules.yml"
  # - 'alerts.yml'

# A scrape configuration containing exactly one endpoint to scrape:
# Here it's Prometheus itself.
scrape_configs: []

remote_read:
  - url: tcp://clickhouse:9000/signoz_metrics
"""

[[config.mounts]]
filePath = "/collector/otel-collector-config.yaml"
content = """
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318
processors:
  batch:
exporters:
  clickhousetraces:
    datasource: tcp://clickhouse:9000/signoz_traces
    use_new_schema: true
  signozclickhousemetrics:
    dsn: tcp://clickhouse:9000/signoz_metrics
    timeout: 15s
  clickhouselogsexporter:
    dsn: tcp://clickhouse:9000/signoz_logs
    timeout: 10s
    use_new_schema: true
  metadataexporter:
    dsn: tcp://clickhouse:9000/signoz_metadata
    timeout: 10s
service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [clickhousetraces, metadataexporter]
    metrics:
      receivers: [otlp]
      processors: [batch]
      exporters: [signozclickhousemetrics, metadataexporter]
    logs:
      receivers: [otlp]
      processors: [batch]
      exporters: [clickhouselogsexporter, metadataexporter]
"""

[[config.mounts]]
filePath = "/clickhouse/user_scripts/empty.txt"
content = ""
```

https://docs.dokploy.com/cdn-cgi/l/email-protection https://docs.dokploy.com/cdn-cgi/l/email-protection

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIngtY29tbW9uOiAmY29tbW9uXG4gIG5ldHdvcmtzOlxuICAgIC0gc2lnbm96LW5ldFxuICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICBsb2dnaW5nOlxuICAgIG9wdGlvbnM6XG4gICAgICBtYXgtc2l6ZTogNTBtXG4gICAgICBtYXgtZmlsZTogXCIzXCJcbngtY2xpY2tob3VzZS1kZWZhdWx0czogJmNsaWNraG91c2UtZGVmYXVsdHNcbiAgISFtZXJnZSA8PDogKmNvbW1vblxuICBpbWFnZTogY2xpY2tob3VzZS9jbGlja2hvdXNlLXNlcnZlcjoyNS41LjZcbiAgdHR5OiB0cnVlXG4gIGxhYmVsczpcbiAgICBzaWdub3ouaW8vc2NyYXBlOiBcInRydWVcIlxuICAgIHNpZ25vei5pby9wb3J0OiBcIjkzNjNcIlxuICAgIHNpZ25vei5pby9wYXRoOiBcIi9tZXRyaWNzXCJcbiAgZGVwZW5kc19vbjpcbiAgICBpbml0LWNsaWNraG91c2U6XG4gICAgICBjb25kaXRpb246IHNlcnZpY2VfY29tcGxldGVkX3N1Y2Nlc3NmdWxseVxuICAgIHpvb2tlZXBlci0xOlxuICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcbiAgaGVhbHRoY2hlY2s6XG4gICAgdGVzdDpcbiAgICAgIC0gQ01EXG4gICAgICAtIHdnZXRcbiAgICAgIC0gLS1zcGlkZXJcbiAgICAgIC0gLXFcbiAgICAgIC0gMC4wLjAuMDo4MTIzL3BpbmdcbiAgICBpbnRlcnZhbDogMzBzXG4gICAgdGltZW91dDogNXNcbiAgICByZXRyaWVzOiAzXG4gIHVsaW1pdHM6XG4gICAgbnByb2M6IDY1NTM1XG4gICAgbm9maWxlOlxuICAgICAgc29mdDogMjYyMTQ0XG4gICAgICBoYXJkOiAyNjIxNDRcbiAgZW52aXJvbm1lbnQ6XG4gICAgLSBDTElDS0hPVVNFX1NLSVBfVVNFUl9TRVRVUD0xXG54LXpvb2tlZXBlci1kZWZhdWx0czogJnpvb2tlZXBlci1kZWZhdWx0c1xuICAhIW1lcmdlIDw8OiAqY29tbW9uXG4gIGltYWdlOiBzaWdub3ovem9va2VlcGVyOjMuNy4xXG4gIHVzZXI6IHJvb3RcbiAgbGFiZWxzOlxuICAgIHNpZ25vei5pby9zY3JhcGU6IFwidHJ1ZVwiXG4gICAgc2lnbm96LmlvL3BvcnQ6IFwiOTE0MVwiXG4gICAgc2lnbm96LmlvL3BhdGg6IFwiL21ldHJpY3NcIlxuICBoZWFsdGhjaGVjazpcbiAgICB0ZXN0OlxuICAgICAgLSBDTUQtU0hFTExcbiAgICAgIC0gY3VybCAtcyAtbSAyIGh0dHA6Ly9sb2NhbGhvc3Q6ODA4MC9jb21tYW5kcy9ydW9rIHwgZ3JlcCBlcnJvciB8IGdyZXAgbnVsbFxuICAgIGludGVydmFsOiAzMHNcbiAgICB0aW1lb3V0OiA1c1xuICAgIHJldHJpZXM6IDNcbngtZGItZGVwZW5kOiAmZGItZGVwZW5kXG4gICEhbWVyZ2UgPDw6ICpjb21tb25cbiAgZGVwZW5kc19vbjpcbiAgICBjbGlja2hvdXNlOlxuICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcbiAgICBzY2hlbWEtbWlncmF0b3Itc3luYzpcbiAgICAgIGNvbmRpdGlvbjogc2VydmljZV9jb21wbGV0ZWRfc3VjY2Vzc2Z1bGx5XG5zZXJ2aWNlczpcbiAgaW5pdC1jbGlja2hvdXNlOlxuICAgICEhbWVyZ2UgPDw6ICpjb21tb25cbiAgICBpbWFnZTogY2xpY2tob3VzZS9jbGlja2hvdXNlLXNlcnZlcjoyNS41LjZcbiAgICBjb21tYW5kOlxuICAgICAgLSBiYXNoXG4gICAgICAtIC1jXG4gICAgICAtIHxcbiAgICAgICAgdmVyc2lvbj1cInYwLjAuMVwiXG4gICAgICAgIG5vZGVfb3M9JCQodW5hbWUgLXMgfCB0ciAnWzp1cHBlcjpdJyAnWzpsb3dlcjpdJylcbiAgICAgICAgbm9kZV9hcmNoPSQkKHVuYW1lIC1tIHwgc2VkIHMvYWFyY2g2NC9hcm02NC8gfCBzZWQgcy94ODZfNjQvYW1kNjQvKVxuICAgICAgICBlY2hvIFwiRmV0Y2hpbmcgaGlzdG9ncmFtLWJpbmFyeSBmb3IgJCR7bm9kZV9vc30vJCR7bm9kZV9hcmNofVwiXG4gICAgICAgIGNkIC90bXBcbiAgICAgICAgd2dldCAtTyBoaXN0b2dyYW0tcXVhbnRpbGUudGFyLmd6IFwiaHR0cHM6Ly9naXRodWIuY29tL1NpZ05vei9zaWdub3ovcmVsZWFzZXMvZG93bmxvYWQvaGlzdG9ncmFtLXF1YW50aWxlJTJGJCR7dmVyc2lvbn0vaGlzdG9ncmFtLXF1YW50aWxlXyQke25vZGVfb3N9XyQke25vZGVfYXJjaH0udGFyLmd6XCJcbiAgICAgICAgdGFyIC14dnpmIGhpc3RvZ3JhbS1xdWFudGlsZS50YXIuZ3pcbiAgICAgICAgbXYgaGlzdG9ncmFtLXF1YW50aWxlIC92YXIvbGliL2NsaWNraG91c2UvdXNlcl9zY3JpcHRzL2hpc3RvZ3JhbVF1YW50aWxlXG4gICAgcmVzdGFydDogb24tZmFpbHVyZVxuICAgIHZvbHVtZXM6XG4gICAgICAtIC4uL2ZpbGVzL2NsaWNraG91c2UvdXNlcl9zY3JpcHRzOi92YXIvbGliL2NsaWNraG91c2UvdXNlcl9zY3JpcHRzL1xuICB6b29rZWVwZXItMTpcbiAgICAhIW1lcmdlIDw8OiAqem9va2VlcGVyLWRlZmF1bHRzXG4gICAgdm9sdW1lczpcbiAgICAgIC0gem9va2VlcGVyLTE6L2JpdG5hbWkvem9va2VlcGVyXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFpPT19TRVJWRVJfSUQ9MVxuICAgICAgLSBBTExPV19BTk9OWU1PVVNfTE9HSU49eWVzXG4gICAgICAtIFpPT19BVVRPUFVSR0VfSU5URVJWQUw9MVxuICAgICAgLSBaT09fRU5BQkxFX1BST01FVEhFVVNfTUVUUklDUz15ZXNcbiAgICAgIC0gWk9PX1BST01FVEhFVVNfTUVUUklDU19QT1JUX05VTUJFUj05MTQxXG4gIGNsaWNraG91c2U6XG4gICAgISFtZXJnZSA8PDogKmNsaWNraG91c2UtZGVmYXVsdHNcbiAgICBjb250YWluZXJfbmFtZTogc2lnbm96LWNsaWNraG91c2VcbiAgICB2b2x1bWVzOlxuICAgICAgLSAuLi9maWxlcy9jbGlja2hvdXNlL2NvbmZpZy54bWw6L2V0Yy9jbGlja2hvdXNlLXNlcnZlci9jb25maWcueG1sXG4gICAgICAtIC4uL2ZpbGVzL2NsaWNraG91c2UvdXNlcl9zY3JpcHRzOi92YXIvbGliL2NsaWNraG91c2UvdXNlcl9zY3JpcHRzL1xuICAgICAgLSAuLi9maWxlcy9jbGlja2hvdXNlL2NsdXN0ZXIueG1sOi9ldGMvY2xpY2tob3VzZS1zZXJ2ZXIvY29uZmlnLmQvY2x1c3Rlci54bWxcbiAgICAgIC0gY2xpY2tob3VzZTovdmFyL2xpYi9jbGlja2hvdXNlL1xuICBzaWdub3o6XG4gICAgISFtZXJnZSA8PDogKmRiLWRlcGVuZFxuICAgIGltYWdlOiBzaWdub3ovc2lnbm96OnYwLjk3LjFcbiAgICBjb21tYW5kOlxuICAgICAgLSAtLWNvbmZpZz0vcm9vdC9jb25maWcvcHJvbWV0aGV1cy55bWxcbiAgICBwb3J0czpcbiAgICAgIC0gXCI4MDgwXCJcbiAgICB2b2x1bWVzOlxuICAgICAgLSAuLi9maWxlcy9zaWdub3ovcHJvbWV0aGV1cy55bWw6L3Jvb3QvY29uZmlnL3Byb21ldGhldXMueW1sXG4gICAgICAtIHNxbGl0ZTovdmFyL2xpYi9zaWdub3ovXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFNJR05PWl9BTEVSVE1BTkFHRVJfUFJPVklERVI9c2lnbm96XG4gICAgICAtIFNJR05PWl9URUxFTUVUUllTVE9SRV9DTElDS0hPVVNFX0RTTj10Y3A6Ly9jbGlja2hvdXNlOjkwMDBcbiAgICAgIC0gU0lHTk9aX1NRTFNUT1JFX1NRTElURV9QQVRIPS92YXIvbGliL3NpZ25vei9zaWdub3ouZGJcbiAgICAgIC0gU1RPUkFHRT1jbGlja2hvdXNlXG4gICAgICAtIFRFTEVNRVRSWV9FTkFCTEVEPXRydWVcbiAgICAgIC0gREVQTE9ZTUVOVF9UWVBFPWRvY2tlci1zdGFuZGFsb25lLWFtZFxuICAgICAgLSBET1RfTUVUUklDU19FTkFCTEVEPXRydWVcbiAgICAgIC0gU0lHTk9aX0pXVF9TRUNSRVQ9JHtTSUdOT1pfSldUX1NFQ1JFVH1cbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6XG4gICAgICAgIC0gQ01EXG4gICAgICAgIC0gd2dldFxuICAgICAgICAtIC0tc3BpZGVyXG4gICAgICAgIC0gLXFcbiAgICAgICAgLSBsb2NhbGhvc3Q6ODA4MC9hcGkvdjEvaGVhbHRoXG4gICAgICBpbnRlcnZhbDogMzBzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogM1xuICBvdGVsLWNvbGxlY3RvcjpcbiAgICAhIW1lcmdlIDw8OiAqZGItZGVwZW5kXG4gICAgaW1hZ2U6IHNpZ25vei9zaWdub3otb3RlbC1jb2xsZWN0b3I6djAuMTI5LjdcbiAgICBjb21tYW5kOlxuICAgICAgLSAtLWNvbmZpZz0vZXRjL290ZWwtY29sbGVjdG9yLWNvbmZpZy55YW1sXG4gICAgdm9sdW1lczpcbiAgICAgIC0gLi4vZmlsZXMvY29sbGVjdG9yL290ZWwtY29sbGVjdG9yLWNvbmZpZy55YW1sOi9ldGMvb3RlbC1jb2xsZWN0b3ItY29uZmlnLnlhbWxcbiAgICBwb3J0czpcbiAgICAgIC0gXCI0MzE3XCIgIyBPVExQIGdSUEMgcmVjZWl2ZXJcbiAgICAgIC0gXCI0MzE4XCIgIyBPVExQIEhUVFAgcmVjZWl2ZXJcbiAgICBkZXBlbmRzX29uOlxuICAgICAgc2lnbm96OlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICBzY2hlbWEtbWlncmF0b3Itc3luYzpcbiAgICAhIW1lcmdlIDw8OiAqY29tbW9uXG4gICAgaW1hZ2U6IHNpZ25vei9zaWdub3otc2NoZW1hLW1pZ3JhdG9yOnYwLjEyOS43XG4gICAgY29tbWFuZDpcbiAgICAgIC0gc3luY1xuICAgICAgLSAtLWRzbj10Y3A6Ly9jbGlja2hvdXNlOjkwMDBcbiAgICAgIC0gLS11cD1cbiAgICBkZXBlbmRzX29uOlxuICAgICAgY2xpY2tob3VzZTpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcbiAgICByZXN0YXJ0OiBvbi1mYWlsdXJlXG4gIHNjaGVtYS1taWdyYXRvci1hc3luYzpcbiAgICAhIW1lcmdlIDw8OiAqZGItZGVwZW5kXG4gICAgaW1hZ2U6IHNpZ25vei9zaWdub3otc2NoZW1hLW1pZ3JhdG9yOnYwLjEyOS43XG4gICAgY29tbWFuZDpcbiAgICAgIC0gYXN5bmNcbiAgICAgIC0gLS1kc249dGNwOi8vY2xpY2tob3VzZTo5MDAwXG4gICAgICAtIC0tdXA9XG4gICAgcmVzdGFydDogb24tZmFpbHVyZVxubmV0d29ya3M6XG4gIHNpZ25vei1uZXQ6XG4gICAgbmFtZTogc2lnbm96LW5ldFxudm9sdW1lczpcbiAgY2xpY2tob3VzZTpcbiAgICBuYW1lOiBzaWdub3otY2xpY2tob3VzZVxuICBzcWxpdGU6XG4gICAgbmFtZTogc2lnbm96LXNxbGl0ZVxuICB6b29rZWVwZXItMTpcbiAgICBuYW1lOiBzaWdub3otem9va2VlcGVyLTFcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5qd3Rfc2VjcmV0ID0gXCIke3Bhc3N3b3JkOjY0fVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJzaWdub3pcIlxucG9ydCA9IDgwODBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcbnBhdGggPSBcIi9cIlxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJvdGVsLWNvbGxlY3RvclwiXG5wb3J0ID0gNDMxOFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxucGF0aCA9IFwiL1wiXG5cbltjb25maWcuZW52XVxuU0lHTk9aX0pXVF9TRUNSRVQgPSBcIiR7and0X3NlY3JldH1cIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuZmlsZVBhdGggPSBcIi9jbGlja2hvdXNlL2NvbmZpZy54bWxcIlxuY29udGVudCA9IFwiXCJcIlxuPD94bWwgdmVyc2lvbj1cIjEuMFwiPz5cbjwhLS1cbiAgTk9URTogVXNlciBhbmQgcXVlcnkgbGV2ZWwgc2V0dGluZ3MgYXJlIHNldCB1cCBpbiBcInVzZXJzLnhtbFwiIGZpbGUuXG4gIElmIHlvdSBoYXZlIGFjY2lkZW50YWxseSBzcGVjaWZpZWQgdXNlci1sZXZlbCBzZXR0aW5ncyBoZXJlLCBzZXJ2ZXIgd29uJ3Qgc3RhcnQuXG4gIFlvdSBjYW4gZWl0aGVyIG1vdmUgdGhlIHNldHRpbmdzIHRvIHRoZSByaWdodCBwbGFjZSBpbnNpZGUgXCJ1c2Vycy54bWxcIiBmaWxlXG4gICBvciBhZGQgPHNraXBfY2hlY2tfZm9yX2luY29ycmVjdF9zZXR0aW5ncz4xPC9za2lwX2NoZWNrX2Zvcl9pbmNvcnJlY3Rfc2V0dGluZ3M+IGhlcmUuXG4tLT5cbjxjbGlja2hvdXNlPlxuICAgIDxsb2dnZXI+XG4gICAgICAgIDwhLS0gUG9zc2libGUgbGV2ZWxzIFsxXTpcblxuICAgICAgICAgIC0gbm9uZSAodHVybnMgb2ZmIGxvZ2dpbmcpXG4gICAgICAgICAgLSBmYXRhbFxuICAgICAgICAgIC0gY3JpdGljYWxcbiAgICAgICAgICAtIGVycm9yXG4gICAgICAgICAgLSB3YXJuaW5nXG4gICAgICAgICAgLSBub3RpY2VcbiAgICAgICAgICAtIGluZm9ybWF0aW9uXG4gICAgICAgICAgLSBkZWJ1Z1xuICAgICAgICAgIC0gdHJhY2VcbiAgICAgICAgICAtIHRlc3QgKG5vdCBmb3IgcHJvZHVjdGlvbiB1c2FnZSlcblxuICAgICAgICAgICAgWzFdOiBodHRwczovL2dpdGh1Yi5jb20vcG9jb3Byb2plY3QvcG9jby9ibG9iL3BvY28tMS45LjQtcmVsZWFzZS9Gb3VuZGF0aW9uL2luY2x1ZGUvUG9jby9Mb2dnZXIuaCNMMTA1LUwxMTRcbiAgICAgICAgLS0+XG4gICAgICAgIDxsZXZlbD5pbmZvcm1hdGlvbjwvbGV2ZWw+XG4gICAgICAgIDxmb3JtYXR0aW5nPlxuICAgICAgICAgICAgPHR5cGU+anNvbjwvdHlwZT5cbiAgICAgICAgPC9mb3JtYXR0aW5nPlxuICAgICAgICA8bG9nPi92YXIvbG9nL2NsaWNraG91c2Utc2VydmVyL2NsaWNraG91c2Utc2VydmVyLmxvZzwvbG9nPlxuICAgICAgICA8ZXJyb3Jsb2c+L3Zhci9sb2cvY2xpY2tob3VzZS1zZXJ2ZXIvY2xpY2tob3VzZS1zZXJ2ZXIuZXJyLmxvZzwvZXJyb3Jsb2c+XG4gICAgICAgIDwhLS0gUm90YXRpb24gcG9saWN5XG4gICAgICAgICAgICAgU2VlIGh0dHBzOi8vZ2l0aHViLmNvbS9wb2NvcHJvamVjdC9wb2NvL2Jsb2IvcG9jby0xLjkuNC1yZWxlYXNlL0ZvdW5kYXRpb24vaW5jbHVkZS9Qb2NvL0ZpbGVDaGFubmVsLmgjTDU0LUw4NVxuICAgICAgICAgIC0tPlxuICAgICAgICA8c2l6ZT4xMDAwTTwvc2l6ZT5cbiAgICAgICAgPGNvdW50PjEwPC9jb3VudD5cbiAgICAgICAgPCEtLSA8Y29uc29sZT4xPC9jb25zb2xlPiAtLT4gPCEtLSBEZWZhdWx0IGJlaGF2aW9yIGlzIGF1dG9kZXRlY3Rpb24gKGxvZyB0byBjb25zb2xlIGlmIG5vdCBkYWVtb24gbW9kZSBhbmQgaXMgdHR5KSAtLT5cblxuICAgICAgICA8IS0tIFBlciBsZXZlbCBvdmVycmlkZXMgKGxlZ2FjeSk6XG5cbiAgICAgICAgRm9yIGV4YW1wbGUgdG8gc3VwcHJlc3MgbG9nZ2luZyBvZiB0aGUgQ29uZmlnUmVsb2FkZXIgeW91IGNhbiB1c2U6XG4gICAgICAgIE5PVEU6IGxldmVscy5sb2dnZXIgaXMgcmVzZXJ2ZWQsIHNlZSBiZWxvdy5cbiAgICAgICAgLS0+XG4gICAgICAgIDwhLS1cbiAgICAgICAgPGxldmVscz5cbiAgICAgICAgICA8Q29uZmlnUmVsb2FkZXI+bm9uZTwvQ29uZmlnUmVsb2FkZXI+XG4gICAgICAgIDwvbGV2ZWxzPlxuICAgICAgICAtLT5cblxuICAgICAgICA8IS0tIFBlciBsZXZlbCBvdmVycmlkZXM6XG5cbiAgICAgICAgRm9yIGV4YW1wbGUgdG8gc3VwcHJlc3MgbG9nZ2luZyBvZiB0aGUgUkJBQyBmb3IgZGVmYXVsdCB1c2VyIHlvdSBjYW4gdXNlOlxuICAgICAgICAoQnV0IHBsZWFzZSBub3RlIHRoYXQgdGhlIGxvZ2dlciBuYW1lIG1heWJlIGNoYW5nZWQgZnJvbSB2ZXJzaW9uIHRvIHZlcnNpb24sIGV2ZW4gYWZ0ZXIgbWlub3IgdXBncmFkZSlcbiAgICAgICAgLS0+XG4gICAgICAgIDwhLS1cbiAgICAgICAgPGxldmVscz5cbiAgICAgICAgICA8bG9nZ2VyPlxuICAgICAgICAgICAgPG5hbWU+Q29udGV4dEFjY2VzcyAoZGVmYXVsdCk8L25hbWU+XG4gICAgICAgICAgICA8bGV2ZWw+bm9uZTwvbGV2ZWw+XG4gICAgICAgICAgPC9sb2dnZXI+XG4gICAgICAgICAgPGxvZ2dlcj5cbiAgICAgICAgICAgIDxuYW1lPkRhdGFiYXNlT3JkaW5hcnkgKHRlc3QpPC9uYW1lPlxuICAgICAgICAgICAgPGxldmVsPm5vbmU8L2xldmVsPlxuICAgICAgICAgIDwvbG9nZ2VyPlxuICAgICAgICA8L2xldmVscz5cbiAgICAgICAgLS0+XG4gICAgPC9sb2dnZXI+XG5cbiAgICA8IS0tIEFkZCBoZWFkZXJzIHRvIHJlc3BvbnNlIGluIG9wdGlvbnMgcmVxdWVzdC4gT1BUSU9OUyBtZXRob2QgaXMgdXNlZCBpbiBDT1JTIHByZWZsaWdodCByZXF1ZXN0cy4gLS0+XG4gICAgPCEtLSBJdCBpcyBvZmYgYnkgZGVmYXVsdC4gTmV4dCBoZWFkZXJzIGFyZSBvYmxpZ2F0ZSBmb3IgQ09SUy4tLT5cbiAgICA8IS0tIGh0dHBfb3B0aW9uc19yZXNwb25zZT5cbiAgICAgICAgPGhlYWRlcj5cbiAgICAgICAgICAgIDxuYW1lPkFjY2Vzcy1Db250cm9sLUFsbG93LU9yaWdpbjwvbmFtZT5cbiAgICAgICAgICAgIDx2YWx1ZT4qPC92YWx1ZT5cbiAgICAgICAgPC9oZWFkZXI+XG4gICAgICAgIDxoZWFkZXI+XG4gICAgICAgICAgICA8bmFtZT5BY2Nlc3MtQ29udHJvbC1BbGxvdy1IZWFkZXJzPC9uYW1lPlxuICAgICAgICAgICAgPHZhbHVlPm9yaWdpbiwgeC1yZXF1ZXN0ZWQtd2l0aDwvdmFsdWU+XG4gICAgICAgIDwvaGVhZGVyPlxuICAgICAgICA8aGVhZGVyPlxuICAgICAgICAgICAgPG5hbWU+QWNjZXNzLUNvbnRyb2wtQWxsb3ctTWV0aG9kczwvbmFtZT5cbiAgICAgICAgICAgIDx2YWx1ZT5QT1NULCBHRVQsIE9QVElPTlM8L3ZhbHVlPlxuICAgICAgICA8L2hlYWRlcj5cbiAgICAgICAgPGhlYWRlcj5cbiAgICAgICAgICAgIDxuYW1lPkFjY2Vzcy1Db250cm9sLU1heC1BZ2U8L25hbWU+XG4gICAgICAgICAgICA8dmFsdWU+ODY0MDA8L3ZhbHVlPlxuICAgICAgICA8L2hlYWRlcj5cbiAgICA8L2h0dHBfb3B0aW9uc19yZXNwb25zZSAtLT5cblxuICAgIDwhLS0gSXQgaXMgdGhlIG5hbWUgdGhhdCB3aWxsIGJlIHNob3duIGluIHRoZSBjbGlja2hvdXNlLWNsaWVudC5cbiAgICAgICAgIEJ5IGRlZmF1bHQsIGFueXRoaW5nIHdpdGggXCJwcm9kdWN0aW9uXCIgd2lsbCBiZSBoaWdobGlnaHRlZCBpbiByZWQgaW4gcXVlcnkgcHJvbXB0LlxuICAgIC0tPlxuICAgIDwhLS1kaXNwbGF5X25hbWU+cHJvZHVjdGlvbjwvZGlzcGxheV9uYW1lLS0+XG5cbiAgICA8IS0tIFBvcnQgZm9yIEhUVFAgQVBJLiBTZWUgYWxzbyAnaHR0cHNfcG9ydCcgZm9yIHNlY3VyZSBjb25uZWN0aW9ucy5cbiAgICAgICAgIFRoaXMgaW50ZXJmYWNlIGlzIGFsc28gdXNlZCBieSBPREJDIGFuZCBKREJDIGRyaXZlcnMgKERhdGFHcmlwLCBEYmVhdmVyLCAuLi4pXG4gICAgICAgICBhbmQgYnkgbW9zdCBvZiB3ZWIgaW50ZXJmYWNlcyAoZW1iZWRkZWQgVUksIEdyYWZhbmEsIFJlZGFzaCwgLi4uKS5cbiAgICAgIC0tPlxuICAgIDxodHRwX3BvcnQ+ODEyMzwvaHR0cF9wb3J0PlxuXG4gICAgPCEtLSBQb3J0IGZvciBpbnRlcmFjdGlvbiBieSBuYXRpdmUgcHJvdG9jb2wgd2l0aDpcbiAgICAgICAgIC0gY2xpY2tob3VzZS1jbGllbnQgYW5kIG90aGVyIG5hdGl2ZSBDbGlja0hvdXNlIHRvb2xzIChjbGlja2hvdXNlLWJlbmNobWFyaywgY2xpY2tob3VzZS1jb3BpZXIpO1xuICAgICAgICAgLSBjbGlja2hvdXNlLXNlcnZlciB3aXRoIG90aGVyIGNsaWNraG91c2Utc2VydmVycyBmb3IgZGlzdHJpYnV0ZWQgcXVlcnkgcHJvY2Vzc2luZztcbiAgICAgICAgIC0gQ2xpY2tIb3VzZSBkcml2ZXJzIGFuZCBhcHBsaWNhdGlvbnMgc3VwcG9ydGluZyBuYXRpdmUgcHJvdG9jb2xcbiAgICAgICAgICh0aGlzIHByb3RvY29sIGlzIGFsc28gaW5mb3JtYWxseSBjYWxsZWQgYXMgXCJ0aGUgVENQIHByb3RvY29sXCIpO1xuICAgICAgICAgU2VlIGFsc28gJ3RjcF9wb3J0X3NlY3VyZScgZm9yIHNlY3VyZSBjb25uZWN0aW9ucy5cbiAgICAtLT5cbiAgICA8dGNwX3BvcnQ+OTAwMDwvdGNwX3BvcnQ+XG5cbiAgICA8IS0tIENvbXBhdGliaWxpdHkgd2l0aCBNeVNRTCBwcm90b2NvbC5cbiAgICAgICAgIENsaWNrSG91c2Ugd2lsbCBwcmV0ZW5kIHRvIGJlIE15U1FMIGZvciBhcHBsaWNhdGlvbnMgY29ubmVjdGluZyB0byB0aGlzIHBvcnQuXG4gICAgLS0+XG4gICAgPG15c3FsX3BvcnQ+OTAwNDwvbXlzcWxfcG9ydD5cblxuICAgIDwhLS0gQ29tcGF0aWJpbGl0eSB3aXRoIFBvc3RncmVTUUwgcHJvdG9jb2wuXG4gICAgICAgICBDbGlja0hvdXNlIHdpbGwgcHJldGVuZCB0byBiZSBQb3N0Z3JlU1FMIGZvciBhcHBsaWNhdGlvbnMgY29ubmVjdGluZyB0byB0aGlzIHBvcnQuXG4gICAgLS0+XG4gICAgPHBvc3RncmVzcWxfcG9ydD45MDA1PC9wb3N0Z3Jlc3FsX3BvcnQ+XG5cbiAgICA8IS0tIEhUVFAgQVBJIHdpdGggVExTIChIVFRQUykuXG4gICAgICAgICBZb3UgaGF2ZSB0byBjb25maWd1cmUgY2VydGlmaWNhdGUgdG8gZW5hYmxlIHRoaXMgaW50ZXJmYWNlLlxuICAgICAgICAgU2VlIHRoZSBvcGVuU1NMIHNlY3Rpb24gYmVsb3cuXG4gICAgLS0+XG4gICAgPCEtLSA8aHR0cHNfcG9ydD44NDQzPC9odHRwc19wb3J0PiAtLT5cblxuICAgIDwhLS0gTmF0aXZlIGludGVyZmFjZSB3aXRoIFRMUy5cbiAgICAgICAgIFlvdSBoYXZlIHRvIGNvbmZpZ3VyZSBjZXJ0aWZpY2F0ZSB0byBlbmFibGUgdGhpcyBpbnRlcmZhY2UuXG4gICAgICAgICBTZWUgdGhlIG9wZW5TU0wgc2VjdGlvbiBiZWxvdy5cbiAgICAtLT5cbiAgICA8IS0tIDx0Y3BfcG9ydF9zZWN1cmU+OTQ0MDwvdGNwX3BvcnRfc2VjdXJlPiAtLT5cblxuICAgIDwhLS0gTmF0aXZlIGludGVyZmFjZSB3cmFwcGVkIHdpdGggUFJPWFl2MSBwcm90b2NvbFxuICAgICAgICAgUFJPWFl2MSBoZWFkZXIgc2VudCBmb3IgZXZlcnkgY29ubmVjdGlvbi5cbiAgICAgICAgIENsaWNrSG91c2Ugd2lsbCBleHRyYWN0IGluZm9ybWF0aW9uIGFib3V0IHByb3h5LWZvcndhcmRlZCBjbGllbnQgYWRkcmVzcyBmcm9tIHRoZSBoZWFkZXIuXG4gICAgLS0+XG4gICAgPCEtLSA8dGNwX3dpdGhfcHJveHlfcG9ydD45MDExPC90Y3Bfd2l0aF9wcm94eV9wb3J0PiAtLT5cblxuICAgIDwhLS0gUG9ydCBmb3IgY29tbXVuaWNhdGlvbiBiZXR3ZWVuIHJlcGxpY2FzLiBVc2VkIGZvciBkYXRhIGV4Y2hhbmdlLlxuICAgICAgICAgSXQgcHJvdmlkZXMgbG93LWxldmVsIGRhdGEgYWNjZXNzIGJldHdlZW4gc2VydmVycy5cbiAgICAgICAgIFRoaXMgcG9ydCBzaG91bGQgbm90IGJlIGFjY2Vzc2libGUgZnJvbSB1bnRydXN0ZWQgbmV0d29ya3MuXG4gICAgICAgICBTZWUgYWxzbyAnaW50ZXJzZXJ2ZXJfaHR0cF9jcmVkZW50aWFscycuXG4gICAgICAgICBEYXRhIHRyYW5zZmVycmVkIG92ZXIgY29ubmVjdGlvbnMgdG8gdGhpcyBwb3J0IHNob3VsZCBub3QgZ28gdGhyb3VnaCB1bnRydXN0ZWQgbmV0d29ya3MuXG4gICAgICAgICBTZWUgYWxzbyAnaW50ZXJzZXJ2ZXJfaHR0cHNfcG9ydCcuXG4gICAgICAtLT5cbiAgICA8aW50ZXJzZXJ2ZXJfaHR0cF9wb3J0PjkwMDk8L2ludGVyc2VydmVyX2h0dHBfcG9ydD5cblxuICAgIDwhLS0gUG9ydCBmb3IgY29tbXVuaWNhdGlvbiBiZXR3ZWVuIHJlcGxpY2FzIHdpdGggVExTLlxuICAgICAgICAgWW91IGhhdmUgdG8gY29uZmlndXJlIGNlcnRpZmljYXRlIHRvIGVuYWJsZSB0aGlzIGludGVyZmFjZS5cbiAgICAgICAgIFNlZSB0aGUgb3BlblNTTCBzZWN0aW9uIGJlbG93LlxuICAgICAgICAgU2VlIGFsc28gJ2ludGVyc2VydmVyX2h0dHBfY3JlZGVudGlhbHMnLlxuICAgICAgLS0+XG4gICAgPCEtLSA8aW50ZXJzZXJ2ZXJfaHR0cHNfcG9ydD45MDEwPC9pbnRlcnNlcnZlcl9odHRwc19wb3J0PiAtLT5cblxuICAgIDwhLS0gSG9zdG5hbWUgdGhhdCBpcyB1c2VkIGJ5IG90aGVyIHJlcGxpY2FzIHRvIHJlcXVlc3QgdGhpcyBzZXJ2ZXIuXG4gICAgICAgICBJZiBub3Qgc3BlY2lmaWVkLCB0aGVuIGl0IGlzIGRldGVybWluZWQgYW5hbG9nb3VzIHRvICdob3N0bmFtZSAtZicgY29tbWFuZC5cbiAgICAgICAgIFRoaXMgc2V0dGluZyBjb3VsZCBiZSB1c2VkIHRvIHN3aXRjaCByZXBsaWNhdGlvbiB0byBhbm90aGVyIG5ldHdvcmsgaW50ZXJmYWNlXG4gICAgICAgICAodGhlIHNlcnZlciBtYXkgYmUgY29ubmVjdGVkIHRvIG11bHRpcGxlIG5ldHdvcmtzIHZpYSBtdWx0aXBsZSBhZGRyZXNzZXMpXG4gICAgICAtLT5cblxuICAgIDwhLS1cbiAgICA8aW50ZXJzZXJ2ZXJfaHR0cF9ob3N0PmV4YW1wbGUuY2xpY2tob3VzZS5jb208L2ludGVyc2VydmVyX2h0dHBfaG9zdD5cbiAgICAtLT5cblxuICAgIDwhLS0gWW91IGNhbiBzcGVjaWZ5IGNyZWRlbnRpYWxzIGZvciBhdXRoZW50aGljYXRpb24gYmV0d2VlbiByZXBsaWNhcy5cbiAgICAgICAgIFRoaXMgaXMgcmVxdWlyZWQgd2hlbiBpbnRlcnNlcnZlcl9odHRwc19wb3J0IGlzIGFjY2Vzc2libGUgZnJvbSB1bnRydXN0ZWQgbmV0d29ya3MsXG4gICAgICAgICBhbmQgYWxzbyByZWNvbW1lbmRlZCB0byBhdm9pZCBTU1JGIGF0dGFja3MgZnJvbSBwb3NzaWJseSBjb21wcm9taXNlZCBzZXJ2aWNlcyBpbiB5b3VyIG5ldHdvcmsuXG4gICAgICAtLT5cbiAgICA8IS0tPGludGVyc2VydmVyX2h0dHBfY3JlZGVudGlhbHM+XG4gICAgICAgIDx1c2VyPmludGVyc2VydmVyPC91c2VyPlxuICAgICAgICA8cGFzc3dvcmQ+PC9wYXNzd29yZD5cbiAgICA8L2ludGVyc2VydmVyX2h0dHBfY3JlZGVudGlhbHM+LS0+XG5cbiAgICA8IS0tIExpc3RlbiBzcGVjaWZpZWQgYWRkcmVzcy5cbiAgICAgICAgIFVzZSA6OiAod2lsZGNhcmQgSVB2NiBhZGRyZXNzKSwgaWYgeW91IHdhbnQgdG8gYWNjZXB0IGNvbm5lY3Rpb25zIGJvdGggd2l0aCBJUHY0IGFuZCBJUHY2IGZyb20gZXZlcnl3aGVyZS5cbiAgICAgICAgIE5vdGVzOlxuICAgICAgICAgSWYgeW91IG9wZW4gY29ubmVjdGlvbnMgZnJvbSB3aWxkY2FyZCBhZGRyZXNzLCBtYWtlIHN1cmUgdGhhdCBhdCBsZWFzdCBvbmUgb2YgdGhlIGZvbGxvd2luZyBtZWFzdXJlcyBhcHBsaWVkOlxuICAgICAgICAgLSBzZXJ2ZXIgaXMgcHJvdGVjdGVkIGJ5IGZpcmV3YWxsIGFuZCBub3QgYWNjZXNzaWJsZSBmcm9tIHVudHJ1c3RlZCBuZXR3b3JrcztcbiAgICAgICAgIC0gYWxsIHVzZXJzIGFyZSByZXN0cmljdGVkIHRvIHN1YnNldCBvZiBuZXR3b3JrIGFkZHJlc3NlcyAoc2VlIHVzZXJzLnhtbCk7XG4gICAgICAgICAtIGFsbCB1c2VycyBoYXZlIHN0cm9uZyBwYXNzd29yZHMsIG9ubHkgc2VjdXJlIChUTFMpIGludGVyZmFjZXMgYXJlIGFjY2Vzc2libGUsIG9yIGNvbm5lY3Rpb25zIGFyZSBvbmx5IG1hZGUgdmlhIFRMUyBpbnRlcmZhY2VzLlxuICAgICAgICAgLSB1c2VycyB3aXRob3V0IHBhc3N3b3JkIGhhdmUgcmVhZG9ubHkgYWNjZXNzLlxuICAgICAgICAgU2VlIGFsc286IGh0dHBzOi8vd3d3LnNob2Rhbi5pby9zZWFyY2g/cXVlcnk9Y2xpY2tob3VzZVxuICAgICAgLS0+XG4gICAgPCEtLSA8bGlzdGVuX2hvc3Q+Ojo8L2xpc3Rlbl9ob3N0PiAtLT5cblxuXG4gICAgPCEtLSBTYW1lIGZvciBob3N0cyB3aXRob3V0IHN1cHBvcnQgZm9yIElQdjY6IC0tPlxuICAgIDwhLS0gPGxpc3Rlbl9ob3N0PjAuMC4wLjA8L2xpc3Rlbl9ob3N0PiAtLT5cblxuICAgIDwhLS0gRGVmYXVsdCB2YWx1ZXMgLSB0cnkgbGlzdGVuIGxvY2FsaG9zdCBvbiBJUHY0IGFuZCBJUHY2LiAtLT5cbiAgICA8IS0tXG4gICAgPGxpc3Rlbl9ob3N0Pjo6MTwvbGlzdGVuX2hvc3Q+XG4gICAgPGxpc3Rlbl9ob3N0PjEyNy4wLjAuMTwvbGlzdGVuX2hvc3Q+XG4gICAgLS0+XG5cbiAgICA8IS0tIERvbid0IGV4aXQgaWYgSVB2NiBvciBJUHY0IG5ldHdvcmtzIGFyZSB1bmF2YWlsYWJsZSB3aGlsZSB0cnlpbmcgdG8gbGlzdGVuLiAtLT5cbiAgICA8IS0tIDxsaXN0ZW5fdHJ5PjA8L2xpc3Rlbl90cnk+IC0tPlxuXG4gICAgPCEtLSBBbGxvdyBtdWx0aXBsZSBzZXJ2ZXJzIHRvIGxpc3RlbiBvbiB0aGUgc2FtZSBhZGRyZXNzOnBvcnQuIFRoaXMgaXMgbm90IHJlY29tbWVuZGVkLlxuICAgICAgLS0+XG4gICAgPCEtLSA8bGlzdGVuX3JldXNlX3BvcnQ+MDwvbGlzdGVuX3JldXNlX3BvcnQ+IC0tPlxuXG4gICAgPCEtLSA8bGlzdGVuX2JhY2tsb2c+NDA5NjwvbGlzdGVuX2JhY2tsb2c+IC0tPlxuXG4gICAgPG1heF9jb25uZWN0aW9ucz40MDk2PC9tYXhfY29ubmVjdGlvbnM+XG5cbiAgICA8IS0tIEZvciAnQ29ubmVjdGlvbjoga2VlcC1hbGl2ZScgaW4gSFRUUCAxLjEgLS0+XG4gICAgPGtlZXBfYWxpdmVfdGltZW91dD4zPC9rZWVwX2FsaXZlX3RpbWVvdXQ+XG5cbiAgICA8IS0tIGdSUEMgcHJvdG9jb2wgKHNlZSBzcmMvU2VydmVyL2dycGNfcHJvdG9zL2NsaWNraG91c2VfZ3JwYy5wcm90byBmb3IgdGhlIEFQSSkgLS0+XG4gICAgPCEtLSA8Z3JwY19wb3J0PjkxMDA8L2dycGNfcG9ydD4gLS0+XG4gICAgPGdycGM+XG4gICAgICAgIDxlbmFibGVfc3NsPmZhbHNlPC9lbmFibGVfc3NsPlxuXG4gICAgICAgIDwhLS0gVGhlIGZvbGxvd2luZyB0d28gZmlsZXMgYXJlIHVzZWQgb25seSBpZiBlbmFibGVfc3NsPTEgLS0+XG4gICAgICAgIDxzc2xfY2VydF9maWxlPi9wYXRoL3RvL3NzbF9jZXJ0X2ZpbGU8L3NzbF9jZXJ0X2ZpbGU+XG4gICAgICAgIDxzc2xfa2V5X2ZpbGU+L3BhdGgvdG8vc3NsX2tleV9maWxlPC9zc2xfa2V5X2ZpbGU+XG5cbiAgICAgICAgPCEtLSBXaGV0aGVyIHNlcnZlciB3aWxsIHJlcXVlc3QgY2xpZW50IGZvciBhIGNlcnRpZmljYXRlIC0tPlxuICAgICAgICA8c3NsX3JlcXVpcmVfY2xpZW50X2F1dGg+ZmFsc2U8L3NzbF9yZXF1aXJlX2NsaWVudF9hdXRoPlxuXG4gICAgICAgIDwhLS0gVGhlIGZvbGxvd2luZyBmaWxlIGlzIHVzZWQgb25seSBpZiBzc2xfcmVxdWlyZV9jbGllbnRfYXV0aD0xIC0tPlxuICAgICAgICA8c3NsX2NhX2NlcnRfZmlsZT4vcGF0aC90by9zc2xfY2FfY2VydF9maWxlPC9zc2xfY2FfY2VydF9maWxlPlxuXG4gICAgICAgIDwhLS0gRGVmYXVsdCB0cmFuc3BvcnQgY29tcHJlc3Npb24gdHlwZSAoY2FuIGJlIG92ZXJyaWRkZW4gYnkgY2xpZW50LCBzZWUgdGhlIHRyYW5zcG9ydF9jb21wcmVzc2lvbl90eXBlIGZpZWxkIGluIFF1ZXJ5SW5mbykuXG4gICAgICAgICAgICAgU3VwcG9ydGVkIGFsZ29yaXRobXM6IG5vbmUsIGRlZmxhdGUsIGd6aXAsIHN0cmVhbV9nemlwIC0tPlxuICAgICAgICA8dHJhbnNwb3J0X2NvbXByZXNzaW9uX3R5cGU+bm9uZTwvdHJhbnNwb3J0X2NvbXByZXNzaW9uX3R5cGU+XG5cbiAgICAgICAgPCEtLSBEZWZhdWx0IHRyYW5zcG9ydCBjb21wcmVzc2lvbiBsZXZlbC4gU3VwcG9ydGVkIGxldmVsczogMC4uMyAtLT5cbiAgICAgICAgPHRyYW5zcG9ydF9jb21wcmVzc2lvbl9sZXZlbD4wPC90cmFuc3BvcnRfY29tcHJlc3Npb25fbGV2ZWw+XG5cbiAgICAgICAgPCEtLSBTZW5kL3JlY2VpdmUgbWVzc2FnZSBzaXplIGxpbWl0cyBpbiBieXRlcy4gLTEgbWVhbnMgdW5saW1pdGVkIC0tPlxuICAgICAgICA8bWF4X3NlbmRfbWVzc2FnZV9zaXplPi0xPC9tYXhfc2VuZF9tZXNzYWdlX3NpemU+XG4gICAgICAgIDxtYXhfcmVjZWl2ZV9tZXNzYWdlX3NpemU+LTE8L21heF9yZWNlaXZlX21lc3NhZ2Vfc2l6ZT5cblxuICAgICAgICA8IS0tIEVuYWJsZSBpZiB5b3Ugd2FudCB2ZXJ5IGRldGFpbGVkIGxvZ3MgLS0+XG4gICAgICAgIDx2ZXJib3NlX2xvZ3M+ZmFsc2U8L3ZlcmJvc2VfbG9ncz5cbiAgICA8L2dycGM+XG5cbiAgICA8IS0tIFVzZWQgd2l0aCBodHRwc19wb3J0IGFuZCB0Y3BfcG9ydF9zZWN1cmUuIEZ1bGwgc3NsIG9wdGlvbnMgbGlzdDogaHR0cHM6Ly9naXRodWIuY29tL0NsaWNrSG91c2UtRXh0cmFzL3BvY28vYmxvYi9tYXN0ZXIvTmV0U1NMX09wZW5TU0wvaW5jbHVkZS9Qb2NvL05ldC9TU0xNYW5hZ2VyLmgjTDcxIC0tPlxuICAgIDxvcGVuU1NMPlxuICAgICAgICA8c2VydmVyPiA8IS0tIFVzZWQgZm9yIGh0dHBzIHNlcnZlciBBTkQgc2VjdXJlIHRjcCBwb3J0IC0tPlxuICAgICAgICAgICAgPCEtLSBvcGVuc3NsIHJlcSAtc3ViaiBcIi9DTj1sb2NhbGhvc3RcIiAtbmV3IC1uZXdrZXkgcnNhOjIwNDggLWRheXMgMzY1IC1ub2RlcyAteDUwOSAta2V5b3V0IC9ldGMvY2xpY2tob3VzZS1zZXJ2ZXIvc2VydmVyLmtleSAtb3V0IC9ldGMvY2xpY2tob3VzZS1zZXJ2ZXIvc2VydmVyLmNydCAtLT5cbiAgICAgICAgICAgIDwhLS0gPGNlcnRpZmljYXRlRmlsZT4vZXRjL2NsaWNraG91c2Utc2VydmVyL3NlcnZlci5jcnQ8L2NlcnRpZmljYXRlRmlsZT4gLS0+XG4gICAgICAgICAgICA8IS0tIDxwcml2YXRlS2V5RmlsZT4vZXRjL2NsaWNraG91c2Utc2VydmVyL3NlcnZlci5rZXk8L3ByaXZhdGVLZXlGaWxlPiAtLT5cbiAgICAgICAgICAgIDwhLS0gZGhwYXJhbXMgYXJlIG9wdGlvbmFsLiBZb3UgY2FuIGRlbGV0ZSB0aGUgPGRoUGFyYW1zRmlsZT4gZWxlbWVudC5cbiAgICAgICAgICAgICAgICAgVG8gZ2VuZXJhdGUgZGhwYXJhbXMsIHVzZSB0aGUgZm9sbG93aW5nIGNvbW1hbmQ6XG4gICAgICAgICAgICAgICAgICBvcGVuc3NsIGRocGFyYW0gLW91dCAvZXRjL2NsaWNraG91c2Utc2VydmVyL2RocGFyYW0ucGVtIDQwOTZcbiAgICAgICAgICAgICAgICAgT25seSBmaWxlIGZvcm1hdCB3aXRoIEJFR0lOIERIIFBBUkFNRVRFUlMgaXMgc3VwcG9ydGVkLlxuICAgICAgICAgICAgICAtLT5cbiAgICAgICAgICAgIDwhLS0gPGRoUGFyYW1zRmlsZT4vZXRjL2NsaWNraG91c2Utc2VydmVyL2RocGFyYW0ucGVtPC9kaFBhcmFtc0ZpbGU+LS0+XG4gICAgICAgICAgICA8dmVyaWZpY2F0aW9uTW9kZT5ub25lPC92ZXJpZmljYXRpb25Nb2RlPlxuICAgICAgICAgICAgPGxvYWREZWZhdWx0Q0FGaWxlPnRydWU8L2xvYWREZWZhdWx0Q0FGaWxlPlxuICAgICAgICAgICAgPGNhY2hlU2Vzc2lvbnM+dHJ1ZTwvY2FjaGVTZXNzaW9ucz5cbiAgICAgICAgICAgIDxkaXNhYmxlUHJvdG9jb2xzPnNzbHYyLHNzbHYzPC9kaXNhYmxlUHJvdG9jb2xzPlxuICAgICAgICAgICAgPHByZWZlclNlcnZlckNpcGhlcnM+dHJ1ZTwvcHJlZmVyU2VydmVyQ2lwaGVycz5cbiAgICAgICAgPC9zZXJ2ZXI+XG5cbiAgICAgICAgPGNsaWVudD4gPCEtLSBVc2VkIGZvciBjb25uZWN0aW5nIHRvIGh0dHBzIGRpY3Rpb25hcnkgc291cmNlIGFuZCBzZWN1cmVkIFpvb2tlZXBlciBjb21tdW5pY2F0aW9uIC0tPlxuICAgICAgICAgICAgPGxvYWREZWZhdWx0Q0FGaWxlPnRydWU8L2xvYWREZWZhdWx0Q0FGaWxlPlxuICAgICAgICAgICAgPGNhY2hlU2Vzc2lvbnM+dHJ1ZTwvY2FjaGVTZXNzaW9ucz5cbiAgICAgICAgICAgIDxkaXNhYmxlUHJvdG9jb2xzPnNzbHYyLHNzbHYzPC9kaXNhYmxlUHJvdG9jb2xzPlxuICAgICAgICAgICAgPHByZWZlclNlcnZlckNpcGhlcnM+dHJ1ZTwvcHJlZmVyU2VydmVyQ2lwaGVycz5cbiAgICAgICAgICAgIDwhLS0gVXNlIGZvciBzZWxmLXNpZ25lZDogPHZlcmlmaWNhdGlvbk1vZGU+bm9uZTwvdmVyaWZpY2F0aW9uTW9kZT4gLS0+XG4gICAgICAgICAgICA8aW52YWxpZENlcnRpZmljYXRlSGFuZGxlcj5cbiAgICAgICAgICAgICAgICA8IS0tIFVzZSBmb3Igc2VsZi1zaWduZWQ6IDxuYW1lPkFjY2VwdENlcnRpZmljYXRlSGFuZGxlcjwvbmFtZT4gLS0+XG4gICAgICAgICAgICAgICAgPG5hbWU+UmVqZWN0Q2VydGlmaWNhdGVIYW5kbGVyPC9uYW1lPlxuICAgICAgICAgICAgPC9pbnZhbGlkQ2VydGlmaWNhdGVIYW5kbGVyPlxuICAgICAgICA8L2NsaWVudD5cbiAgICA8L29wZW5TU0w+XG5cbiAgICA8IS0tIERlZmF1bHQgcm9vdCBwYWdlIG9uIGh0dHBbc10gc2VydmVyLiBGb3IgZXhhbXBsZSBsb2FkIFVJIGZyb20gaHR0cHM6Ly90YWJpeC5pby8gd2hlbiBvcGVuaW5nIGh0dHA6Ly9sb2NhbGhvc3Q6ODEyMyAtLT5cbiAgICA8IS0tXG4gICAgPGh0dHBfc2VydmVyX2RlZmF1bHRfcmVzcG9uc2U+PCFbQ0RBVEFbPGh0bWwgbmctYXBwPVwiU01JMlwiPjxoZWFkPjxiYXNlIGhyZWY9XCJodHRwOi8vdWkudGFiaXguaW8vXCI+PC9oZWFkPjxib2R5PjxkaXYgdWktdmlldz1cIlwiIGNsYXNzPVwiY29udGVudC11aVwiPjwvZGl2PjxzY3JpcHQgc3JjPVwiaHR0cDovL2xvYWRlci50YWJpeC5pby9tYXN0ZXIuanNcIj48L3NjcmlwdD48L2JvZHk+PC9odG1sPl1dPjwvaHR0cF9zZXJ2ZXJfZGVmYXVsdF9yZXNwb25zZT5cbiAgICAtLT5cblxuICAgIDwhLS0gTWF4aW11bSBudW1iZXIgb2YgY29uY3VycmVudCBxdWVyaWVzLiAtLT5cbiAgICA8bWF4X2NvbmN1cnJlbnRfcXVlcmllcz4xMDA8L21heF9jb25jdXJyZW50X3F1ZXJpZXM+XG5cbiAgICA8IS0tIE1heGltdW0gbWVtb3J5IHVzYWdlIChyZXNpZGVudCBzZXQgc2l6ZSkgZm9yIHNlcnZlciBwcm9jZXNzLlxuICAgICAgICAgWmVybyB2YWx1ZSBvciB1bnNldCBtZWFucyBkZWZhdWx0LiBEZWZhdWx0IGlzIFwibWF4X3NlcnZlcl9tZW1vcnlfdXNhZ2VfdG9fcmFtX3JhdGlvXCIgb2YgYXZhaWxhYmxlIHBoeXNpY2FsIFJBTS5cbiAgICAgICAgIElmIHRoZSB2YWx1ZSBpcyBsYXJnZXIgdGhhbiBcIm1heF9zZXJ2ZXJfbWVtb3J5X3VzYWdlX3RvX3JhbV9yYXRpb1wiIG9mIGF2YWlsYWJsZSBwaHlzaWNhbCBSQU0sIGl0IHdpbGwgYmUgY3V0IGRvd24uXG5cbiAgICAgICAgIFRoZSBjb25zdHJhaW50IGlzIGNoZWNrZWQgb24gcXVlcnkgZXhlY3V0aW9uIHRpbWUuXG4gICAgICAgICBJZiBhIHF1ZXJ5IHRyaWVzIHRvIGFsbG9jYXRlIG1lbW9yeSBhbmQgdGhlIGN1cnJlbnQgbWVtb3J5IHVzYWdlIHBsdXMgYWxsb2NhdGlvbiBpcyBncmVhdGVyXG4gICAgICAgICAgdGhhbiBzcGVjaWZpZWQgdGhyZXNob2xkLCBleGNlcHRpb24gd2lsbCBiZSB0aHJvd24uXG5cbiAgICAgICAgIEl0IGlzIG5vdCBwcmFjdGljYWwgdG8gc2V0IHRoaXMgY29uc3RyYWludCB0byBzbWFsbCB2YWx1ZXMgbGlrZSBqdXN0IGEgZmV3IGdpZ2FieXRlcyxcbiAgICAgICAgICBiZWNhdXNlIG1lbW9yeSBhbGxvY2F0b3Igd2lsbCBrZWVwIHRoaXMgYW1vdW50IG9mIG1lbW9yeSBpbiBjYWNoZXMgYW5kIHRoZSBzZXJ2ZXIgd2lsbCBkZW55IHNlcnZpY2Ugb2YgcXVlcmllcy5cbiAgICAgIC0tPlxuICAgIDxtYXhfc2VydmVyX21lbW9yeV91c2FnZT4wPC9tYXhfc2VydmVyX21lbW9yeV91c2FnZT5cblxuICAgIDwhLS0gTWF4aW11bSBudW1iZXIgb2YgdGhyZWFkcyBpbiB0aGUgR2xvYmFsIHRocmVhZCBwb29sLlxuICAgIFRoaXMgd2lsbCBkZWZhdWx0IHRvIGEgbWF4aW11bSBvZiAxMDAwMCB0aHJlYWRzIGlmIG5vdCBzcGVjaWZpZWQuXG4gICAgVGhpcyBzZXR0aW5nIHdpbGwgYmUgdXNlZnVsIGluIHNjZW5hcmlvcyB3aGVyZSB0aGVyZSBhcmUgYSBsYXJnZSBudW1iZXJcbiAgICBvZiBkaXN0cmlidXRlZCBxdWVyaWVzIHRoYXQgYXJlIHJ1bm5pbmcgY29uY3VycmVudGx5IGJ1dCBhcmUgaWRsaW5nIG1vc3RcbiAgICBvZiB0aGUgdGltZSwgaW4gd2hpY2ggY2FzZSBhIGhpZ2hlciBudW1iZXIgb2YgdGhyZWFkcyBtaWdodCBiZSByZXF1aXJlZC5cbiAgICAtLT5cblxuICAgIDxtYXhfdGhyZWFkX3Bvb2xfc2l6ZT4xMDAwMDwvbWF4X3RocmVhZF9wb29sX3NpemU+XG5cbiAgICA8IS0tIE51bWJlciBvZiB3b3JrZXJzIHRvIHJlY3ljbGUgY29ubmVjdGlvbnMgaW4gYmFja2dyb3VuZCAoc2VlIGFsc28gZHJhaW5fdGltZW91dCkuXG4gICAgICAgICBJZiB0aGUgcG9vbCBpcyBmdWxsLCBjb25uZWN0aW9uIHdpbGwgYmUgZHJhaW5lZCBzeW5jaHJvbm91c2x5LiAtLT5cbiAgICA8IS0tIDxtYXhfdGhyZWFkc19mb3JfY29ubmVjdGlvbl9jb2xsZWN0b3I+MTA8L21heF90aHJlYWRzX2Zvcl9jb25uZWN0aW9uX2NvbGxlY3Rvcj4gLS0+XG5cbiAgICA8IS0tIE9uIG1lbW9yeSBjb25zdHJhaW5lZCBlbnZpcm9ubWVudHMgeW91IG1heSBoYXZlIHRvIHNldCB0aGlzIHRvIHZhbHVlIGxhcmdlciB0aGFuIDEuXG4gICAgICAtLT5cbiAgICA8bWF4X3NlcnZlcl9tZW1vcnlfdXNhZ2VfdG9fcmFtX3JhdGlvPjAuOTwvbWF4X3NlcnZlcl9tZW1vcnlfdXNhZ2VfdG9fcmFtX3JhdGlvPlxuXG4gICAgPCEtLSBTaW1wbGUgc2VydmVyLXdpZGUgbWVtb3J5IHByb2ZpbGVyLiBDb2xsZWN0IGEgc3RhY2sgdHJhY2UgYXQgZXZlcnkgcGVhayBhbGxvY2F0aW9uIHN0ZXAgKGluIGJ5dGVzKS5cbiAgICAgICAgIERhdGEgd2lsbCBiZSBzdG9yZWQgaW4gc3lzdGVtLnRyYWNlX2xvZyB0YWJsZSB3aXRoIHF1ZXJ5X2lkID0gZW1wdHkgc3RyaW5nLlxuICAgICAgICAgWmVybyBtZWFucyBkaXNhYmxlZC5cbiAgICAgIC0tPlxuICAgIDx0b3RhbF9tZW1vcnlfcHJvZmlsZXJfc3RlcD40MTk0MzA0PC90b3RhbF9tZW1vcnlfcHJvZmlsZXJfc3RlcD5cblxuICAgIDwhLS0gQ29sbGVjdCByYW5kb20gYWxsb2NhdGlvbnMgYW5kIGRlYWxsb2NhdGlvbnMgYW5kIHdyaXRlIHRoZW0gaW50byBzeXN0ZW0udHJhY2VfbG9nIHdpdGggJ01lbW9yeVNhbXBsZScgdHJhY2VfdHlwZS5cbiAgICAgICAgIFRoZSBwcm9iYWJpbGl0eSBpcyBmb3IgZXZlcnkgYWxsb2MvZnJlZSByZWdhcmRsZXNzIHRvIHRoZSBzaXplIG9mIHRoZSBhbGxvY2F0aW9uLlxuICAgICAgICAgTm90ZSB0aGF0IHNhbXBsaW5nIGhhcHBlbnMgb25seSB3aGVuIHRoZSBhbW91bnQgb2YgdW50cmFja2VkIG1lbW9yeSBleGNlZWRzIHRoZSB1bnRyYWNrZWQgbWVtb3J5IGxpbWl0LFxuICAgICAgICAgIHdoaWNoIGlzIDQgTWlCIGJ5IGRlZmF1bHQgYnV0IGNhbiBiZSBsb3dlcmVkIGlmICd0b3RhbF9tZW1vcnlfcHJvZmlsZXJfc3RlcCcgaXMgbG93ZXJlZC5cbiAgICAgICAgIFlvdSBtYXkgd2FudCB0byBzZXQgJ3RvdGFsX21lbW9yeV9wcm9maWxlcl9zdGVwJyB0byAxIGZvciBleHRyYSBmaW5lIGdyYWluZWQgc2FtcGxpbmcuXG4gICAgICAtLT5cbiAgICA8dG90YWxfbWVtb3J5X3RyYWNrZXJfc2FtcGxlX3Byb2JhYmlsaXR5PjA8L3RvdGFsX21lbW9yeV90cmFja2VyX3NhbXBsZV9wcm9iYWJpbGl0eT5cblxuICAgIDwhLS0gU2V0IGxpbWl0IG9uIG51bWJlciBvZiBvcGVuIGZpbGVzIChkZWZhdWx0OiBtYXhpbXVtKS4gVGhpcyBzZXR0aW5nIG1ha2VzIHNlbnNlIG9uIE1hYyBPUyBYIGJlY2F1c2UgZ2V0cmxpbWl0KCkgZmFpbHMgdG8gcmV0cmlldmVcbiAgICAgICAgIGNvcnJlY3QgbWF4aW11bSB2YWx1ZS4gLS0+XG4gICAgPCEtLSA8bWF4X29wZW5fZmlsZXM+MjYyMTQ0PC9tYXhfb3Blbl9maWxlcz4gLS0+XG5cbiAgICA8IS0tIFNpemUgb2YgY2FjaGUgb2YgdW5jb21wcmVzc2VkIGJsb2NrcyBvZiBkYXRhLCB1c2VkIGluIHRhYmxlcyBvZiBNZXJnZVRyZWUgZmFtaWx5LlxuICAgICAgICAgSW4gYnl0ZXMuIENhY2hlIGlzIHNpbmdsZSBmb3Igc2VydmVyLiBNZW1vcnkgaXMgYWxsb2NhdGVkIG9ubHkgb24gZGVtYW5kLlxuICAgICAgICAgQ2FjaGUgaXMgdXNlZCB3aGVuICd1c2VfdW5jb21wcmVzc2VkX2NhY2hlJyB1c2VyIHNldHRpbmcgdHVybmVkIG9uIChvZmYgYnkgZGVmYXVsdCkuXG4gICAgICAgICBVbmNvbXByZXNzZWQgY2FjaGUgaXMgYWR2YW50YWdlb3VzIG9ubHkgZm9yIHZlcnkgc2hvcnQgcXVlcmllcyBhbmQgaW4gcmFyZSBjYXNlcy5cblxuICAgICAgICAgTm90ZTogdW5jb21wcmVzc2VkIGNhY2hlIGNhbiBiZSBwb2ludGxlc3MgZm9yIGx6NCwgYmVjYXVzZSBtZW1vcnkgYmFuZHdpZHRoXG4gICAgICAgICBpcyBzbG93ZXIgdGhhbiBtdWx0aS1jb3JlIGRlY29tcHJlc3Npb24gb24gc29tZSBzZXJ2ZXIgY29uZmlndXJhdGlvbnMuXG4gICAgICAgICBFbmFibGluZyBpdCBjYW4gc29tZXRpbWVzIHBhcmFkb3hpY2FsbHkgbWFrZSBxdWVyaWVzIHNsb3dlci5cbiAgICAgIC0tPlxuICAgIDx1bmNvbXByZXNzZWRfY2FjaGVfc2l6ZT44NTg5OTM0NTkyPC91bmNvbXByZXNzZWRfY2FjaGVfc2l6ZT5cblxuICAgIDwhLS0gQXBwcm94aW1hdGUgc2l6ZSBvZiBtYXJrIGNhY2hlLCB1c2VkIGluIHRhYmxlcyBvZiBNZXJnZVRyZWUgZmFtaWx5LlxuICAgICAgICAgSW4gYnl0ZXMuIENhY2hlIGlzIHNpbmdsZSBmb3Igc2VydmVyLiBNZW1vcnkgaXMgYWxsb2NhdGVkIG9ubHkgb24gZGVtYW5kLlxuICAgICAgICAgWW91IHNob3VsZCBub3QgbG93ZXIgdGhpcyB2YWx1ZS5cbiAgICAgIC0tPlxuICAgIDxtYXJrX2NhY2hlX3NpemU+NTM2ODcwOTEyMDwvbWFya19jYWNoZV9zaXplPlxuXG5cbiAgICA8IS0tIElmIHlvdSBlbmFibGUgdGhlIGBtaW5fYnl0ZXNfdG9fdXNlX21tYXBfaW9gIHNldHRpbmcsXG4gICAgICAgICB0aGUgZGF0YSBpbiBNZXJnZVRyZWUgdGFibGVzIGNhbiBiZSByZWFkIHdpdGggbW1hcCB0byBhdm9pZCBjb3B5aW5nIGZyb20ga2VybmVsIHRvIHVzZXJzcGFjZS5cbiAgICAgICAgIEl0IG1ha2VzIHNlbnNlIG9ubHkgZm9yIGxhcmdlIGZpbGVzIGFuZCBoZWxwcyBvbmx5IGlmIGRhdGEgcmVzaWRlIGluIHBhZ2UgY2FjaGUuXG4gICAgICAgICBUbyBhdm9pZCBmcmVxdWVudCBvcGVuL21tYXAvbXVubWFwL2Nsb3NlIGNhbGxzICh3aGljaCBhcmUgdmVyeSBleHBlbnNpdmUgZHVlIHRvIGNvbnNlcXVlbnQgcGFnZSBmYXVsdHMpXG4gICAgICAgICBhbmQgdG8gcmV1c2UgbWFwcGluZ3MgZnJvbSBzZXZlcmFsIHRocmVhZHMgYW5kIHF1ZXJpZXMsXG4gICAgICAgICB0aGUgY2FjaGUgb2YgbWFwcGVkIGZpbGVzIGlzIG1haW50YWluZWQuIEl0cyBzaXplIGlzIHRoZSBudW1iZXIgb2YgbWFwcGVkIHJlZ2lvbnMgKHVzdWFsbHkgZXF1YWwgdG8gdGhlIG51bWJlciBvZiBtYXBwZWQgZmlsZXMpLlxuICAgICAgICAgVGhlIGFtb3VudCBvZiBkYXRhIGluIG1hcHBlZCBmaWxlcyBjYW4gYmUgbW9uaXRvcmVkXG4gICAgICAgICBpbiBzeXN0ZW0ubWV0cmljcywgc3lzdGVtLm1ldHJpY19sb2cgYnkgdGhlIE1NYXBwZWRGaWxlcywgTU1hcHBlZEZpbGVCeXRlcyBtZXRyaWNzXG4gICAgICAgICBhbmQgaW4gc3lzdGVtLmFzeW5jaHJvbm91c19tZXRyaWNzLCBzeXN0ZW0uYXN5bmNocm9ub3VzX21ldHJpY3NfbG9nIGJ5IHRoZSBNTWFwQ2FjaGVDZWxscyBtZXRyaWMsXG4gICAgICAgICBhbmQgYWxzbyBpbiBzeXN0ZW0uZXZlbnRzLCBzeXN0ZW0ucHJvY2Vzc2VzLCBzeXN0ZW0ucXVlcnlfbG9nLCBzeXN0ZW0ucXVlcnlfdGhyZWFkX2xvZywgc3lzdGVtLnF1ZXJ5X3ZpZXdzX2xvZyBieSB0aGVcbiAgICAgICAgIENyZWF0ZWRSZWFkQnVmZmVyTU1hcCwgQ3JlYXRlZFJlYWRCdWZmZXJNTWFwRmFpbGVkLCBNTWFwcGVkRmlsZUNhY2hlSGl0cywgTU1hcHBlZEZpbGVDYWNoZU1pc3NlcyBldmVudHMuXG4gICAgICAgICBOb3RlIHRoYXQgdGhlIGFtb3VudCBvZiBkYXRhIGluIG1hcHBlZCBmaWxlcyBkb2VzIG5vdCBjb25zdW1lIG1lbW9yeSBkaXJlY3RseSBhbmQgaXMgbm90IGFjY291bnRlZFxuICAgICAgICAgaW4gcXVlcnkgb3Igc2VydmVyIG1lbW9yeSB1c2FnZSAtIGJlY2F1c2UgdGhpcyBtZW1vcnkgY2FuIGJlIGRpc2NhcmRlZCBzaW1pbGFyIHRvIE9TIHBhZ2UgY2FjaGUuXG4gICAgICAgICBUaGUgY2FjaGUgaXMgZHJvcHBlZCAodGhlIGZpbGVzIGFyZSBjbG9zZWQpIGF1dG9tYXRpY2FsbHkgb24gcmVtb3ZhbCBvZiBvbGQgcGFydHMgaW4gTWVyZ2VUcmVlLFxuICAgICAgICAgYWxzbyBpdCBjYW4gYmUgZHJvcHBlZCBtYW51YWxseSBieSB0aGUgU1lTVEVNIERST1AgTU1BUCBDQUNIRSBxdWVyeS5cbiAgICAgIC0tPlxuICAgIDxtbWFwX2NhY2hlX3NpemU+MTAwMDwvbW1hcF9jYWNoZV9zaXplPlxuXG4gICAgPCEtLSBDYWNoZSBzaXplIGluIGJ5dGVzIGZvciBjb21waWxlZCBleHByZXNzaW9ucy4tLT5cbiAgICA8Y29tcGlsZWRfZXhwcmVzc2lvbl9jYWNoZV9zaXplPjEzNDIxNzcyODwvY29tcGlsZWRfZXhwcmVzc2lvbl9jYWNoZV9zaXplPlxuXG4gICAgPCEtLSBDYWNoZSBzaXplIGluIGVsZW1lbnRzIGZvciBjb21waWxlZCBleHByZXNzaW9ucy4tLT5cbiAgICA8Y29tcGlsZWRfZXhwcmVzc2lvbl9jYWNoZV9lbGVtZW50c19zaXplPjEwMDAwPC9jb21waWxlZF9leHByZXNzaW9uX2NhY2hlX2VsZW1lbnRzX3NpemU+XG5cbiAgICA8IS0tIFBhdGggdG8gZGF0YSBkaXJlY3RvcnksIHdpdGggdHJhaWxpbmcgc2xhc2guIC0tPlxuICAgIDxwYXRoPi92YXIvbGliL2NsaWNraG91c2UvPC9wYXRoPlxuXG4gICAgPCEtLSBQYXRoIHRvIHRlbXBvcmFyeSBkYXRhIGZvciBwcm9jZXNzaW5nIGhhcmQgcXVlcmllcy4gLS0+XG4gICAgPHRtcF9wYXRoPi92YXIvbGliL2NsaWNraG91c2UvdG1wLzwvdG1wX3BhdGg+XG5cbiAgICA8IS0tIERpc2FibGUgQXV0aFR5cGUgcGxhaW50ZXh0X3Bhc3N3b3JkIGFuZCBub19wYXNzd29yZCBmb3IgQUNMLiAtLT5cbiAgICA8IS0tIDxhbGxvd19wbGFpbnRleHRfcGFzc3dvcmQ+MDwvYWxsb3dfcGxhaW50ZXh0X3Bhc3N3b3JkPiAtLT5cbiAgICA8IS0tIDxhbGxvd19ub19wYXNzd29yZD4wPC9hbGxvd19ub19wYXNzd29yZD4gLS0+YFxuXG4gICAgPCEtLSBQb2xpY3kgZnJvbSB0aGUgPHN0b3JhZ2VfY29uZmlndXJhdGlvbj4gZm9yIHRoZSB0ZW1wb3JhcnkgZmlsZXMuXG4gICAgICAgICBJZiBub3Qgc2V0IDx0bXBfcGF0aD4gaXMgdXNlZCwgb3RoZXJ3aXNlIDx0bXBfcGF0aD4gaXMgaWdub3JlZC5cblxuICAgICAgICAgTm90ZXM6XG4gICAgICAgICAtIG1vdmVfZmFjdG9yICAgICAgICAgICAgICBpcyBpZ25vcmVkXG4gICAgICAgICAtIGtlZXBfZnJlZV9zcGFjZV9ieXRlcyAgICBpcyBpZ25vcmVkXG4gICAgICAgICAtIG1heF9kYXRhX3BhcnRfc2l6ZV9ieXRlcyBpcyBpZ25vcmVkXG4gICAgICAgICAtIHlvdSBtdXN0IGhhdmUgZXhhY3RseSBvbmUgdm9sdW1lIGluIHRoYXQgcG9saWN5XG4gICAgLS0+XG4gICAgPCEtLSA8dG1wX3BvbGljeT50bXA8L3RtcF9wb2xpY3k+IC0tPlxuXG4gICAgPCEtLSBEaXJlY3Rvcnkgd2l0aCB1c2VyIHByb3ZpZGVkIGZpbGVzIHRoYXQgYXJlIGFjY2Vzc2libGUgYnkgJ2ZpbGUnIHRhYmxlIGZ1bmN0aW9uLiAtLT5cbiAgICA8dXNlcl9maWxlc19wYXRoPi92YXIvbGliL2NsaWNraG91c2UvdXNlcl9maWxlcy88L3VzZXJfZmlsZXNfcGF0aD5cblxuICAgIDwhLS0gTERBUCBzZXJ2ZXIgZGVmaW5pdGlvbnMuIC0tPlxuICAgIDxsZGFwX3NlcnZlcnM+XG4gICAgICAgIDwhLS0gTGlzdCBMREFQIHNlcnZlcnMgd2l0aCB0aGVpciBjb25uZWN0aW9uIHBhcmFtZXRlcnMgaGVyZSB0byBsYXRlciAxKSB1c2UgdGhlbSBhcyBhdXRoZW50aWNhdG9ycyBmb3IgZGVkaWNhdGVkIGxvY2FsIHVzZXJzLFxuICAgICAgICAgICAgICB3aG8gaGF2ZSAnbGRhcCcgYXV0aGVudGljYXRpb24gbWVjaGFuaXNtIHNwZWNpZmllZCBpbnN0ZWFkIG9mICdwYXNzd29yZCcsIG9yIHRvIDIpIHVzZSB0aGVtIGFzIHJlbW90ZSB1c2VyIGRpcmVjdG9yaWVzLlxuICAgICAgICAgICAgIFBhcmFtZXRlcnM6XG4gICAgICAgICAgICAgICAgaG9zdCAtIExEQVAgc2VydmVyIGhvc3RuYW1lIG9yIElQLCB0aGlzIHBhcmFtZXRlciBpcyBtYW5kYXRvcnkgYW5kIGNhbm5vdCBiZSBlbXB0eS5cbiAgICAgICAgICAgICAgICBwb3J0IC0gTERBUCBzZXJ2ZXIgcG9ydCwgZGVmYXVsdCBpcyA2MzYgaWYgZW5hYmxlX3RscyBpcyBzZXQgdG8gdHJ1ZSwgMzg5IG90aGVyd2lzZS5cbiAgICAgICAgICAgICAgICBiaW5kX2RuIC0gdGVtcGxhdGUgdXNlZCB0byBjb25zdHJ1Y3QgdGhlIEROIHRvIGJpbmQgdG8uXG4gICAgICAgICAgICAgICAgICAgICAgICBUaGUgcmVzdWx0aW5nIEROIHdpbGwgYmUgY29uc3RydWN0ZWQgYnkgcmVwbGFjaW5nIGFsbCAne3VzZXJfbmFtZX0nIHN1YnN0cmluZ3Mgb2YgdGhlIHRlbXBsYXRlIHdpdGggdGhlIGFjdHVhbFxuICAgICAgICAgICAgICAgICAgICAgICAgIHVzZXIgbmFtZSBkdXJpbmcgZWFjaCBhdXRoZW50aWNhdGlvbiBhdHRlbXB0LlxuICAgICAgICAgICAgICAgIHVzZXJfZG5fZGV0ZWN0aW9uIC0gc2VjdGlvbiB3aXRoIExEQVAgc2VhcmNoIHBhcmFtZXRlcnMgZm9yIGRldGVjdGluZyB0aGUgYWN0dWFsIHVzZXIgRE4gb2YgdGhlIGJvdW5kIHVzZXIuXG4gICAgICAgICAgICAgICAgICAgICAgICBUaGlzIGlzIG1haW5seSB1c2VkIGluIHNlYXJjaCBmaWx0ZXJzIGZvciBmdXJ0aGVyIHJvbGUgbWFwcGluZyB3aGVuIHRoZSBzZXJ2ZXIgaXMgQWN0aXZlIERpcmVjdG9yeS4gVGhlXG4gICAgICAgICAgICAgICAgICAgICAgICAgcmVzdWx0aW5nIHVzZXIgRE4gd2lsbCBiZSB1c2VkIHdoZW4gcmVwbGFjaW5nICd7dXNlcl9kbn0nIHN1YnN0cmluZ3Mgd2hlcmV2ZXIgdGhleSBhcmUgYWxsb3dlZC4gQnkgZGVmYXVsdCxcbiAgICAgICAgICAgICAgICAgICAgICAgICB1c2VyIEROIGlzIHNldCBlcXVhbCB0byBiaW5kIEROLCBidXQgb25jZSBzZWFyY2ggaXMgcGVyZm9ybWVkLCBpdCB3aWxsIGJlIHVwZGF0ZWQgd2l0aCB0byB0aGUgYWN0dWFsIGRldGVjdGVkXG4gICAgICAgICAgICAgICAgICAgICAgICAgdXNlciBETiB2YWx1ZS5cbiAgICAgICAgICAgICAgICAgICAgYmFzZV9kbiAtIHRlbXBsYXRlIHVzZWQgdG8gY29uc3RydWN0IHRoZSBiYXNlIEROIGZvciB0aGUgTERBUCBzZWFyY2guXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgVGhlIHJlc3VsdGluZyBETiB3aWxsIGJlIGNvbnN0cnVjdGVkIGJ5IHJlcGxhY2luZyBhbGwgJ3t1c2VyX25hbWV9JyBhbmQgJ3tiaW5kX2RufScgc3Vic3RyaW5nc1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgICBvZiB0aGUgdGVtcGxhdGUgd2l0aCB0aGUgYWN0dWFsIHVzZXIgbmFtZSBhbmQgYmluZCBETiBkdXJpbmcgdGhlIExEQVAgc2VhcmNoLlxuICAgICAgICAgICAgICAgICAgICBzY29wZSAtIHNjb3BlIG9mIHRoZSBMREFQIHNlYXJjaC5cbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBBY2NlcHRlZCB2YWx1ZXMgYXJlOiAnYmFzZScsICdvbmVfbGV2ZWwnLCAnY2hpbGRyZW4nLCAnc3VidHJlZScgKHRoZSBkZWZhdWx0KS5cbiAgICAgICAgICAgICAgICAgICAgc2VhcmNoX2ZpbHRlciAtIHRlbXBsYXRlIHVzZWQgdG8gY29uc3RydWN0IHRoZSBzZWFyY2ggZmlsdGVyIGZvciB0aGUgTERBUCBzZWFyY2guXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgVGhlIHJlc3VsdGluZyBmaWx0ZXIgd2lsbCBiZSBjb25zdHJ1Y3RlZCBieSByZXBsYWNpbmcgYWxsICd7dXNlcl9uYW1lfScsICd7YmluZF9kbn0nLCBhbmQgJ3tiYXNlX2RufSdcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgc3Vic3RyaW5ncyBvZiB0aGUgdGVtcGxhdGUgd2l0aCB0aGUgYWN0dWFsIHVzZXIgbmFtZSwgYmluZCBETiwgYW5kIGJhc2UgRE4gZHVyaW5nIHRoZSBMREFQIHNlYXJjaC5cbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBOb3RlLCB0aGF0IHRoZSBzcGVjaWFsIGNoYXJhY3RlcnMgbXVzdCBiZSBlc2NhcGVkIHByb3Blcmx5IGluIFhNTC5cbiAgICAgICAgICAgICAgICB2ZXJpZmljYXRpb25fY29vbGRvd24gLSBhIHBlcmlvZCBvZiB0aW1lLCBpbiBzZWNvbmRzLCBhZnRlciBhIHN1Y2Nlc3NmdWwgYmluZCBhdHRlbXB0LCBkdXJpbmcgd2hpY2ggYSB1c2VyIHdpbGwgYmUgYXNzdW1lZFxuICAgICAgICAgICAgICAgICAgICAgICAgIHRvIGJlIHN1Y2Nlc3NmdWxseSBhdXRoZW50aWNhdGVkIGZvciBhbGwgY29uc2VjdXRpdmUgcmVxdWVzdHMgd2l0aG91dCBjb250YWN0aW5nIHRoZSBMREFQIHNlcnZlci5cbiAgICAgICAgICAgICAgICAgICAgICAgIFNwZWNpZnkgMCAodGhlIGRlZmF1bHQpIHRvIGRpc2FibGUgY2FjaGluZyBhbmQgZm9yY2UgY29udGFjdGluZyB0aGUgTERBUCBzZXJ2ZXIgZm9yIGVhY2ggYXV0aGVudGljYXRpb24gcmVxdWVzdC5cbiAgICAgICAgICAgICAgICBlbmFibGVfdGxzIC0gZmxhZyB0byB0cmlnZ2VyIHVzZSBvZiBzZWN1cmUgY29ubmVjdGlvbiB0byB0aGUgTERBUCBzZXJ2ZXIuXG4gICAgICAgICAgICAgICAgICAgICAgICBTcGVjaWZ5ICdubycgZm9yIHBsYWluIHRleHQgKGxkYXA6Ly8pIHByb3RvY29sIChub3QgcmVjb21tZW5kZWQpLlxuICAgICAgICAgICAgICAgICAgICAgICAgU3BlY2lmeSAneWVzJyBmb3IgTERBUCBvdmVyIFNTTC9UTFMgKGxkYXBzOi8vKSBwcm90b2NvbCAocmVjb21tZW5kZWQsIHRoZSBkZWZhdWx0KS5cbiAgICAgICAgICAgICAgICAgICAgICAgIFNwZWNpZnkgJ3N0YXJ0dGxzJyBmb3IgbGVnYWN5IFN0YXJ0VExTIHByb3RvY29sIChwbGFpbiB0ZXh0IChsZGFwOi8vKSBwcm90b2NvbCwgdXBncmFkZWQgdG8gVExTKS5cbiAgICAgICAgICAgICAgICB0bHNfbWluaW11bV9wcm90b2NvbF92ZXJzaW9uIC0gdGhlIG1pbmltdW0gcHJvdG9jb2wgdmVyc2lvbiBvZiBTU0wvVExTLlxuICAgICAgICAgICAgICAgICAgICAgICAgQWNjZXB0ZWQgdmFsdWVzIGFyZTogJ3NzbDInLCAnc3NsMycsICd0bHMxLjAnLCAndGxzMS4xJywgJ3RsczEuMicgKHRoZSBkZWZhdWx0KS5cbiAgICAgICAgICAgICAgICB0bHNfcmVxdWlyZV9jZXJ0IC0gU1NML1RMUyBwZWVyIGNlcnRpZmljYXRlIHZlcmlmaWNhdGlvbiBiZWhhdmlvci5cbiAgICAgICAgICAgICAgICAgICAgICAgIEFjY2VwdGVkIHZhbHVlcyBhcmU6ICduZXZlcicsICdhbGxvdycsICd0cnknLCAnZGVtYW5kJyAodGhlIGRlZmF1bHQpLlxuICAgICAgICAgICAgICAgIHRsc19jZXJ0X2ZpbGUgLSBwYXRoIHRvIGNlcnRpZmljYXRlIGZpbGUuXG4gICAgICAgICAgICAgICAgdGxzX2tleV9maWxlIC0gcGF0aCB0byBjZXJ0aWZpY2F0ZSBrZXkgZmlsZS5cbiAgICAgICAgICAgICAgICB0bHNfY2FfY2VydF9maWxlIC0gcGF0aCB0byBDQSBjZXJ0aWZpY2F0ZSBmaWxlLlxuICAgICAgICAgICAgICAgIHRsc19jYV9jZXJ0X2RpciAtIHBhdGggdG8gdGhlIGRpcmVjdG9yeSBjb250YWluaW5nIENBIGNlcnRpZmljYXRlcy5cbiAgICAgICAgICAgICAgICB0bHNfY2lwaGVyX3N1aXRlIC0gYWxsb3dlZCBjaXBoZXIgc3VpdGUgKGluIE9wZW5TU0wgbm90YXRpb24pLlxuICAgICAgICAgICAgIEV4YW1wbGU6XG4gICAgICAgICAgICAgICAgPG15X2xkYXBfc2VydmVyPlxuICAgICAgICAgICAgICAgICAgICA8aG9zdD5sb2NhbGhvc3Q8L2hvc3Q+XG4gICAgICAgICAgICAgICAgICAgIDxwb3J0PjYzNjwvcG9ydD5cbiAgICAgICAgICAgICAgICAgICAgPGJpbmRfZG4+dWlkPXt1c2VyX25hbWV9LG91PXVzZXJzLGRjPWV4YW1wbGUsZGM9Y29tPC9iaW5kX2RuPlxuICAgICAgICAgICAgICAgICAgICA8dmVyaWZpY2F0aW9uX2Nvb2xkb3duPjMwMDwvdmVyaWZpY2F0aW9uX2Nvb2xkb3duPlxuICAgICAgICAgICAgICAgICAgICA8ZW5hYmxlX3Rscz55ZXM8L2VuYWJsZV90bHM+XG4gICAgICAgICAgICAgICAgICAgIDx0bHNfbWluaW11bV9wcm90b2NvbF92ZXJzaW9uPnRsczEuMjwvdGxzX21pbmltdW1fcHJvdG9jb2xfdmVyc2lvbj5cbiAgICAgICAgICAgICAgICAgICAgPHRsc19yZXF1aXJlX2NlcnQ+ZGVtYW5kPC90bHNfcmVxdWlyZV9jZXJ0PlxuICAgICAgICAgICAgICAgICAgICA8dGxzX2NlcnRfZmlsZT4vcGF0aC90by90bHNfY2VydF9maWxlPC90bHNfY2VydF9maWxlPlxuICAgICAgICAgICAgICAgICAgICA8dGxzX2tleV9maWxlPi9wYXRoL3RvL3Rsc19rZXlfZmlsZTwvdGxzX2tleV9maWxlPlxuICAgICAgICAgICAgICAgICAgICA8dGxzX2NhX2NlcnRfZmlsZT4vcGF0aC90by90bHNfY2FfY2VydF9maWxlPC90bHNfY2FfY2VydF9maWxlPlxuICAgICAgICAgICAgICAgICAgICA8dGxzX2NhX2NlcnRfZGlyPi9wYXRoL3RvL3Rsc19jYV9jZXJ0X2RpcjwvdGxzX2NhX2NlcnRfZGlyPlxuICAgICAgICAgICAgICAgICAgICA8dGxzX2NpcGhlcl9zdWl0ZT5FQ0RIRS1FQ0RTQS1BRVMyNTYtR0NNLVNIQTM4NDpFQ0RIRS1SU0EtQUVTMjU2LUdDTS1TSEEzODQ6QUVTMjU2LUdDTS1TSEEzODQ8L3Rsc19jaXBoZXJfc3VpdGU+XG4gICAgICAgICAgICAgICAgPC9teV9sZGFwX3NlcnZlcj5cbiAgICAgICAgICAgICBFeGFtcGxlICh0eXBpY2FsIEFjdGl2ZSBEaXJlY3Rvcnkgd2l0aCBjb25maWd1cmVkIHVzZXIgRE4gZGV0ZWN0aW9uIGZvciBmdXJ0aGVyIHJvbGUgbWFwcGluZyk6XG4gICAgICAgICAgICAgICAgPG15X2FkX3NlcnZlcj5cbiAgICAgICAgICAgICAgICAgICAgPGhvc3Q+bG9jYWxob3N0PC9ob3N0PlxuICAgICAgICAgICAgICAgICAgICA8cG9ydD4zODk8L3BvcnQ+XG4gICAgICAgICAgICAgICAgICAgIDxiaW5kX2RuPkVYQU1QTEVcXHt1c2VyX25hbWV9PC9iaW5kX2RuPlxuICAgICAgICAgICAgICAgICAgICA8dXNlcl9kbl9kZXRlY3Rpb24+XG4gICAgICAgICAgICAgICAgICAgICAgICA8YmFzZV9kbj5DTj1Vc2VycyxEQz1leGFtcGxlLERDPWNvbTwvYmFzZV9kbj5cbiAgICAgICAgICAgICAgICAgICAgICAgIDxzZWFyY2hfZmlsdGVyPigmYW1wOyhvYmplY3RDbGFzcz11c2VyKShzQU1BY2NvdW50TmFtZT17dXNlcl9uYW1lfSkpPC9zZWFyY2hfZmlsdGVyPlxuICAgICAgICAgICAgICAgICAgICA8L3VzZXJfZG5fZGV0ZWN0aW9uPlxuICAgICAgICAgICAgICAgICAgICA8ZW5hYmxlX3Rscz5ubzwvZW5hYmxlX3Rscz5cbiAgICAgICAgICAgICAgICA8L215X2FkX3NlcnZlcj5cbiAgICAgICAgLS0+XG4gICAgPC9sZGFwX3NlcnZlcnM+XG5cbiAgICA8IS0tIFRvIGVuYWJsZSBLZXJiZXJvcyBhdXRoZW50aWNhdGlvbiBzdXBwb3J0IGZvciBIVFRQIHJlcXVlc3RzIChHU1MtU1BORUdPKSwgZm9yIHRob3NlIHVzZXJzIHdobyBhcmUgZXhwbGljaXRseSBjb25maWd1cmVkXG4gICAgICAgICAgdG8gYXV0aGVudGljYXRlIHZpYSBLZXJiZXJvcywgZGVmaW5lIGEgc2luZ2xlICdrZXJiZXJvcycgc2VjdGlvbiBoZXJlLlxuICAgICAgICAgUGFyYW1ldGVyczpcbiAgICAgICAgICAgIHByaW5jaXBhbCAtIGNhbm9uaWNhbCBzZXJ2aWNlIHByaW5jaXBhbCBuYW1lLCB0aGF0IHdpbGwgYmUgYWNxdWlyZWQgYW5kIHVzZWQgd2hlbiBhY2NlcHRpbmcgc2VjdXJpdHkgY29udGV4dHMuXG4gICAgICAgICAgICAgICAgICAgIFRoaXMgcGFyYW1ldGVyIGlzIG9wdGlvbmFsLCBpZiBvbWl0dGVkLCB0aGUgZGVmYXVsdCBwcmluY2lwYWwgd2lsbCBiZSB1c2VkLlxuICAgICAgICAgICAgICAgICAgICBUaGlzIHBhcmFtZXRlciBjYW5ub3QgYmUgc3BlY2lmaWVkIHRvZ2V0aGVyIHdpdGggJ3JlYWxtJyBwYXJhbWV0ZXIuXG4gICAgICAgICAgICByZWFsbSAtIGEgcmVhbG0sIHRoYXQgd2lsbCBiZSB1c2VkIHRvIHJlc3RyaWN0IGF1dGhlbnRpY2F0aW9uIHRvIG9ubHkgdGhvc2UgcmVxdWVzdHMgd2hvc2UgaW5pdGlhdG9yJ3MgcmVhbG0gbWF0Y2hlcyBpdC5cbiAgICAgICAgICAgICAgICAgICAgVGhpcyBwYXJhbWV0ZXIgaXMgb3B0aW9uYWwsIGlmIG9taXR0ZWQsIG5vIGFkZGl0aW9uYWwgZmlsdGVyaW5nIGJ5IHJlYWxtIHdpbGwgYmUgYXBwbGllZC5cbiAgICAgICAgICAgICAgICAgICAgVGhpcyBwYXJhbWV0ZXIgY2Fubm90IGJlIHNwZWNpZmllZCB0b2dldGhlciB3aXRoICdwcmluY2lwYWwnIHBhcmFtZXRlci5cbiAgICAgICAgIEV4YW1wbGU6XG4gICAgICAgICAgICA8a2VyYmVyb3MgLz5cbiAgICAgICAgIEV4YW1wbGU6XG4gICAgICAgICAgICA8a2VyYmVyb3M+XG4gICAgICAgICAgICAgICAgPHByaW5jaXBhbD5IVFRQL2NsaWNraG91c2UuZXhhbXBsZS5jb21ARVhBTVBMRS5DT008L3ByaW5jaXBhbD5cbiAgICAgICAgICAgIDwva2VyYmVyb3M+XG4gICAgICAgICBFeGFtcGxlOlxuICAgICAgICAgICAgPGtlcmJlcm9zPlxuICAgICAgICAgICAgICAgIDxyZWFsbT5FWEFNUExFLkNPTTwvcmVhbG0+XG4gICAgICAgICAgICA8L2tlcmJlcm9zPlxuICAgIC0tPlxuXG4gICAgPCEtLSBTb3VyY2VzIHRvIHJlYWQgdXNlcnMsIHJvbGVzLCBhY2Nlc3MgcmlnaHRzLCBwcm9maWxlcyBvZiBzZXR0aW5ncywgcXVvdGFzLiAtLT5cbiAgICA8dXNlcl9kaXJlY3Rvcmllcz5cbiAgICAgICAgPHVzZXJzX3htbD5cbiAgICAgICAgICAgIDwhLS0gUGF0aCB0byBjb25maWd1cmF0aW9uIGZpbGUgd2l0aCBwcmVkZWZpbmVkIHVzZXJzLiAtLT5cbiAgICAgICAgICAgIDxwYXRoPnVzZXJzLnhtbDwvcGF0aD5cbiAgICAgICAgPC91c2Vyc194bWw+XG4gICAgICAgIDxsb2NhbF9kaXJlY3Rvcnk+XG4gICAgICAgICAgICA8IS0tIFBhdGggdG8gZm9sZGVyIHdoZXJlIHVzZXJzIGNyZWF0ZWQgYnkgU1FMIGNvbW1hbmRzIGFyZSBzdG9yZWQuIC0tPlxuICAgICAgICAgICAgPHBhdGg+L3Zhci9saWIvY2xpY2tob3VzZS9hY2Nlc3MvPC9wYXRoPlxuICAgICAgICA8L2xvY2FsX2RpcmVjdG9yeT5cblxuICAgICAgICA8IS0tIFRvIGFkZCBhbiBMREFQIHNlcnZlciBhcyBhIHJlbW90ZSB1c2VyIGRpcmVjdG9yeSBvZiB1c2VycyB0aGF0IGFyZSBub3QgZGVmaW5lZCBsb2NhbGx5LCBkZWZpbmUgYSBzaW5nbGUgJ2xkYXAnIHNlY3Rpb25cbiAgICAgICAgICAgICAgd2l0aCB0aGUgZm9sbG93aW5nIHBhcmFtZXRlcnM6XG4gICAgICAgICAgICAgICAgc2VydmVyIC0gb25lIG9mIExEQVAgc2VydmVyIG5hbWVzIGRlZmluZWQgaW4gJ2xkYXBfc2VydmVycycgY29uZmlnIHNlY3Rpb24gYWJvdmUuXG4gICAgICAgICAgICAgICAgICAgICAgICBUaGlzIHBhcmFtZXRlciBpcyBtYW5kYXRvcnkgYW5kIGNhbm5vdCBiZSBlbXB0eS5cbiAgICAgICAgICAgICAgICByb2xlcyAtIHNlY3Rpb24gd2l0aCBhIGxpc3Qgb2YgbG9jYWxseSBkZWZpbmVkIHJvbGVzIHRoYXQgd2lsbCBiZSBhc3NpZ25lZCB0byBlYWNoIHVzZXIgcmV0cmlldmVkIGZyb20gdGhlIExEQVAgc2VydmVyLlxuICAgICAgICAgICAgICAgICAgICAgICAgSWYgbm8gcm9sZXMgYXJlIHNwZWNpZmllZCBoZXJlIG9yIGFzc2lnbmVkIGR1cmluZyByb2xlIG1hcHBpbmcgKGJlbG93KSwgdXNlciB3aWxsIG5vdCBiZSBhYmxlIHRvIHBlcmZvcm0gYW55XG4gICAgICAgICAgICAgICAgICAgICAgICAgYWN0aW9ucyBhZnRlciBhdXRoZW50aWNhdGlvbi5cbiAgICAgICAgICAgICAgICByb2xlX21hcHBpbmcgLSBzZWN0aW9uIHdpdGggTERBUCBzZWFyY2ggcGFyYW1ldGVycyBhbmQgbWFwcGluZyBydWxlcy5cbiAgICAgICAgICAgICAgICAgICAgICAgIFdoZW4gYSB1c2VyIGF1dGhlbnRpY2F0ZXMsIHdoaWxlIHN0aWxsIGJvdW5kIHRvIExEQVAsIGFuIExEQVAgc2VhcmNoIGlzIHBlcmZvcm1lZCB1c2luZyBzZWFyY2hfZmlsdGVyIGFuZCB0aGVcbiAgICAgICAgICAgICAgICAgICAgICAgICBuYW1lIG9mIHRoZSBsb2dnZWQgaW4gdXNlci4gRm9yIGVhY2ggZW50cnkgZm91bmQgZHVyaW5nIHRoYXQgc2VhcmNoLCB0aGUgdmFsdWUgb2YgdGhlIHNwZWNpZmllZCBhdHRyaWJ1dGUgaXNcbiAgICAgICAgICAgICAgICAgICAgICAgICBleHRyYWN0ZWQuIEZvciBlYWNoIGF0dHJpYnV0ZSB2YWx1ZSB0aGF0IGhhcyB0aGUgc3BlY2lmaWVkIHByZWZpeCwgdGhlIHByZWZpeCBpcyByZW1vdmVkLCBhbmQgdGhlIHJlc3Qgb2YgdGhlXG4gICAgICAgICAgICAgICAgICAgICAgICAgdmFsdWUgYmVjb21lcyB0aGUgbmFtZSBvZiBhIGxvY2FsIHJvbGUgZGVmaW5lZCBpbiBDbGlja0hvdXNlLCB3aGljaCBpcyBleHBlY3RlZCB0byBiZSBjcmVhdGVkIGJlZm9yZWhhbmQgYnlcbiAgICAgICAgICAgICAgICAgICAgICAgICBDUkVBVEUgUk9MRSBjb21tYW5kLlxuICAgICAgICAgICAgICAgICAgICAgICAgVGhlcmUgY2FuIGJlIG11bHRpcGxlICdyb2xlX21hcHBpbmcnIHNlY3Rpb25zIGRlZmluZWQgaW5zaWRlIHRoZSBzYW1lICdsZGFwJyBzZWN0aW9uLiBBbGwgb2YgdGhlbSB3aWxsIGJlXG4gICAgICAgICAgICAgICAgICAgICAgICAgYXBwbGllZC5cbiAgICAgICAgICAgICAgICAgICAgYmFzZV9kbiAtIHRlbXBsYXRlIHVzZWQgdG8gY29uc3RydWN0IHRoZSBiYXNlIEROIGZvciB0aGUgTERBUCBzZWFyY2guXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgVGhlIHJlc3VsdGluZyBETiB3aWxsIGJlIGNvbnN0cnVjdGVkIGJ5IHJlcGxhY2luZyBhbGwgJ3t1c2VyX25hbWV9JywgJ3tiaW5kX2RufScsIGFuZCAne3VzZXJfZG59J1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgICBzdWJzdHJpbmdzIG9mIHRoZSB0ZW1wbGF0ZSB3aXRoIHRoZSBhY3R1YWwgdXNlciBuYW1lLCBiaW5kIEROLCBhbmQgdXNlciBETiBkdXJpbmcgZWFjaCBMREFQIHNlYXJjaC5cbiAgICAgICAgICAgICAgICAgICAgc2NvcGUgLSBzY29wZSBvZiB0aGUgTERBUCBzZWFyY2guXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgQWNjZXB0ZWQgdmFsdWVzIGFyZTogJ2Jhc2UnLCAnb25lX2xldmVsJywgJ2NoaWxkcmVuJywgJ3N1YnRyZWUnICh0aGUgZGVmYXVsdCkuXG4gICAgICAgICAgICAgICAgICAgIHNlYXJjaF9maWx0ZXIgLSB0ZW1wbGF0ZSB1c2VkIHRvIGNvbnN0cnVjdCB0aGUgc2VhcmNoIGZpbHRlciBmb3IgdGhlIExEQVAgc2VhcmNoLlxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIFRoZSByZXN1bHRpbmcgZmlsdGVyIHdpbGwgYmUgY29uc3RydWN0ZWQgYnkgcmVwbGFjaW5nIGFsbCAne3VzZXJfbmFtZX0nLCAne2JpbmRfZG59JywgJ3t1c2VyX2RufScsIGFuZFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAne2Jhc2VfZG59JyBzdWJzdHJpbmdzIG9mIHRoZSB0ZW1wbGF0ZSB3aXRoIHRoZSBhY3R1YWwgdXNlciBuYW1lLCBiaW5kIEROLCB1c2VyIEROLCBhbmQgYmFzZSBETiBkdXJpbmdcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZWFjaCBMREFQIHNlYXJjaC5cbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBOb3RlLCB0aGF0IHRoZSBzcGVjaWFsIGNoYXJhY3RlcnMgbXVzdCBiZSBlc2NhcGVkIHByb3Blcmx5IGluIFhNTC5cbiAgICAgICAgICAgICAgICAgICAgYXR0cmlidXRlIC0gYXR0cmlidXRlIG5hbWUgd2hvc2UgdmFsdWVzIHdpbGwgYmUgcmV0dXJuZWQgYnkgdGhlIExEQVAgc2VhcmNoLiAnY24nLCBieSBkZWZhdWx0LlxuICAgICAgICAgICAgICAgICAgICBwcmVmaXggLSBwcmVmaXgsIHRoYXQgd2lsbCBiZSBleHBlY3RlZCB0byBiZSBpbiBmcm9udCBvZiBlYWNoIHN0cmluZyBpbiB0aGUgb3JpZ2luYWwgbGlzdCBvZiBzdHJpbmdzIHJldHVybmVkIGJ5XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRoZSBMREFQIHNlYXJjaC4gUHJlZml4IHdpbGwgYmUgcmVtb3ZlZCBmcm9tIHRoZSBvcmlnaW5hbCBzdHJpbmdzIGFuZCByZXN1bHRpbmcgc3RyaW5ncyB3aWxsIGJlIHRyZWF0ZWRcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgYXMgbG9jYWwgcm9sZSBuYW1lcy4gRW1wdHksIGJ5IGRlZmF1bHQuXG4gICAgICAgICAgICAgRXhhbXBsZTpcbiAgICAgICAgICAgICAgICA8bGRhcD5cbiAgICAgICAgICAgICAgICAgICAgPHNlcnZlcj5teV9sZGFwX3NlcnZlcjwvc2VydmVyPlxuICAgICAgICAgICAgICAgICAgICA8cm9sZXM+XG4gICAgICAgICAgICAgICAgICAgICAgICA8bXlfbG9jYWxfcm9sZTEgLz5cbiAgICAgICAgICAgICAgICAgICAgICAgIDxteV9sb2NhbF9yb2xlMiAvPlxuICAgICAgICAgICAgICAgICAgICA8L3JvbGVzPlxuICAgICAgICAgICAgICAgICAgICA8cm9sZV9tYXBwaW5nPlxuICAgICAgICAgICAgICAgICAgICAgICAgPGJhc2VfZG4+b3U9Z3JvdXBzLGRjPWV4YW1wbGUsZGM9Y29tPC9iYXNlX2RuPlxuICAgICAgICAgICAgICAgICAgICAgICAgPHNjb3BlPnN1YnRyZWU8L3Njb3BlPlxuICAgICAgICAgICAgICAgICAgICAgICAgPHNlYXJjaF9maWx0ZXI+KCZhbXA7KG9iamVjdENsYXNzPWdyb3VwT2ZOYW1lcykobWVtYmVyPXtiaW5kX2RufSkpPC9zZWFyY2hfZmlsdGVyPlxuICAgICAgICAgICAgICAgICAgICAgICAgPGF0dHJpYnV0ZT5jbjwvYXR0cmlidXRlPlxuICAgICAgICAgICAgICAgICAgICAgICAgPHByZWZpeD5jbGlja2hvdXNlXzwvcHJlZml4PlxuICAgICAgICAgICAgICAgICAgICA8L3JvbGVfbWFwcGluZz5cbiAgICAgICAgICAgICAgICA8L2xkYXA+XG4gICAgICAgICAgICAgRXhhbXBsZSAodHlwaWNhbCBBY3RpdmUgRGlyZWN0b3J5IHdpdGggcm9sZSBtYXBwaW5nIHRoYXQgcmVsaWVzIG9uIHRoZSBkZXRlY3RlZCB1c2VyIEROKTpcbiAgICAgICAgICAgICAgICA8bGRhcD5cbiAgICAgICAgICAgICAgICAgICAgPHNlcnZlcj5teV9hZF9zZXJ2ZXI8L3NlcnZlcj5cbiAgICAgICAgICAgICAgICAgICAgPHJvbGVfbWFwcGluZz5cbiAgICAgICAgICAgICAgICAgICAgICAgIDxiYXNlX2RuPkNOPVVzZXJzLERDPWV4YW1wbGUsREM9Y29tPC9iYXNlX2RuPlxuICAgICAgICAgICAgICAgICAgICAgICAgPGF0dHJpYnV0ZT5DTjwvYXR0cmlidXRlPlxuICAgICAgICAgICAgICAgICAgICAgICAgPHNjb3BlPnN1YnRyZWU8L3Njb3BlPlxuICAgICAgICAgICAgICAgICAgICAgICAgPHNlYXJjaF9maWx0ZXI+KCZhbXA7KG9iamVjdENsYXNzPWdyb3VwKShtZW1iZXI9e3VzZXJfZG59KSk8L3NlYXJjaF9maWx0ZXI+XG4gICAgICAgICAgICAgICAgICAgICAgICA8cHJlZml4PmNsaWNraG91c2VfPC9wcmVmaXg+XG4gICAgICAgICAgICAgICAgICAgIDwvcm9sZV9tYXBwaW5nPlxuICAgICAgICAgICAgICAgIDwvbGRhcD5cbiAgICAgICAgLS0+XG4gICAgPC91c2VyX2RpcmVjdG9yaWVzPlxuXG4gICAgPCEtLSBEZWZhdWx0IHByb2ZpbGUgb2Ygc2V0dGluZ3MuIC0tPlxuICAgIDxkZWZhdWx0X3Byb2ZpbGU+ZGVmYXVsdDwvZGVmYXVsdF9wcm9maWxlPlxuXG4gICAgPCEtLSBDb21tYS1zZXBhcmF0ZWQgbGlzdCBvZiBwcmVmaXhlcyBmb3IgdXNlci1kZWZpbmVkIHNldHRpbmdzLiAtLT5cbiAgICA8Y3VzdG9tX3NldHRpbmdzX3ByZWZpeGVzPjwvY3VzdG9tX3NldHRpbmdzX3ByZWZpeGVzPlxuXG4gICAgPCEtLSBTeXN0ZW0gcHJvZmlsZSBvZiBzZXR0aW5ncy4gVGhpcyBzZXR0aW5ncyBhcmUgdXNlZCBieSBpbnRlcm5hbCBwcm9jZXNzZXMgKERpc3RyaWJ1dGVkIERETCB3b3JrZXIgYW5kIHNvIG9uKS4gLS0+XG4gICAgPCEtLSA8c3lzdGVtX3Byb2ZpbGU+ZGVmYXVsdDwvc3lzdGVtX3Byb2ZpbGU+IC0tPlxuXG4gICAgPCEtLSBCdWZmZXIgcHJvZmlsZSBvZiBzZXR0aW5ncy5cbiAgICAgICAgIFRoaXMgc2V0dGluZ3MgYXJlIHVzZWQgYnkgQnVmZmVyIHN0b3JhZ2UgdG8gZmx1c2ggZGF0YSB0byB0aGUgdW5kZXJseWluZyB0YWJsZS5cbiAgICAgICAgIERlZmF1bHQ6IHVzZWQgZnJvbSBzeXN0ZW1fcHJvZmlsZSBkaXJlY3RpdmUuXG4gICAgLS0+XG4gICAgPCEtLSA8YnVmZmVyX3Byb2ZpbGU+ZGVmYXVsdDwvYnVmZmVyX3Byb2ZpbGU+IC0tPlxuXG4gICAgPCEtLSBEZWZhdWx0IGRhdGFiYXNlLiAtLT5cbiAgICA8ZGVmYXVsdF9kYXRhYmFzZT5kZWZhdWx0PC9kZWZhdWx0X2RhdGFiYXNlPlxuXG4gICAgPCEtLSBTZXJ2ZXIgdGltZSB6b25lIGNvdWxkIGJlIHNldCBoZXJlLlxuXG4gICAgICAgICBUaW1lIHpvbmUgaXMgdXNlZCB3aGVuIGNvbnZlcnRpbmcgYmV0d2VlbiBTdHJpbmcgYW5kIERhdGVUaW1lIHR5cGVzLFxuICAgICAgICAgIHdoZW4gcHJpbnRpbmcgRGF0ZVRpbWUgaW4gdGV4dCBmb3JtYXRzIGFuZCBwYXJzaW5nIERhdGVUaW1lIGZyb20gdGV4dCxcbiAgICAgICAgICBpdCBpcyB1c2VkIGluIGRhdGUgYW5kIHRpbWUgcmVsYXRlZCBmdW5jdGlvbnMsIGlmIHNwZWNpZmljIHRpbWUgem9uZSB3YXMgbm90IHBhc3NlZCBhcyBhbiBhcmd1bWVudC5cblxuICAgICAgICAgVGltZSB6b25lIGlzIHNwZWNpZmllZCBhcyBpZGVudGlmaWVyIGZyb20gSUFOQSB0aW1lIHpvbmUgZGF0YWJhc2UsIGxpa2UgVVRDIG9yIEFmcmljYS9BYmlkamFuLlxuICAgICAgICAgSWYgbm90IHNwZWNpZmllZCwgc3lzdGVtIHRpbWUgem9uZSBhdCBzZXJ2ZXIgc3RhcnR1cCBpcyB1c2VkLlxuXG4gICAgICAgICBQbGVhc2Ugbm90ZSwgdGhhdCBzZXJ2ZXIgY291bGQgZGlzcGxheSB0aW1lIHpvbmUgYWxpYXMgaW5zdGVhZCBvZiBzcGVjaWZpZWQgbmFtZS5cbiAgICAgICAgIEV4YW1wbGU6IFp1bHUgaXMgYW4gYWxpYXMgZm9yIFVUQy5cbiAgICAtLT5cbiAgICA8IS0tIDx0aW1lem9uZT5VVEM8L3RpbWV6b25lPiAtLT5cblxuICAgIDwhLS0gWW91IGNhbiBzcGVjaWZ5IHVtYXNrIGhlcmUgKHNlZSBcIm1hbiB1bWFza1wiKS4gU2VydmVyIHdpbGwgYXBwbHkgaXQgb24gc3RhcnR1cC5cbiAgICAgICAgIE51bWJlciBpcyBhbHdheXMgcGFyc2VkIGFzIG9jdGFsLiBEZWZhdWx0IHVtYXNrIGlzIDAyNyAob3RoZXIgdXNlcnMgY2Fubm90IHJlYWQgbG9ncywgZGF0YSBmaWxlcywgZXRjOyBncm91cCBjYW4gb25seSByZWFkKS5cbiAgICAtLT5cbiAgICA8IS0tIDx1bWFzaz4wMjI8L3VtYXNrPiAtLT5cblxuICAgIDwhLS0gUGVyZm9ybSBtbG9ja2FsbCBhZnRlciBzdGFydHVwIHRvIGxvd2VyIGZpcnN0IHF1ZXJpZXMgbGF0ZW5jeVxuICAgICAgICAgIGFuZCB0byBwcmV2ZW50IGNsaWNraG91c2UgZXhlY3V0YWJsZSBmcm9tIGJlaW5nIHBhZ2VkIG91dCB1bmRlciBoaWdoIElPIGxvYWQuXG4gICAgICAgICBFbmFibGluZyB0aGlzIG9wdGlvbiBpcyByZWNvbW1lbmRlZCBidXQgd2lsbCBsZWFkIHRvIGluY3JlYXNlZCBzdGFydHVwIHRpbWUgZm9yIHVwIHRvIGEgZmV3IHNlY29uZHMuXG4gICAgLS0+XG4gICAgPG1sb2NrX2V4ZWN1dGFibGU+dHJ1ZTwvbWxvY2tfZXhlY3V0YWJsZT5cblxuICAgIDwhLS0gUmVhbGxvY2F0ZSBtZW1vcnkgZm9yIG1hY2hpbmUgY29kZSAoXCJ0ZXh0XCIpIHVzaW5nIGh1Z2UgcGFnZXMuIEhpZ2hseSBleHBlcmltZW50YWwuIC0tPlxuICAgIDxyZW1hcF9leGVjdXRhYmxlPmZhbHNlPC9yZW1hcF9leGVjdXRhYmxlPlxuXG4gICAgPCFbQ0RBVEFbXG4gICAgICAgICBVbmNvbW1lbnQgYmVsb3cgaW4gb3JkZXIgdG8gdXNlIEpEQkMgdGFibGUgZW5naW5lIGFuZCBmdW5jdGlvbi5cblxuICAgICAgICAgVG8gaW5zdGFsbCBhbmQgcnVuIEpEQkMgYnJpZGdlIGluIGJhY2tncm91bmQ6XG4gICAgICAgICAqIFtEZWJpYW4vVWJ1bnR1XVxuICAgICAgICAgICBleHBvcnQgTVZOX1VSTD1odHRwczovL3JlcG8xLm1hdmVuLm9yZy9tYXZlbjIvcnUveWFuZGV4L2NsaWNraG91c2UvY2xpY2tob3VzZS1qZGJjLWJyaWRnZVxuICAgICAgICAgICBleHBvcnQgUEtHX1ZFUj0kKGN1cmwgLXNMICRNVk5fVVJML21hdmVuLW1ldGFkYXRhLnhtbCB8IGdyZXAgJzxyZWxlYXNlPicgfCBzZWQgLWUgJ3N8Lio+XFwoLipcXCk8Lip8XFwxfCcpXG4gICAgICAgICAgIHdnZXQgaHR0cHM6Ly9naXRodWIuY29tL0NsaWNrSG91c2UvY2xpY2tob3VzZS1qZGJjLWJyaWRnZS9yZWxlYXNlcy9kb3dubG9hZC92JFBLR19WRVIvY2xpY2tob3VzZS1qZGJjLWJyaWRnZV8kUEtHX1ZFUi0xX2FsbC5kZWJcbiAgICAgICAgICAgYXB0IGluc3RhbGwgLS1uby1pbnN0YWxsLXJlY29tbWVuZHMgLWYgLi9jbGlja2hvdXNlLWpkYmMtYnJpZGdlXyRQS0dfVkVSLTFfYWxsLmRlYlxuICAgICAgICAgICBjbGlja2hvdXNlLWpkYmMtYnJpZGdlICZcblxuICAgICAgICAgKiBbQ2VudE9TL1JIRUxdXG4gICAgICAgICAgIGV4cG9ydCBNVk5fVVJMPWh0dHBzOi8vcmVwbzEubWF2ZW4ub3JnL21hdmVuMi9ydS95YW5kZXgvY2xpY2tob3VzZS9jbGlja2hvdXNlLWpkYmMtYnJpZGdlXG4gICAgICAgICAgIGV4cG9ydCBQS0dfVkVSPSQoY3VybCAtc0wgJE1WTl9VUkwvbWF2ZW4tbWV0YWRhdGEueG1sIHwgZ3JlcCAnPHJlbGVhc2U+JyB8IHNlZCAtZSAnc3wuKj5cXCguKlxcKTwuKnxcXDF8JylcbiAgICAgICAgICAgd2dldCBodHRwczovL2dpdGh1Yi5jb20vQ2xpY2tIb3VzZS9jbGlja2hvdXNlLWpkYmMtYnJpZGdlL3JlbGVhc2VzL2Rvd25sb2FkL3YkUEtHX1ZFUi9jbGlja2hvdXNlLWpkYmMtYnJpZGdlLSRQS0dfVkVSLTEubm9hcmNoLnJwbVxuICAgICAgICAgICB5dW0gbG9jYWxpbnN0YWxsIC15IGNsaWNraG91c2UtamRiYy1icmlkZ2UtJFBLR19WRVItMS5ub2FyY2gucnBtXG4gICAgICAgICAgIGNsaWNraG91c2UtamRiYy1icmlkZ2UgJlxuXG4gICAgICAgICBQbGVhc2UgcmVmZXIgdG8gaHR0cHM6Ly9naXRodWIuY29tL0NsaWNrSG91c2UvY2xpY2tob3VzZS1qZGJjLWJyaWRnZSN1c2FnZSBmb3IgbW9yZSBpbmZvcm1hdGlvbi5cbiAgICBdXT5cbiAgICA8IS0tXG4gICAgPGpkYmNfYnJpZGdlPlxuICAgICAgICA8aG9zdD4xMjcuMC4wLjE8L2hvc3Q+XG4gICAgICAgIDxwb3J0PjkwMTk8L3BvcnQ+XG4gICAgPC9qZGJjX2JyaWRnZT5cbiAgICAtLT5cblxuICAgIDwhLS0gVGhlIGxpc3Qgb2YgaG9zdHMgYWxsb3dlZCB0byB1c2UgaW4gVVJMLXJlbGF0ZWQgc3RvcmFnZSBlbmdpbmVzIGFuZCB0YWJsZSBmdW5jdGlvbnMuXG4gICAgICAgIElmIHRoaXMgc2VjdGlvbiBpcyBub3QgcHJlc2VudCBpbiBjb25maWd1cmF0aW9uLCBhbGwgaG9zdHMgYXJlIGFsbG93ZWQuXG4gICAgLS0+XG4gICAgPCEtLTxyZW1vdGVfdXJsX2FsbG93X2hvc3RzPi0tPlxuICAgICAgICA8IS0tIEhvc3Qgc2hvdWxkIGJlIHNwZWNpZmllZCBleGFjdGx5IGFzIGluIFVSTC4gVGhlIG5hbWUgaXMgY2hlY2tlZCBiZWZvcmUgRE5TIHJlc29sdXRpb24uXG4gICAgICAgICAgICBFeGFtcGxlOiBcImNsaWNraG91c2UuY29tXCIsIFwiY2xpY2tob3VzZS5jb20uXCIgYW5kIFwid3d3LmNsaWNraG91c2UuY29tXCIgYXJlIGRpZmZlcmVudCBob3N0cy5cbiAgICAgICAgICAgICAgICAgICAgSWYgcG9ydCBpcyBleHBsaWNpdGx5IHNwZWNpZmllZCBpbiBVUkwsIHRoZSBob3N0OnBvcnQgaXMgY2hlY2tlZCBhcyBhIHdob2xlLlxuICAgICAgICAgICAgICAgICAgICBJZiBob3N0IHNwZWNpZmllZCBoZXJlIHdpdGhvdXQgcG9ydCwgYW55IHBvcnQgd2l0aCB0aGlzIGhvc3QgYWxsb3dlZC5cbiAgICAgICAgICAgICAgICAgICAgXCJjbGlja2hvdXNlLmNvbVwiIC0+IFwiY2xpY2tob3VzZS5jb206NDQzXCIsIFwiY2xpY2tob3VzZS5jb206ODBcIiBldGMuIGlzIGFsbG93ZWQsIGJ1dCBcImNsaWNraG91c2UuY29tOjgwXCIgLT4gb25seSBcImNsaWNraG91c2UuY29tOjgwXCIgaXMgYWxsb3dlZC5cbiAgICAgICAgICAgIElmIHRoZSBob3N0IGlzIHNwZWNpZmllZCBhcyBJUCBhZGRyZXNzLCBpdCBpcyBjaGVja2VkIGFzIHNwZWNpZmllZCBpbiBVUkwuIEV4YW1wbGU6IFwiWzJhMDI6NmI4OmE6OmFdXCIuXG4gICAgICAgICAgICBJZiB0aGVyZSBhcmUgcmVkaXJlY3RzIGFuZCBzdXBwb3J0IGZvciByZWRpcmVjdHMgaXMgZW5hYmxlZCwgZXZlcnkgcmVkaXJlY3QgKHRoZSBMb2NhdGlvbiBmaWVsZCkgaXMgY2hlY2tlZC5cbiAgICAgICAgICAgIEhvc3Qgc2hvdWxkIGJlIHNwZWNpZmllZCB1c2luZyB0aGUgaG9zdCB4bWwgdGFnOlxuICAgICAgICAgICAgICAgICAgICA8aG9zdD5jbGlja2hvdXNlLmNvbTwvaG9zdD5cbiAgICAgICAgLS0+XG5cbiAgICAgICAgPCEtLSBSZWd1bGFyIGV4cHJlc3Npb24gY2FuIGJlIHNwZWNpZmllZC4gUkUyIGVuZ2luZSBpcyB1c2VkIGZvciByZWdleHBzLlxuICAgICAgICAgICAgUmVnZXhwcyBhcmUgbm90IGFsaWduZWQ6IGRvbid0IGZvcmdldCB0byBhZGQgXiBhbmQgJC4gQWxzbyBkb24ndCBmb3JnZXQgdG8gZXNjYXBlIGRvdCAoLikgbWV0YWNoYXJhY3RlclxuICAgICAgICAgICAgKGZvcmdldHRpbmcgdG8gZG8gc28gaXMgYSBjb21tb24gc291cmNlIG9mIGVycm9yKS5cbiAgICAgICAgLS0+XG4gICAgPCEtLTwvcmVtb3RlX3VybF9hbGxvd19ob3N0cz4tLT5cblxuICAgIDwhLS0gSWYgZWxlbWVudCBoYXMgJ2luY2wnIGF0dHJpYnV0ZSwgdGhlbiBmb3IgaXQncyB2YWx1ZSB3aWxsIGJlIHVzZWQgY29ycmVzcG9uZGluZyBzdWJzdGl0dXRpb24gZnJvbSBhbm90aGVyIGZpbGUuXG4gICAgICAgICBCeSBkZWZhdWx0LCBwYXRoIHRvIGZpbGUgd2l0aCBzdWJzdGl0dXRpb25zIGlzIC9ldGMvbWV0cmlrYS54bWwuIEl0IGNvdWxkIGJlIGNoYW5nZWQgaW4gY29uZmlnIGluICdpbmNsdWRlX2Zyb20nIGVsZW1lbnQuXG4gICAgICAgICBWYWx1ZXMgZm9yIHN1YnN0aXR1dGlvbnMgYXJlIHNwZWNpZmllZCBpbiAvY2xpY2tob3VzZS9uYW1lX29mX3N1YnN0aXR1dGlvbiBlbGVtZW50cyBpbiB0aGF0IGZpbGUuXG4gICAgICAtLT5cblxuICAgIDwhLS0gU3Vic3RpdHV0aW9ucyBmb3IgcGFyYW1ldGVycyBvZiByZXBsaWNhdGVkIHRhYmxlcy5cbiAgICAgICAgICBPcHRpb25hbC4gSWYgeW91IGRvbid0IHVzZSByZXBsaWNhdGVkIHRhYmxlcywgeW91IGNvdWxkIG9taXQgdGhhdC5cblxuICAgICAgICAgU2VlIGh0dHBzOi8vY2xpY2tob3VzZS5jb20vZG9jcy9lbi9lbmdpbmVzL3RhYmxlLWVuZ2luZXMvbWVyZ2V0cmVlLWZhbWlseS9yZXBsaWNhdGlvbi8jY3JlYXRpbmctcmVwbGljYXRlZC10YWJsZXNcbiAgICAgIC0tPlxuXG4gICAgPG1hY3Jvcz5cbiAgICAgICAgPHNoYXJkPjAxPC9zaGFyZD5cbiAgICAgICAgPHJlcGxpY2E+ZXhhbXBsZTAxLTAxLTE8L3JlcGxpY2E+XG4gICAgPC9tYWNyb3M+XG5cblxuXG4gICAgPCEtLSBSZWxvYWRpbmcgaW50ZXJ2YWwgZm9yIGVtYmVkZGVkIGRpY3Rpb25hcmllcywgaW4gc2Vjb25kcy4gRGVmYXVsdDogMzYwMC4gLS0+XG4gICAgPGJ1aWx0aW5fZGljdGlvbmFyaWVzX3JlbG9hZF9pbnRlcnZhbD4zNjAwPC9idWlsdGluX2RpY3Rpb25hcmllc19yZWxvYWRfaW50ZXJ2YWw+XG5cblxuICAgIDwhLS0gTWF4aW11bSBzZXNzaW9uIHRpbWVvdXQsIGluIHNlY29uZHMuIERlZmF1bHQ6IDM2MDAuIC0tPlxuICAgIDxtYXhfc2Vzc2lvbl90aW1lb3V0PjM2MDA8L21heF9zZXNzaW9uX3RpbWVvdXQ+XG5cbiAgICA8IS0tIERlZmF1bHQgc2Vzc2lvbiB0aW1lb3V0LCBpbiBzZWNvbmRzLiBEZWZhdWx0OiA2MC4gLS0+XG4gICAgPGRlZmF1bHRfc2Vzc2lvbl90aW1lb3V0PjYwPC9kZWZhdWx0X3Nlc3Npb25fdGltZW91dD5cblxuICAgIDwhLS0gU2VuZGluZyBkYXRhIHRvIEdyYXBoaXRlIGZvciBtb25pdG9yaW5nLiBTZXZlcmFsIHNlY3Rpb25zIGNhbiBiZSBkZWZpbmVkLiAtLT5cbiAgICA8IS0tXG4gICAgICAgIGludGVydmFsIC0gc2VuZCBldmVyeSBYIHNlY29uZFxuICAgICAgICByb290X3BhdGggLSBwcmVmaXggZm9yIGtleXNcbiAgICAgICAgaG9zdG5hbWVfaW5fcGF0aCAtIGFwcGVuZCBob3N0bmFtZSB0byByb290X3BhdGggKGRlZmF1bHQgPSB0cnVlKVxuICAgICAgICBtZXRyaWNzIC0gc2VuZCBkYXRhIGZyb20gdGFibGUgc3lzdGVtLm1ldHJpY3NcbiAgICAgICAgZXZlbnRzIC0gc2VuZCBkYXRhIGZyb20gdGFibGUgc3lzdGVtLmV2ZW50c1xuICAgICAgICBhc3luY2hyb25vdXNfbWV0cmljcyAtIHNlbmQgZGF0YSBmcm9tIHRhYmxlIHN5c3RlbS5hc3luY2hyb25vdXNfbWV0cmljc1xuICAgIC0tPlxuICAgIDwhLS1cbiAgICA8Z3JhcGhpdGU+XG4gICAgICAgIDxob3N0PmxvY2FsaG9zdDwvaG9zdD5cbiAgICAgICAgPHBvcnQ+NDIwMDA8L3BvcnQ+XG4gICAgICAgIDx0aW1lb3V0PjAuMTwvdGltZW91dD5cbiAgICAgICAgPGludGVydmFsPjYwPC9pbnRlcnZhbD5cbiAgICAgICAgPHJvb3RfcGF0aD5vbmVfbWluPC9yb290X3BhdGg+XG4gICAgICAgIDxob3N0bmFtZV9pbl9wYXRoPnRydWU8L2hvc3RuYW1lX2luX3BhdGg+XG5cbiAgICAgICAgPG1ldHJpY3M+dHJ1ZTwvbWV0cmljcz5cbiAgICAgICAgPGV2ZW50cz50cnVlPC9ldmVudHM+XG4gICAgICAgIDxldmVudHNfY3VtdWxhdGl2ZT5mYWxzZTwvZXZlbnRzX2N1bXVsYXRpdmU+XG4gICAgICAgIDxhc3luY2hyb25vdXNfbWV0cmljcz50cnVlPC9hc3luY2hyb25vdXNfbWV0cmljcz5cbiAgICA8L2dyYXBoaXRlPlxuICAgIDxncmFwaGl0ZT5cbiAgICAgICAgPGhvc3Q+bG9jYWxob3N0PC9ob3N0PlxuICAgICAgICA8cG9ydD40MjAwMDwvcG9ydD5cbiAgICAgICAgPHRpbWVvdXQ+MC4xPC90aW1lb3V0PlxuICAgICAgICA8aW50ZXJ2YWw+MTwvaW50ZXJ2YWw+XG4gICAgICAgIDxyb290X3BhdGg+b25lX3NlYzwvcm9vdF9wYXRoPlxuXG4gICAgICAgIDxtZXRyaWNzPnRydWU8L21ldHJpY3M+XG4gICAgICAgIDxldmVudHM+dHJ1ZTwvZXZlbnRzPlxuICAgICAgICA8ZXZlbnRzX2N1bXVsYXRpdmU+ZmFsc2U8L2V2ZW50c19jdW11bGF0aXZlPlxuICAgICAgICA8YXN5bmNocm9ub3VzX21ldHJpY3M+ZmFsc2U8L2FzeW5jaHJvbm91c19tZXRyaWNzPlxuICAgIDwvZ3JhcGhpdGU+XG4gICAgLS0+XG5cbiAgICA8IS0tIFNlcnZlIGVuZHBvaW50IGZvciBQcm9tZXRoZXVzIG1vbml0b3JpbmcuIC0tPlxuICAgIDwhLS1cbiAgICAgICAgZW5kcG9pbnQgLSBtZXJ0aWNzIHBhdGggKHJlbGF0aXZlIHRvIHJvb3QsIHN0YXRyaW5nIHdpdGggXCIvXCIpXG4gICAgICAgIHBvcnQgLSBwb3J0IHRvIHNldHVwIHNlcnZlci4gSWYgbm90IGRlZmluZWQgb3IgMCB0aGFuIGh0dHBfcG9ydCB1c2VkXG4gICAgICAgIG1ldHJpY3MgLSBzZW5kIGRhdGEgZnJvbSB0YWJsZSBzeXN0ZW0ubWV0cmljc1xuICAgICAgICBldmVudHMgLSBzZW5kIGRhdGEgZnJvbSB0YWJsZSBzeXN0ZW0uZXZlbnRzXG4gICAgICAgIGFzeW5jaHJvbm91c19tZXRyaWNzIC0gc2VuZCBkYXRhIGZyb20gdGFibGUgc3lzdGVtLmFzeW5jaHJvbm91c19tZXRyaWNzXG4gICAgICAgIHN0YXR1c19pbmZvIC0gc2VuZCBkYXRhIGZyb20gZGlmZmVyZW50IGNvbXBvbmVudCBmcm9tIENILCBleDogRGljdGlvbmFyaWVzIHN0YXR1c1xuICAgIC0tPlxuXG4gICAgPHByb21ldGhldXM+XG4gICAgICAgIDxlbmRwb2ludD4vbWV0cmljczwvZW5kcG9pbnQ+XG4gICAgICAgIDxwb3J0PjkzNjM8L3BvcnQ+XG5cbiAgICAgICAgPG1ldHJpY3M+dHJ1ZTwvbWV0cmljcz5cbiAgICAgICAgPGV2ZW50cz50cnVlPC9ldmVudHM+XG4gICAgICAgIDxhc3luY2hyb25vdXNfbWV0cmljcz50cnVlPC9hc3luY2hyb25vdXNfbWV0cmljcz5cbiAgICAgICAgPHN0YXR1c19pbmZvPnRydWU8L3N0YXR1c19pbmZvPlxuICAgIDwvcHJvbWV0aGV1cz5cblxuICAgIDwhLS0gUXVlcnkgbG9nLiBVc2VkIG9ubHkgZm9yIHF1ZXJpZXMgd2l0aCBzZXR0aW5nIGxvZ19xdWVyaWVzID0gMS4gLS0+XG4gICAgPHF1ZXJ5X2xvZz5cbiAgICAgICAgPCEtLSBXaGF0IHRhYmxlIHRvIGluc2VydCBkYXRhLiBJZiB0YWJsZSBpcyBub3QgZXhpc3QsIGl0IHdpbGwgYmUgY3JlYXRlZC5cbiAgICAgICAgICAgICBXaGVuIHF1ZXJ5IGxvZyBzdHJ1Y3R1cmUgaXMgY2hhbmdlZCBhZnRlciBzeXN0ZW0gdXBkYXRlLFxuICAgICAgICAgICAgICB0aGVuIG9sZCB0YWJsZSB3aWxsIGJlIHJlbmFtZWQgYW5kIG5ldyB0YWJsZSB3aWxsIGJlIGNyZWF0ZWQgYXV0b21hdGljYWxseS5cbiAgICAgICAgLS0+XG4gICAgICAgIDxkYXRhYmFzZT5zeXN0ZW08L2RhdGFiYXNlPlxuICAgICAgICA8dGFibGU+cXVlcnlfbG9nPC90YWJsZT5cbiAgICAgICAgPCEtLVxuICAgICAgICAgICAgUEFSVElUSU9OIEJZIGV4cHI6IGh0dHBzOi8vY2xpY2tob3VzZS5jb20vZG9jcy9lbi90YWJsZV9lbmdpbmVzL21lcmdldHJlZS1mYW1pbHkvY3VzdG9tX3BhcnRpdGlvbmluZ19rZXkvXG4gICAgICAgICAgICBFeGFtcGxlOlxuICAgICAgICAgICAgICAgIGV2ZW50X2RhdGVcbiAgICAgICAgICAgICAgICB0b01vbmRheShldmVudF9kYXRlKVxuICAgICAgICAgICAgICAgIHRvWVlZWU1NKGV2ZW50X2RhdGUpXG4gICAgICAgICAgICAgICAgdG9TdGFydE9mSG91cihldmVudF90aW1lKVxuICAgICAgICAtLT5cbiAgICAgICAgPHBhcnRpdGlvbl9ieT50b1lZWVlNTShldmVudF9kYXRlKTwvcGFydGl0aW9uX2J5PlxuICAgICAgICA8IS0tXG4gICAgICAgICAgICBUYWJsZSBUVEwgc3BlY2lmaWNhdGlvbjogaHR0cHM6Ly9jbGlja2hvdXNlLmNvbS9kb2NzL2VuL2VuZ2luZXMvdGFibGUtZW5naW5lcy9tZXJnZXRyZWUtZmFtaWx5L21lcmdldHJlZS8jbWVyZ2V0cmVlLXRhYmxlLXR0bFxuICAgICAgICAgICAgRXhhbXBsZTpcbiAgICAgICAgICAgICAgICBldmVudF9kYXRlICsgSU5URVJWQUwgMSBXRUVLXG4gICAgICAgICAgICAgICAgZXZlbnRfZGF0ZSArIElOVEVSVkFMIDcgREFZIERFTEVURVxuICAgICAgICAgICAgICAgIGV2ZW50X2RhdGUgKyBJTlRFUlZBTCAyIFdFRUsgVE8gRElTSyAnYmJiJ1xuXG4gICAgICAgIDx0dGw+ZXZlbnRfZGF0ZSArIElOVEVSVkFMIDMwIERBWSBERUxFVEU8L3R0bD5cbiAgICAgICAgLS0+XG5cbiAgICAgICAgPCEtLSBJbnN0ZWFkIG9mIHBhcnRpdGlvbl9ieSwgeW91IGNhbiBwcm92aWRlIGZ1bGwgZW5naW5lIGV4cHJlc3Npb24gKHN0YXJ0aW5nIHdpdGggRU5HSU5FID0gKSB3aXRoIHBhcmFtZXRlcnMsXG4gICAgICAgICAgICAgRXhhbXBsZTogPGVuZ2luZT5FTkdJTkUgPSBNZXJnZVRyZWUgUEFSVElUSU9OIEJZIHRvWVlZWU1NKGV2ZW50X2RhdGUpIE9SREVSIEJZIChldmVudF9kYXRlLCBldmVudF90aW1lKSBTRVRUSU5HUyBpbmRleF9ncmFudWxhcml0eSA9IDEwMjQ8L2VuZ2luZT5cbiAgICAgICAgICAtLT5cblxuICAgICAgICA8IS0tIEludGVydmFsIG9mIGZsdXNoaW5nIGRhdGEuIC0tPlxuICAgICAgICA8Zmx1c2hfaW50ZXJ2YWxfbWlsbGlzZWNvbmRzPjc1MDA8L2ZsdXNoX2ludGVydmFsX21pbGxpc2Vjb25kcz5cbiAgICA8L3F1ZXJ5X2xvZz5cblxuICAgIDwhLS0gVHJhY2UgbG9nLiBTdG9yZXMgc3RhY2sgdHJhY2VzIGNvbGxlY3RlZCBieSBxdWVyeSBwcm9maWxlcnMuXG4gICAgICAgICBTZWUgcXVlcnlfcHJvZmlsZXJfcmVhbF90aW1lX3BlcmlvZF9ucyBhbmQgcXVlcnlfcHJvZmlsZXJfY3B1X3RpbWVfcGVyaW9kX25zIHNldHRpbmdzLiAtLT5cbiAgICA8dHJhY2VfbG9nPlxuICAgICAgICA8ZGF0YWJhc2U+c3lzdGVtPC9kYXRhYmFzZT5cbiAgICAgICAgPHRhYmxlPnRyYWNlX2xvZzwvdGFibGU+XG5cbiAgICAgICAgPHBhcnRpdGlvbl9ieT50b1lZWVlNTShldmVudF9kYXRlKTwvcGFydGl0aW9uX2J5PlxuICAgICAgICA8Zmx1c2hfaW50ZXJ2YWxfbWlsbGlzZWNvbmRzPjc1MDA8L2ZsdXNoX2ludGVydmFsX21pbGxpc2Vjb25kcz5cbiAgICA8L3RyYWNlX2xvZz5cblxuICAgIDwhLS0gUXVlcnkgdGhyZWFkIGxvZy4gSGFzIGluZm9ybWF0aW9uIGFib3V0IGFsbCB0aHJlYWRzIHBhcnRpY2lwYXRlZCBpbiBxdWVyeSBleGVjdXRpb24uXG4gICAgICAgICBVc2VkIG9ubHkgZm9yIHF1ZXJpZXMgd2l0aCBzZXR0aW5nIGxvZ19xdWVyeV90aHJlYWRzID0gMS4gLS0+XG4gICAgPHF1ZXJ5X3RocmVhZF9sb2c+XG4gICAgICAgIDxkYXRhYmFzZT5zeXN0ZW08L2RhdGFiYXNlPlxuICAgICAgICA8dGFibGU+cXVlcnlfdGhyZWFkX2xvZzwvdGFibGU+XG4gICAgICAgIDxwYXJ0aXRpb25fYnk+dG9ZWVlZTU0oZXZlbnRfZGF0ZSk8L3BhcnRpdGlvbl9ieT5cbiAgICAgICAgPGZsdXNoX2ludGVydmFsX21pbGxpc2Vjb25kcz43NTAwPC9mbHVzaF9pbnRlcnZhbF9taWxsaXNlY29uZHM+XG4gICAgPC9xdWVyeV90aHJlYWRfbG9nPlxuXG4gICAgPCEtLSBRdWVyeSB2aWV3cyBsb2cuIEhhcyBpbmZvcm1hdGlvbiBhYm91dCBhbGwgZGVwZW5kZW50IHZpZXdzIGFzc29jaWF0ZWQgd2l0aCBhIHF1ZXJ5LlxuICAgICAgICAgVXNlZCBvbmx5IGZvciBxdWVyaWVzIHdpdGggc2V0dGluZyBsb2dfcXVlcnlfdmlld3MgPSAxLiAtLT5cbiAgICA8cXVlcnlfdmlld3NfbG9nPlxuICAgICAgICA8ZGF0YWJhc2U+c3lzdGVtPC9kYXRhYmFzZT5cbiAgICAgICAgPHRhYmxlPnF1ZXJ5X3ZpZXdzX2xvZzwvdGFibGU+XG4gICAgICAgIDxwYXJ0aXRpb25fYnk+dG9ZWVlZTU0oZXZlbnRfZGF0ZSk8L3BhcnRpdGlvbl9ieT5cbiAgICAgICAgPGZsdXNoX2ludGVydmFsX21pbGxpc2Vjb25kcz43NTAwPC9mbHVzaF9pbnRlcnZhbF9taWxsaXNlY29uZHM+XG4gICAgPC9xdWVyeV92aWV3c19sb2c+XG5cbiAgICA8IS0tIFVuY29tbWVudCBpZiB1c2UgcGFydCBsb2cuXG4gICAgICAgICBQYXJ0IGxvZyBjb250YWlucyBpbmZvcm1hdGlvbiBhYm91dCBhbGwgYWN0aW9ucyB3aXRoIHBhcnRzIGluIE1lcmdlVHJlZSB0YWJsZXMgKGNyZWF0aW9uLCBkZWxldGlvbiwgbWVyZ2VzLCBkb3dubG9hZHMpLi0tPlxuICAgIDxwYXJ0X2xvZz5cbiAgICAgICAgPGRhdGFiYXNlPnN5c3RlbTwvZGF0YWJhc2U+XG4gICAgICAgIDx0YWJsZT5wYXJ0X2xvZzwvdGFibGU+XG4gICAgICAgIDxwYXJ0aXRpb25fYnk+dG9ZWVlZTU0oZXZlbnRfZGF0ZSk8L3BhcnRpdGlvbl9ieT5cbiAgICAgICAgPGZsdXNoX2ludGVydmFsX21pbGxpc2Vjb25kcz43NTAwPC9mbHVzaF9pbnRlcnZhbF9taWxsaXNlY29uZHM+XG4gICAgPC9wYXJ0X2xvZz5cblxuICAgIDwhLS0gVW5jb21tZW50IHRvIHdyaXRlIHRleHQgbG9nIGludG8gdGFibGUuXG4gICAgICAgICBUZXh0IGxvZyBjb250YWlucyBhbGwgaW5mb3JtYXRpb24gZnJvbSB1c3VhbCBzZXJ2ZXIgbG9nIGJ1dCBzdG9yZXMgaXQgaW4gc3RydWN0dXJlZCBhbmQgZWZmaWNpZW50IHdheS5cbiAgICAgICAgIFRoZSBsZXZlbCBvZiB0aGUgbWVzc2FnZXMgdGhhdCBnb2VzIHRvIHRoZSB0YWJsZSBjYW4gYmUgbGltaXRlZCAoPGxldmVsPiksIGlmIG5vdCBzcGVjaWZpZWQgYWxsIG1lc3NhZ2VzIHdpbGwgZ28gdG8gdGhlIHRhYmxlLlxuICAgIDx0ZXh0X2xvZz5cbiAgICAgICAgPGRhdGFiYXNlPnN5c3RlbTwvZGF0YWJhc2U+XG4gICAgICAgIDx0YWJsZT50ZXh0X2xvZzwvdGFibGU+XG4gICAgICAgIDxmbHVzaF9pbnRlcnZhbF9taWxsaXNlY29uZHM+NzUwMDwvZmx1c2hfaW50ZXJ2YWxfbWlsbGlzZWNvbmRzPlxuICAgICAgICA8bGV2ZWw+PC9sZXZlbD5cbiAgICA8L3RleHRfbG9nPlxuICAgIC0tPlxuXG4gICAgPCEtLSBNZXRyaWMgbG9nIGNvbnRhaW5zIHJvd3Mgd2l0aCBjdXJyZW50IHZhbHVlcyBvZiBQcm9maWxlRXZlbnRzLCBDdXJyZW50TWV0cmljcyBjb2xsZWN0ZWQgd2l0aCBcImNvbGxlY3RfaW50ZXJ2YWxfbWlsbGlzZWNvbmRzXCIgaW50ZXJ2YWwuIC0tPlxuICAgIDxtZXRyaWNfbG9nPlxuICAgICAgICA8ZGF0YWJhc2U+c3lzdGVtPC9kYXRhYmFzZT5cbiAgICAgICAgPHRhYmxlPm1ldHJpY19sb2c8L3RhYmxlPlxuICAgICAgICA8Zmx1c2hfaW50ZXJ2YWxfbWlsbGlzZWNvbmRzPjc1MDA8L2ZsdXNoX2ludGVydmFsX21pbGxpc2Vjb25kcz5cbiAgICAgICAgPGNvbGxlY3RfaW50ZXJ2YWxfbWlsbGlzZWNvbmRzPjEwMDA8L2NvbGxlY3RfaW50ZXJ2YWxfbWlsbGlzZWNvbmRzPlxuICAgIDwvbWV0cmljX2xvZz5cblxuICAgIDwhLS1cbiAgICAgICAgQXN5bmNocm9ub3VzIG1ldHJpYyBsb2cgY29udGFpbnMgdmFsdWVzIG9mIG1ldHJpY3MgZnJvbVxuICAgICAgICBzeXN0ZW0uYXN5bmNocm9ub3VzX21ldHJpY3MuXG4gICAgLS0+XG4gICAgPGFzeW5jaHJvbm91c19tZXRyaWNfbG9nPlxuICAgICAgICA8ZGF0YWJhc2U+c3lzdGVtPC9kYXRhYmFzZT5cbiAgICAgICAgPHRhYmxlPmFzeW5jaHJvbm91c19tZXRyaWNfbG9nPC90YWJsZT5cbiAgICAgICAgPCEtLVxuICAgICAgICAgICAgQXN5bmNocm9ub3VzIG1ldHJpY3MgYXJlIHVwZGF0ZWQgb25jZSBhIG1pbnV0ZSwgc28gdGhlcmUgaXNcbiAgICAgICAgICAgIG5vIG5lZWQgdG8gZmx1c2ggbW9yZSBvZnRlbi5cbiAgICAgICAgLS0+XG4gICAgICAgIDxmbHVzaF9pbnRlcnZhbF9taWxsaXNlY29uZHM+NzAwMDwvZmx1c2hfaW50ZXJ2YWxfbWlsbGlzZWNvbmRzPlxuICAgIDwvYXN5bmNocm9ub3VzX21ldHJpY19sb2c+XG5cbiAgICA8IS0tXG4gICAgICAgIE9wZW5UZWxlbWV0cnkgbG9nIGNvbnRhaW5zIE9wZW5UZWxlbWV0cnkgdHJhY2Ugc3BhbnMuXG4gICAgLS0+XG4gICAgPG9wZW50ZWxlbWV0cnlfc3Bhbl9sb2c+XG4gICAgICAgIDwhLS1cbiAgICAgICAgICAgIFRoZSBkZWZhdWx0IHRhYmxlIGNyZWF0aW9uIGNvZGUgaXMgaW5zdWZmaWNpZW50LCB0aGlzIDxlbmdpbmU+IHNwZWNcbiAgICAgICAgICAgIGlzIGEgd29ya2Fyb3VuZC4gVGhlcmUgaXMgbm8gJ2V2ZW50X3RpbWUnIGZvciB0aGlzIGxvZywgYnV0IHR3byB0aW1lcyxcbiAgICAgICAgICAgIHN0YXJ0IGFuZCBmaW5pc2guIEl0IGlzIHNvcnRlZCBieSBmaW5pc2ggdGltZSwgdG8gYXZvaWQgaW5zZXJ0aW5nXG4gICAgICAgICAgICBkYXRhIHRvbyBmYXIgYXdheSBpbiB0aGUgcGFzdCAocHJvYmFibHkgd2UgY2FuIHNvbWV0aW1lcyBpbnNlcnQgYSBzcGFuXG4gICAgICAgICAgICB0aGF0IGlzIHNlY29uZHMgZWFybGllciB0aGFuIHRoZSBsYXN0IHNwYW4gaW4gdGhlIHRhYmxlLCBkdWUgdG8gYSByYWNlXG4gICAgICAgICAgICBiZXR3ZWVuIHNldmVyYWwgc3BhbnMgaW5zZXJ0ZWQgaW4gcGFyYWxsZWwpLiBUaGlzIGdpdmVzIHRoZSBzcGFucyBhXG4gICAgICAgICAgICBnbG9iYWwgb3JkZXIgdGhhdCB3ZSBjYW4gdXNlIHRvIGUuZy4gcmV0cnkgaW5zZXJ0aW9uIGludG8gc29tZSBleHRlcm5hbFxuICAgICAgICAgICAgc3lzdGVtLlxuICAgICAgICAtLT5cbiAgICAgICAgPGVuZ2luZT5cbiAgICAgICAgICAgIGVuZ2luZSBNZXJnZVRyZWVcbiAgICAgICAgICAgIHBhcnRpdGlvbiBieSB0b1lZWVlNTShmaW5pc2hfZGF0ZSlcbiAgICAgICAgICAgIG9yZGVyIGJ5IChmaW5pc2hfZGF0ZSwgZmluaXNoX3RpbWVfdXMsIHRyYWNlX2lkKVxuICAgICAgICA8L2VuZ2luZT5cbiAgICAgICAgPGRhdGFiYXNlPnN5c3RlbTwvZGF0YWJhc2U+XG4gICAgICAgIDx0YWJsZT5vcGVudGVsZW1ldHJ5X3NwYW5fbG9nPC90YWJsZT5cbiAgICAgICAgPGZsdXNoX2ludGVydmFsX21pbGxpc2Vjb25kcz43NTAwPC9mbHVzaF9pbnRlcnZhbF9taWxsaXNlY29uZHM+XG4gICAgPC9vcGVudGVsZW1ldHJ5X3NwYW5fbG9nPlxuXG5cbiAgICA8IS0tIENyYXNoIGxvZy4gU3RvcmVzIHN0YWNrIHRyYWNlcyBmb3IgZmF0YWwgZXJyb3JzLlxuICAgICAgICAgVGhpcyB0YWJsZSBpcyBub3JtYWxseSBlbXB0eS4gLS0+XG4gICAgPGNyYXNoX2xvZz5cbiAgICAgICAgPGRhdGFiYXNlPnN5c3RlbTwvZGF0YWJhc2U+XG4gICAgICAgIDx0YWJsZT5jcmFzaF9sb2c8L3RhYmxlPlxuXG4gICAgICAgIDxwYXJ0aXRpb25fYnkgLz5cbiAgICAgICAgPGZsdXNoX2ludGVydmFsX21pbGxpc2Vjb25kcz4xMDAwPC9mbHVzaF9pbnRlcnZhbF9taWxsaXNlY29uZHM+XG4gICAgPC9jcmFzaF9sb2c+XG5cbiAgICA8IS0tIFNlc3Npb24gbG9nLiBTdG9yZXMgdXNlciBsb2cgaW4gKHN1Y2Nlc3NmdWwgb3Igbm90KSBhbmQgbG9nIG91dCBldmVudHMuXG5cbiAgICAgICAgTm90ZTogc2Vzc2lvbiBsb2cgaGFzIGtub3duIHNlY3VyaXR5IGlzc3VlcyBhbmQgc2hvdWxkIG5vdCBiZSB1c2VkIGluIHByb2R1Y3Rpb24uXG4gICAgLS0+XG4gICAgPCEtLSA8c2Vzc2lvbl9sb2c+XG4gICAgICAgIDxkYXRhYmFzZT5zeXN0ZW08L2RhdGFiYXNlPlxuICAgICAgICA8dGFibGU+c2Vzc2lvbl9sb2c8L3RhYmxlPlxuXG4gICAgICAgIDxwYXJ0aXRpb25fYnk+dG9ZWVlZTU0oZXZlbnRfZGF0ZSk8L3BhcnRpdGlvbl9ieT5cbiAgICAgICAgPGZsdXNoX2ludGVydmFsX21pbGxpc2Vjb25kcz43NTAwPC9mbHVzaF9pbnRlcnZhbF9taWxsaXNlY29uZHM+XG4gICAgPC9zZXNzaW9uX2xvZz4gLS0+XG5cbiAgICA8IS0tIFByb2ZpbGluZyBvbiBQcm9jZXNzb3JzIGxldmVsLiAtLT5cbiAgICA8cHJvY2Vzc29yc19wcm9maWxlX2xvZz5cbiAgICAgICAgPGRhdGFiYXNlPnN5c3RlbTwvZGF0YWJhc2U+XG4gICAgICAgIDx0YWJsZT5wcm9jZXNzb3JzX3Byb2ZpbGVfbG9nPC90YWJsZT5cblxuICAgICAgICA8cGFydGl0aW9uX2J5PnRvWVlZWU1NKGV2ZW50X2RhdGUpPC9wYXJ0aXRpb25fYnk+XG4gICAgICAgIDxmbHVzaF9pbnRlcnZhbF9taWxsaXNlY29uZHM+NzUwMDwvZmx1c2hfaW50ZXJ2YWxfbWlsbGlzZWNvbmRzPlxuICAgIDwvcHJvY2Vzc29yc19wcm9maWxlX2xvZz5cblxuICAgIDwhLS0gPHRvcF9sZXZlbF9kb21haW5zX3BhdGg+L3Zhci9saWIvY2xpY2tob3VzZS90b3BfbGV2ZWxfZG9tYWlucy88L3RvcF9sZXZlbF9kb21haW5zX3BhdGg+IC0tPlxuICAgIDwhLS0gQ3VzdG9tIFRMRCBsaXN0cy5cbiAgICAgICAgIEZvcm1hdDogPG5hbWU+L3BhdGgvdG8vZmlsZTwvbmFtZT5cblxuICAgICAgICAgQ2hhbmdlcyB3aWxsIG5vdCBiZSBhcHBsaWVkIHcvbyBzZXJ2ZXIgcmVzdGFydC5cbiAgICAgICAgIFBhdGggdG8gdGhlIGxpc3QgaXMgdW5kZXIgdG9wX2xldmVsX2RvbWFpbnNfcGF0aCAoc2VlIGFib3ZlKS5cbiAgICAtLT5cbiAgICA8dG9wX2xldmVsX2RvbWFpbnNfbGlzdHM+XG4gICAgICAgIDwhLS1cbiAgICAgICAgPHB1YmxpY19zdWZmaXhfbGlzdD4vcGF0aC90by9wdWJsaWNfc3VmZml4X2xpc3QuZGF0PC9wdWJsaWNfc3VmZml4X2xpc3Q+XG4gICAgICAgIC0tPlxuICAgIDwvdG9wX2xldmVsX2RvbWFpbnNfbGlzdHM+XG5cbiAgICA8IS0tIENvbmZpZ3VyYXRpb24gb2YgZXh0ZXJuYWwgZGljdGlvbmFyaWVzLiBTZWU6XG4gICAgICAgICBodHRwczovL2NsaWNraG91c2UuY29tL2RvY3MvZW4vc3FsLXJlZmVyZW5jZS9kaWN0aW9uYXJpZXMvZXh0ZXJuYWwtZGljdGlvbmFyaWVzL2V4dGVybmFsLWRpY3RzXG4gICAgLS0+XG4gICAgPGRpY3Rpb25hcmllc19jb25maWc+Kl9kaWN0aW9uYXJ5LnhtbDwvZGljdGlvbmFyaWVzX2NvbmZpZz5cblxuICAgIDwhLS0gQ29uZmlndXJhdGlvbiBvZiB1c2VyIGRlZmluZWQgZXhlY3V0YWJsZSBmdW5jdGlvbnMgLS0+XG4gICAgPHVzZXJfZGVmaW5lZF9leGVjdXRhYmxlX2Z1bmN0aW9uc19jb25maWc+KmZ1bmN0aW9uLnhtbDwvdXNlcl9kZWZpbmVkX2V4ZWN1dGFibGVfZnVuY3Rpb25zX2NvbmZpZz5cbiAgICA8dXNlcl9zY3JpcHRzX3BhdGg+L3Zhci9saWIvY2xpY2tob3VzZS91c2VyX3NjcmlwdHMvPC91c2VyX3NjcmlwdHNfcGF0aD5cblxuICAgIDwhLS0gVW5jb21tZW50IGlmIHlvdSB3YW50IGRhdGEgdG8gYmUgY29tcHJlc3NlZCAzMC0xMDAlIGJldHRlci5cbiAgICAgICAgIERvbid0IGRvIHRoYXQgaWYgeW91IGp1c3Qgc3RhcnRlZCB1c2luZyBDbGlja0hvdXNlLlxuICAgICAgLS0+XG4gICAgPCEtLVxuICAgIDxjb21wcmVzc2lvbj5cbiAgICAgICAgPCEtIC0gU2V0IG9mIHZhcmlhbnRzLiBDaGVja2VkIGluIG9yZGVyLiBMYXN0IG1hdGNoaW5nIGNhc2Ugd2lucy4gSWYgbm90aGluZyBtYXRjaGVzLCBsejQgd2lsbCBiZSB1c2VkLiAtIC0+XG4gICAgICAgIDxjYXNlPlxuXG4gICAgICAgICAgICA8IS0gLSBDb25kaXRpb25zLiBBbGwgbXVzdCBiZSBzYXRpc2ZpZWQuIFNvbWUgY29uZGl0aW9ucyBtYXkgYmUgb21pdHRlZC4gLSAtPlxuICAgICAgICAgICAgPG1pbl9wYXJ0X3NpemU+MTAwMDAwMDAwMDA8L21pbl9wYXJ0X3NpemU+ICAgICAgICA8IS0gLSBNaW4gcGFydCBzaXplIGluIGJ5dGVzLiAtIC0+XG4gICAgICAgICAgICA8bWluX3BhcnRfc2l6ZV9yYXRpbz4wLjAxPC9taW5fcGFydF9zaXplX3JhdGlvPiAgIDwhLSAtIE1pbiBzaXplIG9mIHBhcnQgcmVsYXRpdmUgdG8gd2hvbGUgdGFibGUgc2l6ZS4gLSAtPlxuXG4gICAgICAgICAgICA8IS0gLSBXaGF0IGNvbXByZXNzaW9uIG1ldGhvZCB0byB1c2UuIC0gLT5cbiAgICAgICAgICAgIDxtZXRob2Q+enN0ZDwvbWV0aG9kPlxuICAgICAgICA8L2Nhc2U+XG4gICAgPC9jb21wcmVzc2lvbj5cbiAgICAtLT5cblxuICAgIDwhLS0gQ29uZmlndXJhdGlvbiBvZiBlbmNyeXB0aW9uLiBUaGUgc2VydmVyIGV4ZWN1dGVzIGEgY29tbWFuZCB0b1xuICAgICAgICAgb2J0YWluIGFuIGVuY3J5cHRpb24ga2V5IGF0IHN0YXJ0dXAgaWYgc3VjaCBhIGNvbW1hbmQgaXNcbiAgICAgICAgIGRlZmluZWQsIG9yIGVuY3J5cHRpb24gY29kZWNzIHdpbGwgYmUgZGlzYWJsZWQgb3RoZXJ3aXNlLiBUaGVcbiAgICAgICAgIGNvbW1hbmQgaXMgZXhlY3V0ZWQgdGhyb3VnaCAvYmluL3NoIGFuZCBpcyBleHBlY3RlZCB0byB3cml0ZVxuICAgICAgICAgYSBCYXNlNjQtZW5jb2RlZCBrZXkgdG8gdGhlIHN0ZG91dC4gLS0+XG4gICAgPGVuY3J5cHRpb25fY29kZWNzPlxuICAgICAgICA8IS0tIGFlc18xMjhfZ2NtX3NpdiAtLT5cbiAgICAgICAgICAgIDwhLS0gRXhhbXBsZSBvZiBnZXR0aW5nIGhleCBrZXkgZnJvbSBlbnYgLS0+XG4gICAgICAgICAgICA8IS0tIHRoZSBjb2RlIHNob3VsZCB1c2UgdGhpcyBrZXkgYW5kIHRocm93IGFuIGV4Y2VwdGlvbiBpZiBpdHMgbGVuZ3RoIGlzIG5vdCAxNiBieXRlcyAtLT5cbiAgICAgICAgICAgIDwhLS1rZXlfaGV4IGZyb21fZW52PVwiLi4uXCI+PC9rZXlfaGV4IC0tPlxuXG4gICAgICAgICAgICA8IS0tIEV4YW1wbGUgb2YgbXVsdGlwbGUgaGV4IGtleXMuIFRoZXkgY2FuIGJlIGltcG9ydGVkIGZyb20gZW52IG9yIGJlIHdyaXR0ZW4gZG93biBpbiBjb25maWctLT5cbiAgICAgICAgICAgIDwhLS0gdGhlIGNvZGUgc2hvdWxkIHVzZSB0aGVzZSBrZXlzIGFuZCB0aHJvdyBhbiBleGNlcHRpb24gaWYgdGhlaXIgbGVuZ3RoIGlzIG5vdCAxNiBieXRlcyAtLT5cbiAgICAgICAgICAgIDwhLS0ga2V5X2hleCBpZD1cIjBcIj4uLi48L2tleV9oZXggLS0+XG4gICAgICAgICAgICA8IS0tIGtleV9oZXggaWQ9XCIxXCIgZnJvbV9lbnY9XCIuLlwiPjwva2V5X2hleCAtLT5cbiAgICAgICAgICAgIDwhLS0ga2V5X2hleCBpZD1cIjJcIj4uLi48L2tleV9oZXggLS0+XG4gICAgICAgICAgICA8IS0tIGN1cnJlbnRfa2V5X2lkPjI8L2N1cnJlbnRfa2V5X2lkIC0tPlxuXG4gICAgICAgICAgICA8IS0tIEV4YW1wbGUgb2YgZ2V0dGluZyBoZXgga2V5IGZyb20gY29uZmlnIC0tPlxuICAgICAgICAgICAgPCEtLSB0aGUgY29kZSBzaG91bGQgdXNlIHRoaXMga2V5IGFuZCB0aHJvdyBhbiBleGNlcHRpb24gaWYgaXRzIGxlbmd0aCBpcyBub3QgMTYgYnl0ZXMgLS0+XG4gICAgICAgICAgICA8IS0tIGtleT4uLi48L2tleSAtLT5cblxuICAgICAgICAgICAgPCEtLSBleGFtcGxlIG9mIGFkZGluZyBub25jZSAtLT5cbiAgICAgICAgICAgIDwhLS0gbm9uY2U+Li4uPC9ub25jZSAtLT5cblxuICAgICAgICA8IS0tIC9hZXNfMTI4X2djbV9zaXYgLS0+XG4gICAgPC9lbmNyeXB0aW9uX2NvZGVjcz5cblxuICAgIDwhLS0gQWxsb3cgdG8gZXhlY3V0ZSBkaXN0cmlidXRlZCBEREwgcXVlcmllcyAoQ1JFQVRFLCBEUk9QLCBBTFRFUiwgUkVOQU1FKSBvbiBjbHVzdGVyLlxuICAgICAgICAgV29ya3Mgb25seSBpZiBab29LZWVwZXIgaXMgZW5hYmxlZC4gQ29tbWVudCBpdCBpZiBzdWNoIGZ1bmN0aW9uYWxpdHkgaXNuJ3QgcmVxdWlyZWQuIC0tPlxuICAgIDxkaXN0cmlidXRlZF9kZGw+XG4gICAgICAgIDwhLS0gUGF0aCBpbiBab29LZWVwZXIgdG8gcXVldWUgd2l0aCBEREwgcXVlcmllcyAtLT5cbiAgICAgICAgPHBhdGg+L2NsaWNraG91c2UvdGFza19xdWV1ZS9kZGw8L3BhdGg+XG5cbiAgICAgICAgPCEtLSBTZXR0aW5ncyBmcm9tIHRoaXMgcHJvZmlsZSB3aWxsIGJlIHVzZWQgdG8gZXhlY3V0ZSBEREwgcXVlcmllcyAtLT5cbiAgICAgICAgPCEtLSA8cHJvZmlsZT5kZWZhdWx0PC9wcm9maWxlPiAtLT5cblxuICAgICAgICA8IS0tIENvbnRyb2xzIGhvdyBtdWNoIE9OIENMVVNURVIgcXVlcmllcyBjYW4gYmUgcnVuIHNpbXVsdGFuZW91c2x5LiAtLT5cbiAgICAgICAgPCEtLSA8cG9vbF9zaXplPjE8L3Bvb2xfc2l6ZT4gLS0+XG5cbiAgICAgICAgPCEtLVxuICAgICAgICAgICAgIENsZWFudXAgc2V0dGluZ3MgKGFjdGl2ZSB0YXNrcyB3aWxsIG5vdCBiZSByZW1vdmVkKVxuICAgICAgICAtLT5cblxuICAgICAgICA8IS0tIENvbnRyb2xzIHRhc2sgVFRMIChkZWZhdWx0IDEgd2VlaykgLS0+XG4gICAgICAgIDwhLS0gPHRhc2tfbWF4X2xpZmV0aW1lPjYwNDgwMDwvdGFza19tYXhfbGlmZXRpbWU+IC0tPlxuXG4gICAgICAgIDwhLS0gQ29udHJvbHMgaG93IG9mdGVuIGNsZWFudXAgc2hvdWxkIGJlIHBlcmZvcm1lZCAoaW4gc2Vjb25kcykgLS0+XG4gICAgICAgIDwhLS0gPGNsZWFudXBfZGVsYXlfcGVyaW9kPjYwPC9jbGVhbnVwX2RlbGF5X3BlcmlvZD4gLS0+XG5cbiAgICAgICAgPCEtLSBDb250cm9scyBob3cgbWFueSB0YXNrcyBjb3VsZCBiZSBpbiB0aGUgcXVldWUgLS0+XG4gICAgICAgIDwhLS0gPG1heF90YXNrc19pbl9xdWV1ZT4xMDAwPC9tYXhfdGFza3NfaW5fcXVldWU+IC0tPlxuICAgIDwvZGlzdHJpYnV0ZWRfZGRsPlxuXG4gICAgPCEtLSBTZXR0aW5ncyB0byBmaW5lIHR1bmUgTWVyZ2VUcmVlIHRhYmxlcy4gU2VlIGRvY3VtZW50YXRpb24gaW4gc291cmNlIGNvZGUsIGluIE1lcmdlVHJlZVNldHRpbmdzLmggLS0+XG4gICAgPCEtLVxuICAgIDxtZXJnZV90cmVlPlxuICAgICAgICA8bWF4X3N1c3BpY2lvdXNfYnJva2VuX3BhcnRzPjU8L21heF9zdXNwaWNpb3VzX2Jyb2tlbl9wYXJ0cz5cbiAgICA8L21lcmdlX3RyZWU+XG4gICAgLS0+XG5cbiAgICA8IS0tIFByb3RlY3Rpb24gZnJvbSBhY2NpZGVudGFsIERST1AuXG4gICAgICAgICBJZiBzaXplIG9mIGEgTWVyZ2VUcmVlIHRhYmxlIGlzIGdyZWF0ZXIgdGhhbiBtYXhfdGFibGVfc2l6ZV90b19kcm9wIChpbiBieXRlcykgdGhhbiB0YWJsZSBjb3VsZCBub3QgYmUgZHJvcHBlZCB3aXRoIGFueSBEUk9QIHF1ZXJ5LlxuICAgICAgICAgSWYgeW91IHdhbnQgZG8gZGVsZXRlIG9uZSB0YWJsZSBhbmQgZG9uJ3Qgd2FudCB0byBjaGFuZ2UgY2xpY2tob3VzZS1zZXJ2ZXIgY29uZmlnLCB5b3UgY291bGQgY3JlYXRlIHNwZWNpYWwgZmlsZSA8Y2xpY2tob3VzZS1wYXRoPi9mbGFncy9mb3JjZV9kcm9wX3RhYmxlIGFuZCBtYWtlIERST1Agb25jZS5cbiAgICAgICAgIEJ5IGRlZmF1bHQgbWF4X3RhYmxlX3NpemVfdG9fZHJvcCBpcyA1MEdCOyBtYXhfdGFibGVfc2l6ZV90b19kcm9wPTAgYWxsb3dzIHRvIERST1AgYW55IHRhYmxlcy5cbiAgICAgICAgIFRoZSBzYW1lIGZvciBtYXhfcGFydGl0aW9uX3NpemVfdG9fZHJvcC5cbiAgICAgICAgIFVuY29tbWVudCB0byBkaXNhYmxlIHByb3RlY3Rpb24uXG4gICAgLS0+XG4gICAgPCEtLSA8bWF4X3RhYmxlX3NpemVfdG9fZHJvcD4wPC9tYXhfdGFibGVfc2l6ZV90b19kcm9wPiAtLT5cbiAgICA8IS0tIDxtYXhfcGFydGl0aW9uX3NpemVfdG9fZHJvcD4wPC9tYXhfcGFydGl0aW9uX3NpemVfdG9fZHJvcD4gLS0+XG5cbiAgICA8IS0tIEV4YW1wbGUgb2YgcGFyYW1ldGVycyBmb3IgR3JhcGhpdGVNZXJnZVRyZWUgdGFibGUgZW5naW5lIC0tPlxuICAgIDxncmFwaGl0ZV9yb2xsdXBfZXhhbXBsZT5cbiAgICAgICAgPHBhdHRlcm4+XG4gICAgICAgICAgICA8cmVnZXhwPmNsaWNrX2Nvc3Q8L3JlZ2V4cD5cbiAgICAgICAgICAgIDxmdW5jdGlvbj5hbnk8L2Z1bmN0aW9uPlxuICAgICAgICAgICAgPHJldGVudGlvbj5cbiAgICAgICAgICAgICAgICA8YWdlPjA8L2FnZT5cbiAgICAgICAgICAgICAgICA8cHJlY2lzaW9uPjM2MDA8L3ByZWNpc2lvbj5cbiAgICAgICAgICAgIDwvcmV0ZW50aW9uPlxuICAgICAgICAgICAgPHJldGVudGlvbj5cbiAgICAgICAgICAgICAgICA8YWdlPjg2NDAwPC9hZ2U+XG4gICAgICAgICAgICAgICAgPHByZWNpc2lvbj42MDwvcHJlY2lzaW9uPlxuICAgICAgICAgICAgPC9yZXRlbnRpb24+XG4gICAgICAgIDwvcGF0dGVybj5cbiAgICAgICAgPGRlZmF1bHQ+XG4gICAgICAgICAgICA8ZnVuY3Rpb24+bWF4PC9mdW5jdGlvbj5cbiAgICAgICAgICAgIDxyZXRlbnRpb24+XG4gICAgICAgICAgICAgICAgPGFnZT4wPC9hZ2U+XG4gICAgICAgICAgICAgICAgPHByZWNpc2lvbj42MDwvcHJlY2lzaW9uPlxuICAgICAgICAgICAgPC9yZXRlbnRpb24+XG4gICAgICAgICAgICA8cmV0ZW50aW9uPlxuICAgICAgICAgICAgICAgIDxhZ2U+MzYwMDwvYWdlPlxuICAgICAgICAgICAgICAgIDxwcmVjaXNpb24+MzAwPC9wcmVjaXNpb24+XG4gICAgICAgICAgICA8L3JldGVudGlvbj5cbiAgICAgICAgICAgIDxyZXRlbnRpb24+XG4gICAgICAgICAgICAgICAgPGFnZT44NjQwMDwvYWdlPlxuICAgICAgICAgICAgICAgIDxwcmVjaXNpb24+MzYwMDwvcHJlY2lzaW9uPlxuICAgICAgICAgICAgPC9yZXRlbnRpb24+XG4gICAgICAgIDwvZGVmYXVsdD5cbiAgICA8L2dyYXBoaXRlX3JvbGx1cF9leGFtcGxlPlxuXG4gICAgPCEtLSBEaXJlY3RvcnkgaW4gPGNsaWNraG91c2UtcGF0aD4gY29udGFpbmluZyBzY2hlbWEgZmlsZXMgZm9yIHZhcmlvdXMgaW5wdXQgZm9ybWF0cy5cbiAgICAgICAgIFRoZSBkaXJlY3Rvcnkgd2lsbCBiZSBjcmVhdGVkIGlmIGl0IGRvZXNuJ3QgZXhpc3QuXG4gICAgICAtLT5cbiAgICA8Zm9ybWF0X3NjaGVtYV9wYXRoPi92YXIvbGliL2NsaWNraG91c2UvZm9ybWF0X3NjaGVtYXMvPC9mb3JtYXRfc2NoZW1hX3BhdGg+XG5cbiAgICA8IS0tIERlZmF1bHQgcXVlcnkgbWFza2luZyBydWxlcywgbWF0Y2hpbmcgbGluZXMgd291bGQgYmUgcmVwbGFjZWQgd2l0aCBzb21ldGhpbmcgZWxzZSBpbiB0aGUgbG9nc1xuICAgICAgICAoYm90aCB0ZXh0IGxvZ3MgYW5kIHN5c3RlbS5xdWVyeV9sb2cpLlxuICAgICAgICBuYW1lIC0gbmFtZSBmb3IgdGhlIHJ1bGUgKG9wdGlvbmFsKVxuICAgICAgICByZWdleHAgLSBSRTIgY29tcGF0aWJsZSByZWd1bGFyIGV4cHJlc3Npb24gKG1hbmRhdG9yeSlcbiAgICAgICAgcmVwbGFjZSAtIHN1YnN0aXR1dGlvbiBzdHJpbmcgZm9yIHNlbnNpdGl2ZSBkYXRhIChvcHRpb25hbCwgYnkgZGVmYXVsdCAtIHNpeCBhc3Rlcmlza3MpXG4gICAgLS0+XG4gICAgPHF1ZXJ5X21hc2tpbmdfcnVsZXM+XG4gICAgICAgIDxydWxlPlxuICAgICAgICAgICAgPG5hbWU+aGlkZSBlbmNyeXB0L2RlY3J5cHQgYXJndW1lbnRzPC9uYW1lPlxuICAgICAgICAgICAgPHJlZ2V4cD4oKD86YWVzXyk/KD86ZW5jcnlwdHxkZWNyeXB0KSg/Ol9teXNxbCk/KVxccypcXChcXHMqKD86Jyg/OlxcXFwnfC4pKyd8Lio/KVxccypcXCk8L3JlZ2V4cD5cbiAgICAgICAgICAgIDwhLS0gb3IgbW9yZSBzZWN1cmUsIGJ1dCBhbHNvIG1vcmUgaW52YXNpdmU6XG4gICAgICAgICAgICAgICAgKGFlc19cXHcrKVxccypcXCguKlxcKVxuICAgICAgICAgICAgLS0+XG4gICAgICAgICAgICA8cmVwbGFjZT5cXDEoPz8/KTwvcmVwbGFjZT5cbiAgICAgICAgPC9ydWxlPlxuICAgIDwvcXVlcnlfbWFza2luZ19ydWxlcz5cblxuICAgIDwhLS0gVW5jb21tZW50IHRvIHVzZSBjdXN0b20gaHR0cCBoYW5kbGVycy5cbiAgICAgICAgcnVsZXMgYXJlIGNoZWNrZWQgZnJvbSB0b3AgdG8gYm90dG9tLCBmaXJzdCBtYXRjaCBydW5zIHRoZSBoYW5kbGVyXG4gICAgICAgICAgICB1cmwgLSB0byBtYXRjaCByZXF1ZXN0IFVSTCwgeW91IGNhbiB1c2UgJ3JlZ2V4OicgcHJlZml4IHRvIHVzZSByZWdleCBtYXRjaChvcHRpb25hbClcbiAgICAgICAgICAgIG1ldGhvZHMgLSB0byBtYXRjaCByZXF1ZXN0IG1ldGhvZCwgeW91IGNhbiB1c2UgY29tbWFzIHRvIHNlcGFyYXRlIG11bHRpcGxlIG1ldGhvZCBtYXRjaGVzKG9wdGlvbmFsKVxuICAgICAgICAgICAgaGVhZGVycyAtIHRvIG1hdGNoIHJlcXVlc3QgaGVhZGVycywgbWF0Y2ggZWFjaCBjaGlsZCBlbGVtZW50KGNoaWxkIGVsZW1lbnQgbmFtZSBpcyBoZWFkZXIgbmFtZSksIHlvdSBjYW4gdXNlICdyZWdleDonIHByZWZpeCB0byB1c2UgcmVnZXggbWF0Y2gob3B0aW9uYWwpXG4gICAgICAgIGhhbmRsZXIgaXMgcmVxdWVzdCBoYW5kbGVyXG4gICAgICAgICAgICB0eXBlIC0gc3VwcG9ydGVkIHR5cGVzOiBzdGF0aWMsIGR5bmFtaWNfcXVlcnlfaGFuZGxlciwgcHJlZGVmaW5lZF9xdWVyeV9oYW5kbGVyXG4gICAgICAgICAgICBxdWVyeSAtIHVzZSB3aXRoIHByZWRlZmluZWRfcXVlcnlfaGFuZGxlciB0eXBlLCBleGVjdXRlcyBxdWVyeSB3aGVuIHRoZSBoYW5kbGVyIGlzIGNhbGxlZFxuICAgICAgICAgICAgcXVlcnlfcGFyYW1fbmFtZSAtIHVzZSB3aXRoIGR5bmFtaWNfcXVlcnlfaGFuZGxlciB0eXBlLCBleHRyYWN0cyBhbmQgZXhlY3V0ZXMgdGhlIHZhbHVlIGNvcnJlc3BvbmRpbmcgdG8gdGhlIDxxdWVyeV9wYXJhbV9uYW1lPiB2YWx1ZSBpbiBIVFRQIHJlcXVlc3QgcGFyYW1zXG4gICAgICAgICAgICBzdGF0dXMgLSB1c2Ugd2l0aCBzdGF0aWMgdHlwZSwgcmVzcG9uc2Ugc3RhdHVzIGNvZGVcbiAgICAgICAgICAgIGNvbnRlbnRfdHlwZSAtIHVzZSB3aXRoIHN0YXRpYyB0eXBlLCByZXNwb25zZSBjb250ZW50LXR5cGVcbiAgICAgICAgICAgIHJlc3BvbnNlX2NvbnRlbnQgLSB1c2Ugd2l0aCBzdGF0aWMgdHlwZSwgUmVzcG9uc2UgY29udGVudCBzZW50IHRvIGNsaWVudCwgd2hlbiB1c2luZyB0aGUgcHJlZml4ICdmaWxlOi8vJyBvciAnY29uZmlnOi8vJywgZmluZCB0aGUgY29udGVudCBmcm9tIHRoZSBmaWxlIG9yIGNvbmZpZ3VyYXRpb24gc2VuZCB0byBjbGllbnQuXG5cbiAgICA8aHR0cF9oYW5kbGVycz5cbiAgICAgICAgPHJ1bGU+XG4gICAgICAgICAgICA8dXJsPi88L3VybD5cbiAgICAgICAgICAgIDxtZXRob2RzPlBPU1QsR0VUPC9tZXRob2RzPlxuICAgICAgICAgICAgPGhlYWRlcnM+PHByYWdtYT5uby1jYWNoZTwvcHJhZ21hPjwvaGVhZGVycz5cbiAgICAgICAgICAgIDxoYW5kbGVyPlxuICAgICAgICAgICAgICAgIDx0eXBlPmR5bmFtaWNfcXVlcnlfaGFuZGxlcjwvdHlwZT5cbiAgICAgICAgICAgICAgICA8cXVlcnlfcGFyYW1fbmFtZT5xdWVyeTwvcXVlcnlfcGFyYW1fbmFtZT5cbiAgICAgICAgICAgIDwvaGFuZGxlcj5cbiAgICAgICAgPC9ydWxlPlxuXG4gICAgICAgIDxydWxlPlxuICAgICAgICAgICAgPHVybD4vcHJlZGVmaW5lZF9xdWVyeTwvdXJsPlxuICAgICAgICAgICAgPG1ldGhvZHM+UE9TVCxHRVQ8L21ldGhvZHM+XG4gICAgICAgICAgICA8aGFuZGxlcj5cbiAgICAgICAgICAgICAgICA8dHlwZT5wcmVkZWZpbmVkX3F1ZXJ5X2hhbmRsZXI8L3R5cGU+XG4gICAgICAgICAgICAgICAgPHF1ZXJ5PlNFTEVDVCAqIEZST00gc3lzdGVtLnNldHRpbmdzPC9xdWVyeT5cbiAgICAgICAgICAgIDwvaGFuZGxlcj5cbiAgICAgICAgPC9ydWxlPlxuXG4gICAgICAgIDxydWxlPlxuICAgICAgICAgICAgPGhhbmRsZXI+XG4gICAgICAgICAgICAgICAgPHR5cGU+c3RhdGljPC90eXBlPlxuICAgICAgICAgICAgICAgIDxzdGF0dXM+MjAwPC9zdGF0dXM+XG4gICAgICAgICAgICAgICAgPGNvbnRlbnRfdHlwZT50ZXh0L3BsYWluOyBjaGFyc2V0PVVURi04PC9jb250ZW50X3R5cGU+XG4gICAgICAgICAgICAgICAgPHJlc3BvbnNlX2NvbnRlbnQ+Y29uZmlnOi8vaHR0cF9zZXJ2ZXJfZGVmYXVsdF9yZXNwb25zZTwvcmVzcG9uc2VfY29udGVudD5cbiAgICAgICAgICAgIDwvaGFuZGxlcj5cbiAgICAgICAgPC9ydWxlPlxuICAgIDwvaHR0cF9oYW5kbGVycz5cbiAgICAtLT5cblxuICAgIDxzZW5kX2NyYXNoX3JlcG9ydHM+XG4gICAgICAgIDwhLS0gQ2hhbmdpbmcgPGVuYWJsZWQ+IHRvIHRydWUgYWxsb3dzIHNlbmRpbmcgY3Jhc2ggcmVwb3J0cyB0byAtLT5cbiAgICAgICAgPCEtLSB0aGUgQ2xpY2tIb3VzZSBjb3JlIGRldmVsb3BlcnMgdGVhbSB2aWEgU2VudHJ5IGh0dHBzOi8vc2VudHJ5LmlvIC0tPlxuICAgICAgICA8IS0tIERvaW5nIHNvIGF0IGxlYXN0IGluIHByZS1wcm9kdWN0aW9uIGVudmlyb25tZW50cyBpcyBoaWdobHkgYXBwcmVjaWF0ZWQgLS0+XG4gICAgICAgIDxlbmFibGVkPmZhbHNlPC9lbmFibGVkPlxuICAgICAgICA8IS0tIENoYW5nZSA8YW5vbnltaXplPiB0byB0cnVlIGlmIHlvdSBkb24ndCBmZWVsIGNvbWZvcnRhYmxlIGF0dGFjaGluZyB0aGUgc2VydmVyIGhvc3RuYW1lIHRvIHRoZSBjcmFzaCByZXBvcnQgLS0+XG4gICAgICAgIDxhbm9ueW1pemU+ZmFsc2U8L2Fub255bWl6ZT5cbiAgICAgICAgPCEtLSBEZWZhdWx0IGVuZHBvaW50IHNob3VsZCBiZSBjaGFuZ2VkIHRvIGRpZmZlcmVudCBTZW50cnkgRFNOIG9ubHkgaWYgeW91IGhhdmUgLS0+XG4gICAgICAgIDwhLS0gc29tZSBpbi1ob3VzZSBlbmdpbmVlcnMgb3IgaGlyZWQgY29uc3VsdGFudHMgd2hvJ3JlIGdvaW5nIHRvIGRlYnVnIENsaWNrSG91c2UgaXNzdWVzIGZvciB5b3UgLS0+XG4gICAgICAgIDxlbmRwb2ludD5odHRwczovLzZmMzMwMzRjZmU2ODRkZDdhM2FiOTg3NWU1N2IxYzhkQG8zODg4NzAuaW5nZXN0LnNlbnRyeS5pby81MjI2Mjc3PC9lbmRwb2ludD5cbiAgICA8L3NlbmRfY3Jhc2hfcmVwb3J0cz5cblxuICAgIDwhLS0gVW5jb21tZW50IHRvIGRpc2FibGUgQ2xpY2tIb3VzZSBpbnRlcm5hbCBETlMgY2FjaGluZy4gLS0+XG4gICAgPCEtLSA8ZGlzYWJsZV9pbnRlcm5hbF9kbnNfY2FjaGU+MTwvZGlzYWJsZV9pbnRlcm5hbF9kbnNfY2FjaGU+IC0tPlxuXG4gICAgPCEtLSBZb3UgY2FuIGFsc28gY29uZmlndXJlIHJvY2tzZGIgbGlrZSB0aGlzOiAtLT5cbiAgICA8IS0tXG4gICAgPHJvY2tzZGI+XG4gICAgICAgIDxvcHRpb25zPlxuICAgICAgICAgICAgPG1heF9iYWNrZ3JvdW5kX2pvYnM+ODwvbWF4X2JhY2tncm91bmRfam9icz5cbiAgICAgICAgPC9vcHRpb25zPlxuICAgICAgICA8Y29sdW1uX2ZhbWlseV9vcHRpb25zPlxuICAgICAgICAgICAgPG51bV9sZXZlbHM+MjwvbnVtX2xldmVscz5cbiAgICAgICAgPC9jb2x1bW5fZmFtaWx5X29wdGlvbnM+XG4gICAgICAgIDx0YWJsZXM+XG4gICAgICAgICAgICA8dGFibGU+XG4gICAgICAgICAgICAgICAgPG5hbWU+VEFCTEU8L25hbWU+XG4gICAgICAgICAgICAgICAgPG9wdGlvbnM+XG4gICAgICAgICAgICAgICAgICAgIDxtYXhfYmFja2dyb3VuZF9qb2JzPjg8L21heF9iYWNrZ3JvdW5kX2pvYnM+XG4gICAgICAgICAgICAgICAgPC9vcHRpb25zPlxuICAgICAgICAgICAgICAgIDxjb2x1bW5fZmFtaWx5X29wdGlvbnM+XG4gICAgICAgICAgICAgICAgICAgIDxudW1fbGV2ZWxzPjI8L251bV9sZXZlbHM+XG4gICAgICAgICAgICAgICAgPC9jb2x1bW5fZmFtaWx5X29wdGlvbnM+XG4gICAgICAgICAgICA8L3RhYmxlPlxuICAgICAgICA8L3RhYmxlcz5cbiAgICA8L3JvY2tzZGI+XG4gICAgLS0+XG5cbiAgICA8IS0tIFVuY29tbWVudCBpZiBlbmFibGUgbWVyZ2UgdHJlZSBtZXRhZGF0YSBjYWNoZSAtLT5cbiAgICA8bWVyZ2VfdHJlZV9tZXRhZGF0YV9jYWNoZT5cbiAgICAgICAgPGxydV9jYWNoZV9zaXplPjI2ODQzNTQ1NjwvbHJ1X2NhY2hlX3NpemU+XG4gICAgICAgIDxjb250aW51ZV9pZl9jb3JydXB0ZWQ+dHJ1ZTwvY29udGludWVfaWZfY29ycnVwdGVkPlxuICAgIDwvbWVyZ2VfdHJlZV9tZXRhZGF0YV9jYWNoZT5cbjwvY2xpY2tob3VzZT5cblwiXCJcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuZmlsZVBhdGggPSBcIi9jbGlja2hvdXNlL2NsdXN0ZXIueG1sXCJcbmNvbnRlbnQgPSBcIlwiXCJcbjw/eG1sIHZlcnNpb249XCIxLjBcIj8+XG48Y2xpY2tob3VzZT5cbiAgICA8IS0tIFpvb0tlZXBlciBpcyB1c2VkIHRvIHN0b3JlIG1ldGFkYXRhIGFib3V0IHJlcGxpY2FzLCB3aGVuIHVzaW5nIFJlcGxpY2F0ZWQgdGFibGVzLlxuICAgICAgICAgT3B0aW9uYWwuIElmIHlvdSBkb24ndCB1c2UgcmVwbGljYXRlZCB0YWJsZXMsIHlvdSBjb3VsZCBvbWl0IHRoYXQuXG5cbiAgICAgICAgIFNlZSBodHRwczovL2NsaWNraG91c2UuY29tL2RvY3MvZW4vZW5naW5lcy90YWJsZS1lbmdpbmVzL21lcmdldHJlZS1mYW1pbHkvcmVwbGljYXRpb24vXG4gICAgICAtLT5cbiAgICA8em9va2VlcGVyPlxuICAgICAgICA8bm9kZSBpbmRleD1cIjFcIj5cbiAgICAgICAgICAgIDxob3N0Pnpvb2tlZXBlci0xPC9ob3N0PlxuICAgICAgICAgICAgPHBvcnQ+MjE4MTwvcG9ydD5cbiAgICAgICAgPC9ub2RlPlxuICAgICAgICA8IS0tIDxub2RlIGluZGV4PVwiMlwiPlxuICAgICAgICAgICAgPGhvc3Q+em9va2VlcGVyLTI8L2hvc3Q+XG4gICAgICAgICAgICA8cG9ydD4yMTgxPC9wb3J0PlxuICAgICAgICA8L25vZGU+XG4gICAgICAgIDxub2RlIGluZGV4PVwiM1wiPlxuICAgICAgICAgICAgPGhvc3Q+em9va2VlcGVyLTM8L2hvc3Q+XG4gICAgICAgICAgICA8cG9ydD4yMTgxPC9wb3J0PlxuICAgICAgICA8L25vZGU+IC0tPlxuICAgIDwvem9va2VlcGVyPlxuXG4gICAgPCEtLSBDb25maWd1cmF0aW9uIG9mIGNsdXN0ZXJzIHRoYXQgY291bGQgYmUgdXNlZCBpbiBEaXN0cmlidXRlZCB0YWJsZXMuXG4gICAgICAgICBodHRwczovL2NsaWNraG91c2UuY29tL2RvY3MvZW4vb3BlcmF0aW9ucy90YWJsZV9lbmdpbmVzL2Rpc3RyaWJ1dGVkL1xuICAgICAgLS0+XG4gICAgPHJlbW90ZV9zZXJ2ZXJzPlxuICAgICAgICA8Y2x1c3Rlcj5cbiAgICAgICAgICAgIDwhLS0gSW50ZXItc2VydmVyIHBlci1jbHVzdGVyIHNlY3JldCBmb3IgRGlzdHJpYnV0ZWQgcXVlcmllc1xuICAgICAgICAgICAgICAgICBkZWZhdWx0OiBubyBzZWNyZXQgKG5vIGF1dGhlbnRpY2F0aW9uIHdpbGwgYmUgcGVyZm9ybWVkKVxuXG4gICAgICAgICAgICAgICAgIElmIHNldCwgdGhlbiBEaXN0cmlidXRlZCBxdWVyaWVzIHdpbGwgYmUgdmFsaWRhdGVkIG9uIHNoYXJkcywgc28gYXQgbGVhc3Q6XG4gICAgICAgICAgICAgICAgIC0gc3VjaCBjbHVzdGVyIHNob3VsZCBleGlzdCBvbiB0aGUgc2hhcmQsXG4gICAgICAgICAgICAgICAgIC0gc3VjaCBjbHVzdGVyIHNob3VsZCBoYXZlIHRoZSBzYW1lIHNlY3JldC5cblxuICAgICAgICAgICAgICAgICBBbmQgYWxzbyAoYW5kIHdoaWNoIGlzIG1vcmUgaW1wb3J0YW50KSwgdGhlIGluaXRpYWxfdXNlciB3aWxsXG4gICAgICAgICAgICAgICAgIGJlIHVzZWQgYXMgY3VycmVudCB1c2VyIGZvciB0aGUgcXVlcnkuXG5cbiAgICAgICAgICAgICAgICAgUmlnaHQgbm93IHRoZSBwcm90b2NvbCBpcyBwcmV0dHkgc2ltcGxlIGFuZCBpdCBvbmx5IHRha2VzIGludG8gYWNjb3VudDpcbiAgICAgICAgICAgICAgICAgLSBjbHVzdGVyIG5hbWVcbiAgICAgICAgICAgICAgICAgLSBxdWVyeVxuXG4gICAgICAgICAgICAgICAgIEFsc28gaXQgd2lsbCBiZSBuaWNlIGlmIHRoZSBmb2xsb3dpbmcgd2lsbCBiZSBpbXBsZW1lbnRlZDpcbiAgICAgICAgICAgICAgICAgLSBzb3VyY2UgaG9zdG5hbWUgKHNlZSBpbnRlcnNlcnZlcl9odHRwX2hvc3QpLCBidXQgdGhlbiBpdCB3aWxsIGRlcGVuZHMgZnJvbSBETlMsXG4gICAgICAgICAgICAgICAgICAgaXQgY2FuIHVzZSBJUCBhZGRyZXNzIGluc3RlYWQsIGJ1dCB0aGVuIHRoZSB5b3UgbmVlZCB0byBnZXQgY29ycmVjdCBvbiB0aGUgaW5pdGlhdG9yIG5vZGUuXG4gICAgICAgICAgICAgICAgIC0gdGFyZ2V0IGhvc3RuYW1lIC8gaXAgYWRkcmVzcyAoc2FtZSBub3RlcyBhcyBmb3Igc291cmNlIGhvc3RuYW1lKVxuICAgICAgICAgICAgICAgICAtIHRpbWUtYmFzZWQgc2VjdXJpdHkgdG9rZW5zXG4gICAgICAgICAgICAtLT5cbiAgICAgICAgICAgIDwhLS0gPHNlY3JldD48L3NlY3JldD4gLS0+XG4gICAgICAgICAgICA8c2hhcmQ+XG4gICAgICAgICAgICAgICAgPCEtLSBPcHRpb25hbC4gV2hldGhlciB0byB3cml0ZSBkYXRhIHRvIGp1c3Qgb25lIG9mIHRoZSByZXBsaWNhcy4gRGVmYXVsdDogZmFsc2UgKHdyaXRlIGRhdGEgdG8gYWxsIHJlcGxpY2FzKS4gLS0+XG4gICAgICAgICAgICAgICAgPCEtLSA8aW50ZXJuYWxfcmVwbGljYXRpb24+ZmFsc2U8L2ludGVybmFsX3JlcGxpY2F0aW9uPiAtLT5cbiAgICAgICAgICAgICAgICA8IS0tIE9wdGlvbmFsLiBTaGFyZCB3ZWlnaHQgd2hlbiB3cml0aW5nIGRhdGEuIERlZmF1bHQ6IDEuIC0tPlxuICAgICAgICAgICAgICAgIDwhLS0gPHdlaWdodD4xPC93ZWlnaHQ+IC0tPlxuICAgICAgICAgICAgICAgIDxyZXBsaWNhPlxuICAgICAgICAgICAgICAgICAgICA8aG9zdD5jbGlja2hvdXNlPC9ob3N0PlxuICAgICAgICAgICAgICAgICAgICA8cG9ydD45MDAwPC9wb3J0PlxuICAgICAgICAgICAgICAgICAgICA8IS0tIE9wdGlvbmFsLiBQcmlvcml0eSBvZiB0aGUgcmVwbGljYSBmb3IgbG9hZF9iYWxhbmNpbmcuIERlZmF1bHQ6IDEgKGxlc3MgdmFsdWUgaGFzIG1vcmUgcHJpb3JpdHkpLiAtLT5cbiAgICAgICAgICAgICAgICAgICAgPCEtLSA8cHJpb3JpdHk+MTwvcHJpb3JpdHk+IC0tPlxuICAgICAgICAgICAgICAgIDwvcmVwbGljYT5cbiAgICAgICAgICAgIDwvc2hhcmQ+XG4gICAgICAgICAgICA8IS0tIDxzaGFyZD5cbiAgICAgICAgICAgICAgICA8cmVwbGljYT5cbiAgICAgICAgICAgICAgICAgICAgPGhvc3Q+Y2xpY2tob3VzZS0yPC9ob3N0PlxuICAgICAgICAgICAgICAgICAgICA8cG9ydD45MDAwPC9wb3J0PlxuICAgICAgICAgICAgICAgIDwvcmVwbGljYT5cbiAgICAgICAgICAgIDwvc2hhcmQ+XG4gICAgICAgICAgICA8c2hhcmQ+XG4gICAgICAgICAgICAgICAgPHJlcGxpY2E+XG4gICAgICAgICAgICAgICAgICAgIDxob3N0PmNsaWNraG91c2UtMzwvaG9zdD5cbiAgICAgICAgICAgICAgICAgICAgPHBvcnQ+OTAwMDwvcG9ydD5cbiAgICAgICAgICAgICAgICA8L3JlcGxpY2E+XG4gICAgICAgICAgICA8L3NoYXJkPiAtLT5cbiAgICAgICAgPC9jbHVzdGVyPlxuICAgIDwvcmVtb3RlX3NlcnZlcnM+XG48L2NsaWNraG91c2U+XG5cIlwiXCJcblxuW1tjb25maWcubW91bnRzXV1cbmZpbGVQYXRoID0gXCIvc2lnbm96L3Byb21ldGhldXMueG1sXCJcbmNvbnRlbnQgPSBcIlwiXCJcbiMgbXkgZ2xvYmFsIGNvbmZpZ1xuZ2xvYmFsOlxuICBzY3JhcGVfaW50ZXJ2YWw6ICAgICA1cyAjIFNldCB0aGUgc2NyYXBlIGludGVydmFsIHRvIGV2ZXJ5IDE1IHNlY29uZHMuIERlZmF1bHQgaXMgZXZlcnkgMSBtaW51dGUuXG4gIGV2YWx1YXRpb25faW50ZXJ2YWw6IDE1cyAjIEV2YWx1YXRlIHJ1bGVzIGV2ZXJ5IDE1IHNlY29uZHMuIFRoZSBkZWZhdWx0IGlzIGV2ZXJ5IDEgbWludXRlLlxuICAjIHNjcmFwZV90aW1lb3V0IGlzIHNldCB0byB0aGUgZ2xvYmFsIGRlZmF1bHQgKDEwcykuXG5cbiMgQWxlcnRtYW5hZ2VyIGNvbmZpZ3VyYXRpb25cbmFsZXJ0aW5nOlxuICBhbGVydG1hbmFnZXJzOlxuICAtIHN0YXRpY19jb25maWdzOlxuICAgIC0gdGFyZ2V0czpcbiAgICAgIC0gYWxlcnRtYW5hZ2VyOjkwOTNcblxuIyBMb2FkIHJ1bGVzIG9uY2UgYW5kIHBlcmlvZGljYWxseSBldmFsdWF0ZSB0aGVtIGFjY29yZGluZyB0byB0aGUgZ2xvYmFsICdldmFsdWF0aW9uX2ludGVydmFsJy5cbnJ1bGVfZmlsZXM6IFtdXG4gICMgLSBcImZpcnN0X3J1bGVzLnltbFwiXG4gICMgLSBcInNlY29uZF9ydWxlcy55bWxcIlxuICAjIC0gJ2FsZXJ0cy55bWwnXG5cbiMgQSBzY3JhcGUgY29uZmlndXJhdGlvbiBjb250YWluaW5nIGV4YWN0bHkgb25lIGVuZHBvaW50IHRvIHNjcmFwZTpcbiMgSGVyZSBpdCdzIFByb21ldGhldXMgaXRzZWxmLlxuc2NyYXBlX2NvbmZpZ3M6IFtdXG5cbnJlbW90ZV9yZWFkOlxuICAtIHVybDogdGNwOi8vY2xpY2tob3VzZTo5MDAwL3NpZ25vel9tZXRyaWNzXG5cIlwiXCJcblxuW1tjb25maWcubW91bnRzXV1cbmZpbGVQYXRoID0gXCIvY29sbGVjdG9yL290ZWwtY29sbGVjdG9yLWNvbmZpZy55YW1sXCJcbmNvbnRlbnQgPSBcIlwiXCJcbnJlY2VpdmVyczpcbiAgb3RscDpcbiAgICBwcm90b2NvbHM6XG4gICAgICBncnBjOlxuICAgICAgICBlbmRwb2ludDogMC4wLjAuMDo0MzE3XG4gICAgICBodHRwOlxuICAgICAgICBlbmRwb2ludDogMC4wLjAuMDo0MzE4XG5wcm9jZXNzb3JzOlxuICBiYXRjaDpcbmV4cG9ydGVyczpcbiAgY2xpY2tob3VzZXRyYWNlczpcbiAgICBkYXRhc291cmNlOiB0Y3A6Ly9jbGlja2hvdXNlOjkwMDAvc2lnbm96X3RyYWNlc1xuICAgIHVzZV9uZXdfc2NoZW1hOiB0cnVlXG4gIHNpZ25vemNsaWNraG91c2VtZXRyaWNzOlxuICAgIGRzbjogdGNwOi8vY2xpY2tob3VzZTo5MDAwL3NpZ25vel9tZXRyaWNzXG4gICAgdGltZW91dDogMTVzXG4gIGNsaWNraG91c2Vsb2dzZXhwb3J0ZXI6XG4gICAgZHNuOiB0Y3A6Ly9jbGlja2hvdXNlOjkwMDAvc2lnbm96X2xvZ3NcbiAgICB0aW1lb3V0OiAxMHNcbiAgICB1c2VfbmV3X3NjaGVtYTogdHJ1ZVxuICBtZXRhZGF0YWV4cG9ydGVyOlxuICAgIGRzbjogdGNwOi8vY2xpY2tob3VzZTo5MDAwL3NpZ25vel9tZXRhZGF0YVxuICAgIHRpbWVvdXQ6IDEwc1xuc2VydmljZTpcbiAgcGlwZWxpbmVzOlxuICAgIHRyYWNlczpcbiAgICAgIHJlY2VpdmVyczogW290bHBdXG4gICAgICBwcm9jZXNzb3JzOiBbYmF0Y2hdXG4gICAgICBleHBvcnRlcnM6IFtjbGlja2hvdXNldHJhY2VzLCBtZXRhZGF0YWV4cG9ydGVyXVxuICAgIG1ldHJpY3M6XG4gICAgICByZWNlaXZlcnM6IFtvdGxwXVxuICAgICAgcHJvY2Vzc29yczogW2JhdGNoXVxuICAgICAgZXhwb3J0ZXJzOiBbc2lnbm96Y2xpY2tob3VzZW1ldHJpY3MsIG1ldGFkYXRhZXhwb3J0ZXJdXG4gICAgbG9nczpcbiAgICAgIHJlY2VpdmVyczogW290bHBdXG4gICAgICBwcm9jZXNzb3JzOiBbYmF0Y2hdXG4gICAgICBleHBvcnRlcnM6IFtjbGlja2hvdXNlbG9nc2V4cG9ydGVyLCBtZXRhZGF0YWV4cG9ydGVyXVxuXCJcIlwiXG5cbltbY29uZmlnLm1vdW50c11dXG5maWxlUGF0aCA9IFwiL2NsaWNraG91c2UvdXNlcl9zY3JpcHRzL2VtcHR5LnR4dFwiXG5jb250ZW50ID0gXCJcIiIKfQ==
```

## Links

`monitoring`,`observability`,`metrics`,`traces`,`logs`,`opentelemetry`,`apm`

---

Version:`v0.97.1`

ShlinkURL shortener that can be used to serve shortened URLs under your own domain.

SilverBulletSilverBullet is a personal knowledge base and collaborative note-taking platform.

### On this page

ConfigurationBase64LinksTags