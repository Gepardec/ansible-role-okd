[![](https://img.shields.io/travis/com/gepardec/ansible-role-okd/master?style=flat-square)](https://travis-ci.com/gepardec/ansible-role-okd)
![gplv3](https://img.shields.io/badge/license-GPL%20v3.0-brightgreen.svg?style=flat-square)
![Maintenance](https://img.shields.io/maintenance/yes/2020?style=flat-square)
<p align="right">
<img alt="gepardec" width=100px src="https://www.gepardec.com/files/gepardec_logo_light_background@2000w.png">
</p>
<br>
<br>

# Ansible Role: OKD

An Ansible Role that installs okd 3.11 on centos based systems via oc cluster up. Once there is an OKD installation mechanism for okd 4.x we will update the role accordingly. At the time of writing this readme the roadmap for okd 4.x which includesan install mechanism for okd 4.x has been added to the [openshift/community](https://github.com/openshift/community) repo via  [pull request 55](https://github.com/openshift/community/pull/55) on 28.10.2019.

## Role Variables

`okd` role depends on `gepardec.docker` role. As such the variable(s) defined in those
roles can be used here as well.

`okd_adm_user` specifies which user should own the  docker commands.
By default the value is "vagrant".

`okd_oc_client_version` specifies the okd version for which the client binary gets
installed and conesquently the cluster version that derives the version from the
client.

`okd_public_hostname` specifies the public hostname through which okd is reachable.
e.g. myhostname results in following URL for the console: https://myhostname:8443/console

## Dependencies

required ansible galaxy roles

- gepardec.docker

## Example Playbook

```yaml
- hosts: all
  roles:
  - { role: gepardec.okd, okd_okd_oc_client_version: "v3.11.0-0cbc58b", okd_public_hostname: localhost, okd_adm_user: "admin" }
```