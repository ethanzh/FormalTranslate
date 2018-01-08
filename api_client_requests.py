import webapp2
from security import KEY

from apiclient.discovery import build

service = build('language', 'v1', developerKey=KEY)
collection = service.documents()

data = {}
data['document'] = {}
data['document']['language'] = 'en'
data['document']['content'] = "Google, headquartered in Mountain View, unveiled the new \
                                Android phone at the Consumer Electronic Show. \
                                Sundar Pichai said in his keynote that users love \
                                their new Android phones."
data['document']['type'] = 'PLAIN_TEXT'

request = collection.analyzeSyntax(body=data)
res = request.execute()


class ApiHandler(webapp2.RequestHandler):
    def get(self):

        self.response.write(res)



app = webapp2.WSGIApplication([
    ('/api', ApiHandler)
], debug=True)