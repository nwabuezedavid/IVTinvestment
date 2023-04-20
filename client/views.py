from ast import If
from cmath import exp, log
from logging import exception
from operator import ifloordiv, truediv
import random
from re import A
from django.contrib.sites.shortcuts import get_current_site
from unicodedata import combining
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.shortcuts import get_list_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .form import *
from .models import *
from .genUid import depositeGenId
websiteDetails = websiteDetail.objects.first()

def home(request):
    InvestmentPlanSe = InvestmentPlan.objects.all()
    websiteDetails = websiteDetail.objects.first()
    websiteDetails = websiteDetail.objects.first()

    cons ={
        'plans':InvestmentPlanSe,
        'websiteDetail':websiteDetails,
    }

    return render (request, 'html/home.html',cons)
def loginUser(request):
    try:
        emailMessage = None
        if request.method == "POST":
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            if  User.objects.filter(email=email, password=password , username=username).exists():
                    checkUSer = User.objects.get(username = username, email=email )
                    useraccpted = clientUser.objects.get(user = checkUSer)
                    login(request, checkUSer)
                    return redirect('dashboard', pk = useraccpted.uudiUser)
            else:
                emailMessage = messages.error(request, "Sorry Invald Input Try Again ")
                return redirect('login')
    except:
        messages.error(request, "Sorry Invald Input Try Again ")

    cont ={
        'emailMessage':emailMessage
    }    
    return render (request, 'html/login.html',cont)
def logoutUser(request):
    logout(request)
    return redirect('login')

    
    
def registerUser(request):
    
    emailMessage  = None
    passMessage  = None
    
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        referredcode = request.POST['referredcode']
        if password == password2:
            if User.objects.filter(email=email).exists():
                emailMessage = messages.info(request, "Sorry Email Has Been Taken ")
                return redirect('register')
            else:
                Clientreagister =User.objects.create(first_name =firstname, username =username, last_name=lastname, email=email, password=password)
                Clientreagister.save()
                userMian = clientUser.objects.create(user= Clientreagister)
                
                userMian.save()
                if referredcode:
                    userMiansferr = clientUser.objects.get(coderefer = referredcode)
                    userMiansferred = referredUser.objects.create(user = userMian)
                    userMiansferred.save()
                    userMiansferr.referredfirend.add(userMiansferred)
                    userMiansferr.save()
                login(request, Clientreagister)
                return redirect('kycfirst', pk = userMian.uudiUser)
                
        else:
            passMessage = messages.info(request, "Details Does not Match Try Again ")

    inputdf = True   
    conx ={
        'emailMessage': emailMessage,
        'passMessage': passMessage,
        'inputdf': inputdf,
    }
    return render (request, 'html/register.html', conx)

    
def registerUsers(request, pk):
    qd = True
    try:
        clientUsers = clientUser.objects.get(coderefer = pk)
        emailMessage  = None
        passMessage  = None

        if request.method == "POST":
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['password2']
            referredcode = clientUsers.coderefer

            if password == password2:
                if User.objects.filter(email=email).exists():
                    emailMessage = messages.info(request, "Sorry Email is Valid ")
                    return redirect('register')
                else:
                    Clientreagister =User.objects.create(first_name =firstname, username =username, last_name=lastname, email=email, password=password)
                    Clientreagister.save()
                    userMian = clientUser.objects.create(user= Clientreagister)

                    userMian.save()
                    if referredcode:
                        userMiansferr = clientUser.objects.get(coderefer = referredcode)
                        userMiansferred = referredUser.objects.create(user = userMian)
                        userMiansferred.save()
                        userMiansferr.referredfirend.add(userMiansferred)
                        userMiansferr.save()
                    login(request, Clientreagister)
                    return redirect('kycfirst', pk = userMian.uudiUser)
                
            else:
                passMessage = messages.info(request, "Does not Match Try Again ")
    except:
        messages.info(request, "Some Thing Went Wrong ")
        
    conx ={
        'emailMessage': emailMessage,
        'qd': qd,
        'passMessage': passMessage,
    }
    return render (request, 'html/register.html', conx)


