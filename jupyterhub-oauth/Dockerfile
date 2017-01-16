FROM jupyterhub/jupyterhub

MAINTAINER Luis Fernández Álvarez <luis.fdezalv@gmail.com>

#
# Install libnss-wrapper
#
RUN echo "deb http://http.us.debian.org/debian unstable main non-free contrib" >> /etc/apt/sources.list && \
    echo "deb-src http://http.us.debian.org/debian unstable main non-free contrib" >> /etc/apt/sources.list && \
    echo "deb http://ftp.us.debian.org/debian/ unstable main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb-src http://ftp.us.debian.org/debian/ unstable main contrib non-free" >> /etc/apt/sources.list && \
    apt-get -y update && \
    apt-get install -y -t unstable libnss-wrapper && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

#
# Ensure a dynamic-uid friendly base environment
#
ENV JH_USER jhub
ENV JH_UID 1001
ENV CONDA_DIR /opt/conda
ENV PATH $CONDA_DIR/bin:$PATH
ENV SHELL /bin/bash
ENV HOME /home/$JH_USER

RUN useradd -m -s /bin/bash -N -u $JH_UID $JH_USER && \
    mkdir -p $CONDA_DIR && \
    chown $JH_USER $CONDA_DIR && \
    mkdir /srv/ephemeral

#
# Base should come already with /src/jupyterhub & /srv/jupyterhub
#
RUN chown -R $JH_USER:root /home/$JH_USER
RUN chown -R $JH_USER:root /src/jupyterhub
RUN chown -R $JH_USER:root /srv/jupyterhub
RUN chown -R $JH_USER:root /srv/ephemeral

#
# Use the Oauthenticator for OpenShift
#
RUN python3 -m pip install git+https://github.com/jupyterhub/oauthenticator.git@5d8d7bf1c031ad7a40ffe1a6ba018e18cf7fe6b6 && \
    pip install jupyterhub-kubespawner

WORKDIR /srv/ephemeral

ADD jupyterhub_config.py jupyterhub_config.py
ADD entrypoint.sh entrypoint.sh

RUN chmod 775 /srv/ephemeral/entrypoint.sh
RUN chmod 770 /srv/ephemeral

ENTRYPOINT ["/srv/ephemeral/entrypoint.sh"]
