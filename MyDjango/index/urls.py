#index 的urls.py
from django.urls import path,re_path
from . import views
urlpatterns = [
    # path('',views.index),
    # path('login.html',views.login),
    # #添加带有字符类型、整形和slug的URL
    # path('<year>/<int:month>/<slug:day>',views.mydate),
    # re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2}).html',views.mydate),
    # re_path('(?P<year>[0-9]{4}).html',views.myyear,name='myyear'),
    # re_path('dict/(?P<year>[0-9]{4}.htm)',views.myyear_dict,{'month':'05'},name="myyear_dict"),
    # path('download.html',views.download),
    # #通用视图ListView
    path('index/',views.ProductList.as_view()),
    path('index/<id>.html',views.ProductList.as_view(),{'name':'phone'})

]