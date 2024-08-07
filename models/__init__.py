#!/usr/bin/python3
"""packages"""
import os

storage = None

def initialize_storage():
    global storage
    HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')

    if HBNB_TYPE_STORAGE == 'db':
        from models.engine.db_storage import DBStorage
        storage = DBStorage()
    else:
        from models.engine.file_storage import FileStorage
        storage = FileStorage()

    storage.reload()

# Call the function to initialize storage
initialize_storage()

