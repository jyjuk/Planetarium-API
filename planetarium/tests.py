from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from rest_framework.test import APIClient
from planetarium.models import (
    ShowTheme,
    AstronomyShow,
    ShowSession,
    PlanetariumDome
)
from planetarium.serializers import (
    AstronomyShowListSerializer,
    AstronomyShowDetailSerializer
)

PLANETARIUM_URL = reverse("planetarium:astronomyshow-list")
SHOW_SESSION_URL = reverse("planetarium:showsession-list")


def sample_astronomy_show(**params):
    defaults = {
        "title": "Sample show",
        "description": "Sample description",
        "show_theme": "Sample show theme"
    }
    defaults.update(**params)
    return AstronomyShow.objects.create(**defaults)


def sample_show_session(**params):
    planetarium_dome = PlanetariumDome.objects.create(
        name="Earth",
        rows=20,
        seats_in_row=20
    )
    defaults = {
        "show_time": "2024-11-01 12:00:00",
        "astronomy_show": None,
        "planetarium_dome": planetarium_dome
    }
    defaults.update(params)
    return ShowSession.objects.create(**defaults)


def image_upload_url(astronomy_show_id):
    return reverse(
        "planetarium:astronomy-show-upload-image",
        args=[astronomy_show_id]
    )


def detail_url(astronomy_show_id):
    return reverse("planetarium:astronomy-show-detail", args=astronomy_show_id)


class UnauthenticatedAstronomyShowApiTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_auth_required(self):
        res = self.client.get(PLANETARIUM_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
