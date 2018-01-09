import webapp2
import requests
import requests_toolbelt.adapters.appengine
from security import KEY

# Use the App Engine Requests adapter. This makes sure that Requests uses
# URLFetch.
requests_toolbelt.adapters.appengine.monkeypatch()

API_KEY = KEY


def create_endpoints():
    functions_list = ["analyzeSentiment", "analyzeEntities", "analyzeEntitySentiment", "analyzeSyntax", "classifyText"]

    functions_dict = {}

    for i in range(0, len(functions_list)):
        functions_dict.setdefault(functions_list[i], "https://language.googleapis.com/v1beta2/documents:" +  \
                            functions_list[i] + ("?key=" + API_KEY))

    return functions_dict


ENDPOINTS = create_endpoints()


TEST_DATA = {"document":
                {"type":"PLAIN_TEXT",
                "content":
                    "Google, headquartered in Mountain View, unveiled the new Android \
                    phone at the Consumer Electronic Show. Sundar Pichai said in his  \
                    keynote that users love their new Android phones."
                 }
        }


def syntax_request(sentence):

    return requests.post(url=ENDPOINTS.get('analyzeSyntax'), json=sentence)



syntax_request_variable = requests.post(url=ENDPOINTS.get('analyzeSyntax'), json=TEST_DATA)

entities_request = requests.post(url=ENDPOINTS.get('analyzeEntities'), json=TEST_DATA)
entities_json = entities_request.json()


class RestHandler(webapp2.RequestHandler):
    def get(self):

        print(1) #self.response.write(syntax_json)


app = webapp2.WSGIApplication([
    ('/rest', RestHandler)
], debug=True)