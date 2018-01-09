from security import KEY
from apiclient.discovery import build


def make_api_client_request(sentence):
    data = sentence
    service = build('language', 'v1', developerKey=KEY)
    collection = service.documents()
    request = collection.analyzeSyntax(body=data)
    res = request.execute()
    return res

