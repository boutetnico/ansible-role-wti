[![tests](https://github.com/boutetnico/ansible-role-wti/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-wti/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.wti-blue.svg)](https://galaxy.ansible.com/boutetnico/wti)

ansible-role-wti
===================

This role installs and configures [WebTranslateIt Synchronization Tool: wti](https://github.com/webtranslateit/webtranslateit).

Requirements
------------

Ansible 2.10 or newer.

Supported Platforms
-------------------

- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Debian - 12 (Bookworm)](https://wiki.debian.org/DebianBookworm)
- [Ubuntu - 22.04 (Jammy Jellyfish)](http://releases.ubuntu.com/22.04/)
- [Ubuntu - 24.04 (Noble Numbat)](http://releases.ubuntu.com/24.04/)

Role Variables
--------------

| Variable            | Required | Default             | Choices   | Comments                                 |
|---------------------|----------|---------------------|-----------|------------------------------------------|
| wti_dependencies    | true     |                     | list      | See `defaults/main.yml`.                 |
| wti_gem             | true     | `web_translate_it`  | string    |                                          |
| wti_gem_state       | true     | `present`           | string    |                                          |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - role: ansible-role-wti

Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
