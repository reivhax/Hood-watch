from django.conf.urls import url
from .views import *

urlpatterns = [
    url('^$', home, name='home'),
    url('^editaccount/$', create_profile, name='create'),
    url('^myaccount/$', myprofile, name='view'),
    url('^new/home/$', create_neighbourhood, name='createhood'),
    url('^new/post/$', add_post, name='createpost'),
    url('^new/biz/$', create_biz, name='createbiz'),
    url('^join/(?P<neigh_id>\d+)$', join_neighbourhood, name='join'),
    url('^leave/(?P<neigh_id>\d+)$', leave_neighbourhood, name='left'),
    url('^delete/(?P<neigh_id>\d+)$', delete_neighbourhood, name='deletehood'),
    url('^edit/(?P<neigh_id>\d+)$', edit_neighbourhood, name='edithood'),
    url('^hoods/$', neighbourhoods, name='hoods'),
    url('^myhood/$', myhood, name='hoods'),
]