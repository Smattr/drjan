import os
import sqlite3

DEFAULT_FILE = '.drjan.db'
DEFAULT_PATH = [
    os.curdir,
    os.getenv('USERPROFILE') or os.getenv('HOME'),
    '/etc/drjan/',
]

def _create(filename):
    conn = sqlite3.connect(filename)
    cursor = conn.cursor()
    script = os.path.join(os.path.dirname(__file__), 'init.sql')
    f = open(script, 'r')
    cursor.executescript(f.read())
    f.close()
    conn.commit()
    cursor.close()
    conn.close()

class Database(object):
    def __init__(self, filename):
        if not filename:
            for p in DEFAULT_PATH:
                path = os.path.join(p, DEFAULT_FILE)
                if os.path.exists(path):
                    filename = path
                    break
        if not filename:
            filename = os.path.join(DEFAULT_PATH[0], DEFAULT_FILE)
        if not os.path.exists(filename):
            _create(filename)

        #self._conn = sqlite3.connect(
