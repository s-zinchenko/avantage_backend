import phonenumbers
from django.core.exceptions import ValidationError
from phonenumbers import NumberParseException, PhoneNumber


class ValidatePhoneMixin:
    def clean_contact_phone(self) -> dict:
        contact_phone = self.cleaned_data.get("contact_phone")
        self.validate_phone(contact_phone)
        return contact_phone

    def validate_phone(self, value: str) -> None:
        try:
            phone: PhoneNumber = phonenumbers.parse(value, "RU")
        except NumberParseException:
            raise ValidationError(
                "%(value)s является неверным телефоном", params={"value": value}
            )
        phone_is_valid = phonenumbers.is_valid_number(phone)
        if not phone_is_valid:
            raise ValidationError(
                "%(value)s является неверным телефоном", params={"value": value}
            )
