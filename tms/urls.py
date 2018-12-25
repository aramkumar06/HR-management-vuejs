from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tms.views import CustomAuthToken
from tms.views import AccountsView
from tms.views import ClientsView
from tms.views import CountriesView
from tms.views import EarningsView
from tms.views import ProjectsView
from tms.views import SitesView

router = DefaultRouter()
router.register(r'accounts', AccountsView, 'accounts')
router.register(r'clients', ClientsView, 'clients')
router.register(r'countries', CountriesView, 'countries')
router.register(r'earnings', EarningsView, 'earnings')
router.register(r'projects', ProjectsView, 'projects')
router.register(r'sites', SitesView, 'sites')

urlpatterns = [
    path('login/', CustomAuthToken.as_view()),
    path('', include(router.urls))
]
