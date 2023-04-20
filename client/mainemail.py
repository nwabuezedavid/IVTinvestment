from django.core.mail import send_mail
import uuid
from django.conf import settings
# Simple Usage
# Admin will receive a message
def sendngMail(email, uuids):
    
    Sudject = "Your Reset Password Link,"
    message = f" Hi  Click To Reset Your Password http://127.0.0.1:8000/changepassword/{uuids}/"
    email_from=  settings.EMAIL_HOST_USER 
    recipient_list = {email}
    send_mail(  Sudject ,  message,email_from,recipient_list)
    return True
    