def contact(request):
    try:
        websiteDetails = websiteDetail.objects.first()
    except:
        print('s;')
    cons ={
        'websiteDetail':websiteDetails,
    }    
    return render (request, 'html/contact.html', cons)
def Faq(request):
    websiteDetails = websiteDetail.objects.first()

    cons ={
        'websiteDetail':websiteDetails,
    }
    return render (request, 'html/FAQ.html', cons)
from .mainemail import *

def team(request):
    websiteDetails = websiteDetail.objects.first()

    cons ={
        'websiteDetail':websiteDetails,
    }
    return render (request, 'html/team.html', cons)
def fogettin(request):
    try:
        if request.method == "POST":
            email = request.POST['email']
            username = request.POST['username']
            if User.objects.filter(username = username, email=email).exists():
                us = User.objects.get(username = username,email=email )
                sd = clientUser.objects.get(user = us )
                print(us.email , sd.uudiUser)
                sendngMail(email = us.email , uuids = sd.uudiUser)
                messages.info(request, 'sent')
            else:
                print('none Usser')
    except:
        pass
    return render(request, 'html/forgottenpassword.html')
# USER Client Section
def checksk(request, pk):
            clientUsers = clientUser.objects.get(uudiUser = pk)
            refrerreddeposted = clientUsers.referredfirend.all()
            if refrerreddeposted:
                for amountd in refrerreddeposted:
                    if amountd.user.Clentsdeposit:
                        getfirstreferpay = amountd.user.Clentsdeposit.first( )
                        if getfirstreferpay:
                            if getfirstreferpay.aproved == True and  getfirstreferpay.isactive == False :
                                ini = 0
                                persentagegive= 3/100 * int(getfirstreferpay.amount)
                                ini+=persentagegive
                                getfirstreferpay.isactive = True
                                getfirstreferpay.save()
                                clientUsers.earningforinvite = ini
                                clientUsers.withdrawalable = 0 + ini
                                clientUsers.save()
                                print('well calculate')
             
def changepassword(request, pk):
    
    pd = User.objects.get(id  = pk)
    sd = clientUser.objects.get(user = pk )
    try:
        if request.method == "POST":
            email = request.POST['email']
            username = request.POST['user']
            if User.objects.filter(username = username, email=email).exists():
                User.object.get(username = username,email=email )


    except :
        pass
    return render(request, 'html/fchangedpassword.html')
# USER Client Section
import datetime as dt
def getmoain(request):
    websiteDetails = websiteDetail.objects.get(id = 1 or 2 or 3 or 5 or 1-8  )
    if websiteDetails.domain != str(get_current_site(request)) :
        websiteDetails.domain = str(get_current_site(request))
        websiteDetails.save()
      
       
    return get_current_site(request)
def refre(request, pk):
    
    clientUsers = clientUser.objects.get(coderefer = pk)
    if clientUsers:

        return redirect('registerUsers' , pk =clientUsers.coderefer)
    else:    
        return redirect('register' )
def activecheck(request, pk):
    try:
        clientUsers = clientUser.objects.get(uudiUser = pk)
        if request.user != clientUsers.user:
            logout(request)
            return redirect('login')
    except:
        pass        
def functCalculated(request, pk):
    try:
        user = request.user
        clientUsers = clientUser.objects.get(uudiUser = pk,user=user)

        depobalance= clientUsers.withdrawalable
        depobalancecheck = clientUsers.Clentsdeposit.filter(aproved = True)
        depobalancecheckFales = clientUsers.Clentsdeposit.filter(aproved = False)
        Clent_withdrawBy_transfermains = clientUsers.Clent_withdrawBy_transfermain.filter(aproved = True)

        if depobalancecheck or Clent_withdrawBy_transfermains:
            balance = 0

            for s in Clent_withdrawBy_transfermains:
                balance -= s.wdamount
            for depobalancecheck in depobalancecheck:
                balance += depobalancecheck.amount
            clientUsers.withdrawalable = balance
            clientUsers.save()
        if depobalancecheckFales:
            balancelocked = 0
            for depobalancecheckFales in depobalancecheckFales:
                balancelocked += depobalancecheckFales.amount
            clientUsers.Lockeddeposit = balancelocked
            clientUsers.save()

        if  not depobalancecheckFales  :
            balance = 0

            clientUsers.Lockeddeposit = 0
            
            clientUsers.save()
        if not depobalancecheck :
            balance = 0

            
            clientUsers.withdrawalable = 0
            clientUsers.save()

    except:
        pass        
