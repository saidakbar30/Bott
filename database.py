import sqlite3
from contextlib import closing

from config import DB_PATH


def _conn():
    return sqlite3.connect(DB_PATH)


def init_db():
    with closing(_conn()) as c:
        c.execute(
            """CREATE TABLE IF NOT EXISTS users(
                user_id INTEGER PRIMARY KEY,
                full_name TEXT,
                username TEXT,
                joined_at TEXT DEFAULT CURRENT_TIMESTAMP
            )"""
        )
        c.commit()


def add_user(user_id: int, full_name: str, username: str | None):
    with closing(_conn()) as c:
        c.execute(
            "INSERT OR IGNORE INTO users(user_id, full_name, username) VALUES (?,?,?)",
            (user_id, full_name, username),
        )
        c.commit()


def count_users() -> int:
    with closing(_conn()) as c:
        return c.execute("SELECT COUNT(*) FROM users").fetchone()[0]


def count_today() -> int:
    with closing(_conn()) as c:
        return c.execute(
            "SELECT COUNT(*) FROM users WHERE date(joined_at) = date('now')"
        ).fetchone()[0]


def all_user_ids() -> list[int]:
    with closing(_conn()) as c:
        return [r[0] for r in c.execute("SELECT user_id FROM users")]
