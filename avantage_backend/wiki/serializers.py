from django_serializer.v2.serializer import ModelSerializer
from marshmallow import fields, pre_dump

from avantage_backend.wiki.models import Letter, Record


class RecordSerializer(ModelSerializer):
    class SMeta:
        model = Record
        fields = ("title", "external_link")


class WikiSerializer(ModelSerializer):
    class SMeta:
        model = Letter
        fields = ("value",)

    records = fields.Nested(RecordSerializer(), many=True)

    @pre_dump
    def prepare(self, obj, *args, **kwargs):
        obj.records = obj.record_set.all()
        return obj
