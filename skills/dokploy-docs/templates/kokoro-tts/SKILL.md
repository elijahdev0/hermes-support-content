---
title: "Kokoro TTS | Dokploy"
source: "https://docs.dokploy.com/docs/templates/kokoro-tts"
category: dokploy-docs
created: "2026-06-25T17:21:50.891Z"
---

Kokoro TTS | Dokploy

# Kokoro TTS

Copy as Markdown

Dockerized FastAPI wrapper for the Kokoro-82M text-to-speech model with multi-language support and OpenAI-compatible endpoints.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  kokoro-tts:
    build:
      context: https://github.com/remsky/Kokoro-FastAPI.git#master
      dockerfile: docker/cpu/Dockerfile
    restart: unless-stopped
    ports:
      - 8880
    environment:
      - MODEL_PATH=/app/models
      - DEVICE=${DEVICE:-cpu}
      - HOST=0.0.0.0
      - PORT=8880
    volumes:
      - kokoro-models:/app/models
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8880/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 60s
volumes:
  kokoro-models:
```

```
[variables]
main_domain = "${domain}"
device = "cpu"

[config]
env = [
  "DEVICE=${device}",
  "MODEL_PATH=/app/models",
  "HOST=0.0.0.0",
  "PORT=8880",
  "PYTHONUNBUFFERED=1",
  "UV_SYSTEM_PYTHON=1"
]

[[config.domains]]
serviceName = "kokoro-tts"
port = 8880
host = "${main_domain}"
path = "/"

