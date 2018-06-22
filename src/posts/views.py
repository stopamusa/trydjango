# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

# Create your views here.


def post_create(request):
	return HttpResponse("<h1>Create</h1>")

def post_detail(request):
	# return HttpResponse("<h1>detail</h1>")
	context = {
		"title": "Detail"
	}
	return render(request, "index.html", context)

def post_list(request): #list items
	
	queryset = Post.objects.all()
	context = {
		"object_list": queryset,
		"title": "List"
	}
	return render(request, "index.html", context)
	# if request.user.is_authenticated():
	# 	context = {
	# 		"title": "My User List"
	# 	}
	# else:
	# 	context = {
	# 	"title": "List"
	# 	}
	
	# return HttpResponse("<h1>list</h1>")

def post_update(request):
	return HttpResponse("<h1>update</h1>")

def post_delete(request):
	return HttpResponse("<h1>delete</h1>")
