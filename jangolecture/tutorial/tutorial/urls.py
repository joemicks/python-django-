"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from.import views
from tech.views import session_demo,relog
urlpatterns = [
    url(r'^login/$',views.login_redirect,name='login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^tech/',include('tech.urls')),
    url(r'^$',views.index,name='index'),
    url(r'^base/$',views.base,name='base'),
    url(r'^account/regform.html',views.register,name='register'),
    url('addUser',views.addUser,name='addUser'),
    url('addUser1',views.addUser1,name='addUser1'),
    url('savefirst',views.savefirst,name='savefirst'),
    url('saveupdate', views.saveupdate, name='saveupdate'),
    #url('logins',views.logins,name='logins'),
    url('sessions',session_demo,name='demos-sessions'),
    url('register_savefile_retreive', views.register_savefile_retreive, name='register_savefile_retreive'),
    url('regsiter',relog,name='relog'),
    url('dashboard1',views.dashboard11,name='dashboard11'),
    url('dashboard22',views.dashboard22,name='dashboard22'),
    url('template',views.template,name="template"),
    url('usercreation',views.edit_advance,name='edit_advance'),
    url('datatable',views.datatable,name='datatable'),
    url('District_save', views.District_save, name='District_save'),
    #url('save', views.save, name='save'),
    url('blood_save', views.blood_save, name='blood_save'),
    url('saveuser', views.saveuser, name="saveuser"),
    url('profile_views',views.profile,name='profile'),
    url('edit/<id>/',views.edit,name="edit" ),

    url(r'^mobiles/delete/(?P<pk>\d+)$', views.delete_mobile, name="delete_mobile"),
    url(r'^project/delete/(?P<pk>\d+)$', views.delete_project, name="delete_project"),

    url(r'^laptops/edit_item/(?P<pk>\d+)$',views.edit_laptop, name="edit_laptop"),
    url(r'^laptops/edit_item1/(?P<pk>\d+)$',views.edit_laptop1, name="edit_laptop1"),
    url(r'^laptops/edit_item2/(?P<pk>\d+)$',views.edit_views, name="edit_views"),
    url(r'^laptops/edit4/(?P<id>\d+)$', views.donation_money, name="donation_money"),
    url(r'^invoice/generate/(?P<pk>\d+)$', views.invoice_generate, name="invoice_generate"),
    url(r'^invoice/print/(?P<pk>\d+)$', views.invoice_print, name="invoice_print"),
    #url(r'^laptops/payment/(?P<pk>\d+)$', views.edit_view1, name="edit_view1"),

   # url(r'^laptops/edit_item1/(?P<pk>\d+)$', views.edit_viewproject, name="edit_viewproject"),

    url('homepage',views.homepage,name="homepage"),
    url('mainpage',views.mainpage,name="mainpage"),
    url('project_employe', views.project_employe, name="project_emps"),
     url('project_emps', views.project_emps, name="project_emps"),
    url('project_save', views.project_save, name="project_save"),
    url('project_view', views.project_view, name="project_view"),
   # url('donation_money',views.donation_money,name="donation_money"),
    url('profit_module',views.profit_loss1,name="profit_loss1"),
    url('profit_type',views.profit_type,name="profit_loss1"),
    url('donation_portal', views.donation_portal, name="donations"),
    #url('project_view1', views.edit_project_view, name="project_view"),
    #url('view',views.view,name="view")
    #url('upload', views.upload, name="upload"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
    #urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
