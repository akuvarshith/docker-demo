# A small, simple FastAPI service packaged as a Docker image and published to AWS ECR

## Endpoints

| Path | What it returns |
|---|---|
| `/` | Hello message and version |
| `/health` | `{"status": "ok"}` (used for health checks) |
| `/info` | Hostname (container or pod name) and `APP_ENV` |
| `/items/{item_id}` | Example path parameter with type checking |

## Run locally with Docker

```bash
docker build -t fastapi-demo:1.0 .
docker run -d --name fastapi-demo -p 8000:8000 fastapi-demo:1.0 
curl http://localhost:8000/
```
## Use docker compose
### Set your own .env and host port

```bash
docker compose build
docker compose up -d
```

## clear
`docker compose down`

## Publish

- AWS ECR:  `aws ecr get-login-password | docker login`, `docker tag`, `docker push`


