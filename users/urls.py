from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import SignupView, LogoutView, HomeView, ProfileView


urlpatterns = [
    url(r'^signup/$', SignupView.as_view(), name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    url(r'^profile/$', ProfileView.as_view(), name='profile'),
    url(r'^$', HomeView.as_view(), name='home'),
]