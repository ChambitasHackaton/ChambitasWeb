from django import forms
from usuarios.models import MyUser

class MyUserForm(forms.ModelForm):
	class Meta:
		model = MyUser
		fields = ['telephone','delegacion','zip_code']