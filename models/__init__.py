#!/usr/bin/python
"""init of modules package"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
