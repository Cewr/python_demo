"""定义 demo_app 的 URL 模式"""

from django.conf.urls import url
from . import views

app_name = 'demo_app'

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),

    # 显示所有主题
    url(r'^topics/$', views.topics, name='topics'),

    # 显示特定主题详情
    url(r'^topics/(?P<topic_id>\d+)/$', views.topicsAndItem, name='topics_item'),

    # 用于添加新主题的页面
    url(r'^new_topic/$', views.newTopic, name='new_topic'),

    # 用于添加新条目的页面
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.newEntry, name='new_entry'),

    # 用于编辑条目的页面
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.editEntry, name='edit_entry'),
]
