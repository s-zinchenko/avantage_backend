from django import forms

from avantage_backend.blog.models import Case
from avantage_backend.share.forms import LangForm


class GetCaseListViewForm(LangForm):
    case_type = forms.ChoiceField(
        choices=((key, key) for key in list(Case.TypeEN)), required=False
    )
    show_on_main_page = forms.BooleanField(required=False)


class ValidateShowOnMainPageFormset(forms.BaseInlineFormSet):
    def clean(self):
        cleaned_data = super().clean()
        show_on_main_page_count = 0
        for form in self.forms:
            if form.cleaned_data.get("is_main"):
                show_on_main_page_count += 1

        if show_on_main_page_count != 1:
            raise forms.ValidationError(
                "Только одна запись может оказаться на главной странице"
            )

        return cleaned_data


class GetCaseViewForm(LangForm):
    id = forms.IntegerField()
