from django_serializer.v2.serializer import ModelSerializer, Serializer
from marshmallow import fields, pre_dump

from avantage_backend.core.models import GalleryAttachment
from avantage_backend.share.serializers import LangSerializer


class AboutCompanySerializer(LangSerializer):
    greeting_title = fields.Str()
    greeting_description = fields.Str()
    about_image = fields.Str()
    about_text = fields.Str()
    intro_video = fields.Str()
    interview = fields.Str()
    years_of_experience = fields.Int()
    unique_scenarios = fields.Int()
    implemented_projects = fields.Int()
    welcome_video = fields.Str()
    presentation = fields.Str()


class GetCompanyFilesSerializer(Serializer):
    presentation = fields.Str()
    brief = fields.Str()
    agreement = fields.Str()
    requisites = fields.Str()
    portfolio = fields.Str()
    form_for_freelancers = fields.Str()
    contact_email = fields.Str()
    telegram = fields.Str()
    ok = fields.Str()
    vk = fields.Str()


class GetCompanyContactsSerializer(LangSerializer):
    address = fields.Str()
    contact_phone = fields.Str()
    contact_email = fields.Str()
    telegram = fields.Str()
    ok = fields.Str()
    vk = fields.Str()
    email_for_clients = fields.List(fields.Str())
    email_for_mass_media = fields.Str()
    email_for_partners = fields.Str()
    email_for_applicant = fields.Str()


class TeamMemberSerializer(LangSerializer):
    id = fields.Int()
    name = fields.Str()
    position = fields.Str()
    photo = fields.Str()
    is_chief = fields.Bool()


class GalleryAttachmentSerializer(ModelSerializer):
    class SMeta:
        model = GalleryAttachment
        fields = (
            "id",
        )
    photo = fields.Str()

    @pre_dump
    def prepare(self, obj, *args, **kwargs):
        obj.photo = obj.image.url
        return obj


class AwardSerializer(LangSerializer):
    id = fields.Int()
    year = fields.Int()
    title = fields.Str()
    place = fields.Str()
    nomination = fields.Str()
    event = fields.Str()
    attachment = fields.Str()
    show_on_main_page = fields.Str()
    award_order = fields.Int()
    case_link = fields.Str()
