
# Create your views here.
    
from django.shortcuts import render
from django.contrib.auth.models import User
from twilio.rest import Client
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings




class twiliomail(APIView):
    def get(self, request):
        user_number=request.data.get("whatsapp_number")
        account_sid = settings.ACCOUNT_SID
        auth_token = settings.AUTH_TOKEN
        
        client = Client(account_sid, auth_token) 
        number='whatsapp:'+user_number
        message = client.messages.create( 
                              from_=settings.FROM,
                              body='welcom  ,  ',      
                              to=number, 
                          ) 
 
        print(message.sid)
        return Response(message.sid)    
        