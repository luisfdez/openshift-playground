#!/bin/bash

export USER_ID=$(id -u)
export GROUP_ID=$(id -g)
grep /etc/passwd > "$HOME/passwd"
echo "jh_user:x:${USER_ID}:${GROUP_ID}:JupyterHub Server:${HOME}:/bin/bash" >> "$HOME/passwd"
export LD_PRELOAD=libnss_wrapper.so
export NSS_WRAPPER_PASSWD=${HOME}/passwd
export NSS_WRAPPER_GROUP=/etc/group

exec "/opt/conda/bin/jupyterhub"
