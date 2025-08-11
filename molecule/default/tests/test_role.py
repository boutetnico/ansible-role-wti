import pytest


@pytest.mark.parametrize("pkg", ["ruby-rubygems"])
def test_dependencies_installed(host, pkg):
    assert host.package(pkg).is_installed


def test_gem_binary_exists(host):
    gem = host.run("which gem")
    assert gem.rc == 0
    assert gem.stdout.strip() != ""


def test_wti_gem_installed_system_wide(host):
    cmd = host.run("gem list --local web_translate_it")
    assert cmd.rc == 0
    assert "web_translate_it" in cmd.stdout


def test_wti_command_exists(host):
    cmd = host.run("which wti")
    assert cmd.rc == 0
    assert cmd.stdout.strip() != ""
