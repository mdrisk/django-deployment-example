from django.conf.urls import url
from lvl5app import views

#template URLS
app_name = 'lvl5app'

urlpatterns = [
    url(r'^register/$', views.register, name="register"),
    url(r'^user_login/$', views.user_login, name='user_login'),
]
