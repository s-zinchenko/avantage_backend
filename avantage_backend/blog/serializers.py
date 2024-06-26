from django_serializer.v2.serializer import ModelSerializer
from marshmallow import fields, pre_dump

from avantage_backend.blog.models import CaseAttachment
from avantage_backend.share.serializers import LangSerializer


class ArticleSerializer(LangSerializer):
    id = fields.Int()
    title = fields.Str()
    external_link = fields.Str()
    photo = fields.Str()
    article_order = fields.Int()


class CaseAttachmentSerializer(ModelSerializer):
    class SMeta:
        model = CaseAttachment
        fields = (
            "id",
            "is_main",
            "file",
            "content_type"
        )

    @pre_dump
    def prepare(self, obj, *args, **kwargs):
        obj.file = obj.file.url
        return obj


class CustomerSerializer(LangSerializer):
    id = fields.Int()
    name = fields.Str()
    type = fields.Str()


class CaseSerializer(LangSerializer):
    id = fields.Int()
    title = fields.Str()
    year = fields.Str()
    body = fields.Str()
    type = fields.Str()
    show_on_main_page = fields.Bool()
    cover_image = fields.Str()
    main_attachment_type = fields.Str()
    case_order = fields.Int()

    customer = fields.Nested(CustomerSerializer(), many=False)
    photos = fields.Nested(CaseAttachmentSerializer(), many=True)

    @pre_dump
    def prepare(self, obj, *args, **kwargs):
        data = {"photos": obj.caseattachment_set.all()}
        data.update(**super().prepare(obj, *args, **kwargs))
        data["main_attachment_type"] = obj.caseattachment_set.filter(is_main=True).first().content_type
        return data
