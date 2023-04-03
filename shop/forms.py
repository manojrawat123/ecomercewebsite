from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation
from shop.models import Customer


class MyUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={"class": "border-2 border-gray-700 pr-[2rem] rounded-lg outline-2 mr-[2rem] h-[2.5rem] w-[90%] outline-green-500 mb-2"}))
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={"class": "border-2 border-gray-700 pr-[2rem] rounded-lg outline-2 mr-[2rem] h-[2.5rem] w-[90%] outline-green-500 mb-2"}))
    class Meta:
        model = User
        fields = ["username", "email"]
        widgets = {
            "email": forms.TextInput(attrs={"class":"border-2 border-gray-700 pr-[2rem] rounded-lg outline-2 mr-[2rem] h-[2.5rem] w-[90%] outline-green-500 mb-2" }),
            "username": forms.TextInput(attrs={"class":"border-2 border-gray-700 pr-[2rem] rounded-lg outline-2 mr-[2rem] h-[2.5rem] w-[90%] outline-green-500 mb-2" })
        }
        label = {
            "email": "Email"
        }

class MyLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True, "class": "border-2 border-gray-700 pr-[2rem] rounded-lg outline-2 mr-[2rem] h-[2.5rem] w-[90%] outline-green-500 mb-2"}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "class": "border-2 border-gray-700 pr-[2rem] rounded-lg outline-2 mr-[2rem] h-[2.5rem] w-[90%] outline-green-500 mb-2"}),
    )

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "autofocus": True, "class": "border-2 border-gray-700 pr-[2rem] rounded-lg outline-2 mr-[2rem] h-[2.5rem] w-[90%] outline-green-500 mb-2"}
        ),
    )
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "border-2 border-gray-700 pr-[2rem] rounded-lg outline-2 mr-[2rem] h-[2.5rem] w-[90%] outline-green-500 mb-2"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "border-2 border-gray-700 pr-[2rem] rounded-lg outline-2 mr-[2rem] h-[2.5rem] w-[90%] outline-green-500 mb-2"}),
    )

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email", "class":
                                        "border-2 border-gray-700 pr-[2rem] rounded-lg outline-2 mr-[2rem] h-[2.5rem] w-[90%] outline-green-500 mb-2"}),
    )

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",
                                           "class": "border-2 border-gray-700 pr-[2rem] rounded-lg outline-2 mr-[2rem] h-[2.5rem] w-[90%] outline-green-500 mb-2"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",
                                           "class": "border-2 border-gray-700 pr-[2rem] rounded-lg outline-2 mr-[2rem] h-[2.5rem] w-[90%] outline-green-500 mb-2"}),
    )


class MyCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name","locality","city","state","zipcode"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "border-2 border-gray-700 pr-[2rem] rounded-lg outline-2 mr-[2rem] h-[2.5rem] w-[90%] outline-green-500 mb-2"}),
            "locality": forms.TextInput(attrs={"class": "border-2 border-gray-700 pr-[2rem] rounded-lg outline-2 mr-[2rem] h-[2.5rem] w-[90%] outline-green-500 mb-2"}),
            "city": forms.TextInput(attrs={"class": "border-2 border-gray-700 pr-[2rem] rounded-lg outline-2 mr-[2rem] h-[2.5rem] w-[90%] outline-green-500 mb-2"}),
            "state": forms.Select(attrs={"class": "border-2 border-gray-700 pr-[2rem] rounded-lg outline-2 mr-[2rem] h-[2.5rem] w-[90%] outline-green-500 mb-2"}),
            "zipcode": forms.NumberInput(attrs={"class": "border-2 border-gray-700 pr-[2rem] rounded-lg outline-2 mr-[2rem] h-[2.5rem] w-[90%] outline-green-500 mb-2"}),
            }
