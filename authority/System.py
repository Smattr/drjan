from . import Authority

USERS_FILE = '/etc/passwd'
GROUP_FILE = '/etc/group'

class System(Authority.Authority):
    def __init__(self):
        self._users = None
        self._groups = None

    def get_users(self):
        if self._users is None:
            self._users = []
            f = open(USERS_FILE, 'r')
            for line in f:
                fields = line.split(':')
                entry = {
                    'username':fields[0],
                    'name':fields[4].split(',')[0],
                    'uid':fields[2],
                    'gid':fields[3],
                    'source':'system'
                }
                self._users.append(entry)
            f.close()
        return self._users

    def get_groups(self):
        if self._groups is None:
            self._groups = []
            f = open(GROUP_FILE, 'r')
            for line in f:
                fields = line.split(':')
                entry = {
                    'group':fields[0],
                    'gid':fields[2],
                    'members':filter(None, fields[3].strip().split(',')),
                    'source':'system',
                }
                self._groups.append(entry)
            f.close()
        return self._groups

    def rescan(self):
        self._users = None
        self._groups = None
