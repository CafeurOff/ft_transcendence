from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MinLengthValidator

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
        widget=forms.CheckboxInput(attrs={
            'style': 'width: 5%; height: 5%;',
            'class': 'custom-checkbox',
        }),
        required=False

    )

class SignupForm(UserCreationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'style': 'width: 300px; height: 40px; font-family: "Montserrat"; font-size: 16px; background-color: rgba(198, 182, 182, 0.1); padding: 10px; border: none; border-radius: 7px; color: white;', 'class': 'form-control placeholder-style', 'placeholder': 'Nom d’utilisateur'}),
        required=True,
        max_length=20,
        min_length=1,
        error_messages={'required': 'Veuillez entrer au moins un nom d’utilisateur'},
        # validators=[
        #     RegexValidator(
        #         regex='^[a-zA-Z0-9]*$',
        #         message='Votre nom d’utilisateur ne doit contenir que des lettres et des chiffres',
        #     )
        # ]
    )
    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'style': 'width: 300px; height: 40px; font-family: "Montserrat"; font-size: 16px; background-color: rgba(198, 182, 182, 0.1); padding: 10px; border: none; border-radius: 7px; color: white;',
                                            'class': 'form-control placeholder-style',
                                            'placeholder': 'Mot de passe',
                                            'color': 'white'}),
        error_messages={'required': 'Veuillez entrer un mot de passe'},
        # validators=[
        #     MinLengthValidator(8, message='Votre mot de passe doit contenir au moins 8 caractères'),
        # ]
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'style': 'width: 300px; height: 40px; font-family: "Montserrat"; font-size: 16px; background-color: rgba(198, 182, 182, 0.1); padding: 10px; border: none; border-radius: 7px; color: white;', 'class': 'form-control placeholder-style', 'placeholder': 'Confirmer le mot de passe', 'color': 'white'}), # Ajout de la couleur du texte
    )

