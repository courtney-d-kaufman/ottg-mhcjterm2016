"""superlists URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
# from django.contrib import admin
from lists import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # views.home_page references the view
    # regular expression r'^$', matches an empty string
    # *** write tests and play around with why r'^$' works and not '/' but "" works
    # url(r'^$', views.home_page, name='home'),
    url(r'^$', views.home_page, name='home'),
    #url(r'^foo/$', views.foo, name='foo'),
    url(r'^lists/new$', views.new_list, name='new_list'),
    # (.+) defines the capture group
    url(r'^lists/(.+)/$', views.view_list, name="view_list"),
]

# ViewDoesNotExist: 'None' is not a callable or a dot-notation path
# We didn't give it a function, we gave it a non type
