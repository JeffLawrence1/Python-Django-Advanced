from django.conf.urls import url, include
from django.contrib import admin
from . import views

# def test(request):
#     print "car_app urls"

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^$', test),
    url(r'^$', views.index),
    url(r'^/addcar$', views.addcar),
    url(r'^/caradd$', views.caradd),
    url(r'^/userD/(?P<user_id>\d+)$', views.userD),
]
