from django.shortcuts import render, redirect
    # Create your views here.
def index(request):
		print "Debug"
		return render(request, "secrets/index.html")
def post_comment(request):
	context= {
	"comments": commentshere
	}
	print '*'*50
	if request.method == "POST":
		request.session['comment'] = request.POST['comment']
		print ('newcomment')
		print '*' *50
		return redirect('/')
	else: 
		print ('I Broke!')