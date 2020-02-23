#!/usr/bin/env python3

import json
import logging

from pprint import pprint

from .base import CTFBase
from .ctf import Challenge
from ..const import CHAL_URI


log = logging.getLogger(__name__)


class Challenges(CTFBase):
    def update(self):
        log.debug("Retrieving challenges...")
        self._reset()
        
        for i in self._ctfd.get("challenges")["data"]:
            for x in self.challenges:
                if x.name == i["name"]:
                    x.__init__(i)
                    break
            else:
                self.challenges.append(Challenge(i))
        
        super(Challenges, self).__init__(self._ctfd, self.challenges)

    def get(self, chall_id):
        if not isinstance(chall_id, int):
            raise TypeError("Challenge ID has to be an integer")
        
        info = self._ctfd.get(CHAL_URI.format(chall_id))["data"]
        
        if not info:
            return Exception("Challenge ID does not exist")
        
        return Challenge(info)

    def create(self, name=None, category=None, description=None, value=None, state=None, type=None):
        data = {
            "name": name,
            "category": category,
            "description": description,
            "value": value,
            "state": state,
            "type": type,
        }

        headers = {
            "CSRF-Token": self._ctfd.nonce("admin/challenges/new"),
            "Content-Type": "application/json"
        }

        response = self._ctfd.post("challenges", data=json.dumps(data), allow_redirects=True, headers=headers)
        success = "success" in response and response["success"]
        
        if success:
            chall_id = response["data"]["id"]
            return self.get(chall_id)

        return None

    def __init__(self, ctfd, _data=None):
        self._ctfd = ctfd
        self.challenges = []

        super(Challenges, self).__init__(self._ctfd, _data)

        self.update()

    def __iter__(self):
        for x in self.challenges:
            yield x
