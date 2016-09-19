from django.conf.urls import url
from . import views
urlpatterns = [
		url(r'^$', views.index, name="index"),
		url(r'postcomment', views.post_comment, name="post_comment")
	]
