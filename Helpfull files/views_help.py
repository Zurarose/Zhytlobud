"""
Definition of views.
"""
import os
import logging
from datetime import datetime
from django.http import HttpRequest
from django.http import FileResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django import forms
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.contrib import messages #import messages
from django.contrib.auth import login as log 
from django.contrib.auth import logout as lgout
from django.contrib.auth.decorators import login_required
from .models import *
from .tables import *
from .forms import *
from .forms import *
from django_tables2 import RequestConfig
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.template import context
from datetime import datetime

#Logs
logger = logging.getLogger('mylogs')
date = ""
#logger.error('Something went wrong!')
def login(request):
    """Renders the home page."""
    if request.user.is_authenticated:
       return render(request, 'app/menu.html')

    if request.POST.get('log'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            log(request, user)
            # Redirect to a success page.
            return render(request, 'app/menu.html')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'app/error.html', {'error': 'Wrong data'})                    
    return render(request, 'app/login.html')

@login_required
def logout(request):
    lgout(request)
    return render(request, 'app/error.html', {'error': 'Logout successful'})  

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            log(request, user)
            return render(request, 'app/reg_done.html', {'new_user': username})
    else:
        form = SignUpForm()
    return render(request, 'app/register.html', {'form': form})

@login_required
def menu(request):
    return render(request, "app/menu.html")

def error(request):
    return render(request, "app/error.html")

def Resources(request):
    table = MatTable(Materials.objects.all(), template_name="django_tables2/bootstrap4.html")
    RequestConfig(request).configure(table)
    return render(request, 'app/tabs/Resources.html', {'table': table})

def MaterialAdd(request):
    if request.method == 'POST':
        mname = request.POST['name']
        mstruct = request.POST['struct']
        munit = request.POST['unit']
        mmanuf = request.POST['manuf']
        mprice = request.POST['price']
        mcount = 0
        
        if mname != "" and mstruct != "" and munit != "" and mmanuf != "" and mprice != "":
            b = Materials(name = mname, structure = mstruct, unit = munit, manufacturer = mmanuf,count = mcount, price = mprice)
            b.save()
            #Redirect to a success page.
            table = MatTable(Materials.objects.all(), template_name="django_tables2/bootstrap4.html")           
            return render(request, 'app/tabs/Resources.html', {'table': table})
        else:
            #Return an 'invalid login' error message.
            messages.error(request, 'You must complete the form!')
    return render(request, 'app/appfunct/MaterialAdd.html')

def MaterialDel(request):     
    posts = Materials.objects.all()
    context = {"posts": posts}
    if request.POST.get('material_id'):
        Materials.objects.filter(id_material=request.POST['material_id']).delete()
    return render(request,'app/appfunct/MaterialDel.html', context)

def Matorder(request):
    select = '1'
    table_mat_ord = MatOrdTable(Orders.objects.all(), template_name="django_tables2/bootstrap4.html") 
    if request.POST.get('filter'):
        if request.POST.get('select') == "open":        
            table_mat_ord = MatOrdTable(Orders.objects.filter(status = "Open"), template_name="django_tables2/bootstrap4.html")
            select = '3'
        elif request.POST.get('select') == "completed":
            table_mat_ord = MatOrdTable(Orders.objects.filter(status = "Completed"), template_name="django_tables2/bootstrap4.html")
            select = '2'
        else:
            table_mat_ord = MatOrdTable(Orders.objects.all(), template_name="django_tables2/bootstrap4.html")
            select = '1'
    RequestConfig(request).configure(table_mat_ord)

    if request.POST.get('review'):
        if len(request.POST.getlist("radios")) > 0:
            request.session['reviews'] = request.POST.get('radios')      
            return redirect('MatordReview')
        else:
            return render(request, 'app/error.html', {'error': 'Nothing has been selected'})  
    return render(request, 'app/tabs/Matorder.html', {'table': table_mat_ord, 'which': select })

def MatordReview(request):
    myquery = list(OrderedMaterial.objects.filter(id_order=request.session['reviews']).values_list("id_material", flat=True))
    #logger.error('selected is: ', myquery)
    OpenClose = (Orders.objects.get(pk=request.session['reviews']))
    if OpenClose.status == 'Open':
        isopen = 'true'
    else:
        isopen = 'false'
    
    table_rev_ord = OrdReviewTable(Orders.objects.filter(pk=request.session['reviews']), template_name="django_tables2/bootstrap4.html")
    RequestConfig(request).configure(table_rev_ord)      

    table_rev_mat = MatReviewTable(OrderedMaterial.objects.filter(id_order=request.session['reviews']), template_name="django_tables2/bootstrap4.html")
    RequestConfig(request).configure(table_rev_mat)
    
    if request.POST.get('compl'):
        ids = list(OrderedMaterial.objects.filter(id_order=request.session['reviews']).values_list("id_material", flat=True))
        counts = list(OrderedMaterial.objects.filter(id_order=request.session['reviews']).values_list("count", flat=True))
        #logger.error('logs: ',ids )
        for i in range(len(ids)):
            b = Materials.objects.get(pk=ids[i])
            b.count = b.count + counts[i]                     
            b.save()
        complete_order = Orders.objects.get(pk = request.session['reviews'])
        complete_order.status = "Completed"
        complete_order.save()
        return redirect('Matorder')
    return render(request, 'app/appfunct/MatordReview.html', {'table_1': table_rev_ord, 'table_2': table_rev_mat, "order": request.session['reviews'], 
                                                              'isopen': isopen})

