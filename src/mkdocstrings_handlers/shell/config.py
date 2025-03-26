"""Deprecated. Import from `mkdocstrings_handlers.shell` directly."""

# YORE: Bump 2: Remove file.

import warnings
from typing import Any

from mkdocstrings_handlers.shell._internal import config


def __getattr__(name: str) -> Any:
    warnings.warn(
        "Importing from `mkdocstrings_handlers.shell.config` is deprecated. Import from `mkdocstrings_handlers.shell` directly.",
        DeprecationWarning,
        stacklevel=2,
    )
    return getattr(config, name)
