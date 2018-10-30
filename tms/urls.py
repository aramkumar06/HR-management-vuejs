from django.urls import path
from tms.views import CustomAuthToken

from tms.views import AccountsView
from tms.views import ClientsView
from tms.views import CountriesView
from tms.views import EarningsView
from tms.views import ProjectsView

urlpatterns = [
    path('login/', CustomAuthToken.as_view()),
    path('accounts', AccountsView),
    path('countries', CountriesView),
    path('clients', ClientsView),
    path('earnings', EarningsView),
    path('projects', ProjectsView),
]
