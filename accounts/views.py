from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from homepage.models import Users
from io import BytesIO
import base64
import matplotlib.pyplot as plt
import numpy as np


# Create your views here.
def login(request):
        return render(request,'Login.html')

def register(request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['pswd']
        cnfrmpassword=request.POST['cnfpswd']
        if password!=cnfrmpassword:
            return render(request,'Register.html',{'message':'Passwords does not match!!!','type':'alert-danger'})
        elif Users.objects.filter(username=username).exists():
            return render(request,'Register.html',{'message':'User already exists!!!','type':'alert-danger'})
        else:
            p = Users(username=username,password=password)
            p.save()
            return render(request,'Login.html',{'message':'User saved successfully','type':'alert-success'})
    else:
        return render(request,'Register.html')


def logout(request):
    try:
        del request.session['user_name']
    except KeyError:
        pass
    return redirect("/")

def myaccount(request):
     pos = np.arange(10)+ 2 
     fig = plt.figure(figsize=(8, 3))
     ax = fig.add_subplot(111)

     ax.barh(pos, np.arange(1, 11), align='center')
     ax.set_yticks(pos)
     ax.set_yticklabels(('#hcsm',
            '#ukmedlibs',
            '#ImmunoChat',
            '#HCLDR',
            '#ICTD2015',
            '#hpmglobal',
            '#BRCA',
            '#BCSM',
            '#BTSM',
            '#OTalk',), 
            fontsize=15)
     ax.set_xticks([])
     ax.invert_yaxis()

     ax.set_xlabel('Popularity')
     ax.set_ylabel('Hashtags')
     ax.set_title('Hashtags')

     plt.tight_layout()

     buffer = BytesIO()
     plt.savefig(buffer, format='png')
     buffer.seek(0)
     image_png = buffer.getvalue()
     buffer.close()

     graphic = base64.b64encode(image_png)
     graphic = graphic.decode('utf-8')

     return render(request, 'myaccount.html',{'graphic':graphic})


def updatesession(request):
    request.session['logout'] = False
    return HttpResponse('ok')