def MatorderCancel(request):     
    cancel = Orders.objects.all()
    context = {"cancel": cancel}
    if request.POST.get('cancel_id'):
        Orders.objects.filter(id_order=request.POST['cancel_id']).delete()
    return render(request,'app/appfunct/MatorderCancel.html', context)

def MatordlAdd(request):
    table_mat_add = MatOrdAdd(Materials.objects.order_by('name'), template_name="django_tables2/bootstrap4.html")
    RequestConfig(request).configure(table_mat_add)
    selected_objects = AddedMat(Materials.objects.filter(pk = 0), template_name="django_tables2/bootstrap4.html")
    RequestConfig(request).configure(selected_objects)

    if request.POST.get('nextto'):
        request.session['date'] = request.POST.get('datetime')
        request.session['daten'] = request.POST.get('datetimenow')
        
        return render(request, 'app/appfunct/MatordlAdd.html', {'table': table_mat_add, 'addtable': selected_objects, 'access': 'false', 'nextto': 'true',
                                                               'dateset': 'true', 'dateval': request.session['date']})
    
    if request.POST.get('add') and len(request.POST.getlist("checks")) > 0:
        request.session['ids'] = request.POST.getlist("checks")

        pks = request.POST.getlist("checks")
        #logger.error('logs: ', pks, len(request.POST.getlist("checks")))
        selected_objects = AddedMat(Materials.objects.filter(pk__in=pks), template_name="django_tables2/bootstrap4.html")
        RequestConfig(request).configure(selected_objects)    
        return render(request, 'app/appfunct/MatordlAdd.html', {'table': table_mat_add, 'addtable': selected_objects, 'access': 'true', 'nextto': 'true',
                                                               'dateset': 'true', 'dateval': request.session['date']})
    
    if request.POST.get('create'):
        prkeys = request.session["ids"]
        counts = request.POST.getlist("inpt_count")
        prices = (Materials.objects.filter(pk__in=prkeys).values_list('price', flat=True))
               
        b = Orders(date_order =  request.session['daten'], date_complete =  request.session['date'], status = 'Open')
        b.save()
        #Last added order
        lastobj = list(Orders.objects.values_list('id_order').last())
        temp = int(lastobj[0])
        for i in range(len(prices)):
            b = OrderedMaterial(count = int(counts[i]), price = float(prices[i]))          
            b.id_material_id = prkeys[i]
            b.id_order_id = temp
            b.save()
        return redirect('Matorder')
    return render(request, 'app/appfunct/MatordlAdd.html', {'table': table_mat_add, 'addtable': selected_objects, 'access': 'false', 'nextto': 'false',
                                                           'dateset': 'false'})
    
def Create(request):
    table_mat_add = CrtOrd(Materials.objects.order_by('name'), template_name="django_tables2/bootstrap4.html")
    RequestConfig(request).configure(table_mat_add)

    if request.POST.get('next'):
        request.session['date'] = request.POST.get('datetime')
        request.session['daten'] = request.POST.get('datetimenow')
        request.session['oname'] = request.POST.get('oname')
        request.session['odesc'] = request.POST.get('odesc')
        request.session['cids'] = request.POST.getlist("checks")
        return redirect('CNextStep')

    return render(request,'app/tabs/Create.html',  {'table': table_mat_add})

