from django.conf.urls import url, include
from django.contrib import admin
from . import views
# def test(request):
#     print "apps urls"

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^', test),
    # url(r'^', include("apps.login_reg_app.urls")),
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^dashboard$', views.dashboard),
    url(r'^logout$', views.logout),
]
