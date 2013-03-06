"""
Fabric file for deployment of new code to production server. Example usage:

	fab deploy
"""

from fabric.api import env, run, sudo
from fabric.context_managers import cd

env.DEPLOY_DIR = 'johaneunyoung.com'
env.use_ssh_config = True
env.hosts = ['johaneunyoung.com']


def deploy():
	with cd(env.DEPLOY_DIR):
		run('git checkout -- .')
		run('git pull')
		run('make languages')
		sudo('service uwsgi restart')
