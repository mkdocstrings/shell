# mkdocstrings-shell

[![ci](https://github.com/mkdocstrings/shell/workflows/ci/badge.svg)](https://github.com/mkdocstrings/shell/actions?query=workflow%3Aci)
[![documentation](https://img.shields.io/badge/docs-mkdocs-708FCC.svg?style=flat)](https://mkdocstrings.github.io/shell/)
[![pypi version](https://img.shields.io/pypi/v/mkdocstrings-shell.svg)](https://pypi.org/project/mkdocstrings-shell/)
[![gitter](https://badges.gitter.im/join%20chat.svg)](https://app.gitter.im/#/room/#shell:gitter.im)

A shell scripts/libraries handler for mkdocstrings.
It uses [Shellman](https://github.com/pawamoy/shellman)
to collect documentation from shell scripts.

## Installation

```bash
pip install mkdocstrings-shell
```

## Configuration

In MkDocs configuration file:

```yaml title="mkdocs.yml"
plugins:
- mkdocstrings:
    default_handler: shell  # optional
```

The handler does not offer any option yet.

## Usage

Use *mkdocstrings* syntax to inject documentation for a script:

```md
::: relative/path/to/script
    handler: shell  
```

Specifying `handler: shell` is optional if you declared `shell`
as default handler in mkdocs.yml.
