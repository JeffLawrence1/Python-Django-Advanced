from django.conf.urls import url, include
from django.contrib import admin
from . import views

# def test(request):
#     print "belt app urls"

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^', test),
    url(r'^$', views.index),
    url(r'^addbookpage$', views.addbookpage),
    url(r'^addbook$', views.addbook),
    url(r'^reviewpage$', views.reviewpage),
    url(r'^reviewpage/(?P<book_id>\d+)$', views.reviewpage2),
    url(r'^user/(?P<user_id>\d+)$', views.user),
    url(r'^addreview/(?P<book_id>\d+)$', views.addreview),
    url(r'^delete/(?P<review_id>\d+)$', views.reviewdelete),
    
]
