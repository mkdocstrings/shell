# mkdocstrings-shell

A shell scripts/libraries handler for mkdocstrings. It uses [Shellman](https://github.com/pawamoy/shellman) to collect documentation from shell scripts.

## Installation

```
pip install mkdocstrings-shell
```

## Configuration

In MkDocs configuration file:

mkdocs.yml

```
plugins:
- mkdocstrings:
    default_handler: shell  # optional
```

The handler does not offer any option yet.

## Usage

Use *mkdocstrings* syntax to inject documentation for a script:

```
::: relative/path/to/script
    handler: shell
```

Specifying `handler: shell` is optional if you declared `shell` as default handler in mkdocs.yml.

## Sponsors

## Example

Let say we have a script called `drag` in a scripts folder, enabling a drag-drop feature on the command-line.

View the script's contents:

```
#!/bin/bash

## \author Timothée Mazzucotelli / @pawamoy <dev@pawamoy.fr>

## \brief Save file paths in a buffer to move them somewhere else.
## \desc This tool lets you save file paths into a buffer before moving or copying
## them somewhere else. It acts like a drag-and-drop utility but for the command-line.
## It can be useful when you don't want to type the entire destination path and
## proceed in three or more steps instead, using shortcut commands to move around your
## filesystem, dragging files from multiple directories.

## \example Drag files from multiple directories, drop them in another:
## \example-code bash
##   cd ~/Documents
##   drag ThisPlaylist.s3u
##   cd ../Downloads
##   drag ThisTrack.ogg AndThisVideo.mp4
##   drag --drop ../project
## \example-description
## In this example, we simply move around in the filesystem, picking files in
## each of these directories. At the end, we drop them all in a specific
## directory.

## \example Define a convenient `drop` alias:
## \example-code bash
##   alias drop='drag -d'
##   drag file.txt
##   cd /somewhere/else
##   drop
## \example-description
## In this example, we define a `drop` alias that allows us to actually
## run `drag` then `drop` (instead of `drag --drop`).

## \exit 1 No arguments provided.

if [ $# -eq 0 ]; then
  shellman "$0"
  exit 1
fi

data_file="/tmp/dragdrop"

drop() {
  local dir="${2:-.}"
  local drop=$1
  [ ! -f "${data_file}" ] && { echo "drag (drop): no files list" >&2; exit 0; }
  while read -r f; do
    $drop -v "$f" "${dir}"
  done < "${data_file}"
  rm "${data_file}"
}

main() {
  case $1 in
    ## \option -h, --help
    ## Print this help and exit.
    -h|--help) shellman "$0"; exit 0 ;;
    ## \option -d, --drop [DIR]
    ## Drop the remembered files in the specified directory
    ## (defaul: current directory).
    -d|--drop)
      drop mv "$2"
      exit 0
    ;;
    ## \option -p, --copy [DIR]
    ## Copy (instead of move) the dragged files in the specified directory
    ## (defaul: current directory).
    -p|--copy)
      drop cp "$2"
      exit 0
    ;;
    ## \option -c, --clean
    ## Clean the currently dragged files list (this option does not delete any file).
    -c|--clean)
      rm "${data_file}" 2>/dev/null
      exit 0
    ;;
    ## \option -l, --list
    ## List the currently dragged files.
    -l|--list)
      cat "${data_file}" 2>/dev/null
      exit 0
    ;;
  esac

  for f; do
    if [ "${f:0:1}" = "/" ]; then
      echo "$f" >> "${data_file}"
    else
      echo "${PWD}/$f" >> "${data_file}"
    fi
  done
}

## \usage drag FILES
## \usage drag -d|-p [DIR]
## \usage drag -c|-l
main "$@"
```

*The documentation syntax used in this script is documented here: <https://pawamoy.github.io/shellman/usage/syntax/>.*

We can inject documentation for our script using this markup:

```
::: scripts/drag
    handler: shell
```

...which would render the following documentation:

## drag

Save file paths in a buffer to move them somewhere else.

**Usage**

```
drag FILES
```

```
drag -d|-p [DIR]
```

```
drag -c|-l
```

**Description**

This tool lets you save file paths into a buffer before moving or copying them somewhere else. It acts like a drag-and-drop utility but for the command-line. It can be useful when you don't want to type the entire destination path and proceed in three or more steps instead, using shortcut commands to move around your filesystem, dragging files from multiple directories.

**Options**

- `-h`, `--help`: Print this help and exit.
- `-d`, ``` --drop``[DIR] ```: Drop the remembered files in the specified directory (defaul: current directory).
- `-p`, ``` --copy``[DIR] ```: Copy (instead of move) the dragged files in the specified directory (defaul: current directory).
- `-c`, `--clean`: Clean the currently dragged files list (this option does not delete any file).
- `-l`, `--list`: List the currently dragged files.

**Exit Status**

- `1`: No arguments provided.

**Examples** *Drag files from multiple directories, drop them in another:*

```
cd ~/Documents
drag ThisPlaylist.s3u
cd ../Downloads
drag ThisTrack.ogg AndThisVideo.mp4
drag --drop ../project
```

In this example, we simply move around in the filesystem, picking files in each of these directories. At the end, we drop them all in a specific directory.

*Define a convenient `drop` alias:*

```
alias drop='drag -d'
drag file.txt
cd /somewhere/else
drop
```

In this example, we define a `drop` alias that allows us to actually run `drag` then `drop` (instead of `drag --drop`).

**Authors**

Timothée Mazzucotelli / @pawamoy [dev@pawamoy.fr](mailto:dev@pawamoy.fr)
