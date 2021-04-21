# Nginx Split Testing Prototype

This repository contains a barebones Nginx configuration and can be used to prototype A/B testing.

# Setup

## Spin up Docker

```
docker run --rm --name nginx-prototype -v $PWD/content/geoip:/usr/share/nginx/geoip:ro -v $PWD/content/site:/usr/share/nginx/html/site:ro -v $PWD/nginx.conf:/etc/nginx/nginx.conf -p 8080:80 nginx:latest
```

## Spin up Python backend

For this particular prototype, Python's http server module is used to run a backend that Nginx can proxy to.

```
docker exec -it nginx-prototype bash
apt update && apt install -y python3 && cd /usr/share/nginx/html/site && python3 -m http.server 8080
```

# Testing

```
curl -X GET http://localhost:8080/us/ # `index`
curl -X GET -b 'split_www_home_group=b' http://localhost:8080/us/ # `Home-B`
```
