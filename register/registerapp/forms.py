from django import forms


class FormDataForm(forms.Form):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=255, required=True)
    last_name = forms.CharField(max_length=255, required=True)
    state = forms.CharField(max_length=255, required=True)
    
    subject_1 = forms.CharField(max_length=200,required=False)
    subject_2 = forms.CharField(max_length=200,required=False)
    subject_3 = forms.CharField(max_length=200,required=False)
    subject_4 = forms.CharField(max_length=200,required=False)
    subject_5 = forms.CharField(max_length=200,required=False)

    def clean(self):
        cleaned_data = super(FormDataForm, self).clean()
        email = cleaned_data.get('email')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        state = cleaned_data.get('state')
        subject_1 = cleaned_data.get('subject_1')
        subject_2 = cleaned_data.get('subject_2')
        subject_3 = cleaned_data.get('subject_3')
        subject_4 = cleaned_data.get('subject_4')
        subject_5 = cleaned_data.get('subject_5')

        if not email and not first_name and not last_name:
            raise forms.ValidationError('Fields cannot be empty')
    