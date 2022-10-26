#!/usr/bin/python3
"""Contains initialization scripts for all models."""

import os
from pathlib import Path
from importlib import import_module
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()

def get_model(name):
    """Returns model with the given name"""

    models_path = os.path.dirname(os.path.realpath(__file__))
    for filename in os.listdir(Path(models_path).absolute()):
        if (not filename.startswith("__")):
            module_name = filename.split(".")[0]
            module = import_module("models.{}".format(module_name))
            try:
                return getattr(module, name)
            except AttributeError as ex:
                pass
    return None
