from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
    url("contact/",views.ContactView.as_view())



]