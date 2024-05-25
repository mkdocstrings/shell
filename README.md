# mkdocstrings-shell

[![documentation](https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat)](https://mkdocstrings.github.io/shell/)
[![gitpod](https://img.shields.io/badge/gitpod-workspace-blue.svg?style=flat)](https://gitpod.io/#https://github.com/mkdocstrings/shell)
[![gitter](https://badges.gitter.im/join%20chat.svg)](https://app.gitter.im/#/room/#shell:gitter.im)

A shell scripts/libraries handler for mkdocstrings.
It uses [Shellman](https://github.com/pawamoy/shellman)
to collect documentation from shell scripts.

## Installation

This project is available to sponsors only, through my Insiders program.
See Insiders [explanation](https://mkdocstrings.github.io/shell/insiders/)
and [installation instructions](https://mkdocstrings.github.io/shell/insiders/installation/).

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
