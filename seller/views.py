from django.shortcuts import render,redirect
from homepage.models import Product
from accounts.models import Sellers


# Create your views here.
def home(request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['pswd']
        m=0
        try:
            m = Sellers.objects.get(username=request.POST['uname'])
        except:
            return render(request,'sellerLogin.html',{'message':'Username not found','type':'alert-danger'})
        if m.password == request.POST['pswd']:
            request.session['seller_name'] = m.username
            sa=Product.objects.filter(sellerid=m.id)
            allprod={}
            temp=[]
            i=1
            for products in sa:
                if products.name in temp:
                    pass
                else:
                    allprod.update({i:products.name})
                    temp.append(products.name)
                i=i+1
            return render(request,'seller.html',{'products':allprod,'username':username})
        else:
            return render(request,'sellerLogin.html',{'message':'Username not found','type':'alert-danger'})
    else:
        print("came from add product")
        return render(request,'seller.html')



def login(request):
    return render(request,"sellerLogin.html")

def register(request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['pswd']
        cnfrmpassword=request.POST['cnfpswd']
        if password!=cnfrmpassword:
            return render(request,'sellerRegister.html',{'message':'Passwords does not match!!!','type':'alert-danger'})
        elif Sellers.objects.filter(username=username).exists():
            return render(request,'sellerRegister.html',{'message':'User already exists!!!','type':'alert-danger'})
        else:
            p = Sellers(username=username,password=password)
            p.save()
            return render(request,'sellerLogin.html',{'message':'User saved successfully','type':'alert-success'})
    else:
        return render(request,'sellerRegister.html')

def add(request):
    if request.method=='POST':
        name=request.POST['pname']
        price=request.POST['price']
        totalcount=request.POST['totalcount']
        totalcount=totalcount.split(",")
        image=request.FILES.getlist('images')
        seller=request.session['seller_name']
        sid=Sellers.objects.filter(username=seller).values_list('id', flat=True)[0]
        print("{} Seller id",sid)
        pid=Product.objects.filter(sellerid=sid).values_list('productid', flat=True)
        c=0
        for p in pid:
            if p>c:
                c=p
        pid=c+1
        description={}
        for i in range(len(totalcount)):
            description.update({request.POST['key'+totalcount[i]]: request.POST['value'+totalcount[i]]})
        print(description)
        for img in image:
            photo = Product.objects.create(
                price=price,
                description=description,
                name=name,
                img=img,
                sellerid=sid,
                productid=pid
            )
        return redirect('/seller/home')
    else:
        return render(request,'addProduct.html')

def sellerlogout(request):
    try:
        del request.session['seller_name']
    except KeyError:
        pass
    return redirect("/seller/login")