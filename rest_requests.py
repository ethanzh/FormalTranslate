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
        functions_dict.setdefault(functions_list[i], "https://language.googleapis.com/v1beta2/documents:" + \
                                  functions_list[i] + ("?key=" + API_KEY))

    return functions_dict


ENDPOINTS = create_endpoints()


def syntax_request(sentence):
    return requests.post(url=ENDPOINTS.get('analyzeSyntax'), json=sentence).json()
