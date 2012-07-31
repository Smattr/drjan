import ConfigParser
import os

DEFAULT_FILE = '.drjan.conf'
DEFAULT_PATH = [
    os.curdir,
    os.getenv('USERPROFILE') or os.getenv('HOME'),
    '/etc/drjan/',
]

class Conf(object):

    # Monkey patched file object to deal with ConfigParser failing on indented
    # files. Grr...
    class _FakeFile(object):
        def __init__(self, filename):
            self._i = 0
            f = open(filename, 'r')
            self._lines = f.readlines()
            f.close()

        def readline(self):
            if self._i >= len(self._lines):
                return None
            else:
                s = self._lines[self._i]
                self._i += 1
                return s.strip()


    def __init__(self, filename):
        self._config = ConfigParser.SafeConfigParser()
        if not filename:
            for p in DEFAULT_PATH:
                path = os.path.join(p, DEFAULT_FILE)
                if os.path.exists(path):
                    filename = path
                    break
            if not filename:
                raise Exception('No valid configuration file found')
        f = Conf._FakeFile(filename)
        self._filename = filename
        self._config.readfp(f)

    def get(self, section, key):
        return self._config.get(section, key)

    def set(self, section, key, value):
        return self._config.set(section, key, value)
