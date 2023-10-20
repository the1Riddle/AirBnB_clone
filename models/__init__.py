#!/usr/bin/env python3
"""
	__init__ for models directory
"""
from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
