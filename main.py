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
import sentence_analyzer
import json_parser
import re
from textstat.textstat import textstat
import timeit
import time


class MainHandler(webapp2.RequestHandler):
    def get(self):

        self.response.write("""
        
        <html>
        <head></head>
        
        <body>
        
        <h1> Enter your sentence </h1>
        
        
        <form action="/submit" method="post">
        Message: <textarea rows="8" cols="80" name="msg"></textarea>
        
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
        
        <p> 100 = Least complex, 0 = Most complex </p>
        
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

            start = time.time()

            server_response = rest_requests.syntax_request(data)

            first_raw_list = []
            Word_list = json_parser.create_word_list(server_response)

            for i in range(0, len(Word_list)):
                first_raw_list.append(Word_list[i].content)

            hi = " ".join(first_raw_list)
            print(textstat.flesch_reading_ease(hi))

            self.response.write("<p>Initial: </p>" + hi)

            index_list = sentence_analyzer.create_index_list(Word_list)

            new_word_list = sentence_analyzer.word_replacer(index_list, Word_list)

            new_raw_list = []

            for i in range(0, len(new_word_list)):
                new_raw_list.append(new_word_list[i].content)

            singlestring = " ".join(new_raw_list)
            print(textstat.flesch_reading_ease(singlestring))
            self.response.write("<p>Final: </p>" + singlestring)

            end = time.time()

            print("REST if block " + str(end-start))


        elif request_type == "client":
            server_response = api_client_requests.make_api_client_request(data)
            self.response.write(server_response)

        self.response.write(

            "<p>Initial score: </p>" + str(textstat.flesch_reading_ease(hi)) +
            "<p>Final score: </p>" + str(textstat.flesch_reading_ease(singlestring))

        )


        self.response.write("""

        <button onclick="goBack()">Go Back</button>

        <script>
        function goBack() {
            window.history.back();
            }
        </script>


        """)


app = webapp2.WSGIApplication([
    ('/', MainHandler),

    ('/submit', SubmitHandler)
], debug=True)


