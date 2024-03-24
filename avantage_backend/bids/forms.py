from django import forms

from avantage_backend.bids.models import CooperationBid
from avantage_backend.bids.validators import ValidatePhoneMixin


class CooperationBidCreateForm(ValidatePhoneMixin, forms.ModelForm):
    class Meta:
        model = CooperationBid
        fields = (
            "full_name",
            "contact_phone",
            "email",
            "project_scope",
            "project_goals",
        )

    agreement = forms.BooleanField()

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("agreement") is False:
            raise forms.ValidationError(
                "You must agree to the terms and conditions"
            )

        return cleaned_data
