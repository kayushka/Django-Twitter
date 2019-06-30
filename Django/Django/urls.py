from django.conf.urls import include, url
from django.contrib import admin
from twitter.views import index_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_view),
]
