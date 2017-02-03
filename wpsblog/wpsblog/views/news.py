from django.shortcuts import render
from django.db import models
def news(request):
	return render(request,
		"news.html",
		{"count" : "5"},
		)