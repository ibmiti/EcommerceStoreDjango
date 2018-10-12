from django import forms
                                # to find more widgets go to https://docs.djangoproject.com/en/2.1/ref/forms/widgets/
class ContactForm(forms.Form):  # this widget appended here will add more styling to the form, that is all. redact it to see how it looks without it. it places the labels above the text fields and places 'place holder text within the fields'
    fullname = forms.CharField(widget=forms.TextInput(
                attrs={
                "class": "form-control",
                "placeholder": "Your full name"
                }
            )
        )

    email = forms.EmailField(
             widget=forms.EmailInput(
                    attrs={
                        "class": "form-control",
                        "placeholder": "Your email"
                    }
             )
    )
    content  = forms.CharField(widget=forms.Textarea(
                attrs={
                    'class': 'form-control',
                    "placeholder": "Your message"
                    }))


    def clean_email(self):  #what this will do is check if the email inputted into form is gmail, and if it isnt it will return a string (" has to be gmail.com") a validation
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")
        return email


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField()
    email    = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2= forms.CharField(label='Confirm password', widget=forms.PasswordInput)


def clean(self):
    data = self.cleaned_data
    password = self.cleaned_data.get('password')
    password2 = self.cleaned_data.get('password2')
    if password2 != password: # checking if pass word 2 and 1 are the same
        raise forms.ValidationError("Passwords must match.")
    return data
