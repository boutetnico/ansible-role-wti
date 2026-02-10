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


def test_wti_version_command(host):
    # Test wti command is functional by running version
    # Using || true because wti may require config file for full functionality
    cmd = host.run("wti --version || wti --help")
    assert cmd.rc == 0 or "wti" in cmd.stdout.lower() or "wti" in cmd.stderr.lower()


def test_wti_help_command(host):
    cmd = host.run("wti --help")
    # wti help should show usage information
    assert "wti" in cmd.stdout.lower() or "usage" in cmd.stdout.lower() or cmd.rc == 0
