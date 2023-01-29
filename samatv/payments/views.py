from asyncio.windows_events import NULL
from django.shortcuts import render
import razorpay
from . import config
from .models import User
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):
    return render(request,'payments/home.html')
def about(request):
    return render(request,'payments/about.html')
def donate(request):
    if(request.method=='POST'):
        print(request.POST)
        name=request.POST.get("name")
        amount=int(request.POST.get("amount"))
        email=request.POST.get("email")
        client=razorpay.Client(auth=(config.a,config.b))
        payment=client.order.create({'amount':amount*100,'currency':'INR','payment_capture':'1'})
        cust_data={'name':name,'amount':amount,'email':email,}
        user=User(name=name,amount=amount,email=email,payment_id=payment['id'])
        print(user.amount)
        user.save()
        arrayObj=User.objects.all()
        return render(request,'payments/donate.html',{'payment':payment,'name':name,'amount':amount,'email':email,'data':arrayObj})
    arrayObj=User.objects.all()
    return render(request,'payments/donate.html',{'data':arrayObj})
@csrf_exempt
def success(request):
    return render(request,"payments/success.html")
def contact(request):
    return render(request,'payments/contactus.html')