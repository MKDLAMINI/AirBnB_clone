#!/usr/bin/python3
"""Import FileStorage class from models.engine.file_storage."""
from models.engine.file_storage import FileStorage

def initialize_storage():
    """Initialie FileStorage instance and reload data."""
    global storage
    storage = FileStorage()
    storage.reload()


initialize_storage()