[[config.mounts]]
filePath = "README.md"
content = """# Kokoro TTS FastAPI

This template provides a Dockerized FastAPI wrapper for the Kokoro-82M text-to-speech model.

## Features

- Multi-language support (English, Japanese, Chinese)
- OpenAI-compatible speech endpoint
- CPU and GPU support
- Web interface for monitoring
- RESTful API with comprehensive documentation
- Streaming audio generation
- Word-level timestamps and phonemes

## Usage

- **Web Interface**: Access the web UI at `https://${main_domain}/web`
- **API Documentation**: Available at `https://${main_domain}/docs`
- **Health Check**: Monitor service health at `https://${main_domain}/health`

## Configuration

The service runs on port 8880 and supports both CPU and GPU inference.
For GPU support, ensure your Dokploy instance has NVIDIA GPU support enabled.

## API Endpoints

- `POST /v1/audio/speech` - Generate speech from text (OpenAI compatible)
- `POST /dev/captioned_speech` - Generate speech with timestamps
- `POST /dev/phonemize` - Convert text to phonemes
- `POST /dev/generate_from_phonemes` - Generate audio from phonemes
- `GET /health` - Health check endpoint
- `GET /docs` - Interactive API documentation
- `GET /web` - Web interface

## Model Information

- Model: Kokoro-82M
- License: Apache-2.0
- Repository: https://github.com/remsky/Kokoro-FastAPI
- HuggingFace Model: https://huggingface.co/hexgrad/Kokoro-82M

## Notes

- This template builds the image from source during deployment
- Uses CPU-optimized Dockerfile by default
- Initial build may take several minutes due to model download
- Ensure sufficient disk space for model storage
- For GPU support, change dockerfile path to `docker/gpu/Dockerfile` in docker-compose.yml
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBrb2tvcm8tdHRzOlxuICAgIGJ1aWxkOlxuICAgICAgY29udGV4dDogaHR0cHM6Ly9naXRodWIuY29tL3JlbXNreS9Lb2tvcm8tRmFzdEFQSS5naXQjbWFzdGVyXG4gICAgICBkb2NrZXJmaWxlOiBkb2NrZXIvY3B1L0RvY2tlcmZpbGVcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHBvcnRzOlxuICAgICAgLSA4ODgwXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIE1PREVMX1BBVEg9L2FwcC9tb2RlbHNcbiAgICAgIC0gREVWSUNFPSR7REVWSUNFOi1jcHV9XG4gICAgICAtIEhPU1Q9MC4wLjAuMFxuICAgICAgLSBQT1JUPTg4ODBcbiAgICB2b2x1bWVzOlxuICAgICAgLSBrb2tvcm8tbW9kZWxzOi9hcHAvbW9kZWxzXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTURcIiwgXCJjdXJsXCIsIFwiLWZcIiwgXCJodHRwOi8vbG9jYWxob3N0Ojg4ODAvaGVhbHRoXCJdXG4gICAgICBpbnRlcnZhbDogMzBzXG4gICAgICB0aW1lb3V0OiAxMHNcbiAgICAgIHJldHJpZXM6IDNcbiAgICAgIHN0YXJ0X3BlcmlvZDogNjBzXG52b2x1bWVzOlxuICBrb2tvcm8tbW9kZWxzOlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmRldmljZSA9IFwiY3B1XCJcblxuW2NvbmZpZ11cbmVudiA9IFtcbiAgXCJERVZJQ0U9JHtkZXZpY2V9XCIsXG4gIFwiTU9ERUxfUEFUSD0vYXBwL21vZGVsc1wiLFxuICBcIkhPU1Q9MC4wLjAuMFwiLFxuICBcIlBPUlQ9ODg4MFwiLFxuICBcIlBZVEhPTlVOQlVGRkVSRUQ9MVwiLFxuICBcIlVWX1NZU1RFTV9QWVRIT049MVwiXG5dXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImtva29yby10dHNcIlxucG9ydCA9IDg4ODBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcbnBhdGggPSBcIi9cIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuZmlsZVBhdGggPSBcIlJFQURNRS5tZFwiXG5jb250ZW50ID0gXCJcIlwiIyBLb2tvcm8gVFRTIEZhc3RBUElcblxuVGhpcyB0ZW1wbGF0ZSBwcm92aWRlcyBhIERvY2tlcml6ZWQgRmFzdEFQSSB3cmFwcGVyIGZvciB0aGUgS29rb3JvLTgyTSB0ZXh0LXRvLXNwZWVjaCBtb2RlbC5cblxuIyMgRmVhdHVyZXNcblxuLSBNdWx0aS1sYW5ndWFnZSBzdXBwb3J0IChFbmdsaXNoLCBKYXBhbmVzZSwgQ2hpbmVzZSlcbi0gT3BlbkFJLWNvbXBhdGlibGUgc3BlZWNoIGVuZHBvaW50XG4tIENQVSBhbmQgR1BVIHN1cHBvcnRcbi0gV2ViIGludGVyZmFjZSBmb3IgbW9uaXRvcmluZ1xuLSBSRVNUZnVsIEFQSSB3aXRoIGNvbXByZWhlbnNpdmUgZG9jdW1lbnRhdGlvblxuLSBTdHJlYW1pbmcgYXVkaW8gZ2VuZXJhdGlvblxuLSBXb3JkLWxldmVsIHRpbWVzdGFtcHMgYW5kIHBob25lbWVzXG5cbiMjIFVzYWdlXG5cbi0gKipXZWIgSW50ZXJmYWNlKio6IEFjY2VzcyB0aGUgd2ViIFVJIGF0IGBodHRwczovLyR7bWFpbl9kb21haW59L3dlYmBcbi0gKipBUEkgRG9jdW1lbnRhdGlvbioqOiBBdmFpbGFibGUgYXQgYGh0dHBzOi8vJHttYWluX2RvbWFpbn0vZG9jc2Bcbi0gKipIZWFsdGggQ2hlY2sqKjogTW9uaXRvciBzZXJ2aWNlIGhlYWx0aCBhdCBgaHR0cHM6Ly8ke21haW5fZG9tYWlufS9oZWFsdGhgXG5cbiMjIENvbmZpZ3VyYXRpb25cblxuVGhlIHNlcnZpY2UgcnVucyBvbiBwb3J0IDg4ODAgYW5kIHN1cHBvcnRzIGJvdGggQ1BVIGFuZCBHUFUgaW5mZXJlbmNlLlxuRm9yIEdQVSBzdXBwb3J0LCBlbnN1cmUgeW91ciBEb2twbG95IGluc3RhbmNlIGhhcyBOVklESUEgR1BVIHN1cHBvcnQgZW5hYmxlZC5cblxuIyMgQVBJIEVuZHBvaW50c1xuXG4tIGBQT1NUIC92MS9hdWRpby9zcGVlY2hgIC0gR2VuZXJhdGUgc3BlZWNoIGZyb20gdGV4dCAoT3BlbkFJIGNvbXBhdGlibGUpXG4tIGBQT1NUIC9kZXYvY2FwdGlvbmVkX3NwZWVjaGAgLSBHZW5lcmF0ZSBzcGVlY2ggd2l0aCB0aW1lc3RhbXBzXG4tIGBQT1NUIC9kZXYvcGhvbmVtaXplYCAtIENvbnZlcnQgdGV4dCB0byBwaG9uZW1lc1xuLSBgUE9TVCAvZGV2L2dlbmVyYXRlX2Zyb21fcGhvbmVtZXNgIC0gR2VuZXJhdGUgYXVkaW8gZnJvbSBwaG9uZW1lc1xuLSBgR0VUIC9oZWFsdGhgIC0gSGVhbHRoIGNoZWNrIGVuZHBvaW50XG4tIGBHRVQgL2RvY3NgIC0gSW50ZXJhY3RpdmUgQVBJIGRvY3VtZW50YXRpb25cbi0gYEdFVCAvd2ViYCAtIFdlYiBpbnRlcmZhY2VcblxuIyMgTW9kZWwgSW5mb3JtYXRpb25cblxuLSBNb2RlbDogS29rb3JvLTgyTVxuLSBMaWNlbnNlOiBBcGFjaGUtMi4wXG4tIFJlcG9zaXRvcnk6IGh0dHBzOi8vZ2l0aHViLmNvbS9yZW1za3kvS29rb3JvLUZhc3RBUElcbi0gSHVnZ2luZ0ZhY2UgTW9kZWw6IGh0dHBzOi8vaHVnZ2luZ2ZhY2UuY28vaGV4Z3JhZC9Lb2tvcm8tODJNXG5cbiMjIE5vdGVzXG5cbi0gVGhpcyB0ZW1wbGF0ZSBidWlsZHMgdGhlIGltYWdlIGZyb20gc291cmNlIGR1cmluZyBkZXBsb3ltZW50XG4tIFVzZXMgQ1BVLW9wdGltaXplZCBEb2NrZXJmaWxlIGJ5IGRlZmF1bHRcbi0gSW5pdGlhbCBidWlsZCBtYXkgdGFrZSBzZXZlcmFsIG1pbnV0ZXMgZHVlIHRvIG1vZGVsIGRvd25sb2FkXG4tIEVuc3VyZSBzdWZmaWNpZW50IGRpc2sgc3BhY2UgZm9yIG1vZGVsIHN0b3JhZ2Vcbi0gRm9yIEdQVSBzdXBwb3J0LCBjaGFuZ2UgZG9ja2VyZmlsZSBwYXRoIHRvIGBkb2NrZXIvZ3B1L0RvY2tlcmZpbGVgIGluIGRvY2tlci1jb21wb3NlLnltbFxuXCJcIlwiXG4iCn0=
```

## Links

`text-to-speech`,`ai`,`voice`,`fastapi`,`openai-compatible`

---

Version:`latest`

KitchenOwlKitchenOwl is a self-hosted grocery list and recipe manager.

Kokoro WebKokoro Web provides an interface for text-to-speech using advanced AI voice synthesis. It allows model caching and API integration with authentication.

### On this page

ConfigurationBase64LinksTags