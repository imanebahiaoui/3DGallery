from django.conf.urls import url
from viewer import views


urlpatterns = [
    url(r'^$', views.HomeView.as_view()),
]
