from django.urls import path
from tms.views import CustomAuthToken

urlpatterns = [
    path('login/', CustomAuthToken.as_view()),
    path('countries/', CountryView.as_view()),
    path('accounts/create', AccountCreate.as_view()),
    path('accounts/destroy', AccountDestroy.as_view()),
    path('accounts/list', AccountList.as_view()),
    path('accounts/detail', AccountList.as_view()),
    path('accounts/update', AccountList.as_view()),
]
