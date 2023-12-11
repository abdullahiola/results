from django import forms


class Emailform(forms.Form):
    email = forms.EmailField(required=True)

    def clean(self):
        cleaned_data = super(Emailform, self).clean()
        email = cleaned_data.get('email')

        if not email:
            raise forms.ValidationError('Email cannot be empty')

