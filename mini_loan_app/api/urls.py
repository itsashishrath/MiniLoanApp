from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoanViewSet, RepaymentViewSet

router = DefaultRouter()
router.register(r'loans', LoanViewSet, basename='loan')
router.register(r'repayments', RepaymentViewSet, basename='repayment')

urlpatterns = [
    path('', include(router.urls)),
]
