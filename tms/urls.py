from django.urls import path
from tms.views import CustomAuthToken
from tms.views import CountryView
from tms.views import AccountView

urlpatterns = [
    path('login/', CustomAuthToken.as_view()),
    path('countries', CountryView, basename='country'),
    path('accounts', AccountView, basename='account')
]
