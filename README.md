# Ansible Role: omada_install

[![CI](https://github.com/trfore/ansible-role-omada-install/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/trfore/ansible-role-omada-install/actions/workflows/ci.yml)
[![CD](https://github.com/trfore/ansible-role-omada-install/actions/workflows/cd.yml/badge.svg)](https://github.com/trfore/ansible-role-omada-install/actions/workflows/cd.yml)

Install Omada SDN controller on RedHat/CentOS and Debian/Ubuntu.

This role installs the latest Omada SDN controller software using the latest tarball from https://www.tp-link.com/us/support/download/omada-software-controller/.

If you would like to manually download the tarball to your Ansible control host, download the `Omada_SDN_Controller_v5.*.*_Linux_x64.tar.gz`, to your `files` directory and set the following two variables in your playbook:

- `omada_tar_src: Omada_SDN_Controller_v5.*.*_Linux_x64.tar.gz`
- `omada_tar_src_remote: false`

See 'Example Playbooks' section for working examples. This role **does not configure the Omada controller**, it uses the default configuration values. It does set the service to run as a non-root user, you can change this by setting `omada_non_root: false`.

### Java Requirements

- Starting with Omada SDN `>=v5.15.20`, Java 17 is required and installed with this role.

### Install the Role

You can install this role with the Ansible Galaxy CLI:

```bash
ansible-galaxy role install trfore.omada_install
```

## Tested Platforms and Versions

- MongoDB Community: `7.0.x`
- Omada SDN: `5.x.x`
- CentOS Stream 9
- Debian 11 & 12
- Ubuntu 22.04

## Requirements

- MongoDB Community Edition, a role for installing it via a package manager is available - `trfore.mongodb_install`.
  - Omada SDN `< 5.14.20` only supported MongoDB 3 and 4.
  - Omada SDN `>=5.14.20` now supports up to MongoDB 7.
- Apache Commons Daemon, `jsvc >= 1.1.0`, a role for installing the **latest** binary is available - `trfore.jsvc`.
- You can install these roles by creating a `requirements.yml` file and running `ansible-galaxy install -r requirements.yml`.

  ```yaml
  # requirements.yml
  ---
  roles:
    - name: trfore.jsvc
    - name: trfore.mongodb_install
    - name: trfore.omada_install
  ```

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

| Variable                | Default    | Description                                                                    | Required  |
| ----------------------- | ---------- | ------------------------------------------------------------------------------ | --------- |
| omada_tar_src           | URL        | Omada SDN tar file, URL or relative path                                       | No        |
| omada_tar_src_remote    | `true`     | Boolean, `true` if downloading from URL                                        | No        |
| omada_tar_dir           | `/var/tmp` | Temporary directory on the target host for extracting and installing Omada SDN | No        |
| omada_tar_folder        | Automatic  | Determined from the `omada_tar_src` variable                                   | Automatic |
| omada_non_root          | `true`     | Boolean, configure Omada SDN to run as a non-root user                         | No        |
| omada_remove_tar_folder | `false`    | Boolean, remove the temporary directory on the remote host                     | No        |

OS specific variables are listed below, along with default values (see `vars/main.yml`):

| Variable           | Default                                       | Description                              | Required |
| ------------------ | --------------------------------------------- | ---------------------------------------- | -------- |
| omada_dependencies | `["curl", "openjdk-17-jre-headless"]`         | Required packages for Omada SDN (Debian) | No       |
| omada_dependencies | `["curl", "java-17-openjdk-headless.x86_64"]` | Required packages for Omada SDN (RHEL)   | No       |

## Dependencies

- Apache Commons Daemon, `jsvc >= 1.1.0`
- MongoDB Community Edition `mongodb-org >=4.4.0`

## Example Playbooks

```yaml
- hosts: servers
  become: true
  roles:
    - name: Install MongoDB Community
      role: trfore.mongodb_install

    - name: Install jsvc Binary
      role: trfore.jsvc

    - name: Install Omada SDN
      role: trfore.omada_install

  post_tasks:
    - name: Test Omada SDN Is Running
      tags: ["omada", "test"]
      ansible.builtin.uri:
        url: https://127.0.0.1:8043/login
        status_code: 200
        validate_certs: false
      register: result
      until: result.status == 200
      retries: 12
      delay: 10
```

- If you manually download the tar file.

```yaml
- hosts: servers
  become: true
  vars:
    omada_tar_src: Omada_SDN_Controller_v5.*.*_Linux_x64.tar.gz
    omada_tar_src_remote: false
  roles:
    - name: Install MongoDB Community
      role: trfore.mongodb_install

    - name: Install jsvc Binary
      role: trfore.jsvc

    - name: Install Omada SDN
      role: trfore.omada_install
```

## Depreciation Notice

- **Currently the role still has the ability to install onto Ubuntu 20.04 systems using the method below, however, given 20.04 is EOL this feature will be removed in a future major release and is no longer tested.**
- NOTE: For **Ubuntu 20.04** targets, this role installs **OpenJDK 17**. While `jsvc` is available via APT, it is `< 1.1.0` and will **only work with OpenJDK 8**. If you prefer to use this older version, set `omada_dependencies` to the following in your playbook (see 'Example Playbooks' section below):

  ```yaml
  omada_dependencies: ["curl", "openjdk-8-jre-headless", "jsvc"]
  ```

- If you would like to install OpenJDK JRE 8 and jsvc using APT (Ubuntu 20.04 Only)

```yaml
- hosts: servers
  become: true
  vars:
    omada_dependencies: ["curl", "openjdk-8-jre-headless", "jsvc"]
  roles:
    - name: Install MongoDB Community
      role: trfore.mongodb_install

    - name: Install Omada SDN
      role: trfore.omada_install
      when: ansible_distribution == 'Ubuntu'
```

## License

MIT

## Author Information

Taylor Fore (https://github.com/trfore)

## Related Roles

| Github                         | Ansible Galaxy           |
| ------------------------------ | ------------------------ |
| [ansible-role-jsvc]            | [trfore.jsvc]            |
| [ansible-role-mongodb-install] | [trfore.mongodb_install] |
| [ansible-role-omada-install]   | [trfore.omada_install]   |

## References

### Omada

- https://www.tp-link.com/us/support/download/omada-software-controller/
- https://www.tp-link.com/us/support/faq/3272/
- Run Omada SDN as non-root
  - https://www.tp-link.com/hk/support/faq/3583/
- Omada SDN Port List
  - https://www.tp-link.com/us/support/faq/865/
- Omada Controller - Site Migration
  - https://www.tp-link.com/us/omada-sdn/controller-upgrade/
  - https://www.tp-link.com/us/omada-sdn/controller-upgrade/#content-5_1_2

[ansible-role-jsvc]: https://github.com/trfore/ansible-role-jsvc
[trfore.jsvc]: https://galaxy.ansible.com/trfore/jsvc
[ansible-role-mongodb-install]: https://github.com/trfore/ansible-role-mongodb-install
[trfore.mongodb_install]: https://galaxy.ansible.com/trfore/mongodb_install
[ansible-role-omada-install]: https://github.com/trfore/ansible-role-omada-install
[trfore.omada_install]: https://galaxy.ansible.com/trfore/omada_install