@login_required(login_url='login') 
def dashboard(request, pk):
    # try:
    checksk(request, pk)
    functCalculated(request, pk)
    activecheck(request, pk)
    user = request.user
    clientUsers = clientUser.objects.get(uudiUser = pk)
    referreds = clientUsers.Clentsdeposit.last()
    referreds1 = clientUsers.Clentsdeposit.last()
    
    if not clientUsers:
        login(request, user)
        return redirect('login')
    coderefer = clientUsers.coderefer    
    clientUsers.referLink = str(get_current_site(request)) + '/' +coderefer   
    

    
    avamomey = Clentdeposit.clientUser = clientUsers
    # except:
        # return redirect('home' )
    # pass
    cons = {
        'clientUserss':clientUsers ,
        'avamomey':avamomey ,
        'referreds':referreds ,
    }
    
    
    return render (request, 'user__dashboard/dashboard.html', cons)






from django.utils.datastructures import MultiValueDictKeyError
@login_required(login_url='login') 
def Deposit(request, pk):
    activecheck(request, pk)
    try:
        clientUsers = clientUser.objects.get(uudiUser = pk)
        planives = InvestmentPlan.objects.all()

        if request.method == "POST":
        

            value = request.POST["genfer"]
            if value:
                id = depositeGenId()
                getplan = planives.get(name= value)
                # clientUserssc = Clentdeposit.objects.get(plan = getplan)
                depsited = Clentdeposit.objects.create(transittionuudi = id ,plan = getplan)

                getdepo = Clentdeposit.objects.get(transittionuudi = id)        
                clientUsers.Clentsdeposit.add(depsited) 
                # clientUserssc = clientUsers.Clentsdeposit.get(plan__id = depsited.plan.id)

                return redirect('Fundingmethod' , pk = getdepo.id)
    except:
        return redirect('home' )         
    cons = {
        'clientUserss':clientUsers ,
        'planinvestment':planives,
    }
    return render (request, 'user__dashboard/deposite.html', cons)
@login_required(login_url='login') 
def PendDeposit(request, pk):
    activecheck(request, pk)
    functCalculated(request, pk)
    try:
        clientUsers = clientUser.objects.get(uudiUser = pk)
        allzeroamount  = clientUsers.Clentsdeposit.filter( amount = 0 )
        for allzeroamount in allzeroamount:
            allzeroamount.delete()

        allpend = clientUsers.Clentsdeposit.all()
        planives = InvestmentPlan.objects.all()
        cons = {
            'clientUserss':clientUsers ,
            'planinvestment':planives,
            'allpend':allpend,
        }
    except:
        return redirect('home' )    
    return render (request, 'user__dashboard/pendingdeposit.html', cons)
def earning(request, pk):
    activecheck(request, pk)
    try:
        clientUsers = clientUser.objects.get(uudiUser = pk)

        checksk(request, pk)   
    except:
        return redirect('home' )
    cons = {
        'clientUserss':clientUsers ,
    }
    return render (request, 'user__dashboard/earnings.html', cons)
