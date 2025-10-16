# lab/src/dbclient.py
# Simple in-memory DB client that mimics minimal Redis-like API used in tests.
_db = {}

def set(key, value):
    _db[key] = value
    return True

def get(key):
    return _db.get(key)

def flushdb():
    _db.clear()

def quit():
    # placeholder for compatibility
    pass