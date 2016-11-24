FROM jupyterhub/jupyterhub

MAINTAINER Luis Fernández Álvarez <luis.fdezalv@gmail.com>

# Oauthenticator PR
RUN python3 -m pip install git+https://github.com/luisfdez/oauthenticator.git@5c36617f67935634167edcc42fee61e15453f0d9 && \
    pip install jupyterhub-kubespawner

# Create oauthenticator directory and put necessary files in it
RUN mkdir /srv/ephemeral
WORKDIR /srv/ephemeral
ADD jupyterhub_config.py jupyterhub_config.py
RUN chmod 700 /srv/ephemeral
