from django.conf.urls import include, url, patterns
from django.conf import settings
from django.contrib import admin
from usuarios.views import Index
from usuarios.views import logout, login, signup

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Index.as_view(), name='home'),
    url(r'^accounts/login/', login, name="login"),
    url(r'^logout/', logout, name='logout'),
    url(r'^signup/$', signup, name='signup'),

]
