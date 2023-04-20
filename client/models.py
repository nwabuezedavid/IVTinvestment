import datetime
from django.db import models
from django.contrib.auth.models import User
from . genUid import genUdis,referCode 
# Create your models here.
class clientUser(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    Kycverify = models.OneToOneField('Kyc', blank=True, null=True,  on_delete=models.CASCADE)
    uudiUser = models.CharField( max_length=50, blank=True)
    InvestorSection = models.CharField( max_length=50, blank=True)
    payment = models.ForeignKey('paymentOptionmethods', blank=True, null=True, related_name='method', on_delete=models.CASCADE)
    Clentsdeposit = models.ManyToManyField('Clentdeposit', blank=True, )
    Clentwithdraw = models.ManyToManyField('Clentwithdraw', blank=True, )
    Clent_withdrawBy_transfermain = models.ManyToManyField('Clent_withdrawBy_transfer', blank=True, )
    referredfirend = models.ManyToManyField('referredUser', blank=True, )
    maturtyintresetc = models.ManyToManyField('maturtyintreset', blank=True, )
    referLink = models.CharField( max_length=500,blank=True, null=True)
    coderefer = models.CharField( max_length=500,blank=True)
    profileImg  = models.FileField( upload_to="clientProfilepic/", default='static/avatar_generic_118.png')
    withdrawalable = models.PositiveIntegerField(default="0",blank=True, null=True)
    Lockeddeposit = models.PositiveIntegerField(default="0",blank=True, null=True)
    earningforinvite = models.PositiveIntegerField(default="0",blank=True, null=True)
    earningforplan = models.PositiveIntegerField(default="0",blank=True, null=True)
    def save(self, *args, **kwargs):
        if self.uudiUser == "":
            code = genUdis()
            codes = referCode()
            self.uudiUser = code
            self.coderefer = codes
        super().save(*args, **kwargs)    
        
        
    
    
class Clentdeposit(models.Model):
    checkacc = models.CharField( max_length=50, blank=True, null=True)
    Bankname = models.CharField( max_length=50, blank=True, null=True)
    sendername = models.CharField( max_length=50, blank=True, null=True)
    senderamount = models.CharField( max_length=50, blank=True, null=True)
    transittionuudi = models.CharField( max_length=50, blank=True)
    dateDepsited = models.DateTimeField( auto_now_add=True,blank=True, null=True)
    update = models.DateTimeField( auto_now_add=True,blank=True, null=True)
    aproved = models.BooleanField(default=False)
    amount = models.PositiveIntegerField(default="0")
    plan = models.ForeignKey("InvestmentPlan", blank=True, null=True,  on_delete=models.CASCADE)
    isactive = models.BooleanField(default=False)

    
    

    def __str__(self):
        return f" the amount deposited {self.amount} and the id {self.transittionuudi} "
class referredUser(models.Model):
    user = models.OneToOneField(clientUser,  on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return str(self.date )
class maturtyintreset(models.Model):
    ids = models.CharField( max_length=50 ,blank=True, null=True)
    amount = models.PositiveIntegerField( blank=True, null=True)
    dated = models.DateTimeField(  auto_now_add=False)
    
    def __str__(self):
        return f" the maturity date is{str(self.dated )} and the amount to be added is {self.amount} "
class maturtyinvite(models.Model):
    ids = models.CharField( max_length=50 ,blank=True, null=True)
    amount = models.PositiveIntegerField( blank=True, null=True)
    dated = models.DateTimeField(  auto_now_add=False)
    
    def __str__(self):
        return f" the invite intreset  id{str(self.ids )} and the amount to be added is {self.amount} "


class Clent_withdrawBy_transfer(models.Model):
    
    wdbankname = models.CharField( max_length=50, blank=True)
    bankholdername = models.CharField( max_length=50, blank=True)
    wdamount = models.PositiveIntegerField(default="0", blank=True, null=True)
    accountnum = models.PositiveIntegerField(default="0")
    date = models.DateTimeField( auto_now_add=True,blank=True, null=True)
    aproved = models.BooleanField(default=False)
    

    
    

    def __str__(self):
        return f" the amount Withdraw {self.wdamount} and the name {self.wdbankname} "
 
class Clentwithdraw(models.Model):
    
    transittionuudi = models.CharField( max_length=50, blank=True)
    datewithdraw = models.DateTimeField( auto_now_add=True,blank=True, null=True)
    update = models.DateTimeField( auto_now_add=True,blank=True, null=True)
    amount = models.PositiveIntegerField(default="0")
    aproved = models.BooleanField(default=False)
    

    
    

    def __str__(self):
        return f" the amount Withdraw {self.amount} and the id {self.transittionuudi} "
 

class paymentOptionmethods(models.Model):
    publicKey = models.CharField( max_length=50, blank=True, null=True)
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    privateKey = models.CharField( max_length=50, blank=True, null=True)
    date = models.DateTimeField( auto_now=True)
    paymentName = models.CharField( max_length=50, blank=True, null=True)
    passwordkey = models.CharField( max_length=50, blank=True, null=True)
    amount = models.PositiveIntegerField(blank=True, null=True)
    payIcon = models.ImageField( upload_to="paymenImag", blank=True, null=True)

    

    def __str__(self):
        return self.paymentName

    
    
class Kyc(models.Model):
    front  = models.FileField( upload_to='KYC/', max_length=200,  blank=True, null=True)
    selectedName = models.CharField( max_length=50, blank=True, null=True)
    front2  = models.FileField( upload_to='KYC/', max_length=200, blank=True, null=True)
    dateUploaded = models.DateTimeField( auto_now_add=True)
    aproved = models.BooleanField(default=False)
    
class InvestmentPlan(models.Model):
    name = models.CharField( max_length=50)
    maturityDate = models.PositiveIntegerField( )
    minmuin = models.PositiveIntegerField()
    maxmuin = models.PositiveIntegerField()
    Percen = models.FloatField()
    icon  = models.ImageField( upload_to='plan/', max_length=200)
    dateUploaded = models.DateTimeField( auto_now_add=True)
    def __str__(self):
        return self.name
class websiteDetail(models.Model):
    name = models.CharField( max_length=50)
    domain = models.CharField( max_length=50 , blank=True, null=True)
    addressLocation = models.CharField( max_length=50,blank=True, null=True)
    facebook = models.URLField( max_length=500,blank=True, null=True)
    twitter = models.URLField( max_length=500,blank=True, null=True)
    instagram = models.URLField( max_length=500,blank=True, null=True)
    telegram = models.URLField( max_length=500,blank=True, null=True)
    unknowm = models.URLField( max_length=500,blank=True, null=True)
    gemail = models.URLField( max_length=500,blank=True, null=True)

    Phone = models.CharField( max_length=50)
    Logoicon  = models.ImageField( upload_to='logo/', max_length=200)
    dateUploaded = models.DateTimeField( auto_now_add=True)
    def __str__(self):
        return self.name

class Matualpay(models.Model):
    image = models.ImageField( upload_to="matualpay",blank=True, null=True)
    date = models.DateTimeField( auto_now_add=True, blank=True, null=True)
    name = models.CharField( max_length=50 , blank=True, null=True)
    bankname = models.CharField( max_length=50 , blank=True, null=True)
    AccNum = models.CharField( max_length=50 , blank=True, null=True)
    user = models.ForeignKey("clientUser",  on_delete=models.CASCADE, blank=True, null=True)
    active = models.BooleanField(default=False)

    

    def __str__(self):
        return self.name

class CArdpay(models.Model):
    userOption = models.ForeignKey("clientUser",  on_delete=models.CASCADE)
    firstname = models.CharField( max_length=50)
    email = models.CharField( max_length=50)
    expired = models.DateField( auto_now=False, auto_now_add=False)
    CardName = models.CharField( max_length=50)
    CardCVV = models.CharField( max_length=50)
    CardNumber = models.CharField( max_length=50)
    

    def __str__(self):
        return self.firstname

   


class PaymentOption(models.Model):
    userOption = models.ForeignKey("clientUser",  on_delete=models.CASCADE, blank=True, null=True)
    EwalletApi = models.ForeignKey("paymentOptionmethods",  on_delete=models.CASCADE, blank=True, null=True)
    Card = models.ForeignKey("CArdpay",  on_delete=models.CASCADE,blank=True, null=True)
    matually = models.ForeignKey("Matualpay",  on_delete=models.CASCADE,blank=True, null=True)
    
    

    def __str__(self):
        return self.clientUser.user

class Customerchatting(models.Model):
    usersender =  models.ForeignKey('clientUser', blank=True, null=True, on_delete=models.CASCADE)
    roomid = models.CharField(max_length=50)
    message = models.CharField(max_length=50)
    dateUploaded = models.DateTimeField( auto_now_add=True, blank=True, null=True)
    def sender(self):
        user=  self.usersender.get(uuidUser = self.roomid)
        self.usersender = user
    class Meta:
        verbose_name = ("Service")
        verbose_name_plural = ("customer service")

    def __str__(self):
        return self.roomid

    


