from rest_framework.routers import DefaultRouter
from .views import VerifyEmailView, VerifyEmailConfirmView

router = DefaultRouter()

router.register('verify-email', VerifyEmailView, basename='verify-email')
router.register('verify_email_confirm', VerifyEmailConfirmView, basename='verify-email-confirm')

urlpatterns = router.urls