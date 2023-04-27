# Ansible Role: {NAME}

[![CI](https://github.com/trfore/ansible-role-{NAME}/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/trfore/ansible-role-{NAME}/actions/workflows/ci.yml)
[![CD](https://github.com/trfore/ansible-role-{NAME}/actions/workflows/cd.yml/badge.svg?branch=main)](https://github.com/trfore/ansible-role-{NAME}/actions/workflows/cd.yml)

A brief description of the role goes here.

### Install the Role

You can install this role with the Ansible Galaxy CLI:

```bash
ansible-galaxy role install trfore.{NAME}
```

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy role install -r requirements.yml`, using the format:

```yaml
---
roles:
  - trfore.{NAME}
```

## Requirements

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

## Role Variables

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

| Variable | Default | Description | Required |
| -------- | ------- | ----------- | -------- |
| x        | `1`     | x           | Yes      |

## Dependencies

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

## Example Playbook

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
- hosts: servers
  roles:
    - { role: username.rolename, x: 1 }
```

## License

MIT

## Author Information

Taylor Fore (https://github.com/trfore)

## References
