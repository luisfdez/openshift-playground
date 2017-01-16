import os
import codecs

c = get_config()



##
## Jupyterhub settings
##

c.JupyterHub.log_level = 10
c.JupyterHub.cookie_secret_file = '/srv/jupyterhub/cookie_secret'
c.JupyterHub.db_url = '/srv/jupyterhub/jupyterhub.sqlite'
c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.hub_ip = '0.0.0.0'
c.JupyterHub.port = 8000
c.JupyterHub.cleanup_servers = os.environ['CLEANUP_SERVERS'] == True



##
## Authentication configuration
##

c.JupyterHub.authenticator_class = 'oauthenticator.openshift.LocalOpenShiftOAuthenticator'
c.LocalOpenShiftOAuthenticator.create_system_users = True
# OpenShift Hack - 
with codecs.open('/var/run/secrets/kubernetes.io/serviceaccount/token', 'r', encoding='utf-8') as secret:
        c.OpenShiftOAuthenticator.client_secret = secret.read()


##
## Spawner configuration
##

c.JupyterHub.spawner_class = 'kubespawner.KubeSpawner'
# OpenShift Hack - The downward API doesn't provide yet information about the service name
c.KubeSpawner.hub_connect_ip = os.environ["%s_SERVICE_HOST" % os.environ['SERVICE_NAME'].upper()]
c.KubeSpawner.start_timeout = 60 * 5 
c.KubeSpawner.singleuser_image_spec = 'openshift/minimal-notebook-img'
c.KubeSpawner.mem_limit = '100M'
c.KubeSpawner.mem_guarantee='100M'
c.KubeSpawner.cpu_limit = 0.5
c.KubeSpawner.cpu_guarantee = 0.5
