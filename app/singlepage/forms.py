from django import forms

class UsernamesForm(forms.Form):        
    usernames = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'style': 'width: 300px; height: 40px; font-family: "Montserrat"; font-size: 16px; background-color: rgba(198, 182, 182, 0.1); padding: 10px; border: none; border-radius: 7px; color: white;', 'class': 'form-control placeholder-style', 'placeholder': 'Nom d’utilisateur'}),
        required=True,
        max_length=100,
        min_length=1,
        strip=True,
        error_messages={'required': 'Veuillez entrer au moins un nom d’utilisateur'}
    )


class PasswordForm(forms.Form):
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'style': 'width: 300px; height: 40px; font-family: "Montserrat"; font-size: 16px; background-color: rgba(198, 182, 182, 0.1); padding: 10px; border: none; border-radius: 7px;', 'class': 'form-control placeholder-style', 'placeholder': 'Mot de passe'}),
        required=True,
        max_length=100,
        min_length=1,
        strip=True,
        error_messages={'required': 'Veuillez entrer un mot de passe'}
    )


class RememberForm(forms.Form):
    remember = forms.BooleanField(
        label='',
        widget=forms.CheckboxInput(attrs={'style': 'width: 20px; height: 20px; margin-right: 10px; background-color: #262525;'}),  # Définir directement le style
        required=False
    )