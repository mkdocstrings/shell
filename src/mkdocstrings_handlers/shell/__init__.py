"""Shell handler for mkdocstrings."""

from mkdocstrings_handlers.shell._internal.config import (
    ShellConfig,
    ShellInputConfig,
    ShellInputOptions,
    ShellOptions,
)
from mkdocstrings_handlers.shell._internal.handler import ShellHandler, get_handler

__all__ = [
    "ShellConfig",
    "ShellHandler",
    "ShellInputConfig",
    "ShellInputOptions",
    "ShellOptions",
    "get_handler",
]
