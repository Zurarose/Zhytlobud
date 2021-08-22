"""Definition of views."""from django.shortcuts import render, redirectfrom django.http import HttpRequestfrom django.http import HttpResponsefrom django.http import JsonResponsefrom django.core import serializersimport jsonfrom django.contrib.auth import authenticatefrom django.contrib.auth import login as log from django.contrib.auth import logout as lgoutfrom django.contrib.auth.forms import UserCreationFormfrom django.contrib import messagesfrom django.contrib.auth.decorators import login_requiredfrom django.db.models import Qfrom .models import *from .forms import *import logginglogger = logging.getLogger(__name__)#logger.error('Something went wrong!')def login(request):                      """Renders the home page."""    if request.user.is_authenticated:       return render(request, 'app/menu.html')    if request.POST.get('log'):        username = request.POST['username']        password = request.POST['password']        user = authenticate(request, username=username, password=password)        if user is not None:            log(request, user)            # Redirect to a success page.            return render(request, 'app/menu.html')        else:            # Return an 'invalid login' error message.            messages.error(request,'username or password not correct')            return redirect('login')                      return render(request, 'app/login.html')@login_requireddef menu(request):    return render(request, "app/menu.html")@login_requireddef update_menu(request):    return render(request, "app/update_menu.html")@login_requireddef object_menu(request):    return render(request, "app/object_menu.html")@login_requireddef customer_menu(request):    return render(request, "app/customer_menu.html")@login_requireddef other_menu(request):    return render(request, "app/other_menu.html")def logout(request):    lgout(request)@login_requireddef register(request):    #Регистрация    if request.method == 'POST':        user_form = UserRegistrationForm(request.POST)        if user_form.is_valid():            try:                # Create a new user object but avoid saving it yet                new_user = user_form.save(commit=False)                # Set the chosen password                new_user.set_password(user_form.cleaned_data['password'])                # Save the User object                user_type = (request.POST.get('type', None))                if user_type != None:                    if user_type == "Аналитик":                        new_user.is_staff = True                                     elif user_type == "Администратор":                        new_user.is_superuser = True                  new_user.save()                return redirect('other_menu')            except Exception as e:                messages.error(request,'Что то пошло не так... Проверьте добавленные данные. Дополнительно: ' + str(e))                          return redirect('other_menu')    else:        user_form = UserRegistrationForm()    return render(request, 'app/register.html', {'user_form': user_form})@login_requireddef customers_add(request):    #Формы собственности    posts1 = Ownership.objects.all()     if request.method == 'POST':        try:            try:                form = Ownership.objects.get(form = request.POST.get('form')) #Форма собственности            except Ownership.DoesNotExist:                form = None            if (request.POST.get('name') != "" and request.POST.get('name') != None):                cust_name = request.POST.get('name')  #Имя            else:                cust_name = None            if (request.POST.get('phone') != "" and request.POST.get('phone') != None):                phoneNum = request.POST.get('phone')  #Телефон            else:                phoneNum = None            if (request.POST.get('date') != "" and request.POST.get('date') != None):                year = request.POST.get('date')  #Год            else:                year = None            custAdd = Customers(ownership = form, name = cust_name, phone = phoneNum, start_work = year)            custAdd.save()            return redirect('customers_edit')        except Exception as e:            messages.error(request,'Что то пошло не так... Проверьте добавленные данные. Дополнительно: ' + str(e))                      return redirect('customers_edit')    return render(request, "app/customers_add.html", {"posts1": posts1})@login_requireddef customers_edit(request):    #Просмотр заказчиков     instances = Customers.objects.all()      if request.POST.get('edit'):        if (request.POST.get('selected') != "" and request.POST.get('selected') != None):            select = request.POST.get('selected')  #Имя        else:            select = None        request.session['select'] = select        return redirect('customers_edit_values')        if request.POST.get('delete'):        try:            if (request.POST.get('selected') != "" and request.POST.get('selected') != None):                delete = request.POST.get('selected')  #Имя            else:                delete = None            Customers.objects.filter(id_customer=delete).delete()            return redirect('customers_edit')        except Exception as e:            messages.error(request,'Что то пошло не так... Не удалось удалить. Дополнительно: ' + str(e))                      return redirect('customers_edit')    return render(request, "app/customers_edit.html", {"instances": instances})@login_requireddef customers_edit_values(request):    #Формы собственности      cust = Customers.objects.get(pk = request.session['select'])    posts1 = Ownership.objects.all()    if request.method == 'POST':        try:            try:                formset = Ownership.objects.get(form = request.POST.get('form')) #Форма собственности            except Ownership.DoesNotExist:                formset = None            if (request.POST.get('name') != "" and request.POST.get('name') != None):                cust_name = request.POST.get('name')  #Имя            else:                cust_name = None            if (request.POST.get('phone') != "" and request.POST.get('phone') != None):                phoneNum = request.POST.get('phone')  #Телефон            else:                phoneNum = None            if (request.POST.get('date') != "" and request.POST.get('date') != None):                year = request.POST.get('date')  #Год            else:                year = None            cust.ownership = formset             cust.name = cust_name             cust.phone = phoneNum             cust.start_work = year             cust.save()            return redirect('customers_edit')        except Exception as e:            messages.error(request,'Что то пошло не так... Проверьте добавленные данные. Дополнительно: ' + str(e))                      return redirect('customers_edit_values')    return render(request, "app/customers_edit_values.html", {"posts1": posts1, "cust": cust})@login_requireddef objects_edit(request):    #Просмотр всех комплексов    instances = Buildings.objects.all()      if request.POST.get('review'):        if (request.POST.get('selected') != "" and request.POST.get('selected') != None):            select = request.POST.get('selected')  #Имя        else:            select = None        request.session['select'] = select        return redirect('objects_review')          return render(request, "app/objects_edit.html", {"instances": instances})@login_requireddef objects_review(request):    #Редактирование и просмотр комплексов    complex = Buildings.objects.get(pk = request.session['select'])    houses = Houses.objects.filter(id_buildings = request.session['select'])    if request.POST.get('delete_complex'):        try:            if 'select' in request.session:                delete = request.session['select']                           Buildings.objects.filter(id_buildings=delete).delete()                return redirect('objects_edit')        except Exception as e:            messages.error(request,'Что то пошло не так... Не удалось удалить комплекс. Дополнительно: ' +  str(e))                      return redirect('objects_review')    if request.POST.get('delete_house'):        try:            if request.POST.get('selected_house'):                delete = request.POST.get('selected_house')                Houses.objects.filter(id_house=delete).delete()                return redirect('objects_review')                 except Exception as e:            messages.error(request,'Что то пошло не так... Не удалось удалить дом. Дополнительно: ' +  str(e))                      return redirect('objects_review')    if request.POST.get('delete_section'):        try:            if request.POST.get('selected_section'):                delete = request.POST.get('selected_section')                Sections.objects.filter(id_sections=delete).delete()                return redirect('objects_review')                  except Exception as e:            messages.error(request,'Что то пошло не так... Не удалось удалить секцию. Дополнительно: ' +  str(e))                      return redirect('objects_review')    if request.POST.get('edit_complex'):        return redirect('object_edit_complex')    return render(request, "app/objects_review.html", {"complex": complex, "houses": houses})@login_requireddef object_edit_complex(request):    #Комплекс    build = Buildings.objects.get(pk = request.session['select'])    #Заказчик в селект    posts1 = Customers.objects.all()     #Типы улиц    posts2 = list(Streets.objects.order_by().values_list('type', flat=True).distinct())    if request.POST.get('save'):        #Комплекс        try:            classType = request.POST.get('class-select')  #класс            complexName = request.POST.get('complex-name')  #Название            try:                checkStreet = Streets.objects.get(name = request.POST.get('name-streets'), type = request.POST.get('type-streets'))            except Streets.DoesNotExist:                streetName = None                  else:                       streetName = checkStreet  #Наименование            try:                checkCustomer = Customers.objects.get(name = request.POST.get('customer'))            except Customers.DoesNotExist:                customerName = None                else:                         customerName = checkCustomer  #Наименование            if (request.POST.get('builder') != ""):                builderName = request.POST.get('builder')  #Генподрядчик            else:                builderName = None                           try:                checkSubway = Subways.objects.get(name = request.POST.get('subway'))            except Subways.DoesNotExist:                subwayName = None                       else:                         subwayName = checkSubway  #Наименование            try:                checkArea = Areas.objects.get(name =  request.POST.get('city-area'))            except Areas.DoesNotExist:                cityAreaName = None                         else:                         cityAreaName = checkArea  #Наименование            zoneName = request.POST.get('urban-zone', None)            parkingExist = request.POST.get('parking', None)  #Парковка            parkingType = request.POST.get('parking-type', None)  #Тип парковки                    if (request.POST.get('price-parking-up-hrn') != "" and request.POST.get('price-parking-up-hrn') != None):                parkingNum = int(request.POST.get('num-parking-up'))  #Генподрядчик            else:                parkingNum = None            if (request.POST.get('price-parking-up-hrn_min') != "" and request.POST.get('price-parking-up-hrn_min') != None):                parkingPriceHrn_min = float(request.POST.get('price-parking-up-hrn_min'))  #Генподрядчик            else:                parkingPriceHrn_min = None            if (request.POST.get('price-parking-up-dol_min') != "" and request.POST.get('price-parking-up-dol_min') != None):                parkingPriceDol_min = float(request.POST.get('price-parking-up-dol_min'))  #Генподрядчик            else:                parkingPriceDol_min = None            if (request.POST.get('price-parking-up-hrn_max') != "" and request.POST.get('price-parking-up-hrn_max') != None):                parkingPriceHrn_max = float(request.POST.get('price-parking-up-hrn_max'))  #Генподрядчик            else:                parkingPriceHrn_max = None            if (request.POST.get('price-parking-up-dol_max') != "" and request.POST.get('price-parking-up-dol_max') != None):                parkingPriceDol_max = float(request.POST.get('price-parking-up-dol_max'))  #Генподрядчик            else:                parkingPriceDol_max = None            build.class_field = classType             build.name = complexName             build.street_name = streetName            build.customer = customerName            build.builder = builderName            build.urban_develop_zone = zoneName            build.subway = subwayName            build.city_area = cityAreaName            build.parking = parkingExist             build.parking_type = parkingType            build.parking_num = parkingNum            build.parking_price_hrn_min = parkingPriceHrn_min            build.parking_price_dol_min = parkingPriceDol_min            build.parking_price_hrn_max = parkingPriceHrn_max            build.parking_price_dol_max = parkingPriceDol_max            build.save()              if parkingType == "Надземная":                house = Houses.objects.filter(id_buildings = request.session['select']).values_list('id_house', flat=True)                for i in range(len(house)):                    house = Houses.objects.filter(id_house = i)                    house.parking_num = None                    house.parking_price_hrn_min = None                    house.parking_price_dol_min = None                    house.parking_price_hrn_max = None                    house.parking_price_dol_max = None            return redirect('objects_review')        except Exception as e:            messages.error(request,'Что то пошло не так... Не удалось сохранить изменения. Дополнительно: ' +  str(e))                      return redirect('objects_review')    return render(request, "app/object_edit_complex.html", {"posts1": posts1, "posts2": posts2, "build": build})    @login_requireddef building_add(request):    #Заказчик в селект    posts1 = Customers.objects.all()     #Типы улиц    posts4 = list(Streets.objects.order_by().values_list('type', flat=True).distinct())    #Финансирование    posts5 = list(Financing.objects.order_by().values_list('name', flat=True))        if request.method == 'POST':        #Комплекс        try:            classType = request.POST.get('class-select')  #класс            complexName = request.POST.get('complex-name')  #Название            try:                checkStreet = Streets.objects.get(name = request.POST.get('name-streets'), type = request.POST.get('type-streets'))            except Streets.DoesNotExist:                streetName = None                  else:                       streetName = checkStreet  #Наименование            try:                checkCustomer = Customers.objects.get(name = request.POST.get('customer'))            except Customers.DoesNotExist:                customerName = None                else:                         customerName = checkCustomer  #Наименование            if (request.POST.get('builder') != ""):                builderName = request.POST.get('builder')  #Генподрядчик            else:                builderName = None                           try:                checkSubway = Subways.objects.get(name = request.POST.get('subway'))            except Subways.DoesNotExist:                subwayName = None                       else:                         subwayName = checkSubway  #Наименование            try:                checkArea = Areas.objects.get(name =  request.POST.get('city-area'))            except Areas.DoesNotExist:                cityAreaName = None                         else:                         cityAreaName = checkArea  #Наименование            zoneName = request.POST.get('urban-zone', None)            parkingExist = request.POST.get('parking', None)  #Парковка            parkingType = request.POST.get('parking-type', None)  #Тип парковки                    if (request.POST.get('num-parking-up') != "" and request.POST.get('num-parking-up') != None):                parkingNum = int(request.POST.get('num-parking-up'))  #кол-во мест            else:                parkingNum = None            if (request.POST.get('price-parking-up-hrn_min') != "" and request.POST.get('price-parking-up-hrn_min') != None):                parkingPriceHrn_min = float(request.POST.get('price-parking-up-hrn_min'))  #мин цена            else:                parkingPriceHrn_min = None            if (request.POST.get('price-parking-up-dol_min') != "" and request.POST.get('price-parking-up-dol_min') != None):                parkingPriceDol_min = float(request.POST.get('price-parking-up-dol_min'))  #мин цена            else:                parkingPriceDol_min = None            if (request.POST.get('price-parking-up-hrn_max') != "" and request.POST.get('price-parking-up-hrn_max') != None):                parkingPriceHrn_max = float(request.POST.get('price-parking-up-hrn_max'))  #макс цена            else:                parkingPriceHrn_max = None            if (request.POST.get('price-parking-up-dol_max') != "" and request.POST.get('price-parking-up-dol_max') != None):                parkingPriceDol_max = float(request.POST.get('price-parking-up-dol_max'))  #макс цена            else:                parkingPriceDol_max = None            complexAdd = Buildings(class_field = classType, name = complexName, street_name = streetName, customer = customerName,                                     builder = builderName, urban_develop_zone = zoneName, subway = subwayName, city_area = cityAreaName, parking = parkingExist,                                     parking_type = parkingType, parking_num = parkingNum, parking_price_hrn_min = parkingPriceHrn_min, parking_price_dol_min = parkingPriceDol_min,                                     parking_price_hrn_max = parkingPriceHrn_max, parking_price_dol_max = parkingPriceDol_max)            complexAdd.save()                         #Дома            lastobj = Buildings.objects.last()            counts = request.POST.get('counts-houses') #Количество домов            for i in range(1, int(counts) + 1):                num_build = request.POST.get('num-build' + str(i))  #№ дома                if (request.POST.get('area-build' + str(i)) != "" and request.POST.get('area-build' + str(i)) != None):                    area_build = float(request.POST.get('area-build' + str(i)))  #Площадь дома                else:                    area_build = None                if (request.POST.get('area-apart' + str(i)) != "" and request.POST.get('area-apart' + str(i)) != None):                    area_apart = float(request.POST.get('area-apart' + str(i)))  #Площадь квартир                else:                    area_apart = None                if (request.POST.get('num-storeys' + str(i)) != "" and request.POST.get('num-storeys' + str(i)) != None):                    storeys_num = int(request.POST.get('num-storeys' + str(i))) #Этажность                else:                    storeys_num = None                if (request.POST.get('constr-phase-prc' + str(i)) != "" and request.POST.get('constr-phase-prc' + str(i)) != None):                    phase = request.POST.get('constr-phase-prc' + str(i)) #Этап постройки                else:                    phase = None                if (request.POST.get('info-house' + str(i)) != "" and request.POST.get('info-house' + str(i)) != None):                    info = request.POST.get('info-house' + str(i)) #Примечание                else:                    info = None                             if (request.POST.get('date-pick-start' + str(i)) != "" and request.POST.get('date-pick-start' + str(i)) != None):                    date_start = request.POST.get('date-pick-start' + str(i)) #Год начала                else:                    date_start = None                    if (request.POST.get('date-pick-commis' + str(i)) != "" and request.POST.get('date-pick-commis' + str(i)) != None):                    date_commis = request.POST.get('date-pick-commis' + str(i)) #Год ввода                else:                    date_commis = None                    if (request.POST.get('quarter-pick' + str(i)) != "" and request.POST.get('quarter-pick' + str(i)) != None):                    quarter = int(request.POST.get('quarter-pick' + str(i))) #Квартал                else:                    quarter = None                     if (request.POST.get('num-parking-down' + str(i)) != "" and request.POST.get('num-parking-down' + str(i)) != None):                    parking_nums = int(request.POST.get('num-parking-down' + str(i))) #Стоимость                else:                    parking_nums = None                       #___________________________________________________________________________________________                if (request.POST.get('price-parking-up-hrn_min' + str(i)) != "" and request.POST.get('price-parking-up-hrn_min' + str(i)) != None):                    parking_hrn_min = float(request.POST.get('price-parking-up-hrn_min' + str(i))) #мин стоимость                else:                    parking_hrn_min = None                              if (request.POST.get('price-parking-up-dol_min' + str(i)) != "" and request.POST.get('price-parking-up-dol_min' + str(i)) != None):                    parking_dol_min = float(request.POST.get('price-parking-up-dol_min' + str(i))) #мин стоимость                else:                    parking_dol_min = None                if (request.POST.get('price-parking-up-hrn_max' + str(i)) != "" and request.POST.get('price-parking-up-hrn_max' + str(i)) != None):                    parking_hrn_max = float(request.POST.get('price-parking-up-hrn_max' + str(i))) #макс стоимость                else:                    parking_hrn_max = None                              if (request.POST.get('price-parking-up-dol_max' + str(i)) != "" and request.POST.get('price-parking-up-dol_max' + str(i)) != None):                    parking_dol_max = float(request.POST.get('price-parking-up-dol_max' + str(i))) #макс стоимость                else:                    parking_dol_max = None                houseAdd = Houses(id_buildings = lastobj, street_number = num_build, ttl_area_building = area_build, ttl_area_apartments = area_apart,                                     storeys = storeys_num, construction_phase_prst = phase, parking_num = parking_nums, parking_price_hrn_min = parking_hrn_min,                                     parking_price_dol_min = parking_dol_min, parking_price_hrn_max = parking_hrn_max, parking_price_dol_max = parking_dol_max,                                    remark = info, start_year = date_start, commis_year = date_commis, quarter = quarter)                           houseAdd.save()                         counts_second = request.POST.get('counts-sections') #Количество домов            for i in range(1, int(counts_second) + 1):                houseId = Houses.objects.get(street_number = request.POST.get('num-section-house' + str(i)), id_buildings = lastobj)  #№ дом                sale = request.POST.get('sales' + str(i), None)  #Продажи                try:                    financ = Financing.objects.get(name = request.POST.get('finance' + str(i))) #Финансирование                except Financing.DoesNotExist:                    financ = None                      dupl = request.POST.get('duplex' + str(i), None)  #Дюплекс                penth = request.POST.get('penthouse' + str(i), None)  #Пентхаусы                #Квартиры.  От 1км до 4км                if (request.POST.get('num-apart-ttl' + str(i)) != "" and request.POST.get('num-apart-ttl' + str(i)) != None):                    numApartTtl = int(request.POST.get('num-apart-ttl' + str(i)))                else:                    numApartTtl = None                   if (request.POST.get('avg-area' + str(i)) != "" and request.POST.get('avg-area' + str(i)) != None):                    avgArea = float(request.POST.get('avg-area' + str(i)))                else:                    avgArea = None                   if (request.POST.get('num-apart-one' + str(i)) != "" and request.POST.get('num-apart-one' + str(i)) != None):                    numApartOne = int(request.POST.get('num-apart-one' + str(i)))                else:                    numApartOne = None                 if (request.POST.get('min-area-one' + str(i)) != "" and request.POST.get('min-area-one' + str(i)) != None):                    minAreaOne = float(request.POST.get('min-area-one' + str(i)))                else:                    minAreaOne = None                 if (request.POST.get('max-area-one' + str(i)) != "" and request.POST.get('max-area-one' + str(i)) != None):                    maxAreaOne = float(request.POST.get('max-area-one' + str(i)))                else:                    maxAreaOne = None                 if (request.POST.get('num-apart-two' + str(i)) != "" and request.POST.get('num-apart-two' + str(i)) != None):                    numApartTwo = int(request.POST.get('num-apart-two' + str(i)))                else:                    numApartTwo = None                 if (request.POST.get('min-area-two' + str(i)) != "" and request.POST.get('min-area-two' + str(i)) != None):                    minAreaTwo = float(request.POST.get('min-area-two' + str(i)))                else:                    minAreaTwo = None                             if (request.POST.get('max-area-two' + str(i)) != "" and request.POST.get('max-area-two' + str(i)) != None):                    maxAreaTwo = float(request.POST.get('max-area-two' + str(i)))                else:                    maxAreaTwo = None                 if (request.POST.get('num-apart-three' + str(i)) != "" and request.POST.get('num-apart-three' + str(i)) != None):                    numApartThree = int(request.POST.get('num-apart-three' + str(i)))                else:                    numApartThree = None                 if (request.POST.get('min-area-three' + str(i)) != "" and request.POST.get('min-area-three' + str(i)) != None):                    minAreaThree = float(request.POST.get('min-area-three' + str(i)))                else:                    minAreaThree = None                 if (request.POST.get('max-area-three' + str(i)) != "" and request.POST.get('max-area-three' + str(i)) != None):                    maxAreaThree = float(request.POST.get('max-area-three' + str(i)))                else:                    maxAreaThree = None                 if (request.POST.get('num-apart-four' + str(i)) != "" and request.POST.get('num-apart-four' + str(i)) != None):                    numApartFour = int(request.POST.get('num-apart-four' + str(i)))                else:                    numApartFour = None                if (request.POST.get('min-area-four' + str(i)) != "" and request.POST.get('min-area-four' + str(i)) != None):                    minAreaFour = float(request.POST.get('min-area-four' + str(i)))                else:                    minAreaFour = None                if (request.POST.get('max-area-four' + str(i)) != "" and request.POST.get('max-area-four' + str(i)) != None):                    maxAreaFour = float(request.POST.get('max-area-four' + str(i)))                else:                    maxAreaFour = None                         sectionAdd = Sections(id_house = houseId, attribute = sale, financing = financ, duplex_apartments = dupl, penthouses = penth,                                         apartments_num = numApartTtl, a1_num = numApartOne, a2_num = numApartTwo, a3_num = numApartThree, a4_num = numApartFour,                                         a1_area_min = minAreaOne, a1_area_max = maxAreaOne, a2_area_min = minAreaTwo, a2_area_max = maxAreaTwo, a3_area_min = minAreaThree,                                        a3_area_max = maxAreaThree, a4_area_min = minAreaFour,  a4_area_max = maxAreaFour, avg_area = avgArea)                sectionAdd.save()            #to num sections            housesToNum = Houses.objects.filter(id_buildings = lastobj.id_buildings).values_list("id_house", flat=True)            logger.error(len(housesToNum))            for i in range(len(housesToNum)):                SectionsToNum = Sections.objects.filter(id_house = housesToNum[i]).values_list("id_sections", flat=True)                       logger.error(SectionsToNum.count())                for j in range(SectionsToNum.count()):                    SectionNuming = Sections.objects.get(id_sections = SectionsToNum[j])                    SectionNuming.number = j + 1                    SectionNuming.save()            request.session['select'] = lastobj.id_buildings            return redirect('objects_review')        except Exception as e:            messages.error(request,'Что то пошло не так... Проверьте добавленные данные. Дополнительно: ' +  str(e))                      return redirect('object_menu')    return render(request, "app/building_add.html", {"posts1": posts1, "posts4": posts4, "posts5": posts5 })@login_requireddef getStreets(request):    streets = list(Streets.objects.filter(type = request.GET.get('type')).values_list("name", flat=True))    return JsonResponse({'names': streets }, status=200)@login_requireddef getSubways(request):    subways = list(Subways.objects.filter(zone = request.GET.get('zone')).values_list("name", flat=True))    return JsonResponse({'names': subways }, status=200)@login_requireddef getCityAreas(request):    cityAreas = list(Areas.objects.filter(zone = request.GET.get('zone')).values_list("name", flat=True))    return JsonResponse({'names': cityAreas }, status=200)def getSection(request):    try:        Section = list(Sections.objects.filter(id_house = request.GET.get('selected')).values_list("id_sections", "number", "attribute","financing__name","duplex_apartments",                                                                                               "penthouses","apartments_num","avg_area","a1_num", "a1_area_min",                                                                                                "a1_area_max","a2_num", "a2_area_min", "a2_area_max","a3_num",                                                                                                "a3_area_min", "a3_area_max","a4_num", "a4_area_min", "a4_area_max"))    except:        return redirect('objects_review')    return JsonResponse({'objects': Section }, status=200)