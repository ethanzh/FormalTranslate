#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


import webapp2
import json
import requests
import requests_toolbelt.adapters.appengine
from security import KEY

# Use the App Engine Requests adapter. This makes sure that Requests uses
# URLFetch.
requests_toolbelt.adapters.appengine.monkeypatch()

API_KEY = KEY

SYNTAX_ENDPOINT = "https://language.googleapis.com/v1beta2/documents:analyzeSyntax" + ("?key=" + API_KEY)
ENTITIES_ENDPOINT = "https://language.googleapis.com/v1beta2/documents:analyzeEntities" + ("?key=" + API_KEY)

TEST_DATA = {"document":
                {"type":"PLAIN_TEXT",
                "content":
                    "Google, headquartered in Mountain View, unveiled the new Android phone at the Consumer Electronic Show.  Sundar Pichai said in his keynote that users love their new Android phones."
                 }
        }

syntax_request = requests.post(url = SYNTAX_ENDPOINT, json=TEST_DATA)
syntax_json = syntax_request.json()

entities_request = requests.post(url = SYNTAX_ENDPOINT, json=TEST_DATA)
entities_json = syntax_request.json()


class MainHandler(webapp2.RequestHandler):
    def get(self):

        print(self.response.write(TEST_DATA['document']['content']))



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
