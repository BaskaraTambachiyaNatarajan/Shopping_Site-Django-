from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product,Users

# Create your views here.
def index(request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['pswd']
        m=0
        try:
            m = Users.objects.get(username=request.POST['uname'])
        except:
            return render(request,'Login.html',{'message':'User not found','type':'alert-danger'})
        if m.password == request.POST['pswd']:
            request.session['user_name'] = m.username
            prod1=Product()
            prod1.name="iPad"
            prod1.img="ipad.jpg"
            sa=Product.objects.all()
            allprod=[]
            temp=[]
            i=1
            for products in sa:
                if len(allprod)>=6:
                    break
                if products.name not in temp:
                    allprod.append({"name":products.name,"image":products.img})
                    temp.append(products.name)
                else:
                    pass
            return render(request,'index.html',{'products':allprod})
        else:
            return render(request,'Login.html',{'message':'Wrong password','type':'alert-danger'})
    else:
        return redirect("/")