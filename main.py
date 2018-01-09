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
import rest_requests
import api_client_requests
import json_parser
import re


class MainHandler(webapp2.RequestHandler):
    def get(self):

        self.response.write("""
        
        <html>
        <head></head>
        
        <body>
        
        <h1> Enter your sentence </h1>
        
        
        <form action="/submit" method="post">
        Message: <textarea name="msg"></textarea>
        
        <select name="complexity">
          <option value="1">1</option>
          <option value="2">2</option>
          <option value="3">3</option>
        </select>    
        
        <select name="api_type">
          <option value="rest">REST</option>
          <option value="client">Client API</option>
        </select>    
        
        <input action type="submit" value="Submit">
        
        </form>
        
        </body>
        
        </html>
        
        """)


class SubmitHandler(webapp2.RequestHandler):
    def post(self):

        self.response.write("""
        
        <button onclick="goBack()">Go Back</button>

        <script>
        function goBack() {
            window.history.back();
            }
        </script>
        
        
        """)

        request_type = self.request.POST.get("api_type")
        complexity = self.request.POST.get("complexity")
        message = self.request.POST.get("msg")

        data = {'document': {}}
        data['document']['language'] = 'en'

        stripped = re.sub(r'[^\w\s]', '', message)

        data['document']['content'] = stripped
        data['document']['type'] = 'PLAIN_TEXT'

        if request_type == "rest":
            server_response = rest_requests.syntax_request(data)

            Word_list = json_parser.create_word_list(server_response)

            raw_word_list = json_parser.create_raw_word_list(Word_list)

            for i in range(0, len(Word_list)):
                self.response.write(Word_list[i].tag + " ")

        elif request_type == "client":
            server_response = api_client_requests.make_api_client_request(data)
            self.response.write(server_response)


app = webapp2.WSGIApplication([
    ('/', MainHandler),

    ('/submit', SubmitHandler)
], debug=True)


