from django.conf.urls import url, include
from rest_framework import routers

from . import rest

router = routers.DefaultRouter()
router.register(r'casewhen', rest.CaseWhenViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]