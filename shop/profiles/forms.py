from django import forms


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()
    username = forms.CharField(max_length=255)
    password = forms.CharField(
        min_length=8, widget=forms.PasswordInput()
    )
    repeat_password = forms.CharField(
        min_length=8, widget=forms.PasswordInput()
    )
    are_you_elder_18 = forms.BooleanField(required=False)
