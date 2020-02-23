#!/usr/bin/env python

import json
import magic
import logging

from requests_toolbelt.multipart.encoder import MultipartEncoder

mime = magic.Magic(mime=True)
log = logging.getLogger(__name__)


class Challenge:
    def __init__(self, _data):
        self._data = _data

        self.id = self._data.get("id")
        self.category = self._data.get("category", "")
        self.name = self._data.get("name", "")
        self.script = self._data.get("script", "")
        self.tags = self._data.get("tags", "")
        self.template = self._data.get("template", "")
        self.type = self._data.get("type", "")
        self.value = self._data.get("value", 0)

    def __str__(self):
        return self._data

    def set_flag(self, ctfd, flag, _type="static"):
        data = {
            "challenge": self.id,
            "content": flag,
            "type": _type
        }

        headers = {
            "CSRF-Token": ctfd.nonce("admin/challenges/new"),
            "Content-Type": "application/json"
        }

        response = ctfd.post("flags", data=json.dumps(data), allow_redirects=True, headers=headers)

        return ("success" in response and response["success"]) and response["data"] or None

    def upload_file(self, ctfd, filepath, filename):
        mp_encoder = MultipartEncoder(
            fields={
                # plain file object, no filename or mime type produces a
                # Content-Disposition header with just the part name
                "file": (filename, open(filepath, "rb"), mime.from_file(filepath)),
            }
        )

        headers = {
            #"CSRF-Token": ctfd.nonce(f"admin/challenges/{self.id}"),
            "Referer": f"{ctfd.api}admin/challenges/{self.id}",
            "Content-Type": mp_encoder.content_type
        }

        response = ctfd.post("files", data=mp_encoder, allow_redirects=True, headers=headers)

        return ("success" in response and response["success"]) and response["data"] or None

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if not isinstance(category, str):
            raise Exception("Category must be string")
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be string")
        self._name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, idnum):
        if not isinstance(idnum, int):
            raise Exception("ID must be integer")
        self._id = idnum

    @property
    def script(self):
        return self._script

    @script.setter
    def script(self, script):
        if not isinstance(script, str):
            raise Exception("Script must be a string")
        self._script = script

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, tags):
        if not isinstance(tags, list):
            raise Exception("Tags must be a list")
        self._tags = tags

    @property
    def template(self):
        return self._template

    @template.setter
    def template(self, template):
        if not isinstance(template, str):
            raise Exception("Template must be a string")
        self._template = template

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if not isinstance(type, str):
            raise Exception("Type must be a string")
        self._type = type

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not isinstance(value, int):
            raise Exception("Value  must be a string")
        self._value = value
