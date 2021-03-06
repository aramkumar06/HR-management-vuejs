from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tms.views import CustomAuthToken
from tms.views import AccountsView
from tms.views import CountriesView
from tms.views import EarningsView
from tms.views import ReportsView
from tms.views import SitesView
from tms.views import UsersView
from tms.views import FinancialAccountsView
from tms.views import RewardsView

router = DefaultRouter()
router.register(r'accounts', AccountsView, 'accounts')
router.register(r'countries', CountriesView, 'countries')
router.register(r'earnings', EarningsView, 'earnings')
router.register(r'reports', ReportsView, 'reports')
router.register(r'sites', SitesView, 'sites')
router.register(r'users', UsersView, 'users')
router.register(r'financial_accounts', FinancialAccountsView, 'financial_accounts')
router.register(r'rewards', RewardsView, 'rewards')

urlpatterns = [
    path('login/', CustomAuthToken.as_view()),
    path('', include(router.urls))
]
