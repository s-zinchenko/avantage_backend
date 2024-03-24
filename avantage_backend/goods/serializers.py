from marshmallow import fields

from avantage_backend.share.serializers import LangSerializer


class ProductSerializer(LangSerializer):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    order = fields.Int()
    external_link = fields.Str()
    events = fields.Str()
