from django import forms

from .models import MyUser

# is_activated send_шessages

class ChangeUserinfoForm(forms.ModelForm):
#    email = forms.EmailField(required=True, label='Aдpec электронной почты')
    
    class Meta:
        model = MyUser
        fields = ('username', 'email', 'first_name', 'last_name')




