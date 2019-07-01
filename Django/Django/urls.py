from django.conf.urls import include, url
from django.contrib import admin
from twitter.views import index_view, add_new_tweet_view, home_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', home_view, name='home'),
    url(r'^accounts/', include('django.contrib.auth.urls'), name='login'),
    url(r'^$', index_view, name='index'),
    url(r'^new_tweet/', add_new_tweet_view, name='add_new_tweet'),
]
