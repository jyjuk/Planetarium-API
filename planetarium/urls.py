from django.urls import include, path
from rest_framework import routers

from planetarium.views import (
    ShowThemeViewSet,
    AstronomyShowViewSet,
    ShowSessionViewSet,
    PlanetariumDomeViewSet,
    ReservationViewSet
)

router = routers.DefaultRouter()


router.register("show_themes", ShowThemeViewSet)
router.register("astronomy_show", AstronomyShowViewSet)
router.register("show_session", ShowSessionViewSet)
router.register("planetarium_dome", PlanetariumDomeViewSet)
router.register("reservation", ReservationViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "planetarium"