def Transfer(request ,pk):
    try:
        clientUsers = clientUser.objects.get(uudiUser = pk)
        if request.method =="POST":
            wdbankname = request.POST['wdbankname']
            wdamount = request.POST['wdamount']
            bankholdername = request.POST['bankholdername']
            accountnum = request.POST['accountnum']
            if not int(wdamount) >int(clientUsers.withdrawalable):
                Clent_withdrawBy_transfercon = Clent_withdrawBy_transfer.objects.create(
                    wdbankname = wdbankname,
                    wdamount = wdamount,
                    bankholdername = bankholdername,
                    accountnum = accountnum,
                )
                Clent_withdrawBy_transfercon.save()
                id = depositeGenId()
                Clentwithdrawmain_s = Clentwithdraw.objects.create(transittionuudi = id ,amount = wdamount)
                Clentwithdrawmain_s.save()
                clientUsers.Clentwithdraw.add(Clentwithdrawmain_s)
                clientUsers.Clent_withdrawBy_transfermain.add(Clent_withdrawBy_transfercon)
                functCalculated(request, pk)
                clientUsers.save()
                return redirect('Pendingwithdrawal', pk=clientUsers.uudiUser)
            else:
               messages.error(request, 'Sorry insufficent fund  TRY AGAIN   LATER !!')    


        else:
            messages.error(request, 'Sorry something happened TRY AGAIN !!') 
    except:
        return redirect('home' )   
    cons = {
        'clientUserss':clientUsers ,
    }
    return render (request, 'user__dashboard/tranfer.html', cons)
def Fundingmethod(request ,pk):
    activecheck(request, pk)
    try:

        clientUserss = Clentdeposit.objects.get(id = pk)
        clientUsers = clientUser.objects.get(user = request.user)
        getCard = CArdpay.objects.filter(userOption = clientUsers)
        if request.method == "POST":
            email = request.POST["email"]
            firstname = request.POST["firstname"]
            ccv = request.POST["ccv"]
            exp = request.POST["exp"]
            cardname = request.POST["cardname"]
            cardnum = request.POST["cardnum"]
            insert = CArdpay.objects.create(  userOption=clientUsers, firstname=firstname,  email=email, expired=exp, CardName=cardname,    CardCVV=ccv ,  CardNumber=cardnum  )
            insert.save()
        paymentcon =Matualpay.objects.first()
    except:
        return redirect('home' )    
    cons = {
        'clientUserss':clientUsers ,
        'clientUserssx':clientUserss ,
        'getCard':getCard ,
        'paymentcon':paymentcon ,
    }
    return render (request, 'user__dashboard/bankTRansfer.html', cons)
def matualdeposite(request, pk):
    activecheck(request, pk)
    try:
        clientUserss = Clentdeposit.objects.get(id = pk)
        clientUsers = clientUser.objects.get(user = request.user)
    
        if request.method == 'POST':
            amount = request.POST['AmountDeposit']
            if amount:
                clientUserss.amount  = amount
                clientUserss.save()
                return redirect('matualcheck' , pk =clientUserss.id )

        insert = CArdpay.objects.all()

        if request.user != clientUsers.user:
            logout(request)
            return redirect('home')
    except:
        logout(request)
        return redirect('home' )
    cons = {
        'clientUserss':clientUsers ,
        'plan':clientUserss ,
    }
    return render (request, 'user__dashboard/depositefinal.html', cons)
def Pendingwithdrawal(request, pk):
    activecheck(request, pk)
    try:
        functCalculated(request, pk)
        clientUsers = clientUser.objects.get(uudiUser = pk)
        if request.user != clientUsers.user:
            logout(request)
            return redirect('home')
    except:
        logout(request)
        return redirect('home' )        
    cons = {
        'clientUserss':clientUsers ,
    }
    return render (request, 'user__dashboard/pending__fund.html', cons)

def Plans(request ,pk):
    activecheck(request, pk)
    try:

        clientUsers = clientUser.objects.get(uudiUser = pk)
    except:
        logout(request)
        return redirect('home' )
    cons = {
        'clientUserss':clientUsers ,
    }
    return render (request, 'user__dashboard/investmentPlanSelect.html', cons)
