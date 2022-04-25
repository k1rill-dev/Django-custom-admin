from django.urls import path

from .views import *

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    # path('categories/<int:catid>', categories),
    # path('about/', about, name='about'),
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]