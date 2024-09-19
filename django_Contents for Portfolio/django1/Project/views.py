from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import userForm

def Home(request): 
    # Data={
    #     'Title':'Home New',
    #     'clist':["Pawan","mom","dad","bro","sis"],
    #     'number':[93,5,34,34,40],
    #     'member_details':[
    #         {'Name':'Pawan','Phone':9305343440},
        
    #         {'Name':'bro','Phone':9989563093}
    #     ]
    # }
    return render(request,"index2.html" )


def About(request):
    return render(request,"About.html")

def Contact(request):
    return render(request,"Contact.html")

def Portfolio(request):
    return render(request,"Portfolio.html")

def submitForm(request):
    return HttpResponse(request)

def calculator(request):


    return render(request="calculator.html")

def userform(request):
    # finalAns=0
    # fn=userform()
    # data={'form':fn}
    # try:
    #     if request.method=="POST":
    #     # n1=int(request.GET['num1'])
    #     # n2=int(request.GET['num2'])

    #         n1=int(request.POST.get('num1'))
    #         n2=int(request.POST.get('num2'))
    #         finalAns=n1+n2
    #         data={'form':fn,
    #               'Output':finalAns
    #             }

    #         url="/About/?Output={}".format(finalAns)
    #         return HttpResponseRedirect(url)
    # except:
    #     pass
    return render(request,"userform.html")
