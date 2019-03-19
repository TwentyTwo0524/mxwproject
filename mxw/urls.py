from django.conf.urls import url

from mxw import views

app_name = '[mxw]'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^goods_des/$', views.goods_des, name='goods_des'),
    url(r'^login/$', views.login, name='login'),
    url(r'^loginout/$', views.loginout, name='loginout'),
    url(r'^register/$', views.register, name='register'),


    url(r'^addcart/$',views.addcart,name='addcart'),
    url(r'^changecarteslect/$',views.changecarteslect,name='changecarteslect')
]