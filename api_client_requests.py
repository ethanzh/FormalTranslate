import webapp2
from security import KEY

from apiclient.discovery import build


def api_client_request(sentence):
    data = sentence
    service = build('language', 'v1', developerKey=KEY)
    collection = service.documents()
    request = collection.analyzeSyntax(body=data)
    print("hello!!!!!")
    res = request.execute()
    print(res)
    return res


class ApiHandler(webapp2.RequestHandler):
    def get(self):

        self.response.write(api_client_request("test"))



app = webapp2.WSGIApplication([
    ('/api', ApiHandler)
], debug=True)