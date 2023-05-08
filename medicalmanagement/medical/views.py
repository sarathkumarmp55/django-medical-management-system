from django.shortcuts import render,redirect
from.models import contact,medicine,order
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.

def home(request):
    return render(request,'home.html')
def contactform(request):
    if request.method == "POST":
        cname=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        phonnum=request.POST.get('phone number')
        S=contact(name=cname,email=email,address=address,phno=phonnum)
        S.save()
    return render(request,'contact.html')
def userlogin(request):
    if request.method=="POST":
        uname=request.POST.get("uname")
        pass1=request.POST.get("psw")
        l=authenticate(username=uname,password=pass1)
        if l is not None:
            login(request,l)
            return redirect("/userhome")
        else:
            return redirect("/login")
    return render(request,"login.html")

   
def about(request):
    return render(request,'about.html')
def userhome(request):
    return render(request,'userhome.html')
def signup(request):
    if request.method=="POST":
        uname=request.POST.get("name")
        fname=request.POST.get("fname")
        email=request.POST.get("email")
        pswd=request.POST.get("pass1")
        pswd2=request.POST.get("cpass1")
        if(pswd != pswd2):
            return redirect('/signup')
        try:
            if User.objects.get(username=uname):
                return redirect('/signup')
        except:
            pass
        use=User.objects.create_user(uname,email,pswd)
        use.first_name=fname
        use.save()
        return redirect('/login')

    return render(request,'signup.html')

def medicineshow(request):
    a=medicine.objects.all()
    return render(request,"medicine.html",{'medical':a})

def orders(request):
     item=medicine.objects.all()
     if request.method=="POST":
        oname=request.POST.get('oname')
        oemail=request.POST.get('oemail')
        oaddress=request.POST.get('oaddress')
        ophone=request.POST.get('ophone')
        quan=request.POST.get('quantity')
        items=request.POST.get('select')
        print(oname,oemail,items,quan)
        pri=" "
        for i in item:
            if items==i.prodName:
                pri=i.prodPrice
            pass
        newprice=int(pri)*int(quan)

        K=order(orderName=oname,orderemail=oemail,orderaddress=oaddress,orderphone=ophone,items=items,quantity=quan,price=newprice)
        K.save()
        return redirect('/orderdetails')
     return render(request,'order.html',{'med':item})

def orderdetails(request):
    items=order.objects.all()
    return render(request,'orderdetails.html',{'Order' : items})

def delet(request,id):
    D=order.objects.get(id=id)
    D.delete()
    return redirect('/orderdetails')

