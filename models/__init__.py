#!/usr/bin/python3
"""Contains initialization scripts for all models."""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
