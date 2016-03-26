from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.backwork import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'backend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^signup/$',views.signup_user, name="auth_signup"),
	url(r'^signin/$',views.user_login, name="auth_login"),
	url(r'^verify_code/$',views.verify_code, name="verify_code")
)
