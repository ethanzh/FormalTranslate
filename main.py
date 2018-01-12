import webapp2
import rest_requests
import sentence_analyzer
import json_parser
import re


class MainHandler(webapp2.RequestHandler):
    def get(self):

        self.response.write("""
        
        <form action="/submit" method="post">
        
        Message: <textarea rows="8" cols="80" name="msg"></textarea>
        <input action type="submit" value="Submit">
        
        </form>
        
        """)


class SubmitHandler(webapp2.RequestHandler):
    def post(self):

        message = self.request.POST.get("msg")  # Get text from HTML element

        data = {'document': {}}
        data['document']['language'] = 'en'  # Starting to create the JSON object

        stripped = re.sub(r'[^\w\s]', '', message)  # Takes all the punctuation out. Come back to this later

        data['document']['content'] = stripped
        data['document']['type'] = 'PLAIN_TEXT'  # Finishes creating JSON object to be sent to REST API

        server_response = rest_requests.syntax_request(data)  # JSON object returned from REST API call

        original_text_list = []
        changed_text_list = []

        original_object_list = json_parser.create_word_list(server_response)  # List of word objects

        for i in range(0, len(original_object_list)):
            original_text_list.append(original_object_list[i].content)  # Makes a plain list of words

        original_string = " ".join(original_text_list)  # Makes one string of all the original words

        index_list = sentence_analyzer.create_index_list(original_object_list)  # Index of words to change

        changed_object_list = sentence_analyzer.word_replacer(index_list, original_object_list)

        for i in range(0, len(changed_object_list)):
            changed_text_list.append(changed_object_list[i].content)  # Makes plain list of changed words

        changed_string = " ".join(changed_text_list)  # String made from the new words

        self.response.write("<p>Initial: </p>" + original_string)
        self.response.write("<p>Final: </p>" + changed_string)

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


