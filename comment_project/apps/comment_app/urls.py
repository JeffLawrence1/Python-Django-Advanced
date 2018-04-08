from django.conf.urls import url, include
from django.contrib import admin
from . import views

# def test(request):
#     print "app urls"

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^$', test),
    # url(r'^', include("apps.comment_app.urls")),
    url(r'^$', views.index),
    url(r'^add$', views.add),
]
