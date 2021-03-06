from django.utils.http import is_safe_url
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import stripe

# Create your views here.
stripe.api_key = "sk_test_c9P1UuochpSxiMyPLebfqwYt"
STRIPE_PUB_KEY = "pk_test_eEPEHJg4l59BrjvfH0qOdORO"

def payment_method_view(request):
    next_url= None
    next_ = request.GET.get("next")
    if(is_safe_url(next_,request.get_host())):
        next_url = next_
    return render(request,"billing/payment-method.html",{"publish_key":STRIPE_PUB_KEY,"next_url":next_url})

def payment_method_create_view(request):
    if(request.method=="POST" and request.is_ajax()):
        print(request.POST)
        return JsonResponse({"message":"Done"})
    return HttpResponse("error",status_code=401)
