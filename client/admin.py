from django.contrib import admin
from . models import *



class clientUsers(admin.ModelAdmin):
    list_display = ('user',)

admin.site.register(clientUser, clientUsers)

class Clentdepositc(admin.ModelAdmin):
    list_display = ('transittionuudi',)

admin.site.register(Clentdeposit, Clentdepositc)

class paymentOptionmethodsv(admin.ModelAdmin):
    list_display = ('passwordkey','amount',)
    
    

admin.site.register(paymentOptionmethods, paymentOptionmethodsv)
admin.site.register(Kyc)
admin.site.register(Clentwithdraw)
admin.site.register(InvestmentPlan)
admin.site.register(Matualpay)
admin.site.register(CArdpay)
admin.site.register(PaymentOption)
admin.site.register(Customerchatting)
admin.site.register(referredUser)
admin.site.register(maturtyintreset)
admin.site.register(Clent_withdrawBy_transfer)
admin.site.register(maturtyinvite)
admin.site.register(websiteDetail)

# Register your models here. 
