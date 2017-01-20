import os
import codecs

c = get_config()



##
## Jupyterhub settings
##
c.LocalOpenShiftOAuthenticator.admin_users = {'lfernand'}

c.JupyterHub.log_level = 0
c.Application.log_level = 0
c.JupyterHub.debug_proxy = True
c.Spawner.debug = True
c.JupyterHub.cookie_secret_file = '/srv/jupyterhub/cookie_secret'
c.JupyterHub.db_url = '/srv/jupyterhub/jupyterhub.sqlite'
c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.proxy_api_ip = '0.0.0.0'
c.JupyterHub.hub_ip = '0.0.0.0'
c.JupyterHub.port = 8000
c.JupyterHub.cleanup_servers = os.environ['CLEANUP_SERVERS'] == True

##
## Authentication configuration
##

c.JupyterHub.authenticator_class = 'oauthenticator.openshift.LocalOpenShiftOAuthenticator'
c.LocalOpenShiftOAuthenticator.create_system_users = False
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
c.KubeSpawner.singleuser_image_spec = '172.30.88.184:5000/lfernand/minimal-notebook-img@sha256:ce91433af7ec5271c49dd69d919114197a31797db4ecc12e74a911c1a84c60c3'
c.KubeSpawner.mem_limit = '100M'
c.KubeSpawner.mem_guarantee='100M'
c.KubeSpawner.cpu_limit = 0.5
c.KubeSpawner.cpu_guarantee = 0.5
