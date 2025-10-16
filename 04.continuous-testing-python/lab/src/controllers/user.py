# lab/src/controllers/user.py
from .. import dbclient

def create(user):
    # user is a dict
    username = user.get('username')
    if not username:
        return None, "Wrong user parameters"
    # check existing
    if dbclient.get(username):
        return None, "User already exists"
    # store only firstname/lastname as in original
    user_obj = {
        'username': username,
        'firstname': user.get('firstname'),
        'lastname': user.get('lastname')
    }
    dbclient.set(username, user_obj)
    return "OK", None

def get(username):
    user = dbclient.get(username)
    if not user:
        return None, "User not found"
    return user, None