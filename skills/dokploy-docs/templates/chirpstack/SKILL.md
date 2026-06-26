---
title: "ChirpStack | Dokploy"
source: "https://docs.dokploy.com/docs/templates/chirpstack"
category: dokploy-docs
created: "2026-06-25T17:21:43.963Z"
---

ChirpStack | Dokploy

# ChirpStack

Copy as Markdown

Open-source LoRaWAN Network Server for IoT applications. Complete stack with gateway bridges, REST API, and web interface for managing LoRaWAN devices and gateways.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  chirpstack:
    image: chirpstack/chirpstack:4
    command: -c /etc/chirpstack
    restart: unless-stopped
    volumes:
      - ../files/chirpstack:/etc/chirpstack
    ports:
      - 8080
    environment:
      - MQTT_BROKER_HOST=mosquitto
      - REDIS_HOST=redis
      - POSTGRESQL_HOST=postgres
    depends_on:
      - postgres
      - mosquitto
      - redis

  chirpstack-gateway-bridge:
    image: chirpstack/chirpstack-gateway-bridge:4
    restart: unless-stopped
    volumes:
      - ../files/chirpstack-gateway-bridge:/etc/chirpstack-gateway-bridge
    ports:
      - 1700/udp
    environment:
      - INTEGRATION__MQTT__EVENT_TOPIC_TEMPLATE=eu868/gateway/{{ .GatewayID }}/event/{{ .EventType }}
      - INTEGRATION__MQTT__STATE_TOPIC_TEMPLATE=eu868/gateway/{{ .GatewayID }}/state/{{ .StateType }}
      - INTEGRATION__MQTT__COMMAND_TOPIC_TEMPLATE=eu868/gateway/{{ .GatewayID }}/command/#
    depends_on:
      - mosquitto

  chirpstack-gateway-bridge-basicstation:
    image: chirpstack/chirpstack-gateway-bridge:4
    command: -c /etc/chirpstack-gateway-bridge/chirpstack-gateway-bridge-basicstation-eu868.toml
    restart: unless-stopped
    volumes:
      - ../files/chirpstack-gateway-bridge:/etc/chirpstack-gateway-bridge
    ports:
      - 3001
    depends_on:
      - mosquitto

  chirpstack-rest-api:
    image: chirpstack/chirpstack-rest-api:4
    restart: unless-stopped
    command: --server chirpstack:8080 --bind 0.0.0.0:8090 --insecure
    ports:
      - 8090
    depends_on:
      - chirpstack

  postgres:
    image: postgres:14-alpine
    restart: unless-stopped
    volumes:
      - postgresqldata:/var/lib/postgresql/data
      - ../files/postgresql/initdb:/docker-entrypoint-initdb.d
    environment:
      - POSTGRES_USER=chirpstack
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_DB=chirpstack

  redis:
    image: redis:7-alpine
    restart: unless-stopped
    command: redis-server --save 300 1 --save 60 100 --appendonly no
    volumes:
      - redisdata:/data

  mosquitto:
    image: eclipse-mosquitto:2
    restart: unless-stopped
    volumes:
      - ../files/mosquitto/config/:/mosquitto/config/
    ports:
      - 1883

volumes:
  postgresqldata:
  redisdata:
```

```
[variables]
main_domain = "${domain}"
api_secret = "${base64:32}"
postgres_password = "${password:32}"

[config]
[[config.domains]]
serviceName = "chirpstack"
port = 8080
host = "${main_domain}"
path = "/"

[[config.domains]]
serviceName = "chirpstack-rest-api"
port = 8090
host = "api-${main_domain}"
path = "/"

[config.env]
POSTGRES_PASSWORD = "${postgres_password}"

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/chirpstack.toml"
content = """
# Logging.
[logging]

  # Log level.
  #
  # Options are: trace, debug, info, warn error.
  level="info"

# PostgreSQL configuration.
[postgresql]

  # PostgreSQL DSN.
  #
  # Format example: postgres://<USERNAME>:<PASSWORD>@<HOSTNAME>/<DATABASE>?sslmode=<SSLMODE>.
  #
  # SSL mode options:
  #  * disable - Do not use TLS
  #  * prefer - Attempt to connect with TLS but allow sessions without
  #  * require - Require the use of TLS
  dsn="postgres://chirpstack:${postgres_password}@postgres/chirpstack?sslmode=disable"

  # Max open connections.
  #
  # This sets the max. number of open connections that are allowed in the
  # PostgreSQL connection pool.
  max_open_connections=10

  # Min idle connections.
  #
  # This sets the min. number of idle connections in the PostgreSQL connection
  # pool (0 = equal to max_open_connections).
  min_idle_connections=0

# Redis configuration.
[redis]

  # Server address or addresses.
  #
  # Set multiple addresses when connecting to a cluster.
  servers=[
    "redis://redis/",
  ]

  # TLS enabled.
  tls_enabled=false

  # Redis Cluster.
  #
  # Set this to true when the provided URLs are pointing to a Redis Cluster
  # instance.
  cluster=false

# Network related configuration.
[network]

  # Network identifier (NetID, 3 bytes) encoded as HEX (e.g. 010203).
  net_id="000000"

  # Enabled regions.
  #
  # Multiple regions can be enabled simultaneously. Each region must match
  # the 'name' parameter of the region configuration in '[[regions]]'.
  enabled_regions=[
    "as923",
    "as923_2",
    "as923_3",
    "as923_4",
    "au915_0",
    "cn470_10",
    "cn779",
    "eu433",
    "eu868",
    "in865",
    "ism2400",
    "kr920",
    "ru864",
    "us915_0",
    "us915_1",
  ]

# API interface configuration.
[api]

  # interface:port to bind the API interface to.
  bind="0.0.0.0:8080"

  # Secret.
  #
  # This secret is used for generating login and API tokens, make sure this
  # is never exposed. Changing this secret will invalidate all login and API
  # tokens. The following command can be used to generate a random secret:
  #   openssl rand -base64 32
  secret="${api_secret}"

[integration]
  enabled=["mqtt"]

  [integration.mqtt]
    server="tcp://mosquitto:1883/"
    json=true
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_as923_2.toml"
content = """
# This file contains an example AS923_2 configuration.
[[regions]]

  # ID is an user-defined identifier for this region.
  id="as923_2"

  # Description is a short description for this region.
  description="AS923-2"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="AS923_2"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="as923_2"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=921400000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=921600000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=0

    # RX2 frequency (Hz)
    rx2_frequency=921400000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=5

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=3

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_as923_3.toml"
content = """
# This file contains an example AS923_3 configuration.
[[regions]]

  # ID is an user-defined identifier for this region.
  id="as923_3"

  # Description is a short description for this region.
  description="AS923-3"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="AS923_3"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="as923_3"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=916600000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=916800000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=2

    # RX2 frequency (Hz)
    rx2_frequency=916600000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=5

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=3

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_as923_4.toml"
content = """
# This file contains an example AS923_4 configuration.
[[regions]]

  # ID is an user-defined identifier for this region.
  id="as923_4"

  # Description is a short description for this region.
  description="AS923-4"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="AS923_4"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="as923_4"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=917300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=917500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=2

    # RX2 frequency (Hz)
    rx2_frequency=917300000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=5

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=3

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_as923.toml"
content = """
# This file contains an example AS923 configuration.
[[regions]]

  # ID is an user-defined identifier for this region.
  id="as923"

  # Description is a short description for this region.
  description="AS923"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="AS923"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="as923"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=923200000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=923400000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=2

    # RX2 frequency (Hz)
    rx2_frequency=923200000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=5

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=3

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_au915_0.toml"
content = """
# This file contains an example AU915 example (channels 0-7 + 64).
[[regions]]

  # ID is an use-defined identifier for this region.
  id="au915_0"

  # Description is a short description for this region.
  description="AU915 (channels 0-7 + 64)"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="AU915"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="au915_0"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=915200000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=915400000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=915600000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=915800000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=916000000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=916200000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=916400000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=916600000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=915900000
      bandwidth=500000
      modulation="LORA"
      spreading_factors=[8]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=8

    # RX2 frequency (Hz)
    rx2_frequency=923300000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=5

    # Enabled uplink channels.
    #
    # Use this when ony a sub-set of the by default enabled channels are being
    # used. For example when only using the first 8 channels of the US band.
    # Note: when left blank / empty array, all channels will be enabled.
    enabled_uplink_channels=[0, 1, 2, 3, 4, 5, 6, 7, 64]

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=8

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_au915_1.toml"
content = """
# This file contains an example AU915 example (channels 8-15 + 65).
[[regions]]

  # ID is an use-defined identifier for this region.
  id="au915_1"

  # Description is a short description for this region.
  description="AU915 (channels 8-15 + 65)"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="AU915"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="au915_1"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=916800000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=917000000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=917200000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=917400000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=917600000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=917800000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=918000000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=918200000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=917500000
      bandwidth=500000
      modulation="LORA"
      spreading_factors=[8]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=8

    # RX2 frequency (Hz)
    rx2_frequency=923300000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=5

    # Enabled uplink channels.
    #
    # Use this when ony a sub-set of the by default enabled channels are being
    # used. For example when only using the first 8 channels of the US band.
    # Note: when left blank / empty array, all channels will be enabled.
    enabled_uplink_channels=[8, 9, 10, 11, 12, 13, 14, 15, 65]

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=8

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_au915_2.toml"
content = """
# This file contains an example AU915 example (channels 16-23 + 66).
[[regions]]

  # ID is an use-defined identifier for this region.
  id="au915_2"

  # Description is a short description for this region.
  description="AU915 (channels 16-23 + 65)"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="AU915"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="au915_2"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=918400000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=918600000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=918800000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=919000000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=919200000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=919400000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=919600000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=919800000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=919100000
      bandwidth=500000
      modulation="LORA"
      spreading_factors=[8]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=8

    # RX2 frequency (Hz)
    rx2_frequency=923300000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=5

    # Enabled uplink channels.
    #
    # Use this when ony a sub-set of the by default enabled channels are being
    # used. For example when only using the first 8 channels of the US band.
    # Note: when left blank / empty array, all channels will be enabled.
    enabled_uplink_channels=[16, 17, 18, 19, 20, 21, 22, 23, 65]

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=8

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_au915_3.toml"
content = """
# This file contains an example AU915 example (channels 24-31 + 67).
[[regions]]

  # ID is an use-defined identifier for this region.
  id="au915_3"

  # Description is a short description for this region.
  description="AU915 (channels 24-31 + 67)"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="AU915"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="au915_3"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=920000000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=920200000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=920400000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=920600000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=920800000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=921000000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=921200000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=921400000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=920700000
      bandwidth=500000
      modulation="LORA"
      spreading_factors=[8]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=8

    # RX2 frequency (Hz)
    rx2_frequency=923300000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=5

    # Enabled uplink channels.
    #
    # Use this when ony a sub-set of the by default enabled channels are being
    # used. For example when only using the first 8 channels of the US band.
    # Note: when left blank / empty array, all channels will be enabled.
    enabled_uplink_channels=[24, 25, 26, 27, 28, 29, 30, 31, 67]

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=8

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_au915_4.toml"
content = """
# This file contains an example AU915 example (channels 32-39 + 68).
[[regions]]

  # ID is an use-defined identifier for this region.
  id="au915_4"

  # Description is a short description for this region.
  description="AU915 (channels 32-39 + 68)"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="AU915"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="au915_4"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=921600000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=921800000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=922000000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=922200000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=922400000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=922600000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=922800000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=923000000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=922300000
      bandwidth=500000
      modulation="LORA"
      spreading_factors=[8]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=8

    # RX2 frequency (Hz)
    rx2_frequency=923300000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=5

    # Enabled uplink channels.
    #
    # Use this when ony a sub-set of the by default enabled channels are being
    # used. For example when only using the first 8 channels of the US band.
    # Note: when left blank / empty array, all channels will be enabled.
    enabled_uplink_channels=[32, 33, 34, 35, 36, 37, 38, 39, 68]

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=8

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_au915_5.toml"
content = """
# This file contains an example AU915 example (channels 40-47 + 69).
[[regions]]

  # ID is an use-defined identifier for this region.
  id="au915_5"

  # Description is a short description for this region.
  description="AU915 (channels 40-47 + 69)"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="AU915"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="au915_5"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=923200000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=923400000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=923600000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=923800000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=924000000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=924200000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=924400000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=924600000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=923900000
      bandwidth=500000
      modulation="LORA"
      spreading_factors=[8]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=8

    # RX2 frequency (Hz)
    rx2_frequency=923300000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=5

    # Enabled uplink channels.
    #
    # Use this when ony a sub-set of the by default enabled channels are being
    # used. For example when only using the first 8 channels of the US band.
    # Note: when left blank / empty array, all channels will be enabled.
    enabled_uplink_channels=[40, 41, 42, 43, 44, 45, 46, 47, 69]

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=8

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_au915_6.toml"
content = """
# This file contains an example AU915 example (channels 48-55 + 70).
[[regions]]

  # ID is an use-defined identifier for this region.
  id="au915_6"

  # Description is a short description for this region.
  description="AU915 (channels 48-55 + 70)"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="AU915"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="au915_6"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=924800000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=925000000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=925200000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=925400000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=925600000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=925800000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=926000000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=926200000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=925500000
      bandwidth=500000
      modulation="LORA"
      spreading_factors=[8]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=8

    # RX2 frequency (Hz)
    rx2_frequency=923300000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=5

    # Enabled uplink channels.
    #
    # Use this when ony a sub-set of the by default enabled channels are being
    # used. For example when only using the first 8 channels of the US band.
    # Note: when left blank / empty array, all channels will be enabled.
    enabled_uplink_channels=[48, 49, 50, 51, 52, 53, 54, 55, 70]

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=8

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_au915_7.toml"
content = """
# This file contains an example AU915 example (channels 56-63 + 71).
[[regions]]

  # ID is an use-defined identifier for this region.
  id="au915_7"

  # Description is a short description for this region.
  description="AU915 (channels 56-63 + 71)"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="AU915"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="au915_7"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=926400000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=926600000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=926800000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=927000000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=927200000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=927400000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=927600000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=927800000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=927100000
      bandwidth=500000
      modulation="LORA"
      spreading_factors=[8]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=8

    # RX2 frequency (Hz)
    rx2_frequency=923300000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=5

    # Enabled uplink channels.
    #
    # Use this when ony a sub-set of the by default enabled channels are being
    # used. For example when only using the first 8 channels of the US band.
    # Note: when left blank / empty array, all channels will be enabled.
    enabled_uplink_channels=[56, 57, 58, 59, 60, 61, 62, 63, 71]

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=8

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_cn470_0.toml"
content = """
# This file contains an example CN470 example (channels 0-7).
[[regions]]

  # ID is an use-defined identifier for this region.
  id="cn470_0"

  # Description is a short description for this region.
  description="CN470 (channels 0-7)"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="CN470"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="cn470_0"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=470300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=470500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=470700000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=470900000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=471100000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=471300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=471500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=471700000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=0

    # RX2 frequency (Hz)
    rx2_frequency=505300000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=5

    # Enabled uplink channels.
    #
    # Use this when ony a sub-set of the by default enabled channels are being
    # used. For example when only using the first 8 channels of the US band.
    # Note: when left blank / empty array, all channels will be enabled.
    enabled_uplink_channels=[0, 1, 2, 3, 4, 5, 6, 7]

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=2

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_cn470_10.toml"
content = """
# This file contains an example CN470 example (channels 80-87).
[[regions]]

  # ID is an use-defined identifier for this region.
  id="cn470_10"

  # Description is a short description for this region.
  description="CN470 (channels 80-87)"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="CN470"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="cn470_10"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=486300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=486500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=486700000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=486900000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=487100000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=487300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=487500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=487700000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=0

    # RX2 frequency (Hz)
    rx2_frequency=505300000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=5

    # Enabled uplink channels.
    #
    # Use this when ony a sub-set of the by default enabled channels are being
    # used. For example when only using the first 8 channels of the US band.
    # Note: when left blank / empty array, all channels will be enabled.
    enabled_uplink_channels=[80, 81, 82, 83, 84, 85, 86, 87]

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=2

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_cn470_11.toml"
content = """
# This file contains an example CN470 example (channels 88-95).
[[regions]]

  # ID is an use-defined identifier for this region.
  id="cn470_11"

  # Description is a short description for this region.
  description="CN470 (channels 88-95)"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="CN470"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="cn470_11"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=487900000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=488100000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=488300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=488500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=488700000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=488900000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=489100000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=489300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=0

    # RX2 frequency (Hz)
    rx2_frequency=505300000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=5

    # Enabled uplink channels.
    #
    # Use this when ony a sub-set of the by default enabled channels are being
    # used. For example when only using the first 8 channels of the US band.
    # Note: when left blank / empty array, all channels will be enabled.
    enabled_uplink_channels=[88, 89, 90, 91, 92, 93, 94, 95]

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=2

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_cn470_1.toml"
content = """
# This file contains an example CN470 example (channels 8-15).
[[regions]]

  # ID is an use-defined identifier for this region.
  id="cn470_1"

  # Description is a short description for this region.
  description="CN470 (channels 8-15)"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="CN470"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="cn470_1"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=471900000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=472100000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=472300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=472500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=472700000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=472900000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=473100000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=473300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=0

    # RX2 frequency (Hz)
    rx2_frequency=505300000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=5

    # Enabled uplink channels.
    #
    # Use this when ony a sub-set of the by default enabled channels are being
    # used. For example when only using the first 8 channels of the US band.
    # Note: when left blank / empty array, all channels will be enabled.
    enabled_uplink_channels=[8, 9, 10, 11, 12, 13, 14, 15]

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=2

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_cn470_2.toml"
content = """
# This file contains an example CN470 example (channels 16-23).
[[regions]]

  # ID is an use-defined identifier for this region.
  id="cn470_2"

  # Description is a short description for this region.
  description="CN470 (channels 16-23)"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="CN470"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="cn470_2"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=473500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=473700000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=473900000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=474100000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=474300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=474500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=474700000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=474900000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=0

    # RX2 frequency (Hz)
    rx2_frequency=505300000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=5

    # Enabled uplink channels.
    #
    # Use this when ony a sub-set of the by default enabled channels are being
    # used. For example when only using the first 8 channels of the US band.
    # Note: when left blank / empty array, all channels will be enabled.
    enabled_uplink_channels=[16, 17, 18, 19, 20, 21, 22, 23]

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=2

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_cn470_3.toml"
content = """
# This file contains an example CN470 example (channels 24-31).
[[regions]]

  # ID is an use-defined identifier for this region.
  id="cn470_3"

  # Description is a short description for this region.
  description="CN470 (channels 24-31)"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="CN470"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="cn470_3"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=475100000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=475300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=475500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=475700000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=475900000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=476100000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=476300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=476500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=0

    # RX2 frequency (Hz)
    rx2_frequency=505300000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=5

    # Enabled uplink channels.
    #
    # Use this when ony a sub-set of the by default enabled channels are being
    # used. For example when only using the first 8 channels of the US band.
    # Note: when left blank / empty array, all channels will be enabled.
    enabled_uplink_channels=[24, 25, 26, 27, 28, 29, 30, 31]

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=2

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_cn470_4.toml"
content = """
# This file contains an example CN470 example (channels 32-39).
[[regions]]

  # ID is an use-defined identifier for this region.
  id="cn470_4"

  # Description is a short description for this region.
  description="CN470 (channels 32-39)"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="CN470"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="cn470_4"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=476700000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=476900000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=477100000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=477300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=477500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=477700000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=477900000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=478100000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=0

    # RX2 frequency (Hz)
    rx2_frequency=505300000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=5

    # Enabled uplink channels.
    #
    # Use this when ony a sub-set of the by default enabled channels are being
    # used. For example when only using the first 8 channels of the US band.
    # Note: when left blank / empty array, all channels will be enabled.
    enabled_uplink_channels=[32, 33, 34, 35, 36, 37, 38, 39]

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=2

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_cn470_5.toml"
content = """
# This file contains an example CN470 example (channels 40-47).
[[regions]]

  # ID is an use-defined identifier for this region.
  id="cn470_5"

  # Description is a short description for this region.
  description="CN470 (channels 40-47)"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="CN470"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="cn470_5"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=478300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=478500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=478700000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=478900000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=479100000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=479300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=479500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=479700000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=0

    # RX2 frequency (Hz)
    rx2_frequency=505300000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=5

    # Enabled uplink channels.
    #
    # Use this when ony a sub-set of the by default enabled channels are being
    # used. For example when only using the first 8 channels of the US band.
    # Note: when left blank / empty array, all channels will be enabled.
    enabled_uplink_channels=[40, 41, 42, 43, 44, 45, 46, 47]

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=2

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_cn470_6.toml"
content = """
# This file contains an example CN470 example (channels 48-55).
[[regions]]

  # ID is an use-defined identifier for this region.
  id="cn470_6"

  # Description is a short description for this region.
  description="CN470 (channels 48-55)"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="CN470"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="cn470_6"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=479900000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=480100000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=480300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=480500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=480700000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=480900000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=481100000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=481300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=0

    # RX2 frequency (Hz)
    rx2_frequency=505300000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=5

    # Enabled uplink channels.
    #
    # Use this when ony a sub-set of the by default enabled channels are being
    # used. For example when only using the first 8 channels of the US band.
    # Note: when left blank / empty array, all channels will be enabled.
    enabled_uplink_channels=[48, 49, 50, 51, 52, 53, 54, 55]

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=2

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_cn470_7.toml"
content = """
# This file contains an example CN470 example (channels 56-63).
[[regions]]

  # ID is an use-defined identifier for this region.
  id="cn470_7"

  # Description is a short description for this region.
  description="CN470 (channels 56-63)"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="CN470"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="cn470_7"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=481500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=481700000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=481900000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=482100000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=482300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=482500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=482700000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=482900000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=0

    # RX2 frequency (Hz)
    rx2_frequency=505300000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=5

    # Enabled uplink channels.
    #
    # Use this when ony a sub-set of the by default enabled channels are being
    # used. For example when only using the first 8 channels of the US band.
    # Note: when left blank / empty array, all channels will be enabled.
    enabled_uplink_channels=[56, 57, 58, 59, 60, 61, 62, 63]

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=2

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_cn470_8.toml"
content = """
# This file contains an example CN470 example (channels 64-71).
[[regions]]

  # ID is an use-defined identifier for this region.
  id="cn470_8"

  # Description is a short description for this region.
  description="CN470 (channels 64-71)"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="CN470"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="cn470_8"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=483100000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=483300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=483500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=483700000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=483900000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=484100000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=484300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=484500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=0

    # RX2 frequency (Hz)
    rx2_frequency=505300000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=5

    # Enabled uplink channels.
    #
    # Use this when ony a sub-set of the by default enabled channels are being
    # used. For example when only using the first 8 channels of the US band.
    # Note: when left blank / empty array, all channels will be enabled.
    enabled_uplink_channels=[64, 65, 66, 67, 68, 69, 70, 71]

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=2

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_cn470_9.toml"
content = """
# This file contains an example CN470 example (channels 72-79).
[[regions]]

  # ID is an use-defined identifier for this region.
  id="cn470_9"

  # Description is a short description for this region.
  description="CN470 (channels 72-79)"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="CN470"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="cn470_9"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=484700000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=484900000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=485100000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=485300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=485500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=485700000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=485900000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=486100000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=0

    # RX2 frequency (Hz)
    rx2_frequency=505300000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=5

    # Enabled uplink channels.
    #
    # Use this when ony a sub-set of the by default enabled channels are being
    # used. For example when only using the first 8 channels of the US band.
    # Note: when left blank / empty array, all channels will be enabled.
    enabled_uplink_channels=[72, 73, 74, 75, 76, 77, 78, 79]

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=2

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_cn779.toml"
content = """
# This file contains an example CN779 configuration.
[[regions]]

  # ID is an user-defined identifier for this region.
  id="cn779"

  # Description is a short description for this region.
  description="CN779"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="CN779"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="cn779"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=779500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=779700000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=779900000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=0

    # RX2 frequency (Hz)
    rx2_frequency=786000000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=5

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=3

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_eu433.toml"
content = """
# This file contains an example EU433 configuration.
[[regions]]

  # ID is an user-defined identifier for this region.
  id="eu433"

  # Description is a short description for this region.
  description="EU443"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="EU433"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="eu433"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=433175000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=433375000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=433575000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=0

    # RX2 frequency (Hz)
    rx2_frequency=434665000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=5

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=3

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_eu868.toml"
content = """
# This file contains an example EU868 configuration.
[[regions]]

  # ID is an user-defined identifier for this region.
  id="eu868"

  # Description is a short description for this region.
  description="EU868"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="EU868"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="eu868"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=868100000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=868300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=868500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=867100000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=867300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=867500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=867700000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=867900000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=868300000
      bandwidth=250000
      modulation="LORA"
      spreading_factors=[7]

    [[regions.gateway.channels]]
      frequency=868800000
      bandwidth=125000
      modulation="FSK"
      datarate=50000

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=0

    # RX2 frequency (Hz)
    rx2_frequency=869525000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=5

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=3

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0

    # Below is the common set of extra channels. Please make sure that these
    # channels are also supported by the gateways.
    [[regions.network.extra_channels]]
    frequency=867100000
    min_dr=0
    max_dr=5

    [[regions.network.extra_channels]]
    frequency=867300000
    min_dr=0
    max_dr=5

    [[regions.network.extra_channels]]
    frequency=867500000
    min_dr=0
    max_dr=5

    [[regions.network.extra_channels]]
    frequency=867700000
    min_dr=0
    max_dr=5

    [[regions.network.extra_channels]]
    frequency=867900000
    min_dr=0
    max_dr=5
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_in865.toml"
content = """
# This file contains an example IN865 configuration.
[[regions]]

  # ID is an user-defined identifier for this region.
  id="in865"

  # Description is a short description for this region.
  description="IN865"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="IN865"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="in865"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=865062500
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=865402500
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=865985000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=2

    # RX2 frequency (Hz)
    rx2_frequency=866550000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=5

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=4

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_ism2400.toml"
content = """
# This file contains an example ISM2400 configuration.
[[regions]]

  # ID is an user-defined identifier for this region.
  id="ism2400"

  # Description is a short description for this region.
  description="ISM2400"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="ISM2400"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="ism2400"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=2403000000
      bandwidth=812000
      modulation="LORA"
      spreading_factors=[12]

    [[regions.gateway.channels]]
      frequency=2479000000
      bandwidth=812000
      modulation="LORA"
      spreading_factors=[12]

    [[regions.gateway.channels]]
      frequency=2425000000
      bandwidth=812000
      modulation="LORA"
      spreading_factors=[12]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=0

    # RX2 frequency (Hz)
    rx2_frequency=2423000000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=7

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=0

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_kr920.toml"
content = """
# This file contains an example KR920 configuration.
[[regions]]

  # ID is an user-defined identifier for this region.
  id="kr920"

  # Description is a short description for this region.
  description="KR920"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="KR920"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="kr920"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=922100000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=922300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=922500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=0

    # RX2 frequency (Hz)
    rx2_frequency=921900000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=5

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=3

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_ru864.toml"
content = """
# This file contains an example RU864 configuration.
[[regions]]

  # ID is an user-defined identifier for this region.
  id="ru864"

  # Description is a short description for this region.
  description="RU864"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="RU864"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="ru864"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=868900000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

    [[regions.gateway.channels]]
      frequency=869100000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10, 11, 12]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=0

    # RX2 frequency (Hz)
    rx2_frequency=869100000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=5

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=3

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_us915_0.toml"
content = """
# This file contains an example US915 example (channels 0-7 + 64).
[[regions]]

  # ID is an use-defined identifier for this region.
  id="us915_0"

  # Description is a short description for this region.
  description="US915 (channels 0-7 + 64)"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="US915"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="us915_0"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=902300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=902500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=902700000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=902900000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=903100000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=903300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=903500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=903700000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=903000000
      bandwidth=500000
      modulation="LORA"
      spreading_factors=[8]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=8

    # RX2 frequency (Hz)
    rx2_frequency=923300000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=3

    # Enabled uplink channels.
    #
    # Use this when ony a sub-set of the by default enabled channels are being
    # used. For example when only using the first 8 channels of the US band.
    # Note: when left blank / empty array, all channels will be enabled.
    enabled_uplink_channels=[0, 1, 2, 3, 4, 5, 6, 7, 64]

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=8

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_us915_1.toml"
content = """
# This file contains an example US915 example (channels 8-15 + 65).
[[regions]]

  # ID is an use-defined identifier for this region.
  id="us915_1"

  # Description is a short description for this region.
  description="US915 (channels 8-15 + 65)"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="US915"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="us915_1"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=903900000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=904100000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=904300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=904500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=904700000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=904900000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=905100000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=905300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=904600000
      bandwidth=500000
      modulation="LORA"
      spreading_factors=[8]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=8

    # RX2 frequency (Hz)
    rx2_frequency=923300000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=3

    # Enabled uplink channels.
    #
    # Use this when ony a sub-set of the by default enabled channels are being
    # used. For example when only using the first 8 channels of the US band.
    # Note: when left blank / empty array, all channels will be enabled.
    enabled_uplink_channels=[8, 9, 10, 11, 12, 13, 14, 15, 65]

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=8

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_us915_2.toml"
content = """
# This file contains an example US915 example (channels 16-23 + 66).
[[regions]]

  # ID is an use-defined identifier for this region.
  id="us915_2"

  # Description is a short description for this region.
  description="US915 (channels 16-23 + 66)"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="US915"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="us915_2"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=905500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=905700000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=905900000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=906100000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=906300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=906500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=906700000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=906900000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=906200000
      bandwidth=500000
      modulation="LORA"
      spreading_factors=[8]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=8

    # RX2 frequency (Hz)
    rx2_frequency=923300000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=3

    # Enabled uplink channels.
    #
    # Use this when ony a sub-set of the by default enabled channels are being
    # used. For example when only using the first 8 channels of the US band.
    # Note: when left blank / empty array, all channels will be enabled.
    enabled_uplink_channels=[16, 17, 18, 19, 20, 21, 22, 23, 66]

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=8

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_us915_3.toml"
content = """
# This file contains an example US915 example (channels 24-31 + 67).
[[regions]]

  # ID is an use-defined identifier for this region.
  id="us915_3"

  # Description is a short description for this region.
  description="US915 (channels 24-31 + 67)"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="US915"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="us915_3"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=907100000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=907300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=907500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=907700000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=907900000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=908100000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=908300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=908500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=907800000
      bandwidth=500000
      modulation="LORA"
      spreading_factors=[8]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=8

    # RX2 frequency (Hz)
    rx2_frequency=923300000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=3

    # Enabled uplink channels.
    #
    # Use this when ony a sub-set of the by default enabled channels are being
    # used. For example when only using the first 8 channels of the US band.
    # Note: when left blank / empty array, all channels will be enabled.
    enabled_uplink_channels=[24, 25, 26, 27, 28, 29, 30, 31, 67]

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=8

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_us915_4.toml"
content = """
# This file contains an example US915 example (channels 32-39 + 68).
[[regions]]

  # ID is an use-defined identifier for this region.
  id="us915_4"

  # Description is a short description for this region.
  description="US915 (channels 32-39 + 68)"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="US915"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="us915_4"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=908700000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=908900000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=909100000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=909300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=909500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=909700000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=909900000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=910100000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=909400000
      bandwidth=500000
      modulation="LORA"
      spreading_factors=[8]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=8

    # RX2 frequency (Hz)
    rx2_frequency=923300000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=3

    # Enabled uplink channels.
    #
    # Use this when ony a sub-set of the by default enabled channels are being
    # used. For example when only using the first 8 channels of the US band.
    # Note: when left blank / empty array, all channels will be enabled.
    enabled_uplink_channels=[32, 33, 34, 35, 36, 37, 38, 39, 68]

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=8

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_us915_5.toml"
content = """
# This file contains an example US915 example (channels 40-47 + 69).
[[regions]]

  # ID is an use-defined identifier for this region.
  id="us915_5"

  # Description is a short description for this region.
  description="US915 (channels 40-47 + 69)"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="US915"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="us915_5"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=910300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=910500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=910700000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=910900000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=911100000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=911300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=911500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=911700000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=911000000
      bandwidth=500000
      modulation="LORA"
      spreading_factors=[8]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=8

    # RX2 frequency (Hz)
    rx2_frequency=923300000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=3

    # Enabled uplink channels.
    #
    # Use this when ony a sub-set of the by default enabled channels are being
    # used. For example when only using the first 8 channels of the US band.
    # Note: when left blank / empty array, all channels will be enabled.
    enabled_uplink_channels=[40, 41, 42, 43, 44, 45, 46, 47, 69]

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=8

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_us915_6.toml"
content = """
# This file contains an example US915 example (channels 48-55 + 70).
[[regions]]

  # ID is an use-defined identifier for this region.
  id="us915_6"

  # Description is a short description for this region.
  description="US915 (channels 48-55 + 70)"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="US915"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="us915_6"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=911900000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=912100000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=912300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=912500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=912700000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=912900000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=913100000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=913300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=912600000
      bandwidth=500000
      modulation="LORA"
      spreading_factors=[8]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=8

    # RX2 frequency (Hz)
    rx2_frequency=923300000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=3

    # Enabled uplink channels.
    #
    # Use this when ony a sub-set of the by default enabled channels are being
    # used. For example when only using the first 8 channels of the US band.
    # Note: when left blank / empty array, all channels will be enabled.
    enabled_uplink_channels=[48, 49, 50, 51, 52, 53, 54, 55, 70]

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=8

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack"
filePath = "/chirpstack/region_us915_7.toml"
content = """
# This file contains an example US915 example (channels 56-63 + 71).
[[regions]]

  # ID is an use-defined identifier for this region.
  id="us915_7"

  # Description is a short description for this region.
  description="US915 (channels 56-63 + 71)"

  # Common-name refers to the common-name of this region as defined by
  # the LoRa Alliance.
  common_name="US915"

  # Gateway configuration.
  [regions.gateway]

    # Force gateways as private.
    #
    # If enabled, gateways can only be used by devices under the same tenant.
    force_gws_private=false

    # Gateway backend configuration.
    [regions.gateway.backend]

      # The enabled backend type.
      enabled="mqtt"

      # MQTT configuration.
      [regions.gateway.backend.mqtt]

        # Topic prefix.
        #
        # The topic prefix can be used to define the region of the gateway.
        # Note, there is no need to add a trailing '/' to the prefix. The trailing
        # '/' is automatically added to the prefix if it is configured.
        topic_prefix="us915_7"

        # MQTT server (e.g. scheme://host:port where scheme is tcp, ssl or ws)
        server="tcp://mosquitto:1883"

        # Connect with the given username (optional)
        username=""

        # Connect with the given password (optional)
        password=""

        # Quality of service level
        #
        # 0: at most once
        # 1: at least once
        # 2: exactly once
        #
        # Note: an increase of this value will decrease the performance.
        # For more information: https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels
        qos=0

        # Clean session
        #
        # Set the "clean session" flag in the connect message when this client
        # connects to an MQTT broker. By setting this flag you are indicating
        # that no messages saved by the broker for this client should be delivered.
        clean_session=false

        # Client ID
        #
        # Set the client id to be used by this client when connecting to the MQTT
        # broker. A client id must be no longer than 23 characters. If left blank,
        # a random id will be generated by ChirpStack.
        client_id=""

        # Keep alive interval.
        #
        # This defines the maximum time that that should pass without communication
        # between the client and server.
        keep_alive_interval="30s"

        # CA certificate file (optional)
        #
        # Use this when setting up a secure connection (when server uses ssl://...)
        # but the certificate used by the server is not trusted by any CA certificate
        # on the server (e.g. when self generated).
        ca_cert=""

        # TLS certificate file (optional)
        tls_cert=""

        # TLS key file (optional)
        tls_key=""

    # Gateway channel configuration.
    #
    # Note: this configuration is only used in case the gateway is using the
    # ChirpStack Concentratord daemon. In any other case, this configuration
    # is ignored.
    [[regions.gateway.channels]]
      frequency=913500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=913700000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=913900000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=914100000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=914300000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=914500000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=914700000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=914900000
      bandwidth=125000
      modulation="LORA"
      spreading_factors=[7, 8, 9, 10]

    [[regions.gateway.channels]]
      frequency=914200000
      bandwidth=500000
      modulation="LORA"
      spreading_factors=[8]

  # Region specific network configuration.
  [regions.network]

    # Installation margin (dB) used by the ADR engine.
    #
    # A higher number means that the network-server will keep more margin,
    # resulting in a lower data-rate but decreasing the chance that the
    # device gets disconnected because it is unable to reach one of the
    # surrounded gateways.
    installation_margin=10

    # RX window (Class-A).
    #
    # Set this to:
    # 0: RX1 / RX2
    # 1: RX1 only
    # 2: RX2 only
    rx_window=0

    # RX1 delay (1 - 15 seconds).
    rx1_delay=1

    # RX1 data-rate offset
    rx1_dr_offset=0

    # RX2 data-rate
    rx2_dr=8

    # RX2 frequency (Hz)
    rx2_frequency=923300000

    # Prefer RX2 on RX1 data-rate less than.
    #
    # Prefer RX2 over RX1 based on the RX1 data-rate. When the RX1 data-rate
    # is smaller than the configured value, then the Network Server will
    # first try to schedule the downlink for RX2, failing that (e.g. the gateway
    # has already a payload scheduled at the RX2 timing) it will try RX1.
    rx2_prefer_on_rx1_dr_lt=0

    # Prefer RX2 on link budget.
    #
    # When the link-budget is better for RX2 than for RX1, the Network Server will first
    # try to schedule the downlink in RX2, failing that it will try RX1.
    rx2_prefer_on_link_budget=false

    # Downlink TX Power (dBm)
    #
    # When set to -1, the downlink TX Power from the configured band will
    # be used.
    #
    # Please consult the LoRaWAN Regional Parameters and local regulations
    # for valid and legal options. Note that the configured TX Power must be
    # supported by your gateway(s).
    downlink_tx_power=-1

    # ADR is disabled.
    adr_disabled=false

    # Minimum data-rate.
    min_dr=0

    # Maximum data-rate.
    max_dr=3

    # Enabled uplink channels.
    #
    # Use this when ony a sub-set of the by default enabled channels are being
    # used. For example when only using the first 8 channels of the US band.
    # Note: when left blank / empty array, all channels will be enabled.
    enabled_uplink_channels=[56, 57, 58, 59, 60, 61, 62, 63, 71]

    # Rejoin-request configuration (LoRaWAN 1.1)
    [regions.network.rejoin_request]

      # Request devices to periodically send rejoin-requests.
      enabled=false

      # The device must send a rejoin-request type 0 at least every 2^(max_count_n + 4)
      # uplink messages. Valid values are 0 to 15.
      max_count_n=0

      # The device must send a rejoin-request type 0 at least every 2^(max_time_n + 10)
      # seconds. Valid values are 0 to 15.
      #
      # 0  = roughly 17 minutes
      # 15 = about 1 year
      max_time_n=0

    # Class-B configuration.
    [regions.network.class_b]

      # Ping-slot data-rate.
      ping_slot_dr=8

      # Ping-slot frequency (Hz)
      #
      # set this to 0 to use the default frequency plan for the configured region
      # (which could be frequency hopping).
      ping_slot_frequency=0
"""

[[config.mounts]]
serviceName = "chirpstack-gateway-bridge"
filePath = "/chirpstack-gateway-bridge/chirpstack-gateway-bridge.toml"
content = """
# See https://www.chirpstack.io/gateway-bridge/install/config/ for a full
# configuration example and documentation.

[integration.mqtt.auth.generic]
servers=["tcp://mosquitto:1883"]
username=""
password=""
"""

[[config.mounts]]
serviceName = "chirpstack-gateway-bridge-basicstation"
filePath = "/chirpstack-gateway-bridge/chirpstack-gateway-bridge-basicstation-eu868.toml"
content = """
# See https://www.chirpstack.io/gateway-bridge/install/config/ for a full
# configuration example and documentation.

[integration.mqtt.auth.generic]
servers=["tcp://mosquitto:1883"]
username=""
password=""

[integration.mqtt]
event_topic_template="eu868/gateway/{{ .GatewayID }}/event/{{ .EventType }}"
state_topic_template="eu868/gateway/{{ .GatewayID }}/state/{{ .StateType }}"
command_topic_template="eu868/gateway/{{ .GatewayID }}/command/#"

[backend]
type="basic_station"

  [backend.basic_station]
  bind=":3001"
  tls_cert=""
  tls_key=""
  ca_cert=""

  region="EU868"
  frequency_min=863000000
  frequency_max=870000000

  [[backend.basic_station.concentrators]]

    [backend.basic_station.concentrators.multi_sf]
    frequencies=[
      868100000,
      868300000,
      868500000,
      867100000,
      867300000,
      867500000,
      867700000,
      867900000,
    ]

    [backend.basic_station.concentrators.lora_std]
    frequency=868300000
    bandwidth=250000
    spreading_factor=7

    [backend.basic_station.concentrators.fsk]
    frequency=868800000
"""

[[config.mounts]]
serviceName = "mosquitto"
filePath = "/mosquitto/config/mosquitto.conf"
content = """
listener 1883
allow_anonymous true
"""

[[config.mounts]]
serviceName = "postgres"
filePath = "/postgresql/initdb/001-chirpstack_extensions.sh"
content = """
#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname="$POSTGRES_DB" <<-EOSQL
    create extension pg_trgm;
    create extension hstore;
EOSQL
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBjaGlycHN0YWNrOlxuICAgIGltYWdlOiBjaGlycHN0YWNrL2NoaXJwc3RhY2s6NCBcbiAgICBjb21tYW5kOiAtYyAvZXRjL2NoaXJwc3RhY2tcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHZvbHVtZXM6XG4gICAgICAtIC4uL2ZpbGVzL2NoaXJwc3RhY2s6L2V0Yy9jaGlycHN0YWNrXG4gICAgcG9ydHM6XG4gICAgICAtIDgwODBcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gTVFUVF9CUk9LRVJfSE9TVD1tb3NxdWl0dG9cbiAgICAgIC0gUkVESVNfSE9TVD1yZWRpc1xuICAgICAgLSBQT1NUR1JFU1FMX0hPU1Q9cG9zdGdyZXNcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBwb3N0Z3Jlc1xuICAgICAgLSBtb3NxdWl0dG9cbiAgICAgIC0gcmVkaXNcblxuICBjaGlycHN0YWNrLWdhdGV3YXktYnJpZGdlOlxuICAgIGltYWdlOiBjaGlycHN0YWNrL2NoaXJwc3RhY2stZ2F0ZXdheS1icmlkZ2U6NFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgdm9sdW1lczpcbiAgICAgIC0gLi4vZmlsZXMvY2hpcnBzdGFjay1nYXRld2F5LWJyaWRnZTovZXRjL2NoaXJwc3RhY2stZ2F0ZXdheS1icmlkZ2VcbiAgICBwb3J0czpcbiAgICAgIC0gMTcwMC91ZHBcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gSU5URUdSQVRJT05fX01RVFRfX0VWRU5UX1RPUElDX1RFTVBMQVRFPWV1ODY4L2dhdGV3YXkve3sgLkdhdGV3YXlJRCB9fS9ldmVudC97eyAuRXZlbnRUeXBlIH19XG4gICAgICAtIElOVEVHUkFUSU9OX19NUVRUX19TVEFURV9UT1BJQ19URU1QTEFURT1ldTg2OC9nYXRld2F5L3t7IC5HYXRld2F5SUQgfX0vc3RhdGUve3sgLlN0YXRlVHlwZSB9fVxuICAgICAgLSBJTlRFR1JBVElPTl9fTVFUVF9fQ09NTUFORF9UT1BJQ19URU1QTEFURT1ldTg2OC9nYXRld2F5L3t7IC5HYXRld2F5SUQgfX0vY29tbWFuZC8jXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gbW9zcXVpdHRvXG5cbiAgY2hpcnBzdGFjay1nYXRld2F5LWJyaWRnZS1iYXNpY3N0YXRpb246XG4gICAgaW1hZ2U6IGNoaXJwc3RhY2svY2hpcnBzdGFjay1nYXRld2F5LWJyaWRnZTo0XG4gICAgY29tbWFuZDogLWMgL2V0Yy9jaGlycHN0YWNrLWdhdGV3YXktYnJpZGdlL2NoaXJwc3RhY2stZ2F0ZXdheS1icmlkZ2UtYmFzaWNzdGF0aW9uLWV1ODY4LnRvbWxcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHZvbHVtZXM6XG4gICAgICAtIC4uL2ZpbGVzL2NoaXJwc3RhY2stZ2F0ZXdheS1icmlkZ2U6L2V0Yy9jaGlycHN0YWNrLWdhdGV3YXktYnJpZGdlXG4gICAgcG9ydHM6XG4gICAgICAtIDMwMDFcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBtb3NxdWl0dG9cblxuICBjaGlycHN0YWNrLXJlc3QtYXBpOlxuICAgIGltYWdlOiBjaGlycHN0YWNrL2NoaXJwc3RhY2stcmVzdC1hcGk6NFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgY29tbWFuZDogLS1zZXJ2ZXIgY2hpcnBzdGFjazo4MDgwIC0tYmluZCAwLjAuMC4wOjgwOTAgLS1pbnNlY3VyZVxuICAgIHBvcnRzOlxuICAgICAgLSA4MDkwXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gY2hpcnBzdGFja1xuXG4gIHBvc3RncmVzOlxuICAgIGltYWdlOiBwb3N0Z3JlczoxNC1hbHBpbmVcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHZvbHVtZXM6XG4gICAgICAtIHBvc3RncmVzcWxkYXRhOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuICAgICAgLSAuLi9maWxlcy9wb3N0Z3Jlc3FsL2luaXRkYjovZG9ja2VyLWVudHJ5cG9pbnQtaW5pdGRiLmRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gUE9TVEdSRVNfVVNFUj1jaGlycHN0YWNrXG4gICAgICAtIFBPU1RHUkVTX1BBU1NXT1JEPSR7UE9TVEdSRVNfUEFTU1dPUkR9XG4gICAgICAtIFBPU1RHUkVTX0RCPWNoaXJwc3RhY2tcblxuICByZWRpczpcbiAgICBpbWFnZTogcmVkaXM6Ny1hbHBpbmVcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGNvbW1hbmQ6IHJlZGlzLXNlcnZlciAtLXNhdmUgMzAwIDEgLS1zYXZlIDYwIDEwMCAtLWFwcGVuZG9ubHkgbm9cbiAgICB2b2x1bWVzOlxuICAgICAgLSByZWRpc2RhdGE6L2RhdGFcblxuICBtb3NxdWl0dG86XG4gICAgaW1hZ2U6IGVjbGlwc2UtbW9zcXVpdHRvOjJcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHZvbHVtZXM6XG4gICAgICAtIC4uL2ZpbGVzL21vc3F1aXR0by9jb25maWcvOi9tb3NxdWl0dG8vY29uZmlnL1xuICAgIHBvcnRzOlxuICAgICAgLSAxODgzXG5cbnZvbHVtZXM6XG4gIHBvc3RncmVzcWxkYXRhOlxuICByZWRpc2RhdGE6XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuYXBpX3NlY3JldCA9IFwiJHtiYXNlNjQ6MzJ9XCJcbnBvc3RncmVzX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJjaGlycHN0YWNrXCJcbnBvcnQgPSA4MDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5wYXRoID0gXCIvXCJcblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiY2hpcnBzdGFjay1yZXN0LWFwaVwiXG5wb3J0ID0gODA5MFxuaG9zdCA9IFwiYXBpLSR7bWFpbl9kb21haW59XCJcbnBhdGggPSBcIi9cIlxuXG5bY29uZmlnLmVudl1cblBPU1RHUkVTX1BBU1NXT1JEID0gXCIke3Bvc3RncmVzX3Bhc3N3b3JkfVwiXG5cbltbY29uZmlnLm1vdW50c11dXG5zZXJ2aWNlTmFtZSA9IFwiY2hpcnBzdGFja1wiXG5maWxlUGF0aCA9IFwiL2NoaXJwc3RhY2svY2hpcnBzdGFjay50b21sXCJcbmNvbnRlbnQgPSBcIlwiXCJcbiMgTG9nZ2luZy5cbltsb2dnaW5nXVxuXG4gICMgTG9nIGxldmVsLlxuICAjXG4gICMgT3B0aW9ucyBhcmU6IHRyYWNlLCBkZWJ1ZywgaW5mbywgd2FybiBlcnJvci5cbiAgbGV2ZWw9XCJpbmZvXCJcblxuXG4jIFBvc3RncmVTUUwgY29uZmlndXJhdGlvbi5cbltwb3N0Z3Jlc3FsXVxuXG4gICMgUG9zdGdyZVNRTCBEU04uXG4gICNcbiAgIyBGb3JtYXQgZXhhbXBsZTogcG9zdGdyZXM6Ly88VVNFUk5BTUU+OjxQQVNTV09SRD5APEhPU1ROQU1FPi88REFUQUJBU0U+P3NzbG1vZGU9PFNTTE1PREU+LlxuICAjXG4gICMgU1NMIG1vZGUgb3B0aW9uczpcbiAgIyAgKiBkaXNhYmxlIC0gRG8gbm90IHVzZSBUTFNcbiAgIyAgKiBwcmVmZXIgLSBBdHRlbXB0IHRvIGNvbm5lY3Qgd2l0aCBUTFMgYnV0IGFsbG93IHNlc3Npb25zIHdpdGhvdXRcbiAgIyAgKiByZXF1aXJlIC0gUmVxdWlyZSB0aGUgdXNlIG9mIFRMU1xuICBkc249XCJwb3N0Z3JlczovL2NoaXJwc3RhY2s6JHtwb3N0Z3Jlc19wYXNzd29yZH1AcG9zdGdyZXMvY2hpcnBzdGFjaz9zc2xtb2RlPWRpc2FibGVcIlxuXG4gICMgTWF4IG9wZW4gY29ubmVjdGlvbnMuXG4gICNcbiAgIyBUaGlzIHNldHMgdGhlIG1heC4gbnVtYmVyIG9mIG9wZW4gY29ubmVjdGlvbnMgdGhhdCBhcmUgYWxsb3dlZCBpbiB0aGVcbiAgIyBQb3N0Z3JlU1FMIGNvbm5lY3Rpb24gcG9vbC5cbiAgbWF4X29wZW5fY29ubmVjdGlvbnM9MTBcblxuICAjIE1pbiBpZGxlIGNvbm5lY3Rpb25zLlxuICAjXG4gICMgVGhpcyBzZXRzIHRoZSBtaW4uIG51bWJlciBvZiBpZGxlIGNvbm5lY3Rpb25zIGluIHRoZSBQb3N0Z3JlU1FMIGNvbm5lY3Rpb25cbiAgIyBwb29sICgwID0gZXF1YWwgdG8gbWF4X29wZW5fY29ubmVjdGlvbnMpLlxuICBtaW5faWRsZV9jb25uZWN0aW9ucz0wXG5cblxuIyBSZWRpcyBjb25maWd1cmF0aW9uLlxuW3JlZGlzXVxuXG4gICMgU2VydmVyIGFkZHJlc3Mgb3IgYWRkcmVzc2VzLlxuICAjXG4gICMgU2V0IG11bHRpcGxlIGFkZHJlc3NlcyB3aGVuIGNvbm5lY3RpbmcgdG8gYSBjbHVzdGVyLlxuICBzZXJ2ZXJzPVtcbiAgICBcInJlZGlzOi8vcmVkaXMvXCIsXG4gIF1cblxuICAjIFRMUyBlbmFibGVkLlxuICB0bHNfZW5hYmxlZD1mYWxzZVxuXG4gICMgUmVkaXMgQ2x1c3Rlci5cbiAgI1xuICAjIFNldCB0aGlzIHRvIHRydWUgd2hlbiB0aGUgcHJvdmlkZWQgVVJMcyBhcmUgcG9pbnRpbmcgdG8gYSBSZWRpcyBDbHVzdGVyXG4gICMgaW5zdGFuY2UuXG4gIGNsdXN0ZXI9ZmFsc2VcblxuXG4jIE5ldHdvcmsgcmVsYXRlZCBjb25maWd1cmF0aW9uLlxuW25ldHdvcmtdXG5cbiAgIyBOZXR3b3JrIGlkZW50aWZpZXIgKE5ldElELCAzIGJ5dGVzKSBlbmNvZGVkIGFzIEhFWCAoZS5nLiAwMTAyMDMpLlxuICBuZXRfaWQ9XCIwMDAwMDBcIlxuXG4gICMgRW5hYmxlZCByZWdpb25zLlxuICAjXG4gICMgTXVsdGlwbGUgcmVnaW9ucyBjYW4gYmUgZW5hYmxlZCBzaW11bHRhbmVvdXNseS4gRWFjaCByZWdpb24gbXVzdCBtYXRjaFxuICAjIHRoZSAnbmFtZScgcGFyYW1ldGVyIG9mIHRoZSByZWdpb24gY29uZmlndXJhdGlvbiBpbiAnW1tyZWdpb25zXV0nLlxuICBlbmFibGVkX3JlZ2lvbnM9W1xuICAgIFwiYXM5MjNcIixcbiAgICBcImFzOTIzXzJcIixcbiAgICBcImFzOTIzXzNcIixcbiAgICBcImFzOTIzXzRcIixcbiAgICBcImF1OTE1XzBcIixcbiAgICBcImNuNDcwXzEwXCIsXG4gICAgXCJjbjc3OVwiLFxuICAgIFwiZXU0MzNcIixcbiAgICBcImV1ODY4XCIsXG4gICAgXCJpbjg2NVwiLFxuICAgIFwiaXNtMjQwMFwiLFxuICAgIFwia3I5MjBcIixcbiAgICBcInJ1ODY0XCIsXG4gICAgXCJ1czkxNV8wXCIsXG4gICAgXCJ1czkxNV8xXCIsXG4gIF1cblxuXG4jIEFQSSBpbnRlcmZhY2UgY29uZmlndXJhdGlvbi5cblthcGldXG5cbiAgIyBpbnRlcmZhY2U6cG9ydCB0byBiaW5kIHRoZSBBUEkgaW50ZXJmYWNlIHRvLlxuICBiaW5kPVwiMC4wLjAuMDo4MDgwXCJcblxuICAjIFNlY3JldC5cbiAgI1xuICAjIFRoaXMgc2VjcmV0IGlzIHVzZWQgZm9yIGdlbmVyYXRpbmcgbG9naW4gYW5kIEFQSSB0b2tlbnMsIG1ha2Ugc3VyZSB0aGlzXG4gICMgaXMgbmV2ZXIgZXhwb3NlZC4gQ2hhbmdpbmcgdGhpcyBzZWNyZXQgd2lsbCBpbnZhbGlkYXRlIGFsbCBsb2dpbiBhbmQgQVBJXG4gICMgdG9rZW5zLiBUaGUgZm9sbG93aW5nIGNvbW1hbmQgY2FuIGJlIHVzZWQgdG8gZ2VuZXJhdGUgYSByYW5kb20gc2VjcmV0OlxuICAjICAgb3BlbnNzbCByYW5kIC1iYXNlNjQgMzJcbiAgc2VjcmV0PVwiJHthcGlfc2VjcmV0fVwiXG5cblxuW2ludGVncmF0aW9uXVxuICBlbmFibGVkPVtcIm1xdHRcIl1cblxuICBbaW50ZWdyYXRpb24ubXF0dF1cbiAgICBzZXJ2ZXI9XCJ0Y3A6Ly9tb3NxdWl0dG86MTg4My9cIlxuICAgIGpzb249dHJ1ZVxuXCJcIlwiXG5cbltbY29uZmlnLm1vdW50c11dXG5zZXJ2aWNlTmFtZSA9IFwiY2hpcnBzdGFja1wiXG5maWxlUGF0aCA9IFwiL2NoaXJwc3RhY2svcmVnaW9uX2FzOTIzXzIudG9tbFwiXG5jb250ZW50ID0gXCJcIlwiXG4jIFRoaXMgZmlsZSBjb250YWlucyBhbiBleGFtcGxlIEFTOTIzXzIgY29uZmlndXJhdGlvbi5cbltbcmVnaW9uc11dXG5cbiAgIyBJRCBpcyBhbiB1c2VyLWRlZmluZWQgaWRlbnRpZmllciBmb3IgdGhpcyByZWdpb24uXG4gIGlkPVwiYXM5MjNfMlwiXG5cbiAgIyBEZXNjcmlwdGlvbiBpcyBhIHNob3J0IGRlc2NyaXB0aW9uIGZvciB0aGlzIHJlZ2lvbi5cbiAgZGVzY3JpcHRpb249XCJBUzkyMy0yXCJcblxuICAjIENvbW1vbi1uYW1lIHJlZmVycyB0byB0aGUgY29tbW9uLW5hbWUgb2YgdGhpcyByZWdpb24gYXMgZGVmaW5lZCBieVxuICAjIHRoZSBMb1JhIEFsbGlhbmNlLlxuICBjb21tb25fbmFtZT1cIkFTOTIzXzJcIlxuXG5cbiAgIyBHYXRld2F5IGNvbmZpZ3VyYXRpb24uXG4gIFtyZWdpb25zLmdhdGV3YXldXG5cbiAgICAjIEZvcmNlIGdhdGV3YXlzIGFzIHByaXZhdGUuXG4gICAgI1xuICAgICMgSWYgZW5hYmxlZCwgZ2F0ZXdheXMgY2FuIG9ubHkgYmUgdXNlZCBieSBkZXZpY2VzIHVuZGVyIHRoZSBzYW1lIHRlbmFudC5cbiAgICBmb3JjZV9nd3NfcHJpdmF0ZT1mYWxzZVxuXG5cbiAgICAjIEdhdGV3YXkgYmFja2VuZCBjb25maWd1cmF0aW9uLlxuICAgIFtyZWdpb25zLmdhdGV3YXkuYmFja2VuZF1cblxuICAgICAgIyBUaGUgZW5hYmxlZCBiYWNrZW5kIHR5cGUuXG4gICAgICBlbmFibGVkPVwibXF0dFwiXG5cbiAgICAgICMgTVFUVCBjb25maWd1cmF0aW9uLlxuICAgICAgW3JlZ2lvbnMuZ2F0ZXdheS5iYWNrZW5kLm1xdHRdXG5cbiAgICAgICAgIyBUb3BpYyBwcmVmaXguXG4gICAgICAgICNcbiAgICAgICAgIyBUaGUgdG9waWMgcHJlZml4IGNhbiBiZSB1c2VkIHRvIGRlZmluZSB0aGUgcmVnaW9uIG9mIHRoZSBnYXRld2F5LlxuICAgICAgICAjIE5vdGUsIHRoZXJlIGlzIG5vIG5lZWQgdG8gYWRkIGEgdHJhaWxpbmcgJy8nIHRvIHRoZSBwcmVmaXguIFRoZSB0cmFpbGluZ1xuICAgICAgICAjICcvJyBpcyBhdXRvbWF0aWNhbGx5IGFkZGVkIHRvIHRoZSBwcmVmaXggaWYgaXQgaXMgY29uZmlndXJlZC5cbiAgICAgICAgdG9waWNfcHJlZml4PVwiYXM5MjNfMlwiXG5cbiAgICAgICAgIyBNUVRUIHNlcnZlciAoZS5nLiBzY2hlbWU6Ly9ob3N0OnBvcnQgd2hlcmUgc2NoZW1lIGlzIHRjcCwgc3NsIG9yIHdzKVxuICAgICAgICBzZXJ2ZXI9XCJ0Y3A6Ly9tb3NxdWl0dG86MTg4M1wiXG5cbiAgICAgICAgIyBDb25uZWN0IHdpdGggdGhlIGdpdmVuIHVzZXJuYW1lIChvcHRpb25hbClcbiAgICAgICAgdXNlcm5hbWU9XCJcIlxuXG4gICAgICAgICMgQ29ubmVjdCB3aXRoIHRoZSBnaXZlbiBwYXNzd29yZCAob3B0aW9uYWwpXG4gICAgICAgIHBhc3N3b3JkPVwiXCJcblxuICAgICAgICAjIFF1YWxpdHkgb2Ygc2VydmljZSBsZXZlbFxuICAgICAgICAjXG4gICAgICAgICMgMDogYXQgbW9zdCBvbmNlXG4gICAgICAgICMgMTogYXQgbGVhc3Qgb25jZVxuICAgICAgICAjIDI6IGV4YWN0bHkgb25jZVxuICAgICAgICAjXG4gICAgICAgICMgTm90ZTogYW4gaW5jcmVhc2Ugb2YgdGhpcyB2YWx1ZSB3aWxsIGRlY3JlYXNlIHRoZSBwZXJmb3JtYW5jZS5cbiAgICAgICAgIyBGb3IgbW9yZSBpbmZvcm1hdGlvbjogaHR0cHM6Ly93d3cuaGl2ZW1xLmNvbS9ibG9nL21xdHQtZXNzZW50aWFscy1wYXJ0LTYtbXF0dC1xdWFsaXR5LW9mLXNlcnZpY2UtbGV2ZWxzXG4gICAgICAgIHFvcz0wXG5cbiAgICAgICAgIyBDbGVhbiBzZXNzaW9uXG4gICAgICAgICNcbiAgICAgICAgIyBTZXQgdGhlIFwiY2xlYW4gc2Vzc2lvblwiIGZsYWcgaW4gdGhlIGNvbm5lY3QgbWVzc2FnZSB3aGVuIHRoaXMgY2xpZW50XG4gICAgICAgICMgY29ubmVjdHMgdG8gYW4gTVFUVCBicm9rZXIuIEJ5IHNldHRpbmcgdGhpcyBmbGFnIHlvdSBhcmUgaW5kaWNhdGluZ1xuICAgICAgICAjIHRoYXQgbm8gbWVzc2FnZXMgc2F2ZWQgYnkgdGhlIGJyb2tlciBmb3IgdGhpcyBjbGllbnQgc2hvdWxkIGJlIGRlbGl2ZXJlZC5cbiAgICAgICAgY2xlYW5fc2Vzc2lvbj1mYWxzZVxuXG4gICAgICAgICMgQ2xpZW50IElEXG4gICAgICAgICNcbiAgICAgICAgIyBTZXQgdGhlIGNsaWVudCBpZCB0byBiZSB1c2VkIGJ5IHRoaXMgY2xpZW50IHdoZW4gY29ubmVjdGluZyB0byB0aGUgTVFUVFxuICAgICAgICAjIGJyb2tlci4gQSBjbGllbnQgaWQgbXVzdCBiZSBubyBsb25nZXIgdGhhbiAyMyBjaGFyYWN0ZXJzLiBJZiBsZWZ0IGJsYW5rLFxuICAgICAgICAjIGEgcmFuZG9tIGlkIHdpbGwgYmUgZ2VuZXJhdGVkIGJ5IENoaXJwU3RhY2suXG4gICAgICAgIGNsaWVudF9pZD1cIlwiXG5cbiAgICAgICAgIyBLZWVwIGFsaXZlIGludGVydmFsLlxuICAgICAgICAjXG4gICAgICAgICMgVGhpcyBkZWZpbmVzIHRoZSBtYXhpbXVtIHRpbWUgdGhhdCB0aGF0IHNob3VsZCBwYXNzIHdpdGhvdXQgY29tbXVuaWNhdGlvblxuICAgICAgICAjIGJldHdlZW4gdGhlIGNsaWVudCBhbmQgc2VydmVyLlxuICAgICAgICBrZWVwX2FsaXZlX2ludGVydmFsPVwiMzBzXCJcblxuICAgICAgICAjIENBIGNlcnRpZmljYXRlIGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICAjXG4gICAgICAgICMgVXNlIHRoaXMgd2hlbiBzZXR0aW5nIHVwIGEgc2VjdXJlIGNvbm5lY3Rpb24gKHdoZW4gc2VydmVyIHVzZXMgc3NsOi8vLi4uKVxuICAgICAgICAjIGJ1dCB0aGUgY2VydGlmaWNhdGUgdXNlZCBieSB0aGUgc2VydmVyIGlzIG5vdCB0cnVzdGVkIGJ5IGFueSBDQSBjZXJ0aWZpY2F0ZVxuICAgICAgICAjIG9uIHRoZSBzZXJ2ZXIgKGUuZy4gd2hlbiBzZWxmIGdlbmVyYXRlZCkuXG4gICAgICAgIGNhX2NlcnQ9XCJcIlxuXG4gICAgICAgICMgVExTIGNlcnRpZmljYXRlIGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICB0bHNfY2VydD1cIlwiXG5cbiAgICAgICAgIyBUTFMga2V5IGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICB0bHNfa2V5PVwiXCJcblxuXG4gICAgIyBHYXRld2F5IGNoYW5uZWwgY29uZmlndXJhdGlvbi5cbiAgICAjXG4gICAgIyBOb3RlOiB0aGlzIGNvbmZpZ3VyYXRpb24gaXMgb25seSB1c2VkIGluIGNhc2UgdGhlIGdhdGV3YXkgaXMgdXNpbmcgdGhlXG4gICAgIyBDaGlycFN0YWNrIENvbmNlbnRyYXRvcmQgZGFlbW9uLiBJbiBhbnkgb3RoZXIgY2FzZSwgdGhpcyBjb25maWd1cmF0aW9uIFxuICAgICMgaXMgaWdub3JlZC5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTIxNDAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MjE2MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG5cbiAgIyBSZWdpb24gc3BlY2lmaWMgbmV0d29yayBjb25maWd1cmF0aW9uLlxuICBbcmVnaW9ucy5uZXR3b3JrXVxuICAgIFxuICAgICMgSW5zdGFsbGF0aW9uIG1hcmdpbiAoZEIpIHVzZWQgYnkgdGhlIEFEUiBlbmdpbmUuXG4gICAgI1xuICAgICMgQSBoaWdoZXIgbnVtYmVyIG1lYW5zIHRoYXQgdGhlIG5ldHdvcmstc2VydmVyIHdpbGwga2VlcCBtb3JlIG1hcmdpbixcbiAgICAjIHJlc3VsdGluZyBpbiBhIGxvd2VyIGRhdGEtcmF0ZSBidXQgZGVjcmVhc2luZyB0aGUgY2hhbmNlIHRoYXQgdGhlXG4gICAgIyBkZXZpY2UgZ2V0cyBkaXNjb25uZWN0ZWQgYmVjYXVzZSBpdCBpcyB1bmFibGUgdG8gcmVhY2ggb25lIG9mIHRoZVxuICAgICMgc3Vycm91bmRlZCBnYXRld2F5cy5cbiAgICBpbnN0YWxsYXRpb25fbWFyZ2luPTEwXG5cbiAgICAjIFJYIHdpbmRvdyAoQ2xhc3MtQSkuXG4gICAgI1xuICAgICMgU2V0IHRoaXMgdG86XG4gICAgIyAwOiBSWDEgLyBSWDJcbiAgICAjIDE6IFJYMSBvbmx5XG4gICAgIyAyOiBSWDIgb25seVxuICAgIHJ4X3dpbmRvdz0wXG5cbiAgICAjIFJYMSBkZWxheSAoMSAtIDE1IHNlY29uZHMpLlxuICAgIHJ4MV9kZWxheT0xXG5cbiAgICAjIFJYMSBkYXRhLXJhdGUgb2Zmc2V0XG4gICAgcngxX2RyX29mZnNldD0wXG5cbiAgICAjIFJYMiBkYXRhLXJhdGVcbiAgICByeDJfZHI9MFxuXG4gICAgIyBSWDIgZnJlcXVlbmN5IChIeilcbiAgICByeDJfZnJlcXVlbmN5PTkyMTQwMDAwMFxuXG4gICAgIyBQcmVmZXIgUlgyIG9uIFJYMSBkYXRhLXJhdGUgbGVzcyB0aGFuLlxuICAgICNcbiAgICAjIFByZWZlciBSWDIgb3ZlciBSWDEgYmFzZWQgb24gdGhlIFJYMSBkYXRhLXJhdGUuIFdoZW4gdGhlIFJYMSBkYXRhLXJhdGVcbiAgICAjIGlzIHNtYWxsZXIgdGhhbiB0aGUgY29uZmlndXJlZCB2YWx1ZSwgdGhlbiB0aGUgTmV0d29yayBTZXJ2ZXIgd2lsbFxuICAgICMgZmlyc3QgdHJ5IHRvIHNjaGVkdWxlIHRoZSBkb3dubGluayBmb3IgUlgyLCBmYWlsaW5nIHRoYXQgKGUuZy4gdGhlIGdhdGV3YXlcbiAgICAjIGhhcyBhbHJlYWR5IGEgcGF5bG9hZCBzY2hlZHVsZWQgYXQgdGhlIFJYMiB0aW1pbmcpIGl0IHdpbGwgdHJ5IFJYMS5cbiAgICByeDJfcHJlZmVyX29uX3J4MV9kcl9sdD0wXG5cbiAgICAjIFByZWZlciBSWDIgb24gbGluayBidWRnZXQuXG4gICAgI1xuICAgICMgV2hlbiB0aGUgbGluay1idWRnZXQgaXMgYmV0dGVyIGZvciBSWDIgdGhhbiBmb3IgUlgxLCB0aGUgTmV0d29yayBTZXJ2ZXIgd2lsbCBmaXJzdFxuICAgICMgdHJ5IHRvIHNjaGVkdWxlIHRoZSBkb3dubGluayBpbiBSWDIsIGZhaWxpbmcgdGhhdCBpdCB3aWxsIHRyeSBSWDEuXG4gICAgcngyX3ByZWZlcl9vbl9saW5rX2J1ZGdldD1mYWxzZVxuXG4gICAgIyBEb3dubGluayBUWCBQb3dlciAoZEJtKVxuICAgICNcbiAgICAjIFdoZW4gc2V0IHRvIC0xLCB0aGUgZG93bmxpbmsgVFggUG93ZXIgZnJvbSB0aGUgY29uZmlndXJlZCBiYW5kIHdpbGxcbiAgICAjIGJlIHVzZWQuXG4gICAgI1xuICAgICMgUGxlYXNlIGNvbnN1bHQgdGhlIExvUmFXQU4gUmVnaW9uYWwgUGFyYW1ldGVycyBhbmQgbG9jYWwgcmVndWxhdGlvbnNcbiAgICAjIGZvciB2YWxpZCBhbmQgbGVnYWwgb3B0aW9ucy4gTm90ZSB0aGF0IHRoZSBjb25maWd1cmVkIFRYIFBvd2VyIG11c3QgYmVcbiAgICAjIHN1cHBvcnRlZCBieSB5b3VyIGdhdGV3YXkocykuXG4gICAgZG93bmxpbmtfdHhfcG93ZXI9LTFcblxuICAgICMgQURSIGlzIGRpc2FibGVkLlxuICAgIGFkcl9kaXNhYmxlZD1mYWxzZVxuXG4gICAgIyBNaW5pbXVtIGRhdGEtcmF0ZS5cbiAgICBtaW5fZHI9MFxuXG4gICAgIyBNYXhpbXVtIGRhdGEtcmF0ZS5cbiAgICBtYXhfZHI9NVxuXG5cbiAgICAjIFJlam9pbi1yZXF1ZXN0IGNvbmZpZ3VyYXRpb24gKExvUmFXQU4gMS4xKVxuICAgIFtyZWdpb25zLm5ldHdvcmsucmVqb2luX3JlcXVlc3RdXG5cbiAgICAgICMgUmVxdWVzdCBkZXZpY2VzIHRvIHBlcmlvZGljYWxseSBzZW5kIHJlam9pbi1yZXF1ZXN0cy5cbiAgICAgIGVuYWJsZWQ9ZmFsc2VcblxuICAgICAgIyBUaGUgZGV2aWNlIG11c3Qgc2VuZCBhIHJlam9pbi1yZXF1ZXN0IHR5cGUgMCBhdCBsZWFzdCBldmVyeSAyXihtYXhfY291bnRfbiArIDQpXG4gICAgICAjIHVwbGluayBtZXNzYWdlcy4gVmFsaWQgdmFsdWVzIGFyZSAwIHRvIDE1LlxuICAgICAgbWF4X2NvdW50X249MFxuXG4gICAgICAjIFRoZSBkZXZpY2UgbXVzdCBzZW5kIGEgcmVqb2luLXJlcXVlc3QgdHlwZSAwIGF0IGxlYXN0IGV2ZXJ5IDJeKG1heF90aW1lX24gKyAxMClcbiAgICAgICMgc2Vjb25kcy4gVmFsaWQgdmFsdWVzIGFyZSAwIHRvIDE1LlxuICAgICAgI1xuICAgICAgIyAwICA9IHJvdWdobHkgMTcgbWludXRlc1xuICAgICAgIyAxNSA9IGFib3V0IDEgeWVhclxuICAgICAgbWF4X3RpbWVfbj0wXG4gICAgXG5cbiAgICAjIENsYXNzLUIgY29uZmlndXJhdGlvbi5cbiAgICBbcmVnaW9ucy5uZXR3b3JrLmNsYXNzX2JdXG5cbiAgICAgICMgUGluZy1zbG90IGRhdGEtcmF0ZS4gXG4gICAgICBwaW5nX3Nsb3RfZHI9M1xuXG4gICAgICAjIFBpbmctc2xvdCBmcmVxdWVuY3kgKEh6KVxuICAgICAgI1xuICAgICAgIyBzZXQgdGhpcyB0byAwIHRvIHVzZSB0aGUgZGVmYXVsdCBmcmVxdWVuY3kgcGxhbiBmb3IgdGhlIGNvbmZpZ3VyZWQgcmVnaW9uXG4gICAgICAjICh3aGljaCBjb3VsZCBiZSBmcmVxdWVuY3kgaG9wcGluZykuXG4gICAgICBwaW5nX3Nsb3RfZnJlcXVlbmN5PTBcblwiXCJcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuc2VydmljZU5hbWUgPSBcImNoaXJwc3RhY2tcIlxuZmlsZVBhdGggPSBcIi9jaGlycHN0YWNrL3JlZ2lvbl9hczkyM18zLnRvbWxcIlxuY29udGVudCA9IFwiXCJcIlxuIyBUaGlzIGZpbGUgY29udGFpbnMgYW4gZXhhbXBsZSBBUzkyM18zIGNvbmZpZ3VyYXRpb24uXG5bW3JlZ2lvbnNdXVxuXG4gICMgSUQgaXMgYW4gdXNlci1kZWZpbmVkIGlkZW50aWZpZXIgZm9yIHRoaXMgcmVnaW9uLlxuICBpZD1cImFzOTIzXzNcIlxuXG4gICMgRGVzY3JpcHRpb24gaXMgYSBzaG9ydCBkZXNjcmlwdGlvbiBmb3IgdGhpcyByZWdpb24uXG4gIGRlc2NyaXB0aW9uPVwiQVM5MjMtM1wiXG5cbiAgIyBDb21tb24tbmFtZSByZWZlcnMgdG8gdGhlIGNvbW1vbi1uYW1lIG9mIHRoaXMgcmVnaW9uIGFzIGRlZmluZWQgYnlcbiAgIyB0aGUgTG9SYSBBbGxpYW5jZS5cbiAgY29tbW9uX25hbWU9XCJBUzkyM18zXCJcblxuXG4gICMgR2F0ZXdheSBjb25maWd1cmF0aW9uLlxuICBbcmVnaW9ucy5nYXRld2F5XVxuXG4gICAgIyBGb3JjZSBnYXRld2F5cyBhcyBwcml2YXRlLlxuICAgICNcbiAgICAjIElmIGVuYWJsZWQsIGdhdGV3YXlzIGNhbiBvbmx5IGJlIHVzZWQgYnkgZGV2aWNlcyB1bmRlciB0aGUgc2FtZSB0ZW5hbnQuXG4gICAgZm9yY2VfZ3dzX3ByaXZhdGU9ZmFsc2VcblxuXG4gICAgIyBHYXRld2F5IGJhY2tlbmQgY29uZmlndXJhdGlvbi5cbiAgICBbcmVnaW9ucy5nYXRld2F5LmJhY2tlbmRdXG5cbiAgICAgICMgVGhlIGVuYWJsZWQgYmFja2VuZCB0eXBlLlxuICAgICAgZW5hYmxlZD1cIm1xdHRcIlxuXG4gICAgICAjIE1RVFQgY29uZmlndXJhdGlvbi5cbiAgICAgIFtyZWdpb25zLmdhdGV3YXkuYmFja2VuZC5tcXR0XVxuXG4gICAgICAgICMgVG9waWMgcHJlZml4LlxuICAgICAgICAjXG4gICAgICAgICMgVGhlIHRvcGljIHByZWZpeCBjYW4gYmUgdXNlZCB0byBkZWZpbmUgdGhlIHJlZ2lvbiBvZiB0aGUgZ2F0ZXdheS5cbiAgICAgICAgIyBOb3RlLCB0aGVyZSBpcyBubyBuZWVkIHRvIGFkZCBhIHRyYWlsaW5nICcvJyB0byB0aGUgcHJlZml4LiBUaGUgdHJhaWxpbmdcbiAgICAgICAgIyAnLycgaXMgYXV0b21hdGljYWxseSBhZGRlZCB0byB0aGUgcHJlZml4IGlmIGl0IGlzIGNvbmZpZ3VyZWQuXG4gICAgICAgIHRvcGljX3ByZWZpeD1cImFzOTIzXzNcIlxuXG4gICAgICAgICMgTVFUVCBzZXJ2ZXIgKGUuZy4gc2NoZW1lOi8vaG9zdDpwb3J0IHdoZXJlIHNjaGVtZSBpcyB0Y3AsIHNzbCBvciB3cylcbiAgICAgICAgc2VydmVyPVwidGNwOi8vbW9zcXVpdHRvOjE4ODNcIlxuXG4gICAgICAgICMgQ29ubmVjdCB3aXRoIHRoZSBnaXZlbiB1c2VybmFtZSAob3B0aW9uYWwpXG4gICAgICAgIHVzZXJuYW1lPVwiXCJcblxuICAgICAgICAjIENvbm5lY3Qgd2l0aCB0aGUgZ2l2ZW4gcGFzc3dvcmQgKG9wdGlvbmFsKVxuICAgICAgICBwYXNzd29yZD1cIlwiXG5cbiAgICAgICAgIyBRdWFsaXR5IG9mIHNlcnZpY2UgbGV2ZWxcbiAgICAgICAgI1xuICAgICAgICAjIDA6IGF0IG1vc3Qgb25jZVxuICAgICAgICAjIDE6IGF0IGxlYXN0IG9uY2VcbiAgICAgICAgIyAyOiBleGFjdGx5IG9uY2VcbiAgICAgICAgI1xuICAgICAgICAjIE5vdGU6IGFuIGluY3JlYXNlIG9mIHRoaXMgdmFsdWUgd2lsbCBkZWNyZWFzZSB0aGUgcGVyZm9ybWFuY2UuXG4gICAgICAgICMgRm9yIG1vcmUgaW5mb3JtYXRpb246IGh0dHBzOi8vd3d3LmhpdmVtcS5jb20vYmxvZy9tcXR0LWVzc2VudGlhbHMtcGFydC02LW1xdHQtcXVhbGl0eS1vZi1zZXJ2aWNlLWxldmVsc1xuICAgICAgICBxb3M9MFxuXG4gICAgICAgICMgQ2xlYW4gc2Vzc2lvblxuICAgICAgICAjXG4gICAgICAgICMgU2V0IHRoZSBcImNsZWFuIHNlc3Npb25cIiBmbGFnIGluIHRoZSBjb25uZWN0IG1lc3NhZ2Ugd2hlbiB0aGlzIGNsaWVudFxuICAgICAgICAjIGNvbm5lY3RzIHRvIGFuIE1RVFQgYnJva2VyLiBCeSBzZXR0aW5nIHRoaXMgZmxhZyB5b3UgYXJlIGluZGljYXRpbmdcbiAgICAgICAgIyB0aGF0IG5vIG1lc3NhZ2VzIHNhdmVkIGJ5IHRoZSBicm9rZXIgZm9yIHRoaXMgY2xpZW50IHNob3VsZCBiZSBkZWxpdmVyZWQuXG4gICAgICAgIGNsZWFuX3Nlc3Npb249ZmFsc2VcblxuICAgICAgICAjIENsaWVudCBJRFxuICAgICAgICAjXG4gICAgICAgICMgU2V0IHRoZSBjbGllbnQgaWQgdG8gYmUgdXNlZCBieSB0aGlzIGNsaWVudCB3aGVuIGNvbm5lY3RpbmcgdG8gdGhlIE1RVFRcbiAgICAgICAgIyBicm9rZXIuIEEgY2xpZW50IGlkIG11c3QgYmUgbm8gbG9uZ2VyIHRoYW4gMjMgY2hhcmFjdGVycy4gSWYgbGVmdCBibGFuayxcbiAgICAgICAgIyBhIHJhbmRvbSBpZCB3aWxsIGJlIGdlbmVyYXRlZCBieSBDaGlycFN0YWNrLlxuICAgICAgICBjbGllbnRfaWQ9XCJcIlxuXG4gICAgICAgICMgS2VlcCBhbGl2ZSBpbnRlcnZhbC5cbiAgICAgICAgI1xuICAgICAgICAjIFRoaXMgZGVmaW5lcyB0aGUgbWF4aW11bSB0aW1lIHRoYXQgdGhhdCBzaG91bGQgcGFzcyB3aXRob3V0IGNvbW11bmljYXRpb25cbiAgICAgICAgIyBiZXR3ZWVuIHRoZSBjbGllbnQgYW5kIHNlcnZlci5cbiAgICAgICAga2VlcF9hbGl2ZV9pbnRlcnZhbD1cIjMwc1wiXG5cbiAgICAgICAgIyBDQSBjZXJ0aWZpY2F0ZSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgI1xuICAgICAgICAjIFVzZSB0aGlzIHdoZW4gc2V0dGluZyB1cCBhIHNlY3VyZSBjb25uZWN0aW9uICh3aGVuIHNlcnZlciB1c2VzIHNzbDovLy4uLilcbiAgICAgICAgIyBidXQgdGhlIGNlcnRpZmljYXRlIHVzZWQgYnkgdGhlIHNlcnZlciBpcyBub3QgdHJ1c3RlZCBieSBhbnkgQ0EgY2VydGlmaWNhdGVcbiAgICAgICAgIyBvbiB0aGUgc2VydmVyIChlLmcuIHdoZW4gc2VsZiBnZW5lcmF0ZWQpLlxuICAgICAgICBjYV9jZXJ0PVwiXCJcblxuICAgICAgICAjIFRMUyBjZXJ0aWZpY2F0ZSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgdGxzX2NlcnQ9XCJcIlxuXG4gICAgICAgICMgVExTIGtleSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgdGxzX2tleT1cIlwiXG5cblxuICAgICMgR2F0ZXdheSBjaGFubmVsIGNvbmZpZ3VyYXRpb24uXG4gICAgI1xuICAgICMgTm90ZTogdGhpcyBjb25maWd1cmF0aW9uIGlzIG9ubHkgdXNlZCBpbiBjYXNlIHRoZSBnYXRld2F5IGlzIHVzaW5nIHRoZVxuICAgICMgQ2hpcnBTdGFjayBDb25jZW50cmF0b3JkIGRhZW1vbi4gSW4gYW55IG90aGVyIGNhc2UsIHRoaXMgY29uZmlndXJhdGlvbiBcbiAgICAjIGlzIGlnbm9yZWQuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkxNjYwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTE2ODAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuXG4gICMgUmVnaW9uIHNwZWNpZmljIG5ldHdvcmsgY29uZmlndXJhdGlvbi5cbiAgW3JlZ2lvbnMubmV0d29ya11cbiAgICBcbiAgICAjIEluc3RhbGxhdGlvbiBtYXJnaW4gKGRCKSB1c2VkIGJ5IHRoZSBBRFIgZW5naW5lLlxuICAgICNcbiAgICAjIEEgaGlnaGVyIG51bWJlciBtZWFucyB0aGF0IHRoZSBuZXR3b3JrLXNlcnZlciB3aWxsIGtlZXAgbW9yZSBtYXJnaW4sXG4gICAgIyByZXN1bHRpbmcgaW4gYSBsb3dlciBkYXRhLXJhdGUgYnV0IGRlY3JlYXNpbmcgdGhlIGNoYW5jZSB0aGF0IHRoZVxuICAgICMgZGV2aWNlIGdldHMgZGlzY29ubmVjdGVkIGJlY2F1c2UgaXQgaXMgdW5hYmxlIHRvIHJlYWNoIG9uZSBvZiB0aGVcbiAgICAjIHN1cnJvdW5kZWQgZ2F0ZXdheXMuXG4gICAgaW5zdGFsbGF0aW9uX21hcmdpbj0xMFxuXG4gICAgIyBSWCB3aW5kb3cgKENsYXNzLUEpLlxuICAgICNcbiAgICAjIFNldCB0aGlzIHRvOlxuICAgICMgMDogUlgxIC8gUlgyXG4gICAgIyAxOiBSWDEgb25seVxuICAgICMgMjogUlgyIG9ubHlcbiAgICByeF93aW5kb3c9MFxuXG4gICAgIyBSWDEgZGVsYXkgKDEgLSAxNSBzZWNvbmRzKS5cbiAgICByeDFfZGVsYXk9MVxuXG4gICAgIyBSWDEgZGF0YS1yYXRlIG9mZnNldFxuICAgIHJ4MV9kcl9vZmZzZXQ9MFxuXG4gICAgIyBSWDIgZGF0YS1yYXRlXG4gICAgcngyX2RyPTJcblxuICAgICMgUlgyIGZyZXF1ZW5jeSAoSHopXG4gICAgcngyX2ZyZXF1ZW5jeT05MTY2MDAwMDBcblxuICAgICMgUHJlZmVyIFJYMiBvbiBSWDEgZGF0YS1yYXRlIGxlc3MgdGhhbi5cbiAgICAjXG4gICAgIyBQcmVmZXIgUlgyIG92ZXIgUlgxIGJhc2VkIG9uIHRoZSBSWDEgZGF0YS1yYXRlLiBXaGVuIHRoZSBSWDEgZGF0YS1yYXRlXG4gICAgIyBpcyBzbWFsbGVyIHRoYW4gdGhlIGNvbmZpZ3VyZWQgdmFsdWUsIHRoZW4gdGhlIE5ldHdvcmsgU2VydmVyIHdpbGxcbiAgICAjIGZpcnN0IHRyeSB0byBzY2hlZHVsZSB0aGUgZG93bmxpbmsgZm9yIFJYMiwgZmFpbGluZyB0aGF0IChlLmcuIHRoZSBnYXRld2F5XG4gICAgIyBoYXMgYWxyZWFkeSBhIHBheWxvYWQgc2NoZWR1bGVkIGF0IHRoZSBSWDIgdGltaW5nKSBpdCB3aWxsIHRyeSBSWDEuXG4gICAgcngyX3ByZWZlcl9vbl9yeDFfZHJfbHQ9MFxuXG4gICAgIyBQcmVmZXIgUlgyIG9uIGxpbmsgYnVkZ2V0LlxuICAgICNcbiAgICAjIFdoZW4gdGhlIGxpbmstYnVkZ2V0IGlzIGJldHRlciBmb3IgUlgyIHRoYW4gZm9yIFJYMSwgdGhlIE5ldHdvcmsgU2VydmVyIHdpbGwgZmlyc3RcbiAgICAjIHRyeSB0byBzY2hlZHVsZSB0aGUgZG93bmxpbmsgaW4gUlgyLCBmYWlsaW5nIHRoYXQgaXQgd2lsbCB0cnkgUlgxLlxuICAgIHJ4Ml9wcmVmZXJfb25fbGlua19idWRnZXQ9ZmFsc2VcblxuICAgICMgRG93bmxpbmsgVFggUG93ZXIgKGRCbSlcbiAgICAjXG4gICAgIyBXaGVuIHNldCB0byAtMSwgdGhlIGRvd25saW5rIFRYIFBvd2VyIGZyb20gdGhlIGNvbmZpZ3VyZWQgYmFuZCB3aWxsXG4gICAgIyBiZSB1c2VkLlxuICAgICNcbiAgICAjIFBsZWFzZSBjb25zdWx0IHRoZSBMb1JhV0FOIFJlZ2lvbmFsIFBhcmFtZXRlcnMgYW5kIGxvY2FsIHJlZ3VsYXRpb25zXG4gICAgIyBmb3IgdmFsaWQgYW5kIGxlZ2FsIG9wdGlvbnMuIE5vdGUgdGhhdCB0aGUgY29uZmlndXJlZCBUWCBQb3dlciBtdXN0IGJlXG4gICAgIyBzdXBwb3J0ZWQgYnkgeW91ciBnYXRld2F5KHMpLlxuICAgIGRvd25saW5rX3R4X3Bvd2VyPS0xXG5cbiAgICAjIEFEUiBpcyBkaXNhYmxlZC5cbiAgICBhZHJfZGlzYWJsZWQ9ZmFsc2VcblxuICAgICMgTWluaW11bSBkYXRhLXJhdGUuXG4gICAgbWluX2RyPTBcblxuICAgICMgTWF4aW11bSBkYXRhLXJhdGUuXG4gICAgbWF4X2RyPTVcblxuXG4gICAgIyBSZWpvaW4tcmVxdWVzdCBjb25maWd1cmF0aW9uIChMb1JhV0FOIDEuMSlcbiAgICBbcmVnaW9ucy5uZXR3b3JrLnJlam9pbl9yZXF1ZXN0XVxuXG4gICAgICAjIFJlcXVlc3QgZGV2aWNlcyB0byBwZXJpb2RpY2FsbHkgc2VuZCByZWpvaW4tcmVxdWVzdHMuXG4gICAgICBlbmFibGVkPWZhbHNlXG5cbiAgICAgICMgVGhlIGRldmljZSBtdXN0IHNlbmQgYSByZWpvaW4tcmVxdWVzdCB0eXBlIDAgYXQgbGVhc3QgZXZlcnkgMl4obWF4X2NvdW50X24gKyA0KVxuICAgICAgIyB1cGxpbmsgbWVzc2FnZXMuIFZhbGlkIHZhbHVlcyBhcmUgMCB0byAxNS5cbiAgICAgIG1heF9jb3VudF9uPTBcblxuICAgICAgIyBUaGUgZGV2aWNlIG11c3Qgc2VuZCBhIHJlam9pbi1yZXF1ZXN0IHR5cGUgMCBhdCBsZWFzdCBldmVyeSAyXihtYXhfdGltZV9uICsgMTApXG4gICAgICAjIHNlY29uZHMuIFZhbGlkIHZhbHVlcyBhcmUgMCB0byAxNS5cbiAgICAgICNcbiAgICAgICMgMCAgPSByb3VnaGx5IDE3IG1pbnV0ZXNcbiAgICAgICMgMTUgPSBhYm91dCAxIHllYXJcbiAgICAgIG1heF90aW1lX249MFxuICAgIFxuXG4gICAgIyBDbGFzcy1CIGNvbmZpZ3VyYXRpb24uXG4gICAgW3JlZ2lvbnMubmV0d29yay5jbGFzc19iXVxuXG4gICAgICAjIFBpbmctc2xvdCBkYXRhLXJhdGUuIFxuICAgICAgcGluZ19zbG90X2RyPTNcblxuICAgICAgIyBQaW5nLXNsb3QgZnJlcXVlbmN5IChIeilcbiAgICAgICNcbiAgICAgICMgc2V0IHRoaXMgdG8gMCB0byB1c2UgdGhlIGRlZmF1bHQgZnJlcXVlbmN5IHBsYW4gZm9yIHRoZSBjb25maWd1cmVkIHJlZ2lvblxuICAgICAgIyAod2hpY2ggY291bGQgYmUgZnJlcXVlbmN5IGhvcHBpbmcpLlxuICAgICAgcGluZ19zbG90X2ZyZXF1ZW5jeT0wXG5cIlwiXCJcblxuW1tjb25maWcubW91bnRzXV1cbnNlcnZpY2VOYW1lID0gXCJjaGlycHN0YWNrXCJcbmZpbGVQYXRoID0gXCIvY2hpcnBzdGFjay9yZWdpb25fYXM5MjNfNC50b21sXCJcbmNvbnRlbnQgPSBcIlwiXCJcbiMgVGhpcyBmaWxlIGNvbnRhaW5zIGFuIGV4YW1wbGUgQVM5MjNfNCBjb25maWd1cmF0aW9uLlxuW1tyZWdpb25zXV1cblxuICAjIElEIGlzIGFuIHVzZXItZGVmaW5lZCBpZGVudGlmaWVyIGZvciB0aGlzIHJlZ2lvbi5cbiAgaWQ9XCJhczkyM180XCJcblxuICAjIERlc2NyaXB0aW9uIGlzIGEgc2hvcnQgZGVzY3JpcHRpb24gZm9yIHRoaXMgcmVnaW9uLlxuICBkZXNjcmlwdGlvbj1cIkFTOTIzLTRcIlxuXG4gICMgQ29tbW9uLW5hbWUgcmVmZXJzIHRvIHRoZSBjb21tb24tbmFtZSBvZiB0aGlzIHJlZ2lvbiBhcyBkZWZpbmVkIGJ5XG4gICMgdGhlIExvUmEgQWxsaWFuY2UuXG4gIGNvbW1vbl9uYW1lPVwiQVM5MjNfNFwiXG5cblxuICAjIEdhdGV3YXkgY29uZmlndXJhdGlvbi5cbiAgW3JlZ2lvbnMuZ2F0ZXdheV1cblxuICAgICMgRm9yY2UgZ2F0ZXdheXMgYXMgcHJpdmF0ZS5cbiAgICAjXG4gICAgIyBJZiBlbmFibGVkLCBnYXRld2F5cyBjYW4gb25seSBiZSB1c2VkIGJ5IGRldmljZXMgdW5kZXIgdGhlIHNhbWUgdGVuYW50LlxuICAgIGZvcmNlX2d3c19wcml2YXRlPWZhbHNlXG5cblxuICAgICMgR2F0ZXdheSBiYWNrZW5kIGNvbmZpZ3VyYXRpb24uXG4gICAgW3JlZ2lvbnMuZ2F0ZXdheS5iYWNrZW5kXVxuXG4gICAgICAjIFRoZSBlbmFibGVkIGJhY2tlbmQgdHlwZS5cbiAgICAgIGVuYWJsZWQ9XCJtcXR0XCJcblxuICAgICAgIyBNUVRUIGNvbmZpZ3VyYXRpb24uXG4gICAgICBbcmVnaW9ucy5nYXRld2F5LmJhY2tlbmQubXF0dF1cblxuICAgICAgICAjIFRvcGljIHByZWZpeC5cbiAgICAgICAgI1xuICAgICAgICAjIFRoZSB0b3BpYyBwcmVmaXggY2FuIGJlIHVzZWQgdG8gZGVmaW5lIHRoZSByZWdpb24gb2YgdGhlIGdhdGV3YXkuXG4gICAgICAgICMgTm90ZSwgdGhlcmUgaXMgbm8gbmVlZCB0byBhZGQgYSB0cmFpbGluZyAnLycgdG8gdGhlIHByZWZpeC4gVGhlIHRyYWlsaW5nXG4gICAgICAgICMgJy8nIGlzIGF1dG9tYXRpY2FsbHkgYWRkZWQgdG8gdGhlIHByZWZpeCBpZiBpdCBpcyBjb25maWd1cmVkLlxuICAgICAgICB0b3BpY19wcmVmaXg9XCJhczkyM180XCJcblxuICAgICAgICAjIE1RVFQgc2VydmVyIChlLmcuIHNjaGVtZTovL2hvc3Q6cG9ydCB3aGVyZSBzY2hlbWUgaXMgdGNwLCBzc2wgb3Igd3MpXG4gICAgICAgIHNlcnZlcj1cInRjcDovL21vc3F1aXR0bzoxODgzXCJcblxuICAgICAgICAjIENvbm5lY3Qgd2l0aCB0aGUgZ2l2ZW4gdXNlcm5hbWUgKG9wdGlvbmFsKVxuICAgICAgICB1c2VybmFtZT1cIlwiXG5cbiAgICAgICAgIyBDb25uZWN0IHdpdGggdGhlIGdpdmVuIHBhc3N3b3JkIChvcHRpb25hbClcbiAgICAgICAgcGFzc3dvcmQ9XCJcIlxuXG4gICAgICAgICMgUXVhbGl0eSBvZiBzZXJ2aWNlIGxldmVsXG4gICAgICAgICNcbiAgICAgICAgIyAwOiBhdCBtb3N0IG9uY2VcbiAgICAgICAgIyAxOiBhdCBsZWFzdCBvbmNlXG4gICAgICAgICMgMjogZXhhY3RseSBvbmNlXG4gICAgICAgICNcbiAgICAgICAgIyBOb3RlOiBhbiBpbmNyZWFzZSBvZiB0aGlzIHZhbHVlIHdpbGwgZGVjcmVhc2UgdGhlIHBlcmZvcm1hbmNlLlxuICAgICAgICAjIEZvciBtb3JlIGluZm9ybWF0aW9uOiBodHRwczovL3d3dy5oaXZlbXEuY29tL2Jsb2cvbXF0dC1lc3NlbnRpYWxzLXBhcnQtNi1tcXR0LXF1YWxpdHktb2Ytc2VydmljZS1sZXZlbHNcbiAgICAgICAgcW9zPTBcblxuICAgICAgICAjIENsZWFuIHNlc3Npb25cbiAgICAgICAgI1xuICAgICAgICAjIFNldCB0aGUgXCJjbGVhbiBzZXNzaW9uXCIgZmxhZyBpbiB0aGUgY29ubmVjdCBtZXNzYWdlIHdoZW4gdGhpcyBjbGllbnRcbiAgICAgICAgIyBjb25uZWN0cyB0byBhbiBNUVRUIGJyb2tlci4gQnkgc2V0dGluZyB0aGlzIGZsYWcgeW91IGFyZSBpbmRpY2F0aW5nXG4gICAgICAgICMgdGhhdCBubyBtZXNzYWdlcyBzYXZlZCBieSB0aGUgYnJva2VyIGZvciB0aGlzIGNsaWVudCBzaG91bGQgYmUgZGVsaXZlcmVkLlxuICAgICAgICBjbGVhbl9zZXNzaW9uPWZhbHNlXG5cbiAgICAgICAgIyBDbGllbnQgSURcbiAgICAgICAgI1xuICAgICAgICAjIFNldCB0aGUgY2xpZW50IGlkIHRvIGJlIHVzZWQgYnkgdGhpcyBjbGllbnQgd2hlbiBjb25uZWN0aW5nIHRvIHRoZSBNUVRUXG4gICAgICAgICMgYnJva2VyLiBBIGNsaWVudCBpZCBtdXN0IGJlIG5vIGxvbmdlciB0aGFuIDIzIGNoYXJhY3RlcnMuIElmIGxlZnQgYmxhbmssXG4gICAgICAgICMgYSByYW5kb20gaWQgd2lsbCBiZSBnZW5lcmF0ZWQgYnkgQ2hpcnBTdGFjay5cbiAgICAgICAgY2xpZW50X2lkPVwiXCJcblxuICAgICAgICAjIEtlZXAgYWxpdmUgaW50ZXJ2YWwuXG4gICAgICAgICNcbiAgICAgICAgIyBUaGlzIGRlZmluZXMgdGhlIG1heGltdW0gdGltZSB0aGF0IHRoYXQgc2hvdWxkIHBhc3Mgd2l0aG91dCBjb21tdW5pY2F0aW9uXG4gICAgICAgICMgYmV0d2VlbiB0aGUgY2xpZW50IGFuZCBzZXJ2ZXIuXG4gICAgICAgIGtlZXBfYWxpdmVfaW50ZXJ2YWw9XCIzMHNcIlxuXG4gICAgICAgICMgQ0EgY2VydGlmaWNhdGUgZmlsZSAob3B0aW9uYWwpXG4gICAgICAgICNcbiAgICAgICAgIyBVc2UgdGhpcyB3aGVuIHNldHRpbmcgdXAgYSBzZWN1cmUgY29ubmVjdGlvbiAod2hlbiBzZXJ2ZXIgdXNlcyBzc2w6Ly8uLi4pXG4gICAgICAgICMgYnV0IHRoZSBjZXJ0aWZpY2F0ZSB1c2VkIGJ5IHRoZSBzZXJ2ZXIgaXMgbm90IHRydXN0ZWQgYnkgYW55IENBIGNlcnRpZmljYXRlXG4gICAgICAgICMgb24gdGhlIHNlcnZlciAoZS5nLiB3aGVuIHNlbGYgZ2VuZXJhdGVkKS5cbiAgICAgICAgY2FfY2VydD1cIlwiXG5cbiAgICAgICAgIyBUTFMgY2VydGlmaWNhdGUgZmlsZSAob3B0aW9uYWwpXG4gICAgICAgIHRsc19jZXJ0PVwiXCJcblxuICAgICAgICAjIFRMUyBrZXkgZmlsZSAob3B0aW9uYWwpXG4gICAgICAgIHRsc19rZXk9XCJcIlxuXG5cbiAgICAjIEdhdGV3YXkgY2hhbm5lbCBjb25maWd1cmF0aW9uLlxuICAgICNcbiAgICAjIE5vdGU6IHRoaXMgY29uZmlndXJhdGlvbiBpcyBvbmx5IHVzZWQgaW4gY2FzZSB0aGUgZ2F0ZXdheSBpcyB1c2luZyB0aGVcbiAgICAjIENoaXJwU3RhY2sgQ29uY2VudHJhdG9yZCBkYWVtb24uIEluIGFueSBvdGhlciBjYXNlLCB0aGlzIGNvbmZpZ3VyYXRpb24gXG4gICAgIyBpcyBpZ25vcmVkLlxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MTczMDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkxNzUwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cblxuICAjIFJlZ2lvbiBzcGVjaWZpYyBuZXR3b3JrIGNvbmZpZ3VyYXRpb24uXG4gIFtyZWdpb25zLm5ldHdvcmtdXG4gICAgXG4gICAgIyBJbnN0YWxsYXRpb24gbWFyZ2luIChkQikgdXNlZCBieSB0aGUgQURSIGVuZ2luZS5cbiAgICAjXG4gICAgIyBBIGhpZ2hlciBudW1iZXIgbWVhbnMgdGhhdCB0aGUgbmV0d29yay1zZXJ2ZXIgd2lsbCBrZWVwIG1vcmUgbWFyZ2luLFxuICAgICMgcmVzdWx0aW5nIGluIGEgbG93ZXIgZGF0YS1yYXRlIGJ1dCBkZWNyZWFzaW5nIHRoZSBjaGFuY2UgdGhhdCB0aGVcbiAgICAjIGRldmljZSBnZXRzIGRpc2Nvbm5lY3RlZCBiZWNhdXNlIGl0IGlzIHVuYWJsZSB0byByZWFjaCBvbmUgb2YgdGhlXG4gICAgIyBzdXJyb3VuZGVkIGdhdGV3YXlzLlxuICAgIGluc3RhbGxhdGlvbl9tYXJnaW49MTBcblxuICAgICMgUlggd2luZG93IChDbGFzcy1BKS5cbiAgICAjXG4gICAgIyBTZXQgdGhpcyB0bzpcbiAgICAjIDA6IFJYMSAvIFJYMlxuICAgICMgMTogUlgxIG9ubHlcbiAgICAjIDI6IFJYMiBvbmx5XG4gICAgcnhfd2luZG93PTBcblxuICAgICMgUlgxIGRlbGF5ICgxIC0gMTUgc2Vjb25kcykuXG4gICAgcngxX2RlbGF5PTFcblxuICAgICMgUlgxIGRhdGEtcmF0ZSBvZmZzZXRcbiAgICByeDFfZHJfb2Zmc2V0PTBcblxuICAgICMgUlgyIGRhdGEtcmF0ZVxuICAgIHJ4Ml9kcj0yXG5cbiAgICAjIFJYMiBmcmVxdWVuY3kgKEh6KVxuICAgIHJ4Ml9mcmVxdWVuY3k9OTE3MzAwMDAwXG5cbiAgICAjIFByZWZlciBSWDIgb24gUlgxIGRhdGEtcmF0ZSBsZXNzIHRoYW4uXG4gICAgI1xuICAgICMgUHJlZmVyIFJYMiBvdmVyIFJYMSBiYXNlZCBvbiB0aGUgUlgxIGRhdGEtcmF0ZS4gV2hlbiB0aGUgUlgxIGRhdGEtcmF0ZVxuICAgICMgaXMgc21hbGxlciB0aGFuIHRoZSBjb25maWd1cmVkIHZhbHVlLCB0aGVuIHRoZSBOZXR3b3JrIFNlcnZlciB3aWxsXG4gICAgIyBmaXJzdCB0cnkgdG8gc2NoZWR1bGUgdGhlIGRvd25saW5rIGZvciBSWDIsIGZhaWxpbmcgdGhhdCAoZS5nLiB0aGUgZ2F0ZXdheVxuICAgICMgaGFzIGFscmVhZHkgYSBwYXlsb2FkIHNjaGVkdWxlZCBhdCB0aGUgUlgyIHRpbWluZykgaXQgd2lsbCB0cnkgUlgxLlxuICAgIHJ4Ml9wcmVmZXJfb25fcngxX2RyX2x0PTBcblxuICAgICMgUHJlZmVyIFJYMiBvbiBsaW5rIGJ1ZGdldC5cbiAgICAjXG4gICAgIyBXaGVuIHRoZSBsaW5rLWJ1ZGdldCBpcyBiZXR0ZXIgZm9yIFJYMiB0aGFuIGZvciBSWDEsIHRoZSBOZXR3b3JrIFNlcnZlciB3aWxsIGZpcnN0XG4gICAgIyB0cnkgdG8gc2NoZWR1bGUgdGhlIGRvd25saW5rIGluIFJYMiwgZmFpbGluZyB0aGF0IGl0IHdpbGwgdHJ5IFJYMS5cbiAgICByeDJfcHJlZmVyX29uX2xpbmtfYnVkZ2V0PWZhbHNlXG5cbiAgICAjIERvd25saW5rIFRYIFBvd2VyIChkQm0pXG4gICAgI1xuICAgICMgV2hlbiBzZXQgdG8gLTEsIHRoZSBkb3dubGluayBUWCBQb3dlciBmcm9tIHRoZSBjb25maWd1cmVkIGJhbmQgd2lsbFxuICAgICMgYmUgdXNlZC5cbiAgICAjXG4gICAgIyBQbGVhc2UgY29uc3VsdCB0aGUgTG9SYVdBTiBSZWdpb25hbCBQYXJhbWV0ZXJzIGFuZCBsb2NhbCByZWd1bGF0aW9uc1xuICAgICMgZm9yIHZhbGlkIGFuZCBsZWdhbCBvcHRpb25zLiBOb3RlIHRoYXQgdGhlIGNvbmZpZ3VyZWQgVFggUG93ZXIgbXVzdCBiZVxuICAgICMgc3VwcG9ydGVkIGJ5IHlvdXIgZ2F0ZXdheShzKS5cbiAgICBkb3dubGlua190eF9wb3dlcj0tMVxuXG4gICAgIyBBRFIgaXMgZGlzYWJsZWQuXG4gICAgYWRyX2Rpc2FibGVkPWZhbHNlXG5cbiAgICAjIE1pbmltdW0gZGF0YS1yYXRlLlxuICAgIG1pbl9kcj0wXG5cbiAgICAjIE1heGltdW0gZGF0YS1yYXRlLlxuICAgIG1heF9kcj01XG5cblxuICAgICMgUmVqb2luLXJlcXVlc3QgY29uZmlndXJhdGlvbiAoTG9SYVdBTiAxLjEpXG4gICAgW3JlZ2lvbnMubmV0d29yay5yZWpvaW5fcmVxdWVzdF1cblxuICAgICAgIyBSZXF1ZXN0IGRldmljZXMgdG8gcGVyaW9kaWNhbGx5IHNlbmQgcmVqb2luLXJlcXVlc3RzLlxuICAgICAgZW5hYmxlZD1mYWxzZVxuXG4gICAgICAjIFRoZSBkZXZpY2UgbXVzdCBzZW5kIGEgcmVqb2luLXJlcXVlc3QgdHlwZSAwIGF0IGxlYXN0IGV2ZXJ5IDJeKG1heF9jb3VudF9uICsgNClcbiAgICAgICMgdXBsaW5rIG1lc3NhZ2VzLiBWYWxpZCB2YWx1ZXMgYXJlIDAgdG8gMTUuXG4gICAgICBtYXhfY291bnRfbj0wXG5cbiAgICAgICMgVGhlIGRldmljZSBtdXN0IHNlbmQgYSByZWpvaW4tcmVxdWVzdCB0eXBlIDAgYXQgbGVhc3QgZXZlcnkgMl4obWF4X3RpbWVfbiArIDEwKVxuICAgICAgIyBzZWNvbmRzLiBWYWxpZCB2YWx1ZXMgYXJlIDAgdG8gMTUuXG4gICAgICAjXG4gICAgICAjIDAgID0gcm91Z2hseSAxNyBtaW51dGVzXG4gICAgICAjIDE1ID0gYWJvdXQgMSB5ZWFyXG4gICAgICBtYXhfdGltZV9uPTBcbiAgICBcblxuICAgICMgQ2xhc3MtQiBjb25maWd1cmF0aW9uLlxuICAgIFtyZWdpb25zLm5ldHdvcmsuY2xhc3NfYl1cblxuICAgICAgIyBQaW5nLXNsb3QgZGF0YS1yYXRlLiBcbiAgICAgIHBpbmdfc2xvdF9kcj0zXG5cbiAgICAgICMgUGluZy1zbG90IGZyZXF1ZW5jeSAoSHopXG4gICAgICAjXG4gICAgICAjIHNldCB0aGlzIHRvIDAgdG8gdXNlIHRoZSBkZWZhdWx0IGZyZXF1ZW5jeSBwbGFuIGZvciB0aGUgY29uZmlndXJlZCByZWdpb25cbiAgICAgICMgKHdoaWNoIGNvdWxkIGJlIGZyZXF1ZW5jeSBob3BwaW5nKS5cbiAgICAgIHBpbmdfc2xvdF9mcmVxdWVuY3k9MFxuXCJcIlwiXG5cbltbY29uZmlnLm1vdW50c11dXG5zZXJ2aWNlTmFtZSA9IFwiY2hpcnBzdGFja1wiXG5maWxlUGF0aCA9IFwiL2NoaXJwc3RhY2svcmVnaW9uX2FzOTIzLnRvbWxcIlxuY29udGVudCA9IFwiXCJcIlxuIyBUaGlzIGZpbGUgY29udGFpbnMgYW4gZXhhbXBsZSBBUzkyMyBjb25maWd1cmF0aW9uLlxuW1tyZWdpb25zXV1cblxuICAjIElEIGlzIGFuIHVzZXItZGVmaW5lZCBpZGVudGlmaWVyIGZvciB0aGlzIHJlZ2lvbi5cbiAgaWQ9XCJhczkyM1wiXG5cbiAgIyBEZXNjcmlwdGlvbiBpcyBhIHNob3J0IGRlc2NyaXB0aW9uIGZvciB0aGlzIHJlZ2lvbi5cbiAgZGVzY3JpcHRpb249XCJBUzkyM1wiXG5cbiAgIyBDb21tb24tbmFtZSByZWZlcnMgdG8gdGhlIGNvbW1vbi1uYW1lIG9mIHRoaXMgcmVnaW9uIGFzIGRlZmluZWQgYnlcbiAgIyB0aGUgTG9SYSBBbGxpYW5jZS5cbiAgY29tbW9uX25hbWU9XCJBUzkyM1wiXG5cblxuICAjIEdhdGV3YXkgY29uZmlndXJhdGlvbi5cbiAgW3JlZ2lvbnMuZ2F0ZXdheV1cblxuICAgICMgRm9yY2UgZ2F0ZXdheXMgYXMgcHJpdmF0ZS5cbiAgICAjXG4gICAgIyBJZiBlbmFibGVkLCBnYXRld2F5cyBjYW4gb25seSBiZSB1c2VkIGJ5IGRldmljZXMgdW5kZXIgdGhlIHNhbWUgdGVuYW50LlxuICAgIGZvcmNlX2d3c19wcml2YXRlPWZhbHNlXG5cblxuICAgICMgR2F0ZXdheSBiYWNrZW5kIGNvbmZpZ3VyYXRpb24uXG4gICAgW3JlZ2lvbnMuZ2F0ZXdheS5iYWNrZW5kXVxuXG4gICAgICAjIFRoZSBlbmFibGVkIGJhY2tlbmQgdHlwZS5cbiAgICAgIGVuYWJsZWQ9XCJtcXR0XCJcblxuICAgICAgIyBNUVRUIGNvbmZpZ3VyYXRpb24uXG4gICAgICBbcmVnaW9ucy5nYXRld2F5LmJhY2tlbmQubXF0dF1cblxuICAgICAgICAjIFRvcGljIHByZWZpeC5cbiAgICAgICAgI1xuICAgICAgICAjIFRoZSB0b3BpYyBwcmVmaXggY2FuIGJlIHVzZWQgdG8gZGVmaW5lIHRoZSByZWdpb24gb2YgdGhlIGdhdGV3YXkuXG4gICAgICAgICMgTm90ZSwgdGhlcmUgaXMgbm8gbmVlZCB0byBhZGQgYSB0cmFpbGluZyAnLycgdG8gdGhlIHByZWZpeC4gVGhlIHRyYWlsaW5nXG4gICAgICAgICMgJy8nIGlzIGF1dG9tYXRpY2FsbHkgYWRkZWQgdG8gdGhlIHByZWZpeCBpZiBpdCBpcyBjb25maWd1cmVkLlxuICAgICAgICB0b3BpY19wcmVmaXg9XCJhczkyM1wiXG5cbiAgICAgICAgIyBNUVRUIHNlcnZlciAoZS5nLiBzY2hlbWU6Ly9ob3N0OnBvcnQgd2hlcmUgc2NoZW1lIGlzIHRjcCwgc3NsIG9yIHdzKVxuICAgICAgICBzZXJ2ZXI9XCJ0Y3A6Ly9tb3NxdWl0dG86MTg4M1wiXG5cbiAgICAgICAgIyBDb25uZWN0IHdpdGggdGhlIGdpdmVuIHVzZXJuYW1lIChvcHRpb25hbClcbiAgICAgICAgdXNlcm5hbWU9XCJcIlxuXG4gICAgICAgICMgQ29ubmVjdCB3aXRoIHRoZSBnaXZlbiBwYXNzd29yZCAob3B0aW9uYWwpXG4gICAgICAgIHBhc3N3b3JkPVwiXCJcblxuICAgICAgICAjIFF1YWxpdHkgb2Ygc2VydmljZSBsZXZlbFxuICAgICAgICAjXG4gICAgICAgICMgMDogYXQgbW9zdCBvbmNlXG4gICAgICAgICMgMTogYXQgbGVhc3Qgb25jZVxuICAgICAgICAjIDI6IGV4YWN0bHkgb25jZVxuICAgICAgICAjXG4gICAgICAgICMgTm90ZTogYW4gaW5jcmVhc2Ugb2YgdGhpcyB2YWx1ZSB3aWxsIGRlY3JlYXNlIHRoZSBwZXJmb3JtYW5jZS5cbiAgICAgICAgIyBGb3IgbW9yZSBpbmZvcm1hdGlvbjogaHR0cHM6Ly93d3cuaGl2ZW1xLmNvbS9ibG9nL21xdHQtZXNzZW50aWFscy1wYXJ0LTYtbXF0dC1xdWFsaXR5LW9mLXNlcnZpY2UtbGV2ZWxzXG4gICAgICAgIHFvcz0wXG5cbiAgICAgICAgIyBDbGVhbiBzZXNzaW9uXG4gICAgICAgICNcbiAgICAgICAgIyBTZXQgdGhlIFwiY2xlYW4gc2Vzc2lvblwiIGZsYWcgaW4gdGhlIGNvbm5lY3QgbWVzc2FnZSB3aGVuIHRoaXMgY2xpZW50XG4gICAgICAgICMgY29ubmVjdHMgdG8gYW4gTVFUVCBicm9rZXIuIEJ5IHNldHRpbmcgdGhpcyBmbGFnIHlvdSBhcmUgaW5kaWNhdGluZ1xuICAgICAgICAjIHRoYXQgbm8gbWVzc2FnZXMgc2F2ZWQgYnkgdGhlIGJyb2tlciBmb3IgdGhpcyBjbGllbnQgc2hvdWxkIGJlIGRlbGl2ZXJlZC5cbiAgICAgICAgY2xlYW5fc2Vzc2lvbj1mYWxzZVxuXG4gICAgICAgICMgQ2xpZW50IElEXG4gICAgICAgICNcbiAgICAgICAgIyBTZXQgdGhlIGNsaWVudCBpZCB0byBiZSB1c2VkIGJ5IHRoaXMgY2xpZW50IHdoZW4gY29ubmVjdGluZyB0byB0aGUgTVFUVFxuICAgICAgICAjIGJyb2tlci4gQSBjbGllbnQgaWQgbXVzdCBiZSBubyBsb25nZXIgdGhhbiAyMyBjaGFyYWN0ZXJzLiBJZiBsZWZ0IGJsYW5rLFxuICAgICAgICAjIGEgcmFuZG9tIGlkIHdpbGwgYmUgZ2VuZXJhdGVkIGJ5IENoaXJwU3RhY2suXG4gICAgICAgIGNsaWVudF9pZD1cIlwiXG5cbiAgICAgICAgIyBLZWVwIGFsaXZlIGludGVydmFsLlxuICAgICAgICAjXG4gICAgICAgICMgVGhpcyBkZWZpbmVzIHRoZSBtYXhpbXVtIHRpbWUgdGhhdCB0aGF0IHNob3VsZCBwYXNzIHdpdGhvdXQgY29tbXVuaWNhdGlvblxuICAgICAgICAjIGJldHdlZW4gdGhlIGNsaWVudCBhbmQgc2VydmVyLlxuICAgICAgICBrZWVwX2FsaXZlX2ludGVydmFsPVwiMzBzXCJcblxuICAgICAgICAjIENBIGNlcnRpZmljYXRlIGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICAjXG4gICAgICAgICMgVXNlIHRoaXMgd2hlbiBzZXR0aW5nIHVwIGEgc2VjdXJlIGNvbm5lY3Rpb24gKHdoZW4gc2VydmVyIHVzZXMgc3NsOi8vLi4uKVxuICAgICAgICAjIGJ1dCB0aGUgY2VydGlmaWNhdGUgdXNlZCBieSB0aGUgc2VydmVyIGlzIG5vdCB0cnVzdGVkIGJ5IGFueSBDQSBjZXJ0aWZpY2F0ZVxuICAgICAgICAjIG9uIHRoZSBzZXJ2ZXIgKGUuZy4gd2hlbiBzZWxmIGdlbmVyYXRlZCkuXG4gICAgICAgIGNhX2NlcnQ9XCJcIlxuXG4gICAgICAgICMgVExTIGNlcnRpZmljYXRlIGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICB0bHNfY2VydD1cIlwiXG5cbiAgICAgICAgIyBUTFMga2V5IGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICB0bHNfa2V5PVwiXCJcblxuXG4gICAgIyBHYXRld2F5IGNoYW5uZWwgY29uZmlndXJhdGlvbi5cbiAgICAjXG4gICAgIyBOb3RlOiB0aGlzIGNvbmZpZ3VyYXRpb24gaXMgb25seSB1c2VkIGluIGNhc2UgdGhlIGdhdGV3YXkgaXMgdXNpbmcgdGhlXG4gICAgIyBDaGlycFN0YWNrIENvbmNlbnRyYXRvcmQgZGFlbW9uLiBJbiBhbnkgb3RoZXIgY2FzZSwgdGhpcyBjb25maWd1cmF0aW9uIFxuICAgICMgaXMgaWdub3JlZC5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTIzMjAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MjM0MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG5cbiAgIyBSZWdpb24gc3BlY2lmaWMgbmV0d29yayBjb25maWd1cmF0aW9uLlxuICBbcmVnaW9ucy5uZXR3b3JrXVxuICAgIFxuICAgICMgSW5zdGFsbGF0aW9uIG1hcmdpbiAoZEIpIHVzZWQgYnkgdGhlIEFEUiBlbmdpbmUuXG4gICAgI1xuICAgICMgQSBoaWdoZXIgbnVtYmVyIG1lYW5zIHRoYXQgdGhlIG5ldHdvcmstc2VydmVyIHdpbGwga2VlcCBtb3JlIG1hcmdpbixcbiAgICAjIHJlc3VsdGluZyBpbiBhIGxvd2VyIGRhdGEtcmF0ZSBidXQgZGVjcmVhc2luZyB0aGUgY2hhbmNlIHRoYXQgdGhlXG4gICAgIyBkZXZpY2UgZ2V0cyBkaXNjb25uZWN0ZWQgYmVjYXVzZSBpdCBpcyB1bmFibGUgdG8gcmVhY2ggb25lIG9mIHRoZVxuICAgICMgc3Vycm91bmRlZCBnYXRld2F5cy5cbiAgICBpbnN0YWxsYXRpb25fbWFyZ2luPTEwXG5cbiAgICAjIFJYIHdpbmRvdyAoQ2xhc3MtQSkuXG4gICAgI1xuICAgICMgU2V0IHRoaXMgdG86XG4gICAgIyAwOiBSWDEgLyBSWDJcbiAgICAjIDE6IFJYMSBvbmx5XG4gICAgIyAyOiBSWDIgb25seVxuICAgIHJ4X3dpbmRvdz0wXG5cbiAgICAjIFJYMSBkZWxheSAoMSAtIDE1IHNlY29uZHMpLlxuICAgIHJ4MV9kZWxheT0xXG5cbiAgICAjIFJYMSBkYXRhLXJhdGUgb2Zmc2V0XG4gICAgcngxX2RyX29mZnNldD0wXG5cbiAgICAjIFJYMiBkYXRhLXJhdGVcbiAgICByeDJfZHI9MlxuXG4gICAgIyBSWDIgZnJlcXVlbmN5IChIeilcbiAgICByeDJfZnJlcXVlbmN5PTkyMzIwMDAwMFxuXG4gICAgIyBQcmVmZXIgUlgyIG9uIFJYMSBkYXRhLXJhdGUgbGVzcyB0aGFuLlxuICAgICNcbiAgICAjIFByZWZlciBSWDIgb3ZlciBSWDEgYmFzZWQgb24gdGhlIFJYMSBkYXRhLXJhdGUuIFdoZW4gdGhlIFJYMSBkYXRhLXJhdGVcbiAgICAjIGlzIHNtYWxsZXIgdGhhbiB0aGUgY29uZmlndXJlZCB2YWx1ZSwgdGhlbiB0aGUgTmV0d29yayBTZXJ2ZXIgd2lsbFxuICAgICMgZmlyc3QgdHJ5IHRvIHNjaGVkdWxlIHRoZSBkb3dubGluayBmb3IgUlgyLCBmYWlsaW5nIHRoYXQgKGUuZy4gdGhlIGdhdGV3YXlcbiAgICAjIGhhcyBhbHJlYWR5IGEgcGF5bG9hZCBzY2hlZHVsZWQgYXQgdGhlIFJYMiB0aW1pbmcpIGl0IHdpbGwgdHJ5IFJYMS5cbiAgICByeDJfcHJlZmVyX29uX3J4MV9kcl9sdD0wXG5cbiAgICAjIFByZWZlciBSWDIgb24gbGluayBidWRnZXQuXG4gICAgI1xuICAgICMgV2hlbiB0aGUgbGluay1idWRnZXQgaXMgYmV0dGVyIGZvciBSWDIgdGhhbiBmb3IgUlgxLCB0aGUgTmV0d29yayBTZXJ2ZXIgd2lsbCBmaXJzdFxuICAgICMgdHJ5IHRvIHNjaGVkdWxlIHRoZSBkb3dubGluayBpbiBSWDIsIGZhaWxpbmcgdGhhdCBpdCB3aWxsIHRyeSBSWDEuXG4gICAgcngyX3ByZWZlcl9vbl9saW5rX2J1ZGdldD1mYWxzZVxuXG4gICAgIyBEb3dubGluayBUWCBQb3dlciAoZEJtKVxuICAgICNcbiAgICAjIFdoZW4gc2V0IHRvIC0xLCB0aGUgZG93bmxpbmsgVFggUG93ZXIgZnJvbSB0aGUgY29uZmlndXJlZCBiYW5kIHdpbGxcbiAgICAjIGJlIHVzZWQuXG4gICAgI1xuICAgICMgUGxlYXNlIGNvbnN1bHQgdGhlIExvUmFXQU4gUmVnaW9uYWwgUGFyYW1ldGVycyBhbmQgbG9jYWwgcmVndWxhdGlvbnNcbiAgICAjIGZvciB2YWxpZCBhbmQgbGVnYWwgb3B0aW9ucy4gTm90ZSB0aGF0IHRoZSBjb25maWd1cmVkIFRYIFBvd2VyIG11c3QgYmVcbiAgICAjIHN1cHBvcnRlZCBieSB5b3VyIGdhdGV3YXkocykuXG4gICAgZG93bmxpbmtfdHhfcG93ZXI9LTFcblxuICAgICMgQURSIGlzIGRpc2FibGVkLlxuICAgIGFkcl9kaXNhYmxlZD1mYWxzZVxuXG4gICAgIyBNaW5pbXVtIGRhdGEtcmF0ZS5cbiAgICBtaW5fZHI9MFxuXG4gICAgIyBNYXhpbXVtIGRhdGEtcmF0ZS5cbiAgICBtYXhfZHI9NVxuXG5cbiAgICAjIFJlam9pbi1yZXF1ZXN0IGNvbmZpZ3VyYXRpb24gKExvUmFXQU4gMS4xKVxuICAgIFtyZWdpb25zLm5ldHdvcmsucmVqb2luX3JlcXVlc3RdXG5cbiAgICAgICMgUmVxdWVzdCBkZXZpY2VzIHRvIHBlcmlvZGljYWxseSBzZW5kIHJlam9pbi1yZXF1ZXN0cy5cbiAgICAgIGVuYWJsZWQ9ZmFsc2VcblxuICAgICAgIyBUaGUgZGV2aWNlIG11c3Qgc2VuZCBhIHJlam9pbi1yZXF1ZXN0IHR5cGUgMCBhdCBsZWFzdCBldmVyeSAyXihtYXhfY291bnRfbiArIDQpXG4gICAgICAjIHVwbGluayBtZXNzYWdlcy4gVmFsaWQgdmFsdWVzIGFyZSAwIHRvIDE1LlxuICAgICAgbWF4X2NvdW50X249MFxuXG4gICAgICAjIFRoZSBkZXZpY2UgbXVzdCBzZW5kIGEgcmVqb2luLXJlcXVlc3QgdHlwZSAwIGF0IGxlYXN0IGV2ZXJ5IDJeKG1heF90aW1lX24gKyAxMClcbiAgICAgICMgc2Vjb25kcy4gVmFsaWQgdmFsdWVzIGFyZSAwIHRvIDE1LlxuICAgICAgI1xuICAgICAgIyAwICA9IHJvdWdobHkgMTcgbWludXRlc1xuICAgICAgIyAxNSA9IGFib3V0IDEgeWVhclxuICAgICAgbWF4X3RpbWVfbj0wXG4gICAgXG5cbiAgICAjIENsYXNzLUIgY29uZmlndXJhdGlvbi5cbiAgICBbcmVnaW9ucy5uZXR3b3JrLmNsYXNzX2JdXG5cbiAgICAgICMgUGluZy1zbG90IGRhdGEtcmF0ZS4gXG4gICAgICBwaW5nX3Nsb3RfZHI9M1xuXG4gICAgICAjIFBpbmctc2xvdCBmcmVxdWVuY3kgKEh6KVxuICAgICAgI1xuICAgICAgIyBzZXQgdGhpcyB0byAwIHRvIHVzZSB0aGUgZGVmYXVsdCBmcmVxdWVuY3kgcGxhbiBmb3IgdGhlIGNvbmZpZ3VyZWQgcmVnaW9uXG4gICAgICAjICh3aGljaCBjb3VsZCBiZSBmcmVxdWVuY3kgaG9wcGluZykuXG4gICAgICBwaW5nX3Nsb3RfZnJlcXVlbmN5PTBcblwiXCJcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuc2VydmljZU5hbWUgPSBcImNoaXJwc3RhY2tcIlxuZmlsZVBhdGggPSBcIi9jaGlycHN0YWNrL3JlZ2lvbl9hdTkxNV8wLnRvbWxcIlxuY29udGVudCA9IFwiXCJcIlxuIyBUaGlzIGZpbGUgY29udGFpbnMgYW4gZXhhbXBsZSBBVTkxNSBleGFtcGxlIChjaGFubmVscyAwLTcgKyA2NCkuXG5bW3JlZ2lvbnNdXVxuXG4gICMgSUQgaXMgYW4gdXNlLWRlZmluZWQgaWRlbnRpZmllciBmb3IgdGhpcyByZWdpb24uXG4gIGlkPVwiYXU5MTVfMFwiXG5cbiAgIyBEZXNjcmlwdGlvbiBpcyBhIHNob3J0IGRlc2NyaXB0aW9uIGZvciB0aGlzIHJlZ2lvbi5cbiAgZGVzY3JpcHRpb249XCJBVTkxNSAoY2hhbm5lbHMgMC03ICsgNjQpXCJcblxuICAjIENvbW1vbi1uYW1lIHJlZmVycyB0byB0aGUgY29tbW9uLW5hbWUgb2YgdGhpcyByZWdpb24gYXMgZGVmaW5lZCBieVxuICAjIHRoZSBMb1JhIEFsbGlhbmNlLlxuICBjb21tb25fbmFtZT1cIkFVOTE1XCJcblxuXG4gICMgR2F0ZXdheSBjb25maWd1cmF0aW9uLlxuICBbcmVnaW9ucy5nYXRld2F5XVxuXG4gICAgIyBGb3JjZSBnYXRld2F5cyBhcyBwcml2YXRlLlxuICAgICNcbiAgICAjIElmIGVuYWJsZWQsIGdhdGV3YXlzIGNhbiBvbmx5IGJlIHVzZWQgYnkgZGV2aWNlcyB1bmRlciB0aGUgc2FtZSB0ZW5hbnQuXG4gICAgZm9yY2VfZ3dzX3ByaXZhdGU9ZmFsc2VcblxuICAgIFxuICAgICMgR2F0ZXdheSBiYWNrZW5kIGNvbmZpZ3VyYXRpb24uXG4gICAgW3JlZ2lvbnMuZ2F0ZXdheS5iYWNrZW5kXVxuXG4gICAgICAjIFRoZSBlbmFibGVkIGJhY2tlbmQgdHlwZS5cbiAgICAgIGVuYWJsZWQ9XCJtcXR0XCJcblxuICAgICAgIyBNUVRUIGNvbmZpZ3VyYXRpb24uXG4gICAgICBbcmVnaW9ucy5nYXRld2F5LmJhY2tlbmQubXF0dF1cblxuICAgICAgICAjIFRvcGljIHByZWZpeC5cbiAgICAgICAgI1xuICAgICAgICAjIFRoZSB0b3BpYyBwcmVmaXggY2FuIGJlIHVzZWQgdG8gZGVmaW5lIHRoZSByZWdpb24gb2YgdGhlIGdhdGV3YXkuXG4gICAgICAgICMgTm90ZSwgdGhlcmUgaXMgbm8gbmVlZCB0byBhZGQgYSB0cmFpbGluZyAnLycgdG8gdGhlIHByZWZpeC4gVGhlIHRyYWlsaW5nXG4gICAgICAgICMgJy8nIGlzIGF1dG9tYXRpY2FsbHkgYWRkZWQgdG8gdGhlIHByZWZpeCBpZiBpdCBpcyBjb25maWd1cmVkLlxuICAgICAgICB0b3BpY19wcmVmaXg9XCJhdTkxNV8wXCJcblxuICAgICAgICAjIE1RVFQgc2VydmVyIChlLmcuIHNjaGVtZTovL2hvc3Q6cG9ydCB3aGVyZSBzY2hlbWUgaXMgdGNwLCBzc2wgb3Igd3MpXG4gICAgICAgIHNlcnZlcj1cInRjcDovL21vc3F1aXR0bzoxODgzXCJcblxuICAgICAgICAjIENvbm5lY3Qgd2l0aCB0aGUgZ2l2ZW4gdXNlcm5hbWUgKG9wdGlvbmFsKVxuICAgICAgICB1c2VybmFtZT1cIlwiXG5cbiAgICAgICAgIyBDb25uZWN0IHdpdGggdGhlIGdpdmVuIHBhc3N3b3JkIChvcHRpb25hbClcbiAgICAgICAgcGFzc3dvcmQ9XCJcIlxuXG4gICAgICAgICMgUXVhbGl0eSBvZiBzZXJ2aWNlIGxldmVsXG4gICAgICAgICNcbiAgICAgICAgIyAwOiBhdCBtb3N0IG9uY2VcbiAgICAgICAgIyAxOiBhdCBsZWFzdCBvbmNlXG4gICAgICAgICMgMjogZXhhY3RseSBvbmNlXG4gICAgICAgICNcbiAgICAgICAgIyBOb3RlOiBhbiBpbmNyZWFzZSBvZiB0aGlzIHZhbHVlIHdpbGwgZGVjcmVhc2UgdGhlIHBlcmZvcm1hbmNlLlxuICAgICAgICAjIEZvciBtb3JlIGluZm9ybWF0aW9uOiBodHRwczovL3d3dy5oaXZlbXEuY29tL2Jsb2cvbXF0dC1lc3NlbnRpYWxzLXBhcnQtNi1tcXR0LXF1YWxpdHktb2Ytc2VydmljZS1sZXZlbHNcbiAgICAgICAgcW9zPTBcblxuICAgICAgICAjIENsZWFuIHNlc3Npb25cbiAgICAgICAgI1xuICAgICAgICAjIFNldCB0aGUgXCJjbGVhbiBzZXNzaW9uXCIgZmxhZyBpbiB0aGUgY29ubmVjdCBtZXNzYWdlIHdoZW4gdGhpcyBjbGllbnRcbiAgICAgICAgIyBjb25uZWN0cyB0byBhbiBNUVRUIGJyb2tlci4gQnkgc2V0dGluZyB0aGlzIGZsYWcgeW91IGFyZSBpbmRpY2F0aW5nXG4gICAgICAgICMgdGhhdCBubyBtZXNzYWdlcyBzYXZlZCBieSB0aGUgYnJva2VyIGZvciB0aGlzIGNsaWVudCBzaG91bGQgYmUgZGVsaXZlcmVkLlxuICAgICAgICBjbGVhbl9zZXNzaW9uPWZhbHNlXG5cbiAgICAgICAgIyBDbGllbnQgSURcbiAgICAgICAgI1xuICAgICAgICAjIFNldCB0aGUgY2xpZW50IGlkIHRvIGJlIHVzZWQgYnkgdGhpcyBjbGllbnQgd2hlbiBjb25uZWN0aW5nIHRvIHRoZSBNUVRUXG4gICAgICAgICMgYnJva2VyLiBBIGNsaWVudCBpZCBtdXN0IGJlIG5vIGxvbmdlciB0aGFuIDIzIGNoYXJhY3RlcnMuIElmIGxlZnQgYmxhbmssXG4gICAgICAgICMgYSByYW5kb20gaWQgd2lsbCBiZSBnZW5lcmF0ZWQgYnkgQ2hpcnBTdGFjay5cbiAgICAgICAgY2xpZW50X2lkPVwiXCJcblxuICAgICAgICAjIEtlZXAgYWxpdmUgaW50ZXJ2YWwuXG4gICAgICAgICNcbiAgICAgICAgIyBUaGlzIGRlZmluZXMgdGhlIG1heGltdW0gdGltZSB0aGF0IHRoYXQgc2hvdWxkIHBhc3Mgd2l0aG91dCBjb21tdW5pY2F0aW9uXG4gICAgICAgICMgYmV0d2VlbiB0aGUgY2xpZW50IGFuZCBzZXJ2ZXIuXG4gICAgICAgIGtlZXBfYWxpdmVfaW50ZXJ2YWw9XCIzMHNcIlxuXG4gICAgICAgICMgQ0EgY2VydGlmaWNhdGUgZmlsZSAob3B0aW9uYWwpXG4gICAgICAgICNcbiAgICAgICAgIyBVc2UgdGhpcyB3aGVuIHNldHRpbmcgdXAgYSBzZWN1cmUgY29ubmVjdGlvbiAod2hlbiBzZXJ2ZXIgdXNlcyBzc2w6Ly8uLi4pXG4gICAgICAgICMgYnV0IHRoZSBjZXJ0aWZpY2F0ZSB1c2VkIGJ5IHRoZSBzZXJ2ZXIgaXMgbm90IHRydXN0ZWQgYnkgYW55IENBIGNlcnRpZmljYXRlXG4gICAgICAgICMgb24gdGhlIHNlcnZlciAoZS5nLiB3aGVuIHNlbGYgZ2VuZXJhdGVkKS5cbiAgICAgICAgY2FfY2VydD1cIlwiXG5cbiAgICAgICAgIyBUTFMgY2VydGlmaWNhdGUgZmlsZSAob3B0aW9uYWwpXG4gICAgICAgIHRsc19jZXJ0PVwiXCJcblxuICAgICAgICAjIFRMUyBrZXkgZmlsZSAob3B0aW9uYWwpXG4gICAgICAgIHRsc19rZXk9XCJcIlxuXG5cbiAgICAjIEdhdGV3YXkgY2hhbm5lbCBjb25maWd1cmF0aW9uLlxuICAgICNcbiAgICAjIE5vdGU6IHRoaXMgY29uZmlndXJhdGlvbiBpcyBvbmx5IHVzZWQgaW4gY2FzZSB0aGUgZ2F0ZXdheSBpcyB1c2luZyB0aGVcbiAgICAjIENoaXJwU3RhY2sgQ29uY2VudHJhdG9yZCBkYWVtb24uIEluIGFueSBvdGhlciBjYXNlLCB0aGlzIGNvbmZpZ3VyYXRpb24gXG4gICAgIyBpcyBpZ25vcmVkLlxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MTUyMDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkxNTQwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTE1NjAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MTU4MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkxNjAwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTE2MjAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MTY0MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkxNjYwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTE1OTAwMDAwXG4gICAgICBiYW5kd2lkdGg9NTAwMDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bOF1cblxuXG4gICMgUmVnaW9uIHNwZWNpZmljIG5ldHdvcmsgY29uZmlndXJhdGlvbi5cbiAgW3JlZ2lvbnMubmV0d29ya11cbiAgICBcbiAgICAjIEluc3RhbGxhdGlvbiBtYXJnaW4gKGRCKSB1c2VkIGJ5IHRoZSBBRFIgZW5naW5lLlxuICAgICNcbiAgICAjIEEgaGlnaGVyIG51bWJlciBtZWFucyB0aGF0IHRoZSBuZXR3b3JrLXNlcnZlciB3aWxsIGtlZXAgbW9yZSBtYXJnaW4sXG4gICAgIyByZXN1bHRpbmcgaW4gYSBsb3dlciBkYXRhLXJhdGUgYnV0IGRlY3JlYXNpbmcgdGhlIGNoYW5jZSB0aGF0IHRoZVxuICAgICMgZGV2aWNlIGdldHMgZGlzY29ubmVjdGVkIGJlY2F1c2UgaXQgaXMgdW5hYmxlIHRvIHJlYWNoIG9uZSBvZiB0aGVcbiAgICAjIHN1cnJvdW5kZWQgZ2F0ZXdheXMuXG4gICAgaW5zdGFsbGF0aW9uX21hcmdpbj0xMFxuXG4gICAgIyBSWCB3aW5kb3cgKENsYXNzLUEpLlxuICAgICNcbiAgICAjIFNldCB0aGlzIHRvOlxuICAgICMgMDogUlgxIC8gUlgyXG4gICAgIyAxOiBSWDEgb25seVxuICAgICMgMjogUlgyIG9ubHlcbiAgICByeF93aW5kb3c9MFxuXG4gICAgIyBSWDEgZGVsYXkgKDEgLSAxNSBzZWNvbmRzKS5cbiAgICByeDFfZGVsYXk9MVxuXG4gICAgIyBSWDEgZGF0YS1yYXRlIG9mZnNldFxuICAgIHJ4MV9kcl9vZmZzZXQ9MFxuXG4gICAgIyBSWDIgZGF0YS1yYXRlXG4gICAgcngyX2RyPThcblxuICAgICMgUlgyIGZyZXF1ZW5jeSAoSHopXG4gICAgcngyX2ZyZXF1ZW5jeT05MjMzMDAwMDBcblxuICAgICMgUHJlZmVyIFJYMiBvbiBSWDEgZGF0YS1yYXRlIGxlc3MgdGhhbi5cbiAgICAjXG4gICAgIyBQcmVmZXIgUlgyIG92ZXIgUlgxIGJhc2VkIG9uIHRoZSBSWDEgZGF0YS1yYXRlLiBXaGVuIHRoZSBSWDEgZGF0YS1yYXRlXG4gICAgIyBpcyBzbWFsbGVyIHRoYW4gdGhlIGNvbmZpZ3VyZWQgdmFsdWUsIHRoZW4gdGhlIE5ldHdvcmsgU2VydmVyIHdpbGxcbiAgICAjIGZpcnN0IHRyeSB0byBzY2hlZHVsZSB0aGUgZG93bmxpbmsgZm9yIFJYMiwgZmFpbGluZyB0aGF0IChlLmcuIHRoZSBnYXRld2F5XG4gICAgIyBoYXMgYWxyZWFkeSBhIHBheWxvYWQgc2NoZWR1bGVkIGF0IHRoZSBSWDIgdGltaW5nKSBpdCB3aWxsIHRyeSBSWDEuXG4gICAgcngyX3ByZWZlcl9vbl9yeDFfZHJfbHQ9MFxuXG4gICAgIyBQcmVmZXIgUlgyIG9uIGxpbmsgYnVkZ2V0LlxuICAgICNcbiAgICAjIFdoZW4gdGhlIGxpbmstYnVkZ2V0IGlzIGJldHRlciBmb3IgUlgyIHRoYW4gZm9yIFJYMSwgdGhlIE5ldHdvcmsgU2VydmVyIHdpbGwgZmlyc3RcbiAgICAjIHRyeSB0byBzY2hlZHVsZSB0aGUgZG93bmxpbmsgaW4gUlgyLCBmYWlsaW5nIHRoYXQgaXQgd2lsbCB0cnkgUlgxLlxuICAgIHJ4Ml9wcmVmZXJfb25fbGlua19idWRnZXQ9ZmFsc2VcblxuICAgICMgRG93bmxpbmsgVFggUG93ZXIgKGRCbSlcbiAgICAjXG4gICAgIyBXaGVuIHNldCB0byAtMSwgdGhlIGRvd25saW5rIFRYIFBvd2VyIGZyb20gdGhlIGNvbmZpZ3VyZWQgYmFuZCB3aWxsXG4gICAgIyBiZSB1c2VkLlxuICAgICNcbiAgICAjIFBsZWFzZSBjb25zdWx0IHRoZSBMb1JhV0FOIFJlZ2lvbmFsIFBhcmFtZXRlcnMgYW5kIGxvY2FsIHJlZ3VsYXRpb25zXG4gICAgIyBmb3IgdmFsaWQgYW5kIGxlZ2FsIG9wdGlvbnMuIE5vdGUgdGhhdCB0aGUgY29uZmlndXJlZCBUWCBQb3dlciBtdXN0IGJlXG4gICAgIyBzdXBwb3J0ZWQgYnkgeW91ciBnYXRld2F5KHMpLlxuICAgIGRvd25saW5rX3R4X3Bvd2VyPS0xXG5cbiAgICAjIEFEUiBpcyBkaXNhYmxlZC5cbiAgICBhZHJfZGlzYWJsZWQ9ZmFsc2VcblxuICAgICMgTWluaW11bSBkYXRhLXJhdGUuXG4gICAgbWluX2RyPTBcblxuICAgICMgTWF4aW11bSBkYXRhLXJhdGUuXG4gICAgbWF4X2RyPTVcblxuICAgICMgRW5hYmxlZCB1cGxpbmsgY2hhbm5lbHMuXG4gICAgI1xuICAgICMgVXNlIHRoaXMgd2hlbiBvbnkgYSBzdWItc2V0IG9mIHRoZSBieSBkZWZhdWx0IGVuYWJsZWQgY2hhbm5lbHMgYXJlIGJlaW5nXG4gICAgIyB1c2VkLiBGb3IgZXhhbXBsZSB3aGVuIG9ubHkgdXNpbmcgdGhlIGZpcnN0IDggY2hhbm5lbHMgb2YgdGhlIFVTIGJhbmQuXG4gICAgIyBOb3RlOiB3aGVuIGxlZnQgYmxhbmsgLyBlbXB0eSBhcnJheSwgYWxsIGNoYW5uZWxzIHdpbGwgYmUgZW5hYmxlZC5cbiAgICBlbmFibGVkX3VwbGlua19jaGFubmVscz1bMCwgMSwgMiwgMywgNCwgNSwgNiwgNywgNjRdXG5cblxuICAgICMgUmVqb2luLXJlcXVlc3QgY29uZmlndXJhdGlvbiAoTG9SYVdBTiAxLjEpXG4gICAgW3JlZ2lvbnMubmV0d29yay5yZWpvaW5fcmVxdWVzdF1cblxuICAgICAgIyBSZXF1ZXN0IGRldmljZXMgdG8gcGVyaW9kaWNhbGx5IHNlbmQgcmVqb2luLXJlcXVlc3RzLlxuICAgICAgZW5hYmxlZD1mYWxzZVxuXG4gICAgICAjIFRoZSBkZXZpY2UgbXVzdCBzZW5kIGEgcmVqb2luLXJlcXVlc3QgdHlwZSAwIGF0IGxlYXN0IGV2ZXJ5IDJeKG1heF9jb3VudF9uICsgNClcbiAgICAgICMgdXBsaW5rIG1lc3NhZ2VzLiBWYWxpZCB2YWx1ZXMgYXJlIDAgdG8gMTUuXG4gICAgICBtYXhfY291bnRfbj0wXG5cbiAgICAgICMgVGhlIGRldmljZSBtdXN0IHNlbmQgYSByZWpvaW4tcmVxdWVzdCB0eXBlIDAgYXQgbGVhc3QgZXZlcnkgMl4obWF4X3RpbWVfbiArIDEwKVxuICAgICAgIyBzZWNvbmRzLiBWYWxpZCB2YWx1ZXMgYXJlIDAgdG8gMTUuXG4gICAgICAjXG4gICAgICAjIDAgID0gcm91Z2hseSAxNyBtaW51dGVzXG4gICAgICAjIDE1ID0gYWJvdXQgMSB5ZWFyXG4gICAgICBtYXhfdGltZV9uPTBcbiAgICBcblxuICAgICMgQ2xhc3MtQiBjb25maWd1cmF0aW9uLlxuICAgIFtyZWdpb25zLm5ldHdvcmsuY2xhc3NfYl1cblxuICAgICAgIyBQaW5nLXNsb3QgZGF0YS1yYXRlLiBcbiAgICAgIHBpbmdfc2xvdF9kcj04XG5cbiAgICAgICMgUGluZy1zbG90IGZyZXF1ZW5jeSAoSHopXG4gICAgICAjXG4gICAgICAjIHNldCB0aGlzIHRvIDAgdG8gdXNlIHRoZSBkZWZhdWx0IGZyZXF1ZW5jeSBwbGFuIGZvciB0aGUgY29uZmlndXJlZCByZWdpb25cbiAgICAgICMgKHdoaWNoIGNvdWxkIGJlIGZyZXF1ZW5jeSBob3BwaW5nKS5cbiAgICAgIHBpbmdfc2xvdF9mcmVxdWVuY3k9MFxuXCJcIlwiXG5cbltbY29uZmlnLm1vdW50c11dXG5zZXJ2aWNlTmFtZSA9IFwiY2hpcnBzdGFja1wiXG5maWxlUGF0aCA9IFwiL2NoaXJwc3RhY2svcmVnaW9uX2F1OTE1XzEudG9tbFwiXG5jb250ZW50ID0gXCJcIlwiXG4jIFRoaXMgZmlsZSBjb250YWlucyBhbiBleGFtcGxlIEFVOTE1IGV4YW1wbGUgKGNoYW5uZWxzIDgtMTUgKyA2NSkuXG5bW3JlZ2lvbnNdXVxuXG4gICMgSUQgaXMgYW4gdXNlLWRlZmluZWQgaWRlbnRpZmllciBmb3IgdGhpcyByZWdpb24uXG4gIGlkPVwiYXU5MTVfMVwiXG5cbiAgIyBEZXNjcmlwdGlvbiBpcyBhIHNob3J0IGRlc2NyaXB0aW9uIGZvciB0aGlzIHJlZ2lvbi5cbiAgZGVzY3JpcHRpb249XCJBVTkxNSAoY2hhbm5lbHMgOC0xNSArIDY1KVwiXG5cbiAgIyBDb21tb24tbmFtZSByZWZlcnMgdG8gdGhlIGNvbW1vbi1uYW1lIG9mIHRoaXMgcmVnaW9uIGFzIGRlZmluZWQgYnlcbiAgIyB0aGUgTG9SYSBBbGxpYW5jZS5cbiAgY29tbW9uX25hbWU9XCJBVTkxNVwiXG5cblxuICAjIEdhdGV3YXkgY29uZmlndXJhdGlvbi5cbiAgW3JlZ2lvbnMuZ2F0ZXdheV1cblxuICAgICMgRm9yY2UgZ2F0ZXdheXMgYXMgcHJpdmF0ZS5cbiAgICAjXG4gICAgIyBJZiBlbmFibGVkLCBnYXRld2F5cyBjYW4gb25seSBiZSB1c2VkIGJ5IGRldmljZXMgdW5kZXIgdGhlIHNhbWUgdGVuYW50LlxuICAgIGZvcmNlX2d3c19wcml2YXRlPWZhbHNlXG5cbiAgICBcbiAgICAjIEdhdGV3YXkgYmFja2VuZCBjb25maWd1cmF0aW9uLlxuICAgIFtyZWdpb25zLmdhdGV3YXkuYmFja2VuZF1cblxuICAgICAgIyBUaGUgZW5hYmxlZCBiYWNrZW5kIHR5cGUuXG4gICAgICBlbmFibGVkPVwibXF0dFwiXG5cbiAgICAgICMgTVFUVCBjb25maWd1cmF0aW9uLlxuICAgICAgW3JlZ2lvbnMuZ2F0ZXdheS5iYWNrZW5kLm1xdHRdXG5cbiAgICAgICAgIyBUb3BpYyBwcmVmaXguXG4gICAgICAgICNcbiAgICAgICAgIyBUaGUgdG9waWMgcHJlZml4IGNhbiBiZSB1c2VkIHRvIGRlZmluZSB0aGUgcmVnaW9uIG9mIHRoZSBnYXRld2F5LlxuICAgICAgICAjIE5vdGUsIHRoZXJlIGlzIG5vIG5lZWQgdG8gYWRkIGEgdHJhaWxpbmcgJy8nIHRvIHRoZSBwcmVmaXguIFRoZSB0cmFpbGluZ1xuICAgICAgICAjICcvJyBpcyBhdXRvbWF0aWNhbGx5IGFkZGVkIHRvIHRoZSBwcmVmaXggaWYgaXQgaXMgY29uZmlndXJlZC5cbiAgICAgICAgdG9waWNfcHJlZml4PVwiYXU5MTVfMVwiXG5cbiAgICAgICAgIyBNUVRUIHNlcnZlciAoZS5nLiBzY2hlbWU6Ly9ob3N0OnBvcnQgd2hlcmUgc2NoZW1lIGlzIHRjcCwgc3NsIG9yIHdzKVxuICAgICAgICBzZXJ2ZXI9XCJ0Y3A6Ly9tb3NxdWl0dG86MTg4M1wiXG5cbiAgICAgICAgIyBDb25uZWN0IHdpdGggdGhlIGdpdmVuIHVzZXJuYW1lIChvcHRpb25hbClcbiAgICAgICAgdXNlcm5hbWU9XCJcIlxuXG4gICAgICAgICMgQ29ubmVjdCB3aXRoIHRoZSBnaXZlbiBwYXNzd29yZCAob3B0aW9uYWwpXG4gICAgICAgIHBhc3N3b3JkPVwiXCJcblxuICAgICAgICAjIFF1YWxpdHkgb2Ygc2VydmljZSBsZXZlbFxuICAgICAgICAjXG4gICAgICAgICMgMDogYXQgbW9zdCBvbmNlXG4gICAgICAgICMgMTogYXQgbGVhc3Qgb25jZVxuICAgICAgICAjIDI6IGV4YWN0bHkgb25jZVxuICAgICAgICAjXG4gICAgICAgICMgTm90ZTogYW4gaW5jcmVhc2Ugb2YgdGhpcyB2YWx1ZSB3aWxsIGRlY3JlYXNlIHRoZSBwZXJmb3JtYW5jZS5cbiAgICAgICAgIyBGb3IgbW9yZSBpbmZvcm1hdGlvbjogaHR0cHM6Ly93d3cuaGl2ZW1xLmNvbS9ibG9nL21xdHQtZXNzZW50aWFscy1wYXJ0LTYtbXF0dC1xdWFsaXR5LW9mLXNlcnZpY2UtbGV2ZWxzXG4gICAgICAgIHFvcz0wXG5cbiAgICAgICAgIyBDbGVhbiBzZXNzaW9uXG4gICAgICAgICNcbiAgICAgICAgIyBTZXQgdGhlIFwiY2xlYW4gc2Vzc2lvblwiIGZsYWcgaW4gdGhlIGNvbm5lY3QgbWVzc2FnZSB3aGVuIHRoaXMgY2xpZW50XG4gICAgICAgICMgY29ubmVjdHMgdG8gYW4gTVFUVCBicm9rZXIuIEJ5IHNldHRpbmcgdGhpcyBmbGFnIHlvdSBhcmUgaW5kaWNhdGluZ1xuICAgICAgICAjIHRoYXQgbm8gbWVzc2FnZXMgc2F2ZWQgYnkgdGhlIGJyb2tlciBmb3IgdGhpcyBjbGllbnQgc2hvdWxkIGJlIGRlbGl2ZXJlZC5cbiAgICAgICAgY2xlYW5fc2Vzc2lvbj1mYWxzZVxuXG4gICAgICAgICMgQ2xpZW50IElEXG4gICAgICAgICNcbiAgICAgICAgIyBTZXQgdGhlIGNsaWVudCBpZCB0byBiZSB1c2VkIGJ5IHRoaXMgY2xpZW50IHdoZW4gY29ubmVjdGluZyB0byB0aGUgTVFUVFxuICAgICAgICAjIGJyb2tlci4gQSBjbGllbnQgaWQgbXVzdCBiZSBubyBsb25nZXIgdGhhbiAyMyBjaGFyYWN0ZXJzLiBJZiBsZWZ0IGJsYW5rLFxuICAgICAgICAjIGEgcmFuZG9tIGlkIHdpbGwgYmUgZ2VuZXJhdGVkIGJ5IENoaXJwU3RhY2suXG4gICAgICAgIGNsaWVudF9pZD1cIlwiXG5cbiAgICAgICAgIyBLZWVwIGFsaXZlIGludGVydmFsLlxuICAgICAgICAjXG4gICAgICAgICMgVGhpcyBkZWZpbmVzIHRoZSBtYXhpbXVtIHRpbWUgdGhhdCB0aGF0IHNob3VsZCBwYXNzIHdpdGhvdXQgY29tbXVuaWNhdGlvblxuICAgICAgICAjIGJldHdlZW4gdGhlIGNsaWVudCBhbmQgc2VydmVyLlxuICAgICAgICBrZWVwX2FsaXZlX2ludGVydmFsPVwiMzBzXCJcblxuICAgICAgICAjIENBIGNlcnRpZmljYXRlIGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICAjXG4gICAgICAgICMgVXNlIHRoaXMgd2hlbiBzZXR0aW5nIHVwIGEgc2VjdXJlIGNvbm5lY3Rpb24gKHdoZW4gc2VydmVyIHVzZXMgc3NsOi8vLi4uKVxuICAgICAgICAjIGJ1dCB0aGUgY2VydGlmaWNhdGUgdXNlZCBieSB0aGUgc2VydmVyIGlzIG5vdCB0cnVzdGVkIGJ5IGFueSBDQSBjZXJ0aWZpY2F0ZVxuICAgICAgICAjIG9uIHRoZSBzZXJ2ZXIgKGUuZy4gd2hlbiBzZWxmIGdlbmVyYXRlZCkuXG4gICAgICAgIGNhX2NlcnQ9XCJcIlxuXG4gICAgICAgICMgVExTIGNlcnRpZmljYXRlIGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICB0bHNfY2VydD1cIlwiXG5cbiAgICAgICAgIyBUTFMga2V5IGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICB0bHNfa2V5PVwiXCJcblxuXG4gICAgIyBHYXRld2F5IGNoYW5uZWwgY29uZmlndXJhdGlvbi5cbiAgICAjXG4gICAgIyBOb3RlOiB0aGlzIGNvbmZpZ3VyYXRpb24gaXMgb25seSB1c2VkIGluIGNhc2UgdGhlIGdhdGV3YXkgaXMgdXNpbmcgdGhlXG4gICAgIyBDaGlycFN0YWNrIENvbmNlbnRyYXRvcmQgZGFlbW9uLiBJbiBhbnkgb3RoZXIgY2FzZSwgdGhpcyBjb25maWd1cmF0aW9uIFxuICAgICMgaXMgaWdub3JlZC5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTE2ODAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MTcwMDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkxNzIwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTE3NDAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MTc2MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkxNzgwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTE4MDAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MTgyMDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkxNzUwMDAwMFxuICAgICAgYmFuZHdpZHRoPTUwMDAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzhdXG5cblxuICAjIFJlZ2lvbiBzcGVjaWZpYyBuZXR3b3JrIGNvbmZpZ3VyYXRpb24uXG4gIFtyZWdpb25zLm5ldHdvcmtdXG4gICAgXG4gICAgIyBJbnN0YWxsYXRpb24gbWFyZ2luIChkQikgdXNlZCBieSB0aGUgQURSIGVuZ2luZS5cbiAgICAjXG4gICAgIyBBIGhpZ2hlciBudW1iZXIgbWVhbnMgdGhhdCB0aGUgbmV0d29yay1zZXJ2ZXIgd2lsbCBrZWVwIG1vcmUgbWFyZ2luLFxuICAgICMgcmVzdWx0aW5nIGluIGEgbG93ZXIgZGF0YS1yYXRlIGJ1dCBkZWNyZWFzaW5nIHRoZSBjaGFuY2UgdGhhdCB0aGVcbiAgICAjIGRldmljZSBnZXRzIGRpc2Nvbm5lY3RlZCBiZWNhdXNlIGl0IGlzIHVuYWJsZSB0byByZWFjaCBvbmUgb2YgdGhlXG4gICAgIyBzdXJyb3VuZGVkIGdhdGV3YXlzLlxuICAgIGluc3RhbGxhdGlvbl9tYXJnaW49MTBcblxuICAgICMgUlggd2luZG93IChDbGFzcy1BKS5cbiAgICAjXG4gICAgIyBTZXQgdGhpcyB0bzpcbiAgICAjIDA6IFJYMSAvIFJYMlxuICAgICMgMTogUlgxIG9ubHlcbiAgICAjIDI6IFJYMiBvbmx5XG4gICAgcnhfd2luZG93PTBcblxuICAgICMgUlgxIGRlbGF5ICgxIC0gMTUgc2Vjb25kcykuXG4gICAgcngxX2RlbGF5PTFcblxuICAgICMgUlgxIGRhdGEtcmF0ZSBvZmZzZXRcbiAgICByeDFfZHJfb2Zmc2V0PTBcblxuICAgICMgUlgyIGRhdGEtcmF0ZVxuICAgIHJ4Ml9kcj04XG5cbiAgICAjIFJYMiBmcmVxdWVuY3kgKEh6KVxuICAgIHJ4Ml9mcmVxdWVuY3k9OTIzMzAwMDAwXG5cbiAgICAjIFByZWZlciBSWDIgb24gUlgxIGRhdGEtcmF0ZSBsZXNzIHRoYW4uXG4gICAgI1xuICAgICMgUHJlZmVyIFJYMiBvdmVyIFJYMSBiYXNlZCBvbiB0aGUgUlgxIGRhdGEtcmF0ZS4gV2hlbiB0aGUgUlgxIGRhdGEtcmF0ZVxuICAgICMgaXMgc21hbGxlciB0aGFuIHRoZSBjb25maWd1cmVkIHZhbHVlLCB0aGVuIHRoZSBOZXR3b3JrIFNlcnZlciB3aWxsXG4gICAgIyBmaXJzdCB0cnkgdG8gc2NoZWR1bGUgdGhlIGRvd25saW5rIGZvciBSWDIsIGZhaWxpbmcgdGhhdCAoZS5nLiB0aGUgZ2F0ZXdheVxuICAgICMgaGFzIGFscmVhZHkgYSBwYXlsb2FkIHNjaGVkdWxlZCBhdCB0aGUgUlgyIHRpbWluZykgaXQgd2lsbCB0cnkgUlgxLlxuICAgIHJ4Ml9wcmVmZXJfb25fcngxX2RyX2x0PTBcblxuICAgICMgUHJlZmVyIFJYMiBvbiBsaW5rIGJ1ZGdldC5cbiAgICAjXG4gICAgIyBXaGVuIHRoZSBsaW5rLWJ1ZGdldCBpcyBiZXR0ZXIgZm9yIFJYMiB0aGFuIGZvciBSWDEsIHRoZSBOZXR3b3JrIFNlcnZlciB3aWxsIGZpcnN0XG4gICAgIyB0cnkgdG8gc2NoZWR1bGUgdGhlIGRvd25saW5rIGluIFJYMiwgZmFpbGluZyB0aGF0IGl0IHdpbGwgdHJ5IFJYMS5cbiAgICByeDJfcHJlZmVyX29uX2xpbmtfYnVkZ2V0PWZhbHNlXG5cbiAgICAjIERvd25saW5rIFRYIFBvd2VyIChkQm0pXG4gICAgI1xuICAgICMgV2hlbiBzZXQgdG8gLTEsIHRoZSBkb3dubGluayBUWCBQb3dlciBmcm9tIHRoZSBjb25maWd1cmVkIGJhbmQgd2lsbFxuICAgICMgYmUgdXNlZC5cbiAgICAjXG4gICAgIyBQbGVhc2UgY29uc3VsdCB0aGUgTG9SYVdBTiBSZWdpb25hbCBQYXJhbWV0ZXJzIGFuZCBsb2NhbCByZWd1bGF0aW9uc1xuICAgICMgZm9yIHZhbGlkIGFuZCBsZWdhbCBvcHRpb25zLiBOb3RlIHRoYXQgdGhlIGNvbmZpZ3VyZWQgVFggUG93ZXIgbXVzdCBiZVxuICAgICMgc3VwcG9ydGVkIGJ5IHlvdXIgZ2F0ZXdheShzKS5cbiAgICBkb3dubGlua190eF9wb3dlcj0tMVxuXG4gICAgIyBBRFIgaXMgZGlzYWJsZWQuXG4gICAgYWRyX2Rpc2FibGVkPWZhbHNlXG5cbiAgICAjIE1pbmltdW0gZGF0YS1yYXRlLlxuICAgIG1pbl9kcj0wXG5cbiAgICAjIE1heGltdW0gZGF0YS1yYXRlLlxuICAgIG1heF9kcj01XG5cbiAgICAjIEVuYWJsZWQgdXBsaW5rIGNoYW5uZWxzLlxuICAgICNcbiAgICAjIFVzZSB0aGlzIHdoZW4gb255IGEgc3ViLXNldCBvZiB0aGUgYnkgZGVmYXVsdCBlbmFibGVkIGNoYW5uZWxzIGFyZSBiZWluZ1xuICAgICMgdXNlZC4gRm9yIGV4YW1wbGUgd2hlbiBvbmx5IHVzaW5nIHRoZSBmaXJzdCA4IGNoYW5uZWxzIG9mIHRoZSBVUyBiYW5kLlxuICAgICMgTm90ZTogd2hlbiBsZWZ0IGJsYW5rIC8gZW1wdHkgYXJyYXksIGFsbCBjaGFubmVscyB3aWxsIGJlIGVuYWJsZWQuXG4gICAgZW5hYmxlZF91cGxpbmtfY2hhbm5lbHM9WzgsIDksIDEwLCAxMSwgMTIsIDEzLCAxNCwgMTUsIDY1XVxuXG5cbiAgICAjIFJlam9pbi1yZXF1ZXN0IGNvbmZpZ3VyYXRpb24gKExvUmFXQU4gMS4xKVxuICAgIFtyZWdpb25zLm5ldHdvcmsucmVqb2luX3JlcXVlc3RdXG5cbiAgICAgICMgUmVxdWVzdCBkZXZpY2VzIHRvIHBlcmlvZGljYWxseSBzZW5kIHJlam9pbi1yZXF1ZXN0cy5cbiAgICAgIGVuYWJsZWQ9ZmFsc2VcblxuICAgICAgIyBUaGUgZGV2aWNlIG11c3Qgc2VuZCBhIHJlam9pbi1yZXF1ZXN0IHR5cGUgMCBhdCBsZWFzdCBldmVyeSAyXihtYXhfY291bnRfbiArIDQpXG4gICAgICAjIHVwbGluayBtZXNzYWdlcy4gVmFsaWQgdmFsdWVzIGFyZSAwIHRvIDE1LlxuICAgICAgbWF4X2NvdW50X249MFxuXG4gICAgICAjIFRoZSBkZXZpY2UgbXVzdCBzZW5kIGEgcmVqb2luLXJlcXVlc3QgdHlwZSAwIGF0IGxlYXN0IGV2ZXJ5IDJeKG1heF90aW1lX24gKyAxMClcbiAgICAgICMgc2Vjb25kcy4gVmFsaWQgdmFsdWVzIGFyZSAwIHRvIDE1LlxuICAgICAgI1xuICAgICAgIyAwICA9IHJvdWdobHkgMTcgbWludXRlc1xuICAgICAgIyAxNSA9IGFib3V0IDEgeWVhclxuICAgICAgbWF4X3RpbWVfbj0wXG4gICAgXG5cbiAgICAjIENsYXNzLUIgY29uZmlndXJhdGlvbi5cbiAgICBbcmVnaW9ucy5uZXR3b3JrLmNsYXNzX2JdXG5cbiAgICAgICMgUGluZy1zbG90IGRhdGEtcmF0ZS4gXG4gICAgICBwaW5nX3Nsb3RfZHI9OFxuXG4gICAgICAjIFBpbmctc2xvdCBmcmVxdWVuY3kgKEh6KVxuICAgICAgI1xuICAgICAgIyBzZXQgdGhpcyB0byAwIHRvIHVzZSB0aGUgZGVmYXVsdCBmcmVxdWVuY3kgcGxhbiBmb3IgdGhlIGNvbmZpZ3VyZWQgcmVnaW9uXG4gICAgICAjICh3aGljaCBjb3VsZCBiZSBmcmVxdWVuY3kgaG9wcGluZykuXG4gICAgICBwaW5nX3Nsb3RfZnJlcXVlbmN5PTBcblwiXCJcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuc2VydmljZU5hbWUgPSBcImNoaXJwc3RhY2tcIlxuZmlsZVBhdGggPSBcIi9jaGlycHN0YWNrL3JlZ2lvbl9hdTkxNV8yLnRvbWxcIlxuY29udGVudCA9IFwiXCJcIlxuIyBUaGlzIGZpbGUgY29udGFpbnMgYW4gZXhhbXBsZSBBVTkxNSBleGFtcGxlIChjaGFubmVscyAxNi0yMyArIDY2KS5cbltbcmVnaW9uc11dXG5cbiAgIyBJRCBpcyBhbiB1c2UtZGVmaW5lZCBpZGVudGlmaWVyIGZvciB0aGlzIHJlZ2lvbi5cbiAgaWQ9XCJhdTkxNV8yXCJcblxuICAjIERlc2NyaXB0aW9uIGlzIGEgc2hvcnQgZGVzY3JpcHRpb24gZm9yIHRoaXMgcmVnaW9uLlxuICBkZXNjcmlwdGlvbj1cIkFVOTE1IChjaGFubmVscyAxNi0yMyArIDY1KVwiXG5cbiAgIyBDb21tb24tbmFtZSByZWZlcnMgdG8gdGhlIGNvbW1vbi1uYW1lIG9mIHRoaXMgcmVnaW9uIGFzIGRlZmluZWQgYnlcbiAgIyB0aGUgTG9SYSBBbGxpYW5jZS5cbiAgY29tbW9uX25hbWU9XCJBVTkxNVwiXG5cblxuICAjIEdhdGV3YXkgY29uZmlndXJhdGlvbi5cbiAgW3JlZ2lvbnMuZ2F0ZXdheV1cblxuICAgICMgRm9yY2UgZ2F0ZXdheXMgYXMgcHJpdmF0ZS5cbiAgICAjXG4gICAgIyBJZiBlbmFibGVkLCBnYXRld2F5cyBjYW4gb25seSBiZSB1c2VkIGJ5IGRldmljZXMgdW5kZXIgdGhlIHNhbWUgdGVuYW50LlxuICAgIGZvcmNlX2d3c19wcml2YXRlPWZhbHNlXG5cbiAgICBcbiAgICAjIEdhdGV3YXkgYmFja2VuZCBjb25maWd1cmF0aW9uLlxuICAgIFtyZWdpb25zLmdhdGV3YXkuYmFja2VuZF1cblxuICAgICAgIyBUaGUgZW5hYmxlZCBiYWNrZW5kIHR5cGUuXG4gICAgICBlbmFibGVkPVwibXF0dFwiXG5cbiAgICAgICMgTVFUVCBjb25maWd1cmF0aW9uLlxuICAgICAgW3JlZ2lvbnMuZ2F0ZXdheS5iYWNrZW5kLm1xdHRdXG5cbiAgICAgICAgIyBUb3BpYyBwcmVmaXguXG4gICAgICAgICNcbiAgICAgICAgIyBUaGUgdG9waWMgcHJlZml4IGNhbiBiZSB1c2VkIHRvIGRlZmluZSB0aGUgcmVnaW9uIG9mIHRoZSBnYXRld2F5LlxuICAgICAgICAjIE5vdGUsIHRoZXJlIGlzIG5vIG5lZWQgdG8gYWRkIGEgdHJhaWxpbmcgJy8nIHRvIHRoZSBwcmVmaXguIFRoZSB0cmFpbGluZ1xuICAgICAgICAjICcvJyBpcyBhdXRvbWF0aWNhbGx5IGFkZGVkIHRvIHRoZSBwcmVmaXggaWYgaXQgaXMgY29uZmlndXJlZC5cbiAgICAgICAgdG9waWNfcHJlZml4PVwiYXU5MTVfMlwiXG5cbiAgICAgICAgIyBNUVRUIHNlcnZlciAoZS5nLiBzY2hlbWU6Ly9ob3N0OnBvcnQgd2hlcmUgc2NoZW1lIGlzIHRjcCwgc3NsIG9yIHdzKVxuICAgICAgICBzZXJ2ZXI9XCJ0Y3A6Ly9tb3NxdWl0dG86MTg4M1wiXG5cbiAgICAgICAgIyBDb25uZWN0IHdpdGggdGhlIGdpdmVuIHVzZXJuYW1lIChvcHRpb25hbClcbiAgICAgICAgdXNlcm5hbWU9XCJcIlxuXG4gICAgICAgICMgQ29ubmVjdCB3aXRoIHRoZSBnaXZlbiBwYXNzd29yZCAob3B0aW9uYWwpXG4gICAgICAgIHBhc3N3b3JkPVwiXCJcblxuICAgICAgICAjIFF1YWxpdHkgb2Ygc2VydmljZSBsZXZlbFxuICAgICAgICAjXG4gICAgICAgICMgMDogYXQgbW9zdCBvbmNlXG4gICAgICAgICMgMTogYXQgbGVhc3Qgb25jZVxuICAgICAgICAjIDI6IGV4YWN0bHkgb25jZVxuICAgICAgICAjXG4gICAgICAgICMgTm90ZTogYW4gaW5jcmVhc2Ugb2YgdGhpcyB2YWx1ZSB3aWxsIGRlY3JlYXNlIHRoZSBwZXJmb3JtYW5jZS5cbiAgICAgICAgIyBGb3IgbW9yZSBpbmZvcm1hdGlvbjogaHR0cHM6Ly93d3cuaGl2ZW1xLmNvbS9ibG9nL21xdHQtZXNzZW50aWFscy1wYXJ0LTYtbXF0dC1xdWFsaXR5LW9mLXNlcnZpY2UtbGV2ZWxzXG4gICAgICAgIHFvcz0wXG5cbiAgICAgICAgIyBDbGVhbiBzZXNzaW9uXG4gICAgICAgICNcbiAgICAgICAgIyBTZXQgdGhlIFwiY2xlYW4gc2Vzc2lvblwiIGZsYWcgaW4gdGhlIGNvbm5lY3QgbWVzc2FnZSB3aGVuIHRoaXMgY2xpZW50XG4gICAgICAgICMgY29ubmVjdHMgdG8gYW4gTVFUVCBicm9rZXIuIEJ5IHNldHRpbmcgdGhpcyBmbGFnIHlvdSBhcmUgaW5kaWNhdGluZ1xuICAgICAgICAjIHRoYXQgbm8gbWVzc2FnZXMgc2F2ZWQgYnkgdGhlIGJyb2tlciBmb3IgdGhpcyBjbGllbnQgc2hvdWxkIGJlIGRlbGl2ZXJlZC5cbiAgICAgICAgY2xlYW5fc2Vzc2lvbj1mYWxzZVxuXG4gICAgICAgICMgQ2xpZW50IElEXG4gICAgICAgICNcbiAgICAgICAgIyBTZXQgdGhlIGNsaWVudCBpZCB0byBiZSB1c2VkIGJ5IHRoaXMgY2xpZW50IHdoZW4gY29ubmVjdGluZyB0byB0aGUgTVFUVFxuICAgICAgICAjIGJyb2tlci4gQSBjbGllbnQgaWQgbXVzdCBiZSBubyBsb25nZXIgdGhhbiAyMyBjaGFyYWN0ZXJzLiBJZiBsZWZ0IGJsYW5rLFxuICAgICAgICAjIGEgcmFuZG9tIGlkIHdpbGwgYmUgZ2VuZXJhdGVkIGJ5IENoaXJwU3RhY2suXG4gICAgICAgIGNsaWVudF9pZD1cIlwiXG5cbiAgICAgICAgIyBLZWVwIGFsaXZlIGludGVydmFsLlxuICAgICAgICAjXG4gICAgICAgICMgVGhpcyBkZWZpbmVzIHRoZSBtYXhpbXVtIHRpbWUgdGhhdCB0aGF0IHNob3VsZCBwYXNzIHdpdGhvdXQgY29tbXVuaWNhdGlvblxuICAgICAgICAjIGJldHdlZW4gdGhlIGNsaWVudCBhbmQgc2VydmVyLlxuICAgICAgICBrZWVwX2FsaXZlX2ludGVydmFsPVwiMzBzXCJcblxuICAgICAgICAjIENBIGNlcnRpZmljYXRlIGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICAjXG4gICAgICAgICMgVXNlIHRoaXMgd2hlbiBzZXR0aW5nIHVwIGEgc2VjdXJlIGNvbm5lY3Rpb24gKHdoZW4gc2VydmVyIHVzZXMgc3NsOi8vLi4uKVxuICAgICAgICAjIGJ1dCB0aGUgY2VydGlmaWNhdGUgdXNlZCBieSB0aGUgc2VydmVyIGlzIG5vdCB0cnVzdGVkIGJ5IGFueSBDQSBjZXJ0aWZpY2F0ZVxuICAgICAgICAjIG9uIHRoZSBzZXJ2ZXIgKGUuZy4gd2hlbiBzZWxmIGdlbmVyYXRlZCkuXG4gICAgICAgIGNhX2NlcnQ9XCJcIlxuXG4gICAgICAgICMgVExTIGNlcnRpZmljYXRlIGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICB0bHNfY2VydD1cIlwiXG5cbiAgICAgICAgIyBUTFMga2V5IGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICB0bHNfa2V5PVwiXCJcblxuXG4gICAgIyBHYXRld2F5IGNoYW5uZWwgY29uZmlndXJhdGlvbi5cbiAgICAjXG4gICAgIyBOb3RlOiB0aGlzIGNvbmZpZ3VyYXRpb24gaXMgb25seSB1c2VkIGluIGNhc2UgdGhlIGdhdGV3YXkgaXMgdXNpbmcgdGhlXG4gICAgIyBDaGlycFN0YWNrIENvbmNlbnRyYXRvcmQgZGFlbW9uLiBJbiBhbnkgb3RoZXIgY2FzZSwgdGhpcyBjb25maWd1cmF0aW9uIFxuICAgICMgaXMgaWdub3JlZC5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTE4NDAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MTg2MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkxODgwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTE5MDAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MTkyMDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkxOTQwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTE5NjAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MTk4MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkxOTEwMDAwMFxuICAgICAgYmFuZHdpZHRoPTUwMDAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzhdXG5cblxuICAjIFJlZ2lvbiBzcGVjaWZpYyBuZXR3b3JrIGNvbmZpZ3VyYXRpb24uXG4gIFtyZWdpb25zLm5ldHdvcmtdXG4gICAgXG4gICAgIyBJbnN0YWxsYXRpb24gbWFyZ2luIChkQikgdXNlZCBieSB0aGUgQURSIGVuZ2luZS5cbiAgICAjXG4gICAgIyBBIGhpZ2hlciBudW1iZXIgbWVhbnMgdGhhdCB0aGUgbmV0d29yay1zZXJ2ZXIgd2lsbCBrZWVwIG1vcmUgbWFyZ2luLFxuICAgICMgcmVzdWx0aW5nIGluIGEgbG93ZXIgZGF0YS1yYXRlIGJ1dCBkZWNyZWFzaW5nIHRoZSBjaGFuY2UgdGhhdCB0aGVcbiAgICAjIGRldmljZSBnZXRzIGRpc2Nvbm5lY3RlZCBiZWNhdXNlIGl0IGlzIHVuYWJsZSB0byByZWFjaCBvbmUgb2YgdGhlXG4gICAgIyBzdXJyb3VuZGVkIGdhdGV3YXlzLlxuICAgIGluc3RhbGxhdGlvbl9tYXJnaW49MTBcblxuICAgICMgUlggd2luZG93IChDbGFzcy1BKS5cbiAgICAjXG4gICAgIyBTZXQgdGhpcyB0bzpcbiAgICAjIDA6IFJYMSAvIFJYMlxuICAgICMgMTogUlgxIG9ubHlcbiAgICAjIDI6IFJYMiBvbmx5XG4gICAgcnhfd2luZG93PTBcblxuICAgICMgUlgxIGRlbGF5ICgxIC0gMTUgc2Vjb25kcykuXG4gICAgcngxX2RlbGF5PTFcblxuICAgICMgUlgxIGRhdGEtcmF0ZSBvZmZzZXRcbiAgICByeDFfZHJfb2Zmc2V0PTBcblxuICAgICMgUlgyIGRhdGEtcmF0ZVxuICAgIHJ4Ml9kcj04XG5cbiAgICAjIFJYMiBmcmVxdWVuY3kgKEh6KVxuICAgIHJ4Ml9mcmVxdWVuY3k9OTIzMzAwMDAwXG5cbiAgICAjIFByZWZlciBSWDIgb24gUlgxIGRhdGEtcmF0ZSBsZXNzIHRoYW4uXG4gICAgI1xuICAgICMgUHJlZmVyIFJYMiBvdmVyIFJYMSBiYXNlZCBvbiB0aGUgUlgxIGRhdGEtcmF0ZS4gV2hlbiB0aGUgUlgxIGRhdGEtcmF0ZVxuICAgICMgaXMgc21hbGxlciB0aGFuIHRoZSBjb25maWd1cmVkIHZhbHVlLCB0aGVuIHRoZSBOZXR3b3JrIFNlcnZlciB3aWxsXG4gICAgIyBmaXJzdCB0cnkgdG8gc2NoZWR1bGUgdGhlIGRvd25saW5rIGZvciBSWDIsIGZhaWxpbmcgdGhhdCAoZS5nLiB0aGUgZ2F0ZXdheVxuICAgICMgaGFzIGFscmVhZHkgYSBwYXlsb2FkIHNjaGVkdWxlZCBhdCB0aGUgUlgyIHRpbWluZykgaXQgd2lsbCB0cnkgUlgxLlxuICAgIHJ4Ml9wcmVmZXJfb25fcngxX2RyX2x0PTBcblxuICAgICMgUHJlZmVyIFJYMiBvbiBsaW5rIGJ1ZGdldC5cbiAgICAjXG4gICAgIyBXaGVuIHRoZSBsaW5rLWJ1ZGdldCBpcyBiZXR0ZXIgZm9yIFJYMiB0aGFuIGZvciBSWDEsIHRoZSBOZXR3b3JrIFNlcnZlciB3aWxsIGZpcnN0XG4gICAgIyB0cnkgdG8gc2NoZWR1bGUgdGhlIGRvd25saW5rIGluIFJYMiwgZmFpbGluZyB0aGF0IGl0IHdpbGwgdHJ5IFJYMS5cbiAgICByeDJfcHJlZmVyX29uX2xpbmtfYnVkZ2V0PWZhbHNlXG5cbiAgICAjIERvd25saW5rIFRYIFBvd2VyIChkQm0pXG4gICAgI1xuICAgICMgV2hlbiBzZXQgdG8gLTEsIHRoZSBkb3dubGluayBUWCBQb3dlciBmcm9tIHRoZSBjb25maWd1cmVkIGJhbmQgd2lsbFxuICAgICMgYmUgdXNlZC5cbiAgICAjXG4gICAgIyBQbGVhc2UgY29uc3VsdCB0aGUgTG9SYVdBTiBSZWdpb25hbCBQYXJhbWV0ZXJzIGFuZCBsb2NhbCByZWd1bGF0aW9uc1xuICAgICMgZm9yIHZhbGlkIGFuZCBsZWdhbCBvcHRpb25zLiBOb3RlIHRoYXQgdGhlIGNvbmZpZ3VyZWQgVFggUG93ZXIgbXVzdCBiZVxuICAgICMgc3VwcG9ydGVkIGJ5IHlvdXIgZ2F0ZXdheShzKS5cbiAgICBkb3dubGlua190eF9wb3dlcj0tMVxuXG4gICAgIyBBRFIgaXMgZGlzYWJsZWQuXG4gICAgYWRyX2Rpc2FibGVkPWZhbHNlXG5cbiAgICAjIE1pbmltdW0gZGF0YS1yYXRlLlxuICAgIG1pbl9kcj0wXG5cbiAgICAjIE1heGltdW0gZGF0YS1yYXRlLlxuICAgIG1heF9kcj01XG5cbiAgICAjIEVuYWJsZWQgdXBsaW5rIGNoYW5uZWxzLlxuICAgICNcbiAgICAjIFVzZSB0aGlzIHdoZW4gb255IGEgc3ViLXNldCBvZiB0aGUgYnkgZGVmYXVsdCBlbmFibGVkIGNoYW5uZWxzIGFyZSBiZWluZ1xuICAgICMgdXNlZC4gRm9yIGV4YW1wbGUgd2hlbiBvbmx5IHVzaW5nIHRoZSBmaXJzdCA4IGNoYW5uZWxzIG9mIHRoZSBVUyBiYW5kLlxuICAgICMgTm90ZTogd2hlbiBsZWZ0IGJsYW5rIC8gZW1wdHkgYXJyYXksIGFsbCBjaGFubmVscyB3aWxsIGJlIGVuYWJsZWQuXG4gICAgZW5hYmxlZF91cGxpbmtfY2hhbm5lbHM9WzE2LCAxNywgMTgsIDE5LCAyMCwgMjEsIDIyLCAyMywgNjVdXG5cblxuICAgICMgUmVqb2luLXJlcXVlc3QgY29uZmlndXJhdGlvbiAoTG9SYVdBTiAxLjEpXG4gICAgW3JlZ2lvbnMubmV0d29yay5yZWpvaW5fcmVxdWVzdF1cblxuICAgICAgIyBSZXF1ZXN0IGRldmljZXMgdG8gcGVyaW9kaWNhbGx5IHNlbmQgcmVqb2luLXJlcXVlc3RzLlxuICAgICAgZW5hYmxlZD1mYWxzZVxuXG4gICAgICAjIFRoZSBkZXZpY2UgbXVzdCBzZW5kIGEgcmVqb2luLXJlcXVlc3QgdHlwZSAwIGF0IGxlYXN0IGV2ZXJ5IDJeKG1heF9jb3VudF9uICsgNClcbiAgICAgICMgdXBsaW5rIG1lc3NhZ2VzLiBWYWxpZCB2YWx1ZXMgYXJlIDAgdG8gMTUuXG4gICAgICBtYXhfY291bnRfbj0wXG5cbiAgICAgICMgVGhlIGRldmljZSBtdXN0IHNlbmQgYSByZWpvaW4tcmVxdWVzdCB0eXBlIDAgYXQgbGVhc3QgZXZlcnkgMl4obWF4X3RpbWVfbiArIDEwKVxuICAgICAgIyBzZWNvbmRzLiBWYWxpZCB2YWx1ZXMgYXJlIDAgdG8gMTUuXG4gICAgICAjXG4gICAgICAjIDAgID0gcm91Z2hseSAxNyBtaW51dGVzXG4gICAgICAjIDE1ID0gYWJvdXQgMSB5ZWFyXG4gICAgICBtYXhfdGltZV9uPTBcbiAgICBcblxuICAgICMgQ2xhc3MtQiBjb25maWd1cmF0aW9uLlxuICAgIFtyZWdpb25zLm5ldHdvcmsuY2xhc3NfYl1cblxuICAgICAgIyBQaW5nLXNsb3QgZGF0YS1yYXRlLiBcbiAgICAgIHBpbmdfc2xvdF9kcj04XG5cbiAgICAgICMgUGluZy1zbG90IGZyZXF1ZW5jeSAoSHopXG4gICAgICAjXG4gICAgICAjIHNldCB0aGlzIHRvIDAgdG8gdXNlIHRoZSBkZWZhdWx0IGZyZXF1ZW5jeSBwbGFuIGZvciB0aGUgY29uZmlndXJlZCByZWdpb25cbiAgICAgICMgKHdoaWNoIGNvdWxkIGJlIGZyZXF1ZW5jeSBob3BwaW5nKS5cbiAgICAgIHBpbmdfc2xvdF9mcmVxdWVuY3k9MFxuXCJcIlwiXG5cbltbY29uZmlnLm1vdW50c11dXG5zZXJ2aWNlTmFtZSA9IFwiY2hpcnBzdGFja1wiXG5maWxlUGF0aCA9IFwiL2NoaXJwc3RhY2svcmVnaW9uX2F1OTE1XzMudG9tbFwiXG5jb250ZW50ID0gXCJcIlwiXG4jIFRoaXMgZmlsZSBjb250YWlucyBhbiBleGFtcGxlIEFVOTE1IGV4YW1wbGUgKGNoYW5uZWxzIDI0LTMxICsgNjcpLlxuW1tyZWdpb25zXV1cblxuICAjIElEIGlzIGFuIHVzZS1kZWZpbmVkIGlkZW50aWZpZXIgZm9yIHRoaXMgcmVnaW9uLlxuICBpZD1cImF1OTE1XzNcIlxuXG4gICMgRGVzY3JpcHRpb24gaXMgYSBzaG9ydCBkZXNjcmlwdGlvbiBmb3IgdGhpcyByZWdpb24uXG4gIGRlc2NyaXB0aW9uPVwiQVU5MTUgKGNoYW5uZWxzIDI0LTMxICsgNjcpXCJcblxuICAjIENvbW1vbi1uYW1lIHJlZmVycyB0byB0aGUgY29tbW9uLW5hbWUgb2YgdGhpcyByZWdpb24gYXMgZGVmaW5lZCBieVxuICAjIHRoZSBMb1JhIEFsbGlhbmNlLlxuICBjb21tb25fbmFtZT1cIkFVOTE1XCJcblxuXG4gICMgR2F0ZXdheSBjb25maWd1cmF0aW9uLlxuICBbcmVnaW9ucy5nYXRld2F5XVxuXG4gICAgIyBGb3JjZSBnYXRld2F5cyBhcyBwcml2YXRlLlxuICAgICNcbiAgICAjIElmIGVuYWJsZWQsIGdhdGV3YXlzIGNhbiBvbmx5IGJlIHVzZWQgYnkgZGV2aWNlcyB1bmRlciB0aGUgc2FtZSB0ZW5hbnQuXG4gICAgZm9yY2VfZ3dzX3ByaXZhdGU9ZmFsc2VcblxuICAgIFxuICAgICMgR2F0ZXdheSBiYWNrZW5kIGNvbmZpZ3VyYXRpb24uXG4gICAgW3JlZ2lvbnMuZ2F0ZXdheS5iYWNrZW5kXVxuXG4gICAgICAjIFRoZSBlbmFibGVkIGJhY2tlbmQgdHlwZS5cbiAgICAgIGVuYWJsZWQ9XCJtcXR0XCJcblxuICAgICAgIyBNUVRUIGNvbmZpZ3VyYXRpb24uXG4gICAgICBbcmVnaW9ucy5nYXRld2F5LmJhY2tlbmQubXF0dF1cblxuICAgICAgICAjIFRvcGljIHByZWZpeC5cbiAgICAgICAgI1xuICAgICAgICAjIFRoZSB0b3BpYyBwcmVmaXggY2FuIGJlIHVzZWQgdG8gZGVmaW5lIHRoZSByZWdpb24gb2YgdGhlIGdhdGV3YXkuXG4gICAgICAgICMgTm90ZSwgdGhlcmUgaXMgbm8gbmVlZCB0byBhZGQgYSB0cmFpbGluZyAnLycgdG8gdGhlIHByZWZpeC4gVGhlIHRyYWlsaW5nXG4gICAgICAgICMgJy8nIGlzIGF1dG9tYXRpY2FsbHkgYWRkZWQgdG8gdGhlIHByZWZpeCBpZiBpdCBpcyBjb25maWd1cmVkLlxuICAgICAgICB0b3BpY19wcmVmaXg9XCJhdTkxNV8zXCJcblxuICAgICAgICAjIE1RVFQgc2VydmVyIChlLmcuIHNjaGVtZTovL2hvc3Q6cG9ydCB3aGVyZSBzY2hlbWUgaXMgdGNwLCBzc2wgb3Igd3MpXG4gICAgICAgIHNlcnZlcj1cInRjcDovL21vc3F1aXR0bzoxODgzXCJcblxuICAgICAgICAjIENvbm5lY3Qgd2l0aCB0aGUgZ2l2ZW4gdXNlcm5hbWUgKG9wdGlvbmFsKVxuICAgICAgICB1c2VybmFtZT1cIlwiXG5cbiAgICAgICAgIyBDb25uZWN0IHdpdGggdGhlIGdpdmVuIHBhc3N3b3JkIChvcHRpb25hbClcbiAgICAgICAgcGFzc3dvcmQ9XCJcIlxuXG4gICAgICAgICMgUXVhbGl0eSBvZiBzZXJ2aWNlIGxldmVsXG4gICAgICAgICNcbiAgICAgICAgIyAwOiBhdCBtb3N0IG9uY2VcbiAgICAgICAgIyAxOiBhdCBsZWFzdCBvbmNlXG4gICAgICAgICMgMjogZXhhY3RseSBvbmNlXG4gICAgICAgICNcbiAgICAgICAgIyBOb3RlOiBhbiBpbmNyZWFzZSBvZiB0aGlzIHZhbHVlIHdpbGwgZGVjcmVhc2UgdGhlIHBlcmZvcm1hbmNlLlxuICAgICAgICAjIEZvciBtb3JlIGluZm9ybWF0aW9uOiBodHRwczovL3d3dy5oaXZlbXEuY29tL2Jsb2cvbXF0dC1lc3NlbnRpYWxzLXBhcnQtNi1tcXR0LXF1YWxpdHktb2Ytc2VydmljZS1sZXZlbHNcbiAgICAgICAgcW9zPTBcblxuICAgICAgICAjIENsZWFuIHNlc3Npb25cbiAgICAgICAgI1xuICAgICAgICAjIFNldCB0aGUgXCJjbGVhbiBzZXNzaW9uXCIgZmxhZyBpbiB0aGUgY29ubmVjdCBtZXNzYWdlIHdoZW4gdGhpcyBjbGllbnRcbiAgICAgICAgIyBjb25uZWN0cyB0byBhbiBNUVRUIGJyb2tlci4gQnkgc2V0dGluZyB0aGlzIGZsYWcgeW91IGFyZSBpbmRpY2F0aW5nXG4gICAgICAgICMgdGhhdCBubyBtZXNzYWdlcyBzYXZlZCBieSB0aGUgYnJva2VyIGZvciB0aGlzIGNsaWVudCBzaG91bGQgYmUgZGVsaXZlcmVkLlxuICAgICAgICBjbGVhbl9zZXNzaW9uPWZhbHNlXG5cbiAgICAgICAgIyBDbGllbnQgSURcbiAgICAgICAgI1xuICAgICAgICAjIFNldCB0aGUgY2xpZW50IGlkIHRvIGJlIHVzZWQgYnkgdGhpcyBjbGllbnQgd2hlbiBjb25uZWN0aW5nIHRvIHRoZSBNUVRUXG4gICAgICAgICMgYnJva2VyLiBBIGNsaWVudCBpZCBtdXN0IGJlIG5vIGxvbmdlciB0aGFuIDIzIGNoYXJhY3RlcnMuIElmIGxlZnQgYmxhbmssXG4gICAgICAgICMgYSByYW5kb20gaWQgd2lsbCBiZSBnZW5lcmF0ZWQgYnkgQ2hpcnBTdGFjay5cbiAgICAgICAgY2xpZW50X2lkPVwiXCJcblxuICAgICAgICAjIEtlZXAgYWxpdmUgaW50ZXJ2YWwuXG4gICAgICAgICNcbiAgICAgICAgIyBUaGlzIGRlZmluZXMgdGhlIG1heGltdW0gdGltZSB0aGF0IHRoYXQgc2hvdWxkIHBhc3Mgd2l0aG91dCBjb21tdW5pY2F0aW9uXG4gICAgICAgICMgYmV0d2VlbiB0aGUgY2xpZW50IGFuZCBzZXJ2ZXIuXG4gICAgICAgIGtlZXBfYWxpdmVfaW50ZXJ2YWw9XCIzMHNcIlxuXG4gICAgICAgICMgQ0EgY2VydGlmaWNhdGUgZmlsZSAob3B0aW9uYWwpXG4gICAgICAgICNcbiAgICAgICAgIyBVc2UgdGhpcyB3aGVuIHNldHRpbmcgdXAgYSBzZWN1cmUgY29ubmVjdGlvbiAod2hlbiBzZXJ2ZXIgdXNlcyBzc2w6Ly8uLi4pXG4gICAgICAgICMgYnV0IHRoZSBjZXJ0aWZpY2F0ZSB1c2VkIGJ5IHRoZSBzZXJ2ZXIgaXMgbm90IHRydXN0ZWQgYnkgYW55IENBIGNlcnRpZmljYXRlXG4gICAgICAgICMgb24gdGhlIHNlcnZlciAoZS5nLiB3aGVuIHNlbGYgZ2VuZXJhdGVkKS5cbiAgICAgICAgY2FfY2VydD1cIlwiXG5cbiAgICAgICAgIyBUTFMgY2VydGlmaWNhdGUgZmlsZSAob3B0aW9uYWwpXG4gICAgICAgIHRsc19jZXJ0PVwiXCJcblxuICAgICAgICAjIFRMUyBrZXkgZmlsZSAob3B0aW9uYWwpXG4gICAgICAgIHRsc19rZXk9XCJcIlxuXG5cbiAgICAjIEdhdGV3YXkgY2hhbm5lbCBjb25maWd1cmF0aW9uLlxuICAgICNcbiAgICAjIE5vdGU6IHRoaXMgY29uZmlndXJhdGlvbiBpcyBvbmx5IHVzZWQgaW4gY2FzZSB0aGUgZ2F0ZXdheSBpcyB1c2luZyB0aGVcbiAgICAjIENoaXJwU3RhY2sgQ29uY2VudHJhdG9yZCBkYWVtb24uIEluIGFueSBvdGhlciBjYXNlLCB0aGlzIGNvbmZpZ3VyYXRpb24gXG4gICAgIyBpcyBpZ25vcmVkLlxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MjAwMDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkyMDIwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTIwNDAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MjA2MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkyMDgwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTIxMDAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MjEyMDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkyMTQwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTIwNzAwMDAwXG4gICAgICBiYW5kd2lkdGg9NTAwMDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bOF1cblxuXG4gICMgUmVnaW9uIHNwZWNpZmljIG5ldHdvcmsgY29uZmlndXJhdGlvbi5cbiAgW3JlZ2lvbnMubmV0d29ya11cbiAgICBcbiAgICAjIEluc3RhbGxhdGlvbiBtYXJnaW4gKGRCKSB1c2VkIGJ5IHRoZSBBRFIgZW5naW5lLlxuICAgICNcbiAgICAjIEEgaGlnaGVyIG51bWJlciBtZWFucyB0aGF0IHRoZSBuZXR3b3JrLXNlcnZlciB3aWxsIGtlZXAgbW9yZSBtYXJnaW4sXG4gICAgIyByZXN1bHRpbmcgaW4gYSBsb3dlciBkYXRhLXJhdGUgYnV0IGRlY3JlYXNpbmcgdGhlIGNoYW5jZSB0aGF0IHRoZVxuICAgICMgZGV2aWNlIGdldHMgZGlzY29ubmVjdGVkIGJlY2F1c2UgaXQgaXMgdW5hYmxlIHRvIHJlYWNoIG9uZSBvZiB0aGVcbiAgICAjIHN1cnJvdW5kZWQgZ2F0ZXdheXMuXG4gICAgaW5zdGFsbGF0aW9uX21hcmdpbj0xMFxuXG4gICAgIyBSWCB3aW5kb3cgKENsYXNzLUEpLlxuICAgICNcbiAgICAjIFNldCB0aGlzIHRvOlxuICAgICMgMDogUlgxIC8gUlgyXG4gICAgIyAxOiBSWDEgb25seVxuICAgICMgMjogUlgyIG9ubHlcbiAgICByeF93aW5kb3c9MFxuXG4gICAgIyBSWDEgZGVsYXkgKDEgLSAxNSBzZWNvbmRzKS5cbiAgICByeDFfZGVsYXk9MVxuXG4gICAgIyBSWDEgZGF0YS1yYXRlIG9mZnNldFxuICAgIHJ4MV9kcl9vZmZzZXQ9MFxuXG4gICAgIyBSWDIgZGF0YS1yYXRlXG4gICAgcngyX2RyPThcblxuICAgICMgUlgyIGZyZXF1ZW5jeSAoSHopXG4gICAgcngyX2ZyZXF1ZW5jeT05MjMzMDAwMDBcblxuICAgICMgUHJlZmVyIFJYMiBvbiBSWDEgZGF0YS1yYXRlIGxlc3MgdGhhbi5cbiAgICAjXG4gICAgIyBQcmVmZXIgUlgyIG92ZXIgUlgxIGJhc2VkIG9uIHRoZSBSWDEgZGF0YS1yYXRlLiBXaGVuIHRoZSBSWDEgZGF0YS1yYXRlXG4gICAgIyBpcyBzbWFsbGVyIHRoYW4gdGhlIGNvbmZpZ3VyZWQgdmFsdWUsIHRoZW4gdGhlIE5ldHdvcmsgU2VydmVyIHdpbGxcbiAgICAjIGZpcnN0IHRyeSB0byBzY2hlZHVsZSB0aGUgZG93bmxpbmsgZm9yIFJYMiwgZmFpbGluZyB0aGF0IChlLmcuIHRoZSBnYXRld2F5XG4gICAgIyBoYXMgYWxyZWFkeSBhIHBheWxvYWQgc2NoZWR1bGVkIGF0IHRoZSBSWDIgdGltaW5nKSBpdCB3aWxsIHRyeSBSWDEuXG4gICAgcngyX3ByZWZlcl9vbl9yeDFfZHJfbHQ9MFxuXG4gICAgIyBQcmVmZXIgUlgyIG9uIGxpbmsgYnVkZ2V0LlxuICAgICNcbiAgICAjIFdoZW4gdGhlIGxpbmstYnVkZ2V0IGlzIGJldHRlciBmb3IgUlgyIHRoYW4gZm9yIFJYMSwgdGhlIE5ldHdvcmsgU2VydmVyIHdpbGwgZmlyc3RcbiAgICAjIHRyeSB0byBzY2hlZHVsZSB0aGUgZG93bmxpbmsgaW4gUlgyLCBmYWlsaW5nIHRoYXQgaXQgd2lsbCB0cnkgUlgxLlxuICAgIHJ4Ml9wcmVmZXJfb25fbGlua19idWRnZXQ9ZmFsc2VcblxuICAgICMgRG93bmxpbmsgVFggUG93ZXIgKGRCbSlcbiAgICAjXG4gICAgIyBXaGVuIHNldCB0byAtMSwgdGhlIGRvd25saW5rIFRYIFBvd2VyIGZyb20gdGhlIGNvbmZpZ3VyZWQgYmFuZCB3aWxsXG4gICAgIyBiZSB1c2VkLlxuICAgICNcbiAgICAjIFBsZWFzZSBjb25zdWx0IHRoZSBMb1JhV0FOIFJlZ2lvbmFsIFBhcmFtZXRlcnMgYW5kIGxvY2FsIHJlZ3VsYXRpb25zXG4gICAgIyBmb3IgdmFsaWQgYW5kIGxlZ2FsIG9wdGlvbnMuIE5vdGUgdGhhdCB0aGUgY29uZmlndXJlZCBUWCBQb3dlciBtdXN0IGJlXG4gICAgIyBzdXBwb3J0ZWQgYnkgeW91ciBnYXRld2F5KHMpLlxuICAgIGRvd25saW5rX3R4X3Bvd2VyPS0xXG5cbiAgICAjIEFEUiBpcyBkaXNhYmxlZC5cbiAgICBhZHJfZGlzYWJsZWQ9ZmFsc2VcblxuICAgICMgTWluaW11bSBkYXRhLXJhdGUuXG4gICAgbWluX2RyPTBcblxuICAgICMgTWF4aW11bSBkYXRhLXJhdGUuXG4gICAgbWF4X2RyPTVcblxuICAgICMgRW5hYmxlZCB1cGxpbmsgY2hhbm5lbHMuXG4gICAgI1xuICAgICMgVXNlIHRoaXMgd2hlbiBvbnkgYSBzdWItc2V0IG9mIHRoZSBieSBkZWZhdWx0IGVuYWJsZWQgY2hhbm5lbHMgYXJlIGJlaW5nXG4gICAgIyB1c2VkLiBGb3IgZXhhbXBsZSB3aGVuIG9ubHkgdXNpbmcgdGhlIGZpcnN0IDggY2hhbm5lbHMgb2YgdGhlIFVTIGJhbmQuXG4gICAgIyBOb3RlOiB3aGVuIGxlZnQgYmxhbmsgLyBlbXB0eSBhcnJheSwgYWxsIGNoYW5uZWxzIHdpbGwgYmUgZW5hYmxlZC5cbiAgICBlbmFibGVkX3VwbGlua19jaGFubmVscz1bMjQsIDI1LCAyNiwgMjcsIDI4LCAyOSwgMzAsIDMxLCA2N11cblxuXG4gICAgIyBSZWpvaW4tcmVxdWVzdCBjb25maWd1cmF0aW9uIChMb1JhV0FOIDEuMSlcbiAgICBbcmVnaW9ucy5uZXR3b3JrLnJlam9pbl9yZXF1ZXN0XVxuXG4gICAgICAjIFJlcXVlc3QgZGV2aWNlcyB0byBwZXJpb2RpY2FsbHkgc2VuZCByZWpvaW4tcmVxdWVzdHMuXG4gICAgICBlbmFibGVkPWZhbHNlXG5cbiAgICAgICMgVGhlIGRldmljZSBtdXN0IHNlbmQgYSByZWpvaW4tcmVxdWVzdCB0eXBlIDAgYXQgbGVhc3QgZXZlcnkgMl4obWF4X2NvdW50X24gKyA0KVxuICAgICAgIyB1cGxpbmsgbWVzc2FnZXMuIFZhbGlkIHZhbHVlcyBhcmUgMCB0byAxNS5cbiAgICAgIG1heF9jb3VudF9uPTBcblxuICAgICAgIyBUaGUgZGV2aWNlIG11c3Qgc2VuZCBhIHJlam9pbi1yZXF1ZXN0IHR5cGUgMCBhdCBsZWFzdCBldmVyeSAyXihtYXhfdGltZV9uICsgMTApXG4gICAgICAjIHNlY29uZHMuIFZhbGlkIHZhbHVlcyBhcmUgMCB0byAxNS5cbiAgICAgICNcbiAgICAgICMgMCAgPSByb3VnaGx5IDE3IG1pbnV0ZXNcbiAgICAgICMgMTUgPSBhYm91dCAxIHllYXJcbiAgICAgIG1heF90aW1lX249MFxuICAgIFxuXG4gICAgIyBDbGFzcy1CIGNvbmZpZ3VyYXRpb24uXG4gICAgW3JlZ2lvbnMubmV0d29yay5jbGFzc19iXVxuXG4gICAgICAjIFBpbmctc2xvdCBkYXRhLXJhdGUuIFxuICAgICAgcGluZ19zbG90X2RyPThcblxuICAgICAgIyBQaW5nLXNsb3QgZnJlcXVlbmN5IChIeilcbiAgICAgICNcbiAgICAgICMgc2V0IHRoaXMgdG8gMCB0byB1c2UgdGhlIGRlZmF1bHQgZnJlcXVlbmN5IHBsYW4gZm9yIHRoZSBjb25maWd1cmVkIHJlZ2lvblxuICAgICAgIyAod2hpY2ggY291bGQgYmUgZnJlcXVlbmN5IGhvcHBpbmcpLlxuICAgICAgcGluZ19zbG90X2ZyZXF1ZW5jeT0wXG5cIlwiXCJcblxuW1tjb25maWcubW91bnRzXV1cbnNlcnZpY2VOYW1lID0gXCJjaGlycHN0YWNrXCJcbmZpbGVQYXRoID0gXCIvY2hpcnBzdGFjay9yZWdpb25fYXU5MTVfNC50b21sXCJcbmNvbnRlbnQgPSBcIlwiXCJcbiMgVGhpcyBmaWxlIGNvbnRhaW5zIGFuIGV4YW1wbGUgQVU5MTUgZXhhbXBsZSAoY2hhbm5lbHMgMzItMzkgKyA2OCkuXG5bW3JlZ2lvbnNdXVxuXG4gICMgSUQgaXMgYW4gdXNlLWRlZmluZWQgaWRlbnRpZmllciBmb3IgdGhpcyByZWdpb24uXG4gIGlkPVwiYXU5MTVfNFwiXG5cbiAgIyBEZXNjcmlwdGlvbiBpcyBhIHNob3J0IGRlc2NyaXB0aW9uIGZvciB0aGlzIHJlZ2lvbi5cbiAgZGVzY3JpcHRpb249XCJBVTkxNSAoY2hhbm5lbHMgMzItMzkgKyA2OClcIlxuXG4gICMgQ29tbW9uLW5hbWUgcmVmZXJzIHRvIHRoZSBjb21tb24tbmFtZSBvZiB0aGlzIHJlZ2lvbiBhcyBkZWZpbmVkIGJ5XG4gICMgdGhlIExvUmEgQWxsaWFuY2UuXG4gIGNvbW1vbl9uYW1lPVwiQVU5MTVcIlxuXG5cbiAgIyBHYXRld2F5IGNvbmZpZ3VyYXRpb24uXG4gIFtyZWdpb25zLmdhdGV3YXldXG5cbiAgICAjIEZvcmNlIGdhdGV3YXlzIGFzIHByaXZhdGUuXG4gICAgI1xuICAgICMgSWYgZW5hYmxlZCwgZ2F0ZXdheXMgY2FuIG9ubHkgYmUgdXNlZCBieSBkZXZpY2VzIHVuZGVyIHRoZSBzYW1lIHRlbmFudC5cbiAgICBmb3JjZV9nd3NfcHJpdmF0ZT1mYWxzZVxuXG4gICAgXG4gICAgIyBHYXRld2F5IGJhY2tlbmQgY29uZmlndXJhdGlvbi5cbiAgICBbcmVnaW9ucy5nYXRld2F5LmJhY2tlbmRdXG5cbiAgICAgICMgVGhlIGVuYWJsZWQgYmFja2VuZCB0eXBlLlxuICAgICAgZW5hYmxlZD1cIm1xdHRcIlxuXG4gICAgICAjIE1RVFQgY29uZmlndXJhdGlvbi5cbiAgICAgIFtyZWdpb25zLmdhdGV3YXkuYmFja2VuZC5tcXR0XVxuXG4gICAgICAgICMgVG9waWMgcHJlZml4LlxuICAgICAgICAjXG4gICAgICAgICMgVGhlIHRvcGljIHByZWZpeCBjYW4gYmUgdXNlZCB0byBkZWZpbmUgdGhlIHJlZ2lvbiBvZiB0aGUgZ2F0ZXdheS5cbiAgICAgICAgIyBOb3RlLCB0aGVyZSBpcyBubyBuZWVkIHRvIGFkZCBhIHRyYWlsaW5nICcvJyB0byB0aGUgcHJlZml4LiBUaGUgdHJhaWxpbmdcbiAgICAgICAgIyAnLycgaXMgYXV0b21hdGljYWxseSBhZGRlZCB0byB0aGUgcHJlZml4IGlmIGl0IGlzIGNvbmZpZ3VyZWQuXG4gICAgICAgIHRvcGljX3ByZWZpeD1cImF1OTE1XzRcIlxuXG4gICAgICAgICMgTVFUVCBzZXJ2ZXIgKGUuZy4gc2NoZW1lOi8vaG9zdDpwb3J0IHdoZXJlIHNjaGVtZSBpcyB0Y3AsIHNzbCBvciB3cylcbiAgICAgICAgc2VydmVyPVwidGNwOi8vbW9zcXVpdHRvOjE4ODNcIlxuXG4gICAgICAgICMgQ29ubmVjdCB3aXRoIHRoZSBnaXZlbiB1c2VybmFtZSAob3B0aW9uYWwpXG4gICAgICAgIHVzZXJuYW1lPVwiXCJcblxuICAgICAgICAjIENvbm5lY3Qgd2l0aCB0aGUgZ2l2ZW4gcGFzc3dvcmQgKG9wdGlvbmFsKVxuICAgICAgICBwYXNzd29yZD1cIlwiXG5cbiAgICAgICAgIyBRdWFsaXR5IG9mIHNlcnZpY2UgbGV2ZWxcbiAgICAgICAgI1xuICAgICAgICAjIDA6IGF0IG1vc3Qgb25jZVxuICAgICAgICAjIDE6IGF0IGxlYXN0IG9uY2VcbiAgICAgICAgIyAyOiBleGFjdGx5IG9uY2VcbiAgICAgICAgI1xuICAgICAgICAjIE5vdGU6IGFuIGluY3JlYXNlIG9mIHRoaXMgdmFsdWUgd2lsbCBkZWNyZWFzZSB0aGUgcGVyZm9ybWFuY2UuXG4gICAgICAgICMgRm9yIG1vcmUgaW5mb3JtYXRpb246IGh0dHBzOi8vd3d3LmhpdmVtcS5jb20vYmxvZy9tcXR0LWVzc2VudGlhbHMtcGFydC02LW1xdHQtcXVhbGl0eS1vZi1zZXJ2aWNlLWxldmVsc1xuICAgICAgICBxb3M9MFxuXG4gICAgICAgICMgQ2xlYW4gc2Vzc2lvblxuICAgICAgICAjXG4gICAgICAgICMgU2V0IHRoZSBcImNsZWFuIHNlc3Npb25cIiBmbGFnIGluIHRoZSBjb25uZWN0IG1lc3NhZ2Ugd2hlbiB0aGlzIGNsaWVudFxuICAgICAgICAjIGNvbm5lY3RzIHRvIGFuIE1RVFQgYnJva2VyLiBCeSBzZXR0aW5nIHRoaXMgZmxhZyB5b3UgYXJlIGluZGljYXRpbmdcbiAgICAgICAgIyB0aGF0IG5vIG1lc3NhZ2VzIHNhdmVkIGJ5IHRoZSBicm9rZXIgZm9yIHRoaXMgY2xpZW50IHNob3VsZCBiZSBkZWxpdmVyZWQuXG4gICAgICAgIGNsZWFuX3Nlc3Npb249ZmFsc2VcblxuICAgICAgICAjIENsaWVudCBJRFxuICAgICAgICAjXG4gICAgICAgICMgU2V0IHRoZSBjbGllbnQgaWQgdG8gYmUgdXNlZCBieSB0aGlzIGNsaWVudCB3aGVuIGNvbm5lY3RpbmcgdG8gdGhlIE1RVFRcbiAgICAgICAgIyBicm9rZXIuIEEgY2xpZW50IGlkIG11c3QgYmUgbm8gbG9uZ2VyIHRoYW4gMjMgY2hhcmFjdGVycy4gSWYgbGVmdCBibGFuayxcbiAgICAgICAgIyBhIHJhbmRvbSBpZCB3aWxsIGJlIGdlbmVyYXRlZCBieSBDaGlycFN0YWNrLlxuICAgICAgICBjbGllbnRfaWQ9XCJcIlxuXG4gICAgICAgICMgS2VlcCBhbGl2ZSBpbnRlcnZhbC5cbiAgICAgICAgI1xuICAgICAgICAjIFRoaXMgZGVmaW5lcyB0aGUgbWF4aW11bSB0aW1lIHRoYXQgdGhhdCBzaG91bGQgcGFzcyB3aXRob3V0IGNvbW11bmljYXRpb25cbiAgICAgICAgIyBiZXR3ZWVuIHRoZSBjbGllbnQgYW5kIHNlcnZlci5cbiAgICAgICAga2VlcF9hbGl2ZV9pbnRlcnZhbD1cIjMwc1wiXG5cbiAgICAgICAgIyBDQSBjZXJ0aWZpY2F0ZSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgI1xuICAgICAgICAjIFVzZSB0aGlzIHdoZW4gc2V0dGluZyB1cCBhIHNlY3VyZSBjb25uZWN0aW9uICh3aGVuIHNlcnZlciB1c2VzIHNzbDovLy4uLilcbiAgICAgICAgIyBidXQgdGhlIGNlcnRpZmljYXRlIHVzZWQgYnkgdGhlIHNlcnZlciBpcyBub3QgdHJ1c3RlZCBieSBhbnkgQ0EgY2VydGlmaWNhdGVcbiAgICAgICAgIyBvbiB0aGUgc2VydmVyIChlLmcuIHdoZW4gc2VsZiBnZW5lcmF0ZWQpLlxuICAgICAgICBjYV9jZXJ0PVwiXCJcblxuICAgICAgICAjIFRMUyBjZXJ0aWZpY2F0ZSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgdGxzX2NlcnQ9XCJcIlxuXG4gICAgICAgICMgVExTIGtleSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgdGxzX2tleT1cIlwiXG5cblxuICAgICMgR2F0ZXdheSBjaGFubmVsIGNvbmZpZ3VyYXRpb24uXG4gICAgI1xuICAgICMgTm90ZTogdGhpcyBjb25maWd1cmF0aW9uIGlzIG9ubHkgdXNlZCBpbiBjYXNlIHRoZSBnYXRld2F5IGlzIHVzaW5nIHRoZVxuICAgICMgQ2hpcnBTdGFjayBDb25jZW50cmF0b3JkIGRhZW1vbi4gSW4gYW55IG90aGVyIGNhc2UsIHRoaXMgY29uZmlndXJhdGlvbiBcbiAgICAjIGlzIGlnbm9yZWQuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkyMTYwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTIxODAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MjIwMDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkyMjIwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTIyNDAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MjI2MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkyMjgwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTIzMDAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MjIzMDAwMDBcbiAgICAgIGJhbmR3aWR0aD01MDAwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs4XVxuXG5cbiAgIyBSZWdpb24gc3BlY2lmaWMgbmV0d29yayBjb25maWd1cmF0aW9uLlxuICBbcmVnaW9ucy5uZXR3b3JrXVxuICAgIFxuICAgICMgSW5zdGFsbGF0aW9uIG1hcmdpbiAoZEIpIHVzZWQgYnkgdGhlIEFEUiBlbmdpbmUuXG4gICAgI1xuICAgICMgQSBoaWdoZXIgbnVtYmVyIG1lYW5zIHRoYXQgdGhlIG5ldHdvcmstc2VydmVyIHdpbGwga2VlcCBtb3JlIG1hcmdpbixcbiAgICAjIHJlc3VsdGluZyBpbiBhIGxvd2VyIGRhdGEtcmF0ZSBidXQgZGVjcmVhc2luZyB0aGUgY2hhbmNlIHRoYXQgdGhlXG4gICAgIyBkZXZpY2UgZ2V0cyBkaXNjb25uZWN0ZWQgYmVjYXVzZSBpdCBpcyB1bmFibGUgdG8gcmVhY2ggb25lIG9mIHRoZVxuICAgICMgc3Vycm91bmRlZCBnYXRld2F5cy5cbiAgICBpbnN0YWxsYXRpb25fbWFyZ2luPTEwXG5cbiAgICAjIFJYIHdpbmRvdyAoQ2xhc3MtQSkuXG4gICAgI1xuICAgICMgU2V0IHRoaXMgdG86XG4gICAgIyAwOiBSWDEgLyBSWDJcbiAgICAjIDE6IFJYMSBvbmx5XG4gICAgIyAyOiBSWDIgb25seVxuICAgIHJ4X3dpbmRvdz0wXG5cbiAgICAjIFJYMSBkZWxheSAoMSAtIDE1IHNlY29uZHMpLlxuICAgIHJ4MV9kZWxheT0xXG5cbiAgICAjIFJYMSBkYXRhLXJhdGUgb2Zmc2V0XG4gICAgcngxX2RyX29mZnNldD0wXG5cbiAgICAjIFJYMiBkYXRhLXJhdGVcbiAgICByeDJfZHI9OFxuXG4gICAgIyBSWDIgZnJlcXVlbmN5IChIeilcbiAgICByeDJfZnJlcXVlbmN5PTkyMzMwMDAwMFxuXG4gICAgIyBQcmVmZXIgUlgyIG9uIFJYMSBkYXRhLXJhdGUgbGVzcyB0aGFuLlxuICAgICNcbiAgICAjIFByZWZlciBSWDIgb3ZlciBSWDEgYmFzZWQgb24gdGhlIFJYMSBkYXRhLXJhdGUuIFdoZW4gdGhlIFJYMSBkYXRhLXJhdGVcbiAgICAjIGlzIHNtYWxsZXIgdGhhbiB0aGUgY29uZmlndXJlZCB2YWx1ZSwgdGhlbiB0aGUgTmV0d29yayBTZXJ2ZXIgd2lsbFxuICAgICMgZmlyc3QgdHJ5IHRvIHNjaGVkdWxlIHRoZSBkb3dubGluayBmb3IgUlgyLCBmYWlsaW5nIHRoYXQgKGUuZy4gdGhlIGdhdGV3YXlcbiAgICAjIGhhcyBhbHJlYWR5IGEgcGF5bG9hZCBzY2hlZHVsZWQgYXQgdGhlIFJYMiB0aW1pbmcpIGl0IHdpbGwgdHJ5IFJYMS5cbiAgICByeDJfcHJlZmVyX29uX3J4MV9kcl9sdD0wXG5cbiAgICAjIFByZWZlciBSWDIgb24gbGluayBidWRnZXQuXG4gICAgI1xuICAgICMgV2hlbiB0aGUgbGluay1idWRnZXQgaXMgYmV0dGVyIGZvciBSWDIgdGhhbiBmb3IgUlgxLCB0aGUgTmV0d29yayBTZXJ2ZXIgd2lsbCBmaXJzdFxuICAgICMgdHJ5IHRvIHNjaGVkdWxlIHRoZSBkb3dubGluayBpbiBSWDIsIGZhaWxpbmcgdGhhdCBpdCB3aWxsIHRyeSBSWDEuXG4gICAgcngyX3ByZWZlcl9vbl9saW5rX2J1ZGdldD1mYWxzZVxuXG4gICAgIyBEb3dubGluayBUWCBQb3dlciAoZEJtKVxuICAgICNcbiAgICAjIFdoZW4gc2V0IHRvIC0xLCB0aGUgZG93bmxpbmsgVFggUG93ZXIgZnJvbSB0aGUgY29uZmlndXJlZCBiYW5kIHdpbGxcbiAgICAjIGJlIHVzZWQuXG4gICAgI1xuICAgICMgUGxlYXNlIGNvbnN1bHQgdGhlIExvUmFXQU4gUmVnaW9uYWwgUGFyYW1ldGVycyBhbmQgbG9jYWwgcmVndWxhdGlvbnNcbiAgICAjIGZvciB2YWxpZCBhbmQgbGVnYWwgb3B0aW9ucy4gTm90ZSB0aGF0IHRoZSBjb25maWd1cmVkIFRYIFBvd2VyIG11c3QgYmVcbiAgICAjIHN1cHBvcnRlZCBieSB5b3VyIGdhdGV3YXkocykuXG4gICAgZG93bmxpbmtfdHhfcG93ZXI9LTFcblxuICAgICMgQURSIGlzIGRpc2FibGVkLlxuICAgIGFkcl9kaXNhYmxlZD1mYWxzZVxuXG4gICAgIyBNaW5pbXVtIGRhdGEtcmF0ZS5cbiAgICBtaW5fZHI9MFxuXG4gICAgIyBNYXhpbXVtIGRhdGEtcmF0ZS5cbiAgICBtYXhfZHI9NVxuXG4gICAgIyBFbmFibGVkIHVwbGluayBjaGFubmVscy5cbiAgICAjXG4gICAgIyBVc2UgdGhpcyB3aGVuIG9ueSBhIHN1Yi1zZXQgb2YgdGhlIGJ5IGRlZmF1bHQgZW5hYmxlZCBjaGFubmVscyBhcmUgYmVpbmdcbiAgICAjIHVzZWQuIEZvciBleGFtcGxlIHdoZW4gb25seSB1c2luZyB0aGUgZmlyc3QgOCBjaGFubmVscyBvZiB0aGUgVVMgYmFuZC5cbiAgICAjIE5vdGU6IHdoZW4gbGVmdCBibGFuayAvIGVtcHR5IGFycmF5LCBhbGwgY2hhbm5lbHMgd2lsbCBiZSBlbmFibGVkLlxuICAgIGVuYWJsZWRfdXBsaW5rX2NoYW5uZWxzPVszMiwgMzMsIDM0LCAzNSwgMzYsIDM3LCAzOCwgMzksIDY4XVxuXG5cbiAgICAjIFJlam9pbi1yZXF1ZXN0IGNvbmZpZ3VyYXRpb24gKExvUmFXQU4gMS4xKVxuICAgIFtyZWdpb25zLm5ldHdvcmsucmVqb2luX3JlcXVlc3RdXG5cbiAgICAgICMgUmVxdWVzdCBkZXZpY2VzIHRvIHBlcmlvZGljYWxseSBzZW5kIHJlam9pbi1yZXF1ZXN0cy5cbiAgICAgIGVuYWJsZWQ9ZmFsc2VcblxuICAgICAgIyBUaGUgZGV2aWNlIG11c3Qgc2VuZCBhIHJlam9pbi1yZXF1ZXN0IHR5cGUgMCBhdCBsZWFzdCBldmVyeSAyXihtYXhfY291bnRfbiArIDQpXG4gICAgICAjIHVwbGluayBtZXNzYWdlcy4gVmFsaWQgdmFsdWVzIGFyZSAwIHRvIDE1LlxuICAgICAgbWF4X2NvdW50X249MFxuXG4gICAgICAjIFRoZSBkZXZpY2UgbXVzdCBzZW5kIGEgcmVqb2luLXJlcXVlc3QgdHlwZSAwIGF0IGxlYXN0IGV2ZXJ5IDJeKG1heF90aW1lX24gKyAxMClcbiAgICAgICMgc2Vjb25kcy4gVmFsaWQgdmFsdWVzIGFyZSAwIHRvIDE1LlxuICAgICAgI1xuICAgICAgIyAwICA9IHJvdWdobHkgMTcgbWludXRlc1xuICAgICAgIyAxNSA9IGFib3V0IDEgeWVhclxuICAgICAgbWF4X3RpbWVfbj0wXG4gICAgXG5cbiAgICAjIENsYXNzLUIgY29uZmlndXJhdGlvbi5cbiAgICBbcmVnaW9ucy5uZXR3b3JrLmNsYXNzX2JdXG5cbiAgICAgICMgUGluZy1zbG90IGRhdGEtcmF0ZS4gXG4gICAgICBwaW5nX3Nsb3RfZHI9OFxuXG4gICAgICAjIFBpbmctc2xvdCBmcmVxdWVuY3kgKEh6KVxuICAgICAgI1xuICAgICAgIyBzZXQgdGhpcyB0byAwIHRvIHVzZSB0aGUgZGVmYXVsdCBmcmVxdWVuY3kgcGxhbiBmb3IgdGhlIGNvbmZpZ3VyZWQgcmVnaW9uXG4gICAgICAjICh3aGljaCBjb3VsZCBiZSBmcmVxdWVuY3kgaG9wcGluZykuXG4gICAgICBwaW5nX3Nsb3RfZnJlcXVlbmN5PTBcblwiXCJcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuc2VydmljZU5hbWUgPSBcImNoaXJwc3RhY2tcIlxuZmlsZVBhdGggPSBcIi9jaGlycHN0YWNrL3JlZ2lvbl9hdTkxNV81LnRvbWxcIlxuY29udGVudCA9IFwiXCJcIlxuIyBUaGlzIGZpbGUgY29udGFpbnMgYW4gZXhhbXBsZSBBVTkxNSBleGFtcGxlIChjaGFubmVscyA0MC00NyArIDY5KS5cbltbcmVnaW9uc11dXG5cbiAgIyBJRCBpcyBhbiB1c2UtZGVmaW5lZCBpZGVudGlmaWVyIGZvciB0aGlzIHJlZ2lvbi5cbiAgaWQ9XCJhdTkxNV81XCJcblxuICAjIERlc2NyaXB0aW9uIGlzIGEgc2hvcnQgZGVzY3JpcHRpb24gZm9yIHRoaXMgcmVnaW9uLlxuICBkZXNjcmlwdGlvbj1cIkFVOTE1IChjaGFubmVscyA0MC00NyArIDY5KVwiXG5cbiAgIyBDb21tb24tbmFtZSByZWZlcnMgdG8gdGhlIGNvbW1vbi1uYW1lIG9mIHRoaXMgcmVnaW9uIGFzIGRlZmluZWQgYnlcbiAgIyB0aGUgTG9SYSBBbGxpYW5jZS5cbiAgY29tbW9uX25hbWU9XCJBVTkxNVwiXG5cblxuICAjIEdhdGV3YXkgY29uZmlndXJhdGlvbi5cbiAgW3JlZ2lvbnMuZ2F0ZXdheV1cblxuICAgICMgRm9yY2UgZ2F0ZXdheXMgYXMgcHJpdmF0ZS5cbiAgICAjXG4gICAgIyBJZiBlbmFibGVkLCBnYXRld2F5cyBjYW4gb25seSBiZSB1c2VkIGJ5IGRldmljZXMgdW5kZXIgdGhlIHNhbWUgdGVuYW50LlxuICAgIGZvcmNlX2d3c19wcml2YXRlPWZhbHNlXG5cbiAgICBcbiAgICAjIEdhdGV3YXkgYmFja2VuZCBjb25maWd1cmF0aW9uLlxuICAgIFtyZWdpb25zLmdhdGV3YXkuYmFja2VuZF1cblxuICAgICAgIyBUaGUgZW5hYmxlZCBiYWNrZW5kIHR5cGUuXG4gICAgICBlbmFibGVkPVwibXF0dFwiXG5cbiAgICAgICMgTVFUVCBjb25maWd1cmF0aW9uLlxuICAgICAgW3JlZ2lvbnMuZ2F0ZXdheS5iYWNrZW5kLm1xdHRdXG5cbiAgICAgICAgIyBUb3BpYyBwcmVmaXguXG4gICAgICAgICNcbiAgICAgICAgIyBUaGUgdG9waWMgcHJlZml4IGNhbiBiZSB1c2VkIHRvIGRlZmluZSB0aGUgcmVnaW9uIG9mIHRoZSBnYXRld2F5LlxuICAgICAgICAjIE5vdGUsIHRoZXJlIGlzIG5vIG5lZWQgdG8gYWRkIGEgdHJhaWxpbmcgJy8nIHRvIHRoZSBwcmVmaXguIFRoZSB0cmFpbGluZ1xuICAgICAgICAjICcvJyBpcyBhdXRvbWF0aWNhbGx5IGFkZGVkIHRvIHRoZSBwcmVmaXggaWYgaXQgaXMgY29uZmlndXJlZC5cbiAgICAgICAgdG9waWNfcHJlZml4PVwiYXU5MTVfNVwiXG5cbiAgICAgICAgIyBNUVRUIHNlcnZlciAoZS5nLiBzY2hlbWU6Ly9ob3N0OnBvcnQgd2hlcmUgc2NoZW1lIGlzIHRjcCwgc3NsIG9yIHdzKVxuICAgICAgICBzZXJ2ZXI9XCJ0Y3A6Ly9tb3NxdWl0dG86MTg4M1wiXG5cbiAgICAgICAgIyBDb25uZWN0IHdpdGggdGhlIGdpdmVuIHVzZXJuYW1lIChvcHRpb25hbClcbiAgICAgICAgdXNlcm5hbWU9XCJcIlxuXG4gICAgICAgICMgQ29ubmVjdCB3aXRoIHRoZSBnaXZlbiBwYXNzd29yZCAob3B0aW9uYWwpXG4gICAgICAgIHBhc3N3b3JkPVwiXCJcblxuICAgICAgICAjIFF1YWxpdHkgb2Ygc2VydmljZSBsZXZlbFxuICAgICAgICAjXG4gICAgICAgICMgMDogYXQgbW9zdCBvbmNlXG4gICAgICAgICMgMTogYXQgbGVhc3Qgb25jZVxuICAgICAgICAjIDI6IGV4YWN0bHkgb25jZVxuICAgICAgICAjXG4gICAgICAgICMgTm90ZTogYW4gaW5jcmVhc2Ugb2YgdGhpcyB2YWx1ZSB3aWxsIGRlY3JlYXNlIHRoZSBwZXJmb3JtYW5jZS5cbiAgICAgICAgIyBGb3IgbW9yZSBpbmZvcm1hdGlvbjogaHR0cHM6Ly93d3cuaGl2ZW1xLmNvbS9ibG9nL21xdHQtZXNzZW50aWFscy1wYXJ0LTYtbXF0dC1xdWFsaXR5LW9mLXNlcnZpY2UtbGV2ZWxzXG4gICAgICAgIHFvcz0wXG5cbiAgICAgICAgIyBDbGVhbiBzZXNzaW9uXG4gICAgICAgICNcbiAgICAgICAgIyBTZXQgdGhlIFwiY2xlYW4gc2Vzc2lvblwiIGZsYWcgaW4gdGhlIGNvbm5lY3QgbWVzc2FnZSB3aGVuIHRoaXMgY2xpZW50XG4gICAgICAgICMgY29ubmVjdHMgdG8gYW4gTVFUVCBicm9rZXIuIEJ5IHNldHRpbmcgdGhpcyBmbGFnIHlvdSBhcmUgaW5kaWNhdGluZ1xuICAgICAgICAjIHRoYXQgbm8gbWVzc2FnZXMgc2F2ZWQgYnkgdGhlIGJyb2tlciBmb3IgdGhpcyBjbGllbnQgc2hvdWxkIGJlIGRlbGl2ZXJlZC5cbiAgICAgICAgY2xlYW5fc2Vzc2lvbj1mYWxzZVxuXG4gICAgICAgICMgQ2xpZW50IElEXG4gICAgICAgICNcbiAgICAgICAgIyBTZXQgdGhlIGNsaWVudCBpZCB0byBiZSB1c2VkIGJ5IHRoaXMgY2xpZW50IHdoZW4gY29ubmVjdGluZyB0byB0aGUgTVFUVFxuICAgICAgICAjIGJyb2tlci4gQSBjbGllbnQgaWQgbXVzdCBiZSBubyBsb25nZXIgdGhhbiAyMyBjaGFyYWN0ZXJzLiBJZiBsZWZ0IGJsYW5rLFxuICAgICAgICAjIGEgcmFuZG9tIGlkIHdpbGwgYmUgZ2VuZXJhdGVkIGJ5IENoaXJwU3RhY2suXG4gICAgICAgIGNsaWVudF9pZD1cIlwiXG5cbiAgICAgICAgIyBLZWVwIGFsaXZlIGludGVydmFsLlxuICAgICAgICAjXG4gICAgICAgICMgVGhpcyBkZWZpbmVzIHRoZSBtYXhpbXVtIHRpbWUgdGhhdCB0aGF0IHNob3VsZCBwYXNzIHdpdGhvdXQgY29tbXVuaWNhdGlvblxuICAgICAgICAjIGJldHdlZW4gdGhlIGNsaWVudCBhbmQgc2VydmVyLlxuICAgICAgICBrZWVwX2FsaXZlX2ludGVydmFsPVwiMzBzXCJcblxuICAgICAgICAjIENBIGNlcnRpZmljYXRlIGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICAjXG4gICAgICAgICMgVXNlIHRoaXMgd2hlbiBzZXR0aW5nIHVwIGEgc2VjdXJlIGNvbm5lY3Rpb24gKHdoZW4gc2VydmVyIHVzZXMgc3NsOi8vLi4uKVxuICAgICAgICAjIGJ1dCB0aGUgY2VydGlmaWNhdGUgdXNlZCBieSB0aGUgc2VydmVyIGlzIG5vdCB0cnVzdGVkIGJ5IGFueSBDQSBjZXJ0aWZpY2F0ZVxuICAgICAgICAjIG9uIHRoZSBzZXJ2ZXIgKGUuZy4gd2hlbiBzZWxmIGdlbmVyYXRlZCkuXG4gICAgICAgIGNhX2NlcnQ9XCJcIlxuXG4gICAgICAgICMgVExTIGNlcnRpZmljYXRlIGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICB0bHNfY2VydD1cIlwiXG5cbiAgICAgICAgIyBUTFMga2V5IGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICB0bHNfa2V5PVwiXCJcblxuXG4gICAgIyBHYXRld2F5IGNoYW5uZWwgY29uZmlndXJhdGlvbi5cbiAgICAjXG4gICAgIyBOb3RlOiB0aGlzIGNvbmZpZ3VyYXRpb24gaXMgb25seSB1c2VkIGluIGNhc2UgdGhlIGdhdGV3YXkgaXMgdXNpbmcgdGhlXG4gICAgIyBDaGlycFN0YWNrIENvbmNlbnRyYXRvcmQgZGFlbW9uLiBJbiBhbnkgb3RoZXIgY2FzZSwgdGhpcyBjb25maWd1cmF0aW9uIFxuICAgICMgaXMgaWdub3JlZC5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTIzMjAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MjM0MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkyMzYwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTIzODAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MjQwMDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkyNDIwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTI0NDAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MjQ2MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkyMzkwMDAwMFxuICAgICAgYmFuZHdpZHRoPTUwMDAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzhdXG5cblxuICAjIFJlZ2lvbiBzcGVjaWZpYyBuZXR3b3JrIGNvbmZpZ3VyYXRpb24uXG4gIFtyZWdpb25zLm5ldHdvcmtdXG4gICAgXG4gICAgIyBJbnN0YWxsYXRpb24gbWFyZ2luIChkQikgdXNlZCBieSB0aGUgQURSIGVuZ2luZS5cbiAgICAjXG4gICAgIyBBIGhpZ2hlciBudW1iZXIgbWVhbnMgdGhhdCB0aGUgbmV0d29yay1zZXJ2ZXIgd2lsbCBrZWVwIG1vcmUgbWFyZ2luLFxuICAgICMgcmVzdWx0aW5nIGluIGEgbG93ZXIgZGF0YS1yYXRlIGJ1dCBkZWNyZWFzaW5nIHRoZSBjaGFuY2UgdGhhdCB0aGVcbiAgICAjIGRldmljZSBnZXRzIGRpc2Nvbm5lY3RlZCBiZWNhdXNlIGl0IGlzIHVuYWJsZSB0byByZWFjaCBvbmUgb2YgdGhlXG4gICAgIyBzdXJyb3VuZGVkIGdhdGV3YXlzLlxuICAgIGluc3RhbGxhdGlvbl9tYXJnaW49MTBcblxuICAgICMgUlggd2luZG93IChDbGFzcy1BKS5cbiAgICAjXG4gICAgIyBTZXQgdGhpcyB0bzpcbiAgICAjIDA6IFJYMSAvIFJYMlxuICAgICMgMTogUlgxIG9ubHlcbiAgICAjIDI6IFJYMiBvbmx5XG4gICAgcnhfd2luZG93PTBcblxuICAgICMgUlgxIGRlbGF5ICgxIC0gMTUgc2Vjb25kcykuXG4gICAgcngxX2RlbGF5PTFcblxuICAgICMgUlgxIGRhdGEtcmF0ZSBvZmZzZXRcbiAgICByeDFfZHJfb2Zmc2V0PTBcblxuICAgICMgUlgyIGRhdGEtcmF0ZVxuICAgIHJ4Ml9kcj04XG5cbiAgICAjIFJYMiBmcmVxdWVuY3kgKEh6KVxuICAgIHJ4Ml9mcmVxdWVuY3k9OTIzMzAwMDAwXG5cbiAgICAjIFByZWZlciBSWDIgb24gUlgxIGRhdGEtcmF0ZSBsZXNzIHRoYW4uXG4gICAgI1xuICAgICMgUHJlZmVyIFJYMiBvdmVyIFJYMSBiYXNlZCBvbiB0aGUgUlgxIGRhdGEtcmF0ZS4gV2hlbiB0aGUgUlgxIGRhdGEtcmF0ZVxuICAgICMgaXMgc21hbGxlciB0aGFuIHRoZSBjb25maWd1cmVkIHZhbHVlLCB0aGVuIHRoZSBOZXR3b3JrIFNlcnZlciB3aWxsXG4gICAgIyBmaXJzdCB0cnkgdG8gc2NoZWR1bGUgdGhlIGRvd25saW5rIGZvciBSWDIsIGZhaWxpbmcgdGhhdCAoZS5nLiB0aGUgZ2F0ZXdheVxuICAgICMgaGFzIGFscmVhZHkgYSBwYXlsb2FkIHNjaGVkdWxlZCBhdCB0aGUgUlgyIHRpbWluZykgaXQgd2lsbCB0cnkgUlgxLlxuICAgIHJ4Ml9wcmVmZXJfb25fcngxX2RyX2x0PTBcblxuICAgICMgUHJlZmVyIFJYMiBvbiBsaW5rIGJ1ZGdldC5cbiAgICAjXG4gICAgIyBXaGVuIHRoZSBsaW5rLWJ1ZGdldCBpcyBiZXR0ZXIgZm9yIFJYMiB0aGFuIGZvciBSWDEsIHRoZSBOZXR3b3JrIFNlcnZlciB3aWxsIGZpcnN0XG4gICAgIyB0cnkgdG8gc2NoZWR1bGUgdGhlIGRvd25saW5rIGluIFJYMiwgZmFpbGluZyB0aGF0IGl0IHdpbGwgdHJ5IFJYMS5cbiAgICByeDJfcHJlZmVyX29uX2xpbmtfYnVkZ2V0PWZhbHNlXG5cbiAgICAjIERvd25saW5rIFRYIFBvd2VyIChkQm0pXG4gICAgI1xuICAgICMgV2hlbiBzZXQgdG8gLTEsIHRoZSBkb3dubGluayBUWCBQb3dlciBmcm9tIHRoZSBjb25maWd1cmVkIGJhbmQgd2lsbFxuICAgICMgYmUgdXNlZC5cbiAgICAjXG4gICAgIyBQbGVhc2UgY29uc3VsdCB0aGUgTG9SYVdBTiBSZWdpb25hbCBQYXJhbWV0ZXJzIGFuZCBsb2NhbCByZWd1bGF0aW9uc1xuICAgICMgZm9yIHZhbGlkIGFuZCBsZWdhbCBvcHRpb25zLiBOb3RlIHRoYXQgdGhlIGNvbmZpZ3VyZWQgVFggUG93ZXIgbXVzdCBiZVxuICAgICMgc3VwcG9ydGVkIGJ5IHlvdXIgZ2F0ZXdheShzKS5cbiAgICBkb3dubGlua190eF9wb3dlcj0tMVxuXG4gICAgIyBBRFIgaXMgZGlzYWJsZWQuXG4gICAgYWRyX2Rpc2FibGVkPWZhbHNlXG5cbiAgICAjIE1pbmltdW0gZGF0YS1yYXRlLlxuICAgIG1pbl9kcj0wXG5cbiAgICAjIE1heGltdW0gZGF0YS1yYXRlLlxuICAgIG1heF9kcj01XG5cbiAgICAjIEVuYWJsZWQgdXBsaW5rIGNoYW5uZWxzLlxuICAgICNcbiAgICAjIFVzZSB0aGlzIHdoZW4gb255IGEgc3ViLXNldCBvZiB0aGUgYnkgZGVmYXVsdCBlbmFibGVkIGNoYW5uZWxzIGFyZSBiZWluZ1xuICAgICMgdXNlZC4gRm9yIGV4YW1wbGUgd2hlbiBvbmx5IHVzaW5nIHRoZSBmaXJzdCA4IGNoYW5uZWxzIG9mIHRoZSBVUyBiYW5kLlxuICAgICMgTm90ZTogd2hlbiBsZWZ0IGJsYW5rIC8gZW1wdHkgYXJyYXksIGFsbCBjaGFubmVscyB3aWxsIGJlIGVuYWJsZWQuXG4gICAgZW5hYmxlZF91cGxpbmtfY2hhbm5lbHM9WzQwLCA0MSwgNDIsIDQzLCA0NCwgNDUsIDQ2LCA0NywgNjldXG5cblxuICAgICMgUmVqb2luLXJlcXVlc3QgY29uZmlndXJhdGlvbiAoTG9SYVdBTiAxLjEpXG4gICAgW3JlZ2lvbnMubmV0d29yay5yZWpvaW5fcmVxdWVzdF1cblxuICAgICAgIyBSZXF1ZXN0IGRldmljZXMgdG8gcGVyaW9kaWNhbGx5IHNlbmQgcmVqb2luLXJlcXVlc3RzLlxuICAgICAgZW5hYmxlZD1mYWxzZVxuXG4gICAgICAjIFRoZSBkZXZpY2UgbXVzdCBzZW5kIGEgcmVqb2luLXJlcXVlc3QgdHlwZSAwIGF0IGxlYXN0IGV2ZXJ5IDJeKG1heF9jb3VudF9uICsgNClcbiAgICAgICMgdXBsaW5rIG1lc3NhZ2VzLiBWYWxpZCB2YWx1ZXMgYXJlIDAgdG8gMTUuXG4gICAgICBtYXhfY291bnRfbj0wXG5cbiAgICAgICMgVGhlIGRldmljZSBtdXN0IHNlbmQgYSByZWpvaW4tcmVxdWVzdCB0eXBlIDAgYXQgbGVhc3QgZXZlcnkgMl4obWF4X3RpbWVfbiArIDEwKVxuICAgICAgIyBzZWNvbmRzLiBWYWxpZCB2YWx1ZXMgYXJlIDAgdG8gMTUuXG4gICAgICAjXG4gICAgICAjIDAgID0gcm91Z2hseSAxNyBtaW51dGVzXG4gICAgICAjIDE1ID0gYWJvdXQgMSB5ZWFyXG4gICAgICBtYXhfdGltZV9uPTBcbiAgICBcblxuICAgICMgQ2xhc3MtQiBjb25maWd1cmF0aW9uLlxuICAgIFtyZWdpb25zLm5ldHdvcmsuY2xhc3NfYl1cblxuICAgICAgIyBQaW5nLXNsb3QgZGF0YS1yYXRlLiBcbiAgICAgIHBpbmdfc2xvdF9kcj04XG5cbiAgICAgICMgUGluZy1zbG90IGZyZXF1ZW5jeSAoSHopXG4gICAgICAjXG4gICAgICAjIHNldCB0aGlzIHRvIDAgdG8gdXNlIHRoZSBkZWZhdWx0IGZyZXF1ZW5jeSBwbGFuIGZvciB0aGUgY29uZmlndXJlZCByZWdpb25cbiAgICAgICMgKHdoaWNoIGNvdWxkIGJlIGZyZXF1ZW5jeSBob3BwaW5nKS5cbiAgICAgIHBpbmdfc2xvdF9mcmVxdWVuY3k9MFxuXCJcIlwiXG5cbltbY29uZmlnLm1vdW50c11dXG5zZXJ2aWNlTmFtZSA9IFwiY2hpcnBzdGFja1wiXG5maWxlUGF0aCA9IFwiL2NoaXJwc3RhY2svcmVnaW9uX2F1OTE1XzYudG9tbFwiXG5jb250ZW50ID0gXCJcIlwiXG4jIFRoaXMgZmlsZSBjb250YWlucyBhbiBleGFtcGxlIEFVOTE1IGV4YW1wbGUgKGNoYW5uZWxzIDQ4LTU1ICsgNzApLlxuW1tyZWdpb25zXV1cblxuICAjIElEIGlzIGFuIHVzZS1kZWZpbmVkIGlkZW50aWZpZXIgZm9yIHRoaXMgcmVnaW9uLlxuICBpZD1cImF1OTE1XzZcIlxuXG4gICMgRGVzY3JpcHRpb24gaXMgYSBzaG9ydCBkZXNjcmlwdGlvbiBmb3IgdGhpcyByZWdpb24uXG4gIGRlc2NyaXB0aW9uPVwiQVU5MTUgKGNoYW5uZWxzIDQ4LTU1ICsgNzApXCJcblxuICAjIENvbW1vbi1uYW1lIHJlZmVycyB0byB0aGUgY29tbW9uLW5hbWUgb2YgdGhpcyByZWdpb24gYXMgZGVmaW5lZCBieVxuICAjIHRoZSBMb1JhIEFsbGlhbmNlLlxuICBjb21tb25fbmFtZT1cIkFVOTE1XCJcblxuXG4gICMgR2F0ZXdheSBjb25maWd1cmF0aW9uLlxuICBbcmVnaW9ucy5nYXRld2F5XVxuXG4gICAgIyBGb3JjZSBnYXRld2F5cyBhcyBwcml2YXRlLlxuICAgICNcbiAgICAjIElmIGVuYWJsZWQsIGdhdGV3YXlzIGNhbiBvbmx5IGJlIHVzZWQgYnkgZGV2aWNlcyB1bmRlciB0aGUgc2FtZSB0ZW5hbnQuXG4gICAgZm9yY2VfZ3dzX3ByaXZhdGU9ZmFsc2VcblxuICAgIFxuICAgICMgR2F0ZXdheSBiYWNrZW5kIGNvbmZpZ3VyYXRpb24uXG4gICAgW3JlZ2lvbnMuZ2F0ZXdheS5iYWNrZW5kXVxuXG4gICAgICAjIFRoZSBlbmFibGVkIGJhY2tlbmQgdHlwZS5cbiAgICAgIGVuYWJsZWQ9XCJtcXR0XCJcblxuICAgICAgIyBNUVRUIGNvbmZpZ3VyYXRpb24uXG4gICAgICBbcmVnaW9ucy5nYXRld2F5LmJhY2tlbmQubXF0dF1cblxuICAgICAgICAjIFRvcGljIHByZWZpeC5cbiAgICAgICAgI1xuICAgICAgICAjIFRoZSB0b3BpYyBwcmVmaXggY2FuIGJlIHVzZWQgdG8gZGVmaW5lIHRoZSByZWdpb24gb2YgdGhlIGdhdGV3YXkuXG4gICAgICAgICMgTm90ZSwgdGhlcmUgaXMgbm8gbmVlZCB0byBhZGQgYSB0cmFpbGluZyAnLycgdG8gdGhlIHByZWZpeC4gVGhlIHRyYWlsaW5nXG4gICAgICAgICMgJy8nIGlzIGF1dG9tYXRpY2FsbHkgYWRkZWQgdG8gdGhlIHByZWZpeCBpZiBpdCBpcyBjb25maWd1cmVkLlxuICAgICAgICB0b3BpY19wcmVmaXg9XCJhdTkxNV82XCJcblxuICAgICAgICAjIE1RVFQgc2VydmVyIChlLmcuIHNjaGVtZTovL2hvc3Q6cG9ydCB3aGVyZSBzY2hlbWUgaXMgdGNwLCBzc2wgb3Igd3MpXG4gICAgICAgIHNlcnZlcj1cInRjcDovL21vc3F1aXR0bzoxODgzXCJcblxuICAgICAgICAjIENvbm5lY3Qgd2l0aCB0aGUgZ2l2ZW4gdXNlcm5hbWUgKG9wdGlvbmFsKVxuICAgICAgICB1c2VybmFtZT1cIlwiXG5cbiAgICAgICAgIyBDb25uZWN0IHdpdGggdGhlIGdpdmVuIHBhc3N3b3JkIChvcHRpb25hbClcbiAgICAgICAgcGFzc3dvcmQ9XCJcIlxuXG4gICAgICAgICMgUXVhbGl0eSBvZiBzZXJ2aWNlIGxldmVsXG4gICAgICAgICNcbiAgICAgICAgIyAwOiBhdCBtb3N0IG9uY2VcbiAgICAgICAgIyAxOiBhdCBsZWFzdCBvbmNlXG4gICAgICAgICMgMjogZXhhY3RseSBvbmNlXG4gICAgICAgICNcbiAgICAgICAgIyBOb3RlOiBhbiBpbmNyZWFzZSBvZiB0aGlzIHZhbHVlIHdpbGwgZGVjcmVhc2UgdGhlIHBlcmZvcm1hbmNlLlxuICAgICAgICAjIEZvciBtb3JlIGluZm9ybWF0aW9uOiBodHRwczovL3d3dy5oaXZlbXEuY29tL2Jsb2cvbXF0dC1lc3NlbnRpYWxzLXBhcnQtNi1tcXR0LXF1YWxpdHktb2Ytc2VydmljZS1sZXZlbHNcbiAgICAgICAgcW9zPTBcblxuICAgICAgICAjIENsZWFuIHNlc3Npb25cbiAgICAgICAgI1xuICAgICAgICAjIFNldCB0aGUgXCJjbGVhbiBzZXNzaW9uXCIgZmxhZyBpbiB0aGUgY29ubmVjdCBtZXNzYWdlIHdoZW4gdGhpcyBjbGllbnRcbiAgICAgICAgIyBjb25uZWN0cyB0byBhbiBNUVRUIGJyb2tlci4gQnkgc2V0dGluZyB0aGlzIGZsYWcgeW91IGFyZSBpbmRpY2F0aW5nXG4gICAgICAgICMgdGhhdCBubyBtZXNzYWdlcyBzYXZlZCBieSB0aGUgYnJva2VyIGZvciB0aGlzIGNsaWVudCBzaG91bGQgYmUgZGVsaXZlcmVkLlxuICAgICAgICBjbGVhbl9zZXNzaW9uPWZhbHNlXG5cbiAgICAgICAgIyBDbGllbnQgSURcbiAgICAgICAgI1xuICAgICAgICAjIFNldCB0aGUgY2xpZW50IGlkIHRvIGJlIHVzZWQgYnkgdGhpcyBjbGllbnQgd2hlbiBjb25uZWN0aW5nIHRvIHRoZSBNUVRUXG4gICAgICAgICMgYnJva2VyLiBBIGNsaWVudCBpZCBtdXN0IGJlIG5vIGxvbmdlciB0aGFuIDIzIGNoYXJhY3RlcnMuIElmIGxlZnQgYmxhbmssXG4gICAgICAgICMgYSByYW5kb20gaWQgd2lsbCBiZSBnZW5lcmF0ZWQgYnkgQ2hpcnBTdGFjay5cbiAgICAgICAgY2xpZW50X2lkPVwiXCJcblxuICAgICAgICAjIEtlZXAgYWxpdmUgaW50ZXJ2YWwuXG4gICAgICAgICNcbiAgICAgICAgIyBUaGlzIGRlZmluZXMgdGhlIG1heGltdW0gdGltZSB0aGF0IHRoYXQgc2hvdWxkIHBhc3Mgd2l0aG91dCBjb21tdW5pY2F0aW9uXG4gICAgICAgICMgYmV0d2VlbiB0aGUgY2xpZW50IGFuZCBzZXJ2ZXIuXG4gICAgICAgIGtlZXBfYWxpdmVfaW50ZXJ2YWw9XCIzMHNcIlxuXG4gICAgICAgICMgQ0EgY2VydGlmaWNhdGUgZmlsZSAob3B0aW9uYWwpXG4gICAgICAgICNcbiAgICAgICAgIyBVc2UgdGhpcyB3aGVuIHNldHRpbmcgdXAgYSBzZWN1cmUgY29ubmVjdGlvbiAod2hlbiBzZXJ2ZXIgdXNlcyBzc2w6Ly8uLi4pXG4gICAgICAgICMgYnV0IHRoZSBjZXJ0aWZpY2F0ZSB1c2VkIGJ5IHRoZSBzZXJ2ZXIgaXMgbm90IHRydXN0ZWQgYnkgYW55IENBIGNlcnRpZmljYXRlXG4gICAgICAgICMgb24gdGhlIHNlcnZlciAoZS5nLiB3aGVuIHNlbGYgZ2VuZXJhdGVkKS5cbiAgICAgICAgY2FfY2VydD1cIlwiXG5cbiAgICAgICAgIyBUTFMgY2VydGlmaWNhdGUgZmlsZSAob3B0aW9uYWwpXG4gICAgICAgIHRsc19jZXJ0PVwiXCJcblxuICAgICAgICAjIFRMUyBrZXkgZmlsZSAob3B0aW9uYWwpXG4gICAgICAgIHRsc19rZXk9XCJcIlxuXG5cbiAgICAjIEdhdGV3YXkgY2hhbm5lbCBjb25maWd1cmF0aW9uLlxuICAgICNcbiAgICAjIE5vdGU6IHRoaXMgY29uZmlndXJhdGlvbiBpcyBvbmx5IHVzZWQgaW4gY2FzZSB0aGUgZ2F0ZXdheSBpcyB1c2luZyB0aGVcbiAgICAjIENoaXJwU3RhY2sgQ29uY2VudHJhdG9yZCBkYWVtb24uIEluIGFueSBvdGhlciBjYXNlLCB0aGlzIGNvbmZpZ3VyYXRpb24gXG4gICAgIyBpcyBpZ25vcmVkLlxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MjQ4MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkyNTAwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTI1MjAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MjU0MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkyNTYwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTI1ODAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MjYwMDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkyNjIwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTI1NTAwMDAwXG4gICAgICBiYW5kd2lkdGg9NTAwMDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bOF1cblxuXG4gICMgUmVnaW9uIHNwZWNpZmljIG5ldHdvcmsgY29uZmlndXJhdGlvbi5cbiAgW3JlZ2lvbnMubmV0d29ya11cbiAgICBcbiAgICAjIEluc3RhbGxhdGlvbiBtYXJnaW4gKGRCKSB1c2VkIGJ5IHRoZSBBRFIgZW5naW5lLlxuICAgICNcbiAgICAjIEEgaGlnaGVyIG51bWJlciBtZWFucyB0aGF0IHRoZSBuZXR3b3JrLXNlcnZlciB3aWxsIGtlZXAgbW9yZSBtYXJnaW4sXG4gICAgIyByZXN1bHRpbmcgaW4gYSBsb3dlciBkYXRhLXJhdGUgYnV0IGRlY3JlYXNpbmcgdGhlIGNoYW5jZSB0aGF0IHRoZVxuICAgICMgZGV2aWNlIGdldHMgZGlzY29ubmVjdGVkIGJlY2F1c2UgaXQgaXMgdW5hYmxlIHRvIHJlYWNoIG9uZSBvZiB0aGVcbiAgICAjIHN1cnJvdW5kZWQgZ2F0ZXdheXMuXG4gICAgaW5zdGFsbGF0aW9uX21hcmdpbj0xMFxuXG4gICAgIyBSWCB3aW5kb3cgKENsYXNzLUEpLlxuICAgICNcbiAgICAjIFNldCB0aGlzIHRvOlxuICAgICMgMDogUlgxIC8gUlgyXG4gICAgIyAxOiBSWDEgb25seVxuICAgICMgMjogUlgyIG9ubHlcbiAgICByeF93aW5kb3c9MFxuXG4gICAgIyBSWDEgZGVsYXkgKDEgLSAxNSBzZWNvbmRzKS5cbiAgICByeDFfZGVsYXk9MVxuXG4gICAgIyBSWDEgZGF0YS1yYXRlIG9mZnNldFxuICAgIHJ4MV9kcl9vZmZzZXQ9MFxuXG4gICAgIyBSWDIgZGF0YS1yYXRlXG4gICAgcngyX2RyPThcblxuICAgICMgUlgyIGZyZXF1ZW5jeSAoSHopXG4gICAgcngyX2ZyZXF1ZW5jeT05MjMzMDAwMDBcblxuICAgICMgUHJlZmVyIFJYMiBvbiBSWDEgZGF0YS1yYXRlIGxlc3MgdGhhbi5cbiAgICAjXG4gICAgIyBQcmVmZXIgUlgyIG92ZXIgUlgxIGJhc2VkIG9uIHRoZSBSWDEgZGF0YS1yYXRlLiBXaGVuIHRoZSBSWDEgZGF0YS1yYXRlXG4gICAgIyBpcyBzbWFsbGVyIHRoYW4gdGhlIGNvbmZpZ3VyZWQgdmFsdWUsIHRoZW4gdGhlIE5ldHdvcmsgU2VydmVyIHdpbGxcbiAgICAjIGZpcnN0IHRyeSB0byBzY2hlZHVsZSB0aGUgZG93bmxpbmsgZm9yIFJYMiwgZmFpbGluZyB0aGF0IChlLmcuIHRoZSBnYXRld2F5XG4gICAgIyBoYXMgYWxyZWFkeSBhIHBheWxvYWQgc2NoZWR1bGVkIGF0IHRoZSBSWDIgdGltaW5nKSBpdCB3aWxsIHRyeSBSWDEuXG4gICAgcngyX3ByZWZlcl9vbl9yeDFfZHJfbHQ9MFxuXG4gICAgIyBQcmVmZXIgUlgyIG9uIGxpbmsgYnVkZ2V0LlxuICAgICNcbiAgICAjIFdoZW4gdGhlIGxpbmstYnVkZ2V0IGlzIGJldHRlciBmb3IgUlgyIHRoYW4gZm9yIFJYMSwgdGhlIE5ldHdvcmsgU2VydmVyIHdpbGwgZmlyc3RcbiAgICAjIHRyeSB0byBzY2hlZHVsZSB0aGUgZG93bmxpbmsgaW4gUlgyLCBmYWlsaW5nIHRoYXQgaXQgd2lsbCB0cnkgUlgxLlxuICAgIHJ4Ml9wcmVmZXJfb25fbGlua19idWRnZXQ9ZmFsc2VcblxuICAgICMgRG93bmxpbmsgVFggUG93ZXIgKGRCbSlcbiAgICAjXG4gICAgIyBXaGVuIHNldCB0byAtMSwgdGhlIGRvd25saW5rIFRYIFBvd2VyIGZyb20gdGhlIGNvbmZpZ3VyZWQgYmFuZCB3aWxsXG4gICAgIyBiZSB1c2VkLlxuICAgICNcbiAgICAjIFBsZWFzZSBjb25zdWx0IHRoZSBMb1JhV0FOIFJlZ2lvbmFsIFBhcmFtZXRlcnMgYW5kIGxvY2FsIHJlZ3VsYXRpb25zXG4gICAgIyBmb3IgdmFsaWQgYW5kIGxlZ2FsIG9wdGlvbnMuIE5vdGUgdGhhdCB0aGUgY29uZmlndXJlZCBUWCBQb3dlciBtdXN0IGJlXG4gICAgIyBzdXBwb3J0ZWQgYnkgeW91ciBnYXRld2F5KHMpLlxuICAgIGRvd25saW5rX3R4X3Bvd2VyPS0xXG5cbiAgICAjIEFEUiBpcyBkaXNhYmxlZC5cbiAgICBhZHJfZGlzYWJsZWQ9ZmFsc2VcblxuICAgICMgTWluaW11bSBkYXRhLXJhdGUuXG4gICAgbWluX2RyPTBcblxuICAgICMgTWF4aW11bSBkYXRhLXJhdGUuXG4gICAgbWF4X2RyPTVcblxuICAgICMgRW5hYmxlZCB1cGxpbmsgY2hhbm5lbHMuXG4gICAgI1xuICAgICMgVXNlIHRoaXMgd2hlbiBvbnkgYSBzdWItc2V0IG9mIHRoZSBieSBkZWZhdWx0IGVuYWJsZWQgY2hhbm5lbHMgYXJlIGJlaW5nXG4gICAgIyB1c2VkLiBGb3IgZXhhbXBsZSB3aGVuIG9ubHkgdXNpbmcgdGhlIGZpcnN0IDggY2hhbm5lbHMgb2YgdGhlIFVTIGJhbmQuXG4gICAgIyBOb3RlOiB3aGVuIGxlZnQgYmxhbmsgLyBlbXB0eSBhcnJheSwgYWxsIGNoYW5uZWxzIHdpbGwgYmUgZW5hYmxlZC5cbiAgICBlbmFibGVkX3VwbGlua19jaGFubmVscz1bNDgsIDQ5LCA1MCwgNTEsIDUyLCA1MywgNTQsIDU1LCA3MF1cblxuXG4gICAgIyBSZWpvaW4tcmVxdWVzdCBjb25maWd1cmF0aW9uIChMb1JhV0FOIDEuMSlcbiAgICBbcmVnaW9ucy5uZXR3b3JrLnJlam9pbl9yZXF1ZXN0XVxuXG4gICAgICAjIFJlcXVlc3QgZGV2aWNlcyB0byBwZXJpb2RpY2FsbHkgc2VuZCByZWpvaW4tcmVxdWVzdHMuXG4gICAgICBlbmFibGVkPWZhbHNlXG5cbiAgICAgICMgVGhlIGRldmljZSBtdXN0IHNlbmQgYSByZWpvaW4tcmVxdWVzdCB0eXBlIDAgYXQgbGVhc3QgZXZlcnkgMl4obWF4X2NvdW50X24gKyA0KVxuICAgICAgIyB1cGxpbmsgbWVzc2FnZXMuIFZhbGlkIHZhbHVlcyBhcmUgMCB0byAxNS5cbiAgICAgIG1heF9jb3VudF9uPTBcblxuICAgICAgIyBUaGUgZGV2aWNlIG11c3Qgc2VuZCBhIHJlam9pbi1yZXF1ZXN0IHR5cGUgMCBhdCBsZWFzdCBldmVyeSAyXihtYXhfdGltZV9uICsgMTApXG4gICAgICAjIHNlY29uZHMuIFZhbGlkIHZhbHVlcyBhcmUgMCB0byAxNS5cbiAgICAgICNcbiAgICAgICMgMCAgPSByb3VnaGx5IDE3IG1pbnV0ZXNcbiAgICAgICMgMTUgPSBhYm91dCAxIHllYXJcbiAgICAgIG1heF90aW1lX249MFxuICAgIFxuXG4gICAgIyBDbGFzcy1CIGNvbmZpZ3VyYXRpb24uXG4gICAgW3JlZ2lvbnMubmV0d29yay5jbGFzc19iXVxuXG4gICAgICAjIFBpbmctc2xvdCBkYXRhLXJhdGUuIFxuICAgICAgcGluZ19zbG90X2RyPThcblxuICAgICAgIyBQaW5nLXNsb3QgZnJlcXVlbmN5IChIeilcbiAgICAgICNcbiAgICAgICMgc2V0IHRoaXMgdG8gMCB0byB1c2UgdGhlIGRlZmF1bHQgZnJlcXVlbmN5IHBsYW4gZm9yIHRoZSBjb25maWd1cmVkIHJlZ2lvblxuICAgICAgIyAod2hpY2ggY291bGQgYmUgZnJlcXVlbmN5IGhvcHBpbmcpLlxuICAgICAgcGluZ19zbG90X2ZyZXF1ZW5jeT0wXG5cIlwiXCJcblxuW1tjb25maWcubW91bnRzXV1cbnNlcnZpY2VOYW1lID0gXCJjaGlycHN0YWNrXCJcbmZpbGVQYXRoID0gXCIvY2hpcnBzdGFjay9yZWdpb25fYXU5MTVfNy50b21sXCJcbmNvbnRlbnQgPSBcIlwiXCJcbiMgVGhpcyBmaWxlIGNvbnRhaW5zIGFuIGV4YW1wbGUgQVU5MTUgZXhhbXBsZSAoY2hhbm5lbHMgNTYtNjMgKyA3MSkuXG5bW3JlZ2lvbnNdXVxuXG4gICMgSUQgaXMgYW4gdXNlLWRlZmluZWQgaWRlbnRpZmllciBmb3IgdGhpcyByZWdpb24uXG4gIGlkPVwiYXU5MTVfN1wiXG5cbiAgIyBEZXNjcmlwdGlvbiBpcyBhIHNob3J0IGRlc2NyaXB0aW9uIGZvciB0aGlzIHJlZ2lvbi5cbiAgZGVzY3JpcHRpb249XCJBVTkxNSAoY2hhbm5lbHMgNTYtNjMgKyA3MSlcIlxuXG4gICMgQ29tbW9uLW5hbWUgcmVmZXJzIHRvIHRoZSBjb21tb24tbmFtZSBvZiB0aGlzIHJlZ2lvbiBhcyBkZWZpbmVkIGJ5XG4gICMgdGhlIExvUmEgQWxsaWFuY2UuXG4gIGNvbW1vbl9uYW1lPVwiQVU5MTVcIlxuXG5cbiAgIyBHYXRld2F5IGNvbmZpZ3VyYXRpb24uXG4gIFtyZWdpb25zLmdhdGV3YXldXG5cbiAgICAjIEZvcmNlIGdhdGV3YXlzIGFzIHByaXZhdGUuXG4gICAgI1xuICAgICMgSWYgZW5hYmxlZCwgZ2F0ZXdheXMgY2FuIG9ubHkgYmUgdXNlZCBieSBkZXZpY2VzIHVuZGVyIHRoZSBzYW1lIHRlbmFudC5cbiAgICBmb3JjZV9nd3NfcHJpdmF0ZT1mYWxzZVxuXG4gICAgXG4gICAgIyBHYXRld2F5IGJhY2tlbmQgY29uZmlndXJhdGlvbi5cbiAgICBbcmVnaW9ucy5nYXRld2F5LmJhY2tlbmRdXG5cbiAgICAgICMgVGhlIGVuYWJsZWQgYmFja2VuZCB0eXBlLlxuICAgICAgZW5hYmxlZD1cIm1xdHRcIlxuXG4gICAgICAjIE1RVFQgY29uZmlndXJhdGlvbi5cbiAgICAgIFtyZWdpb25zLmdhdGV3YXkuYmFja2VuZC5tcXR0XVxuXG4gICAgICAgICMgVG9waWMgcHJlZml4LlxuICAgICAgICAjXG4gICAgICAgICMgVGhlIHRvcGljIHByZWZpeCBjYW4gYmUgdXNlZCB0byBkZWZpbmUgdGhlIHJlZ2lvbiBvZiB0aGUgZ2F0ZXdheS5cbiAgICAgICAgIyBOb3RlLCB0aGVyZSBpcyBubyBuZWVkIHRvIGFkZCBhIHRyYWlsaW5nICcvJyB0byB0aGUgcHJlZml4LiBUaGUgdHJhaWxpbmdcbiAgICAgICAgIyAnLycgaXMgYXV0b21hdGljYWxseSBhZGRlZCB0byB0aGUgcHJlZml4IGlmIGl0IGlzIGNvbmZpZ3VyZWQuXG4gICAgICAgIHRvcGljX3ByZWZpeD1cImF1OTE1XzdcIlxuXG4gICAgICAgICMgTVFUVCBzZXJ2ZXIgKGUuZy4gc2NoZW1lOi8vaG9zdDpwb3J0IHdoZXJlIHNjaGVtZSBpcyB0Y3AsIHNzbCBvciB3cylcbiAgICAgICAgc2VydmVyPVwidGNwOi8vbW9zcXVpdHRvOjE4ODNcIlxuXG4gICAgICAgICMgQ29ubmVjdCB3aXRoIHRoZSBnaXZlbiB1c2VybmFtZSAob3B0aW9uYWwpXG4gICAgICAgIHVzZXJuYW1lPVwiXCJcblxuICAgICAgICAjIENvbm5lY3Qgd2l0aCB0aGUgZ2l2ZW4gcGFzc3dvcmQgKG9wdGlvbmFsKVxuICAgICAgICBwYXNzd29yZD1cIlwiXG5cbiAgICAgICAgIyBRdWFsaXR5IG9mIHNlcnZpY2UgbGV2ZWxcbiAgICAgICAgI1xuICAgICAgICAjIDA6IGF0IG1vc3Qgb25jZVxuICAgICAgICAjIDE6IGF0IGxlYXN0IG9uY2VcbiAgICAgICAgIyAyOiBleGFjdGx5IG9uY2VcbiAgICAgICAgI1xuICAgICAgICAjIE5vdGU6IGFuIGluY3JlYXNlIG9mIHRoaXMgdmFsdWUgd2lsbCBkZWNyZWFzZSB0aGUgcGVyZm9ybWFuY2UuXG4gICAgICAgICMgRm9yIG1vcmUgaW5mb3JtYXRpb246IGh0dHBzOi8vd3d3LmhpdmVtcS5jb20vYmxvZy9tcXR0LWVzc2VudGlhbHMtcGFydC02LW1xdHQtcXVhbGl0eS1vZi1zZXJ2aWNlLWxldmVsc1xuICAgICAgICBxb3M9MFxuXG4gICAgICAgICMgQ2xlYW4gc2Vzc2lvblxuICAgICAgICAjXG4gICAgICAgICMgU2V0IHRoZSBcImNsZWFuIHNlc3Npb25cIiBmbGFnIGluIHRoZSBjb25uZWN0IG1lc3NhZ2Ugd2hlbiB0aGlzIGNsaWVudFxuICAgICAgICAjIGNvbm5lY3RzIHRvIGFuIE1RVFQgYnJva2VyLiBCeSBzZXR0aW5nIHRoaXMgZmxhZyB5b3UgYXJlIGluZGljYXRpbmdcbiAgICAgICAgIyB0aGF0IG5vIG1lc3NhZ2VzIHNhdmVkIGJ5IHRoZSBicm9rZXIgZm9yIHRoaXMgY2xpZW50IHNob3VsZCBiZSBkZWxpdmVyZWQuXG4gICAgICAgIGNsZWFuX3Nlc3Npb249ZmFsc2VcblxuICAgICAgICAjIENsaWVudCBJRFxuICAgICAgICAjXG4gICAgICAgICMgU2V0IHRoZSBjbGllbnQgaWQgdG8gYmUgdXNlZCBieSB0aGlzIGNsaWVudCB3aGVuIGNvbm5lY3RpbmcgdG8gdGhlIE1RVFRcbiAgICAgICAgIyBicm9rZXIuIEEgY2xpZW50IGlkIG11c3QgYmUgbm8gbG9uZ2VyIHRoYW4gMjMgY2hhcmFjdGVycy4gSWYgbGVmdCBibGFuayxcbiAgICAgICAgIyBhIHJhbmRvbSBpZCB3aWxsIGJlIGdlbmVyYXRlZCBieSBDaGlycFN0YWNrLlxuICAgICAgICBjbGllbnRfaWQ9XCJcIlxuXG4gICAgICAgICMgS2VlcCBhbGl2ZSBpbnRlcnZhbC5cbiAgICAgICAgI1xuICAgICAgICAjIFRoaXMgZGVmaW5lcyB0aGUgbWF4aW11bSB0aW1lIHRoYXQgdGhhdCBzaG91bGQgcGFzcyB3aXRob3V0IGNvbW11bmljYXRpb25cbiAgICAgICAgIyBiZXR3ZWVuIHRoZSBjbGllbnQgYW5kIHNlcnZlci5cbiAgICAgICAga2VlcF9hbGl2ZV9pbnRlcnZhbD1cIjMwc1wiXG5cbiAgICAgICAgIyBDQSBjZXJ0aWZpY2F0ZSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgI1xuICAgICAgICAjIFVzZSB0aGlzIHdoZW4gc2V0dGluZyB1cCBhIHNlY3VyZSBjb25uZWN0aW9uICh3aGVuIHNlcnZlciB1c2VzIHNzbDovLy4uLilcbiAgICAgICAgIyBidXQgdGhlIGNlcnRpZmljYXRlIHVzZWQgYnkgdGhlIHNlcnZlciBpcyBub3QgdHJ1c3RlZCBieSBhbnkgQ0EgY2VydGlmaWNhdGVcbiAgICAgICAgIyBvbiB0aGUgc2VydmVyIChlLmcuIHdoZW4gc2VsZiBnZW5lcmF0ZWQpLlxuICAgICAgICBjYV9jZXJ0PVwiXCJcblxuICAgICAgICAjIFRMUyBjZXJ0aWZpY2F0ZSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgdGxzX2NlcnQ9XCJcIlxuXG4gICAgICAgICMgVExTIGtleSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgdGxzX2tleT1cIlwiXG5cblxuICAgICMgR2F0ZXdheSBjaGFubmVsIGNvbmZpZ3VyYXRpb24uXG4gICAgI1xuICAgICMgTm90ZTogdGhpcyBjb25maWd1cmF0aW9uIGlzIG9ubHkgdXNlZCBpbiBjYXNlIHRoZSBnYXRld2F5IGlzIHVzaW5nIHRoZVxuICAgICMgQ2hpcnBTdGFjayBDb25jZW50cmF0b3JkIGRhZW1vbi4gSW4gYW55IG90aGVyIGNhc2UsIHRoaXMgY29uZmlndXJhdGlvbiBcbiAgICAjIGlzIGlnbm9yZWQuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkyNjQwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTI2NjAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MjY4MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkyNzAwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTI3MjAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05Mjc0MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkyNzYwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTI3ODAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MjcxMDAwMDBcbiAgICAgIGJhbmR3aWR0aD01MDAwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs4XVxuXG5cbiAgIyBSZWdpb24gc3BlY2lmaWMgbmV0d29yayBjb25maWd1cmF0aW9uLlxuICBbcmVnaW9ucy5uZXR3b3JrXVxuICAgIFxuICAgICMgSW5zdGFsbGF0aW9uIG1hcmdpbiAoZEIpIHVzZWQgYnkgdGhlIEFEUiBlbmdpbmUuXG4gICAgI1xuICAgICMgQSBoaWdoZXIgbnVtYmVyIG1lYW5zIHRoYXQgdGhlIG5ldHdvcmstc2VydmVyIHdpbGwga2VlcCBtb3JlIG1hcmdpbixcbiAgICAjIHJlc3VsdGluZyBpbiBhIGxvd2VyIGRhdGEtcmF0ZSBidXQgZGVjcmVhc2luZyB0aGUgY2hhbmNlIHRoYXQgdGhlXG4gICAgIyBkZXZpY2UgZ2V0cyBkaXNjb25uZWN0ZWQgYmVjYXVzZSBpdCBpcyB1bmFibGUgdG8gcmVhY2ggb25lIG9mIHRoZVxuICAgICMgc3Vycm91bmRlZCBnYXRld2F5cy5cbiAgICBpbnN0YWxsYXRpb25fbWFyZ2luPTEwXG5cbiAgICAjIFJYIHdpbmRvdyAoQ2xhc3MtQSkuXG4gICAgI1xuICAgICMgU2V0IHRoaXMgdG86XG4gICAgIyAwOiBSWDEgLyBSWDJcbiAgICAjIDE6IFJYMSBvbmx5XG4gICAgIyAyOiBSWDIgb25seVxuICAgIHJ4X3dpbmRvdz0wXG5cbiAgICAjIFJYMSBkZWxheSAoMSAtIDE1IHNlY29uZHMpLlxuICAgIHJ4MV9kZWxheT0xXG5cbiAgICAjIFJYMSBkYXRhLXJhdGUgb2Zmc2V0XG4gICAgcngxX2RyX29mZnNldD0wXG5cbiAgICAjIFJYMiBkYXRhLXJhdGVcbiAgICByeDJfZHI9OFxuXG4gICAgIyBSWDIgZnJlcXVlbmN5IChIeilcbiAgICByeDJfZnJlcXVlbmN5PTkyMzMwMDAwMFxuXG4gICAgIyBQcmVmZXIgUlgyIG9uIFJYMSBkYXRhLXJhdGUgbGVzcyB0aGFuLlxuICAgICNcbiAgICAjIFByZWZlciBSWDIgb3ZlciBSWDEgYmFzZWQgb24gdGhlIFJYMSBkYXRhLXJhdGUuIFdoZW4gdGhlIFJYMSBkYXRhLXJhdGVcbiAgICAjIGlzIHNtYWxsZXIgdGhhbiB0aGUgY29uZmlndXJlZCB2YWx1ZSwgdGhlbiB0aGUgTmV0d29yayBTZXJ2ZXIgd2lsbFxuICAgICMgZmlyc3QgdHJ5IHRvIHNjaGVkdWxlIHRoZSBkb3dubGluayBmb3IgUlgyLCBmYWlsaW5nIHRoYXQgKGUuZy4gdGhlIGdhdGV3YXlcbiAgICAjIGhhcyBhbHJlYWR5IGEgcGF5bG9hZCBzY2hlZHVsZWQgYXQgdGhlIFJYMiB0aW1pbmcpIGl0IHdpbGwgdHJ5IFJYMS5cbiAgICByeDJfcHJlZmVyX29uX3J4MV9kcl9sdD0wXG5cbiAgICAjIFByZWZlciBSWDIgb24gbGluayBidWRnZXQuXG4gICAgI1xuICAgICMgV2hlbiB0aGUgbGluay1idWRnZXQgaXMgYmV0dGVyIGZvciBSWDIgdGhhbiBmb3IgUlgxLCB0aGUgTmV0d29yayBTZXJ2ZXIgd2lsbCBmaXJzdFxuICAgICMgdHJ5IHRvIHNjaGVkdWxlIHRoZSBkb3dubGluayBpbiBSWDIsIGZhaWxpbmcgdGhhdCBpdCB3aWxsIHRyeSBSWDEuXG4gICAgcngyX3ByZWZlcl9vbl9saW5rX2J1ZGdldD1mYWxzZVxuXG4gICAgIyBEb3dubGluayBUWCBQb3dlciAoZEJtKVxuICAgICNcbiAgICAjIFdoZW4gc2V0IHRvIC0xLCB0aGUgZG93bmxpbmsgVFggUG93ZXIgZnJvbSB0aGUgY29uZmlndXJlZCBiYW5kIHdpbGxcbiAgICAjIGJlIHVzZWQuXG4gICAgI1xuICAgICMgUGxlYXNlIGNvbnN1bHQgdGhlIExvUmFXQU4gUmVnaW9uYWwgUGFyYW1ldGVycyBhbmQgbG9jYWwgcmVndWxhdGlvbnNcbiAgICAjIGZvciB2YWxpZCBhbmQgbGVnYWwgb3B0aW9ucy4gTm90ZSB0aGF0IHRoZSBjb25maWd1cmVkIFRYIFBvd2VyIG11c3QgYmVcbiAgICAjIHN1cHBvcnRlZCBieSB5b3VyIGdhdGV3YXkocykuXG4gICAgZG93bmxpbmtfdHhfcG93ZXI9LTFcblxuICAgICMgQURSIGlzIGRpc2FibGVkLlxuICAgIGFkcl9kaXNhYmxlZD1mYWxzZVxuXG4gICAgIyBNaW5pbXVtIGRhdGEtcmF0ZS5cbiAgICBtaW5fZHI9MFxuXG4gICAgIyBNYXhpbXVtIGRhdGEtcmF0ZS5cbiAgICBtYXhfZHI9NVxuXG4gICAgIyBFbmFibGVkIHVwbGluayBjaGFubmVscy5cbiAgICAjXG4gICAgIyBVc2UgdGhpcyB3aGVuIG9ueSBhIHN1Yi1zZXQgb2YgdGhlIGJ5IGRlZmF1bHQgZW5hYmxlZCBjaGFubmVscyBhcmUgYmVpbmdcbiAgICAjIHVzZWQuIEZvciBleGFtcGxlIHdoZW4gb25seSB1c2luZyB0aGUgZmlyc3QgOCBjaGFubmVscyBvZiB0aGUgVVMgYmFuZC5cbiAgICAjIE5vdGU6IHdoZW4gbGVmdCBibGFuayAvIGVtcHR5IGFycmF5LCBhbGwgY2hhbm5lbHMgd2lsbCBiZSBlbmFibGVkLlxuICAgIGVuYWJsZWRfdXBsaW5rX2NoYW5uZWxzPVs1NiwgNTcsIDU4LCA1OSwgNjAsIDYxLCA2MiwgNjMsIDcxXVxuXG5cbiAgICAjIFJlam9pbi1yZXF1ZXN0IGNvbmZpZ3VyYXRpb24gKExvUmFXQU4gMS4xKVxuICAgIFtyZWdpb25zLm5ldHdvcmsucmVqb2luX3JlcXVlc3RdXG5cbiAgICAgICMgUmVxdWVzdCBkZXZpY2VzIHRvIHBlcmlvZGljYWxseSBzZW5kIHJlam9pbi1yZXF1ZXN0cy5cbiAgICAgIGVuYWJsZWQ9ZmFsc2VcblxuICAgICAgIyBUaGUgZGV2aWNlIG11c3Qgc2VuZCBhIHJlam9pbi1yZXF1ZXN0IHR5cGUgMCBhdCBsZWFzdCBldmVyeSAyXihtYXhfY291bnRfbiArIDQpXG4gICAgICAjIHVwbGluayBtZXNzYWdlcy4gVmFsaWQgdmFsdWVzIGFyZSAwIHRvIDE1LlxuICAgICAgbWF4X2NvdW50X249MFxuXG4gICAgICAjIFRoZSBkZXZpY2UgbXVzdCBzZW5kIGEgcmVqb2luLXJlcXVlc3QgdHlwZSAwIGF0IGxlYXN0IGV2ZXJ5IDJeKG1heF90aW1lX24gKyAxMClcbiAgICAgICMgc2Vjb25kcy4gVmFsaWQgdmFsdWVzIGFyZSAwIHRvIDE1LlxuICAgICAgI1xuICAgICAgIyAwICA9IHJvdWdobHkgMTcgbWludXRlc1xuICAgICAgIyAxNSA9IGFib3V0IDEgeWVhclxuICAgICAgbWF4X3RpbWVfbj0wXG4gICAgXG5cbiAgICAjIENsYXNzLUIgY29uZmlndXJhdGlvbi5cbiAgICBbcmVnaW9ucy5uZXR3b3JrLmNsYXNzX2JdXG5cbiAgICAgICMgUGluZy1zbG90IGRhdGEtcmF0ZS4gXG4gICAgICBwaW5nX3Nsb3RfZHI9OFxuXG4gICAgICAjIFBpbmctc2xvdCBmcmVxdWVuY3kgKEh6KVxuICAgICAgI1xuICAgICAgIyBzZXQgdGhpcyB0byAwIHRvIHVzZSB0aGUgZGVmYXVsdCBmcmVxdWVuY3kgcGxhbiBmb3IgdGhlIGNvbmZpZ3VyZWQgcmVnaW9uXG4gICAgICAjICh3aGljaCBjb3VsZCBiZSBmcmVxdWVuY3kgaG9wcGluZykuXG4gICAgICBwaW5nX3Nsb3RfZnJlcXVlbmN5PTBcblwiXCJcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuc2VydmljZU5hbWUgPSBcImNoaXJwc3RhY2tcIlxuZmlsZVBhdGggPSBcIi9jaGlycHN0YWNrL3JlZ2lvbl9jbjQ3MF8wLnRvbWxcIlxuY29udGVudCA9IFwiXCJcIlxuIyBUaGlzIGZpbGUgY29udGFpbnMgYW4gZXhhbXBsZSBDTjQ3MCBleGFtcGxlIChjaGFubmVscyAwLTcpLlxuW1tyZWdpb25zXV1cblxuICAjIElEIGlzIGFuIHVzZS1kZWZpbmVkIGlkZW50aWZpZXIgZm9yIHRoaXMgcmVnaW9uLlxuICBpZD1cImNuNDcwXzBcIlxuXG4gICMgRGVzY3JpcHRpb24gaXMgYSBzaG9ydCBkZXNjcmlwdGlvbiBmb3IgdGhpcyByZWdpb24uXG4gIGRlc2NyaXB0aW9uPVwiQ040NzAgKGNoYW5uZWxzIDAtNylcIlxuXG4gICMgQ29tbW9uLW5hbWUgcmVmZXJzIHRvIHRoZSBjb21tb24tbmFtZSBvZiB0aGlzIHJlZ2lvbiBhcyBkZWZpbmVkIGJ5XG4gICMgdGhlIExvUmEgQWxsaWFuY2UuXG4gIGNvbW1vbl9uYW1lPVwiQ040NzBcIlxuXG5cbiAgIyBHYXRld2F5IGNvbmZpZ3VyYXRpb24uXG4gIFtyZWdpb25zLmdhdGV3YXldXG5cbiAgICAjIEZvcmNlIGdhdGV3YXlzIGFzIHByaXZhdGUuXG4gICAgI1xuICAgICMgSWYgZW5hYmxlZCwgZ2F0ZXdheXMgY2FuIG9ubHkgYmUgdXNlZCBieSBkZXZpY2VzIHVuZGVyIHRoZSBzYW1lIHRlbmFudC5cbiAgICBmb3JjZV9nd3NfcHJpdmF0ZT1mYWxzZVxuXG4gICAgXG4gICAgIyBHYXRld2F5IGJhY2tlbmQgY29uZmlndXJhdGlvbi5cbiAgICBbcmVnaW9ucy5nYXRld2F5LmJhY2tlbmRdXG5cbiAgICAgICMgVGhlIGVuYWJsZWQgYmFja2VuZCB0eXBlLlxuICAgICAgZW5hYmxlZD1cIm1xdHRcIlxuXG4gICAgICAjIE1RVFQgY29uZmlndXJhdGlvbi5cbiAgICAgIFtyZWdpb25zLmdhdGV3YXkuYmFja2VuZC5tcXR0XVxuXG4gICAgICAgICMgVG9waWMgcHJlZml4LlxuICAgICAgICAjXG4gICAgICAgICMgVGhlIHRvcGljIHByZWZpeCBjYW4gYmUgdXNlZCB0byBkZWZpbmUgdGhlIHJlZ2lvbiBvZiB0aGUgZ2F0ZXdheS5cbiAgICAgICAgIyBOb3RlLCB0aGVyZSBpcyBubyBuZWVkIHRvIGFkZCBhIHRyYWlsaW5nICcvJyB0byB0aGUgcHJlZml4LiBUaGUgdHJhaWxpbmdcbiAgICAgICAgIyAnLycgaXMgYXV0b21hdGljYWxseSBhZGRlZCB0byB0aGUgcHJlZml4IGlmIGl0IGlzIGNvbmZpZ3VyZWQuXG4gICAgICAgIHRvcGljX3ByZWZpeD1cImNuNDcwXzBcIlxuXG4gICAgICAgICMgTVFUVCBzZXJ2ZXIgKGUuZy4gc2NoZW1lOi8vaG9zdDpwb3J0IHdoZXJlIHNjaGVtZSBpcyB0Y3AsIHNzbCBvciB3cylcbiAgICAgICAgc2VydmVyPVwidGNwOi8vbW9zcXVpdHRvOjE4ODNcIlxuXG4gICAgICAgICMgQ29ubmVjdCB3aXRoIHRoZSBnaXZlbiB1c2VybmFtZSAob3B0aW9uYWwpXG4gICAgICAgIHVzZXJuYW1lPVwiXCJcblxuICAgICAgICAjIENvbm5lY3Qgd2l0aCB0aGUgZ2l2ZW4gcGFzc3dvcmQgKG9wdGlvbmFsKVxuICAgICAgICBwYXNzd29yZD1cIlwiXG5cbiAgICAgICAgIyBRdWFsaXR5IG9mIHNlcnZpY2UgbGV2ZWxcbiAgICAgICAgI1xuICAgICAgICAjIDA6IGF0IG1vc3Qgb25jZVxuICAgICAgICAjIDE6IGF0IGxlYXN0IG9uY2VcbiAgICAgICAgIyAyOiBleGFjdGx5IG9uY2VcbiAgICAgICAgI1xuICAgICAgICAjIE5vdGU6IGFuIGluY3JlYXNlIG9mIHRoaXMgdmFsdWUgd2lsbCBkZWNyZWFzZSB0aGUgcGVyZm9ybWFuY2UuXG4gICAgICAgICMgRm9yIG1vcmUgaW5mb3JtYXRpb246IGh0dHBzOi8vd3d3LmhpdmVtcS5jb20vYmxvZy9tcXR0LWVzc2VudGlhbHMtcGFydC02LW1xdHQtcXVhbGl0eS1vZi1zZXJ2aWNlLWxldmVsc1xuICAgICAgICBxb3M9MFxuXG4gICAgICAgICMgQ2xlYW4gc2Vzc2lvblxuICAgICAgICAjXG4gICAgICAgICMgU2V0IHRoZSBcImNsZWFuIHNlc3Npb25cIiBmbGFnIGluIHRoZSBjb25uZWN0IG1lc3NhZ2Ugd2hlbiB0aGlzIGNsaWVudFxuICAgICAgICAjIGNvbm5lY3RzIHRvIGFuIE1RVFQgYnJva2VyLiBCeSBzZXR0aW5nIHRoaXMgZmxhZyB5b3UgYXJlIGluZGljYXRpbmdcbiAgICAgICAgIyB0aGF0IG5vIG1lc3NhZ2VzIHNhdmVkIGJ5IHRoZSBicm9rZXIgZm9yIHRoaXMgY2xpZW50IHNob3VsZCBiZSBkZWxpdmVyZWQuXG4gICAgICAgIGNsZWFuX3Nlc3Npb249ZmFsc2VcblxuICAgICAgICAjIENsaWVudCBJRFxuICAgICAgICAjXG4gICAgICAgICMgU2V0IHRoZSBjbGllbnQgaWQgdG8gYmUgdXNlZCBieSB0aGlzIGNsaWVudCB3aGVuIGNvbm5lY3RpbmcgdG8gdGhlIE1RVFRcbiAgICAgICAgIyBicm9rZXIuIEEgY2xpZW50IGlkIG11c3QgYmUgbm8gbG9uZ2VyIHRoYW4gMjMgY2hhcmFjdGVycy4gSWYgbGVmdCBibGFuayxcbiAgICAgICAgIyBhIHJhbmRvbSBpZCB3aWxsIGJlIGdlbmVyYXRlZCBieSBDaGlycFN0YWNrLlxuICAgICAgICBjbGllbnRfaWQ9XCJcIlxuXG4gICAgICAgICMgS2VlcCBhbGl2ZSBpbnRlcnZhbC5cbiAgICAgICAgI1xuICAgICAgICAjIFRoaXMgZGVmaW5lcyB0aGUgbWF4aW11bSB0aW1lIHRoYXQgdGhhdCBzaG91bGQgcGFzcyB3aXRob3V0IGNvbW11bmljYXRpb25cbiAgICAgICAgIyBiZXR3ZWVuIHRoZSBjbGllbnQgYW5kIHNlcnZlci5cbiAgICAgICAga2VlcF9hbGl2ZV9pbnRlcnZhbD1cIjMwc1wiXG5cbiAgICAgICAgIyBDQSBjZXJ0aWZpY2F0ZSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgI1xuICAgICAgICAjIFVzZSB0aGlzIHdoZW4gc2V0dGluZyB1cCBhIHNlY3VyZSBjb25uZWN0aW9uICh3aGVuIHNlcnZlciB1c2VzIHNzbDovLy4uLilcbiAgICAgICAgIyBidXQgdGhlIGNlcnRpZmljYXRlIHVzZWQgYnkgdGhlIHNlcnZlciBpcyBub3QgdHJ1c3RlZCBieSBhbnkgQ0EgY2VydGlmaWNhdGVcbiAgICAgICAgIyBvbiB0aGUgc2VydmVyIChlLmcuIHdoZW4gc2VsZiBnZW5lcmF0ZWQpLlxuICAgICAgICBjYV9jZXJ0PVwiXCJcblxuICAgICAgICAjIFRMUyBjZXJ0aWZpY2F0ZSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgdGxzX2NlcnQ9XCJcIlxuXG4gICAgICAgICMgVExTIGtleSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgdGxzX2tleT1cIlwiXG5cblxuICAgICMgR2F0ZXdheSBjaGFubmVsIGNvbmZpZ3VyYXRpb24uXG4gICAgI1xuICAgICMgTm90ZTogdGhpcyBjb25maWd1cmF0aW9uIGlzIG9ubHkgdXNlZCBpbiBjYXNlIHRoZSBnYXRld2F5IGlzIHVzaW5nIHRoZVxuICAgICMgQ2hpcnBTdGFjayBDb25jZW50cmF0b3JkIGRhZW1vbi4gSW4gYW55IG90aGVyIGNhc2UsIHRoaXMgY29uZmlndXJhdGlvbiBcbiAgICAjIGlzIGlnbm9yZWQuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTQ3MDMwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9NDcwNTAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT00NzA3MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTQ3MDkwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9NDcxMTAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT00NzEzMDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTQ3MTUwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9NDcxNzAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuXG4gICMgUmVnaW9uIHNwZWNpZmljIG5ldHdvcmsgY29uZmlndXJhdGlvbi5cbiAgW3JlZ2lvbnMubmV0d29ya11cbiAgICBcbiAgICAjIEluc3RhbGxhdGlvbiBtYXJnaW4gKGRCKSB1c2VkIGJ5IHRoZSBBRFIgZW5naW5lLlxuICAgICNcbiAgICAjIEEgaGlnaGVyIG51bWJlciBtZWFucyB0aGF0IHRoZSBuZXR3b3JrLXNlcnZlciB3aWxsIGtlZXAgbW9yZSBtYXJnaW4sXG4gICAgIyByZXN1bHRpbmcgaW4gYSBsb3dlciBkYXRhLXJhdGUgYnV0IGRlY3JlYXNpbmcgdGhlIGNoYW5jZSB0aGF0IHRoZVxuICAgICMgZGV2aWNlIGdldHMgZGlzY29ubmVjdGVkIGJlY2F1c2UgaXQgaXMgdW5hYmxlIHRvIHJlYWNoIG9uZSBvZiB0aGVcbiAgICAjIHN1cnJvdW5kZWQgZ2F0ZXdheXMuXG4gICAgaW5zdGFsbGF0aW9uX21hcmdpbj0xMFxuXG4gICAgIyBSWCB3aW5kb3cgKENsYXNzLUEpLlxuICAgICNcbiAgICAjIFNldCB0aGlzIHRvOlxuICAgICMgMDogUlgxIC8gUlgyXG4gICAgIyAxOiBSWDEgb25seVxuICAgICMgMjogUlgyIG9ubHlcbiAgICByeF93aW5kb3c9MFxuXG4gICAgIyBSWDEgZGVsYXkgKDEgLSAxNSBzZWNvbmRzKS5cbiAgICByeDFfZGVsYXk9MVxuXG4gICAgIyBSWDEgZGF0YS1yYXRlIG9mZnNldFxuICAgIHJ4MV9kcl9vZmZzZXQ9MFxuXG4gICAgIyBSWDIgZGF0YS1yYXRlXG4gICAgcngyX2RyPTBcblxuICAgICMgUlgyIGZyZXF1ZW5jeSAoSHopXG4gICAgcngyX2ZyZXF1ZW5jeT01MDUzMDAwMDBcblxuICAgICMgUHJlZmVyIFJYMiBvbiBSWDEgZGF0YS1yYXRlIGxlc3MgdGhhbi5cbiAgICAjXG4gICAgIyBQcmVmZXIgUlgyIG92ZXIgUlgxIGJhc2VkIG9uIHRoZSBSWDEgZGF0YS1yYXRlLiBXaGVuIHRoZSBSWDEgZGF0YS1yYXRlXG4gICAgIyBpcyBzbWFsbGVyIHRoYW4gdGhlIGNvbmZpZ3VyZWQgdmFsdWUsIHRoZW4gdGhlIE5ldHdvcmsgU2VydmVyIHdpbGxcbiAgICAjIGZpcnN0IHRyeSB0byBzY2hlZHVsZSB0aGUgZG93bmxpbmsgZm9yIFJYMiwgZmFpbGluZyB0aGF0IChlLmcuIHRoZSBnYXRld2F5XG4gICAgIyBoYXMgYWxyZWFkeSBhIHBheWxvYWQgc2NoZWR1bGVkIGF0IHRoZSBSWDIgdGltaW5nKSBpdCB3aWxsIHRyeSBSWDEuXG4gICAgcngyX3ByZWZlcl9vbl9yeDFfZHJfbHQ9MFxuXG4gICAgIyBQcmVmZXIgUlgyIG9uIGxpbmsgYnVkZ2V0LlxuICAgICNcbiAgICAjIFdoZW4gdGhlIGxpbmstYnVkZ2V0IGlzIGJldHRlciBmb3IgUlgyIHRoYW4gZm9yIFJYMSwgdGhlIE5ldHdvcmsgU2VydmVyIHdpbGwgZmlyc3RcbiAgICAjIHRyeSB0byBzY2hlZHVsZSB0aGUgZG93bmxpbmsgaW4gUlgyLCBmYWlsaW5nIHRoYXQgaXQgd2lsbCB0cnkgUlgxLlxuICAgIHJ4Ml9wcmVmZXJfb25fbGlua19idWRnZXQ9ZmFsc2VcblxuICAgICMgRG93bmxpbmsgVFggUG93ZXIgKGRCbSlcbiAgICAjXG4gICAgIyBXaGVuIHNldCB0byAtMSwgdGhlIGRvd25saW5rIFRYIFBvd2VyIGZyb20gdGhlIGNvbmZpZ3VyZWQgYmFuZCB3aWxsXG4gICAgIyBiZSB1c2VkLlxuICAgICNcbiAgICAjIFBsZWFzZSBjb25zdWx0IHRoZSBMb1JhV0FOIFJlZ2lvbmFsIFBhcmFtZXRlcnMgYW5kIGxvY2FsIHJlZ3VsYXRpb25zXG4gICAgIyBmb3IgdmFsaWQgYW5kIGxlZ2FsIG9wdGlvbnMuIE5vdGUgdGhhdCB0aGUgY29uZmlndXJlZCBUWCBQb3dlciBtdXN0IGJlXG4gICAgIyBzdXBwb3J0ZWQgYnkgeW91ciBnYXRld2F5KHMpLlxuICAgIGRvd25saW5rX3R4X3Bvd2VyPS0xXG5cbiAgICAjIEFEUiBpcyBkaXNhYmxlZC5cbiAgICBhZHJfZGlzYWJsZWQ9ZmFsc2VcblxuICAgICMgTWluaW11bSBkYXRhLXJhdGUuXG4gICAgbWluX2RyPTBcblxuICAgICMgTWF4aW11bSBkYXRhLXJhdGUuXG4gICAgbWF4X2RyPTVcblxuICAgICMgRW5hYmxlZCB1cGxpbmsgY2hhbm5lbHMuXG4gICAgI1xuICAgICMgVXNlIHRoaXMgd2hlbiBvbnkgYSBzdWItc2V0IG9mIHRoZSBieSBkZWZhdWx0IGVuYWJsZWQgY2hhbm5lbHMgYXJlIGJlaW5nXG4gICAgIyB1c2VkLiBGb3IgZXhhbXBsZSB3aGVuIG9ubHkgdXNpbmcgdGhlIGZpcnN0IDggY2hhbm5lbHMgb2YgdGhlIFVTIGJhbmQuXG4gICAgIyBOb3RlOiB3aGVuIGxlZnQgYmxhbmsgLyBlbXB0eSBhcnJheSwgYWxsIGNoYW5uZWxzIHdpbGwgYmUgZW5hYmxlZC5cbiAgICBlbmFibGVkX3VwbGlua19jaGFubmVscz1bMCwgMSwgMiwgMywgNCwgNSwgNiwgN11cblxuXG4gICAgIyBSZWpvaW4tcmVxdWVzdCBjb25maWd1cmF0aW9uIChMb1JhV0FOIDEuMSlcbiAgICBbcmVnaW9ucy5uZXR3b3JrLnJlam9pbl9yZXF1ZXN0XVxuXG4gICAgICAjIFJlcXVlc3QgZGV2aWNlcyB0byBwZXJpb2RpY2FsbHkgc2VuZCByZWpvaW4tcmVxdWVzdHMuXG4gICAgICBlbmFibGVkPWZhbHNlXG5cbiAgICAgICMgVGhlIGRldmljZSBtdXN0IHNlbmQgYSByZWpvaW4tcmVxdWVzdCB0eXBlIDAgYXQgbGVhc3QgZXZlcnkgMl4obWF4X2NvdW50X24gKyA0KVxuICAgICAgIyB1cGxpbmsgbWVzc2FnZXMuIFZhbGlkIHZhbHVlcyBhcmUgMCB0byAxNS5cbiAgICAgIG1heF9jb3VudF9uPTBcblxuICAgICAgIyBUaGUgZGV2aWNlIG11c3Qgc2VuZCBhIHJlam9pbi1yZXF1ZXN0IHR5cGUgMCBhdCBsZWFzdCBldmVyeSAyXihtYXhfdGltZV9uICsgMTApXG4gICAgICAjIHNlY29uZHMuIFZhbGlkIHZhbHVlcyBhcmUgMCB0byAxNS5cbiAgICAgICNcbiAgICAgICMgMCAgPSByb3VnaGx5IDE3IG1pbnV0ZXNcbiAgICAgICMgMTUgPSBhYm91dCAxIHllYXJcbiAgICAgIG1heF90aW1lX249MFxuICAgIFxuXG4gICAgIyBDbGFzcy1CIGNvbmZpZ3VyYXRpb24uXG4gICAgW3JlZ2lvbnMubmV0d29yay5jbGFzc19iXVxuXG4gICAgICAjIFBpbmctc2xvdCBkYXRhLXJhdGUuIFxuICAgICAgcGluZ19zbG90X2RyPTJcblxuICAgICAgIyBQaW5nLXNsb3QgZnJlcXVlbmN5IChIeilcbiAgICAgICNcbiAgICAgICMgc2V0IHRoaXMgdG8gMCB0byB1c2UgdGhlIGRlZmF1bHQgZnJlcXVlbmN5IHBsYW4gZm9yIHRoZSBjb25maWd1cmVkIHJlZ2lvblxuICAgICAgIyAod2hpY2ggY291bGQgYmUgZnJlcXVlbmN5IGhvcHBpbmcpLlxuICAgICAgcGluZ19zbG90X2ZyZXF1ZW5jeT0wXG5cIlwiXCJcblxuW1tjb25maWcubW91bnRzXV1cbnNlcnZpY2VOYW1lID0gXCJjaGlycHN0YWNrXCJcbmZpbGVQYXRoID0gXCIvY2hpcnBzdGFjay9yZWdpb25fY240NzBfMTAudG9tbFwiXG5jb250ZW50ID0gXCJcIlwiXG4jIFRoaXMgZmlsZSBjb250YWlucyBhbiBleGFtcGxlIENONDcwIGV4YW1wbGUgKGNoYW5uZWxzIDgwLTg3KS5cbltbcmVnaW9uc11dXG5cbiAgIyBJRCBpcyBhbiB1c2UtZGVmaW5lZCBpZGVudGlmaWVyIGZvciB0aGlzIHJlZ2lvbi5cbiAgaWQ9XCJjbjQ3MF8xMFwiXG5cbiAgIyBEZXNjcmlwdGlvbiBpcyBhIHNob3J0IGRlc2NyaXB0aW9uIGZvciB0aGlzIHJlZ2lvbi5cbiAgZGVzY3JpcHRpb249XCJDTjQ3MCAoY2hhbm5lbHMgODAtODcpXCJcblxuICAjIENvbW1vbi1uYW1lIHJlZmVycyB0byB0aGUgY29tbW9uLW5hbWUgb2YgdGhpcyByZWdpb24gYXMgZGVmaW5lZCBieVxuICAjIHRoZSBMb1JhIEFsbGlhbmNlLlxuICBjb21tb25fbmFtZT1cIkNONDcwXCJcblxuXG4gICMgR2F0ZXdheSBjb25maWd1cmF0aW9uLlxuICBbcmVnaW9ucy5nYXRld2F5XVxuXG4gICAgIyBGb3JjZSBnYXRld2F5cyBhcyBwcml2YXRlLlxuICAgICNcbiAgICAjIElmIGVuYWJsZWQsIGdhdGV3YXlzIGNhbiBvbmx5IGJlIHVzZWQgYnkgZGV2aWNlcyB1bmRlciB0aGUgc2FtZSB0ZW5hbnQuXG4gICAgZm9yY2VfZ3dzX3ByaXZhdGU9ZmFsc2VcblxuICAgIFxuICAgICMgR2F0ZXdheSBiYWNrZW5kIGNvbmZpZ3VyYXRpb24uXG4gICAgW3JlZ2lvbnMuZ2F0ZXdheS5iYWNrZW5kXVxuXG4gICAgICAjIFRoZSBlbmFibGVkIGJhY2tlbmQgdHlwZS5cbiAgICAgIGVuYWJsZWQ9XCJtcXR0XCJcblxuICAgICAgIyBNUVRUIGNvbmZpZ3VyYXRpb24uXG4gICAgICBbcmVnaW9ucy5nYXRld2F5LmJhY2tlbmQubXF0dF1cblxuICAgICAgICAjIFRvcGljIHByZWZpeC5cbiAgICAgICAgI1xuICAgICAgICAjIFRoZSB0b3BpYyBwcmVmaXggY2FuIGJlIHVzZWQgdG8gZGVmaW5lIHRoZSByZWdpb24gb2YgdGhlIGdhdGV3YXkuXG4gICAgICAgICMgTm90ZSwgdGhlcmUgaXMgbm8gbmVlZCB0byBhZGQgYSB0cmFpbGluZyAnLycgdG8gdGhlIHByZWZpeC4gVGhlIHRyYWlsaW5nXG4gICAgICAgICMgJy8nIGlzIGF1dG9tYXRpY2FsbHkgYWRkZWQgdG8gdGhlIHByZWZpeCBpZiBpdCBpcyBjb25maWd1cmVkLlxuICAgICAgICB0b3BpY19wcmVmaXg9XCJjbjQ3MF8xMFwiXG5cbiAgICAgICAgIyBNUVRUIHNlcnZlciAoZS5nLiBzY2hlbWU6Ly9ob3N0OnBvcnQgd2hlcmUgc2NoZW1lIGlzIHRjcCwgc3NsIG9yIHdzKVxuICAgICAgICBzZXJ2ZXI9XCJ0Y3A6Ly9tb3NxdWl0dG86MTg4M1wiXG5cbiAgICAgICAgIyBDb25uZWN0IHdpdGggdGhlIGdpdmVuIHVzZXJuYW1lIChvcHRpb25hbClcbiAgICAgICAgdXNlcm5hbWU9XCJcIlxuXG4gICAgICAgICMgQ29ubmVjdCB3aXRoIHRoZSBnaXZlbiBwYXNzd29yZCAob3B0aW9uYWwpXG4gICAgICAgIHBhc3N3b3JkPVwiXCJcblxuICAgICAgICAjIFF1YWxpdHkgb2Ygc2VydmljZSBsZXZlbFxuICAgICAgICAjXG4gICAgICAgICMgMDogYXQgbW9zdCBvbmNlXG4gICAgICAgICMgMTogYXQgbGVhc3Qgb25jZVxuICAgICAgICAjIDI6IGV4YWN0bHkgb25jZVxuICAgICAgICAjXG4gICAgICAgICMgTm90ZTogYW4gaW5jcmVhc2Ugb2YgdGhpcyB2YWx1ZSB3aWxsIGRlY3JlYXNlIHRoZSBwZXJmb3JtYW5jZS5cbiAgICAgICAgIyBGb3IgbW9yZSBpbmZvcm1hdGlvbjogaHR0cHM6Ly93d3cuaGl2ZW1xLmNvbS9ibG9nL21xdHQtZXNzZW50aWFscy1wYXJ0LTYtbXF0dC1xdWFsaXR5LW9mLXNlcnZpY2UtbGV2ZWxzXG4gICAgICAgIHFvcz0wXG5cbiAgICAgICAgIyBDbGVhbiBzZXNzaW9uXG4gICAgICAgICNcbiAgICAgICAgIyBTZXQgdGhlIFwiY2xlYW4gc2Vzc2lvblwiIGZsYWcgaW4gdGhlIGNvbm5lY3QgbWVzc2FnZSB3aGVuIHRoaXMgY2xpZW50XG4gICAgICAgICMgY29ubmVjdHMgdG8gYW4gTVFUVCBicm9rZXIuIEJ5IHNldHRpbmcgdGhpcyBmbGFnIHlvdSBhcmUgaW5kaWNhdGluZ1xuICAgICAgICAjIHRoYXQgbm8gbWVzc2FnZXMgc2F2ZWQgYnkgdGhlIGJyb2tlciBmb3IgdGhpcyBjbGllbnQgc2hvdWxkIGJlIGRlbGl2ZXJlZC5cbiAgICAgICAgY2xlYW5fc2Vzc2lvbj1mYWxzZVxuXG4gICAgICAgICMgQ2xpZW50IElEXG4gICAgICAgICNcbiAgICAgICAgIyBTZXQgdGhlIGNsaWVudCBpZCB0byBiZSB1c2VkIGJ5IHRoaXMgY2xpZW50IHdoZW4gY29ubmVjdGluZyB0byB0aGUgTVFUVFxuICAgICAgICAjIGJyb2tlci4gQSBjbGllbnQgaWQgbXVzdCBiZSBubyBsb25nZXIgdGhhbiAyMyBjaGFyYWN0ZXJzLiBJZiBsZWZ0IGJsYW5rLFxuICAgICAgICAjIGEgcmFuZG9tIGlkIHdpbGwgYmUgZ2VuZXJhdGVkIGJ5IENoaXJwU3RhY2suXG4gICAgICAgIGNsaWVudF9pZD1cIlwiXG5cbiAgICAgICAgIyBLZWVwIGFsaXZlIGludGVydmFsLlxuICAgICAgICAjXG4gICAgICAgICMgVGhpcyBkZWZpbmVzIHRoZSBtYXhpbXVtIHRpbWUgdGhhdCB0aGF0IHNob3VsZCBwYXNzIHdpdGhvdXQgY29tbXVuaWNhdGlvblxuICAgICAgICAjIGJldHdlZW4gdGhlIGNsaWVudCBhbmQgc2VydmVyLlxuICAgICAgICBrZWVwX2FsaXZlX2ludGVydmFsPVwiMzBzXCJcblxuICAgICAgICAjIENBIGNlcnRpZmljYXRlIGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICAjXG4gICAgICAgICMgVXNlIHRoaXMgd2hlbiBzZXR0aW5nIHVwIGEgc2VjdXJlIGNvbm5lY3Rpb24gKHdoZW4gc2VydmVyIHVzZXMgc3NsOi8vLi4uKVxuICAgICAgICAjIGJ1dCB0aGUgY2VydGlmaWNhdGUgdXNlZCBieSB0aGUgc2VydmVyIGlzIG5vdCB0cnVzdGVkIGJ5IGFueSBDQSBjZXJ0aWZpY2F0ZVxuICAgICAgICAjIG9uIHRoZSBzZXJ2ZXIgKGUuZy4gd2hlbiBzZWxmIGdlbmVyYXRlZCkuXG4gICAgICAgIGNhX2NlcnQ9XCJcIlxuXG4gICAgICAgICMgVExTIGNlcnRpZmljYXRlIGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICB0bHNfY2VydD1cIlwiXG5cbiAgICAgICAgIyBUTFMga2V5IGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICB0bHNfa2V5PVwiXCJcblxuXG4gICAgIyBHYXRld2F5IGNoYW5uZWwgY29uZmlndXJhdGlvbi5cbiAgICAjXG4gICAgIyBOb3RlOiB0aGlzIGNvbmZpZ3VyYXRpb24gaXMgb25seSB1c2VkIGluIGNhc2UgdGhlIGdhdGV3YXkgaXMgdXNpbmcgdGhlXG4gICAgIyBDaGlycFN0YWNrIENvbmNlbnRyYXRvcmQgZGFlbW9uLiBJbiBhbnkgb3RoZXIgY2FzZSwgdGhpcyBjb25maWd1cmF0aW9uIFxuICAgICMgaXMgaWdub3JlZC5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9NDg2MzAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT00ODY1MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTQ4NjcwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9NDg2OTAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT00ODcxMDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTQ4NzMwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9NDg3NTAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT00ODc3MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG5cbiAgIyBSZWdpb24gc3BlY2lmaWMgbmV0d29yayBjb25maWd1cmF0aW9uLlxuICBbcmVnaW9ucy5uZXR3b3JrXVxuICAgIFxuICAgICMgSW5zdGFsbGF0aW9uIG1hcmdpbiAoZEIpIHVzZWQgYnkgdGhlIEFEUiBlbmdpbmUuXG4gICAgI1xuICAgICMgQSBoaWdoZXIgbnVtYmVyIG1lYW5zIHRoYXQgdGhlIG5ldHdvcmstc2VydmVyIHdpbGwga2VlcCBtb3JlIG1hcmdpbixcbiAgICAjIHJlc3VsdGluZyBpbiBhIGxvd2VyIGRhdGEtcmF0ZSBidXQgZGVjcmVhc2luZyB0aGUgY2hhbmNlIHRoYXQgdGhlXG4gICAgIyBkZXZpY2UgZ2V0cyBkaXNjb25uZWN0ZWQgYmVjYXVzZSBpdCBpcyB1bmFibGUgdG8gcmVhY2ggb25lIG9mIHRoZVxuICAgICMgc3Vycm91bmRlZCBnYXRld2F5cy5cbiAgICBpbnN0YWxsYXRpb25fbWFyZ2luPTEwXG5cbiAgICAjIFJYIHdpbmRvdyAoQ2xhc3MtQSkuXG4gICAgI1xuICAgICMgU2V0IHRoaXMgdG86XG4gICAgIyAwOiBSWDEgLyBSWDJcbiAgICAjIDE6IFJYMSBvbmx5XG4gICAgIyAyOiBSWDIgb25seVxuICAgIHJ4X3dpbmRvdz0wXG5cbiAgICAjIFJYMSBkZWxheSAoMSAtIDE1IHNlY29uZHMpLlxuICAgIHJ4MV9kZWxheT0xXG5cbiAgICAjIFJYMSBkYXRhLXJhdGUgb2Zmc2V0XG4gICAgcngxX2RyX29mZnNldD0wXG5cbiAgICAjIFJYMiBkYXRhLXJhdGVcbiAgICByeDJfZHI9MFxuXG4gICAgIyBSWDIgZnJlcXVlbmN5IChIeilcbiAgICByeDJfZnJlcXVlbmN5PTUwNTMwMDAwMFxuXG4gICAgIyBQcmVmZXIgUlgyIG9uIFJYMSBkYXRhLXJhdGUgbGVzcyB0aGFuLlxuICAgICNcbiAgICAjIFByZWZlciBSWDIgb3ZlciBSWDEgYmFzZWQgb24gdGhlIFJYMSBkYXRhLXJhdGUuIFdoZW4gdGhlIFJYMSBkYXRhLXJhdGVcbiAgICAjIGlzIHNtYWxsZXIgdGhhbiB0aGUgY29uZmlndXJlZCB2YWx1ZSwgdGhlbiB0aGUgTmV0d29yayBTZXJ2ZXIgd2lsbFxuICAgICMgZmlyc3QgdHJ5IHRvIHNjaGVkdWxlIHRoZSBkb3dubGluayBmb3IgUlgyLCBmYWlsaW5nIHRoYXQgKGUuZy4gdGhlIGdhdGV3YXlcbiAgICAjIGhhcyBhbHJlYWR5IGEgcGF5bG9hZCBzY2hlZHVsZWQgYXQgdGhlIFJYMiB0aW1pbmcpIGl0IHdpbGwgdHJ5IFJYMS5cbiAgICByeDJfcHJlZmVyX29uX3J4MV9kcl9sdD0wXG5cbiAgICAjIFByZWZlciBSWDIgb24gbGluayBidWRnZXQuXG4gICAgI1xuICAgICMgV2hlbiB0aGUgbGluay1idWRnZXQgaXMgYmV0dGVyIGZvciBSWDIgdGhhbiBmb3IgUlgxLCB0aGUgTmV0d29yayBTZXJ2ZXIgd2lsbCBmaXJzdFxuICAgICMgdHJ5IHRvIHNjaGVkdWxlIHRoZSBkb3dubGluayBpbiBSWDIsIGZhaWxpbmcgdGhhdCBpdCB3aWxsIHRyeSBSWDEuXG4gICAgcngyX3ByZWZlcl9vbl9saW5rX2J1ZGdldD1mYWxzZVxuXG4gICAgIyBEb3dubGluayBUWCBQb3dlciAoZEJtKVxuICAgICNcbiAgICAjIFdoZW4gc2V0IHRvIC0xLCB0aGUgZG93bmxpbmsgVFggUG93ZXIgZnJvbSB0aGUgY29uZmlndXJlZCBiYW5kIHdpbGxcbiAgICAjIGJlIHVzZWQuXG4gICAgI1xuICAgICMgUGxlYXNlIGNvbnN1bHQgdGhlIExvUmFXQU4gUmVnaW9uYWwgUGFyYW1ldGVycyBhbmQgbG9jYWwgcmVndWxhdGlvbnNcbiAgICAjIGZvciB2YWxpZCBhbmQgbGVnYWwgb3B0aW9ucy4gTm90ZSB0aGF0IHRoZSBjb25maWd1cmVkIFRYIFBvd2VyIG11c3QgYmVcbiAgICAjIHN1cHBvcnRlZCBieSB5b3VyIGdhdGV3YXkocykuXG4gICAgZG93bmxpbmtfdHhfcG93ZXI9LTFcblxuICAgICMgQURSIGlzIGRpc2FibGVkLlxuICAgIGFkcl9kaXNhYmxlZD1mYWxzZVxuXG4gICAgIyBNaW5pbXVtIGRhdGEtcmF0ZS5cbiAgICBtaW5fZHI9MFxuXG4gICAgIyBNYXhpbXVtIGRhdGEtcmF0ZS5cbiAgICBtYXhfZHI9NVxuXG4gICAgIyBFbmFibGVkIHVwbGluayBjaGFubmVscy5cbiAgICAjXG4gICAgIyBVc2UgdGhpcyB3aGVuIG9ueSBhIHN1Yi1zZXQgb2YgdGhlIGJ5IGRlZmF1bHQgZW5hYmxlZCBjaGFubmVscyBhcmUgYmVpbmdcbiAgICAjIHVzZWQuIEZvciBleGFtcGxlIHdoZW4gb25seSB1c2luZyB0aGUgZmlyc3QgOCBjaGFubmVscyBvZiB0aGUgVVMgYmFuZC5cbiAgICAjIE5vdGU6IHdoZW4gbGVmdCBibGFuayAvIGVtcHR5IGFycmF5LCBhbGwgY2hhbm5lbHMgd2lsbCBiZSBlbmFibGVkLlxuICAgIGVuYWJsZWRfdXBsaW5rX2NoYW5uZWxzPVs4MCwgODEsIDgyLCA4MywgODQsIDg1LCA4NiwgODddXG5cblxuICAgICMgUmVqb2luLXJlcXVlc3QgY29uZmlndXJhdGlvbiAoTG9SYVdBTiAxLjEpXG4gICAgW3JlZ2lvbnMubmV0d29yay5yZWpvaW5fcmVxdWVzdF1cblxuICAgICAgIyBSZXF1ZXN0IGRldmljZXMgdG8gcGVyaW9kaWNhbGx5IHNlbmQgcmVqb2luLXJlcXVlc3RzLlxuICAgICAgZW5hYmxlZD1mYWxzZVxuXG4gICAgICAjIFRoZSBkZXZpY2UgbXVzdCBzZW5kIGEgcmVqb2luLXJlcXVlc3QgdHlwZSAwIGF0IGxlYXN0IGV2ZXJ5IDJeKG1heF9jb3VudF9uICsgNClcbiAgICAgICMgdXBsaW5rIG1lc3NhZ2VzLiBWYWxpZCB2YWx1ZXMgYXJlIDAgdG8gMTUuXG4gICAgICBtYXhfY291bnRfbj0wXG5cbiAgICAgICMgVGhlIGRldmljZSBtdXN0IHNlbmQgYSByZWpvaW4tcmVxdWVzdCB0eXBlIDAgYXQgbGVhc3QgZXZlcnkgMl4obWF4X3RpbWVfbiArIDEwKVxuICAgICAgIyBzZWNvbmRzLiBWYWxpZCB2YWx1ZXMgYXJlIDAgdG8gMTUuXG4gICAgICAjXG4gICAgICAjIDAgID0gcm91Z2hseSAxNyBtaW51dGVzXG4gICAgICAjIDE1ID0gYWJvdXQgMSB5ZWFyXG4gICAgICBtYXhfdGltZV9uPTBcbiAgICBcblxuICAgICMgQ2xhc3MtQiBjb25maWd1cmF0aW9uLlxuICAgIFtyZWdpb25zLm5ldHdvcmsuY2xhc3NfYl1cblxuICAgICAgIyBQaW5nLXNsb3QgZGF0YS1yYXRlLiBcbiAgICAgIHBpbmdfc2xvdF9kcj0yXG5cbiAgICAgICMgUGluZy1zbG90IGZyZXF1ZW5jeSAoSHopXG4gICAgICAjXG4gICAgICAjIHNldCB0aGlzIHRvIDAgdG8gdXNlIHRoZSBkZWZhdWx0IGZyZXF1ZW5jeSBwbGFuIGZvciB0aGUgY29uZmlndXJlZCByZWdpb25cbiAgICAgICMgKHdoaWNoIGNvdWxkIGJlIGZyZXF1ZW5jeSBob3BwaW5nKS5cbiAgICAgIHBpbmdfc2xvdF9mcmVxdWVuY3k9MFxuXCJcIlwiXG5cbltbY29uZmlnLm1vdW50c11dXG5zZXJ2aWNlTmFtZSA9IFwiY2hpcnBzdGFja1wiXG5maWxlUGF0aCA9IFwiL2NoaXJwc3RhY2svcmVnaW9uX2NuNDcwXzExLnRvbWxcIlxuY29udGVudCA9IFwiXCJcIlxuIyBUaGlzIGZpbGUgY29udGFpbnMgYW4gZXhhbXBsZSBDTjQ3MCBleGFtcGxlIChjaGFubmVscyA4OC05NSkuXG5bW3JlZ2lvbnNdXVxuXG4gICMgSUQgaXMgYW4gdXNlLWRlZmluZWQgaWRlbnRpZmllciBmb3IgdGhpcyByZWdpb24uXG4gIGlkPVwiY240NzBfMTFcIlxuXG4gICMgRGVzY3JpcHRpb24gaXMgYSBzaG9ydCBkZXNjcmlwdGlvbiBmb3IgdGhpcyByZWdpb24uXG4gIGRlc2NyaXB0aW9uPVwiQ040NzAgKGNoYW5uZWxzIDg4LTk1KVwiXG5cbiAgIyBDb21tb24tbmFtZSByZWZlcnMgdG8gdGhlIGNvbW1vbi1uYW1lIG9mIHRoaXMgcmVnaW9uIGFzIGRlZmluZWQgYnlcbiAgIyB0aGUgTG9SYSBBbGxpYW5jZS5cbiAgY29tbW9uX25hbWU9XCJDTjQ3MFwiXG5cblxuICAjIEdhdGV3YXkgY29uZmlndXJhdGlvbi5cbiAgW3JlZ2lvbnMuZ2F0ZXdheV1cblxuICAgICMgRm9yY2UgZ2F0ZXdheXMgYXMgcHJpdmF0ZS5cbiAgICAjXG4gICAgIyBJZiBlbmFibGVkLCBnYXRld2F5cyBjYW4gb25seSBiZSB1c2VkIGJ5IGRldmljZXMgdW5kZXIgdGhlIHNhbWUgdGVuYW50LlxuICAgIGZvcmNlX2d3c19wcml2YXRlPWZhbHNlXG5cbiAgICBcbiAgICAjIEdhdGV3YXkgYmFja2VuZCBjb25maWd1cmF0aW9uLlxuICAgIFtyZWdpb25zLmdhdGV3YXkuYmFja2VuZF1cblxuICAgICAgIyBUaGUgZW5hYmxlZCBiYWNrZW5kIHR5cGUuXG4gICAgICBlbmFibGVkPVwibXF0dFwiXG5cbiAgICAgICMgTVFUVCBjb25maWd1cmF0aW9uLlxuICAgICAgW3JlZ2lvbnMuZ2F0ZXdheS5iYWNrZW5kLm1xdHRdXG5cbiAgICAgICAgIyBUb3BpYyBwcmVmaXguXG4gICAgICAgICNcbiAgICAgICAgIyBUaGUgdG9waWMgcHJlZml4IGNhbiBiZSB1c2VkIHRvIGRlZmluZSB0aGUgcmVnaW9uIG9mIHRoZSBnYXRld2F5LlxuICAgICAgICAjIE5vdGUsIHRoZXJlIGlzIG5vIG5lZWQgdG8gYWRkIGEgdHJhaWxpbmcgJy8nIHRvIHRoZSBwcmVmaXguIFRoZSB0cmFpbGluZ1xuICAgICAgICAjICcvJyBpcyBhdXRvbWF0aWNhbGx5IGFkZGVkIHRvIHRoZSBwcmVmaXggaWYgaXQgaXMgY29uZmlndXJlZC5cbiAgICAgICAgdG9waWNfcHJlZml4PVwiY240NzBfMTFcIlxuXG4gICAgICAgICMgTVFUVCBzZXJ2ZXIgKGUuZy4gc2NoZW1lOi8vaG9zdDpwb3J0IHdoZXJlIHNjaGVtZSBpcyB0Y3AsIHNzbCBvciB3cylcbiAgICAgICAgc2VydmVyPVwidGNwOi8vbW9zcXVpdHRvOjE4ODNcIlxuXG4gICAgICAgICMgQ29ubmVjdCB3aXRoIHRoZSBnaXZlbiB1c2VybmFtZSAob3B0aW9uYWwpXG4gICAgICAgIHVzZXJuYW1lPVwiXCJcblxuICAgICAgICAjIENvbm5lY3Qgd2l0aCB0aGUgZ2l2ZW4gcGFzc3dvcmQgKG9wdGlvbmFsKVxuICAgICAgICBwYXNzd29yZD1cIlwiXG5cbiAgICAgICAgIyBRdWFsaXR5IG9mIHNlcnZpY2UgbGV2ZWxcbiAgICAgICAgI1xuICAgICAgICAjIDA6IGF0IG1vc3Qgb25jZVxuICAgICAgICAjIDE6IGF0IGxlYXN0IG9uY2VcbiAgICAgICAgIyAyOiBleGFjdGx5IG9uY2VcbiAgICAgICAgI1xuICAgICAgICAjIE5vdGU6IGFuIGluY3JlYXNlIG9mIHRoaXMgdmFsdWUgd2lsbCBkZWNyZWFzZSB0aGUgcGVyZm9ybWFuY2UuXG4gICAgICAgICMgRm9yIG1vcmUgaW5mb3JtYXRpb246IGh0dHBzOi8vd3d3LmhpdmVtcS5jb20vYmxvZy9tcXR0LWVzc2VudGlhbHMtcGFydC02LW1xdHQtcXVhbGl0eS1vZi1zZXJ2aWNlLWxldmVsc1xuICAgICAgICBxb3M9MFxuXG4gICAgICAgICMgQ2xlYW4gc2Vzc2lvblxuICAgICAgICAjXG4gICAgICAgICMgU2V0IHRoZSBcImNsZWFuIHNlc3Npb25cIiBmbGFnIGluIHRoZSBjb25uZWN0IG1lc3NhZ2Ugd2hlbiB0aGlzIGNsaWVudFxuICAgICAgICAjIGNvbm5lY3RzIHRvIGFuIE1RVFQgYnJva2VyLiBCeSBzZXR0aW5nIHRoaXMgZmxhZyB5b3UgYXJlIGluZGljYXRpbmdcbiAgICAgICAgIyB0aGF0IG5vIG1lc3NhZ2VzIHNhdmVkIGJ5IHRoZSBicm9rZXIgZm9yIHRoaXMgY2xpZW50IHNob3VsZCBiZSBkZWxpdmVyZWQuXG4gICAgICAgIGNsZWFuX3Nlc3Npb249ZmFsc2VcblxuICAgICAgICAjIENsaWVudCBJRFxuICAgICAgICAjXG4gICAgICAgICMgU2V0IHRoZSBjbGllbnQgaWQgdG8gYmUgdXNlZCBieSB0aGlzIGNsaWVudCB3aGVuIGNvbm5lY3RpbmcgdG8gdGhlIE1RVFRcbiAgICAgICAgIyBicm9rZXIuIEEgY2xpZW50IGlkIG11c3QgYmUgbm8gbG9uZ2VyIHRoYW4gMjMgY2hhcmFjdGVycy4gSWYgbGVmdCBibGFuayxcbiAgICAgICAgIyBhIHJhbmRvbSBpZCB3aWxsIGJlIGdlbmVyYXRlZCBieSBDaGlycFN0YWNrLlxuICAgICAgICBjbGllbnRfaWQ9XCJcIlxuXG4gICAgICAgICMgS2VlcCBhbGl2ZSBpbnRlcnZhbC5cbiAgICAgICAgI1xuICAgICAgICAjIFRoaXMgZGVmaW5lcyB0aGUgbWF4aW11bSB0aW1lIHRoYXQgdGhhdCBzaG91bGQgcGFzcyB3aXRob3V0IGNvbW11bmljYXRpb25cbiAgICAgICAgIyBiZXR3ZWVuIHRoZSBjbGllbnQgYW5kIHNlcnZlci5cbiAgICAgICAga2VlcF9hbGl2ZV9pbnRlcnZhbD1cIjMwc1wiXG5cbiAgICAgICAgIyBDQSBjZXJ0aWZpY2F0ZSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgI1xuICAgICAgICAjIFVzZSB0aGlzIHdoZW4gc2V0dGluZyB1cCBhIHNlY3VyZSBjb25uZWN0aW9uICh3aGVuIHNlcnZlciB1c2VzIHNzbDovLy4uLilcbiAgICAgICAgIyBidXQgdGhlIGNlcnRpZmljYXRlIHVzZWQgYnkgdGhlIHNlcnZlciBpcyBub3QgdHJ1c3RlZCBieSBhbnkgQ0EgY2VydGlmaWNhdGVcbiAgICAgICAgIyBvbiB0aGUgc2VydmVyIChlLmcuIHdoZW4gc2VsZiBnZW5lcmF0ZWQpLlxuICAgICAgICBjYV9jZXJ0PVwiXCJcblxuICAgICAgICAjIFRMUyBjZXJ0aWZpY2F0ZSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgdGxzX2NlcnQ9XCJcIlxuXG4gICAgICAgICMgVExTIGtleSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgdGxzX2tleT1cIlwiXG5cblxuICAgICMgR2F0ZXdheSBjaGFubmVsIGNvbmZpZ3VyYXRpb24uXG4gICAgI1xuICAgICMgTm90ZTogdGhpcyBjb25maWd1cmF0aW9uIGlzIG9ubHkgdXNlZCBpbiBjYXNlIHRoZSBnYXRld2F5IGlzIHVzaW5nIHRoZVxuICAgICMgQ2hpcnBTdGFjayBDb25jZW50cmF0b3JkIGRhZW1vbi4gSW4gYW55IG90aGVyIGNhc2UsIHRoaXMgY29uZmlndXJhdGlvbiBcbiAgICAjIGlzIGlnbm9yZWQuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTQ4NzkwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9NDg4MTAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT00ODgzMDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTQ4ODUwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9NDg4NzAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT00ODg5MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTQ4OTEwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9NDg5MzAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuXG4gICMgUmVnaW9uIHNwZWNpZmljIG5ldHdvcmsgY29uZmlndXJhdGlvbi5cbiAgW3JlZ2lvbnMubmV0d29ya11cbiAgICBcbiAgICAjIEluc3RhbGxhdGlvbiBtYXJnaW4gKGRCKSB1c2VkIGJ5IHRoZSBBRFIgZW5naW5lLlxuICAgICNcbiAgICAjIEEgaGlnaGVyIG51bWJlciBtZWFucyB0aGF0IHRoZSBuZXR3b3JrLXNlcnZlciB3aWxsIGtlZXAgbW9yZSBtYXJnaW4sXG4gICAgIyByZXN1bHRpbmcgaW4gYSBsb3dlciBkYXRhLXJhdGUgYnV0IGRlY3JlYXNpbmcgdGhlIGNoYW5jZSB0aGF0IHRoZVxuICAgICMgZGV2aWNlIGdldHMgZGlzY29ubmVjdGVkIGJlY2F1c2UgaXQgaXMgdW5hYmxlIHRvIHJlYWNoIG9uZSBvZiB0aGVcbiAgICAjIHN1cnJvdW5kZWQgZ2F0ZXdheXMuXG4gICAgaW5zdGFsbGF0aW9uX21hcmdpbj0xMFxuXG4gICAgIyBSWCB3aW5kb3cgKENsYXNzLUEpLlxuICAgICNcbiAgICAjIFNldCB0aGlzIHRvOlxuICAgICMgMDogUlgxIC8gUlgyXG4gICAgIyAxOiBSWDEgb25seVxuICAgICMgMjogUlgyIG9ubHlcbiAgICByeF93aW5kb3c9MFxuXG4gICAgIyBSWDEgZGVsYXkgKDEgLSAxNSBzZWNvbmRzKS5cbiAgICByeDFfZGVsYXk9MVxuXG4gICAgIyBSWDEgZGF0YS1yYXRlIG9mZnNldFxuICAgIHJ4MV9kcl9vZmZzZXQ9MFxuXG4gICAgIyBSWDIgZGF0YS1yYXRlXG4gICAgcngyX2RyPTBcblxuICAgICMgUlgyIGZyZXF1ZW5jeSAoSHopXG4gICAgcngyX2ZyZXF1ZW5jeT01MDUzMDAwMDBcblxuICAgICMgUHJlZmVyIFJYMiBvbiBSWDEgZGF0YS1yYXRlIGxlc3MgdGhhbi5cbiAgICAjXG4gICAgIyBQcmVmZXIgUlgyIG92ZXIgUlgxIGJhc2VkIG9uIHRoZSBSWDEgZGF0YS1yYXRlLiBXaGVuIHRoZSBSWDEgZGF0YS1yYXRlXG4gICAgIyBpcyBzbWFsbGVyIHRoYW4gdGhlIGNvbmZpZ3VyZWQgdmFsdWUsIHRoZW4gdGhlIE5ldHdvcmsgU2VydmVyIHdpbGxcbiAgICAjIGZpcnN0IHRyeSB0byBzY2hlZHVsZSB0aGUgZG93bmxpbmsgZm9yIFJYMiwgZmFpbGluZyB0aGF0IChlLmcuIHRoZSBnYXRld2F5XG4gICAgIyBoYXMgYWxyZWFkeSBhIHBheWxvYWQgc2NoZWR1bGVkIGF0IHRoZSBSWDIgdGltaW5nKSBpdCB3aWxsIHRyeSBSWDEuXG4gICAgcngyX3ByZWZlcl9vbl9yeDFfZHJfbHQ9MFxuXG4gICAgIyBQcmVmZXIgUlgyIG9uIGxpbmsgYnVkZ2V0LlxuICAgICNcbiAgICAjIFdoZW4gdGhlIGxpbmstYnVkZ2V0IGlzIGJldHRlciBmb3IgUlgyIHRoYW4gZm9yIFJYMSwgdGhlIE5ldHdvcmsgU2VydmVyIHdpbGwgZmlyc3RcbiAgICAjIHRyeSB0byBzY2hlZHVsZSB0aGUgZG93bmxpbmsgaW4gUlgyLCBmYWlsaW5nIHRoYXQgaXQgd2lsbCB0cnkgUlgxLlxuICAgIHJ4Ml9wcmVmZXJfb25fbGlua19idWRnZXQ9ZmFsc2VcblxuICAgICMgRG93bmxpbmsgVFggUG93ZXIgKGRCbSlcbiAgICAjXG4gICAgIyBXaGVuIHNldCB0byAtMSwgdGhlIGRvd25saW5rIFRYIFBvd2VyIGZyb20gdGhlIGNvbmZpZ3VyZWQgYmFuZCB3aWxsXG4gICAgIyBiZSB1c2VkLlxuICAgICNcbiAgICAjIFBsZWFzZSBjb25zdWx0IHRoZSBMb1JhV0FOIFJlZ2lvbmFsIFBhcmFtZXRlcnMgYW5kIGxvY2FsIHJlZ3VsYXRpb25zXG4gICAgIyBmb3IgdmFsaWQgYW5kIGxlZ2FsIG9wdGlvbnMuIE5vdGUgdGhhdCB0aGUgY29uZmlndXJlZCBUWCBQb3dlciBtdXN0IGJlXG4gICAgIyBzdXBwb3J0ZWQgYnkgeW91ciBnYXRld2F5KHMpLlxuICAgIGRvd25saW5rX3R4X3Bvd2VyPS0xXG5cbiAgICAjIEFEUiBpcyBkaXNhYmxlZC5cbiAgICBhZHJfZGlzYWJsZWQ9ZmFsc2VcblxuICAgICMgTWluaW11bSBkYXRhLXJhdGUuXG4gICAgbWluX2RyPTBcblxuICAgICMgTWF4aW11bSBkYXRhLXJhdGUuXG4gICAgbWF4X2RyPTVcblxuICAgICMgRW5hYmxlZCB1cGxpbmsgY2hhbm5lbHMuXG4gICAgI1xuICAgICMgVXNlIHRoaXMgd2hlbiBvbnkgYSBzdWItc2V0IG9mIHRoZSBieSBkZWZhdWx0IGVuYWJsZWQgY2hhbm5lbHMgYXJlIGJlaW5nXG4gICAgIyB1c2VkLiBGb3IgZXhhbXBsZSB3aGVuIG9ubHkgdXNpbmcgdGhlIGZpcnN0IDggY2hhbm5lbHMgb2YgdGhlIFVTIGJhbmQuXG4gICAgIyBOb3RlOiB3aGVuIGxlZnQgYmxhbmsgLyBlbXB0eSBhcnJheSwgYWxsIGNoYW5uZWxzIHdpbGwgYmUgZW5hYmxlZC5cbiAgICBlbmFibGVkX3VwbGlua19jaGFubmVscz1bODgsIDg5LCA5MCwgOTEsIDkyLCA5MywgOTQsIDk1XVxuXG5cbiAgICAjIFJlam9pbi1yZXF1ZXN0IGNvbmZpZ3VyYXRpb24gKExvUmFXQU4gMS4xKVxuICAgIFtyZWdpb25zLm5ldHdvcmsucmVqb2luX3JlcXVlc3RdXG5cbiAgICAgICMgUmVxdWVzdCBkZXZpY2VzIHRvIHBlcmlvZGljYWxseSBzZW5kIHJlam9pbi1yZXF1ZXN0cy5cbiAgICAgIGVuYWJsZWQ9ZmFsc2VcblxuICAgICAgIyBUaGUgZGV2aWNlIG11c3Qgc2VuZCBhIHJlam9pbi1yZXF1ZXN0IHR5cGUgMCBhdCBsZWFzdCBldmVyeSAyXihtYXhfY291bnRfbiArIDQpXG4gICAgICAjIHVwbGluayBtZXNzYWdlcy4gVmFsaWQgdmFsdWVzIGFyZSAwIHRvIDE1LlxuICAgICAgbWF4X2NvdW50X249MFxuXG4gICAgICAjIFRoZSBkZXZpY2UgbXVzdCBzZW5kIGEgcmVqb2luLXJlcXVlc3QgdHlwZSAwIGF0IGxlYXN0IGV2ZXJ5IDJeKG1heF90aW1lX24gKyAxMClcbiAgICAgICMgc2Vjb25kcy4gVmFsaWQgdmFsdWVzIGFyZSAwIHRvIDE1LlxuICAgICAgI1xuICAgICAgIyAwICA9IHJvdWdobHkgMTcgbWludXRlc1xuICAgICAgIyAxNSA9IGFib3V0IDEgeWVhclxuICAgICAgbWF4X3RpbWVfbj0wXG4gICAgXG5cbiAgICAjIENsYXNzLUIgY29uZmlndXJhdGlvbi5cbiAgICBbcmVnaW9ucy5uZXR3b3JrLmNsYXNzX2JdXG5cbiAgICAgICMgUGluZy1zbG90IGRhdGEtcmF0ZS4gXG4gICAgICBwaW5nX3Nsb3RfZHI9MlxuXG4gICAgICAjIFBpbmctc2xvdCBmcmVxdWVuY3kgKEh6KVxuICAgICAgI1xuICAgICAgIyBzZXQgdGhpcyB0byAwIHRvIHVzZSB0aGUgZGVmYXVsdCBmcmVxdWVuY3kgcGxhbiBmb3IgdGhlIGNvbmZpZ3VyZWQgcmVnaW9uXG4gICAgICAjICh3aGljaCBjb3VsZCBiZSBmcmVxdWVuY3kgaG9wcGluZykuXG4gICAgICBwaW5nX3Nsb3RfZnJlcXVlbmN5PTBcblwiXCJcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuc2VydmljZU5hbWUgPSBcImNoaXJwc3RhY2tcIlxuZmlsZVBhdGggPSBcIi9jaGlycHN0YWNrL3JlZ2lvbl9jbjQ3MF8xLnRvbWxcIlxuY29udGVudCA9IFwiXCJcIlxuIyBUaGlzIGZpbGUgY29udGFpbnMgYW4gZXhhbXBsZSBDTjQ3MCBleGFtcGxlIChjaGFubmVscyA4LTE1KS5cbltbcmVnaW9uc11dXG5cbiAgIyBJRCBpcyBhbiB1c2UtZGVmaW5lZCBpZGVudGlmaWVyIGZvciB0aGlzIHJlZ2lvbi5cbiAgaWQ9XCJjbjQ3MF8xXCJcblxuICAjIERlc2NyaXB0aW9uIGlzIGEgc2hvcnQgZGVzY3JpcHRpb24gZm9yIHRoaXMgcmVnaW9uLlxuICBkZXNjcmlwdGlvbj1cIkNONDcwIChjaGFubmVscyA4LTE1KVwiXG5cbiAgIyBDb21tb24tbmFtZSByZWZlcnMgdG8gdGhlIGNvbW1vbi1uYW1lIG9mIHRoaXMgcmVnaW9uIGFzIGRlZmluZWQgYnlcbiAgIyB0aGUgTG9SYSBBbGxpYW5jZS5cbiAgY29tbW9uX25hbWU9XCJDTjQ3MFwiXG5cblxuICAjIEdhdGV3YXkgY29uZmlndXJhdGlvbi5cbiAgW3JlZ2lvbnMuZ2F0ZXdheV1cblxuICAgICMgRm9yY2UgZ2F0ZXdheXMgYXMgcHJpdmF0ZS5cbiAgICAjXG4gICAgIyBJZiBlbmFibGVkLCBnYXRld2F5cyBjYW4gb25seSBiZSB1c2VkIGJ5IGRldmljZXMgdW5kZXIgdGhlIHNhbWUgdGVuYW50LlxuICAgIGZvcmNlX2d3c19wcml2YXRlPWZhbHNlXG5cbiAgICBcbiAgICAjIEdhdGV3YXkgYmFja2VuZCBjb25maWd1cmF0aW9uLlxuICAgIFtyZWdpb25zLmdhdGV3YXkuYmFja2VuZF1cblxuICAgICAgIyBUaGUgZW5hYmxlZCBiYWNrZW5kIHR5cGUuXG4gICAgICBlbmFibGVkPVwibXF0dFwiXG5cbiAgICAgICMgTVFUVCBjb25maWd1cmF0aW9uLlxuICAgICAgW3JlZ2lvbnMuZ2F0ZXdheS5iYWNrZW5kLm1xdHRdXG5cbiAgICAgICAgIyBUb3BpYyBwcmVmaXguXG4gICAgICAgICNcbiAgICAgICAgIyBUaGUgdG9waWMgcHJlZml4IGNhbiBiZSB1c2VkIHRvIGRlZmluZSB0aGUgcmVnaW9uIG9mIHRoZSBnYXRld2F5LlxuICAgICAgICAjIE5vdGUsIHRoZXJlIGlzIG5vIG5lZWQgdG8gYWRkIGEgdHJhaWxpbmcgJy8nIHRvIHRoZSBwcmVmaXguIFRoZSB0cmFpbGluZ1xuICAgICAgICAjICcvJyBpcyBhdXRvbWF0aWNhbGx5IGFkZGVkIHRvIHRoZSBwcmVmaXggaWYgaXQgaXMgY29uZmlndXJlZC5cbiAgICAgICAgdG9waWNfcHJlZml4PVwiY240NzBfMVwiXG5cbiAgICAgICAgIyBNUVRUIHNlcnZlciAoZS5nLiBzY2hlbWU6Ly9ob3N0OnBvcnQgd2hlcmUgc2NoZW1lIGlzIHRjcCwgc3NsIG9yIHdzKVxuICAgICAgICBzZXJ2ZXI9XCJ0Y3A6Ly9tb3NxdWl0dG86MTg4M1wiXG5cbiAgICAgICAgIyBDb25uZWN0IHdpdGggdGhlIGdpdmVuIHVzZXJuYW1lIChvcHRpb25hbClcbiAgICAgICAgdXNlcm5hbWU9XCJcIlxuXG4gICAgICAgICMgQ29ubmVjdCB3aXRoIHRoZSBnaXZlbiBwYXNzd29yZCAob3B0aW9uYWwpXG4gICAgICAgIHBhc3N3b3JkPVwiXCJcblxuICAgICAgICAjIFF1YWxpdHkgb2Ygc2VydmljZSBsZXZlbFxuICAgICAgICAjXG4gICAgICAgICMgMDogYXQgbW9zdCBvbmNlXG4gICAgICAgICMgMTogYXQgbGVhc3Qgb25jZVxuICAgICAgICAjIDI6IGV4YWN0bHkgb25jZVxuICAgICAgICAjXG4gICAgICAgICMgTm90ZTogYW4gaW5jcmVhc2Ugb2YgdGhpcyB2YWx1ZSB3aWxsIGRlY3JlYXNlIHRoZSBwZXJmb3JtYW5jZS5cbiAgICAgICAgIyBGb3IgbW9yZSBpbmZvcm1hdGlvbjogaHR0cHM6Ly93d3cuaGl2ZW1xLmNvbS9ibG9nL21xdHQtZXNzZW50aWFscy1wYXJ0LTYtbXF0dC1xdWFsaXR5LW9mLXNlcnZpY2UtbGV2ZWxzXG4gICAgICAgIHFvcz0wXG5cbiAgICAgICAgIyBDbGVhbiBzZXNzaW9uXG4gICAgICAgICNcbiAgICAgICAgIyBTZXQgdGhlIFwiY2xlYW4gc2Vzc2lvblwiIGZsYWcgaW4gdGhlIGNvbm5lY3QgbWVzc2FnZSB3aGVuIHRoaXMgY2xpZW50XG4gICAgICAgICMgY29ubmVjdHMgdG8gYW4gTVFUVCBicm9rZXIuIEJ5IHNldHRpbmcgdGhpcyBmbGFnIHlvdSBhcmUgaW5kaWNhdGluZ1xuICAgICAgICAjIHRoYXQgbm8gbWVzc2FnZXMgc2F2ZWQgYnkgdGhlIGJyb2tlciBmb3IgdGhpcyBjbGllbnQgc2hvdWxkIGJlIGRlbGl2ZXJlZC5cbiAgICAgICAgY2xlYW5fc2Vzc2lvbj1mYWxzZVxuXG4gICAgICAgICMgQ2xpZW50IElEXG4gICAgICAgICNcbiAgICAgICAgIyBTZXQgdGhlIGNsaWVudCBpZCB0byBiZSB1c2VkIGJ5IHRoaXMgY2xpZW50IHdoZW4gY29ubmVjdGluZyB0byB0aGUgTVFUVFxuICAgICAgICAjIGJyb2tlci4gQSBjbGllbnQgaWQgbXVzdCBiZSBubyBsb25nZXIgdGhhbiAyMyBjaGFyYWN0ZXJzLiBJZiBsZWZ0IGJsYW5rLFxuICAgICAgICAjIGEgcmFuZG9tIGlkIHdpbGwgYmUgZ2VuZXJhdGVkIGJ5IENoaXJwU3RhY2suXG4gICAgICAgIGNsaWVudF9pZD1cIlwiXG5cbiAgICAgICAgIyBLZWVwIGFsaXZlIGludGVydmFsLlxuICAgICAgICAjXG4gICAgICAgICMgVGhpcyBkZWZpbmVzIHRoZSBtYXhpbXVtIHRpbWUgdGhhdCB0aGF0IHNob3VsZCBwYXNzIHdpdGhvdXQgY29tbXVuaWNhdGlvblxuICAgICAgICAjIGJldHdlZW4gdGhlIGNsaWVudCBhbmQgc2VydmVyLlxuICAgICAgICBrZWVwX2FsaXZlX2ludGVydmFsPVwiMzBzXCJcblxuICAgICAgICAjIENBIGNlcnRpZmljYXRlIGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICAjXG4gICAgICAgICMgVXNlIHRoaXMgd2hlbiBzZXR0aW5nIHVwIGEgc2VjdXJlIGNvbm5lY3Rpb24gKHdoZW4gc2VydmVyIHVzZXMgc3NsOi8vLi4uKVxuICAgICAgICAjIGJ1dCB0aGUgY2VydGlmaWNhdGUgdXNlZCBieSB0aGUgc2VydmVyIGlzIG5vdCB0cnVzdGVkIGJ5IGFueSBDQSBjZXJ0aWZpY2F0ZVxuICAgICAgICAjIG9uIHRoZSBzZXJ2ZXIgKGUuZy4gd2hlbiBzZWxmIGdlbmVyYXRlZCkuXG4gICAgICAgIGNhX2NlcnQ9XCJcIlxuXG4gICAgICAgICMgVExTIGNlcnRpZmljYXRlIGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICB0bHNfY2VydD1cIlwiXG5cbiAgICAgICAgIyBUTFMga2V5IGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICB0bHNfa2V5PVwiXCJcblxuXG4gICAgIyBHYXRld2F5IGNoYW5uZWwgY29uZmlndXJhdGlvbi5cbiAgICAjXG4gICAgIyBOb3RlOiB0aGlzIGNvbmZpZ3VyYXRpb24gaXMgb25seSB1c2VkIGluIGNhc2UgdGhlIGdhdGV3YXkgaXMgdXNpbmcgdGhlXG4gICAgIyBDaGlycFN0YWNrIENvbmNlbnRyYXRvcmQgZGFlbW9uLiBJbiBhbnkgb3RoZXIgY2FzZSwgdGhpcyBjb25maWd1cmF0aW9uIFxuICAgICMgaXMgaWdub3JlZC5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9NDcxOTAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT00NzIxMDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTQ3MjMwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9NDcyNTAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT00NzI3MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTQ3MjkwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9NDczMTAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT00NzMzMDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG5cbiAgIyBSZWdpb24gc3BlY2lmaWMgbmV0d29yayBjb25maWd1cmF0aW9uLlxuICBbcmVnaW9ucy5uZXR3b3JrXVxuICAgIFxuICAgICMgSW5zdGFsbGF0aW9uIG1hcmdpbiAoZEIpIHVzZWQgYnkgdGhlIEFEUiBlbmdpbmUuXG4gICAgI1xuICAgICMgQSBoaWdoZXIgbnVtYmVyIG1lYW5zIHRoYXQgdGhlIG5ldHdvcmstc2VydmVyIHdpbGwga2VlcCBtb3JlIG1hcmdpbixcbiAgICAjIHJlc3VsdGluZyBpbiBhIGxvd2VyIGRhdGEtcmF0ZSBidXQgZGVjcmVhc2luZyB0aGUgY2hhbmNlIHRoYXQgdGhlXG4gICAgIyBkZXZpY2UgZ2V0cyBkaXNjb25uZWN0ZWQgYmVjYXVzZSBpdCBpcyB1bmFibGUgdG8gcmVhY2ggb25lIG9mIHRoZVxuICAgICMgc3Vycm91bmRlZCBnYXRld2F5cy5cbiAgICBpbnN0YWxsYXRpb25fbWFyZ2luPTEwXG5cbiAgICAjIFJYIHdpbmRvdyAoQ2xhc3MtQSkuXG4gICAgI1xuICAgICMgU2V0IHRoaXMgdG86XG4gICAgIyAwOiBSWDEgLyBSWDJcbiAgICAjIDE6IFJYMSBvbmx5XG4gICAgIyAyOiBSWDIgb25seVxuICAgIHJ4X3dpbmRvdz0wXG5cbiAgICAjIFJYMSBkZWxheSAoMSAtIDE1IHNlY29uZHMpLlxuICAgIHJ4MV9kZWxheT0xXG5cbiAgICAjIFJYMSBkYXRhLXJhdGUgb2Zmc2V0XG4gICAgcngxX2RyX29mZnNldD0wXG5cbiAgICAjIFJYMiBkYXRhLXJhdGVcbiAgICByeDJfZHI9MFxuXG4gICAgIyBSWDIgZnJlcXVlbmN5IChIeilcbiAgICByeDJfZnJlcXVlbmN5PTUwNTMwMDAwMFxuXG4gICAgIyBQcmVmZXIgUlgyIG9uIFJYMSBkYXRhLXJhdGUgbGVzcyB0aGFuLlxuICAgICNcbiAgICAjIFByZWZlciBSWDIgb3ZlciBSWDEgYmFzZWQgb24gdGhlIFJYMSBkYXRhLXJhdGUuIFdoZW4gdGhlIFJYMSBkYXRhLXJhdGVcbiAgICAjIGlzIHNtYWxsZXIgdGhhbiB0aGUgY29uZmlndXJlZCB2YWx1ZSwgdGhlbiB0aGUgTmV0d29yayBTZXJ2ZXIgd2lsbFxuICAgICMgZmlyc3QgdHJ5IHRvIHNjaGVkdWxlIHRoZSBkb3dubGluayBmb3IgUlgyLCBmYWlsaW5nIHRoYXQgKGUuZy4gdGhlIGdhdGV3YXlcbiAgICAjIGhhcyBhbHJlYWR5IGEgcGF5bG9hZCBzY2hlZHVsZWQgYXQgdGhlIFJYMiB0aW1pbmcpIGl0IHdpbGwgdHJ5IFJYMS5cbiAgICByeDJfcHJlZmVyX29uX3J4MV9kcl9sdD0wXG5cbiAgICAjIFByZWZlciBSWDIgb24gbGluayBidWRnZXQuXG4gICAgI1xuICAgICMgV2hlbiB0aGUgbGluay1idWRnZXQgaXMgYmV0dGVyIGZvciBSWDIgdGhhbiBmb3IgUlgxLCB0aGUgTmV0d29yayBTZXJ2ZXIgd2lsbCBmaXJzdFxuICAgICMgdHJ5IHRvIHNjaGVkdWxlIHRoZSBkb3dubGluayBpbiBSWDIsIGZhaWxpbmcgdGhhdCBpdCB3aWxsIHRyeSBSWDEuXG4gICAgcngyX3ByZWZlcl9vbl9saW5rX2J1ZGdldD1mYWxzZVxuXG4gICAgIyBEb3dubGluayBUWCBQb3dlciAoZEJtKVxuICAgICNcbiAgICAjIFdoZW4gc2V0IHRvIC0xLCB0aGUgZG93bmxpbmsgVFggUG93ZXIgZnJvbSB0aGUgY29uZmlndXJlZCBiYW5kIHdpbGxcbiAgICAjIGJlIHVzZWQuXG4gICAgI1xuICAgICMgUGxlYXNlIGNvbnN1bHQgdGhlIExvUmFXQU4gUmVnaW9uYWwgUGFyYW1ldGVycyBhbmQgbG9jYWwgcmVndWxhdGlvbnNcbiAgICAjIGZvciB2YWxpZCBhbmQgbGVnYWwgb3B0aW9ucy4gTm90ZSB0aGF0IHRoZSBjb25maWd1cmVkIFRYIFBvd2VyIG11c3QgYmVcbiAgICAjIHN1cHBvcnRlZCBieSB5b3VyIGdhdGV3YXkocykuXG4gICAgZG93bmxpbmtfdHhfcG93ZXI9LTFcblxuICAgICMgQURSIGlzIGRpc2FibGVkLlxuICAgIGFkcl9kaXNhYmxlZD1mYWxzZVxuXG4gICAgIyBNaW5pbXVtIGRhdGEtcmF0ZS5cbiAgICBtaW5fZHI9MFxuXG4gICAgIyBNYXhpbXVtIGRhdGEtcmF0ZS5cbiAgICBtYXhfZHI9NVxuXG4gICAgIyBFbmFibGVkIHVwbGluayBjaGFubmVscy5cbiAgICAjXG4gICAgIyBVc2UgdGhpcyB3aGVuIG9ueSBhIHN1Yi1zZXQgb2YgdGhlIGJ5IGRlZmF1bHQgZW5hYmxlZCBjaGFubmVscyBhcmUgYmVpbmdcbiAgICAjIHVzZWQuIEZvciBleGFtcGxlIHdoZW4gb25seSB1c2luZyB0aGUgZmlyc3QgOCBjaGFubmVscyBvZiB0aGUgVVMgYmFuZC5cbiAgICAjIE5vdGU6IHdoZW4gbGVmdCBibGFuayAvIGVtcHR5IGFycmF5LCBhbGwgY2hhbm5lbHMgd2lsbCBiZSBlbmFibGVkLlxuICAgIGVuYWJsZWRfdXBsaW5rX2NoYW5uZWxzPVs4LCA5LCAxMCwgMTEsIDEyLCAxMywgMTQsIDE1XVxuXG5cbiAgICAjIFJlam9pbi1yZXF1ZXN0IGNvbmZpZ3VyYXRpb24gKExvUmFXQU4gMS4xKVxuICAgIFtyZWdpb25zLm5ldHdvcmsucmVqb2luX3JlcXVlc3RdXG5cbiAgICAgICMgUmVxdWVzdCBkZXZpY2VzIHRvIHBlcmlvZGljYWxseSBzZW5kIHJlam9pbi1yZXF1ZXN0cy5cbiAgICAgIGVuYWJsZWQ9ZmFsc2VcblxuICAgICAgIyBUaGUgZGV2aWNlIG11c3Qgc2VuZCBhIHJlam9pbi1yZXF1ZXN0IHR5cGUgMCBhdCBsZWFzdCBldmVyeSAyXihtYXhfY291bnRfbiArIDQpXG4gICAgICAjIHVwbGluayBtZXNzYWdlcy4gVmFsaWQgdmFsdWVzIGFyZSAwIHRvIDE1LlxuICAgICAgbWF4X2NvdW50X249MFxuXG4gICAgICAjIFRoZSBkZXZpY2UgbXVzdCBzZW5kIGEgcmVqb2luLXJlcXVlc3QgdHlwZSAwIGF0IGxlYXN0IGV2ZXJ5IDJeKG1heF90aW1lX24gKyAxMClcbiAgICAgICMgc2Vjb25kcy4gVmFsaWQgdmFsdWVzIGFyZSAwIHRvIDE1LlxuICAgICAgI1xuICAgICAgIyAwICA9IHJvdWdobHkgMTcgbWludXRlc1xuICAgICAgIyAxNSA9IGFib3V0IDEgeWVhclxuICAgICAgbWF4X3RpbWVfbj0wXG4gICAgXG5cbiAgICAjIENsYXNzLUIgY29uZmlndXJhdGlvbi5cbiAgICBbcmVnaW9ucy5uZXR3b3JrLmNsYXNzX2JdXG5cbiAgICAgICMgUGluZy1zbG90IGRhdGEtcmF0ZS4gXG4gICAgICBwaW5nX3Nsb3RfZHI9MlxuXG4gICAgICAjIFBpbmctc2xvdCBmcmVxdWVuY3kgKEh6KVxuICAgICAgI1xuICAgICAgIyBzZXQgdGhpcyB0byAwIHRvIHVzZSB0aGUgZGVmYXVsdCBmcmVxdWVuY3kgcGxhbiBmb3IgdGhlIGNvbmZpZ3VyZWQgcmVnaW9uXG4gICAgICAjICh3aGljaCBjb3VsZCBiZSBmcmVxdWVuY3kgaG9wcGluZykuXG4gICAgICBwaW5nX3Nsb3RfZnJlcXVlbmN5PTBcblwiXCJcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuc2VydmljZU5hbWUgPSBcImNoaXJwc3RhY2tcIlxuZmlsZVBhdGggPSBcIi9jaGlycHN0YWNrL3JlZ2lvbl9jbjQ3MF8yLnRvbWxcIlxuY29udGVudCA9IFwiXCJcIlxuIyBUaGlzIGZpbGUgY29udGFpbnMgYW4gZXhhbXBsZSBDTjQ3MCBleGFtcGxlIChjaGFubmVscyAxNi0yMykuXG5bW3JlZ2lvbnNdXVxuXG4gICMgSUQgaXMgYW4gdXNlLWRlZmluZWQgaWRlbnRpZmllciBmb3IgdGhpcyByZWdpb24uXG4gIGlkPVwiY240NzBfMlwiXG5cbiAgIyBEZXNjcmlwdGlvbiBpcyBhIHNob3J0IGRlc2NyaXB0aW9uIGZvciB0aGlzIHJlZ2lvbi5cbiAgZGVzY3JpcHRpb249XCJDTjQ3MCAoY2hhbm5lbHMgMTYtMjMpXCJcblxuICAjIENvbW1vbi1uYW1lIHJlZmVycyB0byB0aGUgY29tbW9uLW5hbWUgb2YgdGhpcyByZWdpb24gYXMgZGVmaW5lZCBieVxuICAjIHRoZSBMb1JhIEFsbGlhbmNlLlxuICBjb21tb25fbmFtZT1cIkNONDcwXCJcblxuXG4gICMgR2F0ZXdheSBjb25maWd1cmF0aW9uLlxuICBbcmVnaW9ucy5nYXRld2F5XVxuXG4gICAgIyBGb3JjZSBnYXRld2F5cyBhcyBwcml2YXRlLlxuICAgICNcbiAgICAjIElmIGVuYWJsZWQsIGdhdGV3YXlzIGNhbiBvbmx5IGJlIHVzZWQgYnkgZGV2aWNlcyB1bmRlciB0aGUgc2FtZSB0ZW5hbnQuXG4gICAgZm9yY2VfZ3dzX3ByaXZhdGU9ZmFsc2VcblxuICAgIFxuICAgICMgR2F0ZXdheSBiYWNrZW5kIGNvbmZpZ3VyYXRpb24uXG4gICAgW3JlZ2lvbnMuZ2F0ZXdheS5iYWNrZW5kXVxuXG4gICAgICAjIFRoZSBlbmFibGVkIGJhY2tlbmQgdHlwZS5cbiAgICAgIGVuYWJsZWQ9XCJtcXR0XCJcblxuICAgICAgIyBNUVRUIGNvbmZpZ3VyYXRpb24uXG4gICAgICBbcmVnaW9ucy5nYXRld2F5LmJhY2tlbmQubXF0dF1cblxuICAgICAgICAjIFRvcGljIHByZWZpeC5cbiAgICAgICAgI1xuICAgICAgICAjIFRoZSB0b3BpYyBwcmVmaXggY2FuIGJlIHVzZWQgdG8gZGVmaW5lIHRoZSByZWdpb24gb2YgdGhlIGdhdGV3YXkuXG4gICAgICAgICMgTm90ZSwgdGhlcmUgaXMgbm8gbmVlZCB0byBhZGQgYSB0cmFpbGluZyAnLycgdG8gdGhlIHByZWZpeC4gVGhlIHRyYWlsaW5nXG4gICAgICAgICMgJy8nIGlzIGF1dG9tYXRpY2FsbHkgYWRkZWQgdG8gdGhlIHByZWZpeCBpZiBpdCBpcyBjb25maWd1cmVkLlxuICAgICAgICB0b3BpY19wcmVmaXg9XCJjbjQ3MF8yXCJcblxuICAgICAgICAjIE1RVFQgc2VydmVyIChlLmcuIHNjaGVtZTovL2hvc3Q6cG9ydCB3aGVyZSBzY2hlbWUgaXMgdGNwLCBzc2wgb3Igd3MpXG4gICAgICAgIHNlcnZlcj1cInRjcDovL21vc3F1aXR0bzoxODgzXCJcblxuICAgICAgICAjIENvbm5lY3Qgd2l0aCB0aGUgZ2l2ZW4gdXNlcm5hbWUgKG9wdGlvbmFsKVxuICAgICAgICB1c2VybmFtZT1cIlwiXG5cbiAgICAgICAgIyBDb25uZWN0IHdpdGggdGhlIGdpdmVuIHBhc3N3b3JkIChvcHRpb25hbClcbiAgICAgICAgcGFzc3dvcmQ9XCJcIlxuXG4gICAgICAgICMgUXVhbGl0eSBvZiBzZXJ2aWNlIGxldmVsXG4gICAgICAgICNcbiAgICAgICAgIyAwOiBhdCBtb3N0IG9uY2VcbiAgICAgICAgIyAxOiBhdCBsZWFzdCBvbmNlXG4gICAgICAgICMgMjogZXhhY3RseSBvbmNlXG4gICAgICAgICNcbiAgICAgICAgIyBOb3RlOiBhbiBpbmNyZWFzZSBvZiB0aGlzIHZhbHVlIHdpbGwgZGVjcmVhc2UgdGhlIHBlcmZvcm1hbmNlLlxuICAgICAgICAjIEZvciBtb3JlIGluZm9ybWF0aW9uOiBodHRwczovL3d3dy5oaXZlbXEuY29tL2Jsb2cvbXF0dC1lc3NlbnRpYWxzLXBhcnQtNi1tcXR0LXF1YWxpdHktb2Ytc2VydmljZS1sZXZlbHNcbiAgICAgICAgcW9zPTBcblxuICAgICAgICAjIENsZWFuIHNlc3Npb25cbiAgICAgICAgI1xuICAgICAgICAjIFNldCB0aGUgXCJjbGVhbiBzZXNzaW9uXCIgZmxhZyBpbiB0aGUgY29ubmVjdCBtZXNzYWdlIHdoZW4gdGhpcyBjbGllbnRcbiAgICAgICAgIyBjb25uZWN0cyB0byBhbiBNUVRUIGJyb2tlci4gQnkgc2V0dGluZyB0aGlzIGZsYWcgeW91IGFyZSBpbmRpY2F0aW5nXG4gICAgICAgICMgdGhhdCBubyBtZXNzYWdlcyBzYXZlZCBieSB0aGUgYnJva2VyIGZvciB0aGlzIGNsaWVudCBzaG91bGQgYmUgZGVsaXZlcmVkLlxuICAgICAgICBjbGVhbl9zZXNzaW9uPWZhbHNlXG5cbiAgICAgICAgIyBDbGllbnQgSURcbiAgICAgICAgI1xuICAgICAgICAjIFNldCB0aGUgY2xpZW50IGlkIHRvIGJlIHVzZWQgYnkgdGhpcyBjbGllbnQgd2hlbiBjb25uZWN0aW5nIHRvIHRoZSBNUVRUXG4gICAgICAgICMgYnJva2VyLiBBIGNsaWVudCBpZCBtdXN0IGJlIG5vIGxvbmdlciB0aGFuIDIzIGNoYXJhY3RlcnMuIElmIGxlZnQgYmxhbmssXG4gICAgICAgICMgYSByYW5kb20gaWQgd2lsbCBiZSBnZW5lcmF0ZWQgYnkgQ2hpcnBTdGFjay5cbiAgICAgICAgY2xpZW50X2lkPVwiXCJcblxuICAgICAgICAjIEtlZXAgYWxpdmUgaW50ZXJ2YWwuXG4gICAgICAgICNcbiAgICAgICAgIyBUaGlzIGRlZmluZXMgdGhlIG1heGltdW0gdGltZSB0aGF0IHRoYXQgc2hvdWxkIHBhc3Mgd2l0aG91dCBjb21tdW5pY2F0aW9uXG4gICAgICAgICMgYmV0d2VlbiB0aGUgY2xpZW50IGFuZCBzZXJ2ZXIuXG4gICAgICAgIGtlZXBfYWxpdmVfaW50ZXJ2YWw9XCIzMHNcIlxuXG4gICAgICAgICMgQ0EgY2VydGlmaWNhdGUgZmlsZSAob3B0aW9uYWwpXG4gICAgICAgICNcbiAgICAgICAgIyBVc2UgdGhpcyB3aGVuIHNldHRpbmcgdXAgYSBzZWN1cmUgY29ubmVjdGlvbiAod2hlbiBzZXJ2ZXIgdXNlcyBzc2w6Ly8uLi4pXG4gICAgICAgICMgYnV0IHRoZSBjZXJ0aWZpY2F0ZSB1c2VkIGJ5IHRoZSBzZXJ2ZXIgaXMgbm90IHRydXN0ZWQgYnkgYW55IENBIGNlcnRpZmljYXRlXG4gICAgICAgICMgb24gdGhlIHNlcnZlciAoZS5nLiB3aGVuIHNlbGYgZ2VuZXJhdGVkKS5cbiAgICAgICAgY2FfY2VydD1cIlwiXG5cbiAgICAgICAgIyBUTFMgY2VydGlmaWNhdGUgZmlsZSAob3B0aW9uYWwpXG4gICAgICAgIHRsc19jZXJ0PVwiXCJcblxuICAgICAgICAjIFRMUyBrZXkgZmlsZSAob3B0aW9uYWwpXG4gICAgICAgIHRsc19rZXk9XCJcIlxuXG5cbiAgICAjIEdhdGV3YXkgY2hhbm5lbCBjb25maWd1cmF0aW9uLlxuICAgICNcbiAgICAjIE5vdGU6IHRoaXMgY29uZmlndXJhdGlvbiBpcyBvbmx5IHVzZWQgaW4gY2FzZSB0aGUgZ2F0ZXdheSBpcyB1c2luZyB0aGVcbiAgICAjIENoaXJwU3RhY2sgQ29uY2VudHJhdG9yZCBkYWVtb24uIEluIGFueSBvdGhlciBjYXNlLCB0aGlzIGNvbmZpZ3VyYXRpb24gXG4gICAgIyBpcyBpZ25vcmVkLlxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT00NzM1MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTQ3MzcwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9NDczOTAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT00NzQxMDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTQ3NDMwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9NDc0NTAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT00NzQ3MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTQ3NDkwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cblxuICAjIFJlZ2lvbiBzcGVjaWZpYyBuZXR3b3JrIGNvbmZpZ3VyYXRpb24uXG4gIFtyZWdpb25zLm5ldHdvcmtdXG4gICAgXG4gICAgIyBJbnN0YWxsYXRpb24gbWFyZ2luIChkQikgdXNlZCBieSB0aGUgQURSIGVuZ2luZS5cbiAgICAjXG4gICAgIyBBIGhpZ2hlciBudW1iZXIgbWVhbnMgdGhhdCB0aGUgbmV0d29yay1zZXJ2ZXIgd2lsbCBrZWVwIG1vcmUgbWFyZ2luLFxuICAgICMgcmVzdWx0aW5nIGluIGEgbG93ZXIgZGF0YS1yYXRlIGJ1dCBkZWNyZWFzaW5nIHRoZSBjaGFuY2UgdGhhdCB0aGVcbiAgICAjIGRldmljZSBnZXRzIGRpc2Nvbm5lY3RlZCBiZWNhdXNlIGl0IGlzIHVuYWJsZSB0byByZWFjaCBvbmUgb2YgdGhlXG4gICAgIyBzdXJyb3VuZGVkIGdhdGV3YXlzLlxuICAgIGluc3RhbGxhdGlvbl9tYXJnaW49MTBcblxuICAgICMgUlggd2luZG93IChDbGFzcy1BKS5cbiAgICAjXG4gICAgIyBTZXQgdGhpcyB0bzpcbiAgICAjIDA6IFJYMSAvIFJYMlxuICAgICMgMTogUlgxIG9ubHlcbiAgICAjIDI6IFJYMiBvbmx5XG4gICAgcnhfd2luZG93PTBcblxuICAgICMgUlgxIGRlbGF5ICgxIC0gMTUgc2Vjb25kcykuXG4gICAgcngxX2RlbGF5PTFcblxuICAgICMgUlgxIGRhdGEtcmF0ZSBvZmZzZXRcbiAgICByeDFfZHJfb2Zmc2V0PTBcblxuICAgICMgUlgyIGRhdGEtcmF0ZVxuICAgIHJ4Ml9kcj0wXG5cbiAgICAjIFJYMiBmcmVxdWVuY3kgKEh6KVxuICAgIHJ4Ml9mcmVxdWVuY3k9NTA1MzAwMDAwXG5cbiAgICAjIFByZWZlciBSWDIgb24gUlgxIGRhdGEtcmF0ZSBsZXNzIHRoYW4uXG4gICAgI1xuICAgICMgUHJlZmVyIFJYMiBvdmVyIFJYMSBiYXNlZCBvbiB0aGUgUlgxIGRhdGEtcmF0ZS4gV2hlbiB0aGUgUlgxIGRhdGEtcmF0ZVxuICAgICMgaXMgc21hbGxlciB0aGFuIHRoZSBjb25maWd1cmVkIHZhbHVlLCB0aGVuIHRoZSBOZXR3b3JrIFNlcnZlciB3aWxsXG4gICAgIyBmaXJzdCB0cnkgdG8gc2NoZWR1bGUgdGhlIGRvd25saW5rIGZvciBSWDIsIGZhaWxpbmcgdGhhdCAoZS5nLiB0aGUgZ2F0ZXdheVxuICAgICMgaGFzIGFscmVhZHkgYSBwYXlsb2FkIHNjaGVkdWxlZCBhdCB0aGUgUlgyIHRpbWluZykgaXQgd2lsbCB0cnkgUlgxLlxuICAgIHJ4Ml9wcmVmZXJfb25fcngxX2RyX2x0PTBcblxuICAgICMgUHJlZmVyIFJYMiBvbiBsaW5rIGJ1ZGdldC5cbiAgICAjXG4gICAgIyBXaGVuIHRoZSBsaW5rLWJ1ZGdldCBpcyBiZXR0ZXIgZm9yIFJYMiB0aGFuIGZvciBSWDEsIHRoZSBOZXR3b3JrIFNlcnZlciB3aWxsIGZpcnN0XG4gICAgIyB0cnkgdG8gc2NoZWR1bGUgdGhlIGRvd25saW5rIGluIFJYMiwgZmFpbGluZyB0aGF0IGl0IHdpbGwgdHJ5IFJYMS5cbiAgICByeDJfcHJlZmVyX29uX2xpbmtfYnVkZ2V0PWZhbHNlXG5cbiAgICAjIERvd25saW5rIFRYIFBvd2VyIChkQm0pXG4gICAgI1xuICAgICMgV2hlbiBzZXQgdG8gLTEsIHRoZSBkb3dubGluayBUWCBQb3dlciBmcm9tIHRoZSBjb25maWd1cmVkIGJhbmQgd2lsbFxuICAgICMgYmUgdXNlZC5cbiAgICAjXG4gICAgIyBQbGVhc2UgY29uc3VsdCB0aGUgTG9SYVdBTiBSZWdpb25hbCBQYXJhbWV0ZXJzIGFuZCBsb2NhbCByZWd1bGF0aW9uc1xuICAgICMgZm9yIHZhbGlkIGFuZCBsZWdhbCBvcHRpb25zLiBOb3RlIHRoYXQgdGhlIGNvbmZpZ3VyZWQgVFggUG93ZXIgbXVzdCBiZVxuICAgICMgc3VwcG9ydGVkIGJ5IHlvdXIgZ2F0ZXdheShzKS5cbiAgICBkb3dubGlua190eF9wb3dlcj0tMVxuXG4gICAgIyBBRFIgaXMgZGlzYWJsZWQuXG4gICAgYWRyX2Rpc2FibGVkPWZhbHNlXG5cbiAgICAjIE1pbmltdW0gZGF0YS1yYXRlLlxuICAgIG1pbl9kcj0wXG5cbiAgICAjIE1heGltdW0gZGF0YS1yYXRlLlxuICAgIG1heF9kcj01XG5cbiAgICAjIEVuYWJsZWQgdXBsaW5rIGNoYW5uZWxzLlxuICAgICNcbiAgICAjIFVzZSB0aGlzIHdoZW4gb255IGEgc3ViLXNldCBvZiB0aGUgYnkgZGVmYXVsdCBlbmFibGVkIGNoYW5uZWxzIGFyZSBiZWluZ1xuICAgICMgdXNlZC4gRm9yIGV4YW1wbGUgd2hlbiBvbmx5IHVzaW5nIHRoZSBmaXJzdCA4IGNoYW5uZWxzIG9mIHRoZSBVUyBiYW5kLlxuICAgICMgTm90ZTogd2hlbiBsZWZ0IGJsYW5rIC8gZW1wdHkgYXJyYXksIGFsbCBjaGFubmVscyB3aWxsIGJlIGVuYWJsZWQuXG4gICAgZW5hYmxlZF91cGxpbmtfY2hhbm5lbHM9WzE2LCAxNywgMTgsIDE5LCAyMCwgMjEsIDIyLCAyM11cblxuXG4gICAgIyBSZWpvaW4tcmVxdWVzdCBjb25maWd1cmF0aW9uIChMb1JhV0FOIDEuMSlcbiAgICBbcmVnaW9ucy5uZXR3b3JrLnJlam9pbl9yZXF1ZXN0XVxuXG4gICAgICAjIFJlcXVlc3QgZGV2aWNlcyB0byBwZXJpb2RpY2FsbHkgc2VuZCByZWpvaW4tcmVxdWVzdHMuXG4gICAgICBlbmFibGVkPWZhbHNlXG5cbiAgICAgICMgVGhlIGRldmljZSBtdXN0IHNlbmQgYSByZWpvaW4tcmVxdWVzdCB0eXBlIDAgYXQgbGVhc3QgZXZlcnkgMl4obWF4X2NvdW50X24gKyA0KVxuICAgICAgIyB1cGxpbmsgbWVzc2FnZXMuIFZhbGlkIHZhbHVlcyBhcmUgMCB0byAxNS5cbiAgICAgIG1heF9jb3VudF9uPTBcblxuICAgICAgIyBUaGUgZGV2aWNlIG11c3Qgc2VuZCBhIHJlam9pbi1yZXF1ZXN0IHR5cGUgMCBhdCBsZWFzdCBldmVyeSAyXihtYXhfdGltZV9uICsgMTApXG4gICAgICAjIHNlY29uZHMuIFZhbGlkIHZhbHVlcyBhcmUgMCB0byAxNS5cbiAgICAgICNcbiAgICAgICMgMCAgPSByb3VnaGx5IDE3IG1pbnV0ZXNcbiAgICAgICMgMTUgPSBhYm91dCAxIHllYXJcbiAgICAgIG1heF90aW1lX249MFxuICAgIFxuXG4gICAgIyBDbGFzcy1CIGNvbmZpZ3VyYXRpb24uXG4gICAgW3JlZ2lvbnMubmV0d29yay5jbGFzc19iXVxuXG4gICAgICAjIFBpbmctc2xvdCBkYXRhLXJhdGUuIFxuICAgICAgcGluZ19zbG90X2RyPTJcblxuICAgICAgIyBQaW5nLXNsb3QgZnJlcXVlbmN5IChIeilcbiAgICAgICNcbiAgICAgICMgc2V0IHRoaXMgdG8gMCB0byB1c2UgdGhlIGRlZmF1bHQgZnJlcXVlbmN5IHBsYW4gZm9yIHRoZSBjb25maWd1cmVkIHJlZ2lvblxuICAgICAgIyAod2hpY2ggY291bGQgYmUgZnJlcXVlbmN5IGhvcHBpbmcpLlxuICAgICAgcGluZ19zbG90X2ZyZXF1ZW5jeT0wXG5cIlwiXCJcblxuW1tjb25maWcubW91bnRzXV1cbnNlcnZpY2VOYW1lID0gXCJjaGlycHN0YWNrXCJcbmZpbGVQYXRoID0gXCIvY2hpcnBzdGFjay9yZWdpb25fY240NzBfMy50b21sXCJcbmNvbnRlbnQgPSBcIlwiXCJcbiMgVGhpcyBmaWxlIGNvbnRhaW5zIGFuIGV4YW1wbGUgQ040NzAgZXhhbXBsZSAoY2hhbm5lbHMgMjQtMzEpLlxuW1tyZWdpb25zXV1cblxuICAjIElEIGlzIGFuIHVzZS1kZWZpbmVkIGlkZW50aWZpZXIgZm9yIHRoaXMgcmVnaW9uLlxuICBpZD1cImNuNDcwXzNcIlxuXG4gICMgRGVzY3JpcHRpb24gaXMgYSBzaG9ydCBkZXNjcmlwdGlvbiBmb3IgdGhpcyByZWdpb24uXG4gIGRlc2NyaXB0aW9uPVwiQ040NzAgKGNoYW5uZWxzIDI0LTMxKVwiXG5cbiAgIyBDb21tb24tbmFtZSByZWZlcnMgdG8gdGhlIGNvbW1vbi1uYW1lIG9mIHRoaXMgcmVnaW9uIGFzIGRlZmluZWQgYnlcbiAgIyB0aGUgTG9SYSBBbGxpYW5jZS5cbiAgY29tbW9uX25hbWU9XCJDTjQ3MFwiXG5cblxuICAjIEdhdGV3YXkgY29uZmlndXJhdGlvbi5cbiAgW3JlZ2lvbnMuZ2F0ZXdheV1cblxuICAgICMgRm9yY2UgZ2F0ZXdheXMgYXMgcHJpdmF0ZS5cbiAgICAjXG4gICAgIyBJZiBlbmFibGVkLCBnYXRld2F5cyBjYW4gb25seSBiZSB1c2VkIGJ5IGRldmljZXMgdW5kZXIgdGhlIHNhbWUgdGVuYW50LlxuICAgIGZvcmNlX2d3c19wcml2YXRlPWZhbHNlXG5cbiAgICBcbiAgICAjIEdhdGV3YXkgYmFja2VuZCBjb25maWd1cmF0aW9uLlxuICAgIFtyZWdpb25zLmdhdGV3YXkuYmFja2VuZF1cblxuICAgICAgIyBUaGUgZW5hYmxlZCBiYWNrZW5kIHR5cGUuXG4gICAgICBlbmFibGVkPVwibXF0dFwiXG5cbiAgICAgICMgTVFUVCBjb25maWd1cmF0aW9uLlxuICAgICAgW3JlZ2lvbnMuZ2F0ZXdheS5iYWNrZW5kLm1xdHRdXG5cbiAgICAgICAgIyBUb3BpYyBwcmVmaXguXG4gICAgICAgICNcbiAgICAgICAgIyBUaGUgdG9waWMgcHJlZml4IGNhbiBiZSB1c2VkIHRvIGRlZmluZSB0aGUgcmVnaW9uIG9mIHRoZSBnYXRld2F5LlxuICAgICAgICAjIE5vdGUsIHRoZXJlIGlzIG5vIG5lZWQgdG8gYWRkIGEgdHJhaWxpbmcgJy8nIHRvIHRoZSBwcmVmaXguIFRoZSB0cmFpbGluZ1xuICAgICAgICAjICcvJyBpcyBhdXRvbWF0aWNhbGx5IGFkZGVkIHRvIHRoZSBwcmVmaXggaWYgaXQgaXMgY29uZmlndXJlZC5cbiAgICAgICAgdG9waWNfcHJlZml4PVwiY240NzBfM1wiXG5cbiAgICAgICAgIyBNUVRUIHNlcnZlciAoZS5nLiBzY2hlbWU6Ly9ob3N0OnBvcnQgd2hlcmUgc2NoZW1lIGlzIHRjcCwgc3NsIG9yIHdzKVxuICAgICAgICBzZXJ2ZXI9XCJ0Y3A6Ly9tb3NxdWl0dG86MTg4M1wiXG5cbiAgICAgICAgIyBDb25uZWN0IHdpdGggdGhlIGdpdmVuIHVzZXJuYW1lIChvcHRpb25hbClcbiAgICAgICAgdXNlcm5hbWU9XCJcIlxuXG4gICAgICAgICMgQ29ubmVjdCB3aXRoIHRoZSBnaXZlbiBwYXNzd29yZCAob3B0aW9uYWwpXG4gICAgICAgIHBhc3N3b3JkPVwiXCJcblxuICAgICAgICAjIFF1YWxpdHkgb2Ygc2VydmljZSBsZXZlbFxuICAgICAgICAjXG4gICAgICAgICMgMDogYXQgbW9zdCBvbmNlXG4gICAgICAgICMgMTogYXQgbGVhc3Qgb25jZVxuICAgICAgICAjIDI6IGV4YWN0bHkgb25jZVxuICAgICAgICAjXG4gICAgICAgICMgTm90ZTogYW4gaW5jcmVhc2Ugb2YgdGhpcyB2YWx1ZSB3aWxsIGRlY3JlYXNlIHRoZSBwZXJmb3JtYW5jZS5cbiAgICAgICAgIyBGb3IgbW9yZSBpbmZvcm1hdGlvbjogaHR0cHM6Ly93d3cuaGl2ZW1xLmNvbS9ibG9nL21xdHQtZXNzZW50aWFscy1wYXJ0LTYtbXF0dC1xdWFsaXR5LW9mLXNlcnZpY2UtbGV2ZWxzXG4gICAgICAgIHFvcz0wXG5cbiAgICAgICAgIyBDbGVhbiBzZXNzaW9uXG4gICAgICAgICNcbiAgICAgICAgIyBTZXQgdGhlIFwiY2xlYW4gc2Vzc2lvblwiIGZsYWcgaW4gdGhlIGNvbm5lY3QgbWVzc2FnZSB3aGVuIHRoaXMgY2xpZW50XG4gICAgICAgICMgY29ubmVjdHMgdG8gYW4gTVFUVCBicm9rZXIuIEJ5IHNldHRpbmcgdGhpcyBmbGFnIHlvdSBhcmUgaW5kaWNhdGluZ1xuICAgICAgICAjIHRoYXQgbm8gbWVzc2FnZXMgc2F2ZWQgYnkgdGhlIGJyb2tlciBmb3IgdGhpcyBjbGllbnQgc2hvdWxkIGJlIGRlbGl2ZXJlZC5cbiAgICAgICAgY2xlYW5fc2Vzc2lvbj1mYWxzZVxuXG4gICAgICAgICMgQ2xpZW50IElEXG4gICAgICAgICNcbiAgICAgICAgIyBTZXQgdGhlIGNsaWVudCBpZCB0byBiZSB1c2VkIGJ5IHRoaXMgY2xpZW50IHdoZW4gY29ubmVjdGluZyB0byB0aGUgTVFUVFxuICAgICAgICAjIGJyb2tlci4gQSBjbGllbnQgaWQgbXVzdCBiZSBubyBsb25nZXIgdGhhbiAyMyBjaGFyYWN0ZXJzLiBJZiBsZWZ0IGJsYW5rLFxuICAgICAgICAjIGEgcmFuZG9tIGlkIHdpbGwgYmUgZ2VuZXJhdGVkIGJ5IENoaXJwU3RhY2suXG4gICAgICAgIGNsaWVudF9pZD1cIlwiXG5cbiAgICAgICAgIyBLZWVwIGFsaXZlIGludGVydmFsLlxuICAgICAgICAjXG4gICAgICAgICMgVGhpcyBkZWZpbmVzIHRoZSBtYXhpbXVtIHRpbWUgdGhhdCB0aGF0IHNob3VsZCBwYXNzIHdpdGhvdXQgY29tbXVuaWNhdGlvblxuICAgICAgICAjIGJldHdlZW4gdGhlIGNsaWVudCBhbmQgc2VydmVyLlxuICAgICAgICBrZWVwX2FsaXZlX2ludGVydmFsPVwiMzBzXCJcblxuICAgICAgICAjIENBIGNlcnRpZmljYXRlIGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICAjXG4gICAgICAgICMgVXNlIHRoaXMgd2hlbiBzZXR0aW5nIHVwIGEgc2VjdXJlIGNvbm5lY3Rpb24gKHdoZW4gc2VydmVyIHVzZXMgc3NsOi8vLi4uKVxuICAgICAgICAjIGJ1dCB0aGUgY2VydGlmaWNhdGUgdXNlZCBieSB0aGUgc2VydmVyIGlzIG5vdCB0cnVzdGVkIGJ5IGFueSBDQSBjZXJ0aWZpY2F0ZVxuICAgICAgICAjIG9uIHRoZSBzZXJ2ZXIgKGUuZy4gd2hlbiBzZWxmIGdlbmVyYXRlZCkuXG4gICAgICAgIGNhX2NlcnQ9XCJcIlxuXG4gICAgICAgICMgVExTIGNlcnRpZmljYXRlIGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICB0bHNfY2VydD1cIlwiXG5cbiAgICAgICAgIyBUTFMga2V5IGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICB0bHNfa2V5PVwiXCJcblxuXG4gICAgIyBHYXRld2F5IGNoYW5uZWwgY29uZmlndXJhdGlvbi5cbiAgICAjXG4gICAgIyBOb3RlOiB0aGlzIGNvbmZpZ3VyYXRpb24gaXMgb25seSB1c2VkIGluIGNhc2UgdGhlIGdhdGV3YXkgaXMgdXNpbmcgdGhlXG4gICAgIyBDaGlycFN0YWNrIENvbmNlbnRyYXRvcmQgZGFlbW9uLiBJbiBhbnkgb3RoZXIgY2FzZSwgdGhpcyBjb25maWd1cmF0aW9uIFxuICAgICMgaXMgaWdub3JlZC5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9NDc1MTAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT00NzUzMDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTQ3NTUwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9NDc1NzAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT00NzU5MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTQ3NjEwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9NDc2MzAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT00NzY1MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG5cbiAgIyBSZWdpb24gc3BlY2lmaWMgbmV0d29yayBjb25maWd1cmF0aW9uLlxuICBbcmVnaW9ucy5uZXR3b3JrXVxuICAgIFxuICAgICMgSW5zdGFsbGF0aW9uIG1hcmdpbiAoZEIpIHVzZWQgYnkgdGhlIEFEUiBlbmdpbmUuXG4gICAgI1xuICAgICMgQSBoaWdoZXIgbnVtYmVyIG1lYW5zIHRoYXQgdGhlIG5ldHdvcmstc2VydmVyIHdpbGwga2VlcCBtb3JlIG1hcmdpbixcbiAgICAjIHJlc3VsdGluZyBpbiBhIGxvd2VyIGRhdGEtcmF0ZSBidXQgZGVjcmVhc2luZyB0aGUgY2hhbmNlIHRoYXQgdGhlXG4gICAgIyBkZXZpY2UgZ2V0cyBkaXNjb25uZWN0ZWQgYmVjYXVzZSBpdCBpcyB1bmFibGUgdG8gcmVhY2ggb25lIG9mIHRoZVxuICAgICMgc3Vycm91bmRlZCBnYXRld2F5cy5cbiAgICBpbnN0YWxsYXRpb25fbWFyZ2luPTEwXG5cbiAgICAjIFJYIHdpbmRvdyAoQ2xhc3MtQSkuXG4gICAgI1xuICAgICMgU2V0IHRoaXMgdG86XG4gICAgIyAwOiBSWDEgLyBSWDJcbiAgICAjIDE6IFJYMSBvbmx5XG4gICAgIyAyOiBSWDIgb25seVxuICAgIHJ4X3dpbmRvdz0wXG5cbiAgICAjIFJYMSBkZWxheSAoMSAtIDE1IHNlY29uZHMpLlxuICAgIHJ4MV9kZWxheT0xXG5cbiAgICAjIFJYMSBkYXRhLXJhdGUgb2Zmc2V0XG4gICAgcngxX2RyX29mZnNldD0wXG5cbiAgICAjIFJYMiBkYXRhLXJhdGVcbiAgICByeDJfZHI9MFxuXG4gICAgIyBSWDIgZnJlcXVlbmN5IChIeilcbiAgICByeDJfZnJlcXVlbmN5PTUwNTMwMDAwMFxuXG4gICAgIyBQcmVmZXIgUlgyIG9uIFJYMSBkYXRhLXJhdGUgbGVzcyB0aGFuLlxuICAgICNcbiAgICAjIFByZWZlciBSWDIgb3ZlciBSWDEgYmFzZWQgb24gdGhlIFJYMSBkYXRhLXJhdGUuIFdoZW4gdGhlIFJYMSBkYXRhLXJhdGVcbiAgICAjIGlzIHNtYWxsZXIgdGhhbiB0aGUgY29uZmlndXJlZCB2YWx1ZSwgdGhlbiB0aGUgTmV0d29yayBTZXJ2ZXIgd2lsbFxuICAgICMgZmlyc3QgdHJ5IHRvIHNjaGVkdWxlIHRoZSBkb3dubGluayBmb3IgUlgyLCBmYWlsaW5nIHRoYXQgKGUuZy4gdGhlIGdhdGV3YXlcbiAgICAjIGhhcyBhbHJlYWR5IGEgcGF5bG9hZCBzY2hlZHVsZWQgYXQgdGhlIFJYMiB0aW1pbmcpIGl0IHdpbGwgdHJ5IFJYMS5cbiAgICByeDJfcHJlZmVyX29uX3J4MV9kcl9sdD0wXG5cbiAgICAjIFByZWZlciBSWDIgb24gbGluayBidWRnZXQuXG4gICAgI1xuICAgICMgV2hlbiB0aGUgbGluay1idWRnZXQgaXMgYmV0dGVyIGZvciBSWDIgdGhhbiBmb3IgUlgxLCB0aGUgTmV0d29yayBTZXJ2ZXIgd2lsbCBmaXJzdFxuICAgICMgdHJ5IHRvIHNjaGVkdWxlIHRoZSBkb3dubGluayBpbiBSWDIsIGZhaWxpbmcgdGhhdCBpdCB3aWxsIHRyeSBSWDEuXG4gICAgcngyX3ByZWZlcl9vbl9saW5rX2J1ZGdldD1mYWxzZVxuXG4gICAgIyBEb3dubGluayBUWCBQb3dlciAoZEJtKVxuICAgICNcbiAgICAjIFdoZW4gc2V0IHRvIC0xLCB0aGUgZG93bmxpbmsgVFggUG93ZXIgZnJvbSB0aGUgY29uZmlndXJlZCBiYW5kIHdpbGxcbiAgICAjIGJlIHVzZWQuXG4gICAgI1xuICAgICMgUGxlYXNlIGNvbnN1bHQgdGhlIExvUmFXQU4gUmVnaW9uYWwgUGFyYW1ldGVycyBhbmQgbG9jYWwgcmVndWxhdGlvbnNcbiAgICAjIGZvciB2YWxpZCBhbmQgbGVnYWwgb3B0aW9ucy4gTm90ZSB0aGF0IHRoZSBjb25maWd1cmVkIFRYIFBvd2VyIG11c3QgYmVcbiAgICAjIHN1cHBvcnRlZCBieSB5b3VyIGdhdGV3YXkocykuXG4gICAgZG93bmxpbmtfdHhfcG93ZXI9LTFcblxuICAgICMgQURSIGlzIGRpc2FibGVkLlxuICAgIGFkcl9kaXNhYmxlZD1mYWxzZVxuXG4gICAgIyBNaW5pbXVtIGRhdGEtcmF0ZS5cbiAgICBtaW5fZHI9MFxuXG4gICAgIyBNYXhpbXVtIGRhdGEtcmF0ZS5cbiAgICBtYXhfZHI9NVxuXG4gICAgIyBFbmFibGVkIHVwbGluayBjaGFubmVscy5cbiAgICAjXG4gICAgIyBVc2UgdGhpcyB3aGVuIG9ueSBhIHN1Yi1zZXQgb2YgdGhlIGJ5IGRlZmF1bHQgZW5hYmxlZCBjaGFubmVscyBhcmUgYmVpbmdcbiAgICAjIHVzZWQuIEZvciBleGFtcGxlIHdoZW4gb25seSB1c2luZyB0aGUgZmlyc3QgOCBjaGFubmVscyBvZiB0aGUgVVMgYmFuZC5cbiAgICAjIE5vdGU6IHdoZW4gbGVmdCBibGFuayAvIGVtcHR5IGFycmF5LCBhbGwgY2hhbm5lbHMgd2lsbCBiZSBlbmFibGVkLlxuICAgIGVuYWJsZWRfdXBsaW5rX2NoYW5uZWxzPVsyNCwgMjUsIDI2LCAyNywgMjgsIDI5LCAzMCwgMzFdXG5cblxuICAgICMgUmVqb2luLXJlcXVlc3QgY29uZmlndXJhdGlvbiAoTG9SYVdBTiAxLjEpXG4gICAgW3JlZ2lvbnMubmV0d29yay5yZWpvaW5fcmVxdWVzdF1cblxuICAgICAgIyBSZXF1ZXN0IGRldmljZXMgdG8gcGVyaW9kaWNhbGx5IHNlbmQgcmVqb2luLXJlcXVlc3RzLlxuICAgICAgZW5hYmxlZD1mYWxzZVxuXG4gICAgICAjIFRoZSBkZXZpY2UgbXVzdCBzZW5kIGEgcmVqb2luLXJlcXVlc3QgdHlwZSAwIGF0IGxlYXN0IGV2ZXJ5IDJeKG1heF9jb3VudF9uICsgNClcbiAgICAgICMgdXBsaW5rIG1lc3NhZ2VzLiBWYWxpZCB2YWx1ZXMgYXJlIDAgdG8gMTUuXG4gICAgICBtYXhfY291bnRfbj0wXG5cbiAgICAgICMgVGhlIGRldmljZSBtdXN0IHNlbmQgYSByZWpvaW4tcmVxdWVzdCB0eXBlIDAgYXQgbGVhc3QgZXZlcnkgMl4obWF4X3RpbWVfbiArIDEwKVxuICAgICAgIyBzZWNvbmRzLiBWYWxpZCB2YWx1ZXMgYXJlIDAgdG8gMTUuXG4gICAgICAjXG4gICAgICAjIDAgID0gcm91Z2hseSAxNyBtaW51dGVzXG4gICAgICAjIDE1ID0gYWJvdXQgMSB5ZWFyXG4gICAgICBtYXhfdGltZV9uPTBcbiAgICBcblxuICAgICMgQ2xhc3MtQiBjb25maWd1cmF0aW9uLlxuICAgIFtyZWdpb25zLm5ldHdvcmsuY2xhc3NfYl1cblxuICAgICAgIyBQaW5nLXNsb3QgZGF0YS1yYXRlLiBcbiAgICAgIHBpbmdfc2xvdF9kcj0yXG5cbiAgICAgICMgUGluZy1zbG90IGZyZXF1ZW5jeSAoSHopXG4gICAgICAjXG4gICAgICAjIHNldCB0aGlzIHRvIDAgdG8gdXNlIHRoZSBkZWZhdWx0IGZyZXF1ZW5jeSBwbGFuIGZvciB0aGUgY29uZmlndXJlZCByZWdpb25cbiAgICAgICMgKHdoaWNoIGNvdWxkIGJlIGZyZXF1ZW5jeSBob3BwaW5nKS5cbiAgICAgIHBpbmdfc2xvdF9mcmVxdWVuY3k9MFxuXCJcIlwiXG5cbltbY29uZmlnLm1vdW50c11dXG5zZXJ2aWNlTmFtZSA9IFwiY2hpcnBzdGFja1wiXG5maWxlUGF0aCA9IFwiL2NoaXJwc3RhY2svcmVnaW9uX2NuNDcwXzQudG9tbFwiXG5jb250ZW50ID0gXCJcIlwiXG4jIFRoaXMgZmlsZSBjb250YWlucyBhbiBleGFtcGxlIENONDcwIGV4YW1wbGUgKGNoYW5uZWxzIDMyLTM5KS5cbltbcmVnaW9uc11dXG5cbiAgIyBJRCBpcyBhbiB1c2UtZGVmaW5lZCBpZGVudGlmaWVyIGZvciB0aGlzIHJlZ2lvbi5cbiAgaWQ9XCJjbjQ3MF80XCJcblxuICAjIERlc2NyaXB0aW9uIGlzIGEgc2hvcnQgZGVzY3JpcHRpb24gZm9yIHRoaXMgcmVnaW9uLlxuICBkZXNjcmlwdGlvbj1cIkNONDcwIChjaGFubmVscyAzMi0zOSlcIlxuXG4gICMgQ29tbW9uLW5hbWUgcmVmZXJzIHRvIHRoZSBjb21tb24tbmFtZSBvZiB0aGlzIHJlZ2lvbiBhcyBkZWZpbmVkIGJ5XG4gICMgdGhlIExvUmEgQWxsaWFuY2UuXG4gIGNvbW1vbl9uYW1lPVwiQ040NzBcIlxuXG5cbiAgIyBHYXRld2F5IGNvbmZpZ3VyYXRpb24uXG4gIFtyZWdpb25zLmdhdGV3YXldXG5cbiAgICAjIEZvcmNlIGdhdGV3YXlzIGFzIHByaXZhdGUuXG4gICAgI1xuICAgICMgSWYgZW5hYmxlZCwgZ2F0ZXdheXMgY2FuIG9ubHkgYmUgdXNlZCBieSBkZXZpY2VzIHVuZGVyIHRoZSBzYW1lIHRlbmFudC5cbiAgICBmb3JjZV9nd3NfcHJpdmF0ZT1mYWxzZVxuXG4gICAgXG4gICAgIyBHYXRld2F5IGJhY2tlbmQgY29uZmlndXJhdGlvbi5cbiAgICBbcmVnaW9ucy5nYXRld2F5LmJhY2tlbmRdXG5cbiAgICAgICMgVGhlIGVuYWJsZWQgYmFja2VuZCB0eXBlLlxuICAgICAgZW5hYmxlZD1cIm1xdHRcIlxuXG4gICAgICAjIE1RVFQgY29uZmlndXJhdGlvbi5cbiAgICAgIFtyZWdpb25zLmdhdGV3YXkuYmFja2VuZC5tcXR0XVxuXG4gICAgICAgICMgVG9waWMgcHJlZml4LlxuICAgICAgICAjXG4gICAgICAgICMgVGhlIHRvcGljIHByZWZpeCBjYW4gYmUgdXNlZCB0byBkZWZpbmUgdGhlIHJlZ2lvbiBvZiB0aGUgZ2F0ZXdheS5cbiAgICAgICAgIyBOb3RlLCB0aGVyZSBpcyBubyBuZWVkIHRvIGFkZCBhIHRyYWlsaW5nICcvJyB0byB0aGUgcHJlZml4LiBUaGUgdHJhaWxpbmdcbiAgICAgICAgIyAnLycgaXMgYXV0b21hdGljYWxseSBhZGRlZCB0byB0aGUgcHJlZml4IGlmIGl0IGlzIGNvbmZpZ3VyZWQuXG4gICAgICAgIHRvcGljX3ByZWZpeD1cImNuNDcwXzRcIlxuXG4gICAgICAgICMgTVFUVCBzZXJ2ZXIgKGUuZy4gc2NoZW1lOi8vaG9zdDpwb3J0IHdoZXJlIHNjaGVtZSBpcyB0Y3AsIHNzbCBvciB3cylcbiAgICAgICAgc2VydmVyPVwidGNwOi8vbW9zcXVpdHRvOjE4ODNcIlxuXG4gICAgICAgICMgQ29ubmVjdCB3aXRoIHRoZSBnaXZlbiB1c2VybmFtZSAob3B0aW9uYWwpXG4gICAgICAgIHVzZXJuYW1lPVwiXCJcblxuICAgICAgICAjIENvbm5lY3Qgd2l0aCB0aGUgZ2l2ZW4gcGFzc3dvcmQgKG9wdGlvbmFsKVxuICAgICAgICBwYXNzd29yZD1cIlwiXG5cbiAgICAgICAgIyBRdWFsaXR5IG9mIHNlcnZpY2UgbGV2ZWxcbiAgICAgICAgI1xuICAgICAgICAjIDA6IGF0IG1vc3Qgb25jZVxuICAgICAgICAjIDE6IGF0IGxlYXN0IG9uY2VcbiAgICAgICAgIyAyOiBleGFjdGx5IG9uY2VcbiAgICAgICAgI1xuICAgICAgICAjIE5vdGU6IGFuIGluY3JlYXNlIG9mIHRoaXMgdmFsdWUgd2lsbCBkZWNyZWFzZSB0aGUgcGVyZm9ybWFuY2UuXG4gICAgICAgICMgRm9yIG1vcmUgaW5mb3JtYXRpb246IGh0dHBzOi8vd3d3LmhpdmVtcS5jb20vYmxvZy9tcXR0LWVzc2VudGlhbHMtcGFydC02LW1xdHQtcXVhbGl0eS1vZi1zZXJ2aWNlLWxldmVsc1xuICAgICAgICBxb3M9MFxuXG4gICAgICAgICMgQ2xlYW4gc2Vzc2lvblxuICAgICAgICAjXG4gICAgICAgICMgU2V0IHRoZSBcImNsZWFuIHNlc3Npb25cIiBmbGFnIGluIHRoZSBjb25uZWN0IG1lc3NhZ2Ugd2hlbiB0aGlzIGNsaWVudFxuICAgICAgICAjIGNvbm5lY3RzIHRvIGFuIE1RVFQgYnJva2VyLiBCeSBzZXR0aW5nIHRoaXMgZmxhZyB5b3UgYXJlIGluZGljYXRpbmdcbiAgICAgICAgIyB0aGF0IG5vIG1lc3NhZ2VzIHNhdmVkIGJ5IHRoZSBicm9rZXIgZm9yIHRoaXMgY2xpZW50IHNob3VsZCBiZSBkZWxpdmVyZWQuXG4gICAgICAgIGNsZWFuX3Nlc3Npb249ZmFsc2VcblxuICAgICAgICAjIENsaWVudCBJRFxuICAgICAgICAjXG4gICAgICAgICMgU2V0IHRoZSBjbGllbnQgaWQgdG8gYmUgdXNlZCBieSB0aGlzIGNsaWVudCB3aGVuIGNvbm5lY3RpbmcgdG8gdGhlIE1RVFRcbiAgICAgICAgIyBicm9rZXIuIEEgY2xpZW50IGlkIG11c3QgYmUgbm8gbG9uZ2VyIHRoYW4gMjMgY2hhcmFjdGVycy4gSWYgbGVmdCBibGFuayxcbiAgICAgICAgIyBhIHJhbmRvbSBpZCB3aWxsIGJlIGdlbmVyYXRlZCBieSBDaGlycFN0YWNrLlxuICAgICAgICBjbGllbnRfaWQ9XCJcIlxuXG4gICAgICAgICMgS2VlcCBhbGl2ZSBpbnRlcnZhbC5cbiAgICAgICAgI1xuICAgICAgICAjIFRoaXMgZGVmaW5lcyB0aGUgbWF4aW11bSB0aW1lIHRoYXQgdGhhdCBzaG91bGQgcGFzcyB3aXRob3V0IGNvbW11bmljYXRpb25cbiAgICAgICAgIyBiZXR3ZWVuIHRoZSBjbGllbnQgYW5kIHNlcnZlci5cbiAgICAgICAga2VlcF9hbGl2ZV9pbnRlcnZhbD1cIjMwc1wiXG5cbiAgICAgICAgIyBDQSBjZXJ0aWZpY2F0ZSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgI1xuICAgICAgICAjIFVzZSB0aGlzIHdoZW4gc2V0dGluZyB1cCBhIHNlY3VyZSBjb25uZWN0aW9uICh3aGVuIHNlcnZlciB1c2VzIHNzbDovLy4uLilcbiAgICAgICAgIyBidXQgdGhlIGNlcnRpZmljYXRlIHVzZWQgYnkgdGhlIHNlcnZlciBpcyBub3QgdHJ1c3RlZCBieSBhbnkgQ0EgY2VydGlmaWNhdGVcbiAgICAgICAgIyBvbiB0aGUgc2VydmVyIChlLmcuIHdoZW4gc2VsZiBnZW5lcmF0ZWQpLlxuICAgICAgICBjYV9jZXJ0PVwiXCJcblxuICAgICAgICAjIFRMUyBjZXJ0aWZpY2F0ZSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgdGxzX2NlcnQ9XCJcIlxuXG4gICAgICAgICMgVExTIGtleSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgdGxzX2tleT1cIlwiXG5cblxuICAgICMgR2F0ZXdheSBjaGFubmVsIGNvbmZpZ3VyYXRpb24uXG4gICAgI1xuICAgICMgTm90ZTogdGhpcyBjb25maWd1cmF0aW9uIGlzIG9ubHkgdXNlZCBpbiBjYXNlIHRoZSBnYXRld2F5IGlzIHVzaW5nIHRoZVxuICAgICMgQ2hpcnBTdGFjayBDb25jZW50cmF0b3JkIGRhZW1vbi4gSW4gYW55IG90aGVyIGNhc2UsIHRoaXMgY29uZmlndXJhdGlvbiBcbiAgICAjIGlzIGlnbm9yZWQuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTQ3NjcwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9NDc2OTAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT00NzcxMDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTQ3NzMwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9NDc3NTAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT00Nzc3MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTQ3NzkwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9NDc4MTAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuXG4gICMgUmVnaW9uIHNwZWNpZmljIG5ldHdvcmsgY29uZmlndXJhdGlvbi5cbiAgW3JlZ2lvbnMubmV0d29ya11cbiAgICBcbiAgICAjIEluc3RhbGxhdGlvbiBtYXJnaW4gKGRCKSB1c2VkIGJ5IHRoZSBBRFIgZW5naW5lLlxuICAgICNcbiAgICAjIEEgaGlnaGVyIG51bWJlciBtZWFucyB0aGF0IHRoZSBuZXR3b3JrLXNlcnZlciB3aWxsIGtlZXAgbW9yZSBtYXJnaW4sXG4gICAgIyByZXN1bHRpbmcgaW4gYSBsb3dlciBkYXRhLXJhdGUgYnV0IGRlY3JlYXNpbmcgdGhlIGNoYW5jZSB0aGF0IHRoZVxuICAgICMgZGV2aWNlIGdldHMgZGlzY29ubmVjdGVkIGJlY2F1c2UgaXQgaXMgdW5hYmxlIHRvIHJlYWNoIG9uZSBvZiB0aGVcbiAgICAjIHN1cnJvdW5kZWQgZ2F0ZXdheXMuXG4gICAgaW5zdGFsbGF0aW9uX21hcmdpbj0xMFxuXG4gICAgIyBSWCB3aW5kb3cgKENsYXNzLUEpLlxuICAgICNcbiAgICAjIFNldCB0aGlzIHRvOlxuICAgICMgMDogUlgxIC8gUlgyXG4gICAgIyAxOiBSWDEgb25seVxuICAgICMgMjogUlgyIG9ubHlcbiAgICByeF93aW5kb3c9MFxuXG4gICAgIyBSWDEgZGVsYXkgKDEgLSAxNSBzZWNvbmRzKS5cbiAgICByeDFfZGVsYXk9MVxuXG4gICAgIyBSWDEgZGF0YS1yYXRlIG9mZnNldFxuICAgIHJ4MV9kcl9vZmZzZXQ9MFxuXG4gICAgIyBSWDIgZGF0YS1yYXRlXG4gICAgcngyX2RyPTBcblxuICAgICMgUlgyIGZyZXF1ZW5jeSAoSHopXG4gICAgcngyX2ZyZXF1ZW5jeT01MDUzMDAwMDBcblxuICAgICMgUHJlZmVyIFJYMiBvbiBSWDEgZGF0YS1yYXRlIGxlc3MgdGhhbi5cbiAgICAjXG4gICAgIyBQcmVmZXIgUlgyIG92ZXIgUlgxIGJhc2VkIG9uIHRoZSBSWDEgZGF0YS1yYXRlLiBXaGVuIHRoZSBSWDEgZGF0YS1yYXRlXG4gICAgIyBpcyBzbWFsbGVyIHRoYW4gdGhlIGNvbmZpZ3VyZWQgdmFsdWUsIHRoZW4gdGhlIE5ldHdvcmsgU2VydmVyIHdpbGxcbiAgICAjIGZpcnN0IHRyeSB0byBzY2hlZHVsZSB0aGUgZG93bmxpbmsgZm9yIFJYMiwgZmFpbGluZyB0aGF0IChlLmcuIHRoZSBnYXRld2F5XG4gICAgIyBoYXMgYWxyZWFkeSBhIHBheWxvYWQgc2NoZWR1bGVkIGF0IHRoZSBSWDIgdGltaW5nKSBpdCB3aWxsIHRyeSBSWDEuXG4gICAgcngyX3ByZWZlcl9vbl9yeDFfZHJfbHQ9MFxuXG4gICAgIyBQcmVmZXIgUlgyIG9uIGxpbmsgYnVkZ2V0LlxuICAgICNcbiAgICAjIFdoZW4gdGhlIGxpbmstYnVkZ2V0IGlzIGJldHRlciBmb3IgUlgyIHRoYW4gZm9yIFJYMSwgdGhlIE5ldHdvcmsgU2VydmVyIHdpbGwgZmlyc3RcbiAgICAjIHRyeSB0byBzY2hlZHVsZSB0aGUgZG93bmxpbmsgaW4gUlgyLCBmYWlsaW5nIHRoYXQgaXQgd2lsbCB0cnkgUlgxLlxuICAgIHJ4Ml9wcmVmZXJfb25fbGlua19idWRnZXQ9ZmFsc2VcblxuICAgICMgRG93bmxpbmsgVFggUG93ZXIgKGRCbSlcbiAgICAjXG4gICAgIyBXaGVuIHNldCB0byAtMSwgdGhlIGRvd25saW5rIFRYIFBvd2VyIGZyb20gdGhlIGNvbmZpZ3VyZWQgYmFuZCB3aWxsXG4gICAgIyBiZSB1c2VkLlxuICAgICNcbiAgICAjIFBsZWFzZSBjb25zdWx0IHRoZSBMb1JhV0FOIFJlZ2lvbmFsIFBhcmFtZXRlcnMgYW5kIGxvY2FsIHJlZ3VsYXRpb25zXG4gICAgIyBmb3IgdmFsaWQgYW5kIGxlZ2FsIG9wdGlvbnMuIE5vdGUgdGhhdCB0aGUgY29uZmlndXJlZCBUWCBQb3dlciBtdXN0IGJlXG4gICAgIyBzdXBwb3J0ZWQgYnkgeW91ciBnYXRld2F5KHMpLlxuICAgIGRvd25saW5rX3R4X3Bvd2VyPS0xXG5cbiAgICAjIEFEUiBpcyBkaXNhYmxlZC5cbiAgICBhZHJfZGlzYWJsZWQ9ZmFsc2VcblxuICAgICMgTWluaW11bSBkYXRhLXJhdGUuXG4gICAgbWluX2RyPTBcblxuICAgICMgTWF4aW11bSBkYXRhLXJhdGUuXG4gICAgbWF4X2RyPTVcblxuICAgICMgRW5hYmxlZCB1cGxpbmsgY2hhbm5lbHMuXG4gICAgI1xuICAgICMgVXNlIHRoaXMgd2hlbiBvbnkgYSBzdWItc2V0IG9mIHRoZSBieSBkZWZhdWx0IGVuYWJsZWQgY2hhbm5lbHMgYXJlIGJlaW5nXG4gICAgIyB1c2VkLiBGb3IgZXhhbXBsZSB3aGVuIG9ubHkgdXNpbmcgdGhlIGZpcnN0IDggY2hhbm5lbHMgb2YgdGhlIFVTIGJhbmQuXG4gICAgIyBOb3RlOiB3aGVuIGxlZnQgYmxhbmsgLyBlbXB0eSBhcnJheSwgYWxsIGNoYW5uZWxzIHdpbGwgYmUgZW5hYmxlZC5cbiAgICBlbmFibGVkX3VwbGlua19jaGFubmVscz1bMzIsIDMzLCAzNCwgMzUsIDM2LCAzNywgMzgsIDM5XVxuXG5cbiAgICAjIFJlam9pbi1yZXF1ZXN0IGNvbmZpZ3VyYXRpb24gKExvUmFXQU4gMS4xKVxuICAgIFtyZWdpb25zLm5ldHdvcmsucmVqb2luX3JlcXVlc3RdXG5cbiAgICAgICMgUmVxdWVzdCBkZXZpY2VzIHRvIHBlcmlvZGljYWxseSBzZW5kIHJlam9pbi1yZXF1ZXN0cy5cbiAgICAgIGVuYWJsZWQ9ZmFsc2VcblxuICAgICAgIyBUaGUgZGV2aWNlIG11c3Qgc2VuZCBhIHJlam9pbi1yZXF1ZXN0IHR5cGUgMCBhdCBsZWFzdCBldmVyeSAyXihtYXhfY291bnRfbiArIDQpXG4gICAgICAjIHVwbGluayBtZXNzYWdlcy4gVmFsaWQgdmFsdWVzIGFyZSAwIHRvIDE1LlxuICAgICAgbWF4X2NvdW50X249MFxuXG4gICAgICAjIFRoZSBkZXZpY2UgbXVzdCBzZW5kIGEgcmVqb2luLXJlcXVlc3QgdHlwZSAwIGF0IGxlYXN0IGV2ZXJ5IDJeKG1heF90aW1lX24gKyAxMClcbiAgICAgICMgc2Vjb25kcy4gVmFsaWQgdmFsdWVzIGFyZSAwIHRvIDE1LlxuICAgICAgI1xuICAgICAgIyAwICA9IHJvdWdobHkgMTcgbWludXRlc1xuICAgICAgIyAxNSA9IGFib3V0IDEgeWVhclxuICAgICAgbWF4X3RpbWVfbj0wXG4gICAgXG5cbiAgICAjIENsYXNzLUIgY29uZmlndXJhdGlvbi5cbiAgICBbcmVnaW9ucy5uZXR3b3JrLmNsYXNzX2JdXG5cbiAgICAgICMgUGluZy1zbG90IGRhdGEtcmF0ZS4gXG4gICAgICBwaW5nX3Nsb3RfZHI9MlxuXG4gICAgICAjIFBpbmctc2xvdCBmcmVxdWVuY3kgKEh6KVxuICAgICAgI1xuICAgICAgIyBzZXQgdGhpcyB0byAwIHRvIHVzZSB0aGUgZGVmYXVsdCBmcmVxdWVuY3kgcGxhbiBmb3IgdGhlIGNvbmZpZ3VyZWQgcmVnaW9uXG4gICAgICAjICh3aGljaCBjb3VsZCBiZSBmcmVxdWVuY3kgaG9wcGluZykuXG4gICAgICBwaW5nX3Nsb3RfZnJlcXVlbmN5PTBcblwiXCJcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuc2VydmljZU5hbWUgPSBcImNoaXJwc3RhY2tcIlxuZmlsZVBhdGggPSBcIi9jaGlycHN0YWNrL3JlZ2lvbl9jbjQ3MF81LnRvbWxcIlxuY29udGVudCA9IFwiXCJcIlxuIyBUaGlzIGZpbGUgY29udGFpbnMgYW4gZXhhbXBsZSBDTjQ3MCBleGFtcGxlIChjaGFubmVscyA0MC00NykuXG5bW3JlZ2lvbnNdXVxuXG4gICMgSUQgaXMgYW4gdXNlLWRlZmluZWQgaWRlbnRpZmllciBmb3IgdGhpcyByZWdpb24uXG4gIGlkPVwiY240NzBfNVwiXG5cbiAgIyBEZXNjcmlwdGlvbiBpcyBhIHNob3J0IGRlc2NyaXB0aW9uIGZvciB0aGlzIHJlZ2lvbi5cbiAgZGVzY3JpcHRpb249XCJDTjQ3MCAoY2hhbm5lbHMgNDAtNDcpXCJcblxuICAjIENvbW1vbi1uYW1lIHJlZmVycyB0byB0aGUgY29tbW9uLW5hbWUgb2YgdGhpcyByZWdpb24gYXMgZGVmaW5lZCBieVxuICAjIHRoZSBMb1JhIEFsbGlhbmNlLlxuICBjb21tb25fbmFtZT1cIkNONDcwXCJcblxuXG4gICMgR2F0ZXdheSBjb25maWd1cmF0aW9uLlxuICBbcmVnaW9ucy5nYXRld2F5XVxuXG4gICAgIyBGb3JjZSBnYXRld2F5cyBhcyBwcml2YXRlLlxuICAgICNcbiAgICAjIElmIGVuYWJsZWQsIGdhdGV3YXlzIGNhbiBvbmx5IGJlIHVzZWQgYnkgZGV2aWNlcyB1bmRlciB0aGUgc2FtZSB0ZW5hbnQuXG4gICAgZm9yY2VfZ3dzX3ByaXZhdGU9ZmFsc2VcblxuICAgIFxuICAgICMgR2F0ZXdheSBiYWNrZW5kIGNvbmZpZ3VyYXRpb24uXG4gICAgW3JlZ2lvbnMuZ2F0ZXdheS5iYWNrZW5kXVxuXG4gICAgICAjIFRoZSBlbmFibGVkIGJhY2tlbmQgdHlwZS5cbiAgICAgIGVuYWJsZWQ9XCJtcXR0XCJcblxuICAgICAgIyBNUVRUIGNvbmZpZ3VyYXRpb24uXG4gICAgICBbcmVnaW9ucy5nYXRld2F5LmJhY2tlbmQubXF0dF1cblxuICAgICAgICAjIFRvcGljIHByZWZpeC5cbiAgICAgICAgI1xuICAgICAgICAjIFRoZSB0b3BpYyBwcmVmaXggY2FuIGJlIHVzZWQgdG8gZGVmaW5lIHRoZSByZWdpb24gb2YgdGhlIGdhdGV3YXkuXG4gICAgICAgICMgTm90ZSwgdGhlcmUgaXMgbm8gbmVlZCB0byBhZGQgYSB0cmFpbGluZyAnLycgdG8gdGhlIHByZWZpeC4gVGhlIHRyYWlsaW5nXG4gICAgICAgICMgJy8nIGlzIGF1dG9tYXRpY2FsbHkgYWRkZWQgdG8gdGhlIHByZWZpeCBpZiBpdCBpcyBjb25maWd1cmVkLlxuICAgICAgICB0b3BpY19wcmVmaXg9XCJjbjQ3MF81XCJcblxuICAgICAgICAjIE1RVFQgc2VydmVyIChlLmcuIHNjaGVtZTovL2hvc3Q6cG9ydCB3aGVyZSBzY2hlbWUgaXMgdGNwLCBzc2wgb3Igd3MpXG4gICAgICAgIHNlcnZlcj1cInRjcDovL21vc3F1aXR0bzoxODgzXCJcblxuICAgICAgICAjIENvbm5lY3Qgd2l0aCB0aGUgZ2l2ZW4gdXNlcm5hbWUgKG9wdGlvbmFsKVxuICAgICAgICB1c2VybmFtZT1cIlwiXG5cbiAgICAgICAgIyBDb25uZWN0IHdpdGggdGhlIGdpdmVuIHBhc3N3b3JkIChvcHRpb25hbClcbiAgICAgICAgcGFzc3dvcmQ9XCJcIlxuXG4gICAgICAgICMgUXVhbGl0eSBvZiBzZXJ2aWNlIGxldmVsXG4gICAgICAgICNcbiAgICAgICAgIyAwOiBhdCBtb3N0IG9uY2VcbiAgICAgICAgIyAxOiBhdCBsZWFzdCBvbmNlXG4gICAgICAgICMgMjogZXhhY3RseSBvbmNlXG4gICAgICAgICNcbiAgICAgICAgIyBOb3RlOiBhbiBpbmNyZWFzZSBvZiB0aGlzIHZhbHVlIHdpbGwgZGVjcmVhc2UgdGhlIHBlcmZvcm1hbmNlLlxuICAgICAgICAjIEZvciBtb3JlIGluZm9ybWF0aW9uOiBodHRwczovL3d3dy5oaXZlbXEuY29tL2Jsb2cvbXF0dC1lc3NlbnRpYWxzLXBhcnQtNi1tcXR0LXF1YWxpdHktb2Ytc2VydmljZS1sZXZlbHNcbiAgICAgICAgcW9zPTBcblxuICAgICAgICAjIENsZWFuIHNlc3Npb25cbiAgICAgICAgI1xuICAgICAgICAjIFNldCB0aGUgXCJjbGVhbiBzZXNzaW9uXCIgZmxhZyBpbiB0aGUgY29ubmVjdCBtZXNzYWdlIHdoZW4gdGhpcyBjbGllbnRcbiAgICAgICAgIyBjb25uZWN0cyB0byBhbiBNUVRUIGJyb2tlci4gQnkgc2V0dGluZyB0aGlzIGZsYWcgeW91IGFyZSBpbmRpY2F0aW5nXG4gICAgICAgICMgdGhhdCBubyBtZXNzYWdlcyBzYXZlZCBieSB0aGUgYnJva2VyIGZvciB0aGlzIGNsaWVudCBzaG91bGQgYmUgZGVsaXZlcmVkLlxuICAgICAgICBjbGVhbl9zZXNzaW9uPWZhbHNlXG5cbiAgICAgICAgIyBDbGllbnQgSURcbiAgICAgICAgI1xuICAgICAgICAjIFNldCB0aGUgY2xpZW50IGlkIHRvIGJlIHVzZWQgYnkgdGhpcyBjbGllbnQgd2hlbiBjb25uZWN0aW5nIHRvIHRoZSBNUVRUXG4gICAgICAgICMgYnJva2VyLiBBIGNsaWVudCBpZCBtdXN0IGJlIG5vIGxvbmdlciB0aGFuIDIzIGNoYXJhY3RlcnMuIElmIGxlZnQgYmxhbmssXG4gICAgICAgICMgYSByYW5kb20gaWQgd2lsbCBiZSBnZW5lcmF0ZWQgYnkgQ2hpcnBTdGFjay5cbiAgICAgICAgY2xpZW50X2lkPVwiXCJcblxuICAgICAgICAjIEtlZXAgYWxpdmUgaW50ZXJ2YWwuXG4gICAgICAgICNcbiAgICAgICAgIyBUaGlzIGRlZmluZXMgdGhlIG1heGltdW0gdGltZSB0aGF0IHRoYXQgc2hvdWxkIHBhc3Mgd2l0aG91dCBjb21tdW5pY2F0aW9uXG4gICAgICAgICMgYmV0d2VlbiB0aGUgY2xpZW50IGFuZCBzZXJ2ZXIuXG4gICAgICAgIGtlZXBfYWxpdmVfaW50ZXJ2YWw9XCIzMHNcIlxuXG4gICAgICAgICMgQ0EgY2VydGlmaWNhdGUgZmlsZSAob3B0aW9uYWwpXG4gICAgICAgICNcbiAgICAgICAgIyBVc2UgdGhpcyB3aGVuIHNldHRpbmcgdXAgYSBzZWN1cmUgY29ubmVjdGlvbiAod2hlbiBzZXJ2ZXIgdXNlcyBzc2w6Ly8uLi4pXG4gICAgICAgICMgYnV0IHRoZSBjZXJ0aWZpY2F0ZSB1c2VkIGJ5IHRoZSBzZXJ2ZXIgaXMgbm90IHRydXN0ZWQgYnkgYW55IENBIGNlcnRpZmljYXRlXG4gICAgICAgICMgb24gdGhlIHNlcnZlciAoZS5nLiB3aGVuIHNlbGYgZ2VuZXJhdGVkKS5cbiAgICAgICAgY2FfY2VydD1cIlwiXG5cbiAgICAgICAgIyBUTFMgY2VydGlmaWNhdGUgZmlsZSAob3B0aW9uYWwpXG4gICAgICAgIHRsc19jZXJ0PVwiXCJcblxuICAgICAgICAjIFRMUyBrZXkgZmlsZSAob3B0aW9uYWwpXG4gICAgICAgIHRsc19rZXk9XCJcIlxuXG5cbiAgICAjIEdhdGV3YXkgY2hhbm5lbCBjb25maWd1cmF0aW9uLlxuICAgICNcbiAgICAjIE5vdGU6IHRoaXMgY29uZmlndXJhdGlvbiBpcyBvbmx5IHVzZWQgaW4gY2FzZSB0aGUgZ2F0ZXdheSBpcyB1c2luZyB0aGVcbiAgICAjIENoaXJwU3RhY2sgQ29uY2VudHJhdG9yZCBkYWVtb24uIEluIGFueSBvdGhlciBjYXNlLCB0aGlzIGNvbmZpZ3VyYXRpb24gXG4gICAgIyBpcyBpZ25vcmVkLlxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT00NzgzMDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTQ3ODUwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9NDc4NzAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT00Nzg5MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTQ3OTEwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9NDc5MzAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT00Nzk1MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTQ3OTcwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cblxuICAjIFJlZ2lvbiBzcGVjaWZpYyBuZXR3b3JrIGNvbmZpZ3VyYXRpb24uXG4gIFtyZWdpb25zLm5ldHdvcmtdXG4gICAgXG4gICAgIyBJbnN0YWxsYXRpb24gbWFyZ2luIChkQikgdXNlZCBieSB0aGUgQURSIGVuZ2luZS5cbiAgICAjXG4gICAgIyBBIGhpZ2hlciBudW1iZXIgbWVhbnMgdGhhdCB0aGUgbmV0d29yay1zZXJ2ZXIgd2lsbCBrZWVwIG1vcmUgbWFyZ2luLFxuICAgICMgcmVzdWx0aW5nIGluIGEgbG93ZXIgZGF0YS1yYXRlIGJ1dCBkZWNyZWFzaW5nIHRoZSBjaGFuY2UgdGhhdCB0aGVcbiAgICAjIGRldmljZSBnZXRzIGRpc2Nvbm5lY3RlZCBiZWNhdXNlIGl0IGlzIHVuYWJsZSB0byByZWFjaCBvbmUgb2YgdGhlXG4gICAgIyBzdXJyb3VuZGVkIGdhdGV3YXlzLlxuICAgIGluc3RhbGxhdGlvbl9tYXJnaW49MTBcblxuICAgICMgUlggd2luZG93IChDbGFzcy1BKS5cbiAgICAjXG4gICAgIyBTZXQgdGhpcyB0bzpcbiAgICAjIDA6IFJYMSAvIFJYMlxuICAgICMgMTogUlgxIG9ubHlcbiAgICAjIDI6IFJYMiBvbmx5XG4gICAgcnhfd2luZG93PTBcblxuICAgICMgUlgxIGRlbGF5ICgxIC0gMTUgc2Vjb25kcykuXG4gICAgcngxX2RlbGF5PTFcblxuICAgICMgUlgxIGRhdGEtcmF0ZSBvZmZzZXRcbiAgICByeDFfZHJfb2Zmc2V0PTBcblxuICAgICMgUlgyIGRhdGEtcmF0ZVxuICAgIHJ4Ml9kcj0wXG5cbiAgICAjIFJYMiBmcmVxdWVuY3kgKEh6KVxuICAgIHJ4Ml9mcmVxdWVuY3k9NTA1MzAwMDAwXG5cbiAgICAjIFByZWZlciBSWDIgb24gUlgxIGRhdGEtcmF0ZSBsZXNzIHRoYW4uXG4gICAgI1xuICAgICMgUHJlZmVyIFJYMiBvdmVyIFJYMSBiYXNlZCBvbiB0aGUgUlgxIGRhdGEtcmF0ZS4gV2hlbiB0aGUgUlgxIGRhdGEtcmF0ZVxuICAgICMgaXMgc21hbGxlciB0aGFuIHRoZSBjb25maWd1cmVkIHZhbHVlLCB0aGVuIHRoZSBOZXR3b3JrIFNlcnZlciB3aWxsXG4gICAgIyBmaXJzdCB0cnkgdG8gc2NoZWR1bGUgdGhlIGRvd25saW5rIGZvciBSWDIsIGZhaWxpbmcgdGhhdCAoZS5nLiB0aGUgZ2F0ZXdheVxuICAgICMgaGFzIGFscmVhZHkgYSBwYXlsb2FkIHNjaGVkdWxlZCBhdCB0aGUgUlgyIHRpbWluZykgaXQgd2lsbCB0cnkgUlgxLlxuICAgIHJ4Ml9wcmVmZXJfb25fcngxX2RyX2x0PTBcblxuICAgICMgUHJlZmVyIFJYMiBvbiBsaW5rIGJ1ZGdldC5cbiAgICAjXG4gICAgIyBXaGVuIHRoZSBsaW5rLWJ1ZGdldCBpcyBiZXR0ZXIgZm9yIFJYMiB0aGFuIGZvciBSWDEsIHRoZSBOZXR3b3JrIFNlcnZlciB3aWxsIGZpcnN0XG4gICAgIyB0cnkgdG8gc2NoZWR1bGUgdGhlIGRvd25saW5rIGluIFJYMiwgZmFpbGluZyB0aGF0IGl0IHdpbGwgdHJ5IFJYMS5cbiAgICByeDJfcHJlZmVyX29uX2xpbmtfYnVkZ2V0PWZhbHNlXG5cbiAgICAjIERvd25saW5rIFRYIFBvd2VyIChkQm0pXG4gICAgI1xuICAgICMgV2hlbiBzZXQgdG8gLTEsIHRoZSBkb3dubGluayBUWCBQb3dlciBmcm9tIHRoZSBjb25maWd1cmVkIGJhbmQgd2lsbFxuICAgICMgYmUgdXNlZC5cbiAgICAjXG4gICAgIyBQbGVhc2UgY29uc3VsdCB0aGUgTG9SYVdBTiBSZWdpb25hbCBQYXJhbWV0ZXJzIGFuZCBsb2NhbCByZWd1bGF0aW9uc1xuICAgICMgZm9yIHZhbGlkIGFuZCBsZWdhbCBvcHRpb25zLiBOb3RlIHRoYXQgdGhlIGNvbmZpZ3VyZWQgVFggUG93ZXIgbXVzdCBiZVxuICAgICMgc3VwcG9ydGVkIGJ5IHlvdXIgZ2F0ZXdheShzKS5cbiAgICBkb3dubGlua190eF9wb3dlcj0tMVxuXG4gICAgIyBBRFIgaXMgZGlzYWJsZWQuXG4gICAgYWRyX2Rpc2FibGVkPWZhbHNlXG5cbiAgICAjIE1pbmltdW0gZGF0YS1yYXRlLlxuICAgIG1pbl9kcj0wXG5cbiAgICAjIE1heGltdW0gZGF0YS1yYXRlLlxuICAgIG1heF9kcj01XG5cbiAgICAjIEVuYWJsZWQgdXBsaW5rIGNoYW5uZWxzLlxuICAgICNcbiAgICAjIFVzZSB0aGlzIHdoZW4gb255IGEgc3ViLXNldCBvZiB0aGUgYnkgZGVmYXVsdCBlbmFibGVkIGNoYW5uZWxzIGFyZSBiZWluZ1xuICAgICMgdXNlZC4gRm9yIGV4YW1wbGUgd2hlbiBvbmx5IHVzaW5nIHRoZSBmaXJzdCA4IGNoYW5uZWxzIG9mIHRoZSBVUyBiYW5kLlxuICAgICMgTm90ZTogd2hlbiBsZWZ0IGJsYW5rIC8gZW1wdHkgYXJyYXksIGFsbCBjaGFubmVscyB3aWxsIGJlIGVuYWJsZWQuXG4gICAgZW5hYmxlZF91cGxpbmtfY2hhbm5lbHM9WzQwLCA0MSwgNDIsIDQzLCA0NCwgNDUsIDQ2LCA0N11cblxuXG4gICAgIyBSZWpvaW4tcmVxdWVzdCBjb25maWd1cmF0aW9uIChMb1JhV0FOIDEuMSlcbiAgICBbcmVnaW9ucy5uZXR3b3JrLnJlam9pbl9yZXF1ZXN0XVxuXG4gICAgICAjIFJlcXVlc3QgZGV2aWNlcyB0byBwZXJpb2RpY2FsbHkgc2VuZCByZWpvaW4tcmVxdWVzdHMuXG4gICAgICBlbmFibGVkPWZhbHNlXG5cbiAgICAgICMgVGhlIGRldmljZSBtdXN0IHNlbmQgYSByZWpvaW4tcmVxdWVzdCB0eXBlIDAgYXQgbGVhc3QgZXZlcnkgMl4obWF4X2NvdW50X24gKyA0KVxuICAgICAgIyB1cGxpbmsgbWVzc2FnZXMuIFZhbGlkIHZhbHVlcyBhcmUgMCB0byAxNS5cbiAgICAgIG1heF9jb3VudF9uPTBcblxuICAgICAgIyBUaGUgZGV2aWNlIG11c3Qgc2VuZCBhIHJlam9pbi1yZXF1ZXN0IHR5cGUgMCBhdCBsZWFzdCBldmVyeSAyXihtYXhfdGltZV9uICsgMTApXG4gICAgICAjIHNlY29uZHMuIFZhbGlkIHZhbHVlcyBhcmUgMCB0byAxNS5cbiAgICAgICNcbiAgICAgICMgMCAgPSByb3VnaGx5IDE3IG1pbnV0ZXNcbiAgICAgICMgMTUgPSBhYm91dCAxIHllYXJcbiAgICAgIG1heF90aW1lX249MFxuICAgIFxuXG4gICAgIyBDbGFzcy1CIGNvbmZpZ3VyYXRpb24uXG4gICAgW3JlZ2lvbnMubmV0d29yay5jbGFzc19iXVxuXG4gICAgICAjIFBpbmctc2xvdCBkYXRhLXJhdGUuIFxuICAgICAgcGluZ19zbG90X2RyPTJcblxuICAgICAgIyBQaW5nLXNsb3QgZnJlcXVlbmN5IChIeilcbiAgICAgICNcbiAgICAgICMgc2V0IHRoaXMgdG8gMCB0byB1c2UgdGhlIGRlZmF1bHQgZnJlcXVlbmN5IHBsYW4gZm9yIHRoZSBjb25maWd1cmVkIHJlZ2lvblxuICAgICAgIyAod2hpY2ggY291bGQgYmUgZnJlcXVlbmN5IGhvcHBpbmcpLlxuICAgICAgcGluZ19zbG90X2ZyZXF1ZW5jeT0wXG5cIlwiXCJcblxuW1tjb25maWcubW91bnRzXV1cbnNlcnZpY2VOYW1lID0gXCJjaGlycHN0YWNrXCJcbmZpbGVQYXRoID0gXCIvY2hpcnBzdGFjay9yZWdpb25fY240NzBfNi50b21sXCJcbmNvbnRlbnQgPSBcIlwiXCJcbiMgVGhpcyBmaWxlIGNvbnRhaW5zIGFuIGV4YW1wbGUgQ040NzAgZXhhbXBsZSAoY2hhbm5lbHMgNDgtNTUpLlxuW1tyZWdpb25zXV1cblxuICAjIElEIGlzIGFuIHVzZS1kZWZpbmVkIGlkZW50aWZpZXIgZm9yIHRoaXMgcmVnaW9uLlxuICBpZD1cImNuNDcwXzZcIlxuXG4gICMgRGVzY3JpcHRpb24gaXMgYSBzaG9ydCBkZXNjcmlwdGlvbiBmb3IgdGhpcyByZWdpb24uXG4gIGRlc2NyaXB0aW9uPVwiQ040NzAgKGNoYW5uZWxzIDQ4LTU1KVwiXG5cbiAgIyBDb21tb24tbmFtZSByZWZlcnMgdG8gdGhlIGNvbW1vbi1uYW1lIG9mIHRoaXMgcmVnaW9uIGFzIGRlZmluZWQgYnlcbiAgIyB0aGUgTG9SYSBBbGxpYW5jZS5cbiAgY29tbW9uX25hbWU9XCJDTjQ3MFwiXG5cblxuICAjIEdhdGV3YXkgY29uZmlndXJhdGlvbi5cbiAgW3JlZ2lvbnMuZ2F0ZXdheV1cblxuICAgICMgRm9yY2UgZ2F0ZXdheXMgYXMgcHJpdmF0ZS5cbiAgICAjXG4gICAgIyBJZiBlbmFibGVkLCBnYXRld2F5cyBjYW4gb25seSBiZSB1c2VkIGJ5IGRldmljZXMgdW5kZXIgdGhlIHNhbWUgdGVuYW50LlxuICAgIGZvcmNlX2d3c19wcml2YXRlPWZhbHNlXG5cbiAgICBcbiAgICAjIEdhdGV3YXkgYmFja2VuZCBjb25maWd1cmF0aW9uLlxuICAgIFtyZWdpb25zLmdhdGV3YXkuYmFja2VuZF1cblxuICAgICAgIyBUaGUgZW5hYmxlZCBiYWNrZW5kIHR5cGUuXG4gICAgICBlbmFibGVkPVwibXF0dFwiXG5cbiAgICAgICMgTVFUVCBjb25maWd1cmF0aW9uLlxuICAgICAgW3JlZ2lvbnMuZ2F0ZXdheS5iYWNrZW5kLm1xdHRdXG5cbiAgICAgICAgIyBUb3BpYyBwcmVmaXguXG4gICAgICAgICNcbiAgICAgICAgIyBUaGUgdG9waWMgcHJlZml4IGNhbiBiZSB1c2VkIHRvIGRlZmluZSB0aGUgcmVnaW9uIG9mIHRoZSBnYXRld2F5LlxuICAgICAgICAjIE5vdGUsIHRoZXJlIGlzIG5vIG5lZWQgdG8gYWRkIGEgdHJhaWxpbmcgJy8nIHRvIHRoZSBwcmVmaXguIFRoZSB0cmFpbGluZ1xuICAgICAgICAjICcvJyBpcyBhdXRvbWF0aWNhbGx5IGFkZGVkIHRvIHRoZSBwcmVmaXggaWYgaXQgaXMgY29uZmlndXJlZC5cbiAgICAgICAgdG9waWNfcHJlZml4PVwiY240NzBfNlwiXG5cbiAgICAgICAgIyBNUVRUIHNlcnZlciAoZS5nLiBzY2hlbWU6Ly9ob3N0OnBvcnQgd2hlcmUgc2NoZW1lIGlzIHRjcCwgc3NsIG9yIHdzKVxuICAgICAgICBzZXJ2ZXI9XCJ0Y3A6Ly9tb3NxdWl0dG86MTg4M1wiXG5cbiAgICAgICAgIyBDb25uZWN0IHdpdGggdGhlIGdpdmVuIHVzZXJuYW1lIChvcHRpb25hbClcbiAgICAgICAgdXNlcm5hbWU9XCJcIlxuXG4gICAgICAgICMgQ29ubmVjdCB3aXRoIHRoZSBnaXZlbiBwYXNzd29yZCAob3B0aW9uYWwpXG4gICAgICAgIHBhc3N3b3JkPVwiXCJcblxuICAgICAgICAjIFF1YWxpdHkgb2Ygc2VydmljZSBsZXZlbFxuICAgICAgICAjXG4gICAgICAgICMgMDogYXQgbW9zdCBvbmNlXG4gICAgICAgICMgMTogYXQgbGVhc3Qgb25jZVxuICAgICAgICAjIDI6IGV4YWN0bHkgb25jZVxuICAgICAgICAjXG4gICAgICAgICMgTm90ZTogYW4gaW5jcmVhc2Ugb2YgdGhpcyB2YWx1ZSB3aWxsIGRlY3JlYXNlIHRoZSBwZXJmb3JtYW5jZS5cbiAgICAgICAgIyBGb3IgbW9yZSBpbmZvcm1hdGlvbjogaHR0cHM6Ly93d3cuaGl2ZW1xLmNvbS9ibG9nL21xdHQtZXNzZW50aWFscy1wYXJ0LTYtbXF0dC1xdWFsaXR5LW9mLXNlcnZpY2UtbGV2ZWxzXG4gICAgICAgIHFvcz0wXG5cbiAgICAgICAgIyBDbGVhbiBzZXNzaW9uXG4gICAgICAgICNcbiAgICAgICAgIyBTZXQgdGhlIFwiY2xlYW4gc2Vzc2lvblwiIGZsYWcgaW4gdGhlIGNvbm5lY3QgbWVzc2FnZSB3aGVuIHRoaXMgY2xpZW50XG4gICAgICAgICMgY29ubmVjdHMgdG8gYW4gTVFUVCBicm9rZXIuIEJ5IHNldHRpbmcgdGhpcyBmbGFnIHlvdSBhcmUgaW5kaWNhdGluZ1xuICAgICAgICAjIHRoYXQgbm8gbWVzc2FnZXMgc2F2ZWQgYnkgdGhlIGJyb2tlciBmb3IgdGhpcyBjbGllbnQgc2hvdWxkIGJlIGRlbGl2ZXJlZC5cbiAgICAgICAgY2xlYW5fc2Vzc2lvbj1mYWxzZVxuXG4gICAgICAgICMgQ2xpZW50IElEXG4gICAgICAgICNcbiAgICAgICAgIyBTZXQgdGhlIGNsaWVudCBpZCB0byBiZSB1c2VkIGJ5IHRoaXMgY2xpZW50IHdoZW4gY29ubmVjdGluZyB0byB0aGUgTVFUVFxuICAgICAgICAjIGJyb2tlci4gQSBjbGllbnQgaWQgbXVzdCBiZSBubyBsb25nZXIgdGhhbiAyMyBjaGFyYWN0ZXJzLiBJZiBsZWZ0IGJsYW5rLFxuICAgICAgICAjIGEgcmFuZG9tIGlkIHdpbGwgYmUgZ2VuZXJhdGVkIGJ5IENoaXJwU3RhY2suXG4gICAgICAgIGNsaWVudF9pZD1cIlwiXG5cbiAgICAgICAgIyBLZWVwIGFsaXZlIGludGVydmFsLlxuICAgICAgICAjXG4gICAgICAgICMgVGhpcyBkZWZpbmVzIHRoZSBtYXhpbXVtIHRpbWUgdGhhdCB0aGF0IHNob3VsZCBwYXNzIHdpdGhvdXQgY29tbXVuaWNhdGlvblxuICAgICAgICAjIGJldHdlZW4gdGhlIGNsaWVudCBhbmQgc2VydmVyLlxuICAgICAgICBrZWVwX2FsaXZlX2ludGVydmFsPVwiMzBzXCJcblxuICAgICAgICAjIENBIGNlcnRpZmljYXRlIGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICAjXG4gICAgICAgICMgVXNlIHRoaXMgd2hlbiBzZXR0aW5nIHVwIGEgc2VjdXJlIGNvbm5lY3Rpb24gKHdoZW4gc2VydmVyIHVzZXMgc3NsOi8vLi4uKVxuICAgICAgICAjIGJ1dCB0aGUgY2VydGlmaWNhdGUgdXNlZCBieSB0aGUgc2VydmVyIGlzIG5vdCB0cnVzdGVkIGJ5IGFueSBDQSBjZXJ0aWZpY2F0ZVxuICAgICAgICAjIG9uIHRoZSBzZXJ2ZXIgKGUuZy4gd2hlbiBzZWxmIGdlbmVyYXRlZCkuXG4gICAgICAgIGNhX2NlcnQ9XCJcIlxuXG4gICAgICAgICMgVExTIGNlcnRpZmljYXRlIGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICB0bHNfY2VydD1cIlwiXG5cbiAgICAgICAgIyBUTFMga2V5IGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICB0bHNfa2V5PVwiXCJcblxuXG4gICAgIyBHYXRld2F5IGNoYW5uZWwgY29uZmlndXJhdGlvbi5cbiAgICAjXG4gICAgIyBOb3RlOiB0aGlzIGNvbmZpZ3VyYXRpb24gaXMgb25seSB1c2VkIGluIGNhc2UgdGhlIGdhdGV3YXkgaXMgdXNpbmcgdGhlXG4gICAgIyBDaGlycFN0YWNrIENvbmNlbnRyYXRvcmQgZGFlbW9uLiBJbiBhbnkgb3RoZXIgY2FzZSwgdGhpcyBjb25maWd1cmF0aW9uIFxuICAgICMgaXMgaWdub3JlZC5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9NDc5OTAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT00ODAxMDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTQ4MDMwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9NDgwNTAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT00ODA3MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTQ4MDkwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9NDgxMTAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT00ODEzMDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG5cbiAgIyBSZWdpb24gc3BlY2lmaWMgbmV0d29yayBjb25maWd1cmF0aW9uLlxuICBbcmVnaW9ucy5uZXR3b3JrXVxuICAgIFxuICAgICMgSW5zdGFsbGF0aW9uIG1hcmdpbiAoZEIpIHVzZWQgYnkgdGhlIEFEUiBlbmdpbmUuXG4gICAgI1xuICAgICMgQSBoaWdoZXIgbnVtYmVyIG1lYW5zIHRoYXQgdGhlIG5ldHdvcmstc2VydmVyIHdpbGwga2VlcCBtb3JlIG1hcmdpbixcbiAgICAjIHJlc3VsdGluZyBpbiBhIGxvd2VyIGRhdGEtcmF0ZSBidXQgZGVjcmVhc2luZyB0aGUgY2hhbmNlIHRoYXQgdGhlXG4gICAgIyBkZXZpY2UgZ2V0cyBkaXNjb25uZWN0ZWQgYmVjYXVzZSBpdCBpcyB1bmFibGUgdG8gcmVhY2ggb25lIG9mIHRoZVxuICAgICMgc3Vycm91bmRlZCBnYXRld2F5cy5cbiAgICBpbnN0YWxsYXRpb25fbWFyZ2luPTEwXG5cbiAgICAjIFJYIHdpbmRvdyAoQ2xhc3MtQSkuXG4gICAgI1xuICAgICMgU2V0IHRoaXMgdG86XG4gICAgIyAwOiBSWDEgLyBSWDJcbiAgICAjIDE6IFJYMSBvbmx5XG4gICAgIyAyOiBSWDIgb25seVxuICAgIHJ4X3dpbmRvdz0wXG5cbiAgICAjIFJYMSBkZWxheSAoMSAtIDE1IHNlY29uZHMpLlxuICAgIHJ4MV9kZWxheT0xXG5cbiAgICAjIFJYMSBkYXRhLXJhdGUgb2Zmc2V0XG4gICAgcngxX2RyX29mZnNldD0wXG5cbiAgICAjIFJYMiBkYXRhLXJhdGVcbiAgICByeDJfZHI9MFxuXG4gICAgIyBSWDIgZnJlcXVlbmN5IChIeilcbiAgICByeDJfZnJlcXVlbmN5PTUwNTMwMDAwMFxuXG4gICAgIyBQcmVmZXIgUlgyIG9uIFJYMSBkYXRhLXJhdGUgbGVzcyB0aGFuLlxuICAgICNcbiAgICAjIFByZWZlciBSWDIgb3ZlciBSWDEgYmFzZWQgb24gdGhlIFJYMSBkYXRhLXJhdGUuIFdoZW4gdGhlIFJYMSBkYXRhLXJhdGVcbiAgICAjIGlzIHNtYWxsZXIgdGhhbiB0aGUgY29uZmlndXJlZCB2YWx1ZSwgdGhlbiB0aGUgTmV0d29yayBTZXJ2ZXIgd2lsbFxuICAgICMgZmlyc3QgdHJ5IHRvIHNjaGVkdWxlIHRoZSBkb3dubGluayBmb3IgUlgyLCBmYWlsaW5nIHRoYXQgKGUuZy4gdGhlIGdhdGV3YXlcbiAgICAjIGhhcyBhbHJlYWR5IGEgcGF5bG9hZCBzY2hlZHVsZWQgYXQgdGhlIFJYMiB0aW1pbmcpIGl0IHdpbGwgdHJ5IFJYMS5cbiAgICByeDJfcHJlZmVyX29uX3J4MV9kcl9sdD0wXG5cbiAgICAjIFByZWZlciBSWDIgb24gbGluayBidWRnZXQuXG4gICAgI1xuICAgICMgV2hlbiB0aGUgbGluay1idWRnZXQgaXMgYmV0dGVyIGZvciBSWDIgdGhhbiBmb3IgUlgxLCB0aGUgTmV0d29yayBTZXJ2ZXIgd2lsbCBmaXJzdFxuICAgICMgdHJ5IHRvIHNjaGVkdWxlIHRoZSBkb3dubGluayBpbiBSWDIsIGZhaWxpbmcgdGhhdCBpdCB3aWxsIHRyeSBSWDEuXG4gICAgcngyX3ByZWZlcl9vbl9saW5rX2J1ZGdldD1mYWxzZVxuXG4gICAgIyBEb3dubGluayBUWCBQb3dlciAoZEJtKVxuICAgICNcbiAgICAjIFdoZW4gc2V0IHRvIC0xLCB0aGUgZG93bmxpbmsgVFggUG93ZXIgZnJvbSB0aGUgY29uZmlndXJlZCBiYW5kIHdpbGxcbiAgICAjIGJlIHVzZWQuXG4gICAgI1xuICAgICMgUGxlYXNlIGNvbnN1bHQgdGhlIExvUmFXQU4gUmVnaW9uYWwgUGFyYW1ldGVycyBhbmQgbG9jYWwgcmVndWxhdGlvbnNcbiAgICAjIGZvciB2YWxpZCBhbmQgbGVnYWwgb3B0aW9ucy4gTm90ZSB0aGF0IHRoZSBjb25maWd1cmVkIFRYIFBvd2VyIG11c3QgYmVcbiAgICAjIHN1cHBvcnRlZCBieSB5b3VyIGdhdGV3YXkocykuXG4gICAgZG93bmxpbmtfdHhfcG93ZXI9LTFcblxuICAgICMgQURSIGlzIGRpc2FibGVkLlxuICAgIGFkcl9kaXNhYmxlZD1mYWxzZVxuXG4gICAgIyBNaW5pbXVtIGRhdGEtcmF0ZS5cbiAgICBtaW5fZHI9MFxuXG4gICAgIyBNYXhpbXVtIGRhdGEtcmF0ZS5cbiAgICBtYXhfZHI9NVxuXG4gICAgIyBFbmFibGVkIHVwbGluayBjaGFubmVscy5cbiAgICAjXG4gICAgIyBVc2UgdGhpcyB3aGVuIG9ueSBhIHN1Yi1zZXQgb2YgdGhlIGJ5IGRlZmF1bHQgZW5hYmxlZCBjaGFubmVscyBhcmUgYmVpbmdcbiAgICAjIHVzZWQuIEZvciBleGFtcGxlIHdoZW4gb25seSB1c2luZyB0aGUgZmlyc3QgOCBjaGFubmVscyBvZiB0aGUgVVMgYmFuZC5cbiAgICAjIE5vdGU6IHdoZW4gbGVmdCBibGFuayAvIGVtcHR5IGFycmF5LCBhbGwgY2hhbm5lbHMgd2lsbCBiZSBlbmFibGVkLlxuICAgIGVuYWJsZWRfdXBsaW5rX2NoYW5uZWxzPVs0OCwgNDksIDUwLCA1MSwgNTIsIDUzLCA1NCwgNTVdXG5cblxuICAgICMgUmVqb2luLXJlcXVlc3QgY29uZmlndXJhdGlvbiAoTG9SYVdBTiAxLjEpXG4gICAgW3JlZ2lvbnMubmV0d29yay5yZWpvaW5fcmVxdWVzdF1cblxuICAgICAgIyBSZXF1ZXN0IGRldmljZXMgdG8gcGVyaW9kaWNhbGx5IHNlbmQgcmVqb2luLXJlcXVlc3RzLlxuICAgICAgZW5hYmxlZD1mYWxzZVxuXG4gICAgICAjIFRoZSBkZXZpY2UgbXVzdCBzZW5kIGEgcmVqb2luLXJlcXVlc3QgdHlwZSAwIGF0IGxlYXN0IGV2ZXJ5IDJeKG1heF9jb3VudF9uICsgNClcbiAgICAgICMgdXBsaW5rIG1lc3NhZ2VzLiBWYWxpZCB2YWx1ZXMgYXJlIDAgdG8gMTUuXG4gICAgICBtYXhfY291bnRfbj0wXG5cbiAgICAgICMgVGhlIGRldmljZSBtdXN0IHNlbmQgYSByZWpvaW4tcmVxdWVzdCB0eXBlIDAgYXQgbGVhc3QgZXZlcnkgMl4obWF4X3RpbWVfbiArIDEwKVxuICAgICAgIyBzZWNvbmRzLiBWYWxpZCB2YWx1ZXMgYXJlIDAgdG8gMTUuXG4gICAgICAjXG4gICAgICAjIDAgID0gcm91Z2hseSAxNyBtaW51dGVzXG4gICAgICAjIDE1ID0gYWJvdXQgMSB5ZWFyXG4gICAgICBtYXhfdGltZV9uPTBcbiAgICBcblxuICAgICMgQ2xhc3MtQiBjb25maWd1cmF0aW9uLlxuICAgIFtyZWdpb25zLm5ldHdvcmsuY2xhc3NfYl1cblxuICAgICAgIyBQaW5nLXNsb3QgZGF0YS1yYXRlLiBcbiAgICAgIHBpbmdfc2xvdF9kcj0yXG5cbiAgICAgICMgUGluZy1zbG90IGZyZXF1ZW5jeSAoSHopXG4gICAgICAjXG4gICAgICAjIHNldCB0aGlzIHRvIDAgdG8gdXNlIHRoZSBkZWZhdWx0IGZyZXF1ZW5jeSBwbGFuIGZvciB0aGUgY29uZmlndXJlZCByZWdpb25cbiAgICAgICMgKHdoaWNoIGNvdWxkIGJlIGZyZXF1ZW5jeSBob3BwaW5nKS5cbiAgICAgIHBpbmdfc2xvdF9mcmVxdWVuY3k9MFxuXCJcIlwiXG5cbltbY29uZmlnLm1vdW50c11dXG5zZXJ2aWNlTmFtZSA9IFwiY2hpcnBzdGFja1wiXG5maWxlUGF0aCA9IFwiL2NoaXJwc3RhY2svcmVnaW9uX2NuNDcwXzcudG9tbFwiXG5jb250ZW50ID0gXCJcIlwiXG4jIFRoaXMgZmlsZSBjb250YWlucyBhbiBleGFtcGxlIENONDcwIGV4YW1wbGUgKGNoYW5uZWxzIDU2LTYzKS5cbltbcmVnaW9uc11dXG5cbiAgIyBJRCBpcyBhbiB1c2UtZGVmaW5lZCBpZGVudGlmaWVyIGZvciB0aGlzIHJlZ2lvbi5cbiAgaWQ9XCJjbjQ3MF83XCJcblxuICAjIERlc2NyaXB0aW9uIGlzIGEgc2hvcnQgZGVzY3JpcHRpb24gZm9yIHRoaXMgcmVnaW9uLlxuICBkZXNjcmlwdGlvbj1cIkNONDcwIChjaGFubmVscyA1Ni02MylcIlxuXG4gICMgQ29tbW9uLW5hbWUgcmVmZXJzIHRvIHRoZSBjb21tb24tbmFtZSBvZiB0aGlzIHJlZ2lvbiBhcyBkZWZpbmVkIGJ5XG4gICMgdGhlIExvUmEgQWxsaWFuY2UuXG4gIGNvbW1vbl9uYW1lPVwiQ040NzBcIlxuXG5cbiAgIyBHYXRld2F5IGNvbmZpZ3VyYXRpb24uXG4gIFtyZWdpb25zLmdhdGV3YXldXG5cbiAgICAjIEZvcmNlIGdhdGV3YXlzIGFzIHByaXZhdGUuXG4gICAgI1xuICAgICMgSWYgZW5hYmxlZCwgZ2F0ZXdheXMgY2FuIG9ubHkgYmUgdXNlZCBieSBkZXZpY2VzIHVuZGVyIHRoZSBzYW1lIHRlbmFudC5cbiAgICBmb3JjZV9nd3NfcHJpdmF0ZT1mYWxzZVxuXG4gICAgXG4gICAgIyBHYXRld2F5IGJhY2tlbmQgY29uZmlndXJhdGlvbi5cbiAgICBbcmVnaW9ucy5nYXRld2F5LmJhY2tlbmRdXG5cbiAgICAgICMgVGhlIGVuYWJsZWQgYmFja2VuZCB0eXBlLlxuICAgICAgZW5hYmxlZD1cIm1xdHRcIlxuXG4gICAgICAjIE1RVFQgY29uZmlndXJhdGlvbi5cbiAgICAgIFtyZWdpb25zLmdhdGV3YXkuYmFja2VuZC5tcXR0XVxuXG4gICAgICAgICMgVG9waWMgcHJlZml4LlxuICAgICAgICAjXG4gICAgICAgICMgVGhlIHRvcGljIHByZWZpeCBjYW4gYmUgdXNlZCB0byBkZWZpbmUgdGhlIHJlZ2lvbiBvZiB0aGUgZ2F0ZXdheS5cbiAgICAgICAgIyBOb3RlLCB0aGVyZSBpcyBubyBuZWVkIHRvIGFkZCBhIHRyYWlsaW5nICcvJyB0byB0aGUgcHJlZml4LiBUaGUgdHJhaWxpbmdcbiAgICAgICAgIyAnLycgaXMgYXV0b21hdGljYWxseSBhZGRlZCB0byB0aGUgcHJlZml4IGlmIGl0IGlzIGNvbmZpZ3VyZWQuXG4gICAgICAgIHRvcGljX3ByZWZpeD1cImNuNDcwXzdcIlxuXG4gICAgICAgICMgTVFUVCBzZXJ2ZXIgKGUuZy4gc2NoZW1lOi8vaG9zdDpwb3J0IHdoZXJlIHNjaGVtZSBpcyB0Y3AsIHNzbCBvciB3cylcbiAgICAgICAgc2VydmVyPVwidGNwOi8vbW9zcXVpdHRvOjE4ODNcIlxuXG4gICAgICAgICMgQ29ubmVjdCB3aXRoIHRoZSBnaXZlbiB1c2VybmFtZSAob3B0aW9uYWwpXG4gICAgICAgIHVzZXJuYW1lPVwiXCJcblxuICAgICAgICAjIENvbm5lY3Qgd2l0aCB0aGUgZ2l2ZW4gcGFzc3dvcmQgKG9wdGlvbmFsKVxuICAgICAgICBwYXNzd29yZD1cIlwiXG5cbiAgICAgICAgIyBRdWFsaXR5IG9mIHNlcnZpY2UgbGV2ZWxcbiAgICAgICAgI1xuICAgICAgICAjIDA6IGF0IG1vc3Qgb25jZVxuICAgICAgICAjIDE6IGF0IGxlYXN0IG9uY2VcbiAgICAgICAgIyAyOiBleGFjdGx5IG9uY2VcbiAgICAgICAgI1xuICAgICAgICAjIE5vdGU6IGFuIGluY3JlYXNlIG9mIHRoaXMgdmFsdWUgd2lsbCBkZWNyZWFzZSB0aGUgcGVyZm9ybWFuY2UuXG4gICAgICAgICMgRm9yIG1vcmUgaW5mb3JtYXRpb246IGh0dHBzOi8vd3d3LmhpdmVtcS5jb20vYmxvZy9tcXR0LWVzc2VudGlhbHMtcGFydC02LW1xdHQtcXVhbGl0eS1vZi1zZXJ2aWNlLWxldmVsc1xuICAgICAgICBxb3M9MFxuXG4gICAgICAgICMgQ2xlYW4gc2Vzc2lvblxuICAgICAgICAjXG4gICAgICAgICMgU2V0IHRoZSBcImNsZWFuIHNlc3Npb25cIiBmbGFnIGluIHRoZSBjb25uZWN0IG1lc3NhZ2Ugd2hlbiB0aGlzIGNsaWVudFxuICAgICAgICAjIGNvbm5lY3RzIHRvIGFuIE1RVFQgYnJva2VyLiBCeSBzZXR0aW5nIHRoaXMgZmxhZyB5b3UgYXJlIGluZGljYXRpbmdcbiAgICAgICAgIyB0aGF0IG5vIG1lc3NhZ2VzIHNhdmVkIGJ5IHRoZSBicm9rZXIgZm9yIHRoaXMgY2xpZW50IHNob3VsZCBiZSBkZWxpdmVyZWQuXG4gICAgICAgIGNsZWFuX3Nlc3Npb249ZmFsc2VcblxuICAgICAgICAjIENsaWVudCBJRFxuICAgICAgICAjXG4gICAgICAgICMgU2V0IHRoZSBjbGllbnQgaWQgdG8gYmUgdXNlZCBieSB0aGlzIGNsaWVudCB3aGVuIGNvbm5lY3RpbmcgdG8gdGhlIE1RVFRcbiAgICAgICAgIyBicm9rZXIuIEEgY2xpZW50IGlkIG11c3QgYmUgbm8gbG9uZ2VyIHRoYW4gMjMgY2hhcmFjdGVycy4gSWYgbGVmdCBibGFuayxcbiAgICAgICAgIyBhIHJhbmRvbSBpZCB3aWxsIGJlIGdlbmVyYXRlZCBieSBDaGlycFN0YWNrLlxuICAgICAgICBjbGllbnRfaWQ9XCJcIlxuXG4gICAgICAgICMgS2VlcCBhbGl2ZSBpbnRlcnZhbC5cbiAgICAgICAgI1xuICAgICAgICAjIFRoaXMgZGVmaW5lcyB0aGUgbWF4aW11bSB0aW1lIHRoYXQgdGhhdCBzaG91bGQgcGFzcyB3aXRob3V0IGNvbW11bmljYXRpb25cbiAgICAgICAgIyBiZXR3ZWVuIHRoZSBjbGllbnQgYW5kIHNlcnZlci5cbiAgICAgICAga2VlcF9hbGl2ZV9pbnRlcnZhbD1cIjMwc1wiXG5cbiAgICAgICAgIyBDQSBjZXJ0aWZpY2F0ZSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgI1xuICAgICAgICAjIFVzZSB0aGlzIHdoZW4gc2V0dGluZyB1cCBhIHNlY3VyZSBjb25uZWN0aW9uICh3aGVuIHNlcnZlciB1c2VzIHNzbDovLy4uLilcbiAgICAgICAgIyBidXQgdGhlIGNlcnRpZmljYXRlIHVzZWQgYnkgdGhlIHNlcnZlciBpcyBub3QgdHJ1c3RlZCBieSBhbnkgQ0EgY2VydGlmaWNhdGVcbiAgICAgICAgIyBvbiB0aGUgc2VydmVyIChlLmcuIHdoZW4gc2VsZiBnZW5lcmF0ZWQpLlxuICAgICAgICBjYV9jZXJ0PVwiXCJcblxuICAgICAgICAjIFRMUyBjZXJ0aWZpY2F0ZSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgdGxzX2NlcnQ9XCJcIlxuXG4gICAgICAgICMgVExTIGtleSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgdGxzX2tleT1cIlwiXG5cblxuICAgICMgR2F0ZXdheSBjaGFubmVsIGNvbmZpZ3VyYXRpb24uXG4gICAgI1xuICAgICMgTm90ZTogdGhpcyBjb25maWd1cmF0aW9uIGlzIG9ubHkgdXNlZCBpbiBjYXNlIHRoZSBnYXRld2F5IGlzIHVzaW5nIHRoZVxuICAgICMgQ2hpcnBTdGFjayBDb25jZW50cmF0b3JkIGRhZW1vbi4gSW4gYW55IG90aGVyIGNhc2UsIHRoaXMgY29uZmlndXJhdGlvbiBcbiAgICAjIGlzIGlnbm9yZWQuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTQ4MTUwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9NDgxNzAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT00ODE5MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTQ4MjEwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9NDgyMzAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT00ODI1MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTQ4MjcwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9NDgyOTAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuXG4gICMgUmVnaW9uIHNwZWNpZmljIG5ldHdvcmsgY29uZmlndXJhdGlvbi5cbiAgW3JlZ2lvbnMubmV0d29ya11cbiAgICBcbiAgICAjIEluc3RhbGxhdGlvbiBtYXJnaW4gKGRCKSB1c2VkIGJ5IHRoZSBBRFIgZW5naW5lLlxuICAgICNcbiAgICAjIEEgaGlnaGVyIG51bWJlciBtZWFucyB0aGF0IHRoZSBuZXR3b3JrLXNlcnZlciB3aWxsIGtlZXAgbW9yZSBtYXJnaW4sXG4gICAgIyByZXN1bHRpbmcgaW4gYSBsb3dlciBkYXRhLXJhdGUgYnV0IGRlY3JlYXNpbmcgdGhlIGNoYW5jZSB0aGF0IHRoZVxuICAgICMgZGV2aWNlIGdldHMgZGlzY29ubmVjdGVkIGJlY2F1c2UgaXQgaXMgdW5hYmxlIHRvIHJlYWNoIG9uZSBvZiB0aGVcbiAgICAjIHN1cnJvdW5kZWQgZ2F0ZXdheXMuXG4gICAgaW5zdGFsbGF0aW9uX21hcmdpbj0xMFxuXG4gICAgIyBSWCB3aW5kb3cgKENsYXNzLUEpLlxuICAgICNcbiAgICAjIFNldCB0aGlzIHRvOlxuICAgICMgMDogUlgxIC8gUlgyXG4gICAgIyAxOiBSWDEgb25seVxuICAgICMgMjogUlgyIG9ubHlcbiAgICByeF93aW5kb3c9MFxuXG4gICAgIyBSWDEgZGVsYXkgKDEgLSAxNSBzZWNvbmRzKS5cbiAgICByeDFfZGVsYXk9MVxuXG4gICAgIyBSWDEgZGF0YS1yYXRlIG9mZnNldFxuICAgIHJ4MV9kcl9vZmZzZXQ9MFxuXG4gICAgIyBSWDIgZGF0YS1yYXRlXG4gICAgcngyX2RyPTBcblxuICAgICMgUlgyIGZyZXF1ZW5jeSAoSHopXG4gICAgcngyX2ZyZXF1ZW5jeT01MDUzMDAwMDBcblxuICAgICMgUHJlZmVyIFJYMiBvbiBSWDEgZGF0YS1yYXRlIGxlc3MgdGhhbi5cbiAgICAjXG4gICAgIyBQcmVmZXIgUlgyIG92ZXIgUlgxIGJhc2VkIG9uIHRoZSBSWDEgZGF0YS1yYXRlLiBXaGVuIHRoZSBSWDEgZGF0YS1yYXRlXG4gICAgIyBpcyBzbWFsbGVyIHRoYW4gdGhlIGNvbmZpZ3VyZWQgdmFsdWUsIHRoZW4gdGhlIE5ldHdvcmsgU2VydmVyIHdpbGxcbiAgICAjIGZpcnN0IHRyeSB0byBzY2hlZHVsZSB0aGUgZG93bmxpbmsgZm9yIFJYMiwgZmFpbGluZyB0aGF0IChlLmcuIHRoZSBnYXRld2F5XG4gICAgIyBoYXMgYWxyZWFkeSBhIHBheWxvYWQgc2NoZWR1bGVkIGF0IHRoZSBSWDIgdGltaW5nKSBpdCB3aWxsIHRyeSBSWDEuXG4gICAgcngyX3ByZWZlcl9vbl9yeDFfZHJfbHQ9MFxuXG4gICAgIyBQcmVmZXIgUlgyIG9uIGxpbmsgYnVkZ2V0LlxuICAgICNcbiAgICAjIFdoZW4gdGhlIGxpbmstYnVkZ2V0IGlzIGJldHRlciBmb3IgUlgyIHRoYW4gZm9yIFJYMSwgdGhlIE5ldHdvcmsgU2VydmVyIHdpbGwgZmlyc3RcbiAgICAjIHRyeSB0byBzY2hlZHVsZSB0aGUgZG93bmxpbmsgaW4gUlgyLCBmYWlsaW5nIHRoYXQgaXQgd2lsbCB0cnkgUlgxLlxuICAgIHJ4Ml9wcmVmZXJfb25fbGlua19idWRnZXQ9ZmFsc2VcblxuICAgICMgRG93bmxpbmsgVFggUG93ZXIgKGRCbSlcbiAgICAjXG4gICAgIyBXaGVuIHNldCB0byAtMSwgdGhlIGRvd25saW5rIFRYIFBvd2VyIGZyb20gdGhlIGNvbmZpZ3VyZWQgYmFuZCB3aWxsXG4gICAgIyBiZSB1c2VkLlxuICAgICNcbiAgICAjIFBsZWFzZSBjb25zdWx0IHRoZSBMb1JhV0FOIFJlZ2lvbmFsIFBhcmFtZXRlcnMgYW5kIGxvY2FsIHJlZ3VsYXRpb25zXG4gICAgIyBmb3IgdmFsaWQgYW5kIGxlZ2FsIG9wdGlvbnMuIE5vdGUgdGhhdCB0aGUgY29uZmlndXJlZCBUWCBQb3dlciBtdXN0IGJlXG4gICAgIyBzdXBwb3J0ZWQgYnkgeW91ciBnYXRld2F5KHMpLlxuICAgIGRvd25saW5rX3R4X3Bvd2VyPS0xXG5cbiAgICAjIEFEUiBpcyBkaXNhYmxlZC5cbiAgICBhZHJfZGlzYWJsZWQ9ZmFsc2VcblxuICAgICMgTWluaW11bSBkYXRhLXJhdGUuXG4gICAgbWluX2RyPTBcblxuICAgICMgTWF4aW11bSBkYXRhLXJhdGUuXG4gICAgbWF4X2RyPTVcblxuICAgICMgRW5hYmxlZCB1cGxpbmsgY2hhbm5lbHMuXG4gICAgI1xuICAgICMgVXNlIHRoaXMgd2hlbiBvbnkgYSBzdWItc2V0IG9mIHRoZSBieSBkZWZhdWx0IGVuYWJsZWQgY2hhbm5lbHMgYXJlIGJlaW5nXG4gICAgIyB1c2VkLiBGb3IgZXhhbXBsZSB3aGVuIG9ubHkgdXNpbmcgdGhlIGZpcnN0IDggY2hhbm5lbHMgb2YgdGhlIFVTIGJhbmQuXG4gICAgIyBOb3RlOiB3aGVuIGxlZnQgYmxhbmsgLyBlbXB0eSBhcnJheSwgYWxsIGNoYW5uZWxzIHdpbGwgYmUgZW5hYmxlZC5cbiAgICBlbmFibGVkX3VwbGlua19jaGFubmVscz1bNTYsIDU3LCA1OCwgNTksIDYwLCA2MSwgNjIsIDYzXVxuXG5cbiAgICAjIFJlam9pbi1yZXF1ZXN0IGNvbmZpZ3VyYXRpb24gKExvUmFXQU4gMS4xKVxuICAgIFtyZWdpb25zLm5ldHdvcmsucmVqb2luX3JlcXVlc3RdXG5cbiAgICAgICMgUmVxdWVzdCBkZXZpY2VzIHRvIHBlcmlvZGljYWxseSBzZW5kIHJlam9pbi1yZXF1ZXN0cy5cbiAgICAgIGVuYWJsZWQ9ZmFsc2VcblxuICAgICAgIyBUaGUgZGV2aWNlIG11c3Qgc2VuZCBhIHJlam9pbi1yZXF1ZXN0IHR5cGUgMCBhdCBsZWFzdCBldmVyeSAyXihtYXhfY291bnRfbiArIDQpXG4gICAgICAjIHVwbGluayBtZXNzYWdlcy4gVmFsaWQgdmFsdWVzIGFyZSAwIHRvIDE1LlxuICAgICAgbWF4X2NvdW50X249MFxuXG4gICAgICAjIFRoZSBkZXZpY2UgbXVzdCBzZW5kIGEgcmVqb2luLXJlcXVlc3QgdHlwZSAwIGF0IGxlYXN0IGV2ZXJ5IDJeKG1heF90aW1lX24gKyAxMClcbiAgICAgICMgc2Vjb25kcy4gVmFsaWQgdmFsdWVzIGFyZSAwIHRvIDE1LlxuICAgICAgI1xuICAgICAgIyAwICA9IHJvdWdobHkgMTcgbWludXRlc1xuICAgICAgIyAxNSA9IGFib3V0IDEgeWVhclxuICAgICAgbWF4X3RpbWVfbj0wXG4gICAgXG5cbiAgICAjIENsYXNzLUIgY29uZmlndXJhdGlvbi5cbiAgICBbcmVnaW9ucy5uZXR3b3JrLmNsYXNzX2JdXG5cbiAgICAgICMgUGluZy1zbG90IGRhdGEtcmF0ZS4gXG4gICAgICBwaW5nX3Nsb3RfZHI9MlxuXG4gICAgICAjIFBpbmctc2xvdCBmcmVxdWVuY3kgKEh6KVxuICAgICAgI1xuICAgICAgIyBzZXQgdGhpcyB0byAwIHRvIHVzZSB0aGUgZGVmYXVsdCBmcmVxdWVuY3kgcGxhbiBmb3IgdGhlIGNvbmZpZ3VyZWQgcmVnaW9uXG4gICAgICAjICh3aGljaCBjb3VsZCBiZSBmcmVxdWVuY3kgaG9wcGluZykuXG4gICAgICBwaW5nX3Nsb3RfZnJlcXVlbmN5PTBcblwiXCJcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuc2VydmljZU5hbWUgPSBcImNoaXJwc3RhY2tcIlxuZmlsZVBhdGggPSBcIi9jaGlycHN0YWNrL3JlZ2lvbl9jbjQ3MF84LnRvbWxcIlxuY29udGVudCA9IFwiXCJcIlxuIyBUaGlzIGZpbGUgY29udGFpbnMgYW4gZXhhbXBsZSBDTjQ3MCBleGFtcGxlIChjaGFubmVscyA2NC03MSkuXG5bW3JlZ2lvbnNdXVxuXG4gICMgSUQgaXMgYW4gdXNlLWRlZmluZWQgaWRlbnRpZmllciBmb3IgdGhpcyByZWdpb24uXG4gIGlkPVwiY240NzBfOFwiXG5cbiAgIyBEZXNjcmlwdGlvbiBpcyBhIHNob3J0IGRlc2NyaXB0aW9uIGZvciB0aGlzIHJlZ2lvbi5cbiAgZGVzY3JpcHRpb249XCJDTjQ3MCAoY2hhbm5lbHMgNjQtNzEpXCJcblxuICAjIENvbW1vbi1uYW1lIHJlZmVycyB0byB0aGUgY29tbW9uLW5hbWUgb2YgdGhpcyByZWdpb24gYXMgZGVmaW5lZCBieVxuICAjIHRoZSBMb1JhIEFsbGlhbmNlLlxuICBjb21tb25fbmFtZT1cIkNONDcwXCJcblxuXG4gICMgR2F0ZXdheSBjb25maWd1cmF0aW9uLlxuICBbcmVnaW9ucy5nYXRld2F5XVxuXG4gICAgIyBGb3JjZSBnYXRld2F5cyBhcyBwcml2YXRlLlxuICAgICNcbiAgICAjIElmIGVuYWJsZWQsIGdhdGV3YXlzIGNhbiBvbmx5IGJlIHVzZWQgYnkgZGV2aWNlcyB1bmRlciB0aGUgc2FtZSB0ZW5hbnQuXG4gICAgZm9yY2VfZ3dzX3ByaXZhdGU9ZmFsc2VcblxuICAgIFxuICAgICMgR2F0ZXdheSBiYWNrZW5kIGNvbmZpZ3VyYXRpb24uXG4gICAgW3JlZ2lvbnMuZ2F0ZXdheS5iYWNrZW5kXVxuXG4gICAgICAjIFRoZSBlbmFibGVkIGJhY2tlbmQgdHlwZS5cbiAgICAgIGVuYWJsZWQ9XCJtcXR0XCJcblxuICAgICAgIyBNUVRUIGNvbmZpZ3VyYXRpb24uXG4gICAgICBbcmVnaW9ucy5nYXRld2F5LmJhY2tlbmQubXF0dF1cblxuICAgICAgICAjIFRvcGljIHByZWZpeC5cbiAgICAgICAgI1xuICAgICAgICAjIFRoZSB0b3BpYyBwcmVmaXggY2FuIGJlIHVzZWQgdG8gZGVmaW5lIHRoZSByZWdpb24gb2YgdGhlIGdhdGV3YXkuXG4gICAgICAgICMgTm90ZSwgdGhlcmUgaXMgbm8gbmVlZCB0byBhZGQgYSB0cmFpbGluZyAnLycgdG8gdGhlIHByZWZpeC4gVGhlIHRyYWlsaW5nXG4gICAgICAgICMgJy8nIGlzIGF1dG9tYXRpY2FsbHkgYWRkZWQgdG8gdGhlIHByZWZpeCBpZiBpdCBpcyBjb25maWd1cmVkLlxuICAgICAgICB0b3BpY19wcmVmaXg9XCJjbjQ3MF84XCJcblxuICAgICAgICAjIE1RVFQgc2VydmVyIChlLmcuIHNjaGVtZTovL2hvc3Q6cG9ydCB3aGVyZSBzY2hlbWUgaXMgdGNwLCBzc2wgb3Igd3MpXG4gICAgICAgIHNlcnZlcj1cInRjcDovL21vc3F1aXR0bzoxODgzXCJcblxuICAgICAgICAjIENvbm5lY3Qgd2l0aCB0aGUgZ2l2ZW4gdXNlcm5hbWUgKG9wdGlvbmFsKVxuICAgICAgICB1c2VybmFtZT1cIlwiXG5cbiAgICAgICAgIyBDb25uZWN0IHdpdGggdGhlIGdpdmVuIHBhc3N3b3JkIChvcHRpb25hbClcbiAgICAgICAgcGFzc3dvcmQ9XCJcIlxuXG4gICAgICAgICMgUXVhbGl0eSBvZiBzZXJ2aWNlIGxldmVsXG4gICAgICAgICNcbiAgICAgICAgIyAwOiBhdCBtb3N0IG9uY2VcbiAgICAgICAgIyAxOiBhdCBsZWFzdCBvbmNlXG4gICAgICAgICMgMjogZXhhY3RseSBvbmNlXG4gICAgICAgICNcbiAgICAgICAgIyBOb3RlOiBhbiBpbmNyZWFzZSBvZiB0aGlzIHZhbHVlIHdpbGwgZGVjcmVhc2UgdGhlIHBlcmZvcm1hbmNlLlxuICAgICAgICAjIEZvciBtb3JlIGluZm9ybWF0aW9uOiBodHRwczovL3d3dy5oaXZlbXEuY29tL2Jsb2cvbXF0dC1lc3NlbnRpYWxzLXBhcnQtNi1tcXR0LXF1YWxpdHktb2Ytc2VydmljZS1sZXZlbHNcbiAgICAgICAgcW9zPTBcblxuICAgICAgICAjIENsZWFuIHNlc3Npb25cbiAgICAgICAgI1xuICAgICAgICAjIFNldCB0aGUgXCJjbGVhbiBzZXNzaW9uXCIgZmxhZyBpbiB0aGUgY29ubmVjdCBtZXNzYWdlIHdoZW4gdGhpcyBjbGllbnRcbiAgICAgICAgIyBjb25uZWN0cyB0byBhbiBNUVRUIGJyb2tlci4gQnkgc2V0dGluZyB0aGlzIGZsYWcgeW91IGFyZSBpbmRpY2F0aW5nXG4gICAgICAgICMgdGhhdCBubyBtZXNzYWdlcyBzYXZlZCBieSB0aGUgYnJva2VyIGZvciB0aGlzIGNsaWVudCBzaG91bGQgYmUgZGVsaXZlcmVkLlxuICAgICAgICBjbGVhbl9zZXNzaW9uPWZhbHNlXG5cbiAgICAgICAgIyBDbGllbnQgSURcbiAgICAgICAgI1xuICAgICAgICAjIFNldCB0aGUgY2xpZW50IGlkIHRvIGJlIHVzZWQgYnkgdGhpcyBjbGllbnQgd2hlbiBjb25uZWN0aW5nIHRvIHRoZSBNUVRUXG4gICAgICAgICMgYnJva2VyLiBBIGNsaWVudCBpZCBtdXN0IGJlIG5vIGxvbmdlciB0aGFuIDIzIGNoYXJhY3RlcnMuIElmIGxlZnQgYmxhbmssXG4gICAgICAgICMgYSByYW5kb20gaWQgd2lsbCBiZSBnZW5lcmF0ZWQgYnkgQ2hpcnBTdGFjay5cbiAgICAgICAgY2xpZW50X2lkPVwiXCJcblxuICAgICAgICAjIEtlZXAgYWxpdmUgaW50ZXJ2YWwuXG4gICAgICAgICNcbiAgICAgICAgIyBUaGlzIGRlZmluZXMgdGhlIG1heGltdW0gdGltZSB0aGF0IHRoYXQgc2hvdWxkIHBhc3Mgd2l0aG91dCBjb21tdW5pY2F0aW9uXG4gICAgICAgICMgYmV0d2VlbiB0aGUgY2xpZW50IGFuZCBzZXJ2ZXIuXG4gICAgICAgIGtlZXBfYWxpdmVfaW50ZXJ2YWw9XCIzMHNcIlxuXG4gICAgICAgICMgQ0EgY2VydGlmaWNhdGUgZmlsZSAob3B0aW9uYWwpXG4gICAgICAgICNcbiAgICAgICAgIyBVc2UgdGhpcyB3aGVuIHNldHRpbmcgdXAgYSBzZWN1cmUgY29ubmVjdGlvbiAod2hlbiBzZXJ2ZXIgdXNlcyBzc2w6Ly8uLi4pXG4gICAgICAgICMgYnV0IHRoZSBjZXJ0aWZpY2F0ZSB1c2VkIGJ5IHRoZSBzZXJ2ZXIgaXMgbm90IHRydXN0ZWQgYnkgYW55IENBIGNlcnRpZmljYXRlXG4gICAgICAgICMgb24gdGhlIHNlcnZlciAoZS5nLiB3aGVuIHNlbGYgZ2VuZXJhdGVkKS5cbiAgICAgICAgY2FfY2VydD1cIlwiXG5cbiAgICAgICAgIyBUTFMgY2VydGlmaWNhdGUgZmlsZSAob3B0aW9uYWwpXG4gICAgICAgIHRsc19jZXJ0PVwiXCJcblxuICAgICAgICAjIFRMUyBrZXkgZmlsZSAob3B0aW9uYWwpXG4gICAgICAgIHRsc19rZXk9XCJcIlxuXG5cbiAgICAjIEdhdGV3YXkgY2hhbm5lbCBjb25maWd1cmF0aW9uLlxuICAgICNcbiAgICAjIE5vdGU6IHRoaXMgY29uZmlndXJhdGlvbiBpcyBvbmx5IHVzZWQgaW4gY2FzZSB0aGUgZ2F0ZXdheSBpcyB1c2luZyB0aGVcbiAgICAjIENoaXJwU3RhY2sgQ29uY2VudHJhdG9yZCBkYWVtb24uIEluIGFueSBvdGhlciBjYXNlLCB0aGlzIGNvbmZpZ3VyYXRpb24gXG4gICAgIyBpcyBpZ25vcmVkLlxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT00ODMxMDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTQ4MzMwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9NDgzNTAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT00ODM3MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTQ4MzkwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9NDg0MTAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT00ODQzMDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTQ4NDUwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cblxuICAjIFJlZ2lvbiBzcGVjaWZpYyBuZXR3b3JrIGNvbmZpZ3VyYXRpb24uXG4gIFtyZWdpb25zLm5ldHdvcmtdXG4gICAgXG4gICAgIyBJbnN0YWxsYXRpb24gbWFyZ2luIChkQikgdXNlZCBieSB0aGUgQURSIGVuZ2luZS5cbiAgICAjXG4gICAgIyBBIGhpZ2hlciBudW1iZXIgbWVhbnMgdGhhdCB0aGUgbmV0d29yay1zZXJ2ZXIgd2lsbCBrZWVwIG1vcmUgbWFyZ2luLFxuICAgICMgcmVzdWx0aW5nIGluIGEgbG93ZXIgZGF0YS1yYXRlIGJ1dCBkZWNyZWFzaW5nIHRoZSBjaGFuY2UgdGhhdCB0aGVcbiAgICAjIGRldmljZSBnZXRzIGRpc2Nvbm5lY3RlZCBiZWNhdXNlIGl0IGlzIHVuYWJsZSB0byByZWFjaCBvbmUgb2YgdGhlXG4gICAgIyBzdXJyb3VuZGVkIGdhdGV3YXlzLlxuICAgIGluc3RhbGxhdGlvbl9tYXJnaW49MTBcblxuICAgICMgUlggd2luZG93IChDbGFzcy1BKS5cbiAgICAjXG4gICAgIyBTZXQgdGhpcyB0bzpcbiAgICAjIDA6IFJYMSAvIFJYMlxuICAgICMgMTogUlgxIG9ubHlcbiAgICAjIDI6IFJYMiBvbmx5XG4gICAgcnhfd2luZG93PTBcblxuICAgICMgUlgxIGRlbGF5ICgxIC0gMTUgc2Vjb25kcykuXG4gICAgcngxX2RlbGF5PTFcblxuICAgICMgUlgxIGRhdGEtcmF0ZSBvZmZzZXRcbiAgICByeDFfZHJfb2Zmc2V0PTBcblxuICAgICMgUlgyIGRhdGEtcmF0ZVxuICAgIHJ4Ml9kcj0wXG5cbiAgICAjIFJYMiBmcmVxdWVuY3kgKEh6KVxuICAgIHJ4Ml9mcmVxdWVuY3k9NTA1MzAwMDAwXG5cbiAgICAjIFByZWZlciBSWDIgb24gUlgxIGRhdGEtcmF0ZSBsZXNzIHRoYW4uXG4gICAgI1xuICAgICMgUHJlZmVyIFJYMiBvdmVyIFJYMSBiYXNlZCBvbiB0aGUgUlgxIGRhdGEtcmF0ZS4gV2hlbiB0aGUgUlgxIGRhdGEtcmF0ZVxuICAgICMgaXMgc21hbGxlciB0aGFuIHRoZSBjb25maWd1cmVkIHZhbHVlLCB0aGVuIHRoZSBOZXR3b3JrIFNlcnZlciB3aWxsXG4gICAgIyBmaXJzdCB0cnkgdG8gc2NoZWR1bGUgdGhlIGRvd25saW5rIGZvciBSWDIsIGZhaWxpbmcgdGhhdCAoZS5nLiB0aGUgZ2F0ZXdheVxuICAgICMgaGFzIGFscmVhZHkgYSBwYXlsb2FkIHNjaGVkdWxlZCBhdCB0aGUgUlgyIHRpbWluZykgaXQgd2lsbCB0cnkgUlgxLlxuICAgIHJ4Ml9wcmVmZXJfb25fcngxX2RyX2x0PTBcblxuICAgICMgUHJlZmVyIFJYMiBvbiBsaW5rIGJ1ZGdldC5cbiAgICAjXG4gICAgIyBXaGVuIHRoZSBsaW5rLWJ1ZGdldCBpcyBiZXR0ZXIgZm9yIFJYMiB0aGFuIGZvciBSWDEsIHRoZSBOZXR3b3JrIFNlcnZlciB3aWxsIGZpcnN0XG4gICAgIyB0cnkgdG8gc2NoZWR1bGUgdGhlIGRvd25saW5rIGluIFJYMiwgZmFpbGluZyB0aGF0IGl0IHdpbGwgdHJ5IFJYMS5cbiAgICByeDJfcHJlZmVyX29uX2xpbmtfYnVkZ2V0PWZhbHNlXG5cbiAgICAjIERvd25saW5rIFRYIFBvd2VyIChkQm0pXG4gICAgI1xuICAgICMgV2hlbiBzZXQgdG8gLTEsIHRoZSBkb3dubGluayBUWCBQb3dlciBmcm9tIHRoZSBjb25maWd1cmVkIGJhbmQgd2lsbFxuICAgICMgYmUgdXNlZC5cbiAgICAjXG4gICAgIyBQbGVhc2UgY29uc3VsdCB0aGUgTG9SYVdBTiBSZWdpb25hbCBQYXJhbWV0ZXJzIGFuZCBsb2NhbCByZWd1bGF0aW9uc1xuICAgICMgZm9yIHZhbGlkIGFuZCBsZWdhbCBvcHRpb25zLiBOb3RlIHRoYXQgdGhlIGNvbmZpZ3VyZWQgVFggUG93ZXIgbXVzdCBiZVxuICAgICMgc3VwcG9ydGVkIGJ5IHlvdXIgZ2F0ZXdheShzKS5cbiAgICBkb3dubGlua190eF9wb3dlcj0tMVxuXG4gICAgIyBBRFIgaXMgZGlzYWJsZWQuXG4gICAgYWRyX2Rpc2FibGVkPWZhbHNlXG5cbiAgICAjIE1pbmltdW0gZGF0YS1yYXRlLlxuICAgIG1pbl9kcj0wXG5cbiAgICAjIE1heGltdW0gZGF0YS1yYXRlLlxuICAgIG1heF9kcj01XG5cbiAgICAjIEVuYWJsZWQgdXBsaW5rIGNoYW5uZWxzLlxuICAgICNcbiAgICAjIFVzZSB0aGlzIHdoZW4gb255IGEgc3ViLXNldCBvZiB0aGUgYnkgZGVmYXVsdCBlbmFibGVkIGNoYW5uZWxzIGFyZSBiZWluZ1xuICAgICMgdXNlZC4gRm9yIGV4YW1wbGUgd2hlbiBvbmx5IHVzaW5nIHRoZSBmaXJzdCA4IGNoYW5uZWxzIG9mIHRoZSBVUyBiYW5kLlxuICAgICMgTm90ZTogd2hlbiBsZWZ0IGJsYW5rIC8gZW1wdHkgYXJyYXksIGFsbCBjaGFubmVscyB3aWxsIGJlIGVuYWJsZWQuXG4gICAgZW5hYmxlZF91cGxpbmtfY2hhbm5lbHM9WzY0LCA2NSwgNjYsIDY3LCA2OCwgNjksIDcwLCA3MV1cblxuXG4gICAgIyBSZWpvaW4tcmVxdWVzdCBjb25maWd1cmF0aW9uIChMb1JhV0FOIDEuMSlcbiAgICBbcmVnaW9ucy5uZXR3b3JrLnJlam9pbl9yZXF1ZXN0XVxuXG4gICAgICAjIFJlcXVlc3QgZGV2aWNlcyB0byBwZXJpb2RpY2FsbHkgc2VuZCByZWpvaW4tcmVxdWVzdHMuXG4gICAgICBlbmFibGVkPWZhbHNlXG5cbiAgICAgICMgVGhlIGRldmljZSBtdXN0IHNlbmQgYSByZWpvaW4tcmVxdWVzdCB0eXBlIDAgYXQgbGVhc3QgZXZlcnkgMl4obWF4X2NvdW50X24gKyA0KVxuICAgICAgIyB1cGxpbmsgbWVzc2FnZXMuIFZhbGlkIHZhbHVlcyBhcmUgMCB0byAxNS5cbiAgICAgIG1heF9jb3VudF9uPTBcblxuICAgICAgIyBUaGUgZGV2aWNlIG11c3Qgc2VuZCBhIHJlam9pbi1yZXF1ZXN0IHR5cGUgMCBhdCBsZWFzdCBldmVyeSAyXihtYXhfdGltZV9uICsgMTApXG4gICAgICAjIHNlY29uZHMuIFZhbGlkIHZhbHVlcyBhcmUgMCB0byAxNS5cbiAgICAgICNcbiAgICAgICMgMCAgPSByb3VnaGx5IDE3IG1pbnV0ZXNcbiAgICAgICMgMTUgPSBhYm91dCAxIHllYXJcbiAgICAgIG1heF90aW1lX249MFxuICAgIFxuXG4gICAgIyBDbGFzcy1CIGNvbmZpZ3VyYXRpb24uXG4gICAgW3JlZ2lvbnMubmV0d29yay5jbGFzc19iXVxuXG4gICAgICAjIFBpbmctc2xvdCBkYXRhLXJhdGUuIFxuICAgICAgcGluZ19zbG90X2RyPTJcblxuICAgICAgIyBQaW5nLXNsb3QgZnJlcXVlbmN5IChIeilcbiAgICAgICNcbiAgICAgICMgc2V0IHRoaXMgdG8gMCB0byB1c2UgdGhlIGRlZmF1bHQgZnJlcXVlbmN5IHBsYW4gZm9yIHRoZSBjb25maWd1cmVkIHJlZ2lvblxuICAgICAgIyAod2hpY2ggY291bGQgYmUgZnJlcXVlbmN5IGhvcHBpbmcpLlxuICAgICAgcGluZ19zbG90X2ZyZXF1ZW5jeT0wXG5cIlwiXCJcblxuW1tjb25maWcubW91bnRzXV1cbnNlcnZpY2VOYW1lID0gXCJjaGlycHN0YWNrXCJcbmZpbGVQYXRoID0gXCIvY2hpcnBzdGFjay9yZWdpb25fY240NzBfOS50b21sXCJcbmNvbnRlbnQgPSBcIlwiXCJcbiMgVGhpcyBmaWxlIGNvbnRhaW5zIGFuIGV4YW1wbGUgQ040NzAgZXhhbXBsZSAoY2hhbm5lbHMgNzItNzkpLlxuW1tyZWdpb25zXV1cblxuICAjIElEIGlzIGFuIHVzZS1kZWZpbmVkIGlkZW50aWZpZXIgZm9yIHRoaXMgcmVnaW9uLlxuICBpZD1cImNuNDcwXzlcIlxuXG4gICMgRGVzY3JpcHRpb24gaXMgYSBzaG9ydCBkZXNjcmlwdGlvbiBmb3IgdGhpcyByZWdpb24uXG4gIGRlc2NyaXB0aW9uPVwiQ040NzAgKGNoYW5uZWxzIDcyLTc5KVwiXG5cbiAgIyBDb21tb24tbmFtZSByZWZlcnMgdG8gdGhlIGNvbW1vbi1uYW1lIG9mIHRoaXMgcmVnaW9uIGFzIGRlZmluZWQgYnlcbiAgIyB0aGUgTG9SYSBBbGxpYW5jZS5cbiAgY29tbW9uX25hbWU9XCJDTjQ3MFwiXG5cblxuICAjIEdhdGV3YXkgY29uZmlndXJhdGlvbi5cbiAgW3JlZ2lvbnMuZ2F0ZXdheV1cblxuICAgICMgRm9yY2UgZ2F0ZXdheXMgYXMgcHJpdmF0ZS5cbiAgICAjXG4gICAgIyBJZiBlbmFibGVkLCBnYXRld2F5cyBjYW4gb25seSBiZSB1c2VkIGJ5IGRldmljZXMgdW5kZXIgdGhlIHNhbWUgdGVuYW50LlxuICAgIGZvcmNlX2d3c19wcml2YXRlPWZhbHNlXG5cbiAgICBcbiAgICAjIEdhdGV3YXkgYmFja2VuZCBjb25maWd1cmF0aW9uLlxuICAgIFtyZWdpb25zLmdhdGV3YXkuYmFja2VuZF1cblxuICAgICAgIyBUaGUgZW5hYmxlZCBiYWNrZW5kIHR5cGUuXG4gICAgICBlbmFibGVkPVwibXF0dFwiXG5cbiAgICAgICMgTVFUVCBjb25maWd1cmF0aW9uLlxuICAgICAgW3JlZ2lvbnMuZ2F0ZXdheS5iYWNrZW5kLm1xdHRdXG5cbiAgICAgICAgIyBUb3BpYyBwcmVmaXguXG4gICAgICAgICNcbiAgICAgICAgIyBUaGUgdG9waWMgcHJlZml4IGNhbiBiZSB1c2VkIHRvIGRlZmluZSB0aGUgcmVnaW9uIG9mIHRoZSBnYXRld2F5LlxuICAgICAgICAjIE5vdGUsIHRoZXJlIGlzIG5vIG5lZWQgdG8gYWRkIGEgdHJhaWxpbmcgJy8nIHRvIHRoZSBwcmVmaXguIFRoZSB0cmFpbGluZ1xuICAgICAgICAjICcvJyBpcyBhdXRvbWF0aWNhbGx5IGFkZGVkIHRvIHRoZSBwcmVmaXggaWYgaXQgaXMgY29uZmlndXJlZC5cbiAgICAgICAgdG9waWNfcHJlZml4PVwiY240NzBfOVwiXG5cbiAgICAgICAgIyBNUVRUIHNlcnZlciAoZS5nLiBzY2hlbWU6Ly9ob3N0OnBvcnQgd2hlcmUgc2NoZW1lIGlzIHRjcCwgc3NsIG9yIHdzKVxuICAgICAgICBzZXJ2ZXI9XCJ0Y3A6Ly9tb3NxdWl0dG86MTg4M1wiXG5cbiAgICAgICAgIyBDb25uZWN0IHdpdGggdGhlIGdpdmVuIHVzZXJuYW1lIChvcHRpb25hbClcbiAgICAgICAgdXNlcm5hbWU9XCJcIlxuXG4gICAgICAgICMgQ29ubmVjdCB3aXRoIHRoZSBnaXZlbiBwYXNzd29yZCAob3B0aW9uYWwpXG4gICAgICAgIHBhc3N3b3JkPVwiXCJcblxuICAgICAgICAjIFF1YWxpdHkgb2Ygc2VydmljZSBsZXZlbFxuICAgICAgICAjXG4gICAgICAgICMgMDogYXQgbW9zdCBvbmNlXG4gICAgICAgICMgMTogYXQgbGVhc3Qgb25jZVxuICAgICAgICAjIDI6IGV4YWN0bHkgb25jZVxuICAgICAgICAjXG4gICAgICAgICMgTm90ZTogYW4gaW5jcmVhc2Ugb2YgdGhpcyB2YWx1ZSB3aWxsIGRlY3JlYXNlIHRoZSBwZXJmb3JtYW5jZS5cbiAgICAgICAgIyBGb3IgbW9yZSBpbmZvcm1hdGlvbjogaHR0cHM6Ly93d3cuaGl2ZW1xLmNvbS9ibG9nL21xdHQtZXNzZW50aWFscy1wYXJ0LTYtbXF0dC1xdWFsaXR5LW9mLXNlcnZpY2UtbGV2ZWxzXG4gICAgICAgIHFvcz0wXG5cbiAgICAgICAgIyBDbGVhbiBzZXNzaW9uXG4gICAgICAgICNcbiAgICAgICAgIyBTZXQgdGhlIFwiY2xlYW4gc2Vzc2lvblwiIGZsYWcgaW4gdGhlIGNvbm5lY3QgbWVzc2FnZSB3aGVuIHRoaXMgY2xpZW50XG4gICAgICAgICMgY29ubmVjdHMgdG8gYW4gTVFUVCBicm9rZXIuIEJ5IHNldHRpbmcgdGhpcyBmbGFnIHlvdSBhcmUgaW5kaWNhdGluZ1xuICAgICAgICAjIHRoYXQgbm8gbWVzc2FnZXMgc2F2ZWQgYnkgdGhlIGJyb2tlciBmb3IgdGhpcyBjbGllbnQgc2hvdWxkIGJlIGRlbGl2ZXJlZC5cbiAgICAgICAgY2xlYW5fc2Vzc2lvbj1mYWxzZVxuXG4gICAgICAgICMgQ2xpZW50IElEXG4gICAgICAgICNcbiAgICAgICAgIyBTZXQgdGhlIGNsaWVudCBpZCB0byBiZSB1c2VkIGJ5IHRoaXMgY2xpZW50IHdoZW4gY29ubmVjdGluZyB0byB0aGUgTVFUVFxuICAgICAgICAjIGJyb2tlci4gQSBjbGllbnQgaWQgbXVzdCBiZSBubyBsb25nZXIgdGhhbiAyMyBjaGFyYWN0ZXJzLiBJZiBsZWZ0IGJsYW5rLFxuICAgICAgICAjIGEgcmFuZG9tIGlkIHdpbGwgYmUgZ2VuZXJhdGVkIGJ5IENoaXJwU3RhY2suXG4gICAgICAgIGNsaWVudF9pZD1cIlwiXG5cbiAgICAgICAgIyBLZWVwIGFsaXZlIGludGVydmFsLlxuICAgICAgICAjXG4gICAgICAgICMgVGhpcyBkZWZpbmVzIHRoZSBtYXhpbXVtIHRpbWUgdGhhdCB0aGF0IHNob3VsZCBwYXNzIHdpdGhvdXQgY29tbXVuaWNhdGlvblxuICAgICAgICAjIGJldHdlZW4gdGhlIGNsaWVudCBhbmQgc2VydmVyLlxuICAgICAgICBrZWVwX2FsaXZlX2ludGVydmFsPVwiMzBzXCJcblxuICAgICAgICAjIENBIGNlcnRpZmljYXRlIGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICAjXG4gICAgICAgICMgVXNlIHRoaXMgd2hlbiBzZXR0aW5nIHVwIGEgc2VjdXJlIGNvbm5lY3Rpb24gKHdoZW4gc2VydmVyIHVzZXMgc3NsOi8vLi4uKVxuICAgICAgICAjIGJ1dCB0aGUgY2VydGlmaWNhdGUgdXNlZCBieSB0aGUgc2VydmVyIGlzIG5vdCB0cnVzdGVkIGJ5IGFueSBDQSBjZXJ0aWZpY2F0ZVxuICAgICAgICAjIG9uIHRoZSBzZXJ2ZXIgKGUuZy4gd2hlbiBzZWxmIGdlbmVyYXRlZCkuXG4gICAgICAgIGNhX2NlcnQ9XCJcIlxuXG4gICAgICAgICMgVExTIGNlcnRpZmljYXRlIGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICB0bHNfY2VydD1cIlwiXG5cbiAgICAgICAgIyBUTFMga2V5IGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICB0bHNfa2V5PVwiXCJcblxuXG4gICAgIyBHYXRld2F5IGNoYW5uZWwgY29uZmlndXJhdGlvbi5cbiAgICAjXG4gICAgIyBOb3RlOiB0aGlzIGNvbmZpZ3VyYXRpb24gaXMgb25seSB1c2VkIGluIGNhc2UgdGhlIGdhdGV3YXkgaXMgdXNpbmcgdGhlXG4gICAgIyBDaGlycFN0YWNrIENvbmNlbnRyYXRvcmQgZGFlbW9uLiBJbiBhbnkgb3RoZXIgY2FzZSwgdGhpcyBjb25maWd1cmF0aW9uIFxuICAgICMgaXMgaWdub3JlZC5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9NDg0NzAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT00ODQ5MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTQ4NTEwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9NDg1MzAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT00ODU1MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTQ4NTcwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9NDg1OTAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT00ODYxMDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG5cbiAgIyBSZWdpb24gc3BlY2lmaWMgbmV0d29yayBjb25maWd1cmF0aW9uLlxuICBbcmVnaW9ucy5uZXR3b3JrXVxuICAgIFxuICAgICMgSW5zdGFsbGF0aW9uIG1hcmdpbiAoZEIpIHVzZWQgYnkgdGhlIEFEUiBlbmdpbmUuXG4gICAgI1xuICAgICMgQSBoaWdoZXIgbnVtYmVyIG1lYW5zIHRoYXQgdGhlIG5ldHdvcmstc2VydmVyIHdpbGwga2VlcCBtb3JlIG1hcmdpbixcbiAgICAjIHJlc3VsdGluZyBpbiBhIGxvd2VyIGRhdGEtcmF0ZSBidXQgZGVjcmVhc2luZyB0aGUgY2hhbmNlIHRoYXQgdGhlXG4gICAgIyBkZXZpY2UgZ2V0cyBkaXNjb25uZWN0ZWQgYmVjYXVzZSBpdCBpcyB1bmFibGUgdG8gcmVhY2ggb25lIG9mIHRoZVxuICAgICMgc3Vycm91bmRlZCBnYXRld2F5cy5cbiAgICBpbnN0YWxsYXRpb25fbWFyZ2luPTEwXG5cbiAgICAjIFJYIHdpbmRvdyAoQ2xhc3MtQSkuXG4gICAgI1xuICAgICMgU2V0IHRoaXMgdG86XG4gICAgIyAwOiBSWDEgLyBSWDJcbiAgICAjIDE6IFJYMSBvbmx5XG4gICAgIyAyOiBSWDIgb25seVxuICAgIHJ4X3dpbmRvdz0wXG5cbiAgICAjIFJYMSBkZWxheSAoMSAtIDE1IHNlY29uZHMpLlxuICAgIHJ4MV9kZWxheT0xXG5cbiAgICAjIFJYMSBkYXRhLXJhdGUgb2Zmc2V0XG4gICAgcngxX2RyX29mZnNldD0wXG5cbiAgICAjIFJYMiBkYXRhLXJhdGVcbiAgICByeDJfZHI9MFxuXG4gICAgIyBSWDIgZnJlcXVlbmN5IChIeilcbiAgICByeDJfZnJlcXVlbmN5PTUwNTMwMDAwMFxuXG4gICAgIyBQcmVmZXIgUlgyIG9uIFJYMSBkYXRhLXJhdGUgbGVzcyB0aGFuLlxuICAgICNcbiAgICAjIFByZWZlciBSWDIgb3ZlciBSWDEgYmFzZWQgb24gdGhlIFJYMSBkYXRhLXJhdGUuIFdoZW4gdGhlIFJYMSBkYXRhLXJhdGVcbiAgICAjIGlzIHNtYWxsZXIgdGhhbiB0aGUgY29uZmlndXJlZCB2YWx1ZSwgdGhlbiB0aGUgTmV0d29yayBTZXJ2ZXIgd2lsbFxuICAgICMgZmlyc3QgdHJ5IHRvIHNjaGVkdWxlIHRoZSBkb3dubGluayBmb3IgUlgyLCBmYWlsaW5nIHRoYXQgKGUuZy4gdGhlIGdhdGV3YXlcbiAgICAjIGhhcyBhbHJlYWR5IGEgcGF5bG9hZCBzY2hlZHVsZWQgYXQgdGhlIFJYMiB0aW1pbmcpIGl0IHdpbGwgdHJ5IFJYMS5cbiAgICByeDJfcHJlZmVyX29uX3J4MV9kcl9sdD0wXG5cbiAgICAjIFByZWZlciBSWDIgb24gbGluayBidWRnZXQuXG4gICAgI1xuICAgICMgV2hlbiB0aGUgbGluay1idWRnZXQgaXMgYmV0dGVyIGZvciBSWDIgdGhhbiBmb3IgUlgxLCB0aGUgTmV0d29yayBTZXJ2ZXIgd2lsbCBmaXJzdFxuICAgICMgdHJ5IHRvIHNjaGVkdWxlIHRoZSBkb3dubGluayBpbiBSWDIsIGZhaWxpbmcgdGhhdCBpdCB3aWxsIHRyeSBSWDEuXG4gICAgcngyX3ByZWZlcl9vbl9saW5rX2J1ZGdldD1mYWxzZVxuXG4gICAgIyBEb3dubGluayBUWCBQb3dlciAoZEJtKVxuICAgICNcbiAgICAjIFdoZW4gc2V0IHRvIC0xLCB0aGUgZG93bmxpbmsgVFggUG93ZXIgZnJvbSB0aGUgY29uZmlndXJlZCBiYW5kIHdpbGxcbiAgICAjIGJlIHVzZWQuXG4gICAgI1xuICAgICMgUGxlYXNlIGNvbnN1bHQgdGhlIExvUmFXQU4gUmVnaW9uYWwgUGFyYW1ldGVycyBhbmQgbG9jYWwgcmVndWxhdGlvbnNcbiAgICAjIGZvciB2YWxpZCBhbmQgbGVnYWwgb3B0aW9ucy4gTm90ZSB0aGF0IHRoZSBjb25maWd1cmVkIFRYIFBvd2VyIG11c3QgYmVcbiAgICAjIHN1cHBvcnRlZCBieSB5b3VyIGdhdGV3YXkocykuXG4gICAgZG93bmxpbmtfdHhfcG93ZXI9LTFcblxuICAgICMgQURSIGlzIGRpc2FibGVkLlxuICAgIGFkcl9kaXNhYmxlZD1mYWxzZVxuXG4gICAgIyBNaW5pbXVtIGRhdGEtcmF0ZS5cbiAgICBtaW5fZHI9MFxuXG4gICAgIyBNYXhpbXVtIGRhdGEtcmF0ZS5cbiAgICBtYXhfZHI9NVxuXG4gICAgIyBFbmFibGVkIHVwbGluayBjaGFubmVscy5cbiAgICAjXG4gICAgIyBVc2UgdGhpcyB3aGVuIG9ueSBhIHN1Yi1zZXQgb2YgdGhlIGJ5IGRlZmF1bHQgZW5hYmxlZCBjaGFubmVscyBhcmUgYmVpbmdcbiAgICAjIHVzZWQuIEZvciBleGFtcGxlIHdoZW4gb25seSB1c2luZyB0aGUgZmlyc3QgOCBjaGFubmVscyBvZiB0aGUgVVMgYmFuZC5cbiAgICAjIE5vdGU6IHdoZW4gbGVmdCBibGFuayAvIGVtcHR5IGFycmF5LCBhbGwgY2hhbm5lbHMgd2lsbCBiZSBlbmFibGVkLlxuICAgIGVuYWJsZWRfdXBsaW5rX2NoYW5uZWxzPVs3MiwgNzMsIDc0LCA3NSwgNzYsIDc3LCA3OCwgNzldXG5cblxuICAgICMgUmVqb2luLXJlcXVlc3QgY29uZmlndXJhdGlvbiAoTG9SYVdBTiAxLjEpXG4gICAgW3JlZ2lvbnMubmV0d29yay5yZWpvaW5fcmVxdWVzdF1cblxuICAgICAgIyBSZXF1ZXN0IGRldmljZXMgdG8gcGVyaW9kaWNhbGx5IHNlbmQgcmVqb2luLXJlcXVlc3RzLlxuICAgICAgZW5hYmxlZD1mYWxzZVxuXG4gICAgICAjIFRoZSBkZXZpY2UgbXVzdCBzZW5kIGEgcmVqb2luLXJlcXVlc3QgdHlwZSAwIGF0IGxlYXN0IGV2ZXJ5IDJeKG1heF9jb3VudF9uICsgNClcbiAgICAgICMgdXBsaW5rIG1lc3NhZ2VzLiBWYWxpZCB2YWx1ZXMgYXJlIDAgdG8gMTUuXG4gICAgICBtYXhfY291bnRfbj0wXG5cbiAgICAgICMgVGhlIGRldmljZSBtdXN0IHNlbmQgYSByZWpvaW4tcmVxdWVzdCB0eXBlIDAgYXQgbGVhc3QgZXZlcnkgMl4obWF4X3RpbWVfbiArIDEwKVxuICAgICAgIyBzZWNvbmRzLiBWYWxpZCB2YWx1ZXMgYXJlIDAgdG8gMTUuXG4gICAgICAjXG4gICAgICAjIDAgID0gcm91Z2hseSAxNyBtaW51dGVzXG4gICAgICAjIDE1ID0gYWJvdXQgMSB5ZWFyXG4gICAgICBtYXhfdGltZV9uPTBcbiAgICBcblxuICAgICMgQ2xhc3MtQiBjb25maWd1cmF0aW9uLlxuICAgIFtyZWdpb25zLm5ldHdvcmsuY2xhc3NfYl1cblxuICAgICAgIyBQaW5nLXNsb3QgZGF0YS1yYXRlLiBcbiAgICAgIHBpbmdfc2xvdF9kcj0yXG5cbiAgICAgICMgUGluZy1zbG90IGZyZXF1ZW5jeSAoSHopXG4gICAgICAjXG4gICAgICAjIHNldCB0aGlzIHRvIDAgdG8gdXNlIHRoZSBkZWZhdWx0IGZyZXF1ZW5jeSBwbGFuIGZvciB0aGUgY29uZmlndXJlZCByZWdpb25cbiAgICAgICMgKHdoaWNoIGNvdWxkIGJlIGZyZXF1ZW5jeSBob3BwaW5nKS5cbiAgICAgIHBpbmdfc2xvdF9mcmVxdWVuY3k9MFxuXCJcIlwiXG5cbltbY29uZmlnLm1vdW50c11dXG5zZXJ2aWNlTmFtZSA9IFwiY2hpcnBzdGFja1wiXG5maWxlUGF0aCA9IFwiL2NoaXJwc3RhY2svcmVnaW9uX2NuNzc5LnRvbWxcIlxuY29udGVudCA9IFwiXCJcIlxuIyBUaGlzIGZpbGUgY29udGFpbnMgYW4gZXhhbXBsZSBDTjc3OSBjb25maWd1cmF0aW9uLlxuW1tyZWdpb25zXV1cblxuICAjIElEIGlzIGFuIHVzZXItZGVmaW5lZCBpZGVudGlmaWVyIGZvciB0aGlzIHJlZ2lvbi5cbiAgaWQ9XCJjbjc3OVwiXG5cbiAgIyBEZXNjcmlwdGlvbiBpcyBhIHNob3J0IGRlc2NyaXB0aW9uIGZvciB0aGlzIHJlZ2lvbi5cbiAgZGVzY3JpcHRpb249XCJDTjc3OVwiXG5cbiAgIyBDb21tb24tbmFtZSByZWZlcnMgdG8gdGhlIGNvbW1vbi1uYW1lIG9mIHRoaXMgcmVnaW9uIGFzIGRlZmluZWQgYnlcbiAgIyB0aGUgTG9SYSBBbGxpYW5jZS5cbiAgY29tbW9uX25hbWU9XCJDTjc3OVwiXG5cblxuICAjIEdhdGV3YXkgY29uZmlndXJhdGlvbi5cbiAgW3JlZ2lvbnMuZ2F0ZXdheV1cblxuICAgICMgRm9yY2UgZ2F0ZXdheXMgYXMgcHJpdmF0ZS5cbiAgICAjXG4gICAgIyBJZiBlbmFibGVkLCBnYXRld2F5cyBjYW4gb25seSBiZSB1c2VkIGJ5IGRldmljZXMgdW5kZXIgdGhlIHNhbWUgdGVuYW50LlxuICAgIGZvcmNlX2d3c19wcml2YXRlPWZhbHNlXG5cblxuICAgICMgR2F0ZXdheSBiYWNrZW5kIGNvbmZpZ3VyYXRpb24uXG4gICAgW3JlZ2lvbnMuZ2F0ZXdheS5iYWNrZW5kXVxuXG4gICAgICAjIFRoZSBlbmFibGVkIGJhY2tlbmQgdHlwZS5cbiAgICAgIGVuYWJsZWQ9XCJtcXR0XCJcblxuICAgICAgIyBNUVRUIGNvbmZpZ3VyYXRpb24uXG4gICAgICBbcmVnaW9ucy5nYXRld2F5LmJhY2tlbmQubXF0dF1cblxuICAgICAgICAjIFRvcGljIHByZWZpeC5cbiAgICAgICAgI1xuICAgICAgICAjIFRoZSB0b3BpYyBwcmVmaXggY2FuIGJlIHVzZWQgdG8gZGVmaW5lIHRoZSByZWdpb24gb2YgdGhlIGdhdGV3YXkuXG4gICAgICAgICMgTm90ZSwgdGhlcmUgaXMgbm8gbmVlZCB0byBhZGQgYSB0cmFpbGluZyAnLycgdG8gdGhlIHByZWZpeC4gVGhlIHRyYWlsaW5nXG4gICAgICAgICMgJy8nIGlzIGF1dG9tYXRpY2FsbHkgYWRkZWQgdG8gdGhlIHByZWZpeCBpZiBpdCBpcyBjb25maWd1cmVkLlxuICAgICAgICB0b3BpY19wcmVmaXg9XCJjbjc3OVwiXG5cbiAgICAgICAgIyBNUVRUIHNlcnZlciAoZS5nLiBzY2hlbWU6Ly9ob3N0OnBvcnQgd2hlcmUgc2NoZW1lIGlzIHRjcCwgc3NsIG9yIHdzKVxuICAgICAgICBzZXJ2ZXI9XCJ0Y3A6Ly9tb3NxdWl0dG86MTg4M1wiXG5cbiAgICAgICAgIyBDb25uZWN0IHdpdGggdGhlIGdpdmVuIHVzZXJuYW1lIChvcHRpb25hbClcbiAgICAgICAgdXNlcm5hbWU9XCJcIlxuXG4gICAgICAgICMgQ29ubmVjdCB3aXRoIHRoZSBnaXZlbiBwYXNzd29yZCAob3B0aW9uYWwpXG4gICAgICAgIHBhc3N3b3JkPVwiXCJcblxuICAgICAgICAjIFF1YWxpdHkgb2Ygc2VydmljZSBsZXZlbFxuICAgICAgICAjXG4gICAgICAgICMgMDogYXQgbW9zdCBvbmNlXG4gICAgICAgICMgMTogYXQgbGVhc3Qgb25jZVxuICAgICAgICAjIDI6IGV4YWN0bHkgb25jZVxuICAgICAgICAjXG4gICAgICAgICMgTm90ZTogYW4gaW5jcmVhc2Ugb2YgdGhpcyB2YWx1ZSB3aWxsIGRlY3JlYXNlIHRoZSBwZXJmb3JtYW5jZS5cbiAgICAgICAgIyBGb3IgbW9yZSBpbmZvcm1hdGlvbjogaHR0cHM6Ly93d3cuaGl2ZW1xLmNvbS9ibG9nL21xdHQtZXNzZW50aWFscy1wYXJ0LTYtbXF0dC1xdWFsaXR5LW9mLXNlcnZpY2UtbGV2ZWxzXG4gICAgICAgIHFvcz0wXG5cbiAgICAgICAgIyBDbGVhbiBzZXNzaW9uXG4gICAgICAgICNcbiAgICAgICAgIyBTZXQgdGhlIFwiY2xlYW4gc2Vzc2lvblwiIGZsYWcgaW4gdGhlIGNvbm5lY3QgbWVzc2FnZSB3aGVuIHRoaXMgY2xpZW50XG4gICAgICAgICMgY29ubmVjdHMgdG8gYW4gTVFUVCBicm9rZXIuIEJ5IHNldHRpbmcgdGhpcyBmbGFnIHlvdSBhcmUgaW5kaWNhdGluZ1xuICAgICAgICAjIHRoYXQgbm8gbWVzc2FnZXMgc2F2ZWQgYnkgdGhlIGJyb2tlciBmb3IgdGhpcyBjbGllbnQgc2hvdWxkIGJlIGRlbGl2ZXJlZC5cbiAgICAgICAgY2xlYW5fc2Vzc2lvbj1mYWxzZVxuXG4gICAgICAgICMgQ2xpZW50IElEXG4gICAgICAgICNcbiAgICAgICAgIyBTZXQgdGhlIGNsaWVudCBpZCB0byBiZSB1c2VkIGJ5IHRoaXMgY2xpZW50IHdoZW4gY29ubmVjdGluZyB0byB0aGUgTVFUVFxuICAgICAgICAjIGJyb2tlci4gQSBjbGllbnQgaWQgbXVzdCBiZSBubyBsb25nZXIgdGhhbiAyMyBjaGFyYWN0ZXJzLiBJZiBsZWZ0IGJsYW5rLFxuICAgICAgICAjIGEgcmFuZG9tIGlkIHdpbGwgYmUgZ2VuZXJhdGVkIGJ5IENoaXJwU3RhY2suXG4gICAgICAgIGNsaWVudF9pZD1cIlwiXG5cbiAgICAgICAgIyBLZWVwIGFsaXZlIGludGVydmFsLlxuICAgICAgICAjXG4gICAgICAgICMgVGhpcyBkZWZpbmVzIHRoZSBtYXhpbXVtIHRpbWUgdGhhdCB0aGF0IHNob3VsZCBwYXNzIHdpdGhvdXQgY29tbXVuaWNhdGlvblxuICAgICAgICAjIGJldHdlZW4gdGhlIGNsaWVudCBhbmQgc2VydmVyLlxuICAgICAgICBrZWVwX2FsaXZlX2ludGVydmFsPVwiMzBzXCJcblxuICAgICAgICAjIENBIGNlcnRpZmljYXRlIGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICAjXG4gICAgICAgICMgVXNlIHRoaXMgd2hlbiBzZXR0aW5nIHVwIGEgc2VjdXJlIGNvbm5lY3Rpb24gKHdoZW4gc2VydmVyIHVzZXMgc3NsOi8vLi4uKVxuICAgICAgICAjIGJ1dCB0aGUgY2VydGlmaWNhdGUgdXNlZCBieSB0aGUgc2VydmVyIGlzIG5vdCB0cnVzdGVkIGJ5IGFueSBDQSBjZXJ0aWZpY2F0ZVxuICAgICAgICAjIG9uIHRoZSBzZXJ2ZXIgKGUuZy4gd2hlbiBzZWxmIGdlbmVyYXRlZCkuXG4gICAgICAgIGNhX2NlcnQ9XCJcIlxuXG4gICAgICAgICMgVExTIGNlcnRpZmljYXRlIGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICB0bHNfY2VydD1cIlwiXG5cbiAgICAgICAgIyBUTFMga2V5IGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICB0bHNfa2V5PVwiXCJcblxuXG4gICAgIyBHYXRld2F5IGNoYW5uZWwgY29uZmlndXJhdGlvbi5cbiAgICAjXG4gICAgIyBOb3RlOiB0aGlzIGNvbmZpZ3VyYXRpb24gaXMgb25seSB1c2VkIGluIGNhc2UgdGhlIGdhdGV3YXkgaXMgdXNpbmcgdGhlXG4gICAgIyBDaGlycFN0YWNrIENvbmNlbnRyYXRvcmQgZGFlbW9uLiBJbiBhbnkgb3RoZXIgY2FzZSwgdGhpcyBjb25maWd1cmF0aW9uIFxuICAgICMgaXMgaWdub3JlZC5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9Nzc5NTAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT03Nzk3MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTc3OTkwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cblxuICAjIFJlZ2lvbiBzcGVjaWZpYyBuZXR3b3JrIGNvbmZpZ3VyYXRpb24uXG4gIFtyZWdpb25zLm5ldHdvcmtdXG4gICAgXG4gICAgIyBJbnN0YWxsYXRpb24gbWFyZ2luIChkQikgdXNlZCBieSB0aGUgQURSIGVuZ2luZS5cbiAgICAjXG4gICAgIyBBIGhpZ2hlciBudW1iZXIgbWVhbnMgdGhhdCB0aGUgbmV0d29yay1zZXJ2ZXIgd2lsbCBrZWVwIG1vcmUgbWFyZ2luLFxuICAgICMgcmVzdWx0aW5nIGluIGEgbG93ZXIgZGF0YS1yYXRlIGJ1dCBkZWNyZWFzaW5nIHRoZSBjaGFuY2UgdGhhdCB0aGVcbiAgICAjIGRldmljZSBnZXRzIGRpc2Nvbm5lY3RlZCBiZWNhdXNlIGl0IGlzIHVuYWJsZSB0byByZWFjaCBvbmUgb2YgdGhlXG4gICAgIyBzdXJyb3VuZGVkIGdhdGV3YXlzLlxuICAgIGluc3RhbGxhdGlvbl9tYXJnaW49MTBcblxuICAgICMgUlggd2luZG93IChDbGFzcy1BKS5cbiAgICAjXG4gICAgIyBTZXQgdGhpcyB0bzpcbiAgICAjIDA6IFJYMSAvIFJYMlxuICAgICMgMTogUlgxIG9ubHlcbiAgICAjIDI6IFJYMiBvbmx5XG4gICAgcnhfd2luZG93PTBcblxuICAgICMgUlgxIGRlbGF5ICgxIC0gMTUgc2Vjb25kcykuXG4gICAgcngxX2RlbGF5PTFcblxuICAgICMgUlgxIGRhdGEtcmF0ZSBvZmZzZXRcbiAgICByeDFfZHJfb2Zmc2V0PTBcblxuICAgICMgUlgyIGRhdGEtcmF0ZVxuICAgIHJ4Ml9kcj0wXG5cbiAgICAjIFJYMiBmcmVxdWVuY3kgKEh6KVxuICAgIHJ4Ml9mcmVxdWVuY3k9Nzg2MDAwMDAwXG5cbiAgICAjIFByZWZlciBSWDIgb24gUlgxIGRhdGEtcmF0ZSBsZXNzIHRoYW4uXG4gICAgI1xuICAgICMgUHJlZmVyIFJYMiBvdmVyIFJYMSBiYXNlZCBvbiB0aGUgUlgxIGRhdGEtcmF0ZS4gV2hlbiB0aGUgUlgxIGRhdGEtcmF0ZVxuICAgICMgaXMgc21hbGxlciB0aGFuIHRoZSBjb25maWd1cmVkIHZhbHVlLCB0aGVuIHRoZSBOZXR3b3JrIFNlcnZlciB3aWxsXG4gICAgIyBmaXJzdCB0cnkgdG8gc2NoZWR1bGUgdGhlIGRvd25saW5rIGZvciBSWDIsIGZhaWxpbmcgdGhhdCAoZS5nLiB0aGUgZ2F0ZXdheVxuICAgICMgaGFzIGFscmVhZHkgYSBwYXlsb2FkIHNjaGVkdWxlZCBhdCB0aGUgUlgyIHRpbWluZykgaXQgd2lsbCB0cnkgUlgxLlxuICAgIHJ4Ml9wcmVmZXJfb25fcngxX2RyX2x0PTBcblxuICAgICMgUHJlZmVyIFJYMiBvbiBsaW5rIGJ1ZGdldC5cbiAgICAjXG4gICAgIyBXaGVuIHRoZSBsaW5rLWJ1ZGdldCBpcyBiZXR0ZXIgZm9yIFJYMiB0aGFuIGZvciBSWDEsIHRoZSBOZXR3b3JrIFNlcnZlciB3aWxsIGZpcnN0XG4gICAgIyB0cnkgdG8gc2NoZWR1bGUgdGhlIGRvd25saW5rIGluIFJYMiwgZmFpbGluZyB0aGF0IGl0IHdpbGwgdHJ5IFJYMS5cbiAgICByeDJfcHJlZmVyX29uX2xpbmtfYnVkZ2V0PWZhbHNlXG5cbiAgICAjIERvd25saW5rIFRYIFBvd2VyIChkQm0pXG4gICAgI1xuICAgICMgV2hlbiBzZXQgdG8gLTEsIHRoZSBkb3dubGluayBUWCBQb3dlciBmcm9tIHRoZSBjb25maWd1cmVkIGJhbmQgd2lsbFxuICAgICMgYmUgdXNlZC5cbiAgICAjXG4gICAgIyBQbGVhc2UgY29uc3VsdCB0aGUgTG9SYVdBTiBSZWdpb25hbCBQYXJhbWV0ZXJzIGFuZCBsb2NhbCByZWd1bGF0aW9uc1xuICAgICMgZm9yIHZhbGlkIGFuZCBsZWdhbCBvcHRpb25zLiBOb3RlIHRoYXQgdGhlIGNvbmZpZ3VyZWQgVFggUG93ZXIgbXVzdCBiZVxuICAgICMgc3VwcG9ydGVkIGJ5IHlvdXIgZ2F0ZXdheShzKS5cbiAgICBkb3dubGlua190eF9wb3dlcj0tMVxuXG4gICAgIyBBRFIgaXMgZGlzYWJsZWQuXG4gICAgYWRyX2Rpc2FibGVkPWZhbHNlXG5cbiAgICAjIE1pbmltdW0gZGF0YS1yYXRlLlxuICAgIG1pbl9kcj0wXG5cbiAgICAjIE1heGltdW0gZGF0YS1yYXRlLlxuICAgIG1heF9kcj01XG5cblxuICAgICMgUmVqb2luLXJlcXVlc3QgY29uZmlndXJhdGlvbiAoTG9SYVdBTiAxLjEpXG4gICAgW3JlZ2lvbnMubmV0d29yay5yZWpvaW5fcmVxdWVzdF1cblxuICAgICAgIyBSZXF1ZXN0IGRldmljZXMgdG8gcGVyaW9kaWNhbGx5IHNlbmQgcmVqb2luLXJlcXVlc3RzLlxuICAgICAgZW5hYmxlZD1mYWxzZVxuXG4gICAgICAjIFRoZSBkZXZpY2UgbXVzdCBzZW5kIGEgcmVqb2luLXJlcXVlc3QgdHlwZSAwIGF0IGxlYXN0IGV2ZXJ5IDJeKG1heF9jb3VudF9uICsgNClcbiAgICAgICMgdXBsaW5rIG1lc3NhZ2VzLiBWYWxpZCB2YWx1ZXMgYXJlIDAgdG8gMTUuXG4gICAgICBtYXhfY291bnRfbj0wXG5cbiAgICAgICMgVGhlIGRldmljZSBtdXN0IHNlbmQgYSByZWpvaW4tcmVxdWVzdCB0eXBlIDAgYXQgbGVhc3QgZXZlcnkgMl4obWF4X3RpbWVfbiArIDEwKVxuICAgICAgIyBzZWNvbmRzLiBWYWxpZCB2YWx1ZXMgYXJlIDAgdG8gMTUuXG4gICAgICAjXG4gICAgICAjIDAgID0gcm91Z2hseSAxNyBtaW51dGVzXG4gICAgICAjIDE1ID0gYWJvdXQgMSB5ZWFyXG4gICAgICBtYXhfdGltZV9uPTBcbiAgICBcblxuICAgICMgQ2xhc3MtQiBjb25maWd1cmF0aW9uLlxuICAgIFtyZWdpb25zLm5ldHdvcmsuY2xhc3NfYl1cblxuICAgICAgIyBQaW5nLXNsb3QgZGF0YS1yYXRlLiBcbiAgICAgIHBpbmdfc2xvdF9kcj0zXG5cbiAgICAgICMgUGluZy1zbG90IGZyZXF1ZW5jeSAoSHopXG4gICAgICAjXG4gICAgICAjIHNldCB0aGlzIHRvIDAgdG8gdXNlIHRoZSBkZWZhdWx0IGZyZXF1ZW5jeSBwbGFuIGZvciB0aGUgY29uZmlndXJlZCByZWdpb25cbiAgICAgICMgKHdoaWNoIGNvdWxkIGJlIGZyZXF1ZW5jeSBob3BwaW5nKS5cbiAgICAgIHBpbmdfc2xvdF9mcmVxdWVuY3k9MFxuXCJcIlwiXG5cbltbY29uZmlnLm1vdW50c11dXG5zZXJ2aWNlTmFtZSA9IFwiY2hpcnBzdGFja1wiXG5maWxlUGF0aCA9IFwiL2NoaXJwc3RhY2svcmVnaW9uX2V1NDMzLnRvbWxcIlxuY29udGVudCA9IFwiXCJcIlxuIyBUaGlzIGZpbGUgY29udGFpbnMgYW4gZXhhbXBsZSBFVTQzMyBjb25maWd1cmF0aW9uLlxuW1tyZWdpb25zXV1cblxuICAjIElEIGlzIGFuIHVzZXItZGVmaW5lZCBpZGVudGlmaWVyIGZvciB0aGlzIHJlZ2lvbi5cbiAgaWQ9XCJldTQzM1wiXG5cbiAgIyBEZXNjcmlwdGlvbiBpcyBhIHNob3J0IGRlc2NyaXB0aW9uIGZvciB0aGlzIHJlZ2lvbi5cbiAgZGVzY3JpcHRpb249XCJFVTQ0M1wiXG5cbiAgIyBDb21tb24tbmFtZSByZWZlcnMgdG8gdGhlIGNvbW1vbi1uYW1lIG9mIHRoaXMgcmVnaW9uIGFzIGRlZmluZWQgYnlcbiAgIyB0aGUgTG9SYSBBbGxpYW5jZS5cbiAgY29tbW9uX25hbWU9XCJFVTQzM1wiXG5cblxuICAjIEdhdGV3YXkgY29uZmlndXJhdGlvbi5cbiAgW3JlZ2lvbnMuZ2F0ZXdheV1cblxuICAgICMgRm9yY2UgZ2F0ZXdheXMgYXMgcHJpdmF0ZS5cbiAgICAjXG4gICAgIyBJZiBlbmFibGVkLCBnYXRld2F5cyBjYW4gb25seSBiZSB1c2VkIGJ5IGRldmljZXMgdW5kZXIgdGhlIHNhbWUgdGVuYW50LlxuICAgIGZvcmNlX2d3c19wcml2YXRlPWZhbHNlXG5cblxuICAgICMgR2F0ZXdheSBiYWNrZW5kIGNvbmZpZ3VyYXRpb24uXG4gICAgW3JlZ2lvbnMuZ2F0ZXdheS5iYWNrZW5kXVxuXG4gICAgICAjIFRoZSBlbmFibGVkIGJhY2tlbmQgdHlwZS5cbiAgICAgIGVuYWJsZWQ9XCJtcXR0XCJcblxuICAgICAgIyBNUVRUIGNvbmZpZ3VyYXRpb24uXG4gICAgICBbcmVnaW9ucy5nYXRld2F5LmJhY2tlbmQubXF0dF1cblxuICAgICAgICAjIFRvcGljIHByZWZpeC5cbiAgICAgICAgI1xuICAgICAgICAjIFRoZSB0b3BpYyBwcmVmaXggY2FuIGJlIHVzZWQgdG8gZGVmaW5lIHRoZSByZWdpb24gb2YgdGhlIGdhdGV3YXkuXG4gICAgICAgICMgTm90ZSwgdGhlcmUgaXMgbm8gbmVlZCB0byBhZGQgYSB0cmFpbGluZyAnLycgdG8gdGhlIHByZWZpeC4gVGhlIHRyYWlsaW5nXG4gICAgICAgICMgJy8nIGlzIGF1dG9tYXRpY2FsbHkgYWRkZWQgdG8gdGhlIHByZWZpeCBpZiBpdCBpcyBjb25maWd1cmVkLlxuICAgICAgICB0b3BpY19wcmVmaXg9XCJldTQzM1wiXG5cbiAgICAgICAgIyBNUVRUIHNlcnZlciAoZS5nLiBzY2hlbWU6Ly9ob3N0OnBvcnQgd2hlcmUgc2NoZW1lIGlzIHRjcCwgc3NsIG9yIHdzKVxuICAgICAgICBzZXJ2ZXI9XCJ0Y3A6Ly9tb3NxdWl0dG86MTg4M1wiXG5cbiAgICAgICAgIyBDb25uZWN0IHdpdGggdGhlIGdpdmVuIHVzZXJuYW1lIChvcHRpb25hbClcbiAgICAgICAgdXNlcm5hbWU9XCJcIlxuXG4gICAgICAgICMgQ29ubmVjdCB3aXRoIHRoZSBnaXZlbiBwYXNzd29yZCAob3B0aW9uYWwpXG4gICAgICAgIHBhc3N3b3JkPVwiXCJcblxuICAgICAgICAjIFF1YWxpdHkgb2Ygc2VydmljZSBsZXZlbFxuICAgICAgICAjXG4gICAgICAgICMgMDogYXQgbW9zdCBvbmNlXG4gICAgICAgICMgMTogYXQgbGVhc3Qgb25jZVxuICAgICAgICAjIDI6IGV4YWN0bHkgb25jZVxuICAgICAgICAjXG4gICAgICAgICMgTm90ZTogYW4gaW5jcmVhc2Ugb2YgdGhpcyB2YWx1ZSB3aWxsIGRlY3JlYXNlIHRoZSBwZXJmb3JtYW5jZS5cbiAgICAgICAgIyBGb3IgbW9yZSBpbmZvcm1hdGlvbjogaHR0cHM6Ly93d3cuaGl2ZW1xLmNvbS9ibG9nL21xdHQtZXNzZW50aWFscy1wYXJ0LTYtbXF0dC1xdWFsaXR5LW9mLXNlcnZpY2UtbGV2ZWxzXG4gICAgICAgIHFvcz0wXG5cbiAgICAgICAgIyBDbGVhbiBzZXNzaW9uXG4gICAgICAgICNcbiAgICAgICAgIyBTZXQgdGhlIFwiY2xlYW4gc2Vzc2lvblwiIGZsYWcgaW4gdGhlIGNvbm5lY3QgbWVzc2FnZSB3aGVuIHRoaXMgY2xpZW50XG4gICAgICAgICMgY29ubmVjdHMgdG8gYW4gTVFUVCBicm9rZXIuIEJ5IHNldHRpbmcgdGhpcyBmbGFnIHlvdSBhcmUgaW5kaWNhdGluZ1xuICAgICAgICAjIHRoYXQgbm8gbWVzc2FnZXMgc2F2ZWQgYnkgdGhlIGJyb2tlciBmb3IgdGhpcyBjbGllbnQgc2hvdWxkIGJlIGRlbGl2ZXJlZC5cbiAgICAgICAgY2xlYW5fc2Vzc2lvbj1mYWxzZVxuXG4gICAgICAgICMgQ2xpZW50IElEXG4gICAgICAgICNcbiAgICAgICAgIyBTZXQgdGhlIGNsaWVudCBpZCB0byBiZSB1c2VkIGJ5IHRoaXMgY2xpZW50IHdoZW4gY29ubmVjdGluZyB0byB0aGUgTVFUVFxuICAgICAgICAjIGJyb2tlci4gQSBjbGllbnQgaWQgbXVzdCBiZSBubyBsb25nZXIgdGhhbiAyMyBjaGFyYWN0ZXJzLiBJZiBsZWZ0IGJsYW5rLFxuICAgICAgICAjIGEgcmFuZG9tIGlkIHdpbGwgYmUgZ2VuZXJhdGVkIGJ5IENoaXJwU3RhY2suXG4gICAgICAgIGNsaWVudF9pZD1cIlwiXG5cbiAgICAgICAgIyBLZWVwIGFsaXZlIGludGVydmFsLlxuICAgICAgICAjXG4gICAgICAgICMgVGhpcyBkZWZpbmVzIHRoZSBtYXhpbXVtIHRpbWUgdGhhdCB0aGF0IHNob3VsZCBwYXNzIHdpdGhvdXQgY29tbXVuaWNhdGlvblxuICAgICAgICAjIGJldHdlZW4gdGhlIGNsaWVudCBhbmQgc2VydmVyLlxuICAgICAgICBrZWVwX2FsaXZlX2ludGVydmFsPVwiMzBzXCJcblxuICAgICAgICAjIENBIGNlcnRpZmljYXRlIGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICAjXG4gICAgICAgICMgVXNlIHRoaXMgd2hlbiBzZXR0aW5nIHVwIGEgc2VjdXJlIGNvbm5lY3Rpb24gKHdoZW4gc2VydmVyIHVzZXMgc3NsOi8vLi4uKVxuICAgICAgICAjIGJ1dCB0aGUgY2VydGlmaWNhdGUgdXNlZCBieSB0aGUgc2VydmVyIGlzIG5vdCB0cnVzdGVkIGJ5IGFueSBDQSBjZXJ0aWZpY2F0ZVxuICAgICAgICAjIG9uIHRoZSBzZXJ2ZXIgKGUuZy4gd2hlbiBzZWxmIGdlbmVyYXRlZCkuXG4gICAgICAgIGNhX2NlcnQ9XCJcIlxuXG4gICAgICAgICMgVExTIGNlcnRpZmljYXRlIGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICB0bHNfY2VydD1cIlwiXG5cbiAgICAgICAgIyBUTFMga2V5IGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICB0bHNfa2V5PVwiXCJcblxuXG4gICAgIyBHYXRld2F5IGNoYW5uZWwgY29uZmlndXJhdGlvbi5cbiAgICAjXG4gICAgIyBOb3RlOiB0aGlzIGNvbmZpZ3VyYXRpb24gaXMgb25seSB1c2VkIGluIGNhc2UgdGhlIGdhdGV3YXkgaXMgdXNpbmcgdGhlXG4gICAgIyBDaGlycFN0YWNrIENvbmNlbnRyYXRvcmQgZGFlbW9uLiBJbiBhbnkgb3RoZXIgY2FzZSwgdGhpcyBjb25maWd1cmF0aW9uIFxuICAgICMgaXMgaWdub3JlZC5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9NDMzMTc1MDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT00MzMzNzUwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTQzMzU3NTAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cblxuICAjIFJlZ2lvbiBzcGVjaWZpYyBuZXR3b3JrIGNvbmZpZ3VyYXRpb24uXG4gIFtyZWdpb25zLm5ldHdvcmtdXG4gICAgXG4gICAgIyBJbnN0YWxsYXRpb24gbWFyZ2luIChkQikgdXNlZCBieSB0aGUgQURSIGVuZ2luZS5cbiAgICAjXG4gICAgIyBBIGhpZ2hlciBudW1iZXIgbWVhbnMgdGhhdCB0aGUgbmV0d29yay1zZXJ2ZXIgd2lsbCBrZWVwIG1vcmUgbWFyZ2luLFxuICAgICMgcmVzdWx0aW5nIGluIGEgbG93ZXIgZGF0YS1yYXRlIGJ1dCBkZWNyZWFzaW5nIHRoZSBjaGFuY2UgdGhhdCB0aGVcbiAgICAjIGRldmljZSBnZXRzIGRpc2Nvbm5lY3RlZCBiZWNhdXNlIGl0IGlzIHVuYWJsZSB0byByZWFjaCBvbmUgb2YgdGhlXG4gICAgIyBzdXJyb3VuZGVkIGdhdGV3YXlzLlxuICAgIGluc3RhbGxhdGlvbl9tYXJnaW49MTBcblxuICAgICMgUlggd2luZG93IChDbGFzcy1BKS5cbiAgICAjXG4gICAgIyBTZXQgdGhpcyB0bzpcbiAgICAjIDA6IFJYMSAvIFJYMlxuICAgICMgMTogUlgxIG9ubHlcbiAgICAjIDI6IFJYMiBvbmx5XG4gICAgcnhfd2luZG93PTBcblxuICAgICMgUlgxIGRlbGF5ICgxIC0gMTUgc2Vjb25kcykuXG4gICAgcngxX2RlbGF5PTFcblxuICAgICMgUlgxIGRhdGEtcmF0ZSBvZmZzZXRcbiAgICByeDFfZHJfb2Zmc2V0PTBcblxuICAgICMgUlgyIGRhdGEtcmF0ZVxuICAgIHJ4Ml9kcj0wXG5cbiAgICAjIFJYMiBmcmVxdWVuY3kgKEh6KVxuICAgIHJ4Ml9mcmVxdWVuY3k9NDM0NjY1MDAwXG5cbiAgICAjIFByZWZlciBSWDIgb24gUlgxIGRhdGEtcmF0ZSBsZXNzIHRoYW4uXG4gICAgI1xuICAgICMgUHJlZmVyIFJYMiBvdmVyIFJYMSBiYXNlZCBvbiB0aGUgUlgxIGRhdGEtcmF0ZS4gV2hlbiB0aGUgUlgxIGRhdGEtcmF0ZVxuICAgICMgaXMgc21hbGxlciB0aGFuIHRoZSBjb25maWd1cmVkIHZhbHVlLCB0aGVuIHRoZSBOZXR3b3JrIFNlcnZlciB3aWxsXG4gICAgIyBmaXJzdCB0cnkgdG8gc2NoZWR1bGUgdGhlIGRvd25saW5rIGZvciBSWDIsIGZhaWxpbmcgdGhhdCAoZS5nLiB0aGUgZ2F0ZXdheVxuICAgICMgaGFzIGFscmVhZHkgYSBwYXlsb2FkIHNjaGVkdWxlZCBhdCB0aGUgUlgyIHRpbWluZykgaXQgd2lsbCB0cnkgUlgxLlxuICAgIHJ4Ml9wcmVmZXJfb25fcngxX2RyX2x0PTBcblxuICAgICMgUHJlZmVyIFJYMiBvbiBsaW5rIGJ1ZGdldC5cbiAgICAjXG4gICAgIyBXaGVuIHRoZSBsaW5rLWJ1ZGdldCBpcyBiZXR0ZXIgZm9yIFJYMiB0aGFuIGZvciBSWDEsIHRoZSBOZXR3b3JrIFNlcnZlciB3aWxsIGZpcnN0XG4gICAgIyB0cnkgdG8gc2NoZWR1bGUgdGhlIGRvd25saW5rIGluIFJYMiwgZmFpbGluZyB0aGF0IGl0IHdpbGwgdHJ5IFJYMS5cbiAgICByeDJfcHJlZmVyX29uX2xpbmtfYnVkZ2V0PWZhbHNlXG5cbiAgICAjIERvd25saW5rIFRYIFBvd2VyIChkQm0pXG4gICAgI1xuICAgICMgV2hlbiBzZXQgdG8gLTEsIHRoZSBkb3dubGluayBUWCBQb3dlciBmcm9tIHRoZSBjb25maWd1cmVkIGJhbmQgd2lsbFxuICAgICMgYmUgdXNlZC5cbiAgICAjXG4gICAgIyBQbGVhc2UgY29uc3VsdCB0aGUgTG9SYVdBTiBSZWdpb25hbCBQYXJhbWV0ZXJzIGFuZCBsb2NhbCByZWd1bGF0aW9uc1xuICAgICMgZm9yIHZhbGlkIGFuZCBsZWdhbCBvcHRpb25zLiBOb3RlIHRoYXQgdGhlIGNvbmZpZ3VyZWQgVFggUG93ZXIgbXVzdCBiZVxuICAgICMgc3VwcG9ydGVkIGJ5IHlvdXIgZ2F0ZXdheShzKS5cbiAgICBkb3dubGlua190eF9wb3dlcj0tMVxuXG4gICAgIyBBRFIgaXMgZGlzYWJsZWQuXG4gICAgYWRyX2Rpc2FibGVkPWZhbHNlXG5cbiAgICAjIE1pbmltdW0gZGF0YS1yYXRlLlxuICAgIG1pbl9kcj0wXG5cbiAgICAjIE1heGltdW0gZGF0YS1yYXRlLlxuICAgIG1heF9kcj01XG5cblxuICAgICMgUmVqb2luLXJlcXVlc3QgY29uZmlndXJhdGlvbiAoTG9SYVdBTiAxLjEpXG4gICAgW3JlZ2lvbnMubmV0d29yay5yZWpvaW5fcmVxdWVzdF1cblxuICAgICAgIyBSZXF1ZXN0IGRldmljZXMgdG8gcGVyaW9kaWNhbGx5IHNlbmQgcmVqb2luLXJlcXVlc3RzLlxuICAgICAgZW5hYmxlZD1mYWxzZVxuXG4gICAgICAjIFRoZSBkZXZpY2UgbXVzdCBzZW5kIGEgcmVqb2luLXJlcXVlc3QgdHlwZSAwIGF0IGxlYXN0IGV2ZXJ5IDJeKG1heF9jb3VudF9uICsgNClcbiAgICAgICMgdXBsaW5rIG1lc3NhZ2VzLiBWYWxpZCB2YWx1ZXMgYXJlIDAgdG8gMTUuXG4gICAgICBtYXhfY291bnRfbj0wXG5cbiAgICAgICMgVGhlIGRldmljZSBtdXN0IHNlbmQgYSByZWpvaW4tcmVxdWVzdCB0eXBlIDAgYXQgbGVhc3QgZXZlcnkgMl4obWF4X3RpbWVfbiArIDEwKVxuICAgICAgIyBzZWNvbmRzLiBWYWxpZCB2YWx1ZXMgYXJlIDAgdG8gMTUuXG4gICAgICAjXG4gICAgICAjIDAgID0gcm91Z2hseSAxNyBtaW51dGVzXG4gICAgICAjIDE1ID0gYWJvdXQgMSB5ZWFyXG4gICAgICBtYXhfdGltZV9uPTBcbiAgICBcblxuICAgICMgQ2xhc3MtQiBjb25maWd1cmF0aW9uLlxuICAgIFtyZWdpb25zLm5ldHdvcmsuY2xhc3NfYl1cblxuICAgICAgIyBQaW5nLXNsb3QgZGF0YS1yYXRlLiBcbiAgICAgIHBpbmdfc2xvdF9kcj0zXG5cbiAgICAgICMgUGluZy1zbG90IGZyZXF1ZW5jeSAoSHopXG4gICAgICAjXG4gICAgICAjIHNldCB0aGlzIHRvIDAgdG8gdXNlIHRoZSBkZWZhdWx0IGZyZXF1ZW5jeSBwbGFuIGZvciB0aGUgY29uZmlndXJlZCByZWdpb25cbiAgICAgICMgKHdoaWNoIGNvdWxkIGJlIGZyZXF1ZW5jeSBob3BwaW5nKS5cbiAgICAgIHBpbmdfc2xvdF9mcmVxdWVuY3k9MFxuXCJcIlwiXG5cbltbY29uZmlnLm1vdW50c11dXG5zZXJ2aWNlTmFtZSA9IFwiY2hpcnBzdGFja1wiXG5maWxlUGF0aCA9IFwiL2NoaXJwc3RhY2svcmVnaW9uX2V1ODY4LnRvbWxcIlxuY29udGVudCA9IFwiXCJcIlxuIyBUaGlzIGZpbGUgY29udGFpbnMgYW4gZXhhbXBsZSBFVTg2OCBjb25maWd1cmF0aW9uLlxuW1tyZWdpb25zXV1cblxuICAjIElEIGlzIGFuIHVzZXItZGVmaW5lZCBpZGVudGlmaWVyIGZvciB0aGlzIHJlZ2lvbi5cbiAgaWQ9XCJldTg2OFwiXG5cbiAgIyBEZXNjcmlwdGlvbiBpcyBhIHNob3J0IGRlc2NyaXB0aW9uIGZvciB0aGlzIHJlZ2lvbi5cbiAgZGVzY3JpcHRpb249XCJFVTg2OFwiXG5cbiAgIyBDb21tb24tbmFtZSByZWZlcnMgdG8gdGhlIGNvbW1vbi1uYW1lIG9mIHRoaXMgcmVnaW9uIGFzIGRlZmluZWQgYnlcbiAgIyB0aGUgTG9SYSBBbGxpYW5jZS5cbiAgY29tbW9uX25hbWU9XCJFVTg2OFwiXG5cblxuICAjIEdhdGV3YXkgY29uZmlndXJhdGlvbi5cbiAgW3JlZ2lvbnMuZ2F0ZXdheV1cblxuICAgICMgRm9yY2UgZ2F0ZXdheXMgYXMgcHJpdmF0ZS5cbiAgICAjXG4gICAgIyBJZiBlbmFibGVkLCBnYXRld2F5cyBjYW4gb25seSBiZSB1c2VkIGJ5IGRldmljZXMgdW5kZXIgdGhlIHNhbWUgdGVuYW50LlxuICAgIGZvcmNlX2d3c19wcml2YXRlPWZhbHNlXG5cblxuICAgICMgR2F0ZXdheSBiYWNrZW5kIGNvbmZpZ3VyYXRpb24uXG4gICAgW3JlZ2lvbnMuZ2F0ZXdheS5iYWNrZW5kXVxuXG4gICAgICAjIFRoZSBlbmFibGVkIGJhY2tlbmQgdHlwZS5cbiAgICAgIGVuYWJsZWQ9XCJtcXR0XCJcblxuICAgICAgIyBNUVRUIGNvbmZpZ3VyYXRpb24uXG4gICAgICBbcmVnaW9ucy5nYXRld2F5LmJhY2tlbmQubXF0dF1cblxuICAgICAgICAjIFRvcGljIHByZWZpeC5cbiAgICAgICAgI1xuICAgICAgICAjIFRoZSB0b3BpYyBwcmVmaXggY2FuIGJlIHVzZWQgdG8gZGVmaW5lIHRoZSByZWdpb24gb2YgdGhlIGdhdGV3YXkuXG4gICAgICAgICMgTm90ZSwgdGhlcmUgaXMgbm8gbmVlZCB0byBhZGQgYSB0cmFpbGluZyAnLycgdG8gdGhlIHByZWZpeC4gVGhlIHRyYWlsaW5nXG4gICAgICAgICMgJy8nIGlzIGF1dG9tYXRpY2FsbHkgYWRkZWQgdG8gdGhlIHByZWZpeCBpZiBpdCBpcyBjb25maWd1cmVkLlxuICAgICAgICB0b3BpY19wcmVmaXg9XCJldTg2OFwiXG5cbiAgICAgICAgIyBNUVRUIHNlcnZlciAoZS5nLiBzY2hlbWU6Ly9ob3N0OnBvcnQgd2hlcmUgc2NoZW1lIGlzIHRjcCwgc3NsIG9yIHdzKVxuICAgICAgICBzZXJ2ZXI9XCJ0Y3A6Ly9tb3NxdWl0dG86MTg4M1wiXG5cbiAgICAgICAgIyBDb25uZWN0IHdpdGggdGhlIGdpdmVuIHVzZXJuYW1lIChvcHRpb25hbClcbiAgICAgICAgdXNlcm5hbWU9XCJcIlxuXG4gICAgICAgICMgQ29ubmVjdCB3aXRoIHRoZSBnaXZlbiBwYXNzd29yZCAob3B0aW9uYWwpXG4gICAgICAgIHBhc3N3b3JkPVwiXCJcblxuICAgICAgICAjIFF1YWxpdHkgb2Ygc2VydmljZSBsZXZlbFxuICAgICAgICAjXG4gICAgICAgICMgMDogYXQgbW9zdCBvbmNlXG4gICAgICAgICMgMTogYXQgbGVhc3Qgb25jZVxuICAgICAgICAjIDI6IGV4YWN0bHkgb25jZVxuICAgICAgICAjXG4gICAgICAgICMgTm90ZTogYW4gaW5jcmVhc2Ugb2YgdGhpcyB2YWx1ZSB3aWxsIGRlY3JlYXNlIHRoZSBwZXJmb3JtYW5jZS5cbiAgICAgICAgIyBGb3IgbW9yZSBpbmZvcm1hdGlvbjogaHR0cHM6Ly93d3cuaGl2ZW1xLmNvbS9ibG9nL21xdHQtZXNzZW50aWFscy1wYXJ0LTYtbXF0dC1xdWFsaXR5LW9mLXNlcnZpY2UtbGV2ZWxzXG4gICAgICAgIHFvcz0wXG5cbiAgICAgICAgIyBDbGVhbiBzZXNzaW9uXG4gICAgICAgICNcbiAgICAgICAgIyBTZXQgdGhlIFwiY2xlYW4gc2Vzc2lvblwiIGZsYWcgaW4gdGhlIGNvbm5lY3QgbWVzc2FnZSB3aGVuIHRoaXMgY2xpZW50XG4gICAgICAgICMgY29ubmVjdHMgdG8gYW4gTVFUVCBicm9rZXIuIEJ5IHNldHRpbmcgdGhpcyBmbGFnIHlvdSBhcmUgaW5kaWNhdGluZ1xuICAgICAgICAjIHRoYXQgbm8gbWVzc2FnZXMgc2F2ZWQgYnkgdGhlIGJyb2tlciBmb3IgdGhpcyBjbGllbnQgc2hvdWxkIGJlIGRlbGl2ZXJlZC5cbiAgICAgICAgY2xlYW5fc2Vzc2lvbj1mYWxzZVxuXG4gICAgICAgICMgQ2xpZW50IElEXG4gICAgICAgICNcbiAgICAgICAgIyBTZXQgdGhlIGNsaWVudCBpZCB0byBiZSB1c2VkIGJ5IHRoaXMgY2xpZW50IHdoZW4gY29ubmVjdGluZyB0byB0aGUgTVFUVFxuICAgICAgICAjIGJyb2tlci4gQSBjbGllbnQgaWQgbXVzdCBiZSBubyBsb25nZXIgdGhhbiAyMyBjaGFyYWN0ZXJzLiBJZiBsZWZ0IGJsYW5rLFxuICAgICAgICAjIGEgcmFuZG9tIGlkIHdpbGwgYmUgZ2VuZXJhdGVkIGJ5IENoaXJwU3RhY2suXG4gICAgICAgIGNsaWVudF9pZD1cIlwiXG5cbiAgICAgICAgIyBLZWVwIGFsaXZlIGludGVydmFsLlxuICAgICAgICAjXG4gICAgICAgICMgVGhpcyBkZWZpbmVzIHRoZSBtYXhpbXVtIHRpbWUgdGhhdCB0aGF0IHNob3VsZCBwYXNzIHdpdGhvdXQgY29tbXVuaWNhdGlvblxuICAgICAgICAjIGJldHdlZW4gdGhlIGNsaWVudCBhbmQgc2VydmVyLlxuICAgICAgICBrZWVwX2FsaXZlX2ludGVydmFsPVwiMzBzXCJcblxuICAgICAgICAjIENBIGNlcnRpZmljYXRlIGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICAjXG4gICAgICAgICMgVXNlIHRoaXMgd2hlbiBzZXR0aW5nIHVwIGEgc2VjdXJlIGNvbm5lY3Rpb24gKHdoZW4gc2VydmVyIHVzZXMgc3NsOi8vLi4uKVxuICAgICAgICAjIGJ1dCB0aGUgY2VydGlmaWNhdGUgdXNlZCBieSB0aGUgc2VydmVyIGlzIG5vdCB0cnVzdGVkIGJ5IGFueSBDQSBjZXJ0aWZpY2F0ZVxuICAgICAgICAjIG9uIHRoZSBzZXJ2ZXIgKGUuZy4gd2hlbiBzZWxmIGdlbmVyYXRlZCkuXG4gICAgICAgIGNhX2NlcnQ9XCJcIlxuXG4gICAgICAgICMgVExTIGNlcnRpZmljYXRlIGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICB0bHNfY2VydD1cIlwiXG5cbiAgICAgICAgIyBUTFMga2V5IGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICB0bHNfa2V5PVwiXCJcblxuXG4gICAgIyBHYXRld2F5IGNoYW5uZWwgY29uZmlndXJhdGlvbi5cbiAgICAjXG4gICAgIyBOb3RlOiB0aGlzIGNvbmZpZ3VyYXRpb24gaXMgb25seSB1c2VkIGluIGNhc2UgdGhlIGdhdGV3YXkgaXMgdXNpbmcgdGhlXG4gICAgIyBDaGlycFN0YWNrIENvbmNlbnRyYXRvcmQgZGFlbW9uLiBJbiBhbnkgb3RoZXIgY2FzZSwgdGhpcyBjb25maWd1cmF0aW9uIFxuICAgICMgaXMgaWdub3JlZC5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9ODY4MTAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT04NjgzMDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTg2ODUwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9ODY3MTAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT04NjczMDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTg2NzUwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9ODY3NzAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT04Njc5MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuICBcbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9ODY4MzAwMDAwXG4gICAgICBiYW5kd2lkdGg9MjUwMDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bN11cbiAgICBcbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9ODY4ODAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiRlNLXCJcbiAgICAgIGRhdGFyYXRlPTUwMDAwXG5cblxuICAjIFJlZ2lvbiBzcGVjaWZpYyBuZXR3b3JrIGNvbmZpZ3VyYXRpb24uXG4gIFtyZWdpb25zLm5ldHdvcmtdXG4gICAgXG4gICAgIyBJbnN0YWxsYXRpb24gbWFyZ2luIChkQikgdXNlZCBieSB0aGUgQURSIGVuZ2luZS5cbiAgICAjXG4gICAgIyBBIGhpZ2hlciBudW1iZXIgbWVhbnMgdGhhdCB0aGUgbmV0d29yay1zZXJ2ZXIgd2lsbCBrZWVwIG1vcmUgbWFyZ2luLFxuICAgICMgcmVzdWx0aW5nIGluIGEgbG93ZXIgZGF0YS1yYXRlIGJ1dCBkZWNyZWFzaW5nIHRoZSBjaGFuY2UgdGhhdCB0aGVcbiAgICAjIGRldmljZSBnZXRzIGRpc2Nvbm5lY3RlZCBiZWNhdXNlIGl0IGlzIHVuYWJsZSB0byByZWFjaCBvbmUgb2YgdGhlXG4gICAgIyBzdXJyb3VuZGVkIGdhdGV3YXlzLlxuICAgIGluc3RhbGxhdGlvbl9tYXJnaW49MTBcblxuICAgICMgUlggd2luZG93IChDbGFzcy1BKS5cbiAgICAjXG4gICAgIyBTZXQgdGhpcyB0bzpcbiAgICAjIDA6IFJYMSAvIFJYMlxuICAgICMgMTogUlgxIG9ubHlcbiAgICAjIDI6IFJYMiBvbmx5XG4gICAgcnhfd2luZG93PTBcblxuICAgICMgUlgxIGRlbGF5ICgxIC0gMTUgc2Vjb25kcykuXG4gICAgcngxX2RlbGF5PTFcblxuICAgICMgUlgxIGRhdGEtcmF0ZSBvZmZzZXRcbiAgICByeDFfZHJfb2Zmc2V0PTBcblxuICAgICMgUlgyIGRhdGEtcmF0ZVxuICAgIHJ4Ml9kcj0wXG5cbiAgICAjIFJYMiBmcmVxdWVuY3kgKEh6KVxuICAgIHJ4Ml9mcmVxdWVuY3k9ODY5NTI1MDAwXG5cbiAgICAjIFByZWZlciBSWDIgb24gUlgxIGRhdGEtcmF0ZSBsZXNzIHRoYW4uXG4gICAgI1xuICAgICMgUHJlZmVyIFJYMiBvdmVyIFJYMSBiYXNlZCBvbiB0aGUgUlgxIGRhdGEtcmF0ZS4gV2hlbiB0aGUgUlgxIGRhdGEtcmF0ZVxuICAgICMgaXMgc21hbGxlciB0aGFuIHRoZSBjb25maWd1cmVkIHZhbHVlLCB0aGVuIHRoZSBOZXR3b3JrIFNlcnZlciB3aWxsXG4gICAgIyBmaXJzdCB0cnkgdG8gc2NoZWR1bGUgdGhlIGRvd25saW5rIGZvciBSWDIsIGZhaWxpbmcgdGhhdCAoZS5nLiB0aGUgZ2F0ZXdheVxuICAgICMgaGFzIGFscmVhZHkgYSBwYXlsb2FkIHNjaGVkdWxlZCBhdCB0aGUgUlgyIHRpbWluZykgaXQgd2lsbCB0cnkgUlgxLlxuICAgIHJ4Ml9wcmVmZXJfb25fcngxX2RyX2x0PTBcblxuICAgICMgUHJlZmVyIFJYMiBvbiBsaW5rIGJ1ZGdldC5cbiAgICAjXG4gICAgIyBXaGVuIHRoZSBsaW5rLWJ1ZGdldCBpcyBiZXR0ZXIgZm9yIFJYMiB0aGFuIGZvciBSWDEsIHRoZSBOZXR3b3JrIFNlcnZlciB3aWxsIGZpcnN0XG4gICAgIyB0cnkgdG8gc2NoZWR1bGUgdGhlIGRvd25saW5rIGluIFJYMiwgZmFpbGluZyB0aGF0IGl0IHdpbGwgdHJ5IFJYMS5cbiAgICByeDJfcHJlZmVyX29uX2xpbmtfYnVkZ2V0PWZhbHNlXG5cbiAgICAjIERvd25saW5rIFRYIFBvd2VyIChkQm0pXG4gICAgI1xuICAgICMgV2hlbiBzZXQgdG8gLTEsIHRoZSBkb3dubGluayBUWCBQb3dlciBmcm9tIHRoZSBjb25maWd1cmVkIGJhbmQgd2lsbFxuICAgICMgYmUgdXNlZC5cbiAgICAjXG4gICAgIyBQbGVhc2UgY29uc3VsdCB0aGUgTG9SYVdBTiBSZWdpb25hbCBQYXJhbWV0ZXJzIGFuZCBsb2NhbCByZWd1bGF0aW9uc1xuICAgICMgZm9yIHZhbGlkIGFuZCBsZWdhbCBvcHRpb25zLiBOb3RlIHRoYXQgdGhlIGNvbmZpZ3VyZWQgVFggUG93ZXIgbXVzdCBiZVxuICAgICMgc3VwcG9ydGVkIGJ5IHlvdXIgZ2F0ZXdheShzKS5cbiAgICBkb3dubGlua190eF9wb3dlcj0tMVxuXG4gICAgIyBBRFIgaXMgZGlzYWJsZWQuXG4gICAgYWRyX2Rpc2FibGVkPWZhbHNlXG5cbiAgICAjIE1pbmltdW0gZGF0YS1yYXRlLlxuICAgIG1pbl9kcj0wXG5cbiAgICAjIE1heGltdW0gZGF0YS1yYXRlLlxuICAgIG1heF9kcj01XG5cblxuICAgICMgUmVqb2luLXJlcXVlc3QgY29uZmlndXJhdGlvbiAoTG9SYVdBTiAxLjEpXG4gICAgW3JlZ2lvbnMubmV0d29yay5yZWpvaW5fcmVxdWVzdF1cblxuICAgICAgIyBSZXF1ZXN0IGRldmljZXMgdG8gcGVyaW9kaWNhbGx5IHNlbmQgcmVqb2luLXJlcXVlc3RzLlxuICAgICAgZW5hYmxlZD1mYWxzZVxuXG4gICAgICAjIFRoZSBkZXZpY2UgbXVzdCBzZW5kIGEgcmVqb2luLXJlcXVlc3QgdHlwZSAwIGF0IGxlYXN0IGV2ZXJ5IDJeKG1heF9jb3VudF9uICsgNClcbiAgICAgICMgdXBsaW5rIG1lc3NhZ2VzLiBWYWxpZCB2YWx1ZXMgYXJlIDAgdG8gMTUuXG4gICAgICBtYXhfY291bnRfbj0wXG5cbiAgICAgICMgVGhlIGRldmljZSBtdXN0IHNlbmQgYSByZWpvaW4tcmVxdWVzdCB0eXBlIDAgYXQgbGVhc3QgZXZlcnkgMl4obWF4X3RpbWVfbiArIDEwKVxuICAgICAgIyBzZWNvbmRzLiBWYWxpZCB2YWx1ZXMgYXJlIDAgdG8gMTUuXG4gICAgICAjXG4gICAgICAjIDAgID0gcm91Z2hseSAxNyBtaW51dGVzXG4gICAgICAjIDE1ID0gYWJvdXQgMSB5ZWFyXG4gICAgICBtYXhfdGltZV9uPTBcbiAgICBcblxuICAgICMgQ2xhc3MtQiBjb25maWd1cmF0aW9uLlxuICAgIFtyZWdpb25zLm5ldHdvcmsuY2xhc3NfYl1cblxuICAgICAgIyBQaW5nLXNsb3QgZGF0YS1yYXRlLiBcbiAgICAgIHBpbmdfc2xvdF9kcj0zXG5cbiAgICAgICMgUGluZy1zbG90IGZyZXF1ZW5jeSAoSHopXG4gICAgICAjXG4gICAgICAjIHNldCB0aGlzIHRvIDAgdG8gdXNlIHRoZSBkZWZhdWx0IGZyZXF1ZW5jeSBwbGFuIGZvciB0aGUgY29uZmlndXJlZCByZWdpb25cbiAgICAgICMgKHdoaWNoIGNvdWxkIGJlIGZyZXF1ZW5jeSBob3BwaW5nKS5cbiAgICAgIHBpbmdfc2xvdF9mcmVxdWVuY3k9MFxuXG5cbiAgICAjIEJlbG93IGlzIHRoZSBjb21tb24gc2V0IG9mIGV4dHJhIGNoYW5uZWxzLiBQbGVhc2UgbWFrZSBzdXJlIHRoYXQgdGhlc2VcbiAgICAjIGNoYW5uZWxzIGFyZSBhbHNvIHN1cHBvcnRlZCBieSB0aGUgZ2F0ZXdheXMuXG4gICAgW1tyZWdpb25zLm5ldHdvcmsuZXh0cmFfY2hhbm5lbHNdXVxuICAgIGZyZXF1ZW5jeT04NjcxMDAwMDBcbiAgICBtaW5fZHI9MFxuICAgIG1heF9kcj01XG5cbiAgICBbW3JlZ2lvbnMubmV0d29yay5leHRyYV9jaGFubmVsc11dXG4gICAgZnJlcXVlbmN5PTg2NzMwMDAwMFxuICAgIG1pbl9kcj0wXG4gICAgbWF4X2RyPTVcblxuICAgIFtbcmVnaW9ucy5uZXR3b3JrLmV4dHJhX2NoYW5uZWxzXV1cbiAgICBmcmVxdWVuY3k9ODY3NTAwMDAwXG4gICAgbWluX2RyPTBcbiAgICBtYXhfZHI9NVxuXG4gICAgW1tyZWdpb25zLm5ldHdvcmsuZXh0cmFfY2hhbm5lbHNdXVxuICAgIGZyZXF1ZW5jeT04Njc3MDAwMDBcbiAgICBtaW5fZHI9MFxuICAgIG1heF9kcj01XG5cbiAgICBbW3JlZ2lvbnMubmV0d29yay5leHRyYV9jaGFubmVsc11dXG4gICAgZnJlcXVlbmN5PTg2NzkwMDAwMFxuICAgIG1pbl9kcj0wXG4gICAgbWF4X2RyPTVcblwiXCJcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuc2VydmljZU5hbWUgPSBcImNoaXJwc3RhY2tcIlxuZmlsZVBhdGggPSBcIi9jaGlycHN0YWNrL3JlZ2lvbl9pbjg2NS50b21sXCJcbmNvbnRlbnQgPSBcIlwiXCJcbiMgVGhpcyBmaWxlIGNvbnRhaW5zIGFuIGV4YW1wbGUgSU44NjUgY29uZmlndXJhdGlvbi5cbltbcmVnaW9uc11dXG5cbiAgIyBJRCBpcyBhbiB1c2VyLWRlZmluZWQgaWRlbnRpZmllciBmb3IgdGhpcyByZWdpb24uXG4gIGlkPVwiaW44NjVcIlxuXG4gICMgRGVzY3JpcHRpb24gaXMgYSBzaG9ydCBkZXNjcmlwdGlvbiBmb3IgdGhpcyByZWdpb24uXG4gIGRlc2NyaXB0aW9uPVwiSU44NjVcIlxuXG4gICMgQ29tbW9uLW5hbWUgcmVmZXJzIHRvIHRoZSBjb21tb24tbmFtZSBvZiB0aGlzIHJlZ2lvbiBhcyBkZWZpbmVkIGJ5XG4gICMgdGhlIExvUmEgQWxsaWFuY2UuXG4gIGNvbW1vbl9uYW1lPVwiSU44NjVcIlxuXG5cbiAgIyBHYXRld2F5IGNvbmZpZ3VyYXRpb24uXG4gIFtyZWdpb25zLmdhdGV3YXldXG5cbiAgICAjIEZvcmNlIGdhdGV3YXlzIGFzIHByaXZhdGUuXG4gICAgI1xuICAgICMgSWYgZW5hYmxlZCwgZ2F0ZXdheXMgY2FuIG9ubHkgYmUgdXNlZCBieSBkZXZpY2VzIHVuZGVyIHRoZSBzYW1lIHRlbmFudC5cbiAgICBmb3JjZV9nd3NfcHJpdmF0ZT1mYWxzZVxuXG5cbiAgICAjIEdhdGV3YXkgYmFja2VuZCBjb25maWd1cmF0aW9uLlxuICAgIFtyZWdpb25zLmdhdGV3YXkuYmFja2VuZF1cblxuICAgICAgIyBUaGUgZW5hYmxlZCBiYWNrZW5kIHR5cGUuXG4gICAgICBlbmFibGVkPVwibXF0dFwiXG5cbiAgICAgICMgTVFUVCBjb25maWd1cmF0aW9uLlxuICAgICAgW3JlZ2lvbnMuZ2F0ZXdheS5iYWNrZW5kLm1xdHRdXG5cbiAgICAgICAgIyBUb3BpYyBwcmVmaXguXG4gICAgICAgICNcbiAgICAgICAgIyBUaGUgdG9waWMgcHJlZml4IGNhbiBiZSB1c2VkIHRvIGRlZmluZSB0aGUgcmVnaW9uIG9mIHRoZSBnYXRld2F5LlxuICAgICAgICAjIE5vdGUsIHRoZXJlIGlzIG5vIG5lZWQgdG8gYWRkIGEgdHJhaWxpbmcgJy8nIHRvIHRoZSBwcmVmaXguIFRoZSB0cmFpbGluZ1xuICAgICAgICAjICcvJyBpcyBhdXRvbWF0aWNhbGx5IGFkZGVkIHRvIHRoZSBwcmVmaXggaWYgaXQgaXMgY29uZmlndXJlZC5cbiAgICAgICAgdG9waWNfcHJlZml4PVwiaW44NjVcIlxuXG4gICAgICAgICMgTVFUVCBzZXJ2ZXIgKGUuZy4gc2NoZW1lOi8vaG9zdDpwb3J0IHdoZXJlIHNjaGVtZSBpcyB0Y3AsIHNzbCBvciB3cylcbiAgICAgICAgc2VydmVyPVwidGNwOi8vbW9zcXVpdHRvOjE4ODNcIlxuXG4gICAgICAgICMgQ29ubmVjdCB3aXRoIHRoZSBnaXZlbiB1c2VybmFtZSAob3B0aW9uYWwpXG4gICAgICAgIHVzZXJuYW1lPVwiXCJcblxuICAgICAgICAjIENvbm5lY3Qgd2l0aCB0aGUgZ2l2ZW4gcGFzc3dvcmQgKG9wdGlvbmFsKVxuICAgICAgICBwYXNzd29yZD1cIlwiXG5cbiAgICAgICAgIyBRdWFsaXR5IG9mIHNlcnZpY2UgbGV2ZWxcbiAgICAgICAgI1xuICAgICAgICAjIDA6IGF0IG1vc3Qgb25jZVxuICAgICAgICAjIDE6IGF0IGxlYXN0IG9uY2VcbiAgICAgICAgIyAyOiBleGFjdGx5IG9uY2VcbiAgICAgICAgI1xuICAgICAgICAjIE5vdGU6IGFuIGluY3JlYXNlIG9mIHRoaXMgdmFsdWUgd2lsbCBkZWNyZWFzZSB0aGUgcGVyZm9ybWFuY2UuXG4gICAgICAgICMgRm9yIG1vcmUgaW5mb3JtYXRpb246IGh0dHBzOi8vd3d3LmhpdmVtcS5jb20vYmxvZy9tcXR0LWVzc2VudGlhbHMtcGFydC02LW1xdHQtcXVhbGl0eS1vZi1zZXJ2aWNlLWxldmVsc1xuICAgICAgICBxb3M9MFxuXG4gICAgICAgICMgQ2xlYW4gc2Vzc2lvblxuICAgICAgICAjXG4gICAgICAgICMgU2V0IHRoZSBcImNsZWFuIHNlc3Npb25cIiBmbGFnIGluIHRoZSBjb25uZWN0IG1lc3NhZ2Ugd2hlbiB0aGlzIGNsaWVudFxuICAgICAgICAjIGNvbm5lY3RzIHRvIGFuIE1RVFQgYnJva2VyLiBCeSBzZXR0aW5nIHRoaXMgZmxhZyB5b3UgYXJlIGluZGljYXRpbmdcbiAgICAgICAgIyB0aGF0IG5vIG1lc3NhZ2VzIHNhdmVkIGJ5IHRoZSBicm9rZXIgZm9yIHRoaXMgY2xpZW50IHNob3VsZCBiZSBkZWxpdmVyZWQuXG4gICAgICAgIGNsZWFuX3Nlc3Npb249ZmFsc2VcblxuICAgICAgICAjIENsaWVudCBJRFxuICAgICAgICAjXG4gICAgICAgICMgU2V0IHRoZSBjbGllbnQgaWQgdG8gYmUgdXNlZCBieSB0aGlzIGNsaWVudCB3aGVuIGNvbm5lY3RpbmcgdG8gdGhlIE1RVFRcbiAgICAgICAgIyBicm9rZXIuIEEgY2xpZW50IGlkIG11c3QgYmUgbm8gbG9uZ2VyIHRoYW4gMjMgY2hhcmFjdGVycy4gSWYgbGVmdCBibGFuayxcbiAgICAgICAgIyBhIHJhbmRvbSBpZCB3aWxsIGJlIGdlbmVyYXRlZCBieSBDaGlycFN0YWNrLlxuICAgICAgICBjbGllbnRfaWQ9XCJcIlxuXG4gICAgICAgICMgS2VlcCBhbGl2ZSBpbnRlcnZhbC5cbiAgICAgICAgI1xuICAgICAgICAjIFRoaXMgZGVmaW5lcyB0aGUgbWF4aW11bSB0aW1lIHRoYXQgdGhhdCBzaG91bGQgcGFzcyB3aXRob3V0IGNvbW11bmljYXRpb25cbiAgICAgICAgIyBiZXR3ZWVuIHRoZSBjbGllbnQgYW5kIHNlcnZlci5cbiAgICAgICAga2VlcF9hbGl2ZV9pbnRlcnZhbD1cIjMwc1wiXG5cbiAgICAgICAgIyBDQSBjZXJ0aWZpY2F0ZSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgI1xuICAgICAgICAjIFVzZSB0aGlzIHdoZW4gc2V0dGluZyB1cCBhIHNlY3VyZSBjb25uZWN0aW9uICh3aGVuIHNlcnZlciB1c2VzIHNzbDovLy4uLilcbiAgICAgICAgIyBidXQgdGhlIGNlcnRpZmljYXRlIHVzZWQgYnkgdGhlIHNlcnZlciBpcyBub3QgdHJ1c3RlZCBieSBhbnkgQ0EgY2VydGlmaWNhdGVcbiAgICAgICAgIyBvbiB0aGUgc2VydmVyIChlLmcuIHdoZW4gc2VsZiBnZW5lcmF0ZWQpLlxuICAgICAgICBjYV9jZXJ0PVwiXCJcblxuICAgICAgICAjIFRMUyBjZXJ0aWZpY2F0ZSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgdGxzX2NlcnQ9XCJcIlxuXG4gICAgICAgICMgVExTIGtleSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgdGxzX2tleT1cIlwiXG5cblxuICAgICMgR2F0ZXdheSBjaGFubmVsIGNvbmZpZ3VyYXRpb24uXG4gICAgI1xuICAgICMgTm90ZTogdGhpcyBjb25maWd1cmF0aW9uIGlzIG9ubHkgdXNlZCBpbiBjYXNlIHRoZSBnYXRld2F5IGlzIHVzaW5nIHRoZVxuICAgICMgQ2hpcnBTdGFjayBDb25jZW50cmF0b3JkIGRhZW1vbi4gSW4gYW55IG90aGVyIGNhc2UsIHRoaXMgY29uZmlndXJhdGlvbiBcbiAgICAjIGlzIGlnbm9yZWQuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTg2NTA2MjUwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9ODY1NDAyNTAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT04NjU5ODUwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG5cbiAgIyBSZWdpb24gc3BlY2lmaWMgbmV0d29yayBjb25maWd1cmF0aW9uLlxuICBbcmVnaW9ucy5uZXR3b3JrXVxuICAgIFxuICAgICMgSW5zdGFsbGF0aW9uIG1hcmdpbiAoZEIpIHVzZWQgYnkgdGhlIEFEUiBlbmdpbmUuXG4gICAgI1xuICAgICMgQSBoaWdoZXIgbnVtYmVyIG1lYW5zIHRoYXQgdGhlIG5ldHdvcmstc2VydmVyIHdpbGwga2VlcCBtb3JlIG1hcmdpbixcbiAgICAjIHJlc3VsdGluZyBpbiBhIGxvd2VyIGRhdGEtcmF0ZSBidXQgZGVjcmVhc2luZyB0aGUgY2hhbmNlIHRoYXQgdGhlXG4gICAgIyBkZXZpY2UgZ2V0cyBkaXNjb25uZWN0ZWQgYmVjYXVzZSBpdCBpcyB1bmFibGUgdG8gcmVhY2ggb25lIG9mIHRoZVxuICAgICMgc3Vycm91bmRlZCBnYXRld2F5cy5cbiAgICBpbnN0YWxsYXRpb25fbWFyZ2luPTEwXG5cbiAgICAjIFJYIHdpbmRvdyAoQ2xhc3MtQSkuXG4gICAgI1xuICAgICMgU2V0IHRoaXMgdG86XG4gICAgIyAwOiBSWDEgLyBSWDJcbiAgICAjIDE6IFJYMSBvbmx5XG4gICAgIyAyOiBSWDIgb25seVxuICAgIHJ4X3dpbmRvdz0wXG5cbiAgICAjIFJYMSBkZWxheSAoMSAtIDE1IHNlY29uZHMpLlxuICAgIHJ4MV9kZWxheT0xXG5cbiAgICAjIFJYMSBkYXRhLXJhdGUgb2Zmc2V0XG4gICAgcngxX2RyX29mZnNldD0wXG5cbiAgICAjIFJYMiBkYXRhLXJhdGVcbiAgICByeDJfZHI9MlxuXG4gICAgIyBSWDIgZnJlcXVlbmN5IChIeilcbiAgICByeDJfZnJlcXVlbmN5PTg2NjU1MDAwMFxuXG4gICAgIyBQcmVmZXIgUlgyIG9uIFJYMSBkYXRhLXJhdGUgbGVzcyB0aGFuLlxuICAgICNcbiAgICAjIFByZWZlciBSWDIgb3ZlciBSWDEgYmFzZWQgb24gdGhlIFJYMSBkYXRhLXJhdGUuIFdoZW4gdGhlIFJYMSBkYXRhLXJhdGVcbiAgICAjIGlzIHNtYWxsZXIgdGhhbiB0aGUgY29uZmlndXJlZCB2YWx1ZSwgdGhlbiB0aGUgTmV0d29yayBTZXJ2ZXIgd2lsbFxuICAgICMgZmlyc3QgdHJ5IHRvIHNjaGVkdWxlIHRoZSBkb3dubGluayBmb3IgUlgyLCBmYWlsaW5nIHRoYXQgKGUuZy4gdGhlIGdhdGV3YXlcbiAgICAjIGhhcyBhbHJlYWR5IGEgcGF5bG9hZCBzY2hlZHVsZWQgYXQgdGhlIFJYMiB0aW1pbmcpIGl0IHdpbGwgdHJ5IFJYMS5cbiAgICByeDJfcHJlZmVyX29uX3J4MV9kcl9sdD0wXG5cbiAgICAjIFByZWZlciBSWDIgb24gbGluayBidWRnZXQuXG4gICAgI1xuICAgICMgV2hlbiB0aGUgbGluay1idWRnZXQgaXMgYmV0dGVyIGZvciBSWDIgdGhhbiBmb3IgUlgxLCB0aGUgTmV0d29yayBTZXJ2ZXIgd2lsbCBmaXJzdFxuICAgICMgdHJ5IHRvIHNjaGVkdWxlIHRoZSBkb3dubGluayBpbiBSWDIsIGZhaWxpbmcgdGhhdCBpdCB3aWxsIHRyeSBSWDEuXG4gICAgcngyX3ByZWZlcl9vbl9saW5rX2J1ZGdldD1mYWxzZVxuXG4gICAgIyBEb3dubGluayBUWCBQb3dlciAoZEJtKVxuICAgICNcbiAgICAjIFdoZW4gc2V0IHRvIC0xLCB0aGUgZG93bmxpbmsgVFggUG93ZXIgZnJvbSB0aGUgY29uZmlndXJlZCBiYW5kIHdpbGxcbiAgICAjIGJlIHVzZWQuXG4gICAgI1xuICAgICMgUGxlYXNlIGNvbnN1bHQgdGhlIExvUmFXQU4gUmVnaW9uYWwgUGFyYW1ldGVycyBhbmQgbG9jYWwgcmVndWxhdGlvbnNcbiAgICAjIGZvciB2YWxpZCBhbmQgbGVnYWwgb3B0aW9ucy4gTm90ZSB0aGF0IHRoZSBjb25maWd1cmVkIFRYIFBvd2VyIG11c3QgYmVcbiAgICAjIHN1cHBvcnRlZCBieSB5b3VyIGdhdGV3YXkocykuXG4gICAgZG93bmxpbmtfdHhfcG93ZXI9LTFcblxuICAgICMgQURSIGlzIGRpc2FibGVkLlxuICAgIGFkcl9kaXNhYmxlZD1mYWxzZVxuXG4gICAgIyBNaW5pbXVtIGRhdGEtcmF0ZS5cbiAgICBtaW5fZHI9MFxuXG4gICAgIyBNYXhpbXVtIGRhdGEtcmF0ZS5cbiAgICBtYXhfZHI9NVxuXG5cbiAgICAjIFJlam9pbi1yZXF1ZXN0IGNvbmZpZ3VyYXRpb24gKExvUmFXQU4gMS4xKVxuICAgIFtyZWdpb25zLm5ldHdvcmsucmVqb2luX3JlcXVlc3RdXG5cbiAgICAgICMgUmVxdWVzdCBkZXZpY2VzIHRvIHBlcmlvZGljYWxseSBzZW5kIHJlam9pbi1yZXF1ZXN0cy5cbiAgICAgIGVuYWJsZWQ9ZmFsc2VcblxuICAgICAgIyBUaGUgZGV2aWNlIG11c3Qgc2VuZCBhIHJlam9pbi1yZXF1ZXN0IHR5cGUgMCBhdCBsZWFzdCBldmVyeSAyXihtYXhfY291bnRfbiArIDQpXG4gICAgICAjIHVwbGluayBtZXNzYWdlcy4gVmFsaWQgdmFsdWVzIGFyZSAwIHRvIDE1LlxuICAgICAgbWF4X2NvdW50X249MFxuXG4gICAgICAjIFRoZSBkZXZpY2UgbXVzdCBzZW5kIGEgcmVqb2luLXJlcXVlc3QgdHlwZSAwIGF0IGxlYXN0IGV2ZXJ5IDJeKG1heF90aW1lX24gKyAxMClcbiAgICAgICMgc2Vjb25kcy4gVmFsaWQgdmFsdWVzIGFyZSAwIHRvIDE1LlxuICAgICAgI1xuICAgICAgIyAwICA9IHJvdWdobHkgMTcgbWludXRlc1xuICAgICAgIyAxNSA9IGFib3V0IDEgeWVhclxuICAgICAgbWF4X3RpbWVfbj0wXG4gICAgXG5cbiAgICAjIENsYXNzLUIgY29uZmlndXJhdGlvbi5cbiAgICBbcmVnaW9ucy5uZXR3b3JrLmNsYXNzX2JdXG5cbiAgICAgICMgUGluZy1zbG90IGRhdGEtcmF0ZS4gXG4gICAgICBwaW5nX3Nsb3RfZHI9NFxuXG4gICAgICAjIFBpbmctc2xvdCBmcmVxdWVuY3kgKEh6KVxuICAgICAgI1xuICAgICAgIyBzZXQgdGhpcyB0byAwIHRvIHVzZSB0aGUgZGVmYXVsdCBmcmVxdWVuY3kgcGxhbiBmb3IgdGhlIGNvbmZpZ3VyZWQgcmVnaW9uXG4gICAgICAjICh3aGljaCBjb3VsZCBiZSBmcmVxdWVuY3kgaG9wcGluZykuXG4gICAgICBwaW5nX3Nsb3RfZnJlcXVlbmN5PTBcblwiXCJcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuc2VydmljZU5hbWUgPSBcImNoaXJwc3RhY2tcIlxuZmlsZVBhdGggPSBcIi9jaGlycHN0YWNrL3JlZ2lvbl9pc20yNDAwLnRvbWxcIlxuY29udGVudCA9IFwiXCJcIlxuIyBUaGlzIGZpbGUgY29udGFpbnMgYW4gZXhhbXBsZSBJU00yNDAwIGNvbmZpZ3VyYXRpb24uXG5bW3JlZ2lvbnNdXVxuXG4gICMgSUQgaXMgYW4gdXNlci1kZWZpbmVkIGlkZW50aWZpZXIgZm9yIHRoaXMgcmVnaW9uLlxuICBpZD1cImlzbTI0MDBcIlxuXG4gICMgRGVzY3JpcHRpb24gaXMgYSBzaG9ydCBkZXNjcmlwdGlvbiBmb3IgdGhpcyByZWdpb24uXG4gIGRlc2NyaXB0aW9uPVwiSVNNMjQwMFwiXG5cbiAgIyBDb21tb24tbmFtZSByZWZlcnMgdG8gdGhlIGNvbW1vbi1uYW1lIG9mIHRoaXMgcmVnaW9uIGFzIGRlZmluZWQgYnlcbiAgIyB0aGUgTG9SYSBBbGxpYW5jZS5cbiAgY29tbW9uX25hbWU9XCJJU00yNDAwXCJcblxuXG4gICMgR2F0ZXdheSBjb25maWd1cmF0aW9uLlxuICBbcmVnaW9ucy5nYXRld2F5XVxuXG4gICAgIyBGb3JjZSBnYXRld2F5cyBhcyBwcml2YXRlLlxuICAgICNcbiAgICAjIElmIGVuYWJsZWQsIGdhdGV3YXlzIGNhbiBvbmx5IGJlIHVzZWQgYnkgZGV2aWNlcyB1bmRlciB0aGUgc2FtZSB0ZW5hbnQuXG4gICAgZm9yY2VfZ3dzX3ByaXZhdGU9ZmFsc2VcblxuXG4gICAgIyBHYXRld2F5IGJhY2tlbmQgY29uZmlndXJhdGlvbi5cbiAgICBbcmVnaW9ucy5nYXRld2F5LmJhY2tlbmRdXG5cbiAgICAgICMgVGhlIGVuYWJsZWQgYmFja2VuZCB0eXBlLlxuICAgICAgZW5hYmxlZD1cIm1xdHRcIlxuXG4gICAgICAjIE1RVFQgY29uZmlndXJhdGlvbi5cbiAgICAgIFtyZWdpb25zLmdhdGV3YXkuYmFja2VuZC5tcXR0XVxuXG4gICAgICAgICMgVG9waWMgcHJlZml4LlxuICAgICAgICAjXG4gICAgICAgICMgVGhlIHRvcGljIHByZWZpeCBjYW4gYmUgdXNlZCB0byBkZWZpbmUgdGhlIHJlZ2lvbiBvZiB0aGUgZ2F0ZXdheS5cbiAgICAgICAgIyBOb3RlLCB0aGVyZSBpcyBubyBuZWVkIHRvIGFkZCBhIHRyYWlsaW5nICcvJyB0byB0aGUgcHJlZml4LiBUaGUgdHJhaWxpbmdcbiAgICAgICAgIyAnLycgaXMgYXV0b21hdGljYWxseSBhZGRlZCB0byB0aGUgcHJlZml4IGlmIGl0IGlzIGNvbmZpZ3VyZWQuXG4gICAgICAgIHRvcGljX3ByZWZpeD1cImlzbTI0MDBcIlxuXG4gICAgICAgICMgTVFUVCBzZXJ2ZXIgKGUuZy4gc2NoZW1lOi8vaG9zdDpwb3J0IHdoZXJlIHNjaGVtZSBpcyB0Y3AsIHNzbCBvciB3cylcbiAgICAgICAgc2VydmVyPVwidGNwOi8vbW9zcXVpdHRvOjE4ODNcIlxuXG4gICAgICAgICMgQ29ubmVjdCB3aXRoIHRoZSBnaXZlbiB1c2VybmFtZSAob3B0aW9uYWwpXG4gICAgICAgIHVzZXJuYW1lPVwiXCJcblxuICAgICAgICAjIENvbm5lY3Qgd2l0aCB0aGUgZ2l2ZW4gcGFzc3dvcmQgKG9wdGlvbmFsKVxuICAgICAgICBwYXNzd29yZD1cIlwiXG5cbiAgICAgICAgIyBRdWFsaXR5IG9mIHNlcnZpY2UgbGV2ZWxcbiAgICAgICAgI1xuICAgICAgICAjIDA6IGF0IG1vc3Qgb25jZVxuICAgICAgICAjIDE6IGF0IGxlYXN0IG9uY2VcbiAgICAgICAgIyAyOiBleGFjdGx5IG9uY2VcbiAgICAgICAgI1xuICAgICAgICAjIE5vdGU6IGFuIGluY3JlYXNlIG9mIHRoaXMgdmFsdWUgd2lsbCBkZWNyZWFzZSB0aGUgcGVyZm9ybWFuY2UuXG4gICAgICAgICMgRm9yIG1vcmUgaW5mb3JtYXRpb246IGh0dHBzOi8vd3d3LmhpdmVtcS5jb20vYmxvZy9tcXR0LWVzc2VudGlhbHMtcGFydC02LW1xdHQtcXVhbGl0eS1vZi1zZXJ2aWNlLWxldmVsc1xuICAgICAgICBxb3M9MFxuXG4gICAgICAgICMgQ2xlYW4gc2Vzc2lvblxuICAgICAgICAjXG4gICAgICAgICMgU2V0IHRoZSBcImNsZWFuIHNlc3Npb25cIiBmbGFnIGluIHRoZSBjb25uZWN0IG1lc3NhZ2Ugd2hlbiB0aGlzIGNsaWVudFxuICAgICAgICAjIGNvbm5lY3RzIHRvIGFuIE1RVFQgYnJva2VyLiBCeSBzZXR0aW5nIHRoaXMgZmxhZyB5b3UgYXJlIGluZGljYXRpbmdcbiAgICAgICAgIyB0aGF0IG5vIG1lc3NhZ2VzIHNhdmVkIGJ5IHRoZSBicm9rZXIgZm9yIHRoaXMgY2xpZW50IHNob3VsZCBiZSBkZWxpdmVyZWQuXG4gICAgICAgIGNsZWFuX3Nlc3Npb249ZmFsc2VcblxuICAgICAgICAjIENsaWVudCBJRFxuICAgICAgICAjXG4gICAgICAgICMgU2V0IHRoZSBjbGllbnQgaWQgdG8gYmUgdXNlZCBieSB0aGlzIGNsaWVudCB3aGVuIGNvbm5lY3RpbmcgdG8gdGhlIE1RVFRcbiAgICAgICAgIyBicm9rZXIuIEEgY2xpZW50IGlkIG11c3QgYmUgbm8gbG9uZ2VyIHRoYW4gMjMgY2hhcmFjdGVycy4gSWYgbGVmdCBibGFuayxcbiAgICAgICAgIyBhIHJhbmRvbSBpZCB3aWxsIGJlIGdlbmVyYXRlZCBieSBDaGlycFN0YWNrLlxuICAgICAgICBjbGllbnRfaWQ9XCJcIlxuXG4gICAgICAgICMgS2VlcCBhbGl2ZSBpbnRlcnZhbC5cbiAgICAgICAgI1xuICAgICAgICAjIFRoaXMgZGVmaW5lcyB0aGUgbWF4aW11bSB0aW1lIHRoYXQgdGhhdCBzaG91bGQgcGFzcyB3aXRob3V0IGNvbW11bmljYXRpb25cbiAgICAgICAgIyBiZXR3ZWVuIHRoZSBjbGllbnQgYW5kIHNlcnZlci5cbiAgICAgICAga2VlcF9hbGl2ZV9pbnRlcnZhbD1cIjMwc1wiXG5cbiAgICAgICAgIyBDQSBjZXJ0aWZpY2F0ZSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgI1xuICAgICAgICAjIFVzZSB0aGlzIHdoZW4gc2V0dGluZyB1cCBhIHNlY3VyZSBjb25uZWN0aW9uICh3aGVuIHNlcnZlciB1c2VzIHNzbDovLy4uLilcbiAgICAgICAgIyBidXQgdGhlIGNlcnRpZmljYXRlIHVzZWQgYnkgdGhlIHNlcnZlciBpcyBub3QgdHJ1c3RlZCBieSBhbnkgQ0EgY2VydGlmaWNhdGVcbiAgICAgICAgIyBvbiB0aGUgc2VydmVyIChlLmcuIHdoZW4gc2VsZiBnZW5lcmF0ZWQpLlxuICAgICAgICBjYV9jZXJ0PVwiXCJcblxuICAgICAgICAjIFRMUyBjZXJ0aWZpY2F0ZSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgdGxzX2NlcnQ9XCJcIlxuXG4gICAgICAgICMgVExTIGtleSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgdGxzX2tleT1cIlwiXG5cblxuICAgICMgR2F0ZXdheSBjaGFubmVsIGNvbmZpZ3VyYXRpb24uXG4gICAgI1xuICAgICMgTm90ZTogdGhpcyBjb25maWd1cmF0aW9uIGlzIG9ubHkgdXNlZCBpbiBjYXNlIHRoZSBnYXRld2F5IGlzIHVzaW5nIHRoZVxuICAgICMgQ2hpcnBTdGFjayBDb25jZW50cmF0b3JkIGRhZW1vbi4gSW4gYW55IG90aGVyIGNhc2UsIHRoaXMgY29uZmlndXJhdGlvbiBcbiAgICAjIGlzIGlnbm9yZWQuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTI0MDMwMDAwMDBcbiAgICAgIGJhbmR3aWR0aD04MTIwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVsxMl1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT0yNDc5MDAwMDAwXG4gICAgICBiYW5kd2lkdGg9ODEyMDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9MjQyNTAwMDAwMFxuICAgICAgYmFuZHdpZHRoPTgxMjAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzEyXVxuXG5cbiAgIyBSZWdpb24gc3BlY2lmaWMgbmV0d29yayBjb25maWd1cmF0aW9uLlxuICBbcmVnaW9ucy5uZXR3b3JrXVxuICAgIFxuICAgICMgSW5zdGFsbGF0aW9uIG1hcmdpbiAoZEIpIHVzZWQgYnkgdGhlIEFEUiBlbmdpbmUuXG4gICAgI1xuICAgICMgQSBoaWdoZXIgbnVtYmVyIG1lYW5zIHRoYXQgdGhlIG5ldHdvcmstc2VydmVyIHdpbGwga2VlcCBtb3JlIG1hcmdpbixcbiAgICAjIHJlc3VsdGluZyBpbiBhIGxvd2VyIGRhdGEtcmF0ZSBidXQgZGVjcmVhc2luZyB0aGUgY2hhbmNlIHRoYXQgdGhlXG4gICAgIyBkZXZpY2UgZ2V0cyBkaXNjb25uZWN0ZWQgYmVjYXVzZSBpdCBpcyB1bmFibGUgdG8gcmVhY2ggb25lIG9mIHRoZVxuICAgICMgc3Vycm91bmRlZCBnYXRld2F5cy5cbiAgICBpbnN0YWxsYXRpb25fbWFyZ2luPTEwXG5cbiAgICAjIFJYIHdpbmRvdyAoQ2xhc3MtQSkuXG4gICAgI1xuICAgICMgU2V0IHRoaXMgdG86XG4gICAgIyAwOiBSWDEgLyBSWDJcbiAgICAjIDE6IFJYMSBvbmx5XG4gICAgIyAyOiBSWDIgb25seVxuICAgIHJ4X3dpbmRvdz0wXG5cbiAgICAjIFJYMSBkZWxheSAoMSAtIDE1IHNlY29uZHMpLlxuICAgIHJ4MV9kZWxheT0xXG5cbiAgICAjIFJYMSBkYXRhLXJhdGUgb2Zmc2V0XG4gICAgcngxX2RyX29mZnNldD0wXG5cbiAgICAjIFJYMiBkYXRhLXJhdGVcbiAgICByeDJfZHI9MFxuXG4gICAgIyBSWDIgZnJlcXVlbmN5IChIeilcbiAgICByeDJfZnJlcXVlbmN5PTI0MjMwMDAwMDBcblxuICAgICMgUHJlZmVyIFJYMiBvbiBSWDEgZGF0YS1yYXRlIGxlc3MgdGhhbi5cbiAgICAjXG4gICAgIyBQcmVmZXIgUlgyIG92ZXIgUlgxIGJhc2VkIG9uIHRoZSBSWDEgZGF0YS1yYXRlLiBXaGVuIHRoZSBSWDEgZGF0YS1yYXRlXG4gICAgIyBpcyBzbWFsbGVyIHRoYW4gdGhlIGNvbmZpZ3VyZWQgdmFsdWUsIHRoZW4gdGhlIE5ldHdvcmsgU2VydmVyIHdpbGxcbiAgICAjIGZpcnN0IHRyeSB0byBzY2hlZHVsZSB0aGUgZG93bmxpbmsgZm9yIFJYMiwgZmFpbGluZyB0aGF0IChlLmcuIHRoZSBnYXRld2F5XG4gICAgIyBoYXMgYWxyZWFkeSBhIHBheWxvYWQgc2NoZWR1bGVkIGF0IHRoZSBSWDIgdGltaW5nKSBpdCB3aWxsIHRyeSBSWDEuXG4gICAgcngyX3ByZWZlcl9vbl9yeDFfZHJfbHQ9MFxuXG4gICAgIyBQcmVmZXIgUlgyIG9uIGxpbmsgYnVkZ2V0LlxuICAgICNcbiAgICAjIFdoZW4gdGhlIGxpbmstYnVkZ2V0IGlzIGJldHRlciBmb3IgUlgyIHRoYW4gZm9yIFJYMSwgdGhlIE5ldHdvcmsgU2VydmVyIHdpbGwgZmlyc3RcbiAgICAjIHRyeSB0byBzY2hlZHVsZSB0aGUgZG93bmxpbmsgaW4gUlgyLCBmYWlsaW5nIHRoYXQgaXQgd2lsbCB0cnkgUlgxLlxuICAgIHJ4Ml9wcmVmZXJfb25fbGlua19idWRnZXQ9ZmFsc2VcblxuICAgICMgRG93bmxpbmsgVFggUG93ZXIgKGRCbSlcbiAgICAjXG4gICAgIyBXaGVuIHNldCB0byAtMSwgdGhlIGRvd25saW5rIFRYIFBvd2VyIGZyb20gdGhlIGNvbmZpZ3VyZWQgYmFuZCB3aWxsXG4gICAgIyBiZSB1c2VkLlxuICAgICNcbiAgICAjIFBsZWFzZSBjb25zdWx0IHRoZSBMb1JhV0FOIFJlZ2lvbmFsIFBhcmFtZXRlcnMgYW5kIGxvY2FsIHJlZ3VsYXRpb25zXG4gICAgIyBmb3IgdmFsaWQgYW5kIGxlZ2FsIG9wdGlvbnMuIE5vdGUgdGhhdCB0aGUgY29uZmlndXJlZCBUWCBQb3dlciBtdXN0IGJlXG4gICAgIyBzdXBwb3J0ZWQgYnkgeW91ciBnYXRld2F5KHMpLlxuICAgIGRvd25saW5rX3R4X3Bvd2VyPS0xXG5cbiAgICAjIEFEUiBpcyBkaXNhYmxlZC5cbiAgICBhZHJfZGlzYWJsZWQ9ZmFsc2VcblxuICAgICMgTWluaW11bSBkYXRhLXJhdGUuXG4gICAgbWluX2RyPTBcblxuICAgICMgTWF4aW11bSBkYXRhLXJhdGUuXG4gICAgbWF4X2RyPTdcblxuXG4gICAgIyBSZWpvaW4tcmVxdWVzdCBjb25maWd1cmF0aW9uIChMb1JhV0FOIDEuMSlcbiAgICBbcmVnaW9ucy5uZXR3b3JrLnJlam9pbl9yZXF1ZXN0XVxuXG4gICAgICAjIFJlcXVlc3QgZGV2aWNlcyB0byBwZXJpb2RpY2FsbHkgc2VuZCByZWpvaW4tcmVxdWVzdHMuXG4gICAgICBlbmFibGVkPWZhbHNlXG5cbiAgICAgICMgVGhlIGRldmljZSBtdXN0IHNlbmQgYSByZWpvaW4tcmVxdWVzdCB0eXBlIDAgYXQgbGVhc3QgZXZlcnkgMl4obWF4X2NvdW50X24gKyA0KVxuICAgICAgIyB1cGxpbmsgbWVzc2FnZXMuIFZhbGlkIHZhbHVlcyBhcmUgMCB0byAxNS5cbiAgICAgIG1heF9jb3VudF9uPTBcblxuICAgICAgIyBUaGUgZGV2aWNlIG11c3Qgc2VuZCBhIHJlam9pbi1yZXF1ZXN0IHR5cGUgMCBhdCBsZWFzdCBldmVyeSAyXihtYXhfdGltZV9uICsgMTApXG4gICAgICAjIHNlY29uZHMuIFZhbGlkIHZhbHVlcyBhcmUgMCB0byAxNS5cbiAgICAgICNcbiAgICAgICMgMCAgPSByb3VnaGx5IDE3IG1pbnV0ZXNcbiAgICAgICMgMTUgPSBhYm91dCAxIHllYXJcbiAgICAgIG1heF90aW1lX249MFxuICAgIFxuXG4gICAgIyBDbGFzcy1CIGNvbmZpZ3VyYXRpb24uXG4gICAgW3JlZ2lvbnMubmV0d29yay5jbGFzc19iXVxuXG4gICAgICAjIFBpbmctc2xvdCBkYXRhLXJhdGUuIFxuICAgICAgcGluZ19zbG90X2RyPTBcblxuICAgICAgIyBQaW5nLXNsb3QgZnJlcXVlbmN5IChIeilcbiAgICAgICNcbiAgICAgICMgc2V0IHRoaXMgdG8gMCB0byB1c2UgdGhlIGRlZmF1bHQgZnJlcXVlbmN5IHBsYW4gZm9yIHRoZSBjb25maWd1cmVkIHJlZ2lvblxuICAgICAgIyAod2hpY2ggY291bGQgYmUgZnJlcXVlbmN5IGhvcHBpbmcpLlxuICAgICAgcGluZ19zbG90X2ZyZXF1ZW5jeT0wXG5cIlwiXCJcblxuW1tjb25maWcubW91bnRzXV1cbnNlcnZpY2VOYW1lID0gXCJjaGlycHN0YWNrXCJcbmZpbGVQYXRoID0gXCIvY2hpcnBzdGFjay9yZWdpb25fa3I5MjAudG9tbFwiXG5jb250ZW50ID0gXCJcIlwiXG4jIFRoaXMgZmlsZSBjb250YWlucyBhbiBleGFtcGxlIEtSOTIwIGNvbmZpZ3VyYXRpb24uXG5bW3JlZ2lvbnNdXVxuXG4gICMgSUQgaXMgYW4gdXNlci1kZWZpbmVkIGlkZW50aWZpZXIgZm9yIHRoaXMgcmVnaW9uLlxuICBpZD1cImtyOTIwXCJcblxuICAjIERlc2NyaXB0aW9uIGlzIGEgc2hvcnQgZGVzY3JpcHRpb24gZm9yIHRoaXMgcmVnaW9uLlxuICBkZXNjcmlwdGlvbj1cIktSOTIwXCJcblxuICAjIENvbW1vbi1uYW1lIHJlZmVycyB0byB0aGUgY29tbW9uLW5hbWUgb2YgdGhpcyByZWdpb24gYXMgZGVmaW5lZCBieVxuICAjIHRoZSBMb1JhIEFsbGlhbmNlLlxuICBjb21tb25fbmFtZT1cIktSOTIwXCJcblxuXG4gICMgR2F0ZXdheSBjb25maWd1cmF0aW9uLlxuICBbcmVnaW9ucy5nYXRld2F5XVxuXG4gICAgIyBGb3JjZSBnYXRld2F5cyBhcyBwcml2YXRlLlxuICAgICNcbiAgICAjIElmIGVuYWJsZWQsIGdhdGV3YXlzIGNhbiBvbmx5IGJlIHVzZWQgYnkgZGV2aWNlcyB1bmRlciB0aGUgc2FtZSB0ZW5hbnQuXG4gICAgZm9yY2VfZ3dzX3ByaXZhdGU9ZmFsc2VcblxuXG4gICAgIyBHYXRld2F5IGJhY2tlbmQgY29uZmlndXJhdGlvbi5cbiAgICBbcmVnaW9ucy5nYXRld2F5LmJhY2tlbmRdXG5cbiAgICAgICMgVGhlIGVuYWJsZWQgYmFja2VuZCB0eXBlLlxuICAgICAgZW5hYmxlZD1cIm1xdHRcIlxuXG4gICAgICAjIE1RVFQgY29uZmlndXJhdGlvbi5cbiAgICAgIFtyZWdpb25zLmdhdGV3YXkuYmFja2VuZC5tcXR0XVxuXG4gICAgICAgICMgVG9waWMgcHJlZml4LlxuICAgICAgICAjXG4gICAgICAgICMgVGhlIHRvcGljIHByZWZpeCBjYW4gYmUgdXNlZCB0byBkZWZpbmUgdGhlIHJlZ2lvbiBvZiB0aGUgZ2F0ZXdheS5cbiAgICAgICAgIyBOb3RlLCB0aGVyZSBpcyBubyBuZWVkIHRvIGFkZCBhIHRyYWlsaW5nICcvJyB0byB0aGUgcHJlZml4LiBUaGUgdHJhaWxpbmdcbiAgICAgICAgIyAnLycgaXMgYXV0b21hdGljYWxseSBhZGRlZCB0byB0aGUgcHJlZml4IGlmIGl0IGlzIGNvbmZpZ3VyZWQuXG4gICAgICAgIHRvcGljX3ByZWZpeD1cImtyOTIwXCJcblxuICAgICAgICAjIE1RVFQgc2VydmVyIChlLmcuIHNjaGVtZTovL2hvc3Q6cG9ydCB3aGVyZSBzY2hlbWUgaXMgdGNwLCBzc2wgb3Igd3MpXG4gICAgICAgIHNlcnZlcj1cInRjcDovL21vc3F1aXR0bzoxODgzXCJcblxuICAgICAgICAjIENvbm5lY3Qgd2l0aCB0aGUgZ2l2ZW4gdXNlcm5hbWUgKG9wdGlvbmFsKVxuICAgICAgICB1c2VybmFtZT1cIlwiXG5cbiAgICAgICAgIyBDb25uZWN0IHdpdGggdGhlIGdpdmVuIHBhc3N3b3JkIChvcHRpb25hbClcbiAgICAgICAgcGFzc3dvcmQ9XCJcIlxuXG4gICAgICAgICMgUXVhbGl0eSBvZiBzZXJ2aWNlIGxldmVsXG4gICAgICAgICNcbiAgICAgICAgIyAwOiBhdCBtb3N0IG9uY2VcbiAgICAgICAgIyAxOiBhdCBsZWFzdCBvbmNlXG4gICAgICAgICMgMjogZXhhY3RseSBvbmNlXG4gICAgICAgICNcbiAgICAgICAgIyBOb3RlOiBhbiBpbmNyZWFzZSBvZiB0aGlzIHZhbHVlIHdpbGwgZGVjcmVhc2UgdGhlIHBlcmZvcm1hbmNlLlxuICAgICAgICAjIEZvciBtb3JlIGluZm9ybWF0aW9uOiBodHRwczovL3d3dy5oaXZlbXEuY29tL2Jsb2cvbXF0dC1lc3NlbnRpYWxzLXBhcnQtNi1tcXR0LXF1YWxpdHktb2Ytc2VydmljZS1sZXZlbHNcbiAgICAgICAgcW9zPTBcblxuICAgICAgICAjIENsZWFuIHNlc3Npb25cbiAgICAgICAgI1xuICAgICAgICAjIFNldCB0aGUgXCJjbGVhbiBzZXNzaW9uXCIgZmxhZyBpbiB0aGUgY29ubmVjdCBtZXNzYWdlIHdoZW4gdGhpcyBjbGllbnRcbiAgICAgICAgIyBjb25uZWN0cyB0byBhbiBNUVRUIGJyb2tlci4gQnkgc2V0dGluZyB0aGlzIGZsYWcgeW91IGFyZSBpbmRpY2F0aW5nXG4gICAgICAgICMgdGhhdCBubyBtZXNzYWdlcyBzYXZlZCBieSB0aGUgYnJva2VyIGZvciB0aGlzIGNsaWVudCBzaG91bGQgYmUgZGVsaXZlcmVkLlxuICAgICAgICBjbGVhbl9zZXNzaW9uPWZhbHNlXG5cbiAgICAgICAgIyBDbGllbnQgSURcbiAgICAgICAgI1xuICAgICAgICAjIFNldCB0aGUgY2xpZW50IGlkIHRvIGJlIHVzZWQgYnkgdGhpcyBjbGllbnQgd2hlbiBjb25uZWN0aW5nIHRvIHRoZSBNUVRUXG4gICAgICAgICMgYnJva2VyLiBBIGNsaWVudCBpZCBtdXN0IGJlIG5vIGxvbmdlciB0aGFuIDIzIGNoYXJhY3RlcnMuIElmIGxlZnQgYmxhbmssXG4gICAgICAgICMgYSByYW5kb20gaWQgd2lsbCBiZSBnZW5lcmF0ZWQgYnkgQ2hpcnBTdGFjay5cbiAgICAgICAgY2xpZW50X2lkPVwiXCJcblxuICAgICAgICAjIEtlZXAgYWxpdmUgaW50ZXJ2YWwuXG4gICAgICAgICNcbiAgICAgICAgIyBUaGlzIGRlZmluZXMgdGhlIG1heGltdW0gdGltZSB0aGF0IHRoYXQgc2hvdWxkIHBhc3Mgd2l0aG91dCBjb21tdW5pY2F0aW9uXG4gICAgICAgICMgYmV0d2VlbiB0aGUgY2xpZW50IGFuZCBzZXJ2ZXIuXG4gICAgICAgIGtlZXBfYWxpdmVfaW50ZXJ2YWw9XCIzMHNcIlxuXG4gICAgICAgICMgQ0EgY2VydGlmaWNhdGUgZmlsZSAob3B0aW9uYWwpXG4gICAgICAgICNcbiAgICAgICAgIyBVc2UgdGhpcyB3aGVuIHNldHRpbmcgdXAgYSBzZWN1cmUgY29ubmVjdGlvbiAod2hlbiBzZXJ2ZXIgdXNlcyBzc2w6Ly8uLi4pXG4gICAgICAgICMgYnV0IHRoZSBjZXJ0aWZpY2F0ZSB1c2VkIGJ5IHRoZSBzZXJ2ZXIgaXMgbm90IHRydXN0ZWQgYnkgYW55IENBIGNlcnRpZmljYXRlXG4gICAgICAgICMgb24gdGhlIHNlcnZlciAoZS5nLiB3aGVuIHNlbGYgZ2VuZXJhdGVkKS5cbiAgICAgICAgY2FfY2VydD1cIlwiXG5cbiAgICAgICAgIyBUTFMgY2VydGlmaWNhdGUgZmlsZSAob3B0aW9uYWwpXG4gICAgICAgIHRsc19jZXJ0PVwiXCJcblxuICAgICAgICAjIFRMUyBrZXkgZmlsZSAob3B0aW9uYWwpXG4gICAgICAgIHRsc19rZXk9XCJcIlxuXG5cbiAgICAjIEdhdGV3YXkgY2hhbm5lbCBjb25maWd1cmF0aW9uLlxuICAgICNcbiAgICAjIE5vdGU6IHRoaXMgY29uZmlndXJhdGlvbiBpcyBvbmx5IHVzZWQgaW4gY2FzZSB0aGUgZ2F0ZXdheSBpcyB1c2luZyB0aGVcbiAgICAjIENoaXJwU3RhY2sgQ29uY2VudHJhdG9yZCBkYWVtb24uIEluIGFueSBvdGhlciBjYXNlLCB0aGlzIGNvbmZpZ3VyYXRpb24gXG4gICAgIyBpcyBpZ25vcmVkLlxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MjIxMDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkyMjMwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTIyNTAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTAsIDExLCAxMl1cblxuXG4gICMgUmVnaW9uIHNwZWNpZmljIG5ldHdvcmsgY29uZmlndXJhdGlvbi5cbiAgW3JlZ2lvbnMubmV0d29ya11cbiAgICBcbiAgICAjIEluc3RhbGxhdGlvbiBtYXJnaW4gKGRCKSB1c2VkIGJ5IHRoZSBBRFIgZW5naW5lLlxuICAgICNcbiAgICAjIEEgaGlnaGVyIG51bWJlciBtZWFucyB0aGF0IHRoZSBuZXR3b3JrLXNlcnZlciB3aWxsIGtlZXAgbW9yZSBtYXJnaW4sXG4gICAgIyByZXN1bHRpbmcgaW4gYSBsb3dlciBkYXRhLXJhdGUgYnV0IGRlY3JlYXNpbmcgdGhlIGNoYW5jZSB0aGF0IHRoZVxuICAgICMgZGV2aWNlIGdldHMgZGlzY29ubmVjdGVkIGJlY2F1c2UgaXQgaXMgdW5hYmxlIHRvIHJlYWNoIG9uZSBvZiB0aGVcbiAgICAjIHN1cnJvdW5kZWQgZ2F0ZXdheXMuXG4gICAgaW5zdGFsbGF0aW9uX21hcmdpbj0xMFxuXG4gICAgIyBSWCB3aW5kb3cgKENsYXNzLUEpLlxuICAgICNcbiAgICAjIFNldCB0aGlzIHRvOlxuICAgICMgMDogUlgxIC8gUlgyXG4gICAgIyAxOiBSWDEgb25seVxuICAgICMgMjogUlgyIG9ubHlcbiAgICByeF93aW5kb3c9MFxuXG4gICAgIyBSWDEgZGVsYXkgKDEgLSAxNSBzZWNvbmRzKS5cbiAgICByeDFfZGVsYXk9MVxuXG4gICAgIyBSWDEgZGF0YS1yYXRlIG9mZnNldFxuICAgIHJ4MV9kcl9vZmZzZXQ9MFxuXG4gICAgIyBSWDIgZGF0YS1yYXRlXG4gICAgcngyX2RyPTBcblxuICAgICMgUlgyIGZyZXF1ZW5jeSAoSHopXG4gICAgcngyX2ZyZXF1ZW5jeT05MjE5MDAwMDBcblxuICAgICMgUHJlZmVyIFJYMiBvbiBSWDEgZGF0YS1yYXRlIGxlc3MgdGhhbi5cbiAgICAjXG4gICAgIyBQcmVmZXIgUlgyIG92ZXIgUlgxIGJhc2VkIG9uIHRoZSBSWDEgZGF0YS1yYXRlLiBXaGVuIHRoZSBSWDEgZGF0YS1yYXRlXG4gICAgIyBpcyBzbWFsbGVyIHRoYW4gdGhlIGNvbmZpZ3VyZWQgdmFsdWUsIHRoZW4gdGhlIE5ldHdvcmsgU2VydmVyIHdpbGxcbiAgICAjIGZpcnN0IHRyeSB0byBzY2hlZHVsZSB0aGUgZG93bmxpbmsgZm9yIFJYMiwgZmFpbGluZyB0aGF0IChlLmcuIHRoZSBnYXRld2F5XG4gICAgIyBoYXMgYWxyZWFkeSBhIHBheWxvYWQgc2NoZWR1bGVkIGF0IHRoZSBSWDIgdGltaW5nKSBpdCB3aWxsIHRyeSBSWDEuXG4gICAgcngyX3ByZWZlcl9vbl9yeDFfZHJfbHQ9MFxuXG4gICAgIyBQcmVmZXIgUlgyIG9uIGxpbmsgYnVkZ2V0LlxuICAgICNcbiAgICAjIFdoZW4gdGhlIGxpbmstYnVkZ2V0IGlzIGJldHRlciBmb3IgUlgyIHRoYW4gZm9yIFJYMSwgdGhlIE5ldHdvcmsgU2VydmVyIHdpbGwgZmlyc3RcbiAgICAjIHRyeSB0byBzY2hlZHVsZSB0aGUgZG93bmxpbmsgaW4gUlgyLCBmYWlsaW5nIHRoYXQgaXQgd2lsbCB0cnkgUlgxLlxuICAgIHJ4Ml9wcmVmZXJfb25fbGlua19idWRnZXQ9ZmFsc2VcblxuICAgICMgRG93bmxpbmsgVFggUG93ZXIgKGRCbSlcbiAgICAjXG4gICAgIyBXaGVuIHNldCB0byAtMSwgdGhlIGRvd25saW5rIFRYIFBvd2VyIGZyb20gdGhlIGNvbmZpZ3VyZWQgYmFuZCB3aWxsXG4gICAgIyBiZSB1c2VkLlxuICAgICNcbiAgICAjIFBsZWFzZSBjb25zdWx0IHRoZSBMb1JhV0FOIFJlZ2lvbmFsIFBhcmFtZXRlcnMgYW5kIGxvY2FsIHJlZ3VsYXRpb25zXG4gICAgIyBmb3IgdmFsaWQgYW5kIGxlZ2FsIG9wdGlvbnMuIE5vdGUgdGhhdCB0aGUgY29uZmlndXJlZCBUWCBQb3dlciBtdXN0IGJlXG4gICAgIyBzdXBwb3J0ZWQgYnkgeW91ciBnYXRld2F5KHMpLlxuICAgIGRvd25saW5rX3R4X3Bvd2VyPS0xXG5cbiAgICAjIEFEUiBpcyBkaXNhYmxlZC5cbiAgICBhZHJfZGlzYWJsZWQ9ZmFsc2VcblxuICAgICMgTWluaW11bSBkYXRhLXJhdGUuXG4gICAgbWluX2RyPTBcblxuICAgICMgTWF4aW11bSBkYXRhLXJhdGUuXG4gICAgbWF4X2RyPTVcblxuXG4gICAgIyBSZWpvaW4tcmVxdWVzdCBjb25maWd1cmF0aW9uIChMb1JhV0FOIDEuMSlcbiAgICBbcmVnaW9ucy5uZXR3b3JrLnJlam9pbl9yZXF1ZXN0XVxuXG4gICAgICAjIFJlcXVlc3QgZGV2aWNlcyB0byBwZXJpb2RpY2FsbHkgc2VuZCByZWpvaW4tcmVxdWVzdHMuXG4gICAgICBlbmFibGVkPWZhbHNlXG5cbiAgICAgICMgVGhlIGRldmljZSBtdXN0IHNlbmQgYSByZWpvaW4tcmVxdWVzdCB0eXBlIDAgYXQgbGVhc3QgZXZlcnkgMl4obWF4X2NvdW50X24gKyA0KVxuICAgICAgIyB1cGxpbmsgbWVzc2FnZXMuIFZhbGlkIHZhbHVlcyBhcmUgMCB0byAxNS5cbiAgICAgIG1heF9jb3VudF9uPTBcblxuICAgICAgIyBUaGUgZGV2aWNlIG11c3Qgc2VuZCBhIHJlam9pbi1yZXF1ZXN0IHR5cGUgMCBhdCBsZWFzdCBldmVyeSAyXihtYXhfdGltZV9uICsgMTApXG4gICAgICAjIHNlY29uZHMuIFZhbGlkIHZhbHVlcyBhcmUgMCB0byAxNS5cbiAgICAgICNcbiAgICAgICMgMCAgPSByb3VnaGx5IDE3IG1pbnV0ZXNcbiAgICAgICMgMTUgPSBhYm91dCAxIHllYXJcbiAgICAgIG1heF90aW1lX249MFxuICAgIFxuXG4gICAgIyBDbGFzcy1CIGNvbmZpZ3VyYXRpb24uXG4gICAgW3JlZ2lvbnMubmV0d29yay5jbGFzc19iXVxuXG4gICAgICAjIFBpbmctc2xvdCBkYXRhLXJhdGUuIFxuICAgICAgcGluZ19zbG90X2RyPTNcblxuICAgICAgIyBQaW5nLXNsb3QgZnJlcXVlbmN5IChIeilcbiAgICAgICNcbiAgICAgICMgc2V0IHRoaXMgdG8gMCB0byB1c2UgdGhlIGRlZmF1bHQgZnJlcXVlbmN5IHBsYW4gZm9yIHRoZSBjb25maWd1cmVkIHJlZ2lvblxuICAgICAgIyAod2hpY2ggY291bGQgYmUgZnJlcXVlbmN5IGhvcHBpbmcpLlxuICAgICAgcGluZ19zbG90X2ZyZXF1ZW5jeT0wXG5cIlwiXCJcblxuW1tjb25maWcubW91bnRzXV1cbnNlcnZpY2VOYW1lID0gXCJjaGlycHN0YWNrXCJcbmZpbGVQYXRoID0gXCIvY2hpcnBzdGFjay9yZWdpb25fcnU4NjQudG9tbFwiXG5jb250ZW50ID0gXCJcIlwiXG4jIFRoaXMgZmlsZSBjb250YWlucyBhbiBleGFtcGxlIFJVODY0IGNvbmZpZ3VyYXRpb24uXG5bW3JlZ2lvbnNdXVxuXG4gICMgSUQgaXMgYW4gdXNlci1kZWZpbmVkIGlkZW50aWZpZXIgZm9yIHRoaXMgcmVnaW9uLlxuICBpZD1cInJ1ODY0XCJcblxuICAjIERlc2NyaXB0aW9uIGlzIGEgc2hvcnQgZGVzY3JpcHRpb24gZm9yIHRoaXMgcmVnaW9uLlxuICBkZXNjcmlwdGlvbj1cIlJVODY0XCJcblxuICAjIENvbW1vbi1uYW1lIHJlZmVycyB0byB0aGUgY29tbW9uLW5hbWUgb2YgdGhpcyByZWdpb24gYXMgZGVmaW5lZCBieVxuICAjIHRoZSBMb1JhIEFsbGlhbmNlLlxuICBjb21tb25fbmFtZT1cIlJVODY0XCJcblxuXG4gICMgR2F0ZXdheSBjb25maWd1cmF0aW9uLlxuICBbcmVnaW9ucy5nYXRld2F5XVxuXG4gICAgIyBGb3JjZSBnYXRld2F5cyBhcyBwcml2YXRlLlxuICAgICNcbiAgICAjIElmIGVuYWJsZWQsIGdhdGV3YXlzIGNhbiBvbmx5IGJlIHVzZWQgYnkgZGV2aWNlcyB1bmRlciB0aGUgc2FtZSB0ZW5hbnQuXG4gICAgZm9yY2VfZ3dzX3ByaXZhdGU9ZmFsc2VcblxuXG4gICAgIyBHYXRld2F5IGJhY2tlbmQgY29uZmlndXJhdGlvbi5cbiAgICBbcmVnaW9ucy5nYXRld2F5LmJhY2tlbmRdXG5cbiAgICAgICMgVGhlIGVuYWJsZWQgYmFja2VuZCB0eXBlLlxuICAgICAgZW5hYmxlZD1cIm1xdHRcIlxuXG4gICAgICAjIE1RVFQgY29uZmlndXJhdGlvbi5cbiAgICAgIFtyZWdpb25zLmdhdGV3YXkuYmFja2VuZC5tcXR0XVxuXG4gICAgICAgICMgVG9waWMgcHJlZml4LlxuICAgICAgICAjXG4gICAgICAgICMgVGhlIHRvcGljIHByZWZpeCBjYW4gYmUgdXNlZCB0byBkZWZpbmUgdGhlIHJlZ2lvbiBvZiB0aGUgZ2F0ZXdheS5cbiAgICAgICAgIyBOb3RlLCB0aGVyZSBpcyBubyBuZWVkIHRvIGFkZCBhIHRyYWlsaW5nICcvJyB0byB0aGUgcHJlZml4LiBUaGUgdHJhaWxpbmdcbiAgICAgICAgIyAnLycgaXMgYXV0b21hdGljYWxseSBhZGRlZCB0byB0aGUgcHJlZml4IGlmIGl0IGlzIGNvbmZpZ3VyZWQuXG4gICAgICAgIHRvcGljX3ByZWZpeD1cInJ1ODY0XCJcblxuICAgICAgICAjIE1RVFQgc2VydmVyIChlLmcuIHNjaGVtZTovL2hvc3Q6cG9ydCB3aGVyZSBzY2hlbWUgaXMgdGNwLCBzc2wgb3Igd3MpXG4gICAgICAgIHNlcnZlcj1cInRjcDovL21vc3F1aXR0bzoxODgzXCJcblxuICAgICAgICAjIENvbm5lY3Qgd2l0aCB0aGUgZ2l2ZW4gdXNlcm5hbWUgKG9wdGlvbmFsKVxuICAgICAgICB1c2VybmFtZT1cIlwiXG5cbiAgICAgICAgIyBDb25uZWN0IHdpdGggdGhlIGdpdmVuIHBhc3N3b3JkIChvcHRpb25hbClcbiAgICAgICAgcGFzc3dvcmQ9XCJcIlxuXG4gICAgICAgICMgUXVhbGl0eSBvZiBzZXJ2aWNlIGxldmVsXG4gICAgICAgICNcbiAgICAgICAgIyAwOiBhdCBtb3N0IG9uY2VcbiAgICAgICAgIyAxOiBhdCBsZWFzdCBvbmNlXG4gICAgICAgICMgMjogZXhhY3RseSBvbmNlXG4gICAgICAgICNcbiAgICAgICAgIyBOb3RlOiBhbiBpbmNyZWFzZSBvZiB0aGlzIHZhbHVlIHdpbGwgZGVjcmVhc2UgdGhlIHBlcmZvcm1hbmNlLlxuICAgICAgICAjIEZvciBtb3JlIGluZm9ybWF0aW9uOiBodHRwczovL3d3dy5oaXZlbXEuY29tL2Jsb2cvbXF0dC1lc3NlbnRpYWxzLXBhcnQtNi1tcXR0LXF1YWxpdHktb2Ytc2VydmljZS1sZXZlbHNcbiAgICAgICAgcW9zPTBcblxuICAgICAgICAjIENsZWFuIHNlc3Npb25cbiAgICAgICAgI1xuICAgICAgICAjIFNldCB0aGUgXCJjbGVhbiBzZXNzaW9uXCIgZmxhZyBpbiB0aGUgY29ubmVjdCBtZXNzYWdlIHdoZW4gdGhpcyBjbGllbnRcbiAgICAgICAgIyBjb25uZWN0cyB0byBhbiBNUVRUIGJyb2tlci4gQnkgc2V0dGluZyB0aGlzIGZsYWcgeW91IGFyZSBpbmRpY2F0aW5nXG4gICAgICAgICMgdGhhdCBubyBtZXNzYWdlcyBzYXZlZCBieSB0aGUgYnJva2VyIGZvciB0aGlzIGNsaWVudCBzaG91bGQgYmUgZGVsaXZlcmVkLlxuICAgICAgICBjbGVhbl9zZXNzaW9uPWZhbHNlXG5cbiAgICAgICAgIyBDbGllbnQgSURcbiAgICAgICAgI1xuICAgICAgICAjIFNldCB0aGUgY2xpZW50IGlkIHRvIGJlIHVzZWQgYnkgdGhpcyBjbGllbnQgd2hlbiBjb25uZWN0aW5nIHRvIHRoZSBNUVRUXG4gICAgICAgICMgYnJva2VyLiBBIGNsaWVudCBpZCBtdXN0IGJlIG5vIGxvbmdlciB0aGFuIDIzIGNoYXJhY3RlcnMuIElmIGxlZnQgYmxhbmssXG4gICAgICAgICMgYSByYW5kb20gaWQgd2lsbCBiZSBnZW5lcmF0ZWQgYnkgQ2hpcnBTdGFjay5cbiAgICAgICAgY2xpZW50X2lkPVwiXCJcblxuICAgICAgICAjIEtlZXAgYWxpdmUgaW50ZXJ2YWwuXG4gICAgICAgICNcbiAgICAgICAgIyBUaGlzIGRlZmluZXMgdGhlIG1heGltdW0gdGltZSB0aGF0IHRoYXQgc2hvdWxkIHBhc3Mgd2l0aG91dCBjb21tdW5pY2F0aW9uXG4gICAgICAgICMgYmV0d2VlbiB0aGUgY2xpZW50IGFuZCBzZXJ2ZXIuXG4gICAgICAgIGtlZXBfYWxpdmVfaW50ZXJ2YWw9XCIzMHNcIlxuXG4gICAgICAgICMgQ0EgY2VydGlmaWNhdGUgZmlsZSAob3B0aW9uYWwpXG4gICAgICAgICNcbiAgICAgICAgIyBVc2UgdGhpcyB3aGVuIHNldHRpbmcgdXAgYSBzZWN1cmUgY29ubmVjdGlvbiAod2hlbiBzZXJ2ZXIgdXNlcyBzc2w6Ly8uLi4pXG4gICAgICAgICMgYnV0IHRoZSBjZXJ0aWZpY2F0ZSB1c2VkIGJ5IHRoZSBzZXJ2ZXIgaXMgbm90IHRydXN0ZWQgYnkgYW55IENBIGNlcnRpZmljYXRlXG4gICAgICAgICMgb24gdGhlIHNlcnZlciAoZS5nLiB3aGVuIHNlbGYgZ2VuZXJhdGVkKS5cbiAgICAgICAgY2FfY2VydD1cIlwiXG5cbiAgICAgICAgIyBUTFMgY2VydGlmaWNhdGUgZmlsZSAob3B0aW9uYWwpXG4gICAgICAgIHRsc19jZXJ0PVwiXCJcblxuICAgICAgICAjIFRMUyBrZXkgZmlsZSAob3B0aW9uYWwpXG4gICAgICAgIHRsc19rZXk9XCJcIlxuXG5cbiAgICAjIEdhdGV3YXkgY2hhbm5lbCBjb25maWd1cmF0aW9uLlxuICAgICNcbiAgICAjIE5vdGU6IHRoaXMgY29uZmlndXJhdGlvbiBpcyBvbmx5IHVzZWQgaW4gY2FzZSB0aGUgZ2F0ZXdheSBpcyB1c2luZyB0aGVcbiAgICAjIENoaXJwU3RhY2sgQ29uY2VudHJhdG9yZCBkYWVtb24uIEluIGFueSBvdGhlciBjYXNlLCB0aGlzIGNvbmZpZ3VyYXRpb24gXG4gICAgIyBpcyBpZ25vcmVkLlxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT04Njg5MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMCwgMTEsIDEyXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTg2OTEwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwLCAxMSwgMTJdXG5cblxuICAjIFJlZ2lvbiBzcGVjaWZpYyBuZXR3b3JrIGNvbmZpZ3VyYXRpb24uXG4gIFtyZWdpb25zLm5ldHdvcmtdXG4gICAgXG4gICAgIyBJbnN0YWxsYXRpb24gbWFyZ2luIChkQikgdXNlZCBieSB0aGUgQURSIGVuZ2luZS5cbiAgICAjXG4gICAgIyBBIGhpZ2hlciBudW1iZXIgbWVhbnMgdGhhdCB0aGUgbmV0d29yay1zZXJ2ZXIgd2lsbCBrZWVwIG1vcmUgbWFyZ2luLFxuICAgICMgcmVzdWx0aW5nIGluIGEgbG93ZXIgZGF0YS1yYXRlIGJ1dCBkZWNyZWFzaW5nIHRoZSBjaGFuY2UgdGhhdCB0aGVcbiAgICAjIGRldmljZSBnZXRzIGRpc2Nvbm5lY3RlZCBiZWNhdXNlIGl0IGlzIHVuYWJsZSB0byByZWFjaCBvbmUgb2YgdGhlXG4gICAgIyBzdXJyb3VuZGVkIGdhdGV3YXlzLlxuICAgIGluc3RhbGxhdGlvbl9tYXJnaW49MTBcblxuICAgICMgUlggd2luZG93IChDbGFzcy1BKS5cbiAgICAjXG4gICAgIyBTZXQgdGhpcyB0bzpcbiAgICAjIDA6IFJYMSAvIFJYMlxuICAgICMgMTogUlgxIG9ubHlcbiAgICAjIDI6IFJYMiBvbmx5XG4gICAgcnhfd2luZG93PTBcblxuICAgICMgUlgxIGRlbGF5ICgxIC0gMTUgc2Vjb25kcykuXG4gICAgcngxX2RlbGF5PTFcblxuICAgICMgUlgxIGRhdGEtcmF0ZSBvZmZzZXRcbiAgICByeDFfZHJfb2Zmc2V0PTBcblxuICAgICMgUlgyIGRhdGEtcmF0ZVxuICAgIHJ4Ml9kcj0wXG5cbiAgICAjIFJYMiBmcmVxdWVuY3kgKEh6KVxuICAgIHJ4Ml9mcmVxdWVuY3k9ODY5MTAwMDAwXG5cbiAgICAjIFByZWZlciBSWDIgb24gUlgxIGRhdGEtcmF0ZSBsZXNzIHRoYW4uXG4gICAgI1xuICAgICMgUHJlZmVyIFJYMiBvdmVyIFJYMSBiYXNlZCBvbiB0aGUgUlgxIGRhdGEtcmF0ZS4gV2hlbiB0aGUgUlgxIGRhdGEtcmF0ZVxuICAgICMgaXMgc21hbGxlciB0aGFuIHRoZSBjb25maWd1cmVkIHZhbHVlLCB0aGVuIHRoZSBOZXR3b3JrIFNlcnZlciB3aWxsXG4gICAgIyBmaXJzdCB0cnkgdG8gc2NoZWR1bGUgdGhlIGRvd25saW5rIGZvciBSWDIsIGZhaWxpbmcgdGhhdCAoZS5nLiB0aGUgZ2F0ZXdheVxuICAgICMgaGFzIGFscmVhZHkgYSBwYXlsb2FkIHNjaGVkdWxlZCBhdCB0aGUgUlgyIHRpbWluZykgaXQgd2lsbCB0cnkgUlgxLlxuICAgIHJ4Ml9wcmVmZXJfb25fcngxX2RyX2x0PTBcblxuICAgICMgUHJlZmVyIFJYMiBvbiBsaW5rIGJ1ZGdldC5cbiAgICAjXG4gICAgIyBXaGVuIHRoZSBsaW5rLWJ1ZGdldCBpcyBiZXR0ZXIgZm9yIFJYMiB0aGFuIGZvciBSWDEsIHRoZSBOZXR3b3JrIFNlcnZlciB3aWxsIGZpcnN0XG4gICAgIyB0cnkgdG8gc2NoZWR1bGUgdGhlIGRvd25saW5rIGluIFJYMiwgZmFpbGluZyB0aGF0IGl0IHdpbGwgdHJ5IFJYMS5cbiAgICByeDJfcHJlZmVyX29uX2xpbmtfYnVkZ2V0PWZhbHNlXG5cbiAgICAjIERvd25saW5rIFRYIFBvd2VyIChkQm0pXG4gICAgI1xuICAgICMgV2hlbiBzZXQgdG8gLTEsIHRoZSBkb3dubGluayBUWCBQb3dlciBmcm9tIHRoZSBjb25maWd1cmVkIGJhbmQgd2lsbFxuICAgICMgYmUgdXNlZC5cbiAgICAjXG4gICAgIyBQbGVhc2UgY29uc3VsdCB0aGUgTG9SYVdBTiBSZWdpb25hbCBQYXJhbWV0ZXJzIGFuZCBsb2NhbCByZWd1bGF0aW9uc1xuICAgICMgZm9yIHZhbGlkIGFuZCBsZWdhbCBvcHRpb25zLiBOb3RlIHRoYXQgdGhlIGNvbmZpZ3VyZWQgVFggUG93ZXIgbXVzdCBiZVxuICAgICMgc3VwcG9ydGVkIGJ5IHlvdXIgZ2F0ZXdheShzKS5cbiAgICBkb3dubGlua190eF9wb3dlcj0tMVxuXG4gICAgIyBBRFIgaXMgZGlzYWJsZWQuXG4gICAgYWRyX2Rpc2FibGVkPWZhbHNlXG5cbiAgICAjIE1pbmltdW0gZGF0YS1yYXRlLlxuICAgIG1pbl9kcj0wXG5cbiAgICAjIE1heGltdW0gZGF0YS1yYXRlLlxuICAgIG1heF9kcj01XG5cblxuICAgICMgUmVqb2luLXJlcXVlc3QgY29uZmlndXJhdGlvbiAoTG9SYVdBTiAxLjEpXG4gICAgW3JlZ2lvbnMubmV0d29yay5yZWpvaW5fcmVxdWVzdF1cblxuICAgICAgIyBSZXF1ZXN0IGRldmljZXMgdG8gcGVyaW9kaWNhbGx5IHNlbmQgcmVqb2luLXJlcXVlc3RzLlxuICAgICAgZW5hYmxlZD1mYWxzZVxuXG4gICAgICAjIFRoZSBkZXZpY2UgbXVzdCBzZW5kIGEgcmVqb2luLXJlcXVlc3QgdHlwZSAwIGF0IGxlYXN0IGV2ZXJ5IDJeKG1heF9jb3VudF9uICsgNClcbiAgICAgICMgdXBsaW5rIG1lc3NhZ2VzLiBWYWxpZCB2YWx1ZXMgYXJlIDAgdG8gMTUuXG4gICAgICBtYXhfY291bnRfbj0wXG5cbiAgICAgICMgVGhlIGRldmljZSBtdXN0IHNlbmQgYSByZWpvaW4tcmVxdWVzdCB0eXBlIDAgYXQgbGVhc3QgZXZlcnkgMl4obWF4X3RpbWVfbiArIDEwKVxuICAgICAgIyBzZWNvbmRzLiBWYWxpZCB2YWx1ZXMgYXJlIDAgdG8gMTUuXG4gICAgICAjXG4gICAgICAjIDAgID0gcm91Z2hseSAxNyBtaW51dGVzXG4gICAgICAjIDE1ID0gYWJvdXQgMSB5ZWFyXG4gICAgICBtYXhfdGltZV9uPTBcbiAgICBcblxuICAgICMgQ2xhc3MtQiBjb25maWd1cmF0aW9uLlxuICAgIFtyZWdpb25zLm5ldHdvcmsuY2xhc3NfYl1cblxuICAgICAgIyBQaW5nLXNsb3QgZGF0YS1yYXRlLiBcbiAgICAgIHBpbmdfc2xvdF9kcj0zXG5cbiAgICAgICMgUGluZy1zbG90IGZyZXF1ZW5jeSAoSHopXG4gICAgICAjXG4gICAgICAjIHNldCB0aGlzIHRvIDAgdG8gdXNlIHRoZSBkZWZhdWx0IGZyZXF1ZW5jeSBwbGFuIGZvciB0aGUgY29uZmlndXJlZCByZWdpb25cbiAgICAgICMgKHdoaWNoIGNvdWxkIGJlIGZyZXF1ZW5jeSBob3BwaW5nKS5cbiAgICAgIHBpbmdfc2xvdF9mcmVxdWVuY3k9MFxuXCJcIlwiXG5cbltbY29uZmlnLm1vdW50c11dXG5zZXJ2aWNlTmFtZSA9IFwiY2hpcnBzdGFja1wiXG5maWxlUGF0aCA9IFwiL2NoaXJwc3RhY2svcmVnaW9uX3VzOTE1XzAudG9tbFwiXG5jb250ZW50ID0gXCJcIlwiXG4jIFRoaXMgZmlsZSBjb250YWlucyBhbiBleGFtcGxlIFVTOTE1IGV4YW1wbGUgKGNoYW5uZWxzIDAtNyArIDY0KS5cbltbcmVnaW9uc11dXG5cbiAgIyBJRCBpcyBhbiB1c2UtZGVmaW5lZCBpZGVudGlmaWVyIGZvciB0aGlzIHJlZ2lvbi5cbiAgaWQ9XCJ1czkxNV8wXCJcblxuICAjIERlc2NyaXB0aW9uIGlzIGEgc2hvcnQgZGVzY3JpcHRpb24gZm9yIHRoaXMgcmVnaW9uLlxuICBkZXNjcmlwdGlvbj1cIlVTOTE1IChjaGFubmVscyAwLTcgKyA2NClcIlxuXG4gICMgQ29tbW9uLW5hbWUgcmVmZXJzIHRvIHRoZSBjb21tb24tbmFtZSBvZiB0aGlzIHJlZ2lvbiBhcyBkZWZpbmVkIGJ5XG4gICMgdGhlIExvUmEgQWxsaWFuY2UuXG4gIGNvbW1vbl9uYW1lPVwiVVM5MTVcIlxuXG5cbiAgIyBHYXRld2F5IGNvbmZpZ3VyYXRpb24uXG4gIFtyZWdpb25zLmdhdGV3YXldXG5cbiAgICAjIEZvcmNlIGdhdGV3YXlzIGFzIHByaXZhdGUuXG4gICAgI1xuICAgICMgSWYgZW5hYmxlZCwgZ2F0ZXdheXMgY2FuIG9ubHkgYmUgdXNlZCBieSBkZXZpY2VzIHVuZGVyIHRoZSBzYW1lIHRlbmFudC5cbiAgICBmb3JjZV9nd3NfcHJpdmF0ZT1mYWxzZVxuXG4gICAgXG4gICAgIyBHYXRld2F5IGJhY2tlbmQgY29uZmlndXJhdGlvbi5cbiAgICBbcmVnaW9ucy5nYXRld2F5LmJhY2tlbmRdXG5cbiAgICAgICMgVGhlIGVuYWJsZWQgYmFja2VuZCB0eXBlLlxuICAgICAgZW5hYmxlZD1cIm1xdHRcIlxuXG4gICAgICAjIE1RVFQgY29uZmlndXJhdGlvbi5cbiAgICAgIFtyZWdpb25zLmdhdGV3YXkuYmFja2VuZC5tcXR0XVxuXG4gICAgICAgICMgVG9waWMgcHJlZml4LlxuICAgICAgICAjXG4gICAgICAgICMgVGhlIHRvcGljIHByZWZpeCBjYW4gYmUgdXNlZCB0byBkZWZpbmUgdGhlIHJlZ2lvbiBvZiB0aGUgZ2F0ZXdheS5cbiAgICAgICAgIyBOb3RlLCB0aGVyZSBpcyBubyBuZWVkIHRvIGFkZCBhIHRyYWlsaW5nICcvJyB0byB0aGUgcHJlZml4LiBUaGUgdHJhaWxpbmdcbiAgICAgICAgIyAnLycgaXMgYXV0b21hdGljYWxseSBhZGRlZCB0byB0aGUgcHJlZml4IGlmIGl0IGlzIGNvbmZpZ3VyZWQuXG4gICAgICAgIHRvcGljX3ByZWZpeD1cInVzOTE1XzBcIlxuXG4gICAgICAgICMgTVFUVCBzZXJ2ZXIgKGUuZy4gc2NoZW1lOi8vaG9zdDpwb3J0IHdoZXJlIHNjaGVtZSBpcyB0Y3AsIHNzbCBvciB3cylcbiAgICAgICAgc2VydmVyPVwidGNwOi8vbW9zcXVpdHRvOjE4ODNcIlxuXG4gICAgICAgICMgQ29ubmVjdCB3aXRoIHRoZSBnaXZlbiB1c2VybmFtZSAob3B0aW9uYWwpXG4gICAgICAgIHVzZXJuYW1lPVwiXCJcblxuICAgICAgICAjIENvbm5lY3Qgd2l0aCB0aGUgZ2l2ZW4gcGFzc3dvcmQgKG9wdGlvbmFsKVxuICAgICAgICBwYXNzd29yZD1cIlwiXG5cbiAgICAgICAgIyBRdWFsaXR5IG9mIHNlcnZpY2UgbGV2ZWxcbiAgICAgICAgI1xuICAgICAgICAjIDA6IGF0IG1vc3Qgb25jZVxuICAgICAgICAjIDE6IGF0IGxlYXN0IG9uY2VcbiAgICAgICAgIyAyOiBleGFjdGx5IG9uY2VcbiAgICAgICAgI1xuICAgICAgICAjIE5vdGU6IGFuIGluY3JlYXNlIG9mIHRoaXMgdmFsdWUgd2lsbCBkZWNyZWFzZSB0aGUgcGVyZm9ybWFuY2UuXG4gICAgICAgICMgRm9yIG1vcmUgaW5mb3JtYXRpb246IGh0dHBzOi8vd3d3LmhpdmVtcS5jb20vYmxvZy9tcXR0LWVzc2VudGlhbHMtcGFydC02LW1xdHQtcXVhbGl0eS1vZi1zZXJ2aWNlLWxldmVsc1xuICAgICAgICBxb3M9MFxuXG4gICAgICAgICMgQ2xlYW4gc2Vzc2lvblxuICAgICAgICAjXG4gICAgICAgICMgU2V0IHRoZSBcImNsZWFuIHNlc3Npb25cIiBmbGFnIGluIHRoZSBjb25uZWN0IG1lc3NhZ2Ugd2hlbiB0aGlzIGNsaWVudFxuICAgICAgICAjIGNvbm5lY3RzIHRvIGFuIE1RVFQgYnJva2VyLiBCeSBzZXR0aW5nIHRoaXMgZmxhZyB5b3UgYXJlIGluZGljYXRpbmdcbiAgICAgICAgIyB0aGF0IG5vIG1lc3NhZ2VzIHNhdmVkIGJ5IHRoZSBicm9rZXIgZm9yIHRoaXMgY2xpZW50IHNob3VsZCBiZSBkZWxpdmVyZWQuXG4gICAgICAgIGNsZWFuX3Nlc3Npb249ZmFsc2VcblxuICAgICAgICAjIENsaWVudCBJRFxuICAgICAgICAjXG4gICAgICAgICMgU2V0IHRoZSBjbGllbnQgaWQgdG8gYmUgdXNlZCBieSB0aGlzIGNsaWVudCB3aGVuIGNvbm5lY3RpbmcgdG8gdGhlIE1RVFRcbiAgICAgICAgIyBicm9rZXIuIEEgY2xpZW50IGlkIG11c3QgYmUgbm8gbG9uZ2VyIHRoYW4gMjMgY2hhcmFjdGVycy4gSWYgbGVmdCBibGFuayxcbiAgICAgICAgIyBhIHJhbmRvbSBpZCB3aWxsIGJlIGdlbmVyYXRlZCBieSBDaGlycFN0YWNrLlxuICAgICAgICBjbGllbnRfaWQ9XCJcIlxuXG4gICAgICAgICMgS2VlcCBhbGl2ZSBpbnRlcnZhbC5cbiAgICAgICAgI1xuICAgICAgICAjIFRoaXMgZGVmaW5lcyB0aGUgbWF4aW11bSB0aW1lIHRoYXQgdGhhdCBzaG91bGQgcGFzcyB3aXRob3V0IGNvbW11bmljYXRpb25cbiAgICAgICAgIyBiZXR3ZWVuIHRoZSBjbGllbnQgYW5kIHNlcnZlci5cbiAgICAgICAga2VlcF9hbGl2ZV9pbnRlcnZhbD1cIjMwc1wiXG5cbiAgICAgICAgIyBDQSBjZXJ0aWZpY2F0ZSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgI1xuICAgICAgICAjIFVzZSB0aGlzIHdoZW4gc2V0dGluZyB1cCBhIHNlY3VyZSBjb25uZWN0aW9uICh3aGVuIHNlcnZlciB1c2VzIHNzbDovLy4uLilcbiAgICAgICAgIyBidXQgdGhlIGNlcnRpZmljYXRlIHVzZWQgYnkgdGhlIHNlcnZlciBpcyBub3QgdHJ1c3RlZCBieSBhbnkgQ0EgY2VydGlmaWNhdGVcbiAgICAgICAgIyBvbiB0aGUgc2VydmVyIChlLmcuIHdoZW4gc2VsZiBnZW5lcmF0ZWQpLlxuICAgICAgICBjYV9jZXJ0PVwiXCJcblxuICAgICAgICAjIFRMUyBjZXJ0aWZpY2F0ZSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgdGxzX2NlcnQ9XCJcIlxuXG4gICAgICAgICMgVExTIGtleSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgdGxzX2tleT1cIlwiXG5cblxuICAgICMgR2F0ZXdheSBjaGFubmVsIGNvbmZpZ3VyYXRpb24uXG4gICAgI1xuICAgICMgTm90ZTogdGhpcyBjb25maWd1cmF0aW9uIGlzIG9ubHkgdXNlZCBpbiBjYXNlIHRoZSBnYXRld2F5IGlzIHVzaW5nIHRoZVxuICAgICMgQ2hpcnBTdGFjayBDb25jZW50cmF0b3JkIGRhZW1vbi4gSW4gYW55IG90aGVyIGNhc2UsIHRoaXMgY29uZmlndXJhdGlvbiBcbiAgICAjIGlzIGlnbm9yZWQuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkwMjMwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkwMjUwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkwMjcwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkwMjkwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkwMzEwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkwMzMwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkwMzUwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkwMzcwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkwMzAwMDAwMFxuICAgICAgYmFuZHdpZHRoPTUwMDAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzhdXG5cblxuICAjIFJlZ2lvbiBzcGVjaWZpYyBuZXR3b3JrIGNvbmZpZ3VyYXRpb24uXG4gIFtyZWdpb25zLm5ldHdvcmtdXG4gICAgXG4gICAgIyBJbnN0YWxsYXRpb24gbWFyZ2luIChkQikgdXNlZCBieSB0aGUgQURSIGVuZ2luZS5cbiAgICAjXG4gICAgIyBBIGhpZ2hlciBudW1iZXIgbWVhbnMgdGhhdCB0aGUgbmV0d29yay1zZXJ2ZXIgd2lsbCBrZWVwIG1vcmUgbWFyZ2luLFxuICAgICMgcmVzdWx0aW5nIGluIGEgbG93ZXIgZGF0YS1yYXRlIGJ1dCBkZWNyZWFzaW5nIHRoZSBjaGFuY2UgdGhhdCB0aGVcbiAgICAjIGRldmljZSBnZXRzIGRpc2Nvbm5lY3RlZCBiZWNhdXNlIGl0IGlzIHVuYWJsZSB0byByZWFjaCBvbmUgb2YgdGhlXG4gICAgIyBzdXJyb3VuZGVkIGdhdGV3YXlzLlxuICAgIGluc3RhbGxhdGlvbl9tYXJnaW49MTBcblxuICAgICMgUlggd2luZG93IChDbGFzcy1BKS5cbiAgICAjXG4gICAgIyBTZXQgdGhpcyB0bzpcbiAgICAjIDA6IFJYMSAvIFJYMlxuICAgICMgMTogUlgxIG9ubHlcbiAgICAjIDI6IFJYMiBvbmx5XG4gICAgcnhfd2luZG93PTBcblxuICAgICMgUlgxIGRlbGF5ICgxIC0gMTUgc2Vjb25kcykuXG4gICAgcngxX2RlbGF5PTFcblxuICAgICMgUlgxIGRhdGEtcmF0ZSBvZmZzZXRcbiAgICByeDFfZHJfb2Zmc2V0PTBcblxuICAgICMgUlgyIGRhdGEtcmF0ZVxuICAgIHJ4Ml9kcj04XG5cbiAgICAjIFJYMiBmcmVxdWVuY3kgKEh6KVxuICAgIHJ4Ml9mcmVxdWVuY3k9OTIzMzAwMDAwXG5cbiAgICAjIFByZWZlciBSWDIgb24gUlgxIGRhdGEtcmF0ZSBsZXNzIHRoYW4uXG4gICAgI1xuICAgICMgUHJlZmVyIFJYMiBvdmVyIFJYMSBiYXNlZCBvbiB0aGUgUlgxIGRhdGEtcmF0ZS4gV2hlbiB0aGUgUlgxIGRhdGEtcmF0ZVxuICAgICMgaXMgc21hbGxlciB0aGFuIHRoZSBjb25maWd1cmVkIHZhbHVlLCB0aGVuIHRoZSBOZXR3b3JrIFNlcnZlciB3aWxsXG4gICAgIyBmaXJzdCB0cnkgdG8gc2NoZWR1bGUgdGhlIGRvd25saW5rIGZvciBSWDIsIGZhaWxpbmcgdGhhdCAoZS5nLiB0aGUgZ2F0ZXdheVxuICAgICMgaGFzIGFscmVhZHkgYSBwYXlsb2FkIHNjaGVkdWxlZCBhdCB0aGUgUlgyIHRpbWluZykgaXQgd2lsbCB0cnkgUlgxLlxuICAgIHJ4Ml9wcmVmZXJfb25fcngxX2RyX2x0PTBcblxuICAgICMgUHJlZmVyIFJYMiBvbiBsaW5rIGJ1ZGdldC5cbiAgICAjXG4gICAgIyBXaGVuIHRoZSBsaW5rLWJ1ZGdldCBpcyBiZXR0ZXIgZm9yIFJYMiB0aGFuIGZvciBSWDEsIHRoZSBOZXR3b3JrIFNlcnZlciB3aWxsIGZpcnN0XG4gICAgIyB0cnkgdG8gc2NoZWR1bGUgdGhlIGRvd25saW5rIGluIFJYMiwgZmFpbGluZyB0aGF0IGl0IHdpbGwgdHJ5IFJYMS5cbiAgICByeDJfcHJlZmVyX29uX2xpbmtfYnVkZ2V0PWZhbHNlXG5cbiAgICAjIERvd25saW5rIFRYIFBvd2VyIChkQm0pXG4gICAgI1xuICAgICMgV2hlbiBzZXQgdG8gLTEsIHRoZSBkb3dubGluayBUWCBQb3dlciBmcm9tIHRoZSBjb25maWd1cmVkIGJhbmQgd2lsbFxuICAgICMgYmUgdXNlZC5cbiAgICAjXG4gICAgIyBQbGVhc2UgY29uc3VsdCB0aGUgTG9SYVdBTiBSZWdpb25hbCBQYXJhbWV0ZXJzIGFuZCBsb2NhbCByZWd1bGF0aW9uc1xuICAgICMgZm9yIHZhbGlkIGFuZCBsZWdhbCBvcHRpb25zLiBOb3RlIHRoYXQgdGhlIGNvbmZpZ3VyZWQgVFggUG93ZXIgbXVzdCBiZVxuICAgICMgc3VwcG9ydGVkIGJ5IHlvdXIgZ2F0ZXdheShzKS5cbiAgICBkb3dubGlua190eF9wb3dlcj0tMVxuXG4gICAgIyBBRFIgaXMgZGlzYWJsZWQuXG4gICAgYWRyX2Rpc2FibGVkPWZhbHNlXG5cbiAgICAjIE1pbmltdW0gZGF0YS1yYXRlLlxuICAgIG1pbl9kcj0wXG5cbiAgICAjIE1heGltdW0gZGF0YS1yYXRlLlxuICAgIG1heF9kcj0zXG5cbiAgICAjIEVuYWJsZWQgdXBsaW5rIGNoYW5uZWxzLlxuICAgICNcbiAgICAjIFVzZSB0aGlzIHdoZW4gb255IGEgc3ViLXNldCBvZiB0aGUgYnkgZGVmYXVsdCBlbmFibGVkIGNoYW5uZWxzIGFyZSBiZWluZ1xuICAgICMgdXNlZC4gRm9yIGV4YW1wbGUgd2hlbiBvbmx5IHVzaW5nIHRoZSBmaXJzdCA4IGNoYW5uZWxzIG9mIHRoZSBVUyBiYW5kLlxuICAgICMgTm90ZTogd2hlbiBsZWZ0IGJsYW5rIC8gZW1wdHkgYXJyYXksIGFsbCBjaGFubmVscyB3aWxsIGJlIGVuYWJsZWQuXG4gICAgZW5hYmxlZF91cGxpbmtfY2hhbm5lbHM9WzAsIDEsIDIsIDMsIDQsIDUsIDYsIDcsIDY0XVxuXG5cbiAgICAjIFJlam9pbi1yZXF1ZXN0IGNvbmZpZ3VyYXRpb24gKExvUmFXQU4gMS4xKVxuICAgIFtyZWdpb25zLm5ldHdvcmsucmVqb2luX3JlcXVlc3RdXG5cbiAgICAgICMgUmVxdWVzdCBkZXZpY2VzIHRvIHBlcmlvZGljYWxseSBzZW5kIHJlam9pbi1yZXF1ZXN0cy5cbiAgICAgIGVuYWJsZWQ9ZmFsc2VcblxuICAgICAgIyBUaGUgZGV2aWNlIG11c3Qgc2VuZCBhIHJlam9pbi1yZXF1ZXN0IHR5cGUgMCBhdCBsZWFzdCBldmVyeSAyXihtYXhfY291bnRfbiArIDQpXG4gICAgICAjIHVwbGluayBtZXNzYWdlcy4gVmFsaWQgdmFsdWVzIGFyZSAwIHRvIDE1LlxuICAgICAgbWF4X2NvdW50X249MFxuXG4gICAgICAjIFRoZSBkZXZpY2UgbXVzdCBzZW5kIGEgcmVqb2luLXJlcXVlc3QgdHlwZSAwIGF0IGxlYXN0IGV2ZXJ5IDJeKG1heF90aW1lX24gKyAxMClcbiAgICAgICMgc2Vjb25kcy4gVmFsaWQgdmFsdWVzIGFyZSAwIHRvIDE1LlxuICAgICAgI1xuICAgICAgIyAwICA9IHJvdWdobHkgMTcgbWludXRlc1xuICAgICAgIyAxNSA9IGFib3V0IDEgeWVhclxuICAgICAgbWF4X3RpbWVfbj0wXG4gICAgXG5cbiAgICAjIENsYXNzLUIgY29uZmlndXJhdGlvbi5cbiAgICBbcmVnaW9ucy5uZXR3b3JrLmNsYXNzX2JdXG5cbiAgICAgICMgUGluZy1zbG90IGRhdGEtcmF0ZS4gXG4gICAgICBwaW5nX3Nsb3RfZHI9OFxuXG4gICAgICAjIFBpbmctc2xvdCBmcmVxdWVuY3kgKEh6KVxuICAgICAgI1xuICAgICAgIyBzZXQgdGhpcyB0byAwIHRvIHVzZSB0aGUgZGVmYXVsdCBmcmVxdWVuY3kgcGxhbiBmb3IgdGhlIGNvbmZpZ3VyZWQgcmVnaW9uXG4gICAgICAjICh3aGljaCBjb3VsZCBiZSBmcmVxdWVuY3kgaG9wcGluZykuXG4gICAgICBwaW5nX3Nsb3RfZnJlcXVlbmN5PTBcblwiXCJcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuc2VydmljZU5hbWUgPSBcImNoaXJwc3RhY2tcIlxuZmlsZVBhdGggPSBcIi9jaGlycHN0YWNrL3JlZ2lvbl91czkxNV8xLnRvbWxcIlxuY29udGVudCA9IFwiXCJcIlxuIyBUaGlzIGZpbGUgY29udGFpbnMgYW4gZXhhbXBsZSBVUzkxNSBleGFtcGxlIChjaGFubmVscyA4LTE1ICsgNjUpLlxuW1tyZWdpb25zXV1cblxuICAjIElEIGlzIGFuIHVzZS1kZWZpbmVkIGlkZW50aWZpZXIgZm9yIHRoaXMgcmVnaW9uLlxuICBpZD1cInVzOTE1XzFcIlxuXG4gICMgRGVzY3JpcHRpb24gaXMgYSBzaG9ydCBkZXNjcmlwdGlvbiBmb3IgdGhpcyByZWdpb24uXG4gIGRlc2NyaXB0aW9uPVwiVVM5MTUgKGNoYW5uZWxzIDgtMTUgKyA2NSlcIlxuXG4gICMgQ29tbW9uLW5hbWUgcmVmZXJzIHRvIHRoZSBjb21tb24tbmFtZSBvZiB0aGlzIHJlZ2lvbiBhcyBkZWZpbmVkIGJ5XG4gICMgdGhlIExvUmEgQWxsaWFuY2UuXG4gIGNvbW1vbl9uYW1lPVwiVVM5MTVcIlxuXG5cbiAgIyBHYXRld2F5IGNvbmZpZ3VyYXRpb24uXG4gIFtyZWdpb25zLmdhdGV3YXldXG5cbiAgICAjIEZvcmNlIGdhdGV3YXlzIGFzIHByaXZhdGUuXG4gICAgI1xuICAgICMgSWYgZW5hYmxlZCwgZ2F0ZXdheXMgY2FuIG9ubHkgYmUgdXNlZCBieSBkZXZpY2VzIHVuZGVyIHRoZSBzYW1lIHRlbmFudC5cbiAgICBmb3JjZV9nd3NfcHJpdmF0ZT1mYWxzZVxuXG4gICAgXG4gICAgIyBHYXRld2F5IGJhY2tlbmQgY29uZmlndXJhdGlvbi5cbiAgICBbcmVnaW9ucy5nYXRld2F5LmJhY2tlbmRdXG5cbiAgICAgICMgVGhlIGVuYWJsZWQgYmFja2VuZCB0eXBlLlxuICAgICAgZW5hYmxlZD1cIm1xdHRcIlxuXG4gICAgICAjIE1RVFQgY29uZmlndXJhdGlvbi5cbiAgICAgIFtyZWdpb25zLmdhdGV3YXkuYmFja2VuZC5tcXR0XVxuXG4gICAgICAgICMgVG9waWMgcHJlZml4LlxuICAgICAgICAjXG4gICAgICAgICMgVGhlIHRvcGljIHByZWZpeCBjYW4gYmUgdXNlZCB0byBkZWZpbmUgdGhlIHJlZ2lvbiBvZiB0aGUgZ2F0ZXdheS5cbiAgICAgICAgIyBOb3RlLCB0aGVyZSBpcyBubyBuZWVkIHRvIGFkZCBhIHRyYWlsaW5nICcvJyB0byB0aGUgcHJlZml4LiBUaGUgdHJhaWxpbmdcbiAgICAgICAgIyAnLycgaXMgYXV0b21hdGljYWxseSBhZGRlZCB0byB0aGUgcHJlZml4IGlmIGl0IGlzIGNvbmZpZ3VyZWQuXG4gICAgICAgIHRvcGljX3ByZWZpeD1cInVzOTE1XzFcIlxuXG4gICAgICAgICMgTVFUVCBzZXJ2ZXIgKGUuZy4gc2NoZW1lOi8vaG9zdDpwb3J0IHdoZXJlIHNjaGVtZSBpcyB0Y3AsIHNzbCBvciB3cylcbiAgICAgICAgc2VydmVyPVwidGNwOi8vbW9zcXVpdHRvOjE4ODNcIlxuXG4gICAgICAgICMgQ29ubmVjdCB3aXRoIHRoZSBnaXZlbiB1c2VybmFtZSAob3B0aW9uYWwpXG4gICAgICAgIHVzZXJuYW1lPVwiXCJcblxuICAgICAgICAjIENvbm5lY3Qgd2l0aCB0aGUgZ2l2ZW4gcGFzc3dvcmQgKG9wdGlvbmFsKVxuICAgICAgICBwYXNzd29yZD1cIlwiXG5cbiAgICAgICAgIyBRdWFsaXR5IG9mIHNlcnZpY2UgbGV2ZWxcbiAgICAgICAgI1xuICAgICAgICAjIDA6IGF0IG1vc3Qgb25jZVxuICAgICAgICAjIDE6IGF0IGxlYXN0IG9uY2VcbiAgICAgICAgIyAyOiBleGFjdGx5IG9uY2VcbiAgICAgICAgI1xuICAgICAgICAjIE5vdGU6IGFuIGluY3JlYXNlIG9mIHRoaXMgdmFsdWUgd2lsbCBkZWNyZWFzZSB0aGUgcGVyZm9ybWFuY2UuXG4gICAgICAgICMgRm9yIG1vcmUgaW5mb3JtYXRpb246IGh0dHBzOi8vd3d3LmhpdmVtcS5jb20vYmxvZy9tcXR0LWVzc2VudGlhbHMtcGFydC02LW1xdHQtcXVhbGl0eS1vZi1zZXJ2aWNlLWxldmVsc1xuICAgICAgICBxb3M9MFxuXG4gICAgICAgICMgQ2xlYW4gc2Vzc2lvblxuICAgICAgICAjXG4gICAgICAgICMgU2V0IHRoZSBcImNsZWFuIHNlc3Npb25cIiBmbGFnIGluIHRoZSBjb25uZWN0IG1lc3NhZ2Ugd2hlbiB0aGlzIGNsaWVudFxuICAgICAgICAjIGNvbm5lY3RzIHRvIGFuIE1RVFQgYnJva2VyLiBCeSBzZXR0aW5nIHRoaXMgZmxhZyB5b3UgYXJlIGluZGljYXRpbmdcbiAgICAgICAgIyB0aGF0IG5vIG1lc3NhZ2VzIHNhdmVkIGJ5IHRoZSBicm9rZXIgZm9yIHRoaXMgY2xpZW50IHNob3VsZCBiZSBkZWxpdmVyZWQuXG4gICAgICAgIGNsZWFuX3Nlc3Npb249ZmFsc2VcblxuICAgICAgICAjIENsaWVudCBJRFxuICAgICAgICAjXG4gICAgICAgICMgU2V0IHRoZSBjbGllbnQgaWQgdG8gYmUgdXNlZCBieSB0aGlzIGNsaWVudCB3aGVuIGNvbm5lY3RpbmcgdG8gdGhlIE1RVFRcbiAgICAgICAgIyBicm9rZXIuIEEgY2xpZW50IGlkIG11c3QgYmUgbm8gbG9uZ2VyIHRoYW4gMjMgY2hhcmFjdGVycy4gSWYgbGVmdCBibGFuayxcbiAgICAgICAgIyBhIHJhbmRvbSBpZCB3aWxsIGJlIGdlbmVyYXRlZCBieSBDaGlycFN0YWNrLlxuICAgICAgICBjbGllbnRfaWQ9XCJcIlxuXG4gICAgICAgICMgS2VlcCBhbGl2ZSBpbnRlcnZhbC5cbiAgICAgICAgI1xuICAgICAgICAjIFRoaXMgZGVmaW5lcyB0aGUgbWF4aW11bSB0aW1lIHRoYXQgdGhhdCBzaG91bGQgcGFzcyB3aXRob3V0IGNvbW11bmljYXRpb25cbiAgICAgICAgIyBiZXR3ZWVuIHRoZSBjbGllbnQgYW5kIHNlcnZlci5cbiAgICAgICAga2VlcF9hbGl2ZV9pbnRlcnZhbD1cIjMwc1wiXG5cbiAgICAgICAgIyBDQSBjZXJ0aWZpY2F0ZSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgI1xuICAgICAgICAjIFVzZSB0aGlzIHdoZW4gc2V0dGluZyB1cCBhIHNlY3VyZSBjb25uZWN0aW9uICh3aGVuIHNlcnZlciB1c2VzIHNzbDovLy4uLilcbiAgICAgICAgIyBidXQgdGhlIGNlcnRpZmljYXRlIHVzZWQgYnkgdGhlIHNlcnZlciBpcyBub3QgdHJ1c3RlZCBieSBhbnkgQ0EgY2VydGlmaWNhdGVcbiAgICAgICAgIyBvbiB0aGUgc2VydmVyIChlLmcuIHdoZW4gc2VsZiBnZW5lcmF0ZWQpLlxuICAgICAgICBjYV9jZXJ0PVwiXCJcblxuICAgICAgICAjIFRMUyBjZXJ0aWZpY2F0ZSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgdGxzX2NlcnQ9XCJcIlxuXG4gICAgICAgICMgVExTIGtleSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgdGxzX2tleT1cIlwiXG5cblxuICAgICMgR2F0ZXdheSBjaGFubmVsIGNvbmZpZ3VyYXRpb24uXG4gICAgI1xuICAgICMgTm90ZTogdGhpcyBjb25maWd1cmF0aW9uIGlzIG9ubHkgdXNlZCBpbiBjYXNlIHRoZSBnYXRld2F5IGlzIHVzaW5nIHRoZVxuICAgICMgQ2hpcnBTdGFjayBDb25jZW50cmF0b3JkIGRhZW1vbi4gSW4gYW55IG90aGVyIGNhc2UsIHRoaXMgY29uZmlndXJhdGlvbiBcbiAgICAjIGlzIGlnbm9yZWQuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkwMzkwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkwNDEwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkwNDMwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkwNDUwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkwNDcwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkwNDkwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkwNTEwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkwNTMwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkwNDYwMDAwMFxuICAgICAgYmFuZHdpZHRoPTUwMDAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzhdXG5cblxuICAjIFJlZ2lvbiBzcGVjaWZpYyBuZXR3b3JrIGNvbmZpZ3VyYXRpb24uXG4gIFtyZWdpb25zLm5ldHdvcmtdXG4gICAgXG4gICAgIyBJbnN0YWxsYXRpb24gbWFyZ2luIChkQikgdXNlZCBieSB0aGUgQURSIGVuZ2luZS5cbiAgICAjXG4gICAgIyBBIGhpZ2hlciBudW1iZXIgbWVhbnMgdGhhdCB0aGUgbmV0d29yay1zZXJ2ZXIgd2lsbCBrZWVwIG1vcmUgbWFyZ2luLFxuICAgICMgcmVzdWx0aW5nIGluIGEgbG93ZXIgZGF0YS1yYXRlIGJ1dCBkZWNyZWFzaW5nIHRoZSBjaGFuY2UgdGhhdCB0aGVcbiAgICAjIGRldmljZSBnZXRzIGRpc2Nvbm5lY3RlZCBiZWNhdXNlIGl0IGlzIHVuYWJsZSB0byByZWFjaCBvbmUgb2YgdGhlXG4gICAgIyBzdXJyb3VuZGVkIGdhdGV3YXlzLlxuICAgIGluc3RhbGxhdGlvbl9tYXJnaW49MTBcblxuICAgICMgUlggd2luZG93IChDbGFzcy1BKS5cbiAgICAjXG4gICAgIyBTZXQgdGhpcyB0bzpcbiAgICAjIDA6IFJYMSAvIFJYMlxuICAgICMgMTogUlgxIG9ubHlcbiAgICAjIDI6IFJYMiBvbmx5XG4gICAgcnhfd2luZG93PTBcblxuICAgICMgUlgxIGRlbGF5ICgxIC0gMTUgc2Vjb25kcykuXG4gICAgcngxX2RlbGF5PTFcblxuICAgICMgUlgxIGRhdGEtcmF0ZSBvZmZzZXRcbiAgICByeDFfZHJfb2Zmc2V0PTBcblxuICAgICMgUlgyIGRhdGEtcmF0ZVxuICAgIHJ4Ml9kcj04XG5cbiAgICAjIFJYMiBmcmVxdWVuY3kgKEh6KVxuICAgIHJ4Ml9mcmVxdWVuY3k9OTIzMzAwMDAwXG5cbiAgICAjIFByZWZlciBSWDIgb24gUlgxIGRhdGEtcmF0ZSBsZXNzIHRoYW4uXG4gICAgI1xuICAgICMgUHJlZmVyIFJYMiBvdmVyIFJYMSBiYXNlZCBvbiB0aGUgUlgxIGRhdGEtcmF0ZS4gV2hlbiB0aGUgUlgxIGRhdGEtcmF0ZVxuICAgICMgaXMgc21hbGxlciB0aGFuIHRoZSBjb25maWd1cmVkIHZhbHVlLCB0aGVuIHRoZSBOZXR3b3JrIFNlcnZlciB3aWxsXG4gICAgIyBmaXJzdCB0cnkgdG8gc2NoZWR1bGUgdGhlIGRvd25saW5rIGZvciBSWDIsIGZhaWxpbmcgdGhhdCAoZS5nLiB0aGUgZ2F0ZXdheVxuICAgICMgaGFzIGFscmVhZHkgYSBwYXlsb2FkIHNjaGVkdWxlZCBhdCB0aGUgUlgyIHRpbWluZykgaXQgd2lsbCB0cnkgUlgxLlxuICAgIHJ4Ml9wcmVmZXJfb25fcngxX2RyX2x0PTBcblxuICAgICMgUHJlZmVyIFJYMiBvbiBsaW5rIGJ1ZGdldC5cbiAgICAjXG4gICAgIyBXaGVuIHRoZSBsaW5rLWJ1ZGdldCBpcyBiZXR0ZXIgZm9yIFJYMiB0aGFuIGZvciBSWDEsIHRoZSBOZXR3b3JrIFNlcnZlciB3aWxsIGZpcnN0XG4gICAgIyB0cnkgdG8gc2NoZWR1bGUgdGhlIGRvd25saW5rIGluIFJYMiwgZmFpbGluZyB0aGF0IGl0IHdpbGwgdHJ5IFJYMS5cbiAgICByeDJfcHJlZmVyX29uX2xpbmtfYnVkZ2V0PWZhbHNlXG5cbiAgICAjIERvd25saW5rIFRYIFBvd2VyIChkQm0pXG4gICAgI1xuICAgICMgV2hlbiBzZXQgdG8gLTEsIHRoZSBkb3dubGluayBUWCBQb3dlciBmcm9tIHRoZSBjb25maWd1cmVkIGJhbmQgd2lsbFxuICAgICMgYmUgdXNlZC5cbiAgICAjXG4gICAgIyBQbGVhc2UgY29uc3VsdCB0aGUgTG9SYVdBTiBSZWdpb25hbCBQYXJhbWV0ZXJzIGFuZCBsb2NhbCByZWd1bGF0aW9uc1xuICAgICMgZm9yIHZhbGlkIGFuZCBsZWdhbCBvcHRpb25zLiBOb3RlIHRoYXQgdGhlIGNvbmZpZ3VyZWQgVFggUG93ZXIgbXVzdCBiZVxuICAgICMgc3VwcG9ydGVkIGJ5IHlvdXIgZ2F0ZXdheShzKS5cbiAgICBkb3dubGlua190eF9wb3dlcj0tMVxuXG4gICAgIyBBRFIgaXMgZGlzYWJsZWQuXG4gICAgYWRyX2Rpc2FibGVkPWZhbHNlXG5cbiAgICAjIE1pbmltdW0gZGF0YS1yYXRlLlxuICAgIG1pbl9kcj0wXG5cbiAgICAjIE1heGltdW0gZGF0YS1yYXRlLlxuICAgIG1heF9kcj0zXG5cbiAgICAjIEVuYWJsZWQgdXBsaW5rIGNoYW5uZWxzLlxuICAgICNcbiAgICAjIFVzZSB0aGlzIHdoZW4gb255IGEgc3ViLXNldCBvZiB0aGUgYnkgZGVmYXVsdCBlbmFibGVkIGNoYW5uZWxzIGFyZSBiZWluZ1xuICAgICMgdXNlZC4gRm9yIGV4YW1wbGUgd2hlbiBvbmx5IHVzaW5nIHRoZSBmaXJzdCA4IGNoYW5uZWxzIG9mIHRoZSBVUyBiYW5kLlxuICAgICMgTm90ZTogd2hlbiBsZWZ0IGJsYW5rIC8gZW1wdHkgYXJyYXksIGFsbCBjaGFubmVscyB3aWxsIGJlIGVuYWJsZWQuXG4gICAgZW5hYmxlZF91cGxpbmtfY2hhbm5lbHM9WzgsIDksIDEwLCAxMSwgMTIsIDEzLCAxNCwgMTUsIDY1XVxuXG5cbiAgICAjIFJlam9pbi1yZXF1ZXN0IGNvbmZpZ3VyYXRpb24gKExvUmFXQU4gMS4xKVxuICAgIFtyZWdpb25zLm5ldHdvcmsucmVqb2luX3JlcXVlc3RdXG5cbiAgICAgICMgUmVxdWVzdCBkZXZpY2VzIHRvIHBlcmlvZGljYWxseSBzZW5kIHJlam9pbi1yZXF1ZXN0cy5cbiAgICAgIGVuYWJsZWQ9ZmFsc2VcblxuICAgICAgIyBUaGUgZGV2aWNlIG11c3Qgc2VuZCBhIHJlam9pbi1yZXF1ZXN0IHR5cGUgMCBhdCBsZWFzdCBldmVyeSAyXihtYXhfY291bnRfbiArIDQpXG4gICAgICAjIHVwbGluayBtZXNzYWdlcy4gVmFsaWQgdmFsdWVzIGFyZSAwIHRvIDE1LlxuICAgICAgbWF4X2NvdW50X249MFxuXG4gICAgICAjIFRoZSBkZXZpY2UgbXVzdCBzZW5kIGEgcmVqb2luLXJlcXVlc3QgdHlwZSAwIGF0IGxlYXN0IGV2ZXJ5IDJeKG1heF90aW1lX24gKyAxMClcbiAgICAgICMgc2Vjb25kcy4gVmFsaWQgdmFsdWVzIGFyZSAwIHRvIDE1LlxuICAgICAgI1xuICAgICAgIyAwICA9IHJvdWdobHkgMTcgbWludXRlc1xuICAgICAgIyAxNSA9IGFib3V0IDEgeWVhclxuICAgICAgbWF4X3RpbWVfbj0wXG4gICAgXG5cbiAgICAjIENsYXNzLUIgY29uZmlndXJhdGlvbi5cbiAgICBbcmVnaW9ucy5uZXR3b3JrLmNsYXNzX2JdXG5cbiAgICAgICMgUGluZy1zbG90IGRhdGEtcmF0ZS4gXG4gICAgICBwaW5nX3Nsb3RfZHI9OFxuXG4gICAgICAjIFBpbmctc2xvdCBmcmVxdWVuY3kgKEh6KVxuICAgICAgI1xuICAgICAgIyBzZXQgdGhpcyB0byAwIHRvIHVzZSB0aGUgZGVmYXVsdCBmcmVxdWVuY3kgcGxhbiBmb3IgdGhlIGNvbmZpZ3VyZWQgcmVnaW9uXG4gICAgICAjICh3aGljaCBjb3VsZCBiZSBmcmVxdWVuY3kgaG9wcGluZykuXG4gICAgICBwaW5nX3Nsb3RfZnJlcXVlbmN5PTBcblwiXCJcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuc2VydmljZU5hbWUgPSBcImNoaXJwc3RhY2tcIlxuZmlsZVBhdGggPSBcIi9jaGlycHN0YWNrL3JlZ2lvbl91czkxNV8yLnRvbWxcIlxuY29udGVudCA9IFwiXCJcIlxuIyBUaGlzIGZpbGUgY29udGFpbnMgYW4gZXhhbXBsZSBVUzkxNSBleGFtcGxlIChjaGFubmVscyAxNi0yMyArIDY2KS5cbltbcmVnaW9uc11dXG5cbiAgIyBJRCBpcyBhbiB1c2UtZGVmaW5lZCBpZGVudGlmaWVyIGZvciB0aGlzIHJlZ2lvbi5cbiAgaWQ9XCJ1czkxNV8yXCJcblxuICAjIERlc2NyaXB0aW9uIGlzIGEgc2hvcnQgZGVzY3JpcHRpb24gZm9yIHRoaXMgcmVnaW9uLlxuICBkZXNjcmlwdGlvbj1cIlVTOTE1IChjaGFubmVscyAxNi0yMyArIDY2KVwiXG5cbiAgIyBDb21tb24tbmFtZSByZWZlcnMgdG8gdGhlIGNvbW1vbi1uYW1lIG9mIHRoaXMgcmVnaW9uIGFzIGRlZmluZWQgYnlcbiAgIyB0aGUgTG9SYSBBbGxpYW5jZS5cbiAgY29tbW9uX25hbWU9XCJVUzkxNVwiXG5cblxuICAjIEdhdGV3YXkgY29uZmlndXJhdGlvbi5cbiAgW3JlZ2lvbnMuZ2F0ZXdheV1cblxuICAgICMgRm9yY2UgZ2F0ZXdheXMgYXMgcHJpdmF0ZS5cbiAgICAjXG4gICAgIyBJZiBlbmFibGVkLCBnYXRld2F5cyBjYW4gb25seSBiZSB1c2VkIGJ5IGRldmljZXMgdW5kZXIgdGhlIHNhbWUgdGVuYW50LlxuICAgIGZvcmNlX2d3c19wcml2YXRlPWZhbHNlXG5cbiAgICBcbiAgICAjIEdhdGV3YXkgYmFja2VuZCBjb25maWd1cmF0aW9uLlxuICAgIFtyZWdpb25zLmdhdGV3YXkuYmFja2VuZF1cblxuICAgICAgIyBUaGUgZW5hYmxlZCBiYWNrZW5kIHR5cGUuXG4gICAgICBlbmFibGVkPVwibXF0dFwiXG5cbiAgICAgICMgTVFUVCBjb25maWd1cmF0aW9uLlxuICAgICAgW3JlZ2lvbnMuZ2F0ZXdheS5iYWNrZW5kLm1xdHRdXG5cbiAgICAgICAgIyBUb3BpYyBwcmVmaXguXG4gICAgICAgICNcbiAgICAgICAgIyBUaGUgdG9waWMgcHJlZml4IGNhbiBiZSB1c2VkIHRvIGRlZmluZSB0aGUgcmVnaW9uIG9mIHRoZSBnYXRld2F5LlxuICAgICAgICAjIE5vdGUsIHRoZXJlIGlzIG5vIG5lZWQgdG8gYWRkIGEgdHJhaWxpbmcgJy8nIHRvIHRoZSBwcmVmaXguIFRoZSB0cmFpbGluZ1xuICAgICAgICAjICcvJyBpcyBhdXRvbWF0aWNhbGx5IGFkZGVkIHRvIHRoZSBwcmVmaXggaWYgaXQgaXMgY29uZmlndXJlZC5cbiAgICAgICAgdG9waWNfcHJlZml4PVwidXM5MTVfMlwiXG5cbiAgICAgICAgIyBNUVRUIHNlcnZlciAoZS5nLiBzY2hlbWU6Ly9ob3N0OnBvcnQgd2hlcmUgc2NoZW1lIGlzIHRjcCwgc3NsIG9yIHdzKVxuICAgICAgICBzZXJ2ZXI9XCJ0Y3A6Ly9tb3NxdWl0dG86MTg4M1wiXG5cbiAgICAgICAgIyBDb25uZWN0IHdpdGggdGhlIGdpdmVuIHVzZXJuYW1lIChvcHRpb25hbClcbiAgICAgICAgdXNlcm5hbWU9XCJcIlxuXG4gICAgICAgICMgQ29ubmVjdCB3aXRoIHRoZSBnaXZlbiBwYXNzd29yZCAob3B0aW9uYWwpXG4gICAgICAgIHBhc3N3b3JkPVwiXCJcblxuICAgICAgICAjIFF1YWxpdHkgb2Ygc2VydmljZSBsZXZlbFxuICAgICAgICAjXG4gICAgICAgICMgMDogYXQgbW9zdCBvbmNlXG4gICAgICAgICMgMTogYXQgbGVhc3Qgb25jZVxuICAgICAgICAjIDI6IGV4YWN0bHkgb25jZVxuICAgICAgICAjXG4gICAgICAgICMgTm90ZTogYW4gaW5jcmVhc2Ugb2YgdGhpcyB2YWx1ZSB3aWxsIGRlY3JlYXNlIHRoZSBwZXJmb3JtYW5jZS5cbiAgICAgICAgIyBGb3IgbW9yZSBpbmZvcm1hdGlvbjogaHR0cHM6Ly93d3cuaGl2ZW1xLmNvbS9ibG9nL21xdHQtZXNzZW50aWFscy1wYXJ0LTYtbXF0dC1xdWFsaXR5LW9mLXNlcnZpY2UtbGV2ZWxzXG4gICAgICAgIHFvcz0wXG5cbiAgICAgICAgIyBDbGVhbiBzZXNzaW9uXG4gICAgICAgICNcbiAgICAgICAgIyBTZXQgdGhlIFwiY2xlYW4gc2Vzc2lvblwiIGZsYWcgaW4gdGhlIGNvbm5lY3QgbWVzc2FnZSB3aGVuIHRoaXMgY2xpZW50XG4gICAgICAgICMgY29ubmVjdHMgdG8gYW4gTVFUVCBicm9rZXIuIEJ5IHNldHRpbmcgdGhpcyBmbGFnIHlvdSBhcmUgaW5kaWNhdGluZ1xuICAgICAgICAjIHRoYXQgbm8gbWVzc2FnZXMgc2F2ZWQgYnkgdGhlIGJyb2tlciBmb3IgdGhpcyBjbGllbnQgc2hvdWxkIGJlIGRlbGl2ZXJlZC5cbiAgICAgICAgY2xlYW5fc2Vzc2lvbj1mYWxzZVxuXG4gICAgICAgICMgQ2xpZW50IElEXG4gICAgICAgICNcbiAgICAgICAgIyBTZXQgdGhlIGNsaWVudCBpZCB0byBiZSB1c2VkIGJ5IHRoaXMgY2xpZW50IHdoZW4gY29ubmVjdGluZyB0byB0aGUgTVFUVFxuICAgICAgICAjIGJyb2tlci4gQSBjbGllbnQgaWQgbXVzdCBiZSBubyBsb25nZXIgdGhhbiAyMyBjaGFyYWN0ZXJzLiBJZiBsZWZ0IGJsYW5rLFxuICAgICAgICAjIGEgcmFuZG9tIGlkIHdpbGwgYmUgZ2VuZXJhdGVkIGJ5IENoaXJwU3RhY2suXG4gICAgICAgIGNsaWVudF9pZD1cIlwiXG5cbiAgICAgICAgIyBLZWVwIGFsaXZlIGludGVydmFsLlxuICAgICAgICAjXG4gICAgICAgICMgVGhpcyBkZWZpbmVzIHRoZSBtYXhpbXVtIHRpbWUgdGhhdCB0aGF0IHNob3VsZCBwYXNzIHdpdGhvdXQgY29tbXVuaWNhdGlvblxuICAgICAgICAjIGJldHdlZW4gdGhlIGNsaWVudCBhbmQgc2VydmVyLlxuICAgICAgICBrZWVwX2FsaXZlX2ludGVydmFsPVwiMzBzXCJcblxuICAgICAgICAjIENBIGNlcnRpZmljYXRlIGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICAjXG4gICAgICAgICMgVXNlIHRoaXMgd2hlbiBzZXR0aW5nIHVwIGEgc2VjdXJlIGNvbm5lY3Rpb24gKHdoZW4gc2VydmVyIHVzZXMgc3NsOi8vLi4uKVxuICAgICAgICAjIGJ1dCB0aGUgY2VydGlmaWNhdGUgdXNlZCBieSB0aGUgc2VydmVyIGlzIG5vdCB0cnVzdGVkIGJ5IGFueSBDQSBjZXJ0aWZpY2F0ZVxuICAgICAgICAjIG9uIHRoZSBzZXJ2ZXIgKGUuZy4gd2hlbiBzZWxmIGdlbmVyYXRlZCkuXG4gICAgICAgIGNhX2NlcnQ9XCJcIlxuXG4gICAgICAgICMgVExTIGNlcnRpZmljYXRlIGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICB0bHNfY2VydD1cIlwiXG5cbiAgICAgICAgIyBUTFMga2V5IGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICB0bHNfa2V5PVwiXCJcblxuXG4gICAgIyBHYXRld2F5IGNoYW5uZWwgY29uZmlndXJhdGlvbi5cbiAgICAjXG4gICAgIyBOb3RlOiB0aGlzIGNvbmZpZ3VyYXRpb24gaXMgb25seSB1c2VkIGluIGNhc2UgdGhlIGdhdGV3YXkgaXMgdXNpbmcgdGhlXG4gICAgIyBDaGlycFN0YWNrIENvbmNlbnRyYXRvcmQgZGFlbW9uLiBJbiBhbnkgb3RoZXIgY2FzZSwgdGhpcyBjb25maWd1cmF0aW9uIFxuICAgICMgaXMgaWdub3JlZC5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTA1NTAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTBdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTA1NzAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTBdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTA1OTAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTBdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTA2MTAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTBdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTA2MzAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTBdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTA2NTAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTBdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTA2NzAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTBdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTA2OTAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTBdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTA2MjAwMDAwXG4gICAgICBiYW5kd2lkdGg9NTAwMDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bOF1cblxuXG4gICMgUmVnaW9uIHNwZWNpZmljIG5ldHdvcmsgY29uZmlndXJhdGlvbi5cbiAgW3JlZ2lvbnMubmV0d29ya11cbiAgICBcbiAgICAjIEluc3RhbGxhdGlvbiBtYXJnaW4gKGRCKSB1c2VkIGJ5IHRoZSBBRFIgZW5naW5lLlxuICAgICNcbiAgICAjIEEgaGlnaGVyIG51bWJlciBtZWFucyB0aGF0IHRoZSBuZXR3b3JrLXNlcnZlciB3aWxsIGtlZXAgbW9yZSBtYXJnaW4sXG4gICAgIyByZXN1bHRpbmcgaW4gYSBsb3dlciBkYXRhLXJhdGUgYnV0IGRlY3JlYXNpbmcgdGhlIGNoYW5jZSB0aGF0IHRoZVxuICAgICMgZGV2aWNlIGdldHMgZGlzY29ubmVjdGVkIGJlY2F1c2UgaXQgaXMgdW5hYmxlIHRvIHJlYWNoIG9uZSBvZiB0aGVcbiAgICAjIHN1cnJvdW5kZWQgZ2F0ZXdheXMuXG4gICAgaW5zdGFsbGF0aW9uX21hcmdpbj0xMFxuXG4gICAgIyBSWCB3aW5kb3cgKENsYXNzLUEpLlxuICAgICNcbiAgICAjIFNldCB0aGlzIHRvOlxuICAgICMgMDogUlgxIC8gUlgyXG4gICAgIyAxOiBSWDEgb25seVxuICAgICMgMjogUlgyIG9ubHlcbiAgICByeF93aW5kb3c9MFxuXG4gICAgIyBSWDEgZGVsYXkgKDEgLSAxNSBzZWNvbmRzKS5cbiAgICByeDFfZGVsYXk9MVxuXG4gICAgIyBSWDEgZGF0YS1yYXRlIG9mZnNldFxuICAgIHJ4MV9kcl9vZmZzZXQ9MFxuXG4gICAgIyBSWDIgZGF0YS1yYXRlXG4gICAgcngyX2RyPThcblxuICAgICMgUlgyIGZyZXF1ZW5jeSAoSHopXG4gICAgcngyX2ZyZXF1ZW5jeT05MjMzMDAwMDBcblxuICAgICMgUHJlZmVyIFJYMiBvbiBSWDEgZGF0YS1yYXRlIGxlc3MgdGhhbi5cbiAgICAjXG4gICAgIyBQcmVmZXIgUlgyIG92ZXIgUlgxIGJhc2VkIG9uIHRoZSBSWDEgZGF0YS1yYXRlLiBXaGVuIHRoZSBSWDEgZGF0YS1yYXRlXG4gICAgIyBpcyBzbWFsbGVyIHRoYW4gdGhlIGNvbmZpZ3VyZWQgdmFsdWUsIHRoZW4gdGhlIE5ldHdvcmsgU2VydmVyIHdpbGxcbiAgICAjIGZpcnN0IHRyeSB0byBzY2hlZHVsZSB0aGUgZG93bmxpbmsgZm9yIFJYMiwgZmFpbGluZyB0aGF0IChlLmcuIHRoZSBnYXRld2F5XG4gICAgIyBoYXMgYWxyZWFkeSBhIHBheWxvYWQgc2NoZWR1bGVkIGF0IHRoZSBSWDIgdGltaW5nKSBpdCB3aWxsIHRyeSBSWDEuXG4gICAgcngyX3ByZWZlcl9vbl9yeDFfZHJfbHQ9MFxuXG4gICAgIyBQcmVmZXIgUlgyIG9uIGxpbmsgYnVkZ2V0LlxuICAgICNcbiAgICAjIFdoZW4gdGhlIGxpbmstYnVkZ2V0IGlzIGJldHRlciBmb3IgUlgyIHRoYW4gZm9yIFJYMSwgdGhlIE5ldHdvcmsgU2VydmVyIHdpbGwgZmlyc3RcbiAgICAjIHRyeSB0byBzY2hlZHVsZSB0aGUgZG93bmxpbmsgaW4gUlgyLCBmYWlsaW5nIHRoYXQgaXQgd2lsbCB0cnkgUlgxLlxuICAgIHJ4Ml9wcmVmZXJfb25fbGlua19idWRnZXQ9ZmFsc2VcblxuICAgICMgRG93bmxpbmsgVFggUG93ZXIgKGRCbSlcbiAgICAjXG4gICAgIyBXaGVuIHNldCB0byAtMSwgdGhlIGRvd25saW5rIFRYIFBvd2VyIGZyb20gdGhlIGNvbmZpZ3VyZWQgYmFuZCB3aWxsXG4gICAgIyBiZSB1c2VkLlxuICAgICNcbiAgICAjIFBsZWFzZSBjb25zdWx0IHRoZSBMb1JhV0FOIFJlZ2lvbmFsIFBhcmFtZXRlcnMgYW5kIGxvY2FsIHJlZ3VsYXRpb25zXG4gICAgIyBmb3IgdmFsaWQgYW5kIGxlZ2FsIG9wdGlvbnMuIE5vdGUgdGhhdCB0aGUgY29uZmlndXJlZCBUWCBQb3dlciBtdXN0IGJlXG4gICAgIyBzdXBwb3J0ZWQgYnkgeW91ciBnYXRld2F5KHMpLlxuICAgIGRvd25saW5rX3R4X3Bvd2VyPS0xXG5cbiAgICAjIEFEUiBpcyBkaXNhYmxlZC5cbiAgICBhZHJfZGlzYWJsZWQ9ZmFsc2VcblxuICAgICMgTWluaW11bSBkYXRhLXJhdGUuXG4gICAgbWluX2RyPTBcblxuICAgICMgTWF4aW11bSBkYXRhLXJhdGUuXG4gICAgbWF4X2RyPTNcblxuICAgICMgRW5hYmxlZCB1cGxpbmsgY2hhbm5lbHMuXG4gICAgI1xuICAgICMgVXNlIHRoaXMgd2hlbiBvbnkgYSBzdWItc2V0IG9mIHRoZSBieSBkZWZhdWx0IGVuYWJsZWQgY2hhbm5lbHMgYXJlIGJlaW5nXG4gICAgIyB1c2VkLiBGb3IgZXhhbXBsZSB3aGVuIG9ubHkgdXNpbmcgdGhlIGZpcnN0IDggY2hhbm5lbHMgb2YgdGhlIFVTIGJhbmQuXG4gICAgIyBOb3RlOiB3aGVuIGxlZnQgYmxhbmsgLyBlbXB0eSBhcnJheSwgYWxsIGNoYW5uZWxzIHdpbGwgYmUgZW5hYmxlZC5cbiAgICBlbmFibGVkX3VwbGlua19jaGFubmVscz1bMTYsIDE3LCAxOCwgMTksIDIwLCAyMSwgMjIsIDIzLCA2Nl1cblxuXG4gICAgIyBSZWpvaW4tcmVxdWVzdCBjb25maWd1cmF0aW9uIChMb1JhV0FOIDEuMSlcbiAgICBbcmVnaW9ucy5uZXR3b3JrLnJlam9pbl9yZXF1ZXN0XVxuXG4gICAgICAjIFJlcXVlc3QgZGV2aWNlcyB0byBwZXJpb2RpY2FsbHkgc2VuZCByZWpvaW4tcmVxdWVzdHMuXG4gICAgICBlbmFibGVkPWZhbHNlXG5cbiAgICAgICMgVGhlIGRldmljZSBtdXN0IHNlbmQgYSByZWpvaW4tcmVxdWVzdCB0eXBlIDAgYXQgbGVhc3QgZXZlcnkgMl4obWF4X2NvdW50X24gKyA0KVxuICAgICAgIyB1cGxpbmsgbWVzc2FnZXMuIFZhbGlkIHZhbHVlcyBhcmUgMCB0byAxNS5cbiAgICAgIG1heF9jb3VudF9uPTBcblxuICAgICAgIyBUaGUgZGV2aWNlIG11c3Qgc2VuZCBhIHJlam9pbi1yZXF1ZXN0IHR5cGUgMCBhdCBsZWFzdCBldmVyeSAyXihtYXhfdGltZV9uICsgMTApXG4gICAgICAjIHNlY29uZHMuIFZhbGlkIHZhbHVlcyBhcmUgMCB0byAxNS5cbiAgICAgICNcbiAgICAgICMgMCAgPSByb3VnaGx5IDE3IG1pbnV0ZXNcbiAgICAgICMgMTUgPSBhYm91dCAxIHllYXJcbiAgICAgIG1heF90aW1lX249MFxuICAgIFxuXG4gICAgIyBDbGFzcy1CIGNvbmZpZ3VyYXRpb24uXG4gICAgW3JlZ2lvbnMubmV0d29yay5jbGFzc19iXVxuXG4gICAgICAjIFBpbmctc2xvdCBkYXRhLXJhdGUuIFxuICAgICAgcGluZ19zbG90X2RyPThcblxuICAgICAgIyBQaW5nLXNsb3QgZnJlcXVlbmN5IChIeilcbiAgICAgICNcbiAgICAgICMgc2V0IHRoaXMgdG8gMCB0byB1c2UgdGhlIGRlZmF1bHQgZnJlcXVlbmN5IHBsYW4gZm9yIHRoZSBjb25maWd1cmVkIHJlZ2lvblxuICAgICAgIyAod2hpY2ggY291bGQgYmUgZnJlcXVlbmN5IGhvcHBpbmcpLlxuICAgICAgcGluZ19zbG90X2ZyZXF1ZW5jeT0wXG5cIlwiXCJcblxuW1tjb25maWcubW91bnRzXV1cbnNlcnZpY2VOYW1lID0gXCJjaGlycHN0YWNrXCJcbmZpbGVQYXRoID0gXCIvY2hpcnBzdGFjay9yZWdpb25fdXM5MTVfMy50b21sXCJcbmNvbnRlbnQgPSBcIlwiXCJcbiMgVGhpcyBmaWxlIGNvbnRhaW5zIGFuIGV4YW1wbGUgVVM5MTUgZXhhbXBsZSAoY2hhbm5lbHMgMjQtMzEgKyA2NykuXG5bW3JlZ2lvbnNdXVxuXG4gICMgSUQgaXMgYW4gdXNlLWRlZmluZWQgaWRlbnRpZmllciBmb3IgdGhpcyByZWdpb24uXG4gIGlkPVwidXM5MTVfM1wiXG5cbiAgIyBEZXNjcmlwdGlvbiBpcyBhIHNob3J0IGRlc2NyaXB0aW9uIGZvciB0aGlzIHJlZ2lvbi5cbiAgZGVzY3JpcHRpb249XCJVUzkxNSAoY2hhbm5lbHMgMjQtMzEgKyA2NylcIlxuXG4gICMgQ29tbW9uLW5hbWUgcmVmZXJzIHRvIHRoZSBjb21tb24tbmFtZSBvZiB0aGlzIHJlZ2lvbiBhcyBkZWZpbmVkIGJ5XG4gICMgdGhlIExvUmEgQWxsaWFuY2UuXG4gIGNvbW1vbl9uYW1lPVwiVVM5MTVcIlxuXG5cbiAgIyBHYXRld2F5IGNvbmZpZ3VyYXRpb24uXG4gIFtyZWdpb25zLmdhdGV3YXldXG5cbiAgICAjIEZvcmNlIGdhdGV3YXlzIGFzIHByaXZhdGUuXG4gICAgI1xuICAgICMgSWYgZW5hYmxlZCwgZ2F0ZXdheXMgY2FuIG9ubHkgYmUgdXNlZCBieSBkZXZpY2VzIHVuZGVyIHRoZSBzYW1lIHRlbmFudC5cbiAgICBmb3JjZV9nd3NfcHJpdmF0ZT1mYWxzZVxuXG4gICAgXG4gICAgIyBHYXRld2F5IGJhY2tlbmQgY29uZmlndXJhdGlvbi5cbiAgICBbcmVnaW9ucy5nYXRld2F5LmJhY2tlbmRdXG5cbiAgICAgICMgVGhlIGVuYWJsZWQgYmFja2VuZCB0eXBlLlxuICAgICAgZW5hYmxlZD1cIm1xdHRcIlxuXG4gICAgICAjIE1RVFQgY29uZmlndXJhdGlvbi5cbiAgICAgIFtyZWdpb25zLmdhdGV3YXkuYmFja2VuZC5tcXR0XVxuXG4gICAgICAgICMgVG9waWMgcHJlZml4LlxuICAgICAgICAjXG4gICAgICAgICMgVGhlIHRvcGljIHByZWZpeCBjYW4gYmUgdXNlZCB0byBkZWZpbmUgdGhlIHJlZ2lvbiBvZiB0aGUgZ2F0ZXdheS5cbiAgICAgICAgIyBOb3RlLCB0aGVyZSBpcyBubyBuZWVkIHRvIGFkZCBhIHRyYWlsaW5nICcvJyB0byB0aGUgcHJlZml4LiBUaGUgdHJhaWxpbmdcbiAgICAgICAgIyAnLycgaXMgYXV0b21hdGljYWxseSBhZGRlZCB0byB0aGUgcHJlZml4IGlmIGl0IGlzIGNvbmZpZ3VyZWQuXG4gICAgICAgIHRvcGljX3ByZWZpeD1cInVzOTE1XzNcIlxuXG4gICAgICAgICMgTVFUVCBzZXJ2ZXIgKGUuZy4gc2NoZW1lOi8vaG9zdDpwb3J0IHdoZXJlIHNjaGVtZSBpcyB0Y3AsIHNzbCBvciB3cylcbiAgICAgICAgc2VydmVyPVwidGNwOi8vbW9zcXVpdHRvOjE4ODNcIlxuXG4gICAgICAgICMgQ29ubmVjdCB3aXRoIHRoZSBnaXZlbiB1c2VybmFtZSAob3B0aW9uYWwpXG4gICAgICAgIHVzZXJuYW1lPVwiXCJcblxuICAgICAgICAjIENvbm5lY3Qgd2l0aCB0aGUgZ2l2ZW4gcGFzc3dvcmQgKG9wdGlvbmFsKVxuICAgICAgICBwYXNzd29yZD1cIlwiXG5cbiAgICAgICAgIyBRdWFsaXR5IG9mIHNlcnZpY2UgbGV2ZWxcbiAgICAgICAgI1xuICAgICAgICAjIDA6IGF0IG1vc3Qgb25jZVxuICAgICAgICAjIDE6IGF0IGxlYXN0IG9uY2VcbiAgICAgICAgIyAyOiBleGFjdGx5IG9uY2VcbiAgICAgICAgI1xuICAgICAgICAjIE5vdGU6IGFuIGluY3JlYXNlIG9mIHRoaXMgdmFsdWUgd2lsbCBkZWNyZWFzZSB0aGUgcGVyZm9ybWFuY2UuXG4gICAgICAgICMgRm9yIG1vcmUgaW5mb3JtYXRpb246IGh0dHBzOi8vd3d3LmhpdmVtcS5jb20vYmxvZy9tcXR0LWVzc2VudGlhbHMtcGFydC02LW1xdHQtcXVhbGl0eS1vZi1zZXJ2aWNlLWxldmVsc1xuICAgICAgICBxb3M9MFxuXG4gICAgICAgICMgQ2xlYW4gc2Vzc2lvblxuICAgICAgICAjXG4gICAgICAgICMgU2V0IHRoZSBcImNsZWFuIHNlc3Npb25cIiBmbGFnIGluIHRoZSBjb25uZWN0IG1lc3NhZ2Ugd2hlbiB0aGlzIGNsaWVudFxuICAgICAgICAjIGNvbm5lY3RzIHRvIGFuIE1RVFQgYnJva2VyLiBCeSBzZXR0aW5nIHRoaXMgZmxhZyB5b3UgYXJlIGluZGljYXRpbmdcbiAgICAgICAgIyB0aGF0IG5vIG1lc3NhZ2VzIHNhdmVkIGJ5IHRoZSBicm9rZXIgZm9yIHRoaXMgY2xpZW50IHNob3VsZCBiZSBkZWxpdmVyZWQuXG4gICAgICAgIGNsZWFuX3Nlc3Npb249ZmFsc2VcblxuICAgICAgICAjIENsaWVudCBJRFxuICAgICAgICAjXG4gICAgICAgICMgU2V0IHRoZSBjbGllbnQgaWQgdG8gYmUgdXNlZCBieSB0aGlzIGNsaWVudCB3aGVuIGNvbm5lY3RpbmcgdG8gdGhlIE1RVFRcbiAgICAgICAgIyBicm9rZXIuIEEgY2xpZW50IGlkIG11c3QgYmUgbm8gbG9uZ2VyIHRoYW4gMjMgY2hhcmFjdGVycy4gSWYgbGVmdCBibGFuayxcbiAgICAgICAgIyBhIHJhbmRvbSBpZCB3aWxsIGJlIGdlbmVyYXRlZCBieSBDaGlycFN0YWNrLlxuICAgICAgICBjbGllbnRfaWQ9XCJcIlxuXG4gICAgICAgICMgS2VlcCBhbGl2ZSBpbnRlcnZhbC5cbiAgICAgICAgI1xuICAgICAgICAjIFRoaXMgZGVmaW5lcyB0aGUgbWF4aW11bSB0aW1lIHRoYXQgdGhhdCBzaG91bGQgcGFzcyB3aXRob3V0IGNvbW11bmljYXRpb25cbiAgICAgICAgIyBiZXR3ZWVuIHRoZSBjbGllbnQgYW5kIHNlcnZlci5cbiAgICAgICAga2VlcF9hbGl2ZV9pbnRlcnZhbD1cIjMwc1wiXG5cbiAgICAgICAgIyBDQSBjZXJ0aWZpY2F0ZSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgI1xuICAgICAgICAjIFVzZSB0aGlzIHdoZW4gc2V0dGluZyB1cCBhIHNlY3VyZSBjb25uZWN0aW9uICh3aGVuIHNlcnZlciB1c2VzIHNzbDovLy4uLilcbiAgICAgICAgIyBidXQgdGhlIGNlcnRpZmljYXRlIHVzZWQgYnkgdGhlIHNlcnZlciBpcyBub3QgdHJ1c3RlZCBieSBhbnkgQ0EgY2VydGlmaWNhdGVcbiAgICAgICAgIyBvbiB0aGUgc2VydmVyIChlLmcuIHdoZW4gc2VsZiBnZW5lcmF0ZWQpLlxuICAgICAgICBjYV9jZXJ0PVwiXCJcblxuICAgICAgICAjIFRMUyBjZXJ0aWZpY2F0ZSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgdGxzX2NlcnQ9XCJcIlxuXG4gICAgICAgICMgVExTIGtleSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgdGxzX2tleT1cIlwiXG5cblxuICAgICMgR2F0ZXdheSBjaGFubmVsIGNvbmZpZ3VyYXRpb24uXG4gICAgI1xuICAgICMgTm90ZTogdGhpcyBjb25maWd1cmF0aW9uIGlzIG9ubHkgdXNlZCBpbiBjYXNlIHRoZSBnYXRld2F5IGlzIHVzaW5nIHRoZVxuICAgICMgQ2hpcnBTdGFjayBDb25jZW50cmF0b3JkIGRhZW1vbi4gSW4gYW55IG90aGVyIGNhc2UsIHRoaXMgY29uZmlndXJhdGlvbiBcbiAgICAjIGlzIGlnbm9yZWQuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkwNzEwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkwNzMwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkwNzUwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkwNzcwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkwNzkwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkwODEwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkwODMwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkwODUwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkwNzgwMDAwMFxuICAgICAgYmFuZHdpZHRoPTUwMDAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzhdXG5cblxuICAjIFJlZ2lvbiBzcGVjaWZpYyBuZXR3b3JrIGNvbmZpZ3VyYXRpb24uXG4gIFtyZWdpb25zLm5ldHdvcmtdXG4gICAgXG4gICAgIyBJbnN0YWxsYXRpb24gbWFyZ2luIChkQikgdXNlZCBieSB0aGUgQURSIGVuZ2luZS5cbiAgICAjXG4gICAgIyBBIGhpZ2hlciBudW1iZXIgbWVhbnMgdGhhdCB0aGUgbmV0d29yay1zZXJ2ZXIgd2lsbCBrZWVwIG1vcmUgbWFyZ2luLFxuICAgICMgcmVzdWx0aW5nIGluIGEgbG93ZXIgZGF0YS1yYXRlIGJ1dCBkZWNyZWFzaW5nIHRoZSBjaGFuY2UgdGhhdCB0aGVcbiAgICAjIGRldmljZSBnZXRzIGRpc2Nvbm5lY3RlZCBiZWNhdXNlIGl0IGlzIHVuYWJsZSB0byByZWFjaCBvbmUgb2YgdGhlXG4gICAgIyBzdXJyb3VuZGVkIGdhdGV3YXlzLlxuICAgIGluc3RhbGxhdGlvbl9tYXJnaW49MTBcblxuICAgICMgUlggd2luZG93IChDbGFzcy1BKS5cbiAgICAjXG4gICAgIyBTZXQgdGhpcyB0bzpcbiAgICAjIDA6IFJYMSAvIFJYMlxuICAgICMgMTogUlgxIG9ubHlcbiAgICAjIDI6IFJYMiBvbmx5XG4gICAgcnhfd2luZG93PTBcblxuICAgICMgUlgxIGRlbGF5ICgxIC0gMTUgc2Vjb25kcykuXG4gICAgcngxX2RlbGF5PTFcblxuICAgICMgUlgxIGRhdGEtcmF0ZSBvZmZzZXRcbiAgICByeDFfZHJfb2Zmc2V0PTBcblxuICAgICMgUlgyIGRhdGEtcmF0ZVxuICAgIHJ4Ml9kcj04XG5cbiAgICAjIFJYMiBmcmVxdWVuY3kgKEh6KVxuICAgIHJ4Ml9mcmVxdWVuY3k9OTIzMzAwMDAwXG5cbiAgICAjIFByZWZlciBSWDIgb24gUlgxIGRhdGEtcmF0ZSBsZXNzIHRoYW4uXG4gICAgI1xuICAgICMgUHJlZmVyIFJYMiBvdmVyIFJYMSBiYXNlZCBvbiB0aGUgUlgxIGRhdGEtcmF0ZS4gV2hlbiB0aGUgUlgxIGRhdGEtcmF0ZVxuICAgICMgaXMgc21hbGxlciB0aGFuIHRoZSBjb25maWd1cmVkIHZhbHVlLCB0aGVuIHRoZSBOZXR3b3JrIFNlcnZlciB3aWxsXG4gICAgIyBmaXJzdCB0cnkgdG8gc2NoZWR1bGUgdGhlIGRvd25saW5rIGZvciBSWDIsIGZhaWxpbmcgdGhhdCAoZS5nLiB0aGUgZ2F0ZXdheVxuICAgICMgaGFzIGFscmVhZHkgYSBwYXlsb2FkIHNjaGVkdWxlZCBhdCB0aGUgUlgyIHRpbWluZykgaXQgd2lsbCB0cnkgUlgxLlxuICAgIHJ4Ml9wcmVmZXJfb25fcngxX2RyX2x0PTBcblxuICAgICMgUHJlZmVyIFJYMiBvbiBsaW5rIGJ1ZGdldC5cbiAgICAjXG4gICAgIyBXaGVuIHRoZSBsaW5rLWJ1ZGdldCBpcyBiZXR0ZXIgZm9yIFJYMiB0aGFuIGZvciBSWDEsIHRoZSBOZXR3b3JrIFNlcnZlciB3aWxsIGZpcnN0XG4gICAgIyB0cnkgdG8gc2NoZWR1bGUgdGhlIGRvd25saW5rIGluIFJYMiwgZmFpbGluZyB0aGF0IGl0IHdpbGwgdHJ5IFJYMS5cbiAgICByeDJfcHJlZmVyX29uX2xpbmtfYnVkZ2V0PWZhbHNlXG5cbiAgICAjIERvd25saW5rIFRYIFBvd2VyIChkQm0pXG4gICAgI1xuICAgICMgV2hlbiBzZXQgdG8gLTEsIHRoZSBkb3dubGluayBUWCBQb3dlciBmcm9tIHRoZSBjb25maWd1cmVkIGJhbmQgd2lsbFxuICAgICMgYmUgdXNlZC5cbiAgICAjXG4gICAgIyBQbGVhc2UgY29uc3VsdCB0aGUgTG9SYVdBTiBSZWdpb25hbCBQYXJhbWV0ZXJzIGFuZCBsb2NhbCByZWd1bGF0aW9uc1xuICAgICMgZm9yIHZhbGlkIGFuZCBsZWdhbCBvcHRpb25zLiBOb3RlIHRoYXQgdGhlIGNvbmZpZ3VyZWQgVFggUG93ZXIgbXVzdCBiZVxuICAgICMgc3VwcG9ydGVkIGJ5IHlvdXIgZ2F0ZXdheShzKS5cbiAgICBkb3dubGlua190eF9wb3dlcj0tMVxuXG4gICAgIyBBRFIgaXMgZGlzYWJsZWQuXG4gICAgYWRyX2Rpc2FibGVkPWZhbHNlXG5cbiAgICAjIE1pbmltdW0gZGF0YS1yYXRlLlxuICAgIG1pbl9kcj0wXG5cbiAgICAjIE1heGltdW0gZGF0YS1yYXRlLlxuICAgIG1heF9kcj0zXG5cbiAgICAjIEVuYWJsZWQgdXBsaW5rIGNoYW5uZWxzLlxuICAgICNcbiAgICAjIFVzZSB0aGlzIHdoZW4gb255IGEgc3ViLXNldCBvZiB0aGUgYnkgZGVmYXVsdCBlbmFibGVkIGNoYW5uZWxzIGFyZSBiZWluZ1xuICAgICMgdXNlZC4gRm9yIGV4YW1wbGUgd2hlbiBvbmx5IHVzaW5nIHRoZSBmaXJzdCA4IGNoYW5uZWxzIG9mIHRoZSBVUyBiYW5kLlxuICAgICMgTm90ZTogd2hlbiBsZWZ0IGJsYW5rIC8gZW1wdHkgYXJyYXksIGFsbCBjaGFubmVscyB3aWxsIGJlIGVuYWJsZWQuXG4gICAgZW5hYmxlZF91cGxpbmtfY2hhbm5lbHM9WzI0LCAyNSwgMjYsIDI3LCAyOCwgMjksIDMwLCAzMSwgNjddXG5cblxuICAgICMgUmVqb2luLXJlcXVlc3QgY29uZmlndXJhdGlvbiAoTG9SYVdBTiAxLjEpXG4gICAgW3JlZ2lvbnMubmV0d29yay5yZWpvaW5fcmVxdWVzdF1cblxuICAgICAgIyBSZXF1ZXN0IGRldmljZXMgdG8gcGVyaW9kaWNhbGx5IHNlbmQgcmVqb2luLXJlcXVlc3RzLlxuICAgICAgZW5hYmxlZD1mYWxzZVxuXG4gICAgICAjIFRoZSBkZXZpY2UgbXVzdCBzZW5kIGEgcmVqb2luLXJlcXVlc3QgdHlwZSAwIGF0IGxlYXN0IGV2ZXJ5IDJeKG1heF9jb3VudF9uICsgNClcbiAgICAgICMgdXBsaW5rIG1lc3NhZ2VzLiBWYWxpZCB2YWx1ZXMgYXJlIDAgdG8gMTUuXG4gICAgICBtYXhfY291bnRfbj0wXG5cbiAgICAgICMgVGhlIGRldmljZSBtdXN0IHNlbmQgYSByZWpvaW4tcmVxdWVzdCB0eXBlIDAgYXQgbGVhc3QgZXZlcnkgMl4obWF4X3RpbWVfbiArIDEwKVxuICAgICAgIyBzZWNvbmRzLiBWYWxpZCB2YWx1ZXMgYXJlIDAgdG8gMTUuXG4gICAgICAjXG4gICAgICAjIDAgID0gcm91Z2hseSAxNyBtaW51dGVzXG4gICAgICAjIDE1ID0gYWJvdXQgMSB5ZWFyXG4gICAgICBtYXhfdGltZV9uPTBcbiAgICBcblxuICAgICMgQ2xhc3MtQiBjb25maWd1cmF0aW9uLlxuICAgIFtyZWdpb25zLm5ldHdvcmsuY2xhc3NfYl1cblxuICAgICAgIyBQaW5nLXNsb3QgZGF0YS1yYXRlLiBcbiAgICAgIHBpbmdfc2xvdF9kcj04XG5cbiAgICAgICMgUGluZy1zbG90IGZyZXF1ZW5jeSAoSHopXG4gICAgICAjXG4gICAgICAjIHNldCB0aGlzIHRvIDAgdG8gdXNlIHRoZSBkZWZhdWx0IGZyZXF1ZW5jeSBwbGFuIGZvciB0aGUgY29uZmlndXJlZCByZWdpb25cbiAgICAgICMgKHdoaWNoIGNvdWxkIGJlIGZyZXF1ZW5jeSBob3BwaW5nKS5cbiAgICAgIHBpbmdfc2xvdF9mcmVxdWVuY3k9MFxuXCJcIlwiXG5cbltbY29uZmlnLm1vdW50c11dXG5zZXJ2aWNlTmFtZSA9IFwiY2hpcnBzdGFja1wiXG5maWxlUGF0aCA9IFwiL2NoaXJwc3RhY2svcmVnaW9uX3VzOTE1XzQudG9tbFwiXG5jb250ZW50ID0gXCJcIlwiXG4jIFRoaXMgZmlsZSBjb250YWlucyBhbiBleGFtcGxlIFVTOTE1IGV4YW1wbGUgKGNoYW5uZWxzIDMyLTM5ICsgNjgpLlxuW1tyZWdpb25zXV1cblxuICAjIElEIGlzIGFuIHVzZS1kZWZpbmVkIGlkZW50aWZpZXIgZm9yIHRoaXMgcmVnaW9uLlxuICBpZD1cInVzOTE1XzRcIlxuXG4gICMgRGVzY3JpcHRpb24gaXMgYSBzaG9ydCBkZXNjcmlwdGlvbiBmb3IgdGhpcyByZWdpb24uXG4gIGRlc2NyaXB0aW9uPVwiVVM5MTUgKGNoYW5uZWxzIDMyLTM5ICsgNjgpXCJcblxuICAjIENvbW1vbi1uYW1lIHJlZmVycyB0byB0aGUgY29tbW9uLW5hbWUgb2YgdGhpcyByZWdpb24gYXMgZGVmaW5lZCBieVxuICAjIHRoZSBMb1JhIEFsbGlhbmNlLlxuICBjb21tb25fbmFtZT1cIlVTOTE1XCJcblxuXG4gICMgR2F0ZXdheSBjb25maWd1cmF0aW9uLlxuICBbcmVnaW9ucy5nYXRld2F5XVxuXG4gICAgIyBGb3JjZSBnYXRld2F5cyBhcyBwcml2YXRlLlxuICAgICNcbiAgICAjIElmIGVuYWJsZWQsIGdhdGV3YXlzIGNhbiBvbmx5IGJlIHVzZWQgYnkgZGV2aWNlcyB1bmRlciB0aGUgc2FtZSB0ZW5hbnQuXG4gICAgZm9yY2VfZ3dzX3ByaXZhdGU9ZmFsc2VcblxuICAgIFxuICAgICMgR2F0ZXdheSBiYWNrZW5kIGNvbmZpZ3VyYXRpb24uXG4gICAgW3JlZ2lvbnMuZ2F0ZXdheS5iYWNrZW5kXVxuXG4gICAgICAjIFRoZSBlbmFibGVkIGJhY2tlbmQgdHlwZS5cbiAgICAgIGVuYWJsZWQ9XCJtcXR0XCJcblxuICAgICAgIyBNUVRUIGNvbmZpZ3VyYXRpb24uXG4gICAgICBbcmVnaW9ucy5nYXRld2F5LmJhY2tlbmQubXF0dF1cblxuICAgICAgICAjIFRvcGljIHByZWZpeC5cbiAgICAgICAgI1xuICAgICAgICAjIFRoZSB0b3BpYyBwcmVmaXggY2FuIGJlIHVzZWQgdG8gZGVmaW5lIHRoZSByZWdpb24gb2YgdGhlIGdhdGV3YXkuXG4gICAgICAgICMgTm90ZSwgdGhlcmUgaXMgbm8gbmVlZCB0byBhZGQgYSB0cmFpbGluZyAnLycgdG8gdGhlIHByZWZpeC4gVGhlIHRyYWlsaW5nXG4gICAgICAgICMgJy8nIGlzIGF1dG9tYXRpY2FsbHkgYWRkZWQgdG8gdGhlIHByZWZpeCBpZiBpdCBpcyBjb25maWd1cmVkLlxuICAgICAgICB0b3BpY19wcmVmaXg9XCJ1czkxNV80XCJcblxuICAgICAgICAjIE1RVFQgc2VydmVyIChlLmcuIHNjaGVtZTovL2hvc3Q6cG9ydCB3aGVyZSBzY2hlbWUgaXMgdGNwLCBzc2wgb3Igd3MpXG4gICAgICAgIHNlcnZlcj1cInRjcDovL21vc3F1aXR0bzoxODgzXCJcblxuICAgICAgICAjIENvbm5lY3Qgd2l0aCB0aGUgZ2l2ZW4gdXNlcm5hbWUgKG9wdGlvbmFsKVxuICAgICAgICB1c2VybmFtZT1cIlwiXG5cbiAgICAgICAgIyBDb25uZWN0IHdpdGggdGhlIGdpdmVuIHBhc3N3b3JkIChvcHRpb25hbClcbiAgICAgICAgcGFzc3dvcmQ9XCJcIlxuXG4gICAgICAgICMgUXVhbGl0eSBvZiBzZXJ2aWNlIGxldmVsXG4gICAgICAgICNcbiAgICAgICAgIyAwOiBhdCBtb3N0IG9uY2VcbiAgICAgICAgIyAxOiBhdCBsZWFzdCBvbmNlXG4gICAgICAgICMgMjogZXhhY3RseSBvbmNlXG4gICAgICAgICNcbiAgICAgICAgIyBOb3RlOiBhbiBpbmNyZWFzZSBvZiB0aGlzIHZhbHVlIHdpbGwgZGVjcmVhc2UgdGhlIHBlcmZvcm1hbmNlLlxuICAgICAgICAjIEZvciBtb3JlIGluZm9ybWF0aW9uOiBodHRwczovL3d3dy5oaXZlbXEuY29tL2Jsb2cvbXF0dC1lc3NlbnRpYWxzLXBhcnQtNi1tcXR0LXF1YWxpdHktb2Ytc2VydmljZS1sZXZlbHNcbiAgICAgICAgcW9zPTBcblxuICAgICAgICAjIENsZWFuIHNlc3Npb25cbiAgICAgICAgI1xuICAgICAgICAjIFNldCB0aGUgXCJjbGVhbiBzZXNzaW9uXCIgZmxhZyBpbiB0aGUgY29ubmVjdCBtZXNzYWdlIHdoZW4gdGhpcyBjbGllbnRcbiAgICAgICAgIyBjb25uZWN0cyB0byBhbiBNUVRUIGJyb2tlci4gQnkgc2V0dGluZyB0aGlzIGZsYWcgeW91IGFyZSBpbmRpY2F0aW5nXG4gICAgICAgICMgdGhhdCBubyBtZXNzYWdlcyBzYXZlZCBieSB0aGUgYnJva2VyIGZvciB0aGlzIGNsaWVudCBzaG91bGQgYmUgZGVsaXZlcmVkLlxuICAgICAgICBjbGVhbl9zZXNzaW9uPWZhbHNlXG5cbiAgICAgICAgIyBDbGllbnQgSURcbiAgICAgICAgI1xuICAgICAgICAjIFNldCB0aGUgY2xpZW50IGlkIHRvIGJlIHVzZWQgYnkgdGhpcyBjbGllbnQgd2hlbiBjb25uZWN0aW5nIHRvIHRoZSBNUVRUXG4gICAgICAgICMgYnJva2VyLiBBIGNsaWVudCBpZCBtdXN0IGJlIG5vIGxvbmdlciB0aGFuIDIzIGNoYXJhY3RlcnMuIElmIGxlZnQgYmxhbmssXG4gICAgICAgICMgYSByYW5kb20gaWQgd2lsbCBiZSBnZW5lcmF0ZWQgYnkgQ2hpcnBTdGFjay5cbiAgICAgICAgY2xpZW50X2lkPVwiXCJcblxuICAgICAgICAjIEtlZXAgYWxpdmUgaW50ZXJ2YWwuXG4gICAgICAgICNcbiAgICAgICAgIyBUaGlzIGRlZmluZXMgdGhlIG1heGltdW0gdGltZSB0aGF0IHRoYXQgc2hvdWxkIHBhc3Mgd2l0aG91dCBjb21tdW5pY2F0aW9uXG4gICAgICAgICMgYmV0d2VlbiB0aGUgY2xpZW50IGFuZCBzZXJ2ZXIuXG4gICAgICAgIGtlZXBfYWxpdmVfaW50ZXJ2YWw9XCIzMHNcIlxuXG4gICAgICAgICMgQ0EgY2VydGlmaWNhdGUgZmlsZSAob3B0aW9uYWwpXG4gICAgICAgICNcbiAgICAgICAgIyBVc2UgdGhpcyB3aGVuIHNldHRpbmcgdXAgYSBzZWN1cmUgY29ubmVjdGlvbiAod2hlbiBzZXJ2ZXIgdXNlcyBzc2w6Ly8uLi4pXG4gICAgICAgICMgYnV0IHRoZSBjZXJ0aWZpY2F0ZSB1c2VkIGJ5IHRoZSBzZXJ2ZXIgaXMgbm90IHRydXN0ZWQgYnkgYW55IENBIGNlcnRpZmljYXRlXG4gICAgICAgICMgb24gdGhlIHNlcnZlciAoZS5nLiB3aGVuIHNlbGYgZ2VuZXJhdGVkKS5cbiAgICAgICAgY2FfY2VydD1cIlwiXG5cbiAgICAgICAgIyBUTFMgY2VydGlmaWNhdGUgZmlsZSAob3B0aW9uYWwpXG4gICAgICAgIHRsc19jZXJ0PVwiXCJcblxuICAgICAgICAjIFRMUyBrZXkgZmlsZSAob3B0aW9uYWwpXG4gICAgICAgIHRsc19rZXk9XCJcIlxuXG5cbiAgICAjIEdhdGV3YXkgY2hhbm5lbCBjb25maWd1cmF0aW9uLlxuICAgICNcbiAgICAjIE5vdGU6IHRoaXMgY29uZmlndXJhdGlvbiBpcyBvbmx5IHVzZWQgaW4gY2FzZSB0aGUgZ2F0ZXdheSBpcyB1c2luZyB0aGVcbiAgICAjIENoaXJwU3RhY2sgQ29uY2VudHJhdG9yZCBkYWVtb24uIEluIGFueSBvdGhlciBjYXNlLCB0aGlzIGNvbmZpZ3VyYXRpb24gXG4gICAgIyBpcyBpZ25vcmVkLlxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MDg3MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMF1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MDg5MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMF1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MDkxMDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMF1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MDkzMDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMF1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MDk1MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMF1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MDk3MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMF1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MDk5MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMF1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MTAxMDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMF1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MDk0MDAwMDBcbiAgICAgIGJhbmR3aWR0aD01MDAwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs4XVxuXG5cbiAgIyBSZWdpb24gc3BlY2lmaWMgbmV0d29yayBjb25maWd1cmF0aW9uLlxuICBbcmVnaW9ucy5uZXR3b3JrXVxuICAgIFxuICAgICMgSW5zdGFsbGF0aW9uIG1hcmdpbiAoZEIpIHVzZWQgYnkgdGhlIEFEUiBlbmdpbmUuXG4gICAgI1xuICAgICMgQSBoaWdoZXIgbnVtYmVyIG1lYW5zIHRoYXQgdGhlIG5ldHdvcmstc2VydmVyIHdpbGwga2VlcCBtb3JlIG1hcmdpbixcbiAgICAjIHJlc3VsdGluZyBpbiBhIGxvd2VyIGRhdGEtcmF0ZSBidXQgZGVjcmVhc2luZyB0aGUgY2hhbmNlIHRoYXQgdGhlXG4gICAgIyBkZXZpY2UgZ2V0cyBkaXNjb25uZWN0ZWQgYmVjYXVzZSBpdCBpcyB1bmFibGUgdG8gcmVhY2ggb25lIG9mIHRoZVxuICAgICMgc3Vycm91bmRlZCBnYXRld2F5cy5cbiAgICBpbnN0YWxsYXRpb25fbWFyZ2luPTEwXG5cbiAgICAjIFJYIHdpbmRvdyAoQ2xhc3MtQSkuXG4gICAgI1xuICAgICMgU2V0IHRoaXMgdG86XG4gICAgIyAwOiBSWDEgLyBSWDJcbiAgICAjIDE6IFJYMSBvbmx5XG4gICAgIyAyOiBSWDIgb25seVxuICAgIHJ4X3dpbmRvdz0wXG5cbiAgICAjIFJYMSBkZWxheSAoMSAtIDE1IHNlY29uZHMpLlxuICAgIHJ4MV9kZWxheT0xXG5cbiAgICAjIFJYMSBkYXRhLXJhdGUgb2Zmc2V0XG4gICAgcngxX2RyX29mZnNldD0wXG5cbiAgICAjIFJYMiBkYXRhLXJhdGVcbiAgICByeDJfZHI9OFxuXG4gICAgIyBSWDIgZnJlcXVlbmN5IChIeilcbiAgICByeDJfZnJlcXVlbmN5PTkyMzMwMDAwMFxuXG4gICAgIyBQcmVmZXIgUlgyIG9uIFJYMSBkYXRhLXJhdGUgbGVzcyB0aGFuLlxuICAgICNcbiAgICAjIFByZWZlciBSWDIgb3ZlciBSWDEgYmFzZWQgb24gdGhlIFJYMSBkYXRhLXJhdGUuIFdoZW4gdGhlIFJYMSBkYXRhLXJhdGVcbiAgICAjIGlzIHNtYWxsZXIgdGhhbiB0aGUgY29uZmlndXJlZCB2YWx1ZSwgdGhlbiB0aGUgTmV0d29yayBTZXJ2ZXIgd2lsbFxuICAgICMgZmlyc3QgdHJ5IHRvIHNjaGVkdWxlIHRoZSBkb3dubGluayBmb3IgUlgyLCBmYWlsaW5nIHRoYXQgKGUuZy4gdGhlIGdhdGV3YXlcbiAgICAjIGhhcyBhbHJlYWR5IGEgcGF5bG9hZCBzY2hlZHVsZWQgYXQgdGhlIFJYMiB0aW1pbmcpIGl0IHdpbGwgdHJ5IFJYMS5cbiAgICByeDJfcHJlZmVyX29uX3J4MV9kcl9sdD0wXG5cbiAgICAjIFByZWZlciBSWDIgb24gbGluayBidWRnZXQuXG4gICAgI1xuICAgICMgV2hlbiB0aGUgbGluay1idWRnZXQgaXMgYmV0dGVyIGZvciBSWDIgdGhhbiBmb3IgUlgxLCB0aGUgTmV0d29yayBTZXJ2ZXIgd2lsbCBmaXJzdFxuICAgICMgdHJ5IHRvIHNjaGVkdWxlIHRoZSBkb3dubGluayBpbiBSWDIsIGZhaWxpbmcgdGhhdCBpdCB3aWxsIHRyeSBSWDEuXG4gICAgcngyX3ByZWZlcl9vbl9saW5rX2J1ZGdldD1mYWxzZVxuXG4gICAgIyBEb3dubGluayBUWCBQb3dlciAoZEJtKVxuICAgICNcbiAgICAjIFdoZW4gc2V0IHRvIC0xLCB0aGUgZG93bmxpbmsgVFggUG93ZXIgZnJvbSB0aGUgY29uZmlndXJlZCBiYW5kIHdpbGxcbiAgICAjIGJlIHVzZWQuXG4gICAgI1xuICAgICMgUGxlYXNlIGNvbnN1bHQgdGhlIExvUmFXQU4gUmVnaW9uYWwgUGFyYW1ldGVycyBhbmQgbG9jYWwgcmVndWxhdGlvbnNcbiAgICAjIGZvciB2YWxpZCBhbmQgbGVnYWwgb3B0aW9ucy4gTm90ZSB0aGF0IHRoZSBjb25maWd1cmVkIFRYIFBvd2VyIG11c3QgYmVcbiAgICAjIHN1cHBvcnRlZCBieSB5b3VyIGdhdGV3YXkocykuXG4gICAgZG93bmxpbmtfdHhfcG93ZXI9LTFcblxuICAgICMgQURSIGlzIGRpc2FibGVkLlxuICAgIGFkcl9kaXNhYmxlZD1mYWxzZVxuXG4gICAgIyBNaW5pbXVtIGRhdGEtcmF0ZS5cbiAgICBtaW5fZHI9MFxuXG4gICAgIyBNYXhpbXVtIGRhdGEtcmF0ZS5cbiAgICBtYXhfZHI9M1xuXG4gICAgIyBFbmFibGVkIHVwbGluayBjaGFubmVscy5cbiAgICAjXG4gICAgIyBVc2UgdGhpcyB3aGVuIG9ueSBhIHN1Yi1zZXQgb2YgdGhlIGJ5IGRlZmF1bHQgZW5hYmxlZCBjaGFubmVscyBhcmUgYmVpbmdcbiAgICAjIHVzZWQuIEZvciBleGFtcGxlIHdoZW4gb25seSB1c2luZyB0aGUgZmlyc3QgOCBjaGFubmVscyBvZiB0aGUgVVMgYmFuZC5cbiAgICAjIE5vdGU6IHdoZW4gbGVmdCBibGFuayAvIGVtcHR5IGFycmF5LCBhbGwgY2hhbm5lbHMgd2lsbCBiZSBlbmFibGVkLlxuICAgIGVuYWJsZWRfdXBsaW5rX2NoYW5uZWxzPVszMiwgMzMsIDM0LCAzNSwgMzYsIDM3LCAzOCwgMzksIDY4XVxuXG5cbiAgICAjIFJlam9pbi1yZXF1ZXN0IGNvbmZpZ3VyYXRpb24gKExvUmFXQU4gMS4xKVxuICAgIFtyZWdpb25zLm5ldHdvcmsucmVqb2luX3JlcXVlc3RdXG5cbiAgICAgICMgUmVxdWVzdCBkZXZpY2VzIHRvIHBlcmlvZGljYWxseSBzZW5kIHJlam9pbi1yZXF1ZXN0cy5cbiAgICAgIGVuYWJsZWQ9ZmFsc2VcblxuICAgICAgIyBUaGUgZGV2aWNlIG11c3Qgc2VuZCBhIHJlam9pbi1yZXF1ZXN0IHR5cGUgMCBhdCBsZWFzdCBldmVyeSAyXihtYXhfY291bnRfbiArIDQpXG4gICAgICAjIHVwbGluayBtZXNzYWdlcy4gVmFsaWQgdmFsdWVzIGFyZSAwIHRvIDE1LlxuICAgICAgbWF4X2NvdW50X249MFxuXG4gICAgICAjIFRoZSBkZXZpY2UgbXVzdCBzZW5kIGEgcmVqb2luLXJlcXVlc3QgdHlwZSAwIGF0IGxlYXN0IGV2ZXJ5IDJeKG1heF90aW1lX24gKyAxMClcbiAgICAgICMgc2Vjb25kcy4gVmFsaWQgdmFsdWVzIGFyZSAwIHRvIDE1LlxuICAgICAgI1xuICAgICAgIyAwICA9IHJvdWdobHkgMTcgbWludXRlc1xuICAgICAgIyAxNSA9IGFib3V0IDEgeWVhclxuICAgICAgbWF4X3RpbWVfbj0wXG4gICAgXG5cbiAgICAjIENsYXNzLUIgY29uZmlndXJhdGlvbi5cbiAgICBbcmVnaW9ucy5uZXR3b3JrLmNsYXNzX2JdXG5cbiAgICAgICMgUGluZy1zbG90IGRhdGEtcmF0ZS4gXG4gICAgICBwaW5nX3Nsb3RfZHI9OFxuXG4gICAgICAjIFBpbmctc2xvdCBmcmVxdWVuY3kgKEh6KVxuICAgICAgI1xuICAgICAgIyBzZXQgdGhpcyB0byAwIHRvIHVzZSB0aGUgZGVmYXVsdCBmcmVxdWVuY3kgcGxhbiBmb3IgdGhlIGNvbmZpZ3VyZWQgcmVnaW9uXG4gICAgICAjICh3aGljaCBjb3VsZCBiZSBmcmVxdWVuY3kgaG9wcGluZykuXG4gICAgICBwaW5nX3Nsb3RfZnJlcXVlbmN5PTBcblwiXCJcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuc2VydmljZU5hbWUgPSBcImNoaXJwc3RhY2tcIlxuZmlsZVBhdGggPSBcIi9jaGlycHN0YWNrL3JlZ2lvbl91czkxNV81LnRvbWxcIlxuY29udGVudCA9IFwiXCJcIlxuIyBUaGlzIGZpbGUgY29udGFpbnMgYW4gZXhhbXBsZSBVUzkxNSBleGFtcGxlIChjaGFubmVscyA0MC00NyArIDY5KS5cbltbcmVnaW9uc11dXG5cbiAgIyBJRCBpcyBhbiB1c2UtZGVmaW5lZCBpZGVudGlmaWVyIGZvciB0aGlzIHJlZ2lvbi5cbiAgaWQ9XCJ1czkxNV81XCJcblxuICAjIERlc2NyaXB0aW9uIGlzIGEgc2hvcnQgZGVzY3JpcHRpb24gZm9yIHRoaXMgcmVnaW9uLlxuICBkZXNjcmlwdGlvbj1cIlVTOTE1IChjaGFubmVscyA0MC00NyArIDY5KVwiXG5cbiAgIyBDb21tb24tbmFtZSByZWZlcnMgdG8gdGhlIGNvbW1vbi1uYW1lIG9mIHRoaXMgcmVnaW9uIGFzIGRlZmluZWQgYnlcbiAgIyB0aGUgTG9SYSBBbGxpYW5jZS5cbiAgY29tbW9uX25hbWU9XCJVUzkxNVwiXG5cblxuICAjIEdhdGV3YXkgY29uZmlndXJhdGlvbi5cbiAgW3JlZ2lvbnMuZ2F0ZXdheV1cblxuICAgICMgRm9yY2UgZ2F0ZXdheXMgYXMgcHJpdmF0ZS5cbiAgICAjXG4gICAgIyBJZiBlbmFibGVkLCBnYXRld2F5cyBjYW4gb25seSBiZSB1c2VkIGJ5IGRldmljZXMgdW5kZXIgdGhlIHNhbWUgdGVuYW50LlxuICAgIGZvcmNlX2d3c19wcml2YXRlPWZhbHNlXG5cbiAgICBcbiAgICAjIEdhdGV3YXkgYmFja2VuZCBjb25maWd1cmF0aW9uLlxuICAgIFtyZWdpb25zLmdhdGV3YXkuYmFja2VuZF1cblxuICAgICAgIyBUaGUgZW5hYmxlZCBiYWNrZW5kIHR5cGUuXG4gICAgICBlbmFibGVkPVwibXF0dFwiXG5cbiAgICAgICMgTVFUVCBjb25maWd1cmF0aW9uLlxuICAgICAgW3JlZ2lvbnMuZ2F0ZXdheS5iYWNrZW5kLm1xdHRdXG5cbiAgICAgICAgIyBUb3BpYyBwcmVmaXguXG4gICAgICAgICNcbiAgICAgICAgIyBUaGUgdG9waWMgcHJlZml4IGNhbiBiZSB1c2VkIHRvIGRlZmluZSB0aGUgcmVnaW9uIG9mIHRoZSBnYXRld2F5LlxuICAgICAgICAjIE5vdGUsIHRoZXJlIGlzIG5vIG5lZWQgdG8gYWRkIGEgdHJhaWxpbmcgJy8nIHRvIHRoZSBwcmVmaXguIFRoZSB0cmFpbGluZ1xuICAgICAgICAjICcvJyBpcyBhdXRvbWF0aWNhbGx5IGFkZGVkIHRvIHRoZSBwcmVmaXggaWYgaXQgaXMgY29uZmlndXJlZC5cbiAgICAgICAgdG9waWNfcHJlZml4PVwidXM5MTVfNVwiXG5cbiAgICAgICAgIyBNUVRUIHNlcnZlciAoZS5nLiBzY2hlbWU6Ly9ob3N0OnBvcnQgd2hlcmUgc2NoZW1lIGlzIHRjcCwgc3NsIG9yIHdzKVxuICAgICAgICBzZXJ2ZXI9XCJ0Y3A6Ly9tb3NxdWl0dG86MTg4M1wiXG5cbiAgICAgICAgIyBDb25uZWN0IHdpdGggdGhlIGdpdmVuIHVzZXJuYW1lIChvcHRpb25hbClcbiAgICAgICAgdXNlcm5hbWU9XCJcIlxuXG4gICAgICAgICMgQ29ubmVjdCB3aXRoIHRoZSBnaXZlbiBwYXNzd29yZCAob3B0aW9uYWwpXG4gICAgICAgIHBhc3N3b3JkPVwiXCJcblxuICAgICAgICAjIFF1YWxpdHkgb2Ygc2VydmljZSBsZXZlbFxuICAgICAgICAjXG4gICAgICAgICMgMDogYXQgbW9zdCBvbmNlXG4gICAgICAgICMgMTogYXQgbGVhc3Qgb25jZVxuICAgICAgICAjIDI6IGV4YWN0bHkgb25jZVxuICAgICAgICAjXG4gICAgICAgICMgTm90ZTogYW4gaW5jcmVhc2Ugb2YgdGhpcyB2YWx1ZSB3aWxsIGRlY3JlYXNlIHRoZSBwZXJmb3JtYW5jZS5cbiAgICAgICAgIyBGb3IgbW9yZSBpbmZvcm1hdGlvbjogaHR0cHM6Ly93d3cuaGl2ZW1xLmNvbS9ibG9nL21xdHQtZXNzZW50aWFscy1wYXJ0LTYtbXF0dC1xdWFsaXR5LW9mLXNlcnZpY2UtbGV2ZWxzXG4gICAgICAgIHFvcz0wXG5cbiAgICAgICAgIyBDbGVhbiBzZXNzaW9uXG4gICAgICAgICNcbiAgICAgICAgIyBTZXQgdGhlIFwiY2xlYW4gc2Vzc2lvblwiIGZsYWcgaW4gdGhlIGNvbm5lY3QgbWVzc2FnZSB3aGVuIHRoaXMgY2xpZW50XG4gICAgICAgICMgY29ubmVjdHMgdG8gYW4gTVFUVCBicm9rZXIuIEJ5IHNldHRpbmcgdGhpcyBmbGFnIHlvdSBhcmUgaW5kaWNhdGluZ1xuICAgICAgICAjIHRoYXQgbm8gbWVzc2FnZXMgc2F2ZWQgYnkgdGhlIGJyb2tlciBmb3IgdGhpcyBjbGllbnQgc2hvdWxkIGJlIGRlbGl2ZXJlZC5cbiAgICAgICAgY2xlYW5fc2Vzc2lvbj1mYWxzZVxuXG4gICAgICAgICMgQ2xpZW50IElEXG4gICAgICAgICNcbiAgICAgICAgIyBTZXQgdGhlIGNsaWVudCBpZCB0byBiZSB1c2VkIGJ5IHRoaXMgY2xpZW50IHdoZW4gY29ubmVjdGluZyB0byB0aGUgTVFUVFxuICAgICAgICAjIGJyb2tlci4gQSBjbGllbnQgaWQgbXVzdCBiZSBubyBsb25nZXIgdGhhbiAyMyBjaGFyYWN0ZXJzLiBJZiBsZWZ0IGJsYW5rLFxuICAgICAgICAjIGEgcmFuZG9tIGlkIHdpbGwgYmUgZ2VuZXJhdGVkIGJ5IENoaXJwU3RhY2suXG4gICAgICAgIGNsaWVudF9pZD1cIlwiXG5cbiAgICAgICAgIyBLZWVwIGFsaXZlIGludGVydmFsLlxuICAgICAgICAjXG4gICAgICAgICMgVGhpcyBkZWZpbmVzIHRoZSBtYXhpbXVtIHRpbWUgdGhhdCB0aGF0IHNob3VsZCBwYXNzIHdpdGhvdXQgY29tbXVuaWNhdGlvblxuICAgICAgICAjIGJldHdlZW4gdGhlIGNsaWVudCBhbmQgc2VydmVyLlxuICAgICAgICBrZWVwX2FsaXZlX2ludGVydmFsPVwiMzBzXCJcblxuICAgICAgICAjIENBIGNlcnRpZmljYXRlIGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICAjXG4gICAgICAgICMgVXNlIHRoaXMgd2hlbiBzZXR0aW5nIHVwIGEgc2VjdXJlIGNvbm5lY3Rpb24gKHdoZW4gc2VydmVyIHVzZXMgc3NsOi8vLi4uKVxuICAgICAgICAjIGJ1dCB0aGUgY2VydGlmaWNhdGUgdXNlZCBieSB0aGUgc2VydmVyIGlzIG5vdCB0cnVzdGVkIGJ5IGFueSBDQSBjZXJ0aWZpY2F0ZVxuICAgICAgICAjIG9uIHRoZSBzZXJ2ZXIgKGUuZy4gd2hlbiBzZWxmIGdlbmVyYXRlZCkuXG4gICAgICAgIGNhX2NlcnQ9XCJcIlxuXG4gICAgICAgICMgVExTIGNlcnRpZmljYXRlIGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICB0bHNfY2VydD1cIlwiXG5cbiAgICAgICAgIyBUTFMga2V5IGZpbGUgKG9wdGlvbmFsKVxuICAgICAgICB0bHNfa2V5PVwiXCJcblxuXG4gICAgIyBHYXRld2F5IGNoYW5uZWwgY29uZmlndXJhdGlvbi5cbiAgICAjXG4gICAgIyBOb3RlOiB0aGlzIGNvbmZpZ3VyYXRpb24gaXMgb25seSB1c2VkIGluIGNhc2UgdGhlIGdhdGV3YXkgaXMgdXNpbmcgdGhlXG4gICAgIyBDaGlycFN0YWNrIENvbmNlbnRyYXRvcmQgZGFlbW9uLiBJbiBhbnkgb3RoZXIgY2FzZSwgdGhpcyBjb25maWd1cmF0aW9uIFxuICAgICMgaXMgaWdub3JlZC5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTEwMzAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTBdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTEwNTAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTBdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTEwNzAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTBdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTEwOTAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTBdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTExMTAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTBdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTExMzAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTBdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTExNTAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTBdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTExNzAwMDAwXG4gICAgICBiYW5kd2lkdGg9MTI1MDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bNywgOCwgOSwgMTBdXG5cbiAgICBbW3JlZ2lvbnMuZ2F0ZXdheS5jaGFubmVsc11dXG4gICAgICBmcmVxdWVuY3k9OTExMDAwMDAwXG4gICAgICBiYW5kd2lkdGg9NTAwMDAwXG4gICAgICBtb2R1bGF0aW9uPVwiTE9SQVwiXG4gICAgICBzcHJlYWRpbmdfZmFjdG9ycz1bOF1cblxuXG4gICMgUmVnaW9uIHNwZWNpZmljIG5ldHdvcmsgY29uZmlndXJhdGlvbi5cbiAgW3JlZ2lvbnMubmV0d29ya11cbiAgICBcbiAgICAjIEluc3RhbGxhdGlvbiBtYXJnaW4gKGRCKSB1c2VkIGJ5IHRoZSBBRFIgZW5naW5lLlxuICAgICNcbiAgICAjIEEgaGlnaGVyIG51bWJlciBtZWFucyB0aGF0IHRoZSBuZXR3b3JrLXNlcnZlciB3aWxsIGtlZXAgbW9yZSBtYXJnaW4sXG4gICAgIyByZXN1bHRpbmcgaW4gYSBsb3dlciBkYXRhLXJhdGUgYnV0IGRlY3JlYXNpbmcgdGhlIGNoYW5jZSB0aGF0IHRoZVxuICAgICMgZGV2aWNlIGdldHMgZGlzY29ubmVjdGVkIGJlY2F1c2UgaXQgaXMgdW5hYmxlIHRvIHJlYWNoIG9uZSBvZiB0aGVcbiAgICAjIHN1cnJvdW5kZWQgZ2F0ZXdheXMuXG4gICAgaW5zdGFsbGF0aW9uX21hcmdpbj0xMFxuXG4gICAgIyBSWCB3aW5kb3cgKENsYXNzLUEpLlxuICAgICNcbiAgICAjIFNldCB0aGlzIHRvOlxuICAgICMgMDogUlgxIC8gUlgyXG4gICAgIyAxOiBSWDEgb25seVxuICAgICMgMjogUlgyIG9ubHlcbiAgICByeF93aW5kb3c9MFxuXG4gICAgIyBSWDEgZGVsYXkgKDEgLSAxNSBzZWNvbmRzKS5cbiAgICByeDFfZGVsYXk9MVxuXG4gICAgIyBSWDEgZGF0YS1yYXRlIG9mZnNldFxuICAgIHJ4MV9kcl9vZmZzZXQ9MFxuXG4gICAgIyBSWDIgZGF0YS1yYXRlXG4gICAgcngyX2RyPThcblxuICAgICMgUlgyIGZyZXF1ZW5jeSAoSHopXG4gICAgcngyX2ZyZXF1ZW5jeT05MjMzMDAwMDBcblxuICAgICMgUHJlZmVyIFJYMiBvbiBSWDEgZGF0YS1yYXRlIGxlc3MgdGhhbi5cbiAgICAjXG4gICAgIyBQcmVmZXIgUlgyIG92ZXIgUlgxIGJhc2VkIG9uIHRoZSBSWDEgZGF0YS1yYXRlLiBXaGVuIHRoZSBSWDEgZGF0YS1yYXRlXG4gICAgIyBpcyBzbWFsbGVyIHRoYW4gdGhlIGNvbmZpZ3VyZWQgdmFsdWUsIHRoZW4gdGhlIE5ldHdvcmsgU2VydmVyIHdpbGxcbiAgICAjIGZpcnN0IHRyeSB0byBzY2hlZHVsZSB0aGUgZG93bmxpbmsgZm9yIFJYMiwgZmFpbGluZyB0aGF0IChlLmcuIHRoZSBnYXRld2F5XG4gICAgIyBoYXMgYWxyZWFkeSBhIHBheWxvYWQgc2NoZWR1bGVkIGF0IHRoZSBSWDIgdGltaW5nKSBpdCB3aWxsIHRyeSBSWDEuXG4gICAgcngyX3ByZWZlcl9vbl9yeDFfZHJfbHQ9MFxuXG4gICAgIyBQcmVmZXIgUlgyIG9uIGxpbmsgYnVkZ2V0LlxuICAgICNcbiAgICAjIFdoZW4gdGhlIGxpbmstYnVkZ2V0IGlzIGJldHRlciBmb3IgUlgyIHRoYW4gZm9yIFJYMSwgdGhlIE5ldHdvcmsgU2VydmVyIHdpbGwgZmlyc3RcbiAgICAjIHRyeSB0byBzY2hlZHVsZSB0aGUgZG93bmxpbmsgaW4gUlgyLCBmYWlsaW5nIHRoYXQgaXQgd2lsbCB0cnkgUlgxLlxuICAgIHJ4Ml9wcmVmZXJfb25fbGlua19idWRnZXQ9ZmFsc2VcblxuICAgICMgRG93bmxpbmsgVFggUG93ZXIgKGRCbSlcbiAgICAjXG4gICAgIyBXaGVuIHNldCB0byAtMSwgdGhlIGRvd25saW5rIFRYIFBvd2VyIGZyb20gdGhlIGNvbmZpZ3VyZWQgYmFuZCB3aWxsXG4gICAgIyBiZSB1c2VkLlxuICAgICNcbiAgICAjIFBsZWFzZSBjb25zdWx0IHRoZSBMb1JhV0FOIFJlZ2lvbmFsIFBhcmFtZXRlcnMgYW5kIGxvY2FsIHJlZ3VsYXRpb25zXG4gICAgIyBmb3IgdmFsaWQgYW5kIGxlZ2FsIG9wdGlvbnMuIE5vdGUgdGhhdCB0aGUgY29uZmlndXJlZCBUWCBQb3dlciBtdXN0IGJlXG4gICAgIyBzdXBwb3J0ZWQgYnkgeW91ciBnYXRld2F5KHMpLlxuICAgIGRvd25saW5rX3R4X3Bvd2VyPS0xXG5cbiAgICAjIEFEUiBpcyBkaXNhYmxlZC5cbiAgICBhZHJfZGlzYWJsZWQ9ZmFsc2VcblxuICAgICMgTWluaW11bSBkYXRhLXJhdGUuXG4gICAgbWluX2RyPTBcblxuICAgICMgTWF4aW11bSBkYXRhLXJhdGUuXG4gICAgbWF4X2RyPTNcblxuICAgICMgRW5hYmxlZCB1cGxpbmsgY2hhbm5lbHMuXG4gICAgI1xuICAgICMgVXNlIHRoaXMgd2hlbiBvbnkgYSBzdWItc2V0IG9mIHRoZSBieSBkZWZhdWx0IGVuYWJsZWQgY2hhbm5lbHMgYXJlIGJlaW5nXG4gICAgIyB1c2VkLiBGb3IgZXhhbXBsZSB3aGVuIG9ubHkgdXNpbmcgdGhlIGZpcnN0IDggY2hhbm5lbHMgb2YgdGhlIFVTIGJhbmQuXG4gICAgIyBOb3RlOiB3aGVuIGxlZnQgYmxhbmsgLyBlbXB0eSBhcnJheSwgYWxsIGNoYW5uZWxzIHdpbGwgYmUgZW5hYmxlZC5cbiAgICBlbmFibGVkX3VwbGlua19jaGFubmVscz1bNDAsIDQxLCA0MiwgNDMsIDQ0LCA0NSwgNDYsIDQ3LCA2OV1cblxuXG4gICAgIyBSZWpvaW4tcmVxdWVzdCBjb25maWd1cmF0aW9uIChMb1JhV0FOIDEuMSlcbiAgICBbcmVnaW9ucy5uZXR3b3JrLnJlam9pbl9yZXF1ZXN0XVxuXG4gICAgICAjIFJlcXVlc3QgZGV2aWNlcyB0byBwZXJpb2RpY2FsbHkgc2VuZCByZWpvaW4tcmVxdWVzdHMuXG4gICAgICBlbmFibGVkPWZhbHNlXG5cbiAgICAgICMgVGhlIGRldmljZSBtdXN0IHNlbmQgYSByZWpvaW4tcmVxdWVzdCB0eXBlIDAgYXQgbGVhc3QgZXZlcnkgMl4obWF4X2NvdW50X24gKyA0KVxuICAgICAgIyB1cGxpbmsgbWVzc2FnZXMuIFZhbGlkIHZhbHVlcyBhcmUgMCB0byAxNS5cbiAgICAgIG1heF9jb3VudF9uPTBcblxuICAgICAgIyBUaGUgZGV2aWNlIG11c3Qgc2VuZCBhIHJlam9pbi1yZXF1ZXN0IHR5cGUgMCBhdCBsZWFzdCBldmVyeSAyXihtYXhfdGltZV9uICsgMTApXG4gICAgICAjIHNlY29uZHMuIFZhbGlkIHZhbHVlcyBhcmUgMCB0byAxNS5cbiAgICAgICNcbiAgICAgICMgMCAgPSByb3VnaGx5IDE3IG1pbnV0ZXNcbiAgICAgICMgMTUgPSBhYm91dCAxIHllYXJcbiAgICAgIG1heF90aW1lX249MFxuICAgIFxuXG4gICAgIyBDbGFzcy1CIGNvbmZpZ3VyYXRpb24uXG4gICAgW3JlZ2lvbnMubmV0d29yay5jbGFzc19iXVxuXG4gICAgICAjIFBpbmctc2xvdCBkYXRhLXJhdGUuIFxuICAgICAgcGluZ19zbG90X2RyPThcblxuICAgICAgIyBQaW5nLXNsb3QgZnJlcXVlbmN5IChIeilcbiAgICAgICNcbiAgICAgICMgc2V0IHRoaXMgdG8gMCB0byB1c2UgdGhlIGRlZmF1bHQgZnJlcXVlbmN5IHBsYW4gZm9yIHRoZSBjb25maWd1cmVkIHJlZ2lvblxuICAgICAgIyAod2hpY2ggY291bGQgYmUgZnJlcXVlbmN5IGhvcHBpbmcpLlxuICAgICAgcGluZ19zbG90X2ZyZXF1ZW5jeT0wXG5cIlwiXCJcblxuW1tjb25maWcubW91bnRzXV1cbnNlcnZpY2VOYW1lID0gXCJjaGlycHN0YWNrXCJcbmZpbGVQYXRoID0gXCIvY2hpcnBzdGFjay9yZWdpb25fdXM5MTVfNi50b21sXCJcbmNvbnRlbnQgPSBcIlwiXCJcbiMgVGhpcyBmaWxlIGNvbnRhaW5zIGFuIGV4YW1wbGUgVVM5MTUgZXhhbXBsZSAoY2hhbm5lbHMgNDgtNTUgKyA3MCkuXG5bW3JlZ2lvbnNdXVxuXG4gICMgSUQgaXMgYW4gdXNlLWRlZmluZWQgaWRlbnRpZmllciBmb3IgdGhpcyByZWdpb24uXG4gIGlkPVwidXM5MTVfNlwiXG5cbiAgIyBEZXNjcmlwdGlvbiBpcyBhIHNob3J0IGRlc2NyaXB0aW9uIGZvciB0aGlzIHJlZ2lvbi5cbiAgZGVzY3JpcHRpb249XCJVUzkxNSAoY2hhbm5lbHMgNDgtNTUgKyA3MClcIlxuXG4gICMgQ29tbW9uLW5hbWUgcmVmZXJzIHRvIHRoZSBjb21tb24tbmFtZSBvZiB0aGlzIHJlZ2lvbiBhcyBkZWZpbmVkIGJ5XG4gICMgdGhlIExvUmEgQWxsaWFuY2UuXG4gIGNvbW1vbl9uYW1lPVwiVVM5MTVcIlxuXG5cbiAgIyBHYXRld2F5IGNvbmZpZ3VyYXRpb24uXG4gIFtyZWdpb25zLmdhdGV3YXldXG5cbiAgICAjIEZvcmNlIGdhdGV3YXlzIGFzIHByaXZhdGUuXG4gICAgI1xuICAgICMgSWYgZW5hYmxlZCwgZ2F0ZXdheXMgY2FuIG9ubHkgYmUgdXNlZCBieSBkZXZpY2VzIHVuZGVyIHRoZSBzYW1lIHRlbmFudC5cbiAgICBmb3JjZV9nd3NfcHJpdmF0ZT1mYWxzZVxuXG4gICAgXG4gICAgIyBHYXRld2F5IGJhY2tlbmQgY29uZmlndXJhdGlvbi5cbiAgICBbcmVnaW9ucy5nYXRld2F5LmJhY2tlbmRdXG5cbiAgICAgICMgVGhlIGVuYWJsZWQgYmFja2VuZCB0eXBlLlxuICAgICAgZW5hYmxlZD1cIm1xdHRcIlxuXG4gICAgICAjIE1RVFQgY29uZmlndXJhdGlvbi5cbiAgICAgIFtyZWdpb25zLmdhdGV3YXkuYmFja2VuZC5tcXR0XVxuXG4gICAgICAgICMgVG9waWMgcHJlZml4LlxuICAgICAgICAjXG4gICAgICAgICMgVGhlIHRvcGljIHByZWZpeCBjYW4gYmUgdXNlZCB0byBkZWZpbmUgdGhlIHJlZ2lvbiBvZiB0aGUgZ2F0ZXdheS5cbiAgICAgICAgIyBOb3RlLCB0aGVyZSBpcyBubyBuZWVkIHRvIGFkZCBhIHRyYWlsaW5nICcvJyB0byB0aGUgcHJlZml4LiBUaGUgdHJhaWxpbmdcbiAgICAgICAgIyAnLycgaXMgYXV0b21hdGljYWxseSBhZGRlZCB0byB0aGUgcHJlZml4IGlmIGl0IGlzIGNvbmZpZ3VyZWQuXG4gICAgICAgIHRvcGljX3ByZWZpeD1cInVzOTE1XzZcIlxuXG4gICAgICAgICMgTVFUVCBzZXJ2ZXIgKGUuZy4gc2NoZW1lOi8vaG9zdDpwb3J0IHdoZXJlIHNjaGVtZSBpcyB0Y3AsIHNzbCBvciB3cylcbiAgICAgICAgc2VydmVyPVwidGNwOi8vbW9zcXVpdHRvOjE4ODNcIlxuXG4gICAgICAgICMgQ29ubmVjdCB3aXRoIHRoZSBnaXZlbiB1c2VybmFtZSAob3B0aW9uYWwpXG4gICAgICAgIHVzZXJuYW1lPVwiXCJcblxuICAgICAgICAjIENvbm5lY3Qgd2l0aCB0aGUgZ2l2ZW4gcGFzc3dvcmQgKG9wdGlvbmFsKVxuICAgICAgICBwYXNzd29yZD1cIlwiXG5cbiAgICAgICAgIyBRdWFsaXR5IG9mIHNlcnZpY2UgbGV2ZWxcbiAgICAgICAgI1xuICAgICAgICAjIDA6IGF0IG1vc3Qgb25jZVxuICAgICAgICAjIDE6IGF0IGxlYXN0IG9uY2VcbiAgICAgICAgIyAyOiBleGFjdGx5IG9uY2VcbiAgICAgICAgI1xuICAgICAgICAjIE5vdGU6IGFuIGluY3JlYXNlIG9mIHRoaXMgdmFsdWUgd2lsbCBkZWNyZWFzZSB0aGUgcGVyZm9ybWFuY2UuXG4gICAgICAgICMgRm9yIG1vcmUgaW5mb3JtYXRpb246IGh0dHBzOi8vd3d3LmhpdmVtcS5jb20vYmxvZy9tcXR0LWVzc2VudGlhbHMtcGFydC02LW1xdHQtcXVhbGl0eS1vZi1zZXJ2aWNlLWxldmVsc1xuICAgICAgICBxb3M9MFxuXG4gICAgICAgICMgQ2xlYW4gc2Vzc2lvblxuICAgICAgICAjXG4gICAgICAgICMgU2V0IHRoZSBcImNsZWFuIHNlc3Npb25cIiBmbGFnIGluIHRoZSBjb25uZWN0IG1lc3NhZ2Ugd2hlbiB0aGlzIGNsaWVudFxuICAgICAgICAjIGNvbm5lY3RzIHRvIGFuIE1RVFQgYnJva2VyLiBCeSBzZXR0aW5nIHRoaXMgZmxhZyB5b3UgYXJlIGluZGljYXRpbmdcbiAgICAgICAgIyB0aGF0IG5vIG1lc3NhZ2VzIHNhdmVkIGJ5IHRoZSBicm9rZXIgZm9yIHRoaXMgY2xpZW50IHNob3VsZCBiZSBkZWxpdmVyZWQuXG4gICAgICAgIGNsZWFuX3Nlc3Npb249ZmFsc2VcblxuICAgICAgICAjIENsaWVudCBJRFxuICAgICAgICAjXG4gICAgICAgICMgU2V0IHRoZSBjbGllbnQgaWQgdG8gYmUgdXNlZCBieSB0aGlzIGNsaWVudCB3aGVuIGNvbm5lY3RpbmcgdG8gdGhlIE1RVFRcbiAgICAgICAgIyBicm9rZXIuIEEgY2xpZW50IGlkIG11c3QgYmUgbm8gbG9uZ2VyIHRoYW4gMjMgY2hhcmFjdGVycy4gSWYgbGVmdCBibGFuayxcbiAgICAgICAgIyBhIHJhbmRvbSBpZCB3aWxsIGJlIGdlbmVyYXRlZCBieSBDaGlycFN0YWNrLlxuICAgICAgICBjbGllbnRfaWQ9XCJcIlxuXG4gICAgICAgICMgS2VlcCBhbGl2ZSBpbnRlcnZhbC5cbiAgICAgICAgI1xuICAgICAgICAjIFRoaXMgZGVmaW5lcyB0aGUgbWF4aW11bSB0aW1lIHRoYXQgdGhhdCBzaG91bGQgcGFzcyB3aXRob3V0IGNvbW11bmljYXRpb25cbiAgICAgICAgIyBiZXR3ZWVuIHRoZSBjbGllbnQgYW5kIHNlcnZlci5cbiAgICAgICAga2VlcF9hbGl2ZV9pbnRlcnZhbD1cIjMwc1wiXG5cbiAgICAgICAgIyBDQSBjZXJ0aWZpY2F0ZSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgI1xuICAgICAgICAjIFVzZSB0aGlzIHdoZW4gc2V0dGluZyB1cCBhIHNlY3VyZSBjb25uZWN0aW9uICh3aGVuIHNlcnZlciB1c2VzIHNzbDovLy4uLilcbiAgICAgICAgIyBidXQgdGhlIGNlcnRpZmljYXRlIHVzZWQgYnkgdGhlIHNlcnZlciBpcyBub3QgdHJ1c3RlZCBieSBhbnkgQ0EgY2VydGlmaWNhdGVcbiAgICAgICAgIyBvbiB0aGUgc2VydmVyIChlLmcuIHdoZW4gc2VsZiBnZW5lcmF0ZWQpLlxuICAgICAgICBjYV9jZXJ0PVwiXCJcblxuICAgICAgICAjIFRMUyBjZXJ0aWZpY2F0ZSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgdGxzX2NlcnQ9XCJcIlxuXG4gICAgICAgICMgVExTIGtleSBmaWxlIChvcHRpb25hbClcbiAgICAgICAgdGxzX2tleT1cIlwiXG5cblxuICAgICMgR2F0ZXdheSBjaGFubmVsIGNvbmZpZ3VyYXRpb24uXG4gICAgI1xuICAgICMgTm90ZTogdGhpcyBjb25maWd1cmF0aW9uIGlzIG9ubHkgdXNlZCBpbiBjYXNlIHRoZSBnYXRld2F5IGlzIHVzaW5nIHRoZVxuICAgICMgQ2hpcnBTdGFjayBDb25jZW50cmF0b3JkIGRhZW1vbi4gSW4gYW55IG90aGVyIGNhc2UsIHRoaXMgY29uZmlndXJhdGlvbiBcbiAgICAjIGlzIGlnbm9yZWQuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkxMTkwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkxMjEwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkxMjMwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkxMjUwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkxMjcwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkxMjkwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkxMzEwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkxMzMwMDAwMFxuICAgICAgYmFuZHdpZHRoPTEyNTAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzcsIDgsIDksIDEwXVxuXG4gICAgW1tyZWdpb25zLmdhdGV3YXkuY2hhbm5lbHNdXVxuICAgICAgZnJlcXVlbmN5PTkxMjYwMDAwMFxuICAgICAgYmFuZHdpZHRoPTUwMDAwMFxuICAgICAgbW9kdWxhdGlvbj1cIkxPUkFcIlxuICAgICAgc3ByZWFkaW5nX2ZhY3RvcnM9WzhdXG5cblxuICAjIFJlZ2lvbiBzcGVjaWZpYyBuZXR3b3JrIGNvbmZpZ3VyYXRpb24uXG4gIFtyZWdpb25zLm5ldHdvcmtdXG4gICAgXG4gICAgIyBJbnN0YWxsYXRpb24gbWFyZ2luIChkQikgdXNlZCBieSB0aGUgQURSIGVuZ2luZS5cbiAgICAjXG4gICAgIyBBIGhpZ2hlciBudW1iZXIgbWVhbnMgdGhhdCB0aGUgbmV0d29yay1zZXJ2ZXIgd2lsbCBrZWVwIG1vcmUgbWFyZ2luLFxuICAgICMgcmVzdWx0aW5nIGluIGEgbG93ZXIgZGF0YS1yYXRlIGJ1dCBkZWNyZWFzaW5nIHRoZSBjaGFuY2UgdGhhdCB0aGVcbiAgICAjIGRldmljZSBnZXRzIGRpc2Nvbm5lY3RlZCBiZWNhdXNlIGl0IGlzIHVuYWJsZSB0byByZWFjaCBvbmUgb2YgdGhlXG4gICAgIyBzdXJyb3VuZGVkIGdhdGV3YXlzLlxuICAgIGluc3RhbGxhdGlvbl9tYXJnaW49MTBcblxuICAgICMgUlggd2luZG93IChDbGFzcy1BKS5cbiAgICAjXG4gICAgIyBTZXQgdGhpcyB0bzpcbiAgICAjIDA6IFJYMSAvIFJYMlxuICAgICMgMTogUlgxIG9ubHlcbiAgICAjIDI6IFJYMiBvbmx5XG4gICAgcnhfd2luZG93PTBcblxuICAgICMgUlgxIGRlbGF5ICgxIC0gMTUgc2Vjb25kcykuXG4gICAgcngxX2RlbGF5PTFcblxuICAgICMgUlgxIGRhdGEtcmF0ZSBvZmZzZXRcbiAgICByeDFfZHJfb2Zmc2V0PTBcblxuICAgICMgUlgyIGRhdGEtcmF0ZVxuICAgIHJ4Ml9kcj04XG5cbiAgICAjIFJYMiBmcmVxdWVuY3kgKEh6KVxuICAgIHJ4Ml9mcmVxdWVuY3k9OTIzMzAwMDAwXG5cbiAgICAjIFByZWZlciBSWDIgb24gUlgxIGRhdGEtcmF0ZSBsZXNzIHRoYW4uXG4gICAgI1xuICAgICMgUHJlZmVyIFJYMiBvdmVyIFJYMSBiYXNlZCBvbiB0aGUgUlgxIGRhdGEtcmF0ZS4gV2hlbiB0aGUgUlgxIGRhdGEtcmF0ZVxuICAgICMgaXMgc21hbGxlciB0aGFuIHRoZSBjb25maWd1cmVkIHZhbHVlLCB0aGVuIHRoZSBOZXR3b3JrIFNlcnZlciB3aWxsXG4gICAgIyBmaXJzdCB0cnkgdG8gc2NoZWR1bGUgdGhlIGRvd25saW5rIGZvciBSWDIsIGZhaWxpbmcgdGhhdCAoZS5nLiB0aGUgZ2F0ZXdheVxuICAgICMgaGFzIGFscmVhZHkgYSBwYXlsb2FkIHNjaGVkdWxlZCBhdCB0aGUgUlgyIHRpbWluZykgaXQgd2lsbCB0cnkgUlgxLlxuICAgIHJ4Ml9wcmVmZXJfb25fcngxX2RyX2x0PTBcblxuICAgICMgUHJlZmVyIFJYMiBvbiBsaW5rIGJ1ZGdldC5cbiAgICAjXG4gICAgIyBXaGVuIHRoZSBsaW5rLWJ1ZGdldCBpcyBiZXR0ZXIgZm9yIFJYMiB0aGFuIGZvciBSWDEsIHRoZSBOZXR3b3JrIFNlcnZlciB3aWxsIGZpcnN0XG4gICAgIyB0cnkgdG8gc2NoZWR1bGUgdGhlIGRvd25saW5rIGluIFJYMiwgZmFpbGluZyB0aGF0IGl0IHdpbGwgdHJ5IFJYMS5cbiAgICByeDJfcHJlZmVyX29uX2xpbmtfYnVkZ2V0PWZhbHNlXG5cbiAgICAjIERvd25saW5rIFRYIFBvd2VyIChkQm0pXG4gICAgI1xuICAgICMgV2hlbiBzZXQgdG8gLTEsIHRoZSBkb3dubGluayBUWCBQb3dlciBmcm9tIHRoZSBjb25maWd1cmVkIGJhbmQgd2lsbFxuICAgICMgYmUgdXNlZC5cbiAgICAjXG4gICAgIyBQbGVhc2UgY29uc3VsdCB0aGUgTG9SYVdBTiBSZWdpb25hbCBQYXJhbWV0ZXJzIGFuZCBsb2NhbCByZWd1bGF0aW9uc1xuICAgICMgZm9yIHZhbGlkIGFuZCBsZWdhbCBvcHRpb25zLiBOb3RlIHRoYXQgdGhlIGNvbmZpZ3VyZWQgVFggUG93ZXIgbXVzdCBiZVxuICAgICMgc3VwcG9ydGVkIGJ5IHlvdXIgZ2F0ZXdheShzKS5cbiAgICBkb3dubGlua190eF9wb3dlcj0tMVxuXG4gICAgIyBBRFIgaXMgZGlzYWJsZWQuXG4gICAgYWRyX2Rpc2FibGVkPWZhbHNlXG5cbiAgICAjIE1pbmltdW0gZGF0YS1yYXRlLlxuICAgIG1pbl9kcj0wXG5cbiAgICAjIE1heGltdW0gZGF0YS1yYXRlLlxuICAgIG1heF9kcj0zXG5cbiAgICAjIEVuYWJsZWQgdXBsaW5rIGNoYW5uZWxzLlxuICAgICNcbiAgICAjIFVzZSB0aGlzIHdoZW4gb255IGEgc3ViLXNldCBvZiB0aGUgYnkgZGVmYXVsdCBlbmFibGVkIGNoYW5uZWxzIGFyZSBiZWluZ1xuICAgICMgdXNlZC4gRm9yIGV4YW1wbGUgd2hlbiBvbmx5IHVzaW5nIHRoZSBmaXJzdCA4IGNoYW5uZWxzIG9mIHRoZSBVUyBiYW5kLlxuICAgICMgTm90ZTogd2hlbiBsZWZ0IGJsYW5rIC8gZW1wdHkgYXJyYXksIGFsbCBjaGFubmVscyB3aWxsIGJlIGVuYWJsZWQuXG4gICAgZW5hYmxlZF91cGxpbmtfY2hhbm5lbHM9WzQ4LCA0OSwgNTAsIDUxLCA1MiwgNTMsIDU0LCA1NSwgNzBdXG5cblxuICAgICMgUmVqb2luLXJlcXVlc3QgY29uZmlndXJhdGlvbiAoTG9SYVdBTiAxLjEpXG4gICAgW3JlZ2lvbnMubmV0d29yay5yZWpvaW5fcmVxdWVzdF1cblxuICAgICAgIyBSZXF1ZXN0IGRldmljZXMgdG8gcGVyaW9kaWNhbGx5IHNlbmQgcmVqb2luLXJlcXVlc3RzLlxuICAgICAgZW5hYmxlZD1mYWxzZVxuXG4gICAgICAjIFRoZSBkZXZpY2UgbXVzdCBzZW5kIGEgcmVqb2luLXJlcXVlc3QgdHlwZSAwIGF0IGxlYXN0IGV2ZXJ5IDJeKG1heF9jb3VudF9uICsgNClcbiAgICAgICMgdXBsaW5rIG1lc3NhZ2VzLiBWYWxpZCB2YWx1ZXMgYXJlIDAgdG8gMTUuXG4gICAgICBtYXhfY291bnRfbj0wXG5cbiAgICAgICMgVGhlIGRldmljZSBtdXN0IHNlbmQgYSByZWpvaW4tcmVxdWVzdCB0eXBlIDAgYXQgbGVhc3QgZXZlcnkgMl4obWF4X3RpbWVfbiArIDEwKVxuICAgICAgIyBzZWNvbmRzLiBWYWxpZCB2YWx1ZXMgYXJlIDAgdG8gMTUuXG4gICAgICAjXG4gICAgICAjIDAgID0gcm91Z2hseSAxNyBtaW51dGVzXG4gICAgICAjIDE1ID0gYWJvdXQgMSB5ZWFyXG4gICAgICBtYXhfdGltZV9uPTBcbiAgICBcblxuICAgICMgQ2xhc3MtQiBjb25maWd1cmF0aW9uLlxuICAgIFtyZWdpb25zLm5ldHdvcmsuY2xhc3NfYl1cblxuICAgICAgIyBQaW5nLXNsb3QgZGF0YS1yYXRlLiBcbiAgICAgIHBpbmdfc2xvdF9kcj04XG5cbiAgICAgICMgUGluZy1zbG90IGZyZXF1ZW5jeSAoSHopXG4gICAgICAjXG4gICAgICAjIHNldCB0aGlzIHRvIDAgdG8gdXNlIHRoZSBkZWZhdWx0IGZyZXF1ZW5jeSBwbGFuIGZvciB0aGUgY29uZmlndXJlZCByZWdpb25cbiAgICAgICMgKHdoaWNoIGNvdWxkIGJlIGZyZXF1ZW5jeSBob3BwaW5nKS5cbiAgICAgIHBpbmdfc2xvdF9mcmVxdWVuY3k9MFxuXCJcIlwiXG5cbltbY29uZmlnLm1vdW50c11dXG5zZXJ2aWNlTmFtZSA9IFwiY2hpcnBzdGFja1wiXG5maWxlUGF0aCA9IFwiL2NoaXJwc3RhY2svcmVnaW9uX3VzOTE1XzcudG9tbFwiXG5jb250ZW50ID0gXCJcIlwiXG4jIFRoaXMgZmlsZSBjb250YWlucyBhbiBleGFtcGxlIFVTOTE1IGV4YW1wbGUgKGNoYW5uZWxzIDU2LTYzICsgNzEpLlxuW1tyZWdpb25zXV1cblxuICAjIElEIGlzIGFuIHVzZS1kZWZpbmVkIGlkZW50aWZpZXIgZm9yIHRoaXMgcmVnaW9uLlxuICBpZD1cInVzOTE1XzdcIlxuXG4gICMgRGVzY3JpcHRpb24gaXMgYSBzaG9ydCBkZXNjcmlwdGlvbiBmb3IgdGhpcyByZWdpb24uXG4gIGRlc2NyaXB0aW9uPVwiVVM5MTUgKGNoYW5uZWxzIDU2LTYzICsgNzEpXCJcblxuICAjIENvbW1vbi1uYW1lIHJlZmVycyB0byB0aGUgY29tbW9uLW5hbWUgb2YgdGhpcyByZWdpb24gYXMgZGVmaW5lZCBieVxuICAjIHRoZSBMb1JhIEFsbGlhbmNlLlxuICBjb21tb25fbmFtZT1cIlVTOTE1XCJcblxuXG4gICMgR2F0ZXdheSBjb25maWd1cmF0aW9uLlxuICBbcmVnaW9ucy5nYXRld2F5XVxuXG4gICAgIyBGb3JjZSBnYXRld2F5cyBhcyBwcml2YXRlLlxuICAgICNcbiAgICAjIElmIGVuYWJsZWQsIGdhdGV3YXlzIGNhbiBvbmx5IGJlIHVzZWQgYnkgZGV2aWNlcyB1bmRlciB0aGUgc2FtZSB0ZW5hbnQuXG4gICAgZm9yY2VfZ3dzX3ByaXZhdGU9ZmFsc2VcblxuICAgIFxuICAgICMgR2F0ZXdheSBiYWNrZW5kIGNvbmZpZ3VyYXRpb24uXG4gICAgW3JlZ2lvbnMuZ2F0ZXdheS5iYWNrZW5kXVxuXG4gICAgICAjIFRoZSBlbmFibGVkIGJhY2tlbmQgdHlwZS5cbiAgICAgIGVuYWJsZWQ9XCJtcXR0XCJcblxuICAgICAgIyBNUVRUIGNvbmZpZ3VyYXRpb24uXG4gICAgICBbcmVnaW9ucy5nYXRld2F5LmJhY2tlbmQubXF0dF1cblxuICAgICAgICAjIFRvcGljIHByZWZpeC5cbiAgICAgICAgI1xuICAgICAgICAjIFRoZSB0b3BpYyBwcmVmaXggY2FuIGJlIHVzZWQgdG8gZGVmaW5lIHRoZSByZWdpb24gb2YgdGhlIGdhdGV3YXkuXG4gICAgICAgICMgTm90ZSwgdGhlcmUgaXMgbm8gbmVlZCB0byBhZGQgYSB0cmFpbGluZyAnLycgdG8gdGhlIHByZWZpeC4gVGhlIHRyYWlsaW5nXG4gICAgICAgICMgJy8nIGlzIGF1dG9tYXRpY2FsbHkgYWRkZWQgdG8gdGhlIHByZWZpeCBpZiBpdCBpcyBjb25maWd1cmVkLlxuICAgICAgICB0b3BpY19wcmVmaXg9XCJ1czkxNV83XCJcblxuICAgICAgICAjIE1RVFQgc2VydmVyIChlLmcuIHNjaGVtZTovL2hvc3Q6cG9ydCB3aGVyZSBzY2hlbWUgaXMgdGNwLCBzc2wgb3Igd3MpXG4gICAgICAgIHNlcnZlcj1cInRjcDovL21vc3F1aXR0bzoxODgzXCJcblxuICAgICAgICAjIENvbm5lY3Qgd2l0aCB0aGUgZ2l2ZW4gdXNlcm5hbWUgKG9wdGlvbmFsKVxuICAgICAgICB1c2VybmFtZT1cIlwiXG5cbiAgICAgICAgIyBDb25uZWN0IHdpdGggdGhlIGdpdmVuIHBhc3N3b3JkIChvcHRpb25hbClcbiAgICAgICAgcGFzc3dvcmQ9XCJcIlxuXG4gICAgICAgICMgUXVhbGl0eSBvZiBzZXJ2aWNlIGxldmVsXG4gICAgICAgICNcbiAgICAgICAgIyAwOiBhdCBtb3N0IG9uY2VcbiAgICAgICAgIyAxOiBhdCBsZWFzdCBvbmNlXG4gICAgICAgICMgMjogZXhhY3RseSBvbmNlXG4gICAgICAgICNcbiAgICAgICAgIyBOb3RlOiBhbiBpbmNyZWFzZSBvZiB0aGlzIHZhbHVlIHdpbGwgZGVjcmVhc2UgdGhlIHBlcmZvcm1hbmNlLlxuICAgICAgICAjIEZvciBtb3JlIGluZm9ybWF0aW9uOiBodHRwczovL3d3dy5oaXZlbXEuY29tL2Jsb2cvbXF0dC1lc3NlbnRpYWxzLXBhcnQtNi1tcXR0LXF1YWxpdHktb2Ytc2VydmljZS1sZXZlbHNcbiAgICAgICAgcW9zPTBcblxuICAgICAgICAjIENsZWFuIHNlc3Npb25cbiAgICAgICAgI1xuICAgICAgICAjIFNldCB0aGUgXCJjbGVhbiBzZXNzaW9uXCIgZmxhZyBpbiB0aGUgY29ubmVjdCBtZXNzYWdlIHdoZW4gdGhpcyBjbGllbnRcbiAgICAgICAgIyBjb25uZWN0cyB0byBhbiBNUVRUIGJyb2tlci4gQnkgc2V0dGluZyB0aGlzIGZsYWcgeW91IGFyZSBpbmRpY2F0aW5nXG4gICAgICAgICMgdGhhdCBubyBtZXNzYWdlcyBzYXZlZCBieSB0aGUgYnJva2VyIGZvciB0aGlzIGNsaWVudCBzaG91bGQgYmUgZGVsaXZlcmVkLlxuICAgICAgICBjbGVhbl9zZXNzaW9uPWZhbHNlXG5cbiAgICAgICAgIyBDbGllbnQgSURcbiAgICAgICAgI1xuICAgICAgICAjIFNldCB0aGUgY2xpZW50IGlkIHRvIGJlIHVzZWQgYnkgdGhpcyBjbGllbnQgd2hlbiBjb25uZWN0aW5nIHRvIHRoZSBNUVRUXG4gICAgICAgICMgYnJva2VyLiBBIGNsaWVudCBpZCBtdXN0IGJlIG5vIGxvbmdlciB0aGFuIDIzIGNoYXJhY3RlcnMuIElmIGxlZnQgYmxhbmssXG4gICAgICAgICMgYSByYW5kb20gaWQgd2lsbCBiZSBnZW5lcmF0ZWQgYnkgQ2hpcnBTdGFjay5cbiAgICAgICAgY2xpZW50X2lkPVwiXCJcblxuICAgICAgICAjIEtlZXAgYWxpdmUgaW50ZXJ2YWwuXG4gICAgICAgICNcbiAgICAgICAgIyBUaGlzIGRlZmluZXMgdGhlIG1heGltdW0gdGltZSB0aGF0IHRoYXQgc2hvdWxkIHBhc3Mgd2l0aG91dCBjb21tdW5pY2F0aW9uXG4gICAgICAgICMgYmV0d2VlbiB0aGUgY2xpZW50IGFuZCBzZXJ2ZXIuXG4gICAgICAgIGtlZXBfYWxpdmVfaW50ZXJ2YWw9XCIzMHNcIlxuXG4gICAgICAgICMgQ0EgY2VydGlmaWNhdGUgZmlsZSAob3B0aW9uYWwpXG4gICAgICAgICNcbiAgICAgICAgIyBVc2UgdGhpcyB3aGVuIHNldHRpbmcgdXAgYSBzZWN1cmUgY29ubmVjdGlvbiAod2hlbiBzZXJ2ZXIgdXNlcyBzc2w6Ly8uLi4pXG4gICAgICAgICMgYnV0IHRoZSBjZXJ0aWZpY2F0ZSB1c2VkIGJ5IHRoZSBzZXJ2ZXIgaXMgbm90IHRydXN0ZWQgYnkgYW55IENBIGNlcnRpZmljYXRlXG4gICAgICAgICMgb24gdGhlIHNlcnZlciAoZS5nLiB3aGVuIHNlbGYgZ2VuZXJhdGVkKS5cbiAgICAgICAgY2FfY2VydD1cIlwiXG5cbiAgICAgICAgIyBUTFMgY2VydGlmaWNhdGUgZmlsZSAob3B0aW9uYWwpXG4gICAgICAgIHRsc19jZXJ0PVwiXCJcblxuICAgICAgICAjIFRMUyBrZXkgZmlsZSAob3B0aW9uYWwpXG4gICAgICAgIHRsc19rZXk9XCJcIlxuXG5cbiAgICAjIEdhdGV3YXkgY2hhbm5lbCBjb25maWd1cmF0aW9uLlxuICAgICNcbiAgICAjIE5vdGU6IHRoaXMgY29uZmlndXJhdGlvbiBpcyBvbmx5IHVzZWQgaW4gY2FzZSB0aGUgZ2F0ZXdheSBpcyB1c2luZyB0aGVcbiAgICAjIENoaXJwU3RhY2sgQ29uY2VudHJhdG9yZCBkYWVtb24uIEluIGFueSBvdGhlciBjYXNlLCB0aGlzIGNvbmZpZ3VyYXRpb24gXG4gICAgIyBpcyBpZ25vcmVkLlxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MTM1MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMF1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MTM3MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMF1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MTM5MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMF1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MTQxMDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMF1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MTQzMDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMF1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MTQ1MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMF1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MTQ3MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMF1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MTQ5MDAwMDBcbiAgICAgIGJhbmR3aWR0aD0xMjUwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs3LCA4LCA5LCAxMF1cblxuICAgIFtbcmVnaW9ucy5nYXRld2F5LmNoYW5uZWxzXV1cbiAgICAgIGZyZXF1ZW5jeT05MTQyMDAwMDBcbiAgICAgIGJhbmR3aWR0aD01MDAwMDBcbiAgICAgIG1vZHVsYXRpb249XCJMT1JBXCJcbiAgICAgIHNwcmVhZGluZ19mYWN0b3JzPVs4XVxuXG5cbiAgIyBSZWdpb24gc3BlY2lmaWMgbmV0d29yayBjb25maWd1cmF0aW9uLlxuICBbcmVnaW9ucy5uZXR3b3JrXVxuICAgIFxuICAgICMgSW5zdGFsbGF0aW9uIG1hcmdpbiAoZEIpIHVzZWQgYnkgdGhlIEFEUiBlbmdpbmUuXG4gICAgI1xuICAgICMgQSBoaWdoZXIgbnVtYmVyIG1lYW5zIHRoYXQgdGhlIG5ldHdvcmstc2VydmVyIHdpbGwga2VlcCBtb3JlIG1hcmdpbixcbiAgICAjIHJlc3VsdGluZyBpbiBhIGxvd2VyIGRhdGEtcmF0ZSBidXQgZGVjcmVhc2luZyB0aGUgY2hhbmNlIHRoYXQgdGhlXG4gICAgIyBkZXZpY2UgZ2V0cyBkaXNjb25uZWN0ZWQgYmVjYXVzZSBpdCBpcyB1bmFibGUgdG8gcmVhY2ggb25lIG9mIHRoZVxuICAgICMgc3Vycm91bmRlZCBnYXRld2F5cy5cbiAgICBpbnN0YWxsYXRpb25fbWFyZ2luPTEwXG5cbiAgICAjIFJYIHdpbmRvdyAoQ2xhc3MtQSkuXG4gICAgI1xuICAgICMgU2V0IHRoaXMgdG86XG4gICAgIyAwOiBSWDEgLyBSWDJcbiAgICAjIDE6IFJYMSBvbmx5XG4gICAgIyAyOiBSWDIgb25seVxuICAgIHJ4X3dpbmRvdz0wXG5cbiAgICAjIFJYMSBkZWxheSAoMSAtIDE1IHNlY29uZHMpLlxuICAgIHJ4MV9kZWxheT0xXG5cbiAgICAjIFJYMSBkYXRhLXJhdGUgb2Zmc2V0XG4gICAgcngxX2RyX29mZnNldD0wXG5cbiAgICAjIFJYMiBkYXRhLXJhdGVcbiAgICByeDJfZHI9OFxuXG4gICAgIyBSWDIgZnJlcXVlbmN5IChIeilcbiAgICByeDJfZnJlcXVlbmN5PTkyMzMwMDAwMFxuXG4gICAgIyBQcmVmZXIgUlgyIG9uIFJYMSBkYXRhLXJhdGUgbGVzcyB0aGFuLlxuICAgICNcbiAgICAjIFByZWZlciBSWDIgb3ZlciBSWDEgYmFzZWQgb24gdGhlIFJYMSBkYXRhLXJhdGUuIFdoZW4gdGhlIFJYMSBkYXRhLXJhdGVcbiAgICAjIGlzIHNtYWxsZXIgdGhhbiB0aGUgY29uZmlndXJlZCB2YWx1ZSwgdGhlbiB0aGUgTmV0d29yayBTZXJ2ZXIgd2lsbFxuICAgICMgZmlyc3QgdHJ5IHRvIHNjaGVkdWxlIHRoZSBkb3dubGluayBmb3IgUlgyLCBmYWlsaW5nIHRoYXQgKGUuZy4gdGhlIGdhdGV3YXlcbiAgICAjIGhhcyBhbHJlYWR5IGEgcGF5bG9hZCBzY2hlZHVsZWQgYXQgdGhlIFJYMiB0aW1pbmcpIGl0IHdpbGwgdHJ5IFJYMS5cbiAgICByeDJfcHJlZmVyX29uX3J4MV9kcl9sdD0wXG5cbiAgICAjIFByZWZlciBSWDIgb24gbGluayBidWRnZXQuXG4gICAgI1xuICAgICMgV2hlbiB0aGUgbGluay1idWRnZXQgaXMgYmV0dGVyIGZvciBSWDIgdGhhbiBmb3IgUlgxLCB0aGUgTmV0d29yayBTZXJ2ZXIgd2lsbCBmaXJzdFxuICAgICMgdHJ5IHRvIHNjaGVkdWxlIHRoZSBkb3dubGluayBpbiBSWDIsIGZhaWxpbmcgdGhhdCBpdCB3aWxsIHRyeSBSWDEuXG4gICAgcngyX3ByZWZlcl9vbl9saW5rX2J1ZGdldD1mYWxzZVxuXG4gICAgIyBEb3dubGluayBUWCBQb3dlciAoZEJtKVxuICAgICNcbiAgICAjIFdoZW4gc2V0IHRvIC0xLCB0aGUgZG93bmxpbmsgVFggUG93ZXIgZnJvbSB0aGUgY29uZmlndXJlZCBiYW5kIHdpbGxcbiAgICAjIGJlIHVzZWQuXG4gICAgI1xuICAgICMgUGxlYXNlIGNvbnN1bHQgdGhlIExvUmFXQU4gUmVnaW9uYWwgUGFyYW1ldGVycyBhbmQgbG9jYWwgcmVndWxhdGlvbnNcbiAgICAjIGZvciB2YWxpZCBhbmQgbGVnYWwgb3B0aW9ucy4gTm90ZSB0aGF0IHRoZSBjb25maWd1cmVkIFRYIFBvd2VyIG11c3QgYmVcbiAgICAjIHN1cHBvcnRlZCBieSB5b3VyIGdhdGV3YXkocykuXG4gICAgZG93bmxpbmtfdHhfcG93ZXI9LTFcblxuICAgICMgQURSIGlzIGRpc2FibGVkLlxuICAgIGFkcl9kaXNhYmxlZD1mYWxzZVxuXG4gICAgIyBNaW5pbXVtIGRhdGEtcmF0ZS5cbiAgICBtaW5fZHI9MFxuXG4gICAgIyBNYXhpbXVtIGRhdGEtcmF0ZS5cbiAgICBtYXhfZHI9M1xuXG4gICAgIyBFbmFibGVkIHVwbGluayBjaGFubmVscy5cbiAgICAjXG4gICAgIyBVc2UgdGhpcyB3aGVuIG9ueSBhIHN1Yi1zZXQgb2YgdGhlIGJ5IGRlZmF1bHQgZW5hYmxlZCBjaGFubmVscyBhcmUgYmVpbmdcbiAgICAjIHVzZWQuIEZvciBleGFtcGxlIHdoZW4gb25seSB1c2luZyB0aGUgZmlyc3QgOCBjaGFubmVscyBvZiB0aGUgVVMgYmFuZC5cbiAgICAjIE5vdGU6IHdoZW4gbGVmdCBibGFuayAvIGVtcHR5IGFycmF5LCBhbGwgY2hhbm5lbHMgd2lsbCBiZSBlbmFibGVkLlxuICAgIGVuYWJsZWRfdXBsaW5rX2NoYW5uZWxzPVs1NiwgNTcsIDU4LCA1OSwgNjAsIDYxLCA2MiwgNjMsIDcxXVxuXG5cbiAgICAjIFJlam9pbi1yZXF1ZXN0IGNvbmZpZ3VyYXRpb24gKExvUmFXQU4gMS4xKVxuICAgIFtyZWdpb25zLm5ldHdvcmsucmVqb2luX3JlcXVlc3RdXG5cbiAgICAgICMgUmVxdWVzdCBkZXZpY2VzIHRvIHBlcmlvZGljYWxseSBzZW5kIHJlam9pbi1yZXF1ZXN0cy5cbiAgICAgIGVuYWJsZWQ9ZmFsc2VcblxuICAgICAgIyBUaGUgZGV2aWNlIG11c3Qgc2VuZCBhIHJlam9pbi1yZXF1ZXN0IHR5cGUgMCBhdCBsZWFzdCBldmVyeSAyXihtYXhfY291bnRfbiArIDQpXG4gICAgICAjIHVwbGluayBtZXNzYWdlcy4gVmFsaWQgdmFsdWVzIGFyZSAwIHRvIDE1LlxuICAgICAgbWF4X2NvdW50X249MFxuXG4gICAgICAjIFRoZSBkZXZpY2UgbXVzdCBzZW5kIGEgcmVqb2luLXJlcXVlc3QgdHlwZSAwIGF0IGxlYXN0IGV2ZXJ5IDJeKG1heF90aW1lX24gKyAxMClcbiAgICAgICMgc2Vjb25kcy4gVmFsaWQgdmFsdWVzIGFyZSAwIHRvIDE1LlxuICAgICAgI1xuICAgICAgIyAwICA9IHJvdWdobHkgMTcgbWludXRlc1xuICAgICAgIyAxNSA9IGFib3V0IDEgeWVhclxuICAgICAgbWF4X3RpbWVfbj0wXG4gICAgXG5cbiAgICAjIENsYXNzLUIgY29uZmlndXJhdGlvbi5cbiAgICBbcmVnaW9ucy5uZXR3b3JrLmNsYXNzX2JdXG5cbiAgICAgICMgUGluZy1zbG90IGRhdGEtcmF0ZS4gXG4gICAgICBwaW5nX3Nsb3RfZHI9OFxuXG4gICAgICAjIFBpbmctc2xvdCBmcmVxdWVuY3kgKEh6KVxuICAgICAgI1xuICAgICAgIyBzZXQgdGhpcyB0byAwIHRvIHVzZSB0aGUgZGVmYXVsdCBmcmVxdWVuY3kgcGxhbiBmb3IgdGhlIGNvbmZpZ3VyZWQgcmVnaW9uXG4gICAgICAjICh3aGljaCBjb3VsZCBiZSBmcmVxdWVuY3kgaG9wcGluZykuXG4gICAgICBwaW5nX3Nsb3RfZnJlcXVlbmN5PTBcblwiXCJcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuc2VydmljZU5hbWUgPSBcImNoaXJwc3RhY2stZ2F0ZXdheS1icmlkZ2VcIlxuZmlsZVBhdGggPSBcIi9jaGlycHN0YWNrLWdhdGV3YXktYnJpZGdlL2NoaXJwc3RhY2stZ2F0ZXdheS1icmlkZ2UudG9tbFwiXG5jb250ZW50ID0gXCJcIlwiXG4jIFNlZSBodHRwczovL3d3dy5jaGlycHN0YWNrLmlvL2dhdGV3YXktYnJpZGdlL2luc3RhbGwvY29uZmlnLyBmb3IgYSBmdWxsXG4jIGNvbmZpZ3VyYXRpb24gZXhhbXBsZSBhbmQgZG9jdW1lbnRhdGlvbi5cblxuW2ludGVncmF0aW9uLm1xdHQuYXV0aC5nZW5lcmljXVxuc2VydmVycz1bXCJ0Y3A6Ly9tb3NxdWl0dG86MTg4M1wiXVxudXNlcm5hbWU9XCJcIlxucGFzc3dvcmQ9XCJcIlxuXCJcIlwiXG5cbltbY29uZmlnLm1vdW50c11dXG5zZXJ2aWNlTmFtZSA9IFwiY2hpcnBzdGFjay1nYXRld2F5LWJyaWRnZS1iYXNpY3N0YXRpb25cIlxuZmlsZVBhdGggPSBcIi9jaGlycHN0YWNrLWdhdGV3YXktYnJpZGdlL2NoaXJwc3RhY2stZ2F0ZXdheS1icmlkZ2UtYmFzaWNzdGF0aW9uLWV1ODY4LnRvbWxcIlxuY29udGVudCA9IFwiXCJcIlxuIyBTZWUgaHR0cHM6Ly93d3cuY2hpcnBzdGFjay5pby9nYXRld2F5LWJyaWRnZS9pbnN0YWxsL2NvbmZpZy8gZm9yIGEgZnVsbFxuIyBjb25maWd1cmF0aW9uIGV4YW1wbGUgYW5kIGRvY3VtZW50YXRpb24uXG5cbltpbnRlZ3JhdGlvbi5tcXR0LmF1dGguZ2VuZXJpY11cbnNlcnZlcnM9W1widGNwOi8vbW9zcXVpdHRvOjE4ODNcIl1cbnVzZXJuYW1lPVwiXCJcbnBhc3N3b3JkPVwiXCJcblxuW2ludGVncmF0aW9uLm1xdHRdXG5ldmVudF90b3BpY190ZW1wbGF0ZT1cImV1ODY4L2dhdGV3YXkve3sgLkdhdGV3YXlJRCB9fS9ldmVudC97eyAuRXZlbnRUeXBlIH19XCJcbnN0YXRlX3RvcGljX3RlbXBsYXRlPVwiZXU4NjgvZ2F0ZXdheS97eyAuR2F0ZXdheUlEIH19L3N0YXRlL3t7IC5TdGF0ZVR5cGUgfX1cIlxuY29tbWFuZF90b3BpY190ZW1wbGF0ZT1cImV1ODY4L2dhdGV3YXkve3sgLkdhdGV3YXlJRCB9fS9jb21tYW5kLyNcIlxuXG5bYmFja2VuZF1cbnR5cGU9XCJiYXNpY19zdGF0aW9uXCJcblxuICBbYmFja2VuZC5iYXNpY19zdGF0aW9uXVxuICBiaW5kPVwiOjMwMDFcIlxuICB0bHNfY2VydD1cIlwiXG4gIHRsc19rZXk9XCJcIlxuICBjYV9jZXJ0PVwiXCJcblxuICByZWdpb249XCJFVTg2OFwiXG4gIGZyZXF1ZW5jeV9taW49ODYzMDAwMDAwXG4gIGZyZXF1ZW5jeV9tYXg9ODcwMDAwMDAwXG5cblxuICBbW2JhY2tlbmQuYmFzaWNfc3RhdGlvbi5jb25jZW50cmF0b3JzXV1cblxuICAgIFtiYWNrZW5kLmJhc2ljX3N0YXRpb24uY29uY2VudHJhdG9ycy5tdWx0aV9zZl1cbiAgICBmcmVxdWVuY2llcz1bXG4gICAgICA4NjgxMDAwMDAsXG4gICAgICA4NjgzMDAwMDAsXG4gICAgICA4Njg1MDAwMDAsXG4gICAgICA4NjcxMDAwMDAsXG4gICAgICA4NjczMDAwMDAsXG4gICAgICA4Njc1MDAwMDAsXG4gICAgICA4Njc3MDAwMDAsXG4gICAgICA4Njc5MDAwMDAsXG4gICAgXVxuICBcbiAgICBbYmFja2VuZC5iYXNpY19zdGF0aW9uLmNvbmNlbnRyYXRvcnMubG9yYV9zdGRdXG4gICAgZnJlcXVlbmN5PTg2ODMwMDAwMFxuICAgIGJhbmR3aWR0aD0yNTAwMDBcbiAgICBzcHJlYWRpbmdfZmFjdG9yPTdcbiAgXG4gICAgW2JhY2tlbmQuYmFzaWNfc3RhdGlvbi5jb25jZW50cmF0b3JzLmZza11cbiAgICBmcmVxdWVuY3k9ODY4ODAwMDAwXG5cIlwiXCJcblxuW1tjb25maWcubW91bnRzXV1cbnNlcnZpY2VOYW1lID0gXCJtb3NxdWl0dG9cIlxuZmlsZVBhdGggPSBcIi9tb3NxdWl0dG8vY29uZmlnL21vc3F1aXR0by5jb25mXCJcbmNvbnRlbnQgPSBcIlwiXCJcbmxpc3RlbmVyIDE4ODNcbmFsbG93X2Fub255bW91cyB0cnVlXG5cIlwiXCJcblxuW1tjb25maWcubW91bnRzXV1cbnNlcnZpY2VOYW1lID0gXCJwb3N0Z3Jlc1wiXG5maWxlUGF0aCA9IFwiL3Bvc3RncmVzcWwvaW5pdGRiLzAwMS1jaGlycHN0YWNrX2V4dGVuc2lvbnMuc2hcIlxuY29udGVudCA9IFwiXCJcIlxuIyEvYmluL2Jhc2hcbnNldCAtZVxuXG5wc3FsIC12IE9OX0VSUk9SX1NUT1A9MSAtLXVzZXJuYW1lIFwiJFBPU1RHUkVTX1VTRVJcIiAtLWRibmFtZT1cIiRQT1NUR1JFU19EQlwiIDw8LUVPU1FMXG4gICAgY3JlYXRlIGV4dGVuc2lvbiBwZ190cmdtO1xuICAgIGNyZWF0ZSBleHRlbnNpb24gaHN0b3JlO1xuRU9TUUxcblwiXCJcIlxuIgp9
```

## Links

`iot`,`lorawan`,`network-server`,`gateway`,`monitoring`

---

Version:`4`

Chief-OnboardingChief-Onboarding is a comprehensive, self-hosted onboarding and employee management platform designed for businesses to streamline their onboarding processes.

ChromiumChromium is an open-source browser project that is designed to provide a safer, faster, and more stable way for all users to experience the web in a containerized environment.

### On this page

ConfigurationBase64LinksTags