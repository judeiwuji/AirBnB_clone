#!/usr/bin/python3
"""Contains initialization scripts for all models."""

import os
from pathlib import Path
from importlib import import_module
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
