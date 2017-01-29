from django.comf import settings
from django.http.response import HttpResponse

def render(template_name, context):
    with open(settings.BASE_DIR) + "/wpsblog/templates/" + template_name + ".html", "r") as template:
        content = template.read()
        for key, value in context.items():
            content = content.replace(
                    "## " + key + " ##",
                    value,
                    )

    return HttpResponse(content)