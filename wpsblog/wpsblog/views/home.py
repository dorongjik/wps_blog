from django.shortcuts import render
from wpsblog.models import Post

def home(request):
	return render(request,
		"home.html",
		{
            "public_posts": Post.objects.public(),
            "ad_posts": Post.objects.ad(),
        },
		)