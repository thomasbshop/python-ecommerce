from django.conf.urls import url


# own

from .views import (
    SearchProductView
    )

urlpatterns = [
    url(r'^$', SearchProductView.as_view(), name="list"),
]

