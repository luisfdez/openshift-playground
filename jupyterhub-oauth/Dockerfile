FROM 172.30.88.184:5000/lfernand/jupyterhub

MAINTAINER Luis Fernández Álvarez <luis.fdezalv@gmail.com>

# Oauthenticator PR
RUN python3 -m pip install git+https://github.com/jupyterhub/oauthenticator.git@5d8d7bf1c031ad7a40ffe1a6ba018e18cf7fe6b6 && \
    pip install jupyterhub-kubespawner

# Create oauthenticator directory and put necessary files in it
RUN mkdir /srv/ephemeral
WORKDIR /srv/ephemeral
ADD jupyterhub_config.py jupyterhub_config.py
RUN chmod 700 /srv/ephemeral
