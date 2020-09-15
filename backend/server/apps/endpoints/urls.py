from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from ..endpoints.views import EndpointViewSet, MLAlgorithmStatusViewSet, MLRequestViewSet, PredictView

router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", EndpointViewSet, basename="endpoints")
router.register(r"mlalgorithms", MLAlgorithmStatusViewSet, basename="mlalgorithms")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")

urlpatterns = [
    url(r"^api/v1/", include(router.urls)),
    url(
        r'^api/v1(?P<endpoint_name>+)/predict$', PredictView.as_view(), name='predict'
    )
]