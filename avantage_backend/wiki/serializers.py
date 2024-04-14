from django_serializer.v2.serializer import ModelSerializer, Serializer
from marshmallow import fields, pre_dump, post_dump

from avantage_backend.wiki.models import Letter, Record


class RecordSerializer(ModelSerializer):
    class SMeta:
        model = Record
        fields = ("title", "external_link")


class LetterSerializer(ModelSerializer):
    class SMeta:
        model = Letter
        fields = ("value",)

    records = fields.Nested(RecordSerializer(), many=True)

    @pre_dump
    def prepare(self, obj, *args, **kwargs):
        obj.records = obj.record_set.all()
        return obj


class WikiSerializer(Serializer):
    langs = fields.Dict(keys=fields.Str(), values=fields.Nested(LetterSerializer(), many=True))

    @post_dump(pass_original=True, pass_many=True)
    def prepare(self, obj, original, *args, **kwargs):
        res = {lang: [] for lang in Letter.Lang.values}
        for letter in original:
            if letter.lang:
                lang = letter.lang
            else:
                lang = Letter.Lang.RU.value

            res[lang].append(LetterSerializer().dump(letter))

        return {"langs": res}
