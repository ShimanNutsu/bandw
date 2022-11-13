import redis
import random
import string

class Run():
    def __init__(self, project: str, name: str = None) -> None:
        self.db = redis.StrictRedis(db=0, host='redishost')
        self.project = project
        if name is None:
            name = self._get_random_name()
        self.name = name

    def log(self, values: dict):
        for key in values:
            self.db.rpush(':'.join([self.project, self.name, key]), values[key])

    def _get_random_name(name_len=10):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=name_len))