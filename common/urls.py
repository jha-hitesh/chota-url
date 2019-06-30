from django.conf.urls import url
import common.views as common_views

app_name = 'common'

urlpatterns = [

	url(r'^get-short-url/$', common_views.URLMaps.as_view(), name='get-short-url'),
	url(r'^(?P<surl>[-\w]+)/$', common_views.URLMaps.as_view(), name='redirect-to-long-url'),
	url(r'^$', common_views.Home.as_view(), name='home'),
	]