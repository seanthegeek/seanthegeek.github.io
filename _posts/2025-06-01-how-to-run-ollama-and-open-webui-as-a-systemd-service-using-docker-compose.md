---
layout: post
title: How to run Ollama and Open WebUI as a systemd service using Docker Compose
date: 2025-06-01 12:42 -0400
description: You can host your own alterative to ChatGPT and access it on any device
image:
  path: /assets/images/llama-on-a-container-ship.webp
  alt: An AI-generated image using the flux-dev model and the prompt " A realistic photo of a llama standing on a container ship"
category: Guides
tags:
- AI
- LLMs
- Local LLMs
- Ollama
- Open WebUI
- Docker
---
I wanted to get started running Large Language Models (LLMs) on my own hardware to learn more about how they work and provide more privacy than a service like ChatGPT. [Ollama](https://ollama.com/) is an open source, easy to use backend for running local LLMs, and [Open WebUI](https://docs.openwebui.com/) provides a powerful ChatGPT-like interface to Ollama.

## What you'll need

- A [Turing](https://en.wikipedia.org/wiki/Turing_(microarchitecture)) generation or newer Nvidia GPU
- A Linux distribution on bare metal or on a VM with the GPU passed through
- The open source [Nvidia drivers](https://developer.nvidia.com/blog/nvidia-transitions-fully-towards-open-source-gpu-kernel-modules/)
  - `sudo apt-get install nvidia-open` on Debian-based distributions like Ubuntu
  - `sudo dnf module install nvidia-driver:open-dkms` on RHEL-based distributions
- [Docker](https://docs.docker.com/engine/install/)
- The [Nvidia Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)

GPUs with more video memory can use larger AI models, so a card with 24 GB of video memory or more is ideal. But even cards with a small amount of VRAM can can run small models like Gemma 3 1B (a text-only model with one billion parameters).

> Check for used or refurbished older models with high amounts of VRAM like the GeForce RTX 3090 or RTX A5000 on sites like eBay and serverpartdeals.com.
{: .prompt-tip }

## Why use Docker for Ollama?

The standard installation method for installing or upgrading Ollama on Linux is to execute an install script that gets downloaded via `curl` and piped to `sh`. The install script creates an `ollama` user, downloads the latest version of ollama, and creates a `systemd` service to run it at startup.

There are two problems with that approach.

- A script being downloaded and running commands as root should always be reviewed before running it
- The Open WebUI container cannot access Ollama, because on Linux Ollama only binds to `127.0.0.1` by default
  - This can be changed by setting `Environment="OLLAMA_HOST=172.17.0.1"` to the `[Service]` section of the service configuration
  - But this change would be overwritten each time the install script runs

Plus, I wanted to learn more about Docker anyway.

## Docker disadvantages

Using Docker for this does have a couple of disadvantages.

Docker can only use Nvidia GPUs, and the GPU must be reserved by a container, so the GPU cannot be shared across multiple Docker containers. That said, the GPU is still usable by the host outside of Docker. For example, I can run Stable Diffusion projects on the host outside of Docker when the GPU is reserved by ba Docker container but is not actively in use.

See the [Docker documentation](https://docs.docker.com/compose/how-tos/gpu-support/) for more details.

## Docker Compose configuration

With that covered, let's get started, First, create some directories.

```bash
sudo mkdir /opt/openwebui
sudo mkdir /opt/openwebui/ollama_custom
```

Then create the `docker-compose.yml` file.

```bash
sudo nano /opt/openwebui/docker-compose.yml
```

```yaml
services:
  ollama:
    image: ollama/ollama
    container_name: ollama
    restart: unless-stopped
    ports:
      - "127.0.0.1:11434:11434"
    volumes:
      - ollama:/root/.ollama # Used for Ollama backend storage
      # Used for building and testing custom models
      - type: bind
        source: ./ollama_custom
        target: /root/custom
    environment:
      OLLAMA_HOST: 0.0.0.0  # Allow access from other containers
    deploy:
     resources:
       reservations:
         devices:
           - driver: nvidia
             count: 1
             capabilities: [gpu]
  open-webui:
    image: ghcr.io/open-webui/open-webui
    container_name: open-webui
    restart: unless-stopped
    depends_on:
      - ollama
    ports:
      - "127.0.0.1:3000:8080"
    volumes:
      - open-webui:/app/backend/data
    environment:
      - OLLAMA_BASE_URL=http://ollama:11434
      - WEBUI_URL=https://chat.example.net
      - GLOBAL_LOG_LEVEL=WARNING
volumes:
  ollama:
  open-webui:
```

### The services section

#### The `ollama` Service

- `image: ollama/ollama`: Uses the official `ollama/ollama` Docker image, which contains the Ollama server.
- `container_name: ollama`:  Assigns the container a name of “ollama” for easier identification.
- `restart: unless-stopped`:  Ensures the container automatically restarts if it stops, unless you explicitly stop it.
- `ports: - "127.0.0.1:11434:11434"`: Exposes port `11434` of the container to port `11434` on your local machine'a loopback interface. This is the standard port used by Ollama for communication.
- `volumes: - ollama:/root/.ollama`:  This is crucial for persisting Ollama’s configuration and downloaded models.  It creates a named volume called `ollama` which mounts to `/root/.ollama` inside the container. This means that even if you stop or remove the container, your downloaded models and settings will be preserved.
- `volumes: - type: bind source: ./ollama_custom target: /root/custom`: This uses a *bind mount* to link a local directory named `ollama_custom` to `/root/custom` inside the container. I use this directory to build custom models for testing.
- `environment: OLLAMA_HOST: 0.0.0.0`: This sets the `OLLAMA_HOST` environment variable to `0.0.0.0`.  By default, Ollama will only listen for connections from `127.0.0.1`. Setting this to `0.0.0.0` makes the Ollama server accessible from *other* containers on the same Docker network, which is necessary for Open WebUI to connect to Ollama.
- `deploy`: This section reserves one GPU for the `ollama` container.

#### The `open-webui` Service

- `image: ghcr.io/open-webui/open-webui`: Uses the `open-webui` Docker image from the Ghcr.io registry.
- `container_name: open-webui`: Assigns the container a name of “open-webui”.
- `restart: unless-stopped`: Similar to Ollama, restarts automatically unless stopped.
- `depends_on: - ollama`:  This tells Docker Compose that `open-webui` *depends* on `ollama`. Docker Compose will ensure that the `ollama` container is started *before* the `open-webui` container.
- `ports: - "127.0.0.1:3000:8080"`:  Exposes port `8080` of the container to port `3000` the loopback interface on your local machine.  This is the port `open-webui` listens on for web traffic.
- `volumes: - open-webui:/app/backend/data`: Creates a named volume called `open-webui` and mounts it to `/app/backend/data` inside the container. This is used for storing data related to the `open-webui`’s backend.
- `environment: - OLLAMA_BASE_URL=http://ollama:11434`:  Sets the `OLLAMA_BASE_URL` environment variable to `http://ollama:11434`. This tells the `open-webui` container where to find the Ollama server. The use of `ollama` here is important; Docker Compose automatically resolves `ollama` to the correct IP address of the running `ollama` container.
- `environment: - WEBUI_URL=https://chat.example.net`:  Tells Open WebUI where it can be accessed at.
- `environment: - GLOBAL_LOG_LEVEL=WARNING`:  Sets the logging level to `WARNING` so that the logs are not flooded with websocket requests.

### The volumes Section

- The `ollama:` and `open-webui:` sections define named volumes.  Named volumes are managed by Docker and are the preferred approach for persistent data.

### Key relationships & flow

1. Docker Compose starts the `ollama` container first.
2. Once `ollama` is running, Docker Compose starts the `open-webui` container.
3. `open-webui` then communicates with  `ollama` to access and interact with LLMs.

## The systemd service

Configure a systemd service that will start the services defined `docker-compose.yml` at system boot.

```bash
sudo nano /etc/systemd/system/openwebui.service
```

```ini
[Unit]
Description=An extensible, feature-rich, and user-friendly self-hosted AI platform
Documentation=https://docs.openwebui.com/
Requires=docker.service network-online.target

[Service]
WorkingDirectory=/opt/openwebui
Type=oneshot
RemainAfterExit=yes
user=docker
group=docker

ExecStartPre=/usr/bin/docker compose pull --quiet
ExecStart=/usr/bin/docker compose up -d

ExecStop=/usr/bin/docker compose down

ExecReload=/usr/bin/docker compose pull --quiet
ExecReload=/usr/bin/docker compose up -d

[Install]
WantedBy=multi-user.target
```

Save the file, then run

```bash
sudo systemctl daemon-reload
sudo systemctl enable openwebui.service
sudo service openwebui start
```

This systend service is designed to pull the latest images every time it starts and restarts, so it might take a few minutes to start or restart. That is normal.

## Install and configure the nginx webserver

In the `docker-compose.yml` file, OpenWeb UI is configured to only listen on `127.0.0.1:3000` for security reasons. If you would like it to be accessible from outside hosts, you should install nginx and configure it as a reverse proxy using the following configuration, replacing `your_domain_or_IP` with the actual domain or IP address that you are .

```nginx
server {
    listen 80;
    listen [::]:80;
    server_name your_domain_or_IP;

    location / {
        # Add WebSocket support
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";

        proxy_pass http://127.0.0.1:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

        # (Optional) Disable proxy buffering for better streaming response from models
        proxy_buffering off;

        # (Optional) Increase max request size for large attachments and long audio messages
        client_max_body_size 20M;
        proxy_read_timeout 10m;
    }
}
```

For more details on setting up a nginx reverse proxy, see my [blog post](/posts/how-to-run-multiple-web-services-behind-one-public-ip-address/) on that topic.

> The nginx configuration settings for websockets support must be added to any internal or edge server proxying traffic for Open WebUI.
{: .prompt-warning }

## First visit

When you first visit Open WebUI in a browser, you will be prompted to enter an email address and password to create an administrator account.

After that, you will need to select a model. Click on the model picker, and type in the name of the model from [the Ollama Library](https://ollama.com/library) that you want to download and install, then click pull from Ollama.com. Once the model is installed, select it and start chatting!

## Sharing access with others

To share access with others, click on your initials in the top right, then click Admin Panel. From there, you will see the Users Overview page. Click on the + to add more users.

> Open WebUI supports different authentication methods, such as LDAP and Okta. See the documentation for more details.
{: .prompt-tip }

### Granting access to models

Out of the box, users you add won't have access to any models because all models have their visibility set to `Private` by default, meaning only those with explicit access other than admins can see the model. There are two ways to fix this:

- Create a group, assign users to it, and grant the group access to the model
- Set a the visibility of a model to `Public` so it can be seen by all users

To add user groups to the access list for a `Private` model or change the model's visibility to `Public`, navigate to the Admin Panel, click on Settings, Models, and then click on a model. Make changes, then click `Save & update`.
