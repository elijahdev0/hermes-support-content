# Dokploy Compose API: Error Traces and Recovery Steps

## Error: "Github Provider not found"

### Full trace
```
Docker Compose Deployment: ❌
Error: Github Provider not found
```

### When it occurs
After calling `compose.create` with a raw compose file, then calling `compose.deploy`. The API created the compose object with `sourceType: "github"` even when the create payload specified `"raw"`.

### Root cause
The `compose.create` endpoint does not reliably respect the `sourceType` field. It defaults to `"github"` which triggers a path expecting a configured git provider. Since no git provider exists, the deploy fails.

### Fix
```
# After compose.create returns
full = compose.one({"composeId": new_id})
full["sourceType"] = "raw"
compose.update(full)
compose.deploy({"composeId": new_id})
```

### Key detail
Sending a partial update like `{"composeId": "...", "sourceType": "raw"}` to `compose.update` returns HTTP 200 but does NOT persist. You MUST send every field from `compose.one()`.

---

## Error: Application with this name already exists

### When it occurs
Creating a compose with an `appName` that's already in use in the same environment.

### Fix
Use a different `appName` or omit it and let the API generate one.

---

## Error: Unsafe example API key, starting warning-only server

### Full trace (container logs)
```
unsafe example API key configured; starting warning-only server
CLIProxyAPI Version: v7.2.41
API server started in UNSAFE production mode.
The server is operating with EXAMPLE API keys. This is NOT safe for production.
```

### When it occurs
The app's config.yaml contains example/placeholder API keys (e.g., `your-api-key-1`). The app detects these and starts a warning server instead of the actual proxy.

### Fix
In the docker-compose `command`, replace example keys with random values at startup:
```
sh -c '
  cp /app/config.example.yaml /app/config.yaml 2>/dev/null || true;
  if grep -q "your-api-key" /app/config.yaml 2>/dev/null; then
    sed -i "s/your-api-key-1/$(tr -dc A-Za-z0-9 </dev/urandom | head -c 32)/g" /app/config.yaml;
    sed -i "s/your-api-key-2/$(tr -dc A-Za-z0-9 </dev/urandom | head -c 32)/g" /app/config.yaml;
  fi;
  exec /app/start.sh
'
```

---

## compose.update silently ignores partial payloads

### Symptom
```
# This returns success but does NOT persist:
compose.update({"composeId": id, "sourceType": "raw"})
# → HTTP 200, but compose.one(id) still shows old sourceType
```

### Root cause
The `compose.update` endpoint treats omitted fields as "reset to default" rather than "keep current value". Only fields included in the request body are written; everything else gets re-saved from the previous persisted defaults.

### Fix
Always re-fetch the full object, modify, and re-send:
```
full = compose.one({"composeId": id})
full["sourceType"] = "raw"
compose.update(full)
```
