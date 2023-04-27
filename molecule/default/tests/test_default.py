import os
import pytest


@pytest.fixture(scope="module")
def ansible_vars(host):
    return host.ansible("include_vars", "./defaults/main.yml")["ansible_facts"]


def test_ansible_vars(host, ansible_vars):
    assert ansible_vars["MY_VAR"] == "1.0"  # for debugging ansible_vars


def test_package_version(host, ansible_vars):
    pkg = host.package("MY_PKG")
    assert pkg.is_installed
    # example tests
    assert pkg.version == ansible_vars["MY_VAR"]  # ansible default value
    assert pkg.version == os.environ["MY_VAR"]  # env var value
    assert pkg.version.startswith("1.0")  # hardcoded value


def test_service_running_and_enabled(host):
    service = host.service("MY_PKG")
    assert service.is_running
    assert service.is_enabled


def test_service_tcp_port(host):
    socket = host.socket("tcp://127.0.0.1:6443")
    assert socket.is_listening
