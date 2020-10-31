from django.urls import include, path
from .router import router

urlpatterns = [path("api/v1/", include(router.urls))]
