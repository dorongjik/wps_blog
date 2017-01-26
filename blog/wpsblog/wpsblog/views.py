#import requests
#import json
from django.http.response import HttpResponse
from django.conf import settings
#MVC Controller
def home(request):
    return HttpResponse("hello world")

def room(request, room_id):
    return HttpResponse("This is a room detail " + room_id)

def news(request):
    with open(settings.BASE_DIR + "/wpsblog/templates/news.html") as template:
        content = template.read()
    return HttpResponse(content)
        #    response = requests.get("https://watcha.net/home/news.json?page=1&per=50")
#    news_dict = json.loads(response.text)
#
#    content = "<h1>News</h1>" + \
#        "<p>This is news page.</p>" + \
#        "".join([
#            news["title"]
#            for news
#            in news_dict["news"]
#        ])
#
#    return HttpResponse(
#        content,
#        content_type = "application/json",
#    )
#    return HttpResponse("This is news")
