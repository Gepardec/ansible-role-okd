import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_oc_binary(host):
    assert host.file("/usr/local/bin/oc").exists


def test_okd_folder(host):
    okd_home = host.file("/opt/okd")
    assert okd_home.exists
    assert okd_home.is_directory


# def test_okd_cluster(host):
#     host.process.get(user="root", comm="nginx")
