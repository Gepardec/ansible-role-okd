okd
=========

install okd on CentOS based systems

Requirements
------------

None

Role Variables
--------------

'okd' role depends on 'docker' and 'oc' role. As such the variable(s) defined in those
roles can be used here as well.

'docker_user' specifies which user should be given access to run docker commands.
By default the value is "vagrant".

'okd_user' specifies which user should own the  docker commands.
By default the value is "vagrant".

'okd_oc_client_version' specifies the okd version for which the client binary gets
installed and conesquently the cluster version that derives the version from the
client.

'okd_public_hostname' specifies the public hostname through which okd is reachable.
e.g. myhostname results in following URL for the console
https://myhostname:8443/console

Dependencies
------------

- gepardec.docker

Example Playbook
----------------
- hosts: servers
  roles:
  - { role: okd, docker_user: vagrant,  okd_okd_oc_client_version: "v3.11.0-0cbc58b", okd_public_hostname: localhost }

License
-------

GPLv3

Author Information
------------------

Clemens Kaserer (clemens.kaserer@gepardec.com)