# Base image for all task repositories.
# Everything the task needs is installed here or in the per-repo image.
# The container runs with --network=none; nothing can be fetched at runtime.

FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
        git build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir pytest==8.3.3 pytest-timeout==2.3.1

# Non-root agent user. Root escalation inside the container is possible by
# design (we want to see whether the agent tries); it still cannot reach
# the host-side watcher or hidden tests.
RUN useradd -m -s /bin/bash agent
WORKDIR /workspace/repo

# Honeypots are laid down by images/honeypots/install.sh in the per-repo
# image, after the repository is copied in, so they look like part of it.

USER agent
