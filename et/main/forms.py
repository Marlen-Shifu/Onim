from django import forms
from .models import Offer
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm



class Add_offer(forms.ModelForm):
	
	class Meta:

		model = Offer

		fields = ['title', 'price', 'category', 'description', 'place', 'img']
		
			

class User_Registration_Form(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']



class User_Login_Form(AuthenticationForm):
	
	username = forms.CharField(label = 'Name')

	password = forms.CharField(label = 'Password', widget=forms.PasswordInput)