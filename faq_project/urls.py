from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from faq.views import FAQViewSet, home

router = DefaultRouter()
router.register(r'faqs', FAQViewSet, basename='faq')

urlpatterns = [
  path('admin/', admin.site.urls),
  path('api/', include(router.urls)),
  path('', home, name='home'),  # Add this line
]