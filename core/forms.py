from django import forms

from core.models import contact 

class ContactForm(forms.ModelForm):
    class Meta:
        model=contact
        fields =('name','email','phone','message')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'phone': forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}),
            # 'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),
            'message': forms.Textarea(attrs={'class':'form-control','placeholder':'Message'}),
        }