def CNextStep(request):
     if not request.session["cids"]:
          return render(request, 'app/error.html', {'error': 'Nothing has been selected'})

     countlist = list(Materials.objects.filter(pk__in=request.session["cids"]).values_list("count", flat=True))
     #logger.error('logs: ', countlist[0])

     selected_objects = CrtAddedMat(Materials.objects.filter(pk__in = request.session["cids"]), template_name="django_tables2/bootstrap4.html")
     RequestConfig(request).configure(selected_objects)

     if request.method == 'POST':
        prkeys = request.session["cids"]
        counts = request.POST.getlist("inpt_count")
        convert_ocost = float(request.POST.get("ocost"))
        convert_scost = float(request.POST.get("scost"))
        
        prices = Materials.objects.filter(pk__in=prkeys).values_list('price', flat=True)    
        b = BuildOrders(scost =  convert_scost, ocost = convert_ocost , name =  request.session['oname'], desc =  request.session['odesc'], 
                        date_order =  request.session['daten'], date_complete =  request.session['date'], status = 'Open')
        b.save()
        #Last added order
        lastobj = list(BuildOrders.objects.values_list('id_order').last())
        temp = int(lastobj[0])
        try:
            my = request.FILES['files']        
            fs = FileSystemStorage()
            filename = fs.save(str(temp) + ".pdf", my)
        except Exception as e:
            print("File does not exist")

        for i in range(len(prices)):
            a = UsedMaterial(count = int(counts[i]), price = float(prices[i]))          
            a.id_material_id = prkeys[i]
            a.id_order_id = temp
            a.save()

        for i in range(len(prices)):
            c = Materials.objects.get(pk = prkeys[i])
            temp = countlist[i] - int(counts[i]) 
            c.count = temp                
            c.save()
        return redirect('menu')
     return render(request,'app/tabs/CNextStep.html',  {'table': selected_objects, 'countlist': countlist })

def Review(request):
    select = '1'
    table_mat_ord = RewOrdTable(BuildOrders.objects.all(), template_name="django_tables2/bootstrap4.html") 
    if request.POST.get('filter'):
        if request.POST.get('select') == "open":        
            table_mat_ord = RewOrdTable(BuildOrders.objects.filter(status = "Open"), template_name="django_tables2/bootstrap4.html")
            select = '3'
        elif request.POST.get('select') == "completed":
            table_mat_ord = RewOrdTable(BuildOrders.objects.filter(status = "Completed"), template_name="django_tables2/bootstrap4.html")
            select = '2'
        else:
            table_mat_ord = RewOrdTable(BuildOrders.objects.all(), template_name="django_tables2/bootstrap4.html")
            select = '1'
    RequestConfig(request).configure(table_mat_ord)

    if request.POST.get('review'):
        if len(request.POST.getlist("radios")) > 0:
            request.session['reviews'] = request.POST.get('radios')      
            return redirect('OrderReview')
        else:
            return render(request, 'app/error.html', {'error': 'Nothing has been selected'})  
    return render(request, 'app/tabs/Review.html', {'table': table_mat_ord, 'which': select })

def OrderReview(request):
    myquery = list(UsedMaterial.objects.filter(id_order=request.session['reviews']).values_list("id_material", flat=True))
    desk = list(BuildOrders.objects.filter(id_order=request.session['reviews']).values_list("desc", flat=True))
    scost = list(BuildOrders.objects.filter(id_order=request.session['reviews']).values_list("scost", flat=True))
    ocost = list(BuildOrders.objects.filter(id_order=request.session['reviews']).values_list("ocost", flat=True))
    #logger.error('selected is: ', myquery)
    OpenClose = (BuildOrders.objects.get(pk=request.session['reviews']))
    if OpenClose.status == 'Open':
        isopen = 'true'
    else:
        isopen = 'false'

    if os.path.exists("app/media/" + request.session['reviews'] + ".pdf"):
        #logger.error('Fine: ')
        fileexist = 'true'
    else:
        fileexist = 'false'
    table_rev_ord = ReviewOrdTable(BuildOrders.objects.filter(pk=request.session['reviews']), template_name="django_tables2/bootstrap4.html")
    RequestConfig(request).configure(table_rev_ord)      

    table_rev_mat = ReviewMatTable(UsedMaterial.objects.filter(id_order=request.session['reviews']), template_name="django_tables2/bootstrap4.html")
    RequestConfig(request).configure(table_rev_mat)
    if request.POST.get('bp'):
        filename = request.session['reviews'] + ".pdf"
        filepath = os.path.join("app/media/", filename)
        return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

    if request.POST.get('compl'):
        complete_order = BuildOrders.objects.get(pk = request.session['reviews'])
        complete_order.status = "Completed"
        complete_order.save()
        return redirect('Review')
    
    if request.POST.get('cancl'):
        cancel_ids = list(UsedMaterial.objects.filter(id_order=request.session['reviews']).values_list('id_material', flat=True))
        cancel_counts = list(UsedMaterial.objects.filter(id_order=request.session['reviews']).values_list('count', flat=True))
        countlist = list(Materials.objects.filter(pk__in=cancel_ids).values_list("count", flat=True))

        for i in range(len(cancel_ids)):
            c = Materials.objects.get(pk = cancel_ids[i])
            temp = countlist[i] + int(cancel_counts[i]) 
            c.count = temp                
            c.save()
            BuildOrders.objects.filter(id_order=request.session['reviews']).delete()
        return redirect('Review')
    return render(request, 'app/appfunct/OrderReview.html', {'table_1': table_rev_ord, 'table_2': table_rev_mat,'fileexist':fileexist,  
                                                             "order": request.session['reviews'], 'isopen': isopen, 'desk': desk[0], 
                                                             'ocost': ocost[0], 'scost': scost[0] })