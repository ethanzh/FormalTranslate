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


class MainHandler(webapp2.RequestHandler):
    def get(self):

        self.response.write("""
        
        <html>
        <head></head>
        
        <body>
        
        <h1> Enter your sentence </h1>
        
        
        <form action="/submit" method="post">
        Message: <input type="text" name="msg"><br>
        Complexity (1-10): <input type="text" name="complexity"><br>
        
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

        request_type = self.request.POST.get("api_type")

        data = {'document': {}}
        data['document']['language'] = 'en'
        data['document']['content'] = self.request.POST.get("msg")
        data['document']['type'] = 'PLAIN_TEXT'

        if request_type == "rest":
            server_response = rest_requests.syntax_request(data)
            self.response.write(server_response.text)

        elif request_type == "client":
            server_response = api_client_requests.make_api_client_request(data)
            self.response.write(server_response)


app = webapp2.WSGIApplication([
    ('/', MainHandler),

    ('/submit', SubmitHandler)
], debug=True)


