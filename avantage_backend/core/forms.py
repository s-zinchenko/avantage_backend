from django import forms

from avantage_backend.core.models import Award
from avantage_backend.share.forms import LangForm


class GetAwardsListForm(LangForm):
    show_on_main_page = forms.BooleanField(required=False)


class AwardFormAdmin(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        if (
            cleaned_data["show_on_main_page"] is True
            and Award.objects.filter(show_on_main_page=True).exists()
        ):
            raise forms.ValidationError(
                "На главной может выводиться только 1 награда"
            )

        return cleaned_data


class GetTeamListForm(LangForm):
    is_chief = forms.NullBooleanField(required=False)
