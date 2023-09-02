from django.core.mail import send_mail
from django.views import View
from django.shortcuts import render, redirect


   
def sendEmail(recipient):
        recipient_email = recipient
        subject = "Please Verify your Account"
        message ="Hello world"
        sender_email = 'komaljan4@gmail.com'  # Replace with your email address

        try:
            send_mail(subject, message, sender_email, [recipient_email])
            return True  # Redirect to a success page
        except Exception as e:
            error_message = str(e)
            print(error_message)
            return False
