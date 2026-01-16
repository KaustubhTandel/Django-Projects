from django.shortcuts import render,redirect
from django.http import HttpResponse
# form .models import Login
from .models import Personal_Informations
from .models import Car_Collections
from .models import Payment
# from .models import Password

# Create your views here.

# def l_g(request):
#     if request.method=="POST":
#         username=request.POST.get("USERNAME")
#         password=request.POST.get("PASSWORD")
#         Login.object.create()


def p_d(request):
    if request.method=="POST":
        name=request.POST.get("NAME")
        contact=request.POST.get("CONTACT")
        age=request.POST.get("AGE")
        gender=request.POST.get("GENDER")
        email=request.POST.get("EMAIL")
        address=request.POST.get("ADDRESS")
        Personal_Informations.objects.create(Name=name,Contact=contact,Age=age,Gender=gender,Email=email,Address=address)
        return redirect("F2")
    return render(request,"PD1.html")



def c_c(request):
    if request.method=="POST":
        car_name=request.POST.get("CAR_NAME")
        model_name=request.POST.get("MODEL_NAME")
        car_colour=request.POST.get("CAR_COLOUR")
        Car_Collections.objects.create(Car_Name=car_name,Model_Name=model_name,Car_Colour=car_colour)
        return redirect("F3")
    return render(request,"CC2.html")


def p_t(request):
    if request.method=="POST":
        card_number=request.POST.get("CARD_NUMBER")
        cv_number=request.POST.get("CV_NUMBER")
        Payment.objects.create(Card_Number=card_number,CV_Number=cv_number)
        return redirect("TY")
    return render(request,"PY3.html")

def t_y(request):
    if request.method=="POST":
        return render("F1")
    return render(request,"Thank You.html")

def index(request):
    return render(request,"index.html") 



        