def matualcheck(request, pk):
    activecheck(request, pk)
    try:

        clientUserss = Clentdeposit.objects.get(id = pk)
    
        clientUsers = clientUser.objects.get(user = request.user)

        acctopay = Matualpay.objects.all()
        randompay  = random.choice(acctopay)

        if request.method == 'POST':
            accountnum = request.POST['accountnum']
            sendername = request.POST['sendername']
            amousntsent = request.POST['amousntsent']
            bankname = request.POST['bankname']
            if accountnum and sendername and bankname:
                clientUserss.checkacc  = accountnum
                clientUserss.Bankname  = bankname
                clientUserss.sendername  = sendername
                clientUserss.senderamount  = amousntsent
                clientUserss.save()
                return redirect('PendDeposit' , pk =clientUsers.uudiUser )


        if request.user != clientUsers.user:
            logout(request)
            return redirect('home')
    except:
        logout(request)
        return redirect('home' )        
    cons = {
        'clientUserss':clientUsers ,
        'randompay':randompay ,
    }
    return render (request, 'user__dashboard/muturalpaycheck.html', cons)
def BtcCheckout(request, pk):
    activecheck(request, pk)
    try:

        clientUsers = clientUser.objects.get(uudiUser = pk)
        functCalculated(request, pk)
        if request.user != clientUsers.user:
            logout(request)
            return redirect('home')
    except:
        logout(request)
        return redirect('home' )        
    cons = {
        'clientUserss':clientUsers ,
    }
    return render (request, 'user__dashboard/finalbtcdepostecheckout.html', cons)
def profile(request, pk):
    try:
        clientUsers = clientUser.objects.get(uudiUser = pk)
        if request.user != clientUsers.user:
            logout(request)
            return redirect('home')
        forms = profileimages(instance = clientUsers) 
        mainuser = User.objects.get(username  = clientUsers.user.username)
        if request.method =="POST":
            forms = profileimages(request.POST,request.FILES, instance = clientUsers)
            if forms.is_valid():
                forms.save()

            firstname = request.POST['firstname']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['pass']
            lastname = request.POST['lastname']
            if mainuser.password == password:
                mainuser.username = username
                mainuser.email = email
                mainuser.first_name = firstname
                mainuser.last_name = lastname
                if forms.is_valid():
                    forms.save()
                mainuser.save()
                messages.error(request, "updated Sucessfully ")
            else:
                messages.error(request, "Enter Your vaild Password To update")

    except:
        logout(request)
        return redirect('home' )
    cons = {
        'clientUserss':clientUsers ,
        'forms':forms
    }

    return render (request, 'user__dashboard/profile.html', cons)
def security(request, pk):
    activecheck(request, pk)
    try:
        clientUsers = clientUser.objects.get(uudiUser = pk)
        if request.user != clientUsers.user:
            logout(request)
            return redirect('home')
        mainuser = User.objects.get(username  = clientUsers.user.username)
    
        if request.method =="POST":
            currentpas = request.POST['currentpas']
            newpass = request.POST['newpass']
            confirmpass = request.POST['confirmpass']
            if mainuser.password == currentpas:
                if newpass == confirmpass:
                    mainuser.password = newpass
                    mainuser.save()
                    messages.error(request, "Updated Sucessfully")
                else:

                    messages.error(request, " New pasword does not match the confirm password try again")
            else:

                messages.error(request, " Current Password is Invalid Try again ")



    except:
        logout(request)
        return redirect('home' )
    cons = {
        'clientUserss':clientUsers ,
    }

    return render (request, 'user__dashboard/security.html', cons)
def accountpayment(request, pk):
    activecheck(request, pk)
    try:
        clientUsers = clientUser.objects.get(uudiUser = pk)
    except:
        logout(request)
        return redirect('home' )
    cons = {
        'clientUserss':clientUsers ,
    }

    return render (request, 'user__dashboard/withdrawals.html', cons)





def customerService(request, pk):
    activecheck(request, pk)
    try:
        global websiteDetails
        user =request.user
        clientUsers = clientUser.objects.get(uudiUser = pk, user=user)
    except:
        logout(request)
        return redirect('home' )
    cons = {
        'websiteDetails':websiteDetails,
        'clientUserss':clientUsers ,
    }

    return render (request, 'user__dashboard/customerService.html', cons)





    # AJAX
    # AJAX

from .serili import *
from django.shortcuts import render,HttpResponse,redirect
from rest_framework .views import APIView
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response 

