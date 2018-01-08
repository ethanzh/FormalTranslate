import webapp2
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
                    "Google, headquartered in Mountain View, unveiled the new Android phone at the Consumer Electronic Show. \
                     Sundar Pichai said in his keynote that users love their new Android phones."
                 }
        }

syntax_request = requests.post(url = SYNTAX_ENDPOINT, json=TEST_DATA)
syntax_json = syntax_request.json()

entities_request = requests.post(url = SYNTAX_ENDPOINT, json=TEST_DATA)
entities_json = entities_request.json()


class RestHandler(webapp2.RequestHandler):
    def get(self):

        self.response.write(syntax_json)



app = webapp2.WSGIApplication([
    ('/rest', RestHandler)
], debug=True)