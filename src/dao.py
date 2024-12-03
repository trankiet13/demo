import hashlib
from src import app, db
from src.models import Account


def auth_user(username, password, role=None):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

    u = Account.query.filter(Account.username.__eq__(username),
                          Account.password.__eq__(password))

    if role:
        u = u.filter(Account.user_role.__eq__(role))

    return u.first()

def get_user_by_id(id):
    return Account.query.get(id)