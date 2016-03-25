from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.backwork import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'backend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

     url(r'^signup/$',views.signup, name="auth_login"),
)
