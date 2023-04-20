from django.urls import path
from . views import *
urlpatterns = [
    path('', home, name="home"),
    path('contact/', contact, name="contact"),
    path('Faq/', Faq, name="faq"),
    path('team/', team, name="team"),
    path('fogetten/', fogettin, name="fogetten"),
    path('changepassword/<pk>/', changepassword, name="changepassword"),
    path('dashboard/<pk>/', dashboard, name="dashboard"),
    path('deposit/<pk>/', Deposit, name="Deposit"),
    path('wtTransfer/<pk>/', Transfer, name="WithdrawalTransfer"),
    path('earning/<pk>/', earning, name="earning"),
    path('fdmethod/<pk>/', Fundingmethod, name="Fundingmethod"),
    path('chkbtc/<pk>/', BtcCheckout, name="BtcCheckout"),
    path('viewpdeposit/<pk>/', PendDeposit, name="PendDeposit"),
    path('investsplans/<pk>/', Plans, name="Plans"),
    path('profile/<pk>/', profile, name="profile"),
    path('matualdp/<pk>/', matualdeposite, name="matualdeposite"),
    path('mtcheck/<pk>/', matualcheck, name="matualcheck"),
    path('security/<pk>/', security, name="security"), 
    path('pdwithdraw/<pk>/', Pendingwithdrawal, name="Pendingwithdrawal"),
    path('accountPa/<pk>/', accountpayment, name="accountpayment"),
    path('service/<pk>/', customerService, name="customerService"),
    path('/<pk>/', refre, name="refre"),
    path('login/', loginUser, name="login"),
    path('register/', registerUser, name="register"),
    path('register/<pk>', registerUsers, name="registerUsers"),
    path('logout/', logoutUser, name="logout"),

    # aJAX
    path('fetchdeposite/<pk>/', fetchdeposite, name="fetchdeposite"),
    path('fetchwithdraw/<pk>/', fetchdewithdraw, name="fetchdewithdraw"),
    path('fetchclientmassage/<pk>/', fetchclientmassage, name="fetchclientmassage"),



# KYC
    path('kyc1/<pk>/', kycfirst, name="kycfirst"),
    path('kycsec/<pk>/', kycsec, name="kycsec"),
    path('kycthr/<pk>/', kycthr, name="kycthr"),
    path('kycfiv/<pk>/', kycfiv, name="kycfiv"),
    path('kycsx/<pk>/', kycsx, name="kycsx"),


]

