from django.conf.urls import include, url, patterns
from django.conf import settings
from django.contrib import admin
from usuarios.views import Index
from usuarios.views import logout, login, signup
from buscador.views import SearchResults


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Index.as_view(), name='index'),
    url(r'^accounts/login/', login, name="login"),
    url(r'^logout/', logout, name='logout'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^search/', SearchResults.as_view(), name='search_results'),
]