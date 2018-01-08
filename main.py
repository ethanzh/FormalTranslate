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

# Use the App Engine Requests adapter. This makes sure that Requests uses
# URLFetch.
requests_toolbelt.adapters.appengine.monkeypatch()

API_KEY = "AIzaSyDJYEdEXmQhAn9n_oR8D4v_0mXz_7atfH8"

SYNTAX_ENDPOINT = "https://language.googleapis.com/v1beta2/documents:analyzeSyntax"
SYNTAX_ENDPOINT += ("?key=" + API_KEY)

ENTITIES_ENDPOINT = "https://language.googleapis.com/v1beta2/documents:analyzeEntities"
ENTITIES_ENDPOINT += ("?key=" + API_KEY)

data = {"document":
            {"type":"PLAIN_TEXT",
             "content":
                    "Google, headquartered in Mountain View, unveiled the new Android phone at the Consumer Electronic Show.  Sundar Pichai said in his keynote that users love their new Android phones."
                 }
        }

# sending post request and saving response as response object

syntax_request = requests.post(url = SYNTAX_ENDPOINT, json=data)

syntax_json_data = syntax_request.json()

entities_json_data = requests.post(url = ENTITIES_ENDPOINT, json=data)

print_me = str(entities_json_data.text)


class MainHandler(webapp2.RequestHandler):
    def get(self):



        print(print_me)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
