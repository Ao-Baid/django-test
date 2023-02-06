from django import forms
from crispy_forms import layout
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
    
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if not username and not password:
            raise forms.ValidationError('You have to write something!')

        return cleaned_data


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        email = cleaned_data.get('email')

        if not username and not password and not password2 and not email:
            raise forms.ValidationError('You have to write something!')

        if password != password2:
            raise forms.ValidationError('Passwords do not match!')

        return cleaned_data
    
