from django_serializer.v2.serializer import Serializer
from marshmallow import pre_dump


class LangSerializer(Serializer):
    @pre_dump
    def prepare(self, obj, *args, **kwargs):
        lang = self.context["request"].GET["lang"]
        if lang == "en":
            data = obj.en
        else:
            data = obj.ru

        return data