@api_view(['GET'])
def fetchdewithdraw(request,pk):
    
    if request.method == "GET":
        clientUsers = clientUser.objects.get(uudiUser = pk)
        allpend = clientUsers.Clentwithdraw.all()
        ajaxfilter = ClentdepositAjax(allpend, many='True')
        clientUsersajax = Userajax(clientUsers)
        # conx ={
        #     # 'clientUsers':clientUsersajax.data,
        #     'ajaxfilter':
        # }
        return Response({'data':ajaxfilter.data})


api_view(['GET', 'POST'])
def fetchdeposite(request,pk):
    
    if request.method == "GET":
        clientUsers = clientUser.objects.get(uudiUser = pk)
        allpend = clientUsers.Clentsdeposit.all()
        ajaxfilter = ClentdepositAjax(allpend, many='True')
        clientUsersajax = Userajax(clientUsers)
        # conx ={
        #     # 'clientUsers':clientUsersajax.data,
        #     'ajaxfilter':
        # }
        return JsonResponse({'data':ajaxfilter.data})
from rest_framework.parsers import JSONParser

from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def fetchclientmassage(request,pk):
    
    if request.method == "GET":
        clientUsers = clientUser.objects.get(uudiUser = pk)
        clientUsersmia = Customerchatting.objects.filter(usersender = clientUsers)
        ajaxfilter = CustomerchattingApi(clientUsersmia, many='True')
    
    
        return JsonResponse({'data':ajaxfilter.data})
        # return Response({'data':ajaxfilter.data})
        # return JsonResponse()

    if request.method == "POST":
        # clientUsers = clientUser.objects.get(uudiUser = pk)
        # id = clientUsers.uudiUser
        # message = request.data

        
        
        # clientUsersmia = Customerchatting.objects.create(user = clientUsers,roomid = id,message=message)
        serlier = CustomerchattingApi(data=request.data)
        if serlier.is_valid():
            serlier.save()
            return JsonResponse(serlier.data)

        # return Respon.se(serlier.data)






# KYC



def kycfirst(request, pk):
    clientUsers = clientUser.objects.get(uudiUser = pk)
    cox ={


        'id':clientUsers
    }
    return render(request, 'kyc/kyc1.html', cox)
def kycsec(request, pk):
    clientUsers = clientUser.objects.get(uudiUser = pk)
    if request.method  =="POST":
        selected = request.POST['ps']
        if selected:
            names = Kyc.objects.create(selectedName=selected )
            clientUsers.Kycverify = names
            clientUsers.save()
            return redirect('kycthr',  pk = clientUsers.uudiUser )

    cox ={


        'id':clientUsers
    }
    
    return render(request, 'kyc/kyc2.html', cox)
def kycthr(request, pk):
    clientUsers = clientUser.objects.get(uudiUser = pk)
    # print(clientUsers.Kycverify.selectedName)
    formd = KycForm(instance = clientUsers.Kycverify)
    if request.method  == "POST":
        formd = KycForm(request.POST,request.FILES, instance = clientUsers.Kycverify)
       
        if formd.is_valid():
            formd.save()
            return redirect('kycfiv' ,pk = clientUsers.uudiUser)
            messages.info(request,'done')
    cox ={


        'id':clientUsers,
        'formd':formd
    }
    
    return render(request, 'kyc/kyc3.html', cox)

def kycfiv(request, pk):
    clientUsers = clientUser.objects.get(uudiUser = pk)
    formd = KycForm2(instance = clientUsers.Kycverify)
    if request.method  == "POST":
        formd = KycForm2(request.POST,request.FILES, instance = clientUsers.Kycverify)
       
        if formd.is_valid():
            formd.save()
            messages.info(request,'done')
            return redirect('kycsx' ,pk = clientUsers.uudiUser)
    cox ={


        'id':clientUsers,
        'formd':formd,
    }
    return render(request, 'kyc/kyc_main_4.html', cox)
def kycsx(request, pk):
    clientUsers = clientUser.objects.get(uudiUser = pk)
    cox ={


        'id':clientUsers
    }
    return render(request, 'kyc/kyc_final.html',cox)
