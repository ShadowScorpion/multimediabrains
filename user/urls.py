from django.conf.urls import url
from . import views

urlpatterns = [
#    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.register, name='register'),
    url(r'^(?P<username>\w+)/$', views.infobyuser, name='infobyuser')
]
