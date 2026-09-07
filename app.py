from db import run_query


def list_active_users():
    return run_query("SELECT id, username FROM users WHERE active = 1")


def get_config():
    return {"debug": False}
