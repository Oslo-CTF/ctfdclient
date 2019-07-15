#!/usr/bin/env python

# Version

__version__ = "0.1"

# Cookie Name

COOKIE_PREFIX = "__cfduid"

# API Base

PREFIX = "/api/v1"

# API Paths

PATH = {}

ROUTES = {
    "challenges": "/challenges",
    "tags": "/tags",
    "awards": "/awards",
    "hints": "/hints",
    "flags": "/flags",
    "submissions": "/submissions",
    "scoreboard": "/scoreboard",
    "teams": "/teams",
    "users": "/users",
    "statistics": "/statistics",
    "files": "/files",
    "notifications": "/notifications",
    "configs": "/configs",
    "pages": "/pages",
    "unlocks": "/unlocks",
}

RESPONSE_CODES = {
    "200": "OK",
    "204": "No Content",
    "400": "The request was invalid or cannot be otherwise served. An accompanying error message will explain further.",
    "401": "Authentication credentials were missing or incorrect.",
    "403": "The request is understood, but it has been refused or access is not allowed",
    "404": "The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.",
    "409": "The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.",
    "429": "Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.",
    "500": "Something went wrong on the server.",
    "503": "Server is overloaded with requests. Try again later.",
}
