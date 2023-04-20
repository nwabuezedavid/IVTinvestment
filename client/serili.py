from dataclasses import field
import imp
from msilib.schema import Class
from rest_framework import serializers
from . models import *

class Userajax(serializers.ModelSerializer):
    class Meta:
        model = clientUser
        fields ='__all__'
class CustomerchattingApi(serializers.ModelSerializer):
    class Meta:
        model = Customerchatting
        fields ='__all__'
                # fields = ['id', 'user',  'Kycverify',  'uudiUser', 'InvestorSection',  'payment',  'Clentsdeposit',  'Clentwithdraw', 'referLink', 'coderefer', 'profileImg', 'withdrawalable', 'Lockeddeposit',]
class ClentdepositAjax(serializers.ModelSerializer):
    class Meta:
        model = Clentdeposit
        fields ='__all__'
                # fields = ['id', 'user',  'Kycverify',  'uudiUser', 'InvestorSection',  'payment',  'Clentsdeposit',  'Clentwithdraw', 'referLink', 'coderefer', 'profileImg', 'withdrawalable', 'Lockeddeposit',]
class ClentwithdrawAjax(serializers.ModelSerializer):
    class Meta:
        model = Clentwithdraw
        fields ='__all__'
                # fields = ['id', 'user',  'Kycverify',  'uudiUser', 'InvestorSection',  'payment',  'Clentsdeposit',  'Clentwithdraw', 'referLink', 'coderefer', 'profileImg', 'withdrawalable', 'Lockeddeposit',]