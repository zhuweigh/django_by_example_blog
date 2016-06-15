from django.conf.urls import url, include
from . import views
from .feeds import LatestPostsFeed

urlpatterns = [
url(r'^feed/$',LatestPostsFeed(),name='post_feed'),
url(r'^search/$', views.post_search, name='post_search'),
url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list,name='post_list_by_tag'),
url(r'^(?P<post>[-\w]+)/$',views.post_detail,name='post_detail'),url(r'^$', views.post_list, name='post_list'),
url(r'^(?P<post_id>\d+)/share/$', views.post_share,name='post_share'),
url(r'^$', views.post_list, name='post_list'),
        ]
#urlpatterns += [
 # url(r'^$', views.PostListView.as_view(), name='post_list'),
#url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',views.post_detail,name='post_detail'),
#]
