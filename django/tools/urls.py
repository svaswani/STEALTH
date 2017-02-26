from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^feed/$', views.feed, name='feed'),
    url(r'^login/$', views.login, name='login'),
    url(r'^chat/$', views.chat, name='chat'),
    url(r'^about/$', views.about, name='about'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^register/$', views.register, name='register'),
    url(r'^resources/$', views.resources, name='resources'),
    url(r'^splash/$', views.splash, name='splash'),
    url(r'^(?P<tool_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>\d+)/comment/$', views.add_comment, name='add_comment'),
    url(r'^create/$', views.CreateTool.as_view(success_url="/feed"), name='create'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.EditTool.as_view(success_url="/feed"), name='edit')
]
