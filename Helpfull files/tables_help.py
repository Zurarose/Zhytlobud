# tutorial/tables.py
import django_tables2 as tables
from .models import *

class MatTable(tables.Table):
    id_material = tables.Column(verbose_name="ID")
    class Meta:
        model = Materials
        # add class="paleblue" to <table> tag
        attrs = {"class": "table table-striped table-hover col-12"}
        #attrs={"td": {"class": "table-light "}}
        #sequence - последовательность

class MatOrdTable(tables.Table):
    selection = tables.TemplateColumn('<input type="radio" name="radios" value="{{ record.pk }}" />', verbose_name="Select", orderable=False)
    id_order = tables.Column(verbose_name="ID")
    class Meta:
        model = Orders
        attrs = {"class": "table table-striped table-hover col-12"}
        attrs = {"td": {"class": "wdt"}}
        
class MatOrdAdd(tables.Table):
    selection = tables.TemplateColumn('<input type="checkbox" name="checks" value="{{ record.pk }}" />', verbose_name="Select", orderable=False)
    id_material = tables.Column(orderable=False,verbose_name="ID")
    name = tables.Column(orderable=False)
    structure = tables.Column(orderable=False)
    unit = tables.Column(orderable=False)
    manufacturer = tables.Column(orderable=False)
    count = tables.Column(orderable=False)
    price = tables.Column(orderable=False)

    class Meta:
        model = Materials
        attrs = {"class": "table table-striped table-hover col-12"}

class AddedMat(tables.Table):
    count = tables.TemplateColumn('<input type="number" min="1" required class="inpt" name="inpt_count" style="width: 5em;"/>', verbose_name="Count", orderable=False)
    #total = tables.TemplateColumn('<input class="tab1" style="width: 5em;"
    #type="text" disabled value="0" />', verbose_name="Total price",
    #orderable=False)
    total = tables.Column(attrs={"td": {"name": 'prices', "class": "vtotal"}}, verbose_name="Total price", orderable=False, default='0')   
    price = tables.Column(attrs={"td": {"class": "vprice"}}, orderable=False)

    id_material =  tables.Column(orderable=False,verbose_name="ID")
    name =  tables.Column(orderable=False)
    structure =  tables.Column(orderable=False)

    class Meta:
        model = Materials
        attrs = {"class": "table table-bordered border-primary col-12"}
        fields = ('id_material', 'name', 'structure',"price") # fields to display

class OrdReviewTable(tables.Table):
    id_order = tables.Column(orderable=False , verbose_name="ID") 
    date_order = tables.Column(orderable=False) 
    date_complete = tables.Column(orderable=False) 
    status = tables.Column(orderable=False) 

    class Meta:
        model = Orders
        attrs = {"td": {"class": "wdt"}}
        fields = ('id_order', 'date_order', 'date_complete', 'status')

class MatReviewTable(tables.Table):
    ID = tables.Column(attrs={"td": {"class": "pk"}}, accessor='id_material.id_material', verbose_name="ID", orderable=False)
    price = tables.Column(attrs={"td": {"class": "vprice"}}, orderable=False)
    count = tables.Column(attrs={"td": {"class": "vcount"}}, orderable=False)
    class Meta:
        model = OrderedMaterial

        fields = ('ID','count', 'price')

class CrtOrd(tables.Table):
    selection = tables.TemplateColumn('<input type="checkbox" name="checks" value="{{ record.pk }}" />', verbose_name="Select", orderable=False)
    id_material = tables.Column(orderable=False, verbose_name="ID")
    name = tables.Column(orderable=False)
    structure = tables.Column(orderable=False)
    unit = tables.Column(orderable=False)
    manufacturer = tables.Column(orderable=False, verbose_name="Manuf.")
    count = tables.Column(orderable=False)
    price = tables.Column(orderable=False)

    class Meta:
        model = Materials
        attrs = {"class": "table table-striped table-hover col-12"}

class CrtAddedMat(tables.Table):
    count = tables.TemplateColumn('<input type="number" min="1" required class="inpt" value="0" name="inpt_count" style="width: 5em;"/>', verbose_name="Count", orderable=False)
    total = tables.Column(attrs={"td": {"name": 'prices', "class": "vtotal"}}, verbose_name="Total price", orderable=False, default='0')   
    price = tables.Column(attrs={"td": {"class": "vprice"}}, orderable=False)

    id_material =  tables.Column(orderable=False, verbose_name="ID")
    name =  tables.Column(orderable=False)
    structure =  tables.Column(orderable=False)
    manufacturer =  tables.Column(orderable=False)

    class Meta:
        model = Materials
        attrs = {"class": "table table-bordered border-primary col-12"}
        fields = ('id_material', 'name', 'structure', 'manufacturer',"price")

class RewOrdTable(tables.Table):
    selection = tables.TemplateColumn('<input type="radio" name="radios" value="{{ record.pk }}" />', verbose_name="Select", orderable=False)
    id_order = tables.Column(verbose_name="ID")
    class Meta:
        model = BuildOrders
        attrs = {"class": "table table-striped table-hover col-12"}
        attrs = {"td": {"class": "wdt"}}

        fields = ('id_order','name', 'date_order', 'date_complete', 'status')


class ReviewOrdTable(tables.Table):
    id_order = tables.Column(orderable=False , verbose_name="ID") 
    name = tables.Column(orderable=False) 
    date_order = tables.Column(orderable=False) 
    date_complete = tables.Column(orderable=False) 
    status = tables.Column(orderable=False) 

    class Meta:
        model = BuildOrders
        attrs = {"td": {"class": "wdt"}}
        fields = ('id_order', 'name', 'date_order', 'date_complete', 'status')

class ReviewMatTable(tables.Table):
    ID = tables.Column(attrs={"td": {"class": "pk"}}, accessor='id_material.id_material', verbose_name="ID", orderable=False)
    price = tables.Column(attrs={"td": {"class": "vprice"}}, orderable=False)
    count = tables.Column(attrs={"td": {"class": "vcount"}}, orderable=False)
    class Meta:
        model = UsedMaterial

        fields = ('ID','count', 'price')