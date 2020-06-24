from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('',views.Index.as_view(),name='index'),
    url(r'^user/(?P<pk>\d+)/messages$',views.messages,name='messages'),
    path('sendmsg',views.sendmessage,name='sendmsg'),
    path('reg',views.UserCreateView.as_view(),name='reg'),
    path('login',views.user_login,name='login'),
    path('logout',views.user_logout,name='logout'),
]