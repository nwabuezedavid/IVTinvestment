from django import forms


from .models import *

class profileimages(forms.ModelForm):
    class Meta:
        model = clientUser
        fields =[ "profileImg"]
class KycForm(forms.ModelForm):
    class Meta:
        model = Kyc
        fields =[ "front"]
class KycForm2(forms.ModelForm):
    class Meta:
        model = Kyc
        fields =[ "front2"]
    

    
