from django.urls import path
from tms.views import CustomAuthToken

urlpatterns = [
    path('/login', CustomAuthToken.as_view())
]
