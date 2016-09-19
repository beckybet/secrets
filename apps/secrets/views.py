from django.shortcuts import render, redirect
    # Create your views here.
def index(request):
		print "Debug"
		return render(request, "secrets/index.html")
def post_comment(request):
	newcomment = request.POST['comment']
	print '*'*50
	print newcomment
	print '*'*50
	redirect ('/')