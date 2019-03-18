from django.conf.urls import url
from .import views
from django.contrib.auth.views import login,logout
urlpatterns=[

    url(r'^login/$',login,{'template_name':'account/cpy_index_base.html'}),
    url(r'^logout/$', logout, {'template_name': 'account/logout.html'}),
    url(r'^reg/$', logout, {'template_name': 'account/regform.html'}),

      url(r'^profile/$',views.profile,name='profile'),
    url('register_savefile_retreive', views.register_savefile_retreive, name='register_savefile_retreive'),
    ]


