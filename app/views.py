"""Definition of views."""from django.shortcuts import render, redirectfrom django.http import HttpRequestfrom django.http import HttpResponsefrom django.http import JsonResponsefrom django.contrib.auth import authenticatefrom django.contrib.auth import login as log from django.contrib.auth import logout as lgoutfrom django.contrib import messagesfrom django.contrib.auth.decorators import login_requiredfrom .models import *from .forms import *import logginglogger = logging.getLogger(__name__)#logger.error('Something went wrong!')def login(request):                      """Renders the home page."""    if request.user.is_authenticated:       return render(request, 'app/menu.html')    if request.POST.get('log'):        username = request.POST['username']        password = request.POST['password']        user = authenticate(request, username=username, password=password)        if user is not None:            log(request, user)            # Redirect to a success page.            return render(request, 'app/menu.html')        else:            # Return an 'invalid login' error message.            messages.error(request,'username or password not correct')            return redirect('login')                      return render(request, 'app/login.html')@login_requireddef menu(request):    return render(request, "app/menu.html")@login_requireddef update_menu(request):    return render(request, "app/update_menu.html")@login_requireddef object_menu(request):    return render(request, "app/object_menu.html")@login_requireddef customer_menu(request):    return render(request, "app/customer_menu.html")@login_requireddef other_menu(request):    return render(request, "app/other_menu.html")def logout(request):    lgout(request)@login_requireddef customers_add(request):    return render(request, "app/customers_add.html")@login_requireddef building_add(request):    #Заказчик в селект    posts1 = Customers.objects.all()     #Типы улиц    posts4 = list(Streets.objects.order_by().values_list('type', flat=True).distinct())    #Финансирование    posts5 = list(Financing.objects.order_by().values_list('name', flat=True))        if request.method == 'POST':        #Комплекс        try:            classType = request.POST.get('class-select')  #класс            complexName = request.POST.get('complex-name')  #Название            try:                checkStreet = Streets.objects.get(name = request.POST.get('name-streets'), type = request.POST.get('type-streets'))            except Streets.DoesNotExist:                streetName = None                  else:                       streetName = checkStreet  #Наименование                  try:                checkCustomer = Customers.objects.get(name = request.POST.get('customer'))            except Customers.DoesNotExist:                customerName = None                else:                         customerName = checkCustomer  #Наименование                 if (request.POST.get('builder') != ""):                builderName = request.POST.get('builder')  #Генподрядчик            else:                builderName = None                           try:                checkSubway = Subways.objects.get(name = request.POST.get('subway'))            except Subways.DoesNotExist:                subwayName = None                       else:                         subwayName = checkSubway  #Наименование            try:                checkArea = Areas.objects.get(name =  request.POST.get('city-area'))            except Areas.DoesNotExist:                cityAreaName = None                         else:                         cityAreaName = checkArea  #Наименование            zoneName = request.POST.get('urban-zone', None)            parkingExist = request.POST.get('parking', None)  #Парковка            parkingType = request.POST.get('parking-type', None)  #Тип парковки                    if (request.POST.get('price-parking-up-hrn1') != "" and request.POST.get('price-parking-up-hrn1') != None):                parkingNum = int(request.POST.get('num-parking-up1'))  #Генподрядчик            else:                parkingNum = None            if (request.POST.get('price-parking-up-hrn1') != "" and request.POST.get('price-parking-up-hrn1') != None):                parkingPriceHrn = float(request.POST.get('price-parking-up-hrn1'))  #Генподрядчик            else:                parkingPriceHrn = None            if (request.POST.get('price-parking-up-dol1') != "" and request.POST.get('price-parking-up-dol1') != None):                parkingPriceDol = float(request.POST.get('price-parking-up-dol1'))  #Генподрядчик            else:                parkingPriceDol = None            complexAdd = Buildings(class_field = classType, name = complexName, street_name = streetName, customer = customerName,                                     builder = builderName, urban_develop_zone = zoneName, subway = subwayName, city_area = cityAreaName, parking = parkingExist,                                     parking_type = parkingType, parking_num = parkingNum, parking_price_hrn = parkingPriceHrn, parking_price_dol = parkingPriceDol)            complexAdd.save()                         #Дома            lastobj = Buildings.objects.last()            counts = request.POST.get('counts-houses') #Количество домов            for i in range(1, int(counts) + 1):                num_build = request.POST.get('num-build' + str(i))  #№ дома                if (request.POST.get('area-build' + str(i)) != "" and request.POST.get('area-build' + str(i)) != None):                    area_build = float(request.POST.get('area-build' + str(i)))  #Площадь дома                else:                    area_build = None                if (request.POST.get('area-apart' + str(i)) != "" and request.POST.get('area-apart' + str(i)) != None):                    area_apart = float(request.POST.get('area-apart' + str(i)))  #Площадь квартир                else:                    area_apart = None                if (request.POST.get('num-storeys' + str(i)) != "" and request.POST.get('num-storeys' + str(i)) != None):                    storeys_num = int(request.POST.get('num-storeys' + str(i))) #Этажность                else:                    storeys_num = None                if (request.POST.get('constr-phase-prc' + str(i)) != "" and request.POST.get('constr-phase-prc' + str(i)) != None):                    phase = request.POST.get('constr-phase-prc' + str(i)) #Этап постройки                else:                    phase = None                if (request.POST.get('info-house' + str(i)) != "" and request.POST.get('info-house' + str(i)) != None):                    info = request.POST.get('info-house' + str(i)) #Примечание                else:                    info = None                        date_start = request.POST.get('date-pick-start' + str(i), None)  #Год начала                date_commis = request.POST.get('date-pick-commis' + str(i), None)  #Год ввода                if (request.POST.get('quarter-pick' + str(i)) != "" and request.POST.get('quarter-pick' + str(i)) != None):                    quarter = int(request.POST.get('quarter-pick' + str(i))) #Квартал                else:                    quarter = None                     if (request.POST.get('num-parking-down' + str(i)) != "" and request.POST.get('num-parking-down' + str(i)) != None):                    parking_nums = int(request.POST.get('num-parking-down' + str(i))) #Стоимость                else:                    parking_nums = None                        if (request.POST.get('price-parking-down-hrn' + str(i)) != "" and request.POST.get('price-parking-down-hrn' + str(i))!= None ):                    parking_hrn = float(request.POST.get('price-parking-down-hrn' + str(i))) #Стоимость                else:                    parking_hrn = None                              if (request.POST.get('price-parking-down-dol' + str(i)) != "" and request.POST.get('price-parking-down-dol' + str(i)) != None):                    parking_dol = float(request.POST.get('price-parking-down-dol' + str(i))) #Стоимость                else:                    parking_dol = None                   houseAdd = Houses(id_buildings = lastobj, street_number = num_build, ttl_area_building = area_build, ttl_area_apartments = area_apart,                                     storeys = storeys_num, construction_phase_prst = phase, parking_num = parking_nums, parking_price_hrn = parking_hrn,                                     parking_price_dol = parking_dol, remark = info, start_year = date_start, commis_year = date_commis, quarter = quarter)                           houseAdd.save()                         counts_second = request.POST.get('counts-sections') #Количество домов            for i in range(1, int(counts_second) + 1):                houseId = Houses.objects.get(street_number = request.POST.get('num-section-house' + str(i)), id_buildings = lastobj)  #№ дом                sale = request.POST.get('sales'+ str(i), None)  #Продажи                try:                    financ = Financing.objects.get(name = request.POST.get('finance'+ str(i))) #Финансирование                except Financing.DoesNotExist:                    financ = None                      dupl = request.POST.get('duplex'+ str(i), None)  #Дюплекс                penth = request.POST.get('penthouse'+ str(i), None)  #Пентхаусы                #Квартиры. От 1км до 4км                if (request.POST.get('num-apart-ttl'+ str(i)) != "" and request.POST.get('num-apart-ttl'+ str(i))!= None ):                    numApartTtl = int(request.POST.get('num-apart-ttl'+ str(i)))                else:                    numApartTtl = None                   if (request.POST.get('avg-area'+ str(i)) != "" and request.POST.get('avg-area'+ str(i))!= None ):                    avgArea = float(request.POST.get('avg-area'+ str(i)))                else:                    avgArea = None                   if (request.POST.get('num-apart-one'+ str(i)) != "" and request.POST.get('num-apart-one'+ str(i))!= None ):                    numApartOne = int(request.POST.get('num-apart-one'+ str(i)))                else:                    numApartOne = None                 if (request.POST.get('min-area-one'+ str(i)) != "" and request.POST.get('min-area-one'+ str(i))!= None ):                    minAreaOne = float(request.POST.get('min-area-one'+ str(i)))                else:                    minAreaOne = None                 if (request.POST.get('max-area-one'+ str(i)) != "" and request.POST.get('max-area-one'+ str(i))!= None ):                    maxAreaOne = float(request.POST.get('max-area-one'+ str(i)))                else:                    maxAreaOne = None                 if (request.POST.get('num-apart-two'+ str(i)) != "" and request.POST.get('num-apart-two'+ str(i))!= None ):                    numApartTwo = int(request.POST.get('num-apart-two'+ str(i)))                else:                    numApartTwo = None                 if (request.POST.get('min-area-two'+ str(i)) != "" and request.POST.get('min-area-two'+ str(i))!= None ):                    minAreaTwo = float(request.POST.get('min-area-two'+ str(i)))                else:                    minAreaTwo = None                             if (request.POST.get('max-area-two'+ str(i)) != "" and request.POST.get('max-area-two'+ str(i))!= None ):                    maxAreaTwo = float(request.POST.get('max-area-two'+ str(i)))                else:                    maxAreaTwo = None                 if (request.POST.get('num-apart-three'+ str(i)) != "" and request.POST.get('num-apart-three'+ str(i))!= None ):                    numApartThree = int(request.POST.get('num-apart-three'+ str(i)))                else:                    numApartThree = None                 if (request.POST.get('min-area-three'+ str(i)) != "" and request.POST.get('min-area-three'+ str(i))!= None ):                    minAreaThree = float(request.POST.get('min-area-three'+ str(i)))                else:                    minAreaThree = None                 if (request.POST.get('max-area-three'+ str(i)) != "" and request.POST.get('max-area-three'+ str(i))!= None ):                    maxAreaThree = float(request.POST.get('max-area-three'+ str(i)))                else:                    maxAreaThree = None                 if (request.POST.get('num-apart-four'+ str(i)) != "" and request.POST.get('num-apart-four'+ str(i))!= None ):                    numApartFour = int(request.POST.get('num-apart-four'+ str(i)))                else:                    numApartFour = None                if (request.POST.get('min-area-four'+ str(i)) != "" and request.POST.get('min-area-four'+ str(i))!= None ):                    minAreaFour = float(request.POST.get('min-area-four'+ str(i)))                else:                    minAreaFour = None                if (request.POST.get('max-area-four'+ str(i)) != "" and request.POST.get('max-area-four'+ str(i))!= None ):                    maxAreaFour = float(request.POST.get('max-area-four'+ str(i)))                else:                    maxAreaFour = None                         sectionAdd = Sections(id_house = houseId, attribute = sale, financing = financ, duplex_apartments = dupl, penthouses = penth,                                         apartments_num = numApartTtl, a1_num = numApartOne, a2_num = numApartTwo, a3_num = numApartThree, a4_num = numApartFour,                                         a1_area_min = minAreaOne, a1_area_max = maxAreaOne, a2_area_min = minAreaTwo, a2_area_max = maxAreaTwo, a3_area_min = minAreaThree,                                        a3_area_max = maxAreaThree, a4_area_min = minAreaFour,  a4_area_max = maxAreaFour, avg_area = avgArea)                sectionAdd.save()        except:            messages.error(request,'Что то пошло не так... Проверьте добавленные данные')                      return redirect('update_menu')    return render(request, "app/building_add.html", {"posts1": posts1, "posts4": posts4, "posts5": posts5 })def getStreets(request):    streets = list(Streets.objects.filter(type = request.GET.get('type')).values_list("name", flat=True))    #Here is where I don't know if I am doing correctly    #I don't know how to send the client list or if I have to send it as a JSON    #Please help here    return JsonResponse({'names': streets }, status=200)def getSubways(request):    subways = list(Subways.objects.filter(zone = request.GET.get('zone')).values_list("name", flat=True))    #Here is where I don't know if I am doing correctly    #I don't know how to send the client list or if I have to send it as a JSON    #Please help here    return JsonResponse({'names': subways }, status=200)def getCityAreas(request):    cityAreas = list(Areas.objects.filter(zone = request.GET.get('zone')).values_list("name", flat=True))    #Here is where I don't know if I am doing correctly    #I don't know how to send the client list or if I have to send it as a JSON    #Please help here    return JsonResponse({'names': cityAreas }, status=200)@login_requireddef customers(request):    instances = Customers.objects.all()    return render(request, "app/customers.html", {"instances": instances})