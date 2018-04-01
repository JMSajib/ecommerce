from django.shortcuts import render
import stripe

# Create your views here.
stripe.api_key = "sk_test_c9P1UuochpSxiMyPLebfqwYt"
STRIPE_PUB_KEY = "pk_test_eEPEHJg4l59BrjvfH0qOdORO"

def payment_method_view(request):
    if(request.method=="POST"):
        print(request.POST)
    return render(request,"billing/payment-method.html",{"publish_key":STRIPE_PUB_KEY})
