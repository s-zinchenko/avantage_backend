from typing import Any, Optional

from django_serializer.v2.serializer import ModelSerializer
from marshmallow import pre_dump

from avantage_backend.cooperation.models import (
    Partner,
    Rating,
)


class PartnerItemSerializer(ModelSerializer):
    class SMeta:
        model = Partner
        fields = ("logo",)

    @pre_dump
    def prepare(self, obj: Partner, **kwargs: Optional[Any]) -> Partner:
        obj.logo = obj.logo.url
        return obj


class RatingItemSerializer(ModelSerializer):
    class SMeta:
        model = Rating
        fields = ("logo",)

    @pre_dump
    def prepare(self, obj: Rating, **kwargs: Optional[Any]) -> Rating:
        obj.logo = obj.logo.url
        return obj
