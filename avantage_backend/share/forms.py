from django import forms


class LangForm(forms.Form):
    lang = forms.ChoiceField(choices=[("ru", "ru"), ("en", "en")])
