# Contributing

## Contribute

### Setup a Dev Environment

```sh
python3 -m venv .venv && source .venv/bin/activate
python3 -m pip install -r requirements/dev-requirements.txt
pre-commit install
```

### Running Test

```sh
pre-commit run --all-files

# list environments and test
tox list
# lint all files
tox -e lint run

# run a specific test environment
tox -e py3.11-ansible2.19-ubuntu20-default run

# run all test in parallel
tox run-parallel

# run a group of test
tox -f ubuntu run-parallel

# pass Ansible Molecule args via Tox
tox -e py3.11-ansible2.19-ubuntu22-default run -- test --destroy=never
```

- For iterative development and testing, the tox molecule environments are written to accept `molecule` arguments. This allows for codebase changes to be tested as you write across multiple distros and versions of `ansible-core`.

```sh
# molecule converge
tox -e py3.11-ansible2.19-ubuntu22-default run -- converge -s default
# molecule test w/o destroying the container
tox -e py3.11-ansible2.19-ubuntu22-root -- test -s root-user --destroy=never
```

## Additional References

- [Ansible community guide](https://docs.ansible.com/ansible/devel/community/index.html)
- [Ansible Docs: `ansible-core` support matrix](https://docs.ansible.com/ansible/latest/reference_appendices/release_and_maintenance.html#ansible-core-support-matrix)
- [Github Docs: Forking a repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository)
- [MongoDB Docs: MongoDB Agent Compatibility Matrix](https://www.mongodb.com/docs/ops-manager/current/core/requirements/#operating-systems-compatible-with-the-mongodb-agent)
- [Omada Controller Forum](https://community.tp-link.com/en/business/forum/582)
- [RHEL: OpenJDK Life Cycle and Support Policy](https://access.redhat.com/articles/1299013)
