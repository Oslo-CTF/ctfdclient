from .base import CTFBase
from .ctf import Team

import logging

log = logging.getLogger(__name__)


class Scoreboard(CTFBase):
    def fetch_scoreboard(self):
        log.debug("Retrieving scores...")

        for i in self._ctfd.get("scoreboard")["data"]:
            for x in self.scores:
                if x.name == i["name"]:
                    x.__init__(i)
                    break
            else:
                self.scores.append(Team(i))

    def update(self):
        self._reset()
        self.fetch_scoreboard()

        super(Scoreboard, self).__init__(self._ctfd, self.scores)

    def __init__(self, ctfd, _data=None):
        self._ctfd = ctfd
        self.scores = []
        
        super(Scoreboard, self).__init__(self._ctfd, _data)

        self.fetch_scoreboard()

    def __iter__(self):
        for x in self.scores:
            yield x
