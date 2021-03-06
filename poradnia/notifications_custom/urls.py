# -*- coding: utf-8 -*-

import notifications
from django.conf.urls import url

from . import views

urlpatterns = [url(r'^$', views.NotificationListView.as_view(), name='all'), ]

urlpatterns += [
    url(r'^unread$', notifications.views.unread, name='unread'),
    url(r'^mark-all-as-read$', notifications.views.mark_all_as_read, name='mark_all_as_read'),
    url(r'^mark-as-read/(?P<slug>\d+)$', notifications.views.mark_as_read, name='mark_as_read'),
    url(r'^mark-as-unread/(?P<slug>\d+)$', notifications.views.mark_as_unread, name='mark_as_unread'),
)
