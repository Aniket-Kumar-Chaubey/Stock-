from navigation import salseform
from django.shortcuts import render, redirect
from .itemforms import itemForm
from .vendorforms import vendorForm
from .customerforms import customerForm
from .purchesforms import purchesForm
from .pricingschemeforms import pricingshemeForm
from django.http import HttpResponse
from .models import *
from .salseform import*
from .paymentform import paymentvoucherForm
from django.http import JsonResponse
from collections import OrderedDict
import itertools 
 
import copy
import xlwt
import decimal
globaldict={}
a=0
Pgst=[]
Sgst=[]
#dropdwon function test
def drptest():
    print("in in drp test")



# Create your views here.
def mainpage(request):
    return render(request, 'mainpage.html')
def about(request):
    return render(request, 'about.html')


def item_something(request):
    form = itemForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            idd=item.objects.last().id
            formm=item.objects.get(pk=idd)
            formm.itemcode="ICODE000"+str(idd)
            formm.save()
            print(formm.itemcode)
            return redirect('navigation:createitem')
        else:
            print(form.errors)

    it= item.objects.all()
    pscheme=pricingscheme.objects.all()
    print(it)
    context = {'form':form, 'itm':it,'pscheme':pscheme}
    print('GET', form.data)
    return render(request, 'item.html', context)



#vendor list crud view
def createitem(request):
    items = item.objects.all()
    print(items)
    print("itemview")
    return render(request,'createitem.html', {'items': items})



#item update
def update_item(request, id):
    if request.method=='POST':
        pi = item.objects.get(pk=id)
        form = itemForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            return redirect('navigation:createitem')
    else:
        pi = item.objects.get(pk=id)
        form = itemForm(instance=pi)

    return render(request, 'updateitem.html', {'form':form})

#item view
def view_item(request, id):
    print()
    if request.method == 'POST':
        pi = item.objects.get(pk=id)
        form = itemForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            return redirect('navigation:createitem')
    else:
        pi = item.objects.get(pk=id)
        form = itemForm(instance=pi)



    return render(request, 'viewitem.html', {'form': form})




#item delete
def delete_item(request, id):
    if request.method=='POST':
        pi = item.objects.get(pk=id)
        pi.delete()
        return redirect('navigation:createitem')


def vendor_something(request):
    form = vendorForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            idd=vendor.objects.last().id
            formm=vendor.objects.get(pk=idd)
            formm.vcode="VCODE000"+str(idd)
            formm.save()
            return redirect('navigation:vendor')
        else:
            print(form.errors)

    vn= vendor.objects.all()
    print(vn)
    context = {'form':form, 'vnd':vn}
    print('GET', form.data)
    return render(request, 'vendor.html', context)



#vendor list crud view
def createvendor(request):
    vendors = vendor.objects.all()
    print(vendors)
    return render(request,'createvendor.html', {'vendors': vendors})

#vendor update
def update_vendor(request, id):
    if request.method=='POST':
        pi = vendor.objects.get(pk=id)
        form = vendorForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            return redirect('navigation:createvendor')
    else:
        pi = vendor.objects.get(pk=id)
        form = vendorForm(instance=pi)

    return render(request, 'updatevendor.html', {'form':form})

#vendor view
def view_vendor(request, id):
    if request.method == 'POST':
        pi = vendor.objects.get(pk=id)
        form = vendorForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            return redirect('navigation:createvendor')
    else:
        pi = vendor.objects.get(pk=id)
        form = vendorForm(instance=pi)



    return render(request, 'viewvendor.html', {'form': form})




#vendor delete
def delete_vendor(request, id):
    if request.method=='POST':
        pi = vendor.objects.get(pk=id)
        pi.delete()
        return redirect('navigation:createvendor')



def purchase(request):
    vcodedata=vendor.objects.all()
    itemcodedata=item.objects.all()

    form = purchesForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            print(form)
            print("----___------")
            print(purchesinvoice.objects.all())
            form.save()

            idd=purchesinvoice.objects.last().id
            formm=purchesinvoice.objects.get(pk=idd)
            formm.invoiceno="PIV00"+str(idd)
            formm.batchno="BTN-00"+str(idd)
            formm.save()

            return redirect('navigation:createpurchase')
        else:
            print(form.errors)

    return render(request, 'purchase.html',{"vcodedata":vcodedata,"itemcodedata":itemcodedata})




#view purchesinvoice
def createpurchase(request):
    items = purchesinvoice.objects.all()
    testAr=[]
    # print(items)
    # print("itemviewpuches")
    print(list(salseinvoice.objects.filter().values('batchno')))
    for i in list(salseinvoice.objects.filter().values('batchno')):
        testAr.append(i['batchno'])
    print(testAr)    
    return render(request,'createpurchase.html', {'items': items,'testAr':testAr})

def delete_purchase(request, id):
    if request.method=='POST':
        pi = purchesinvoice.objects.get(pk=id)
        pi.delete()
        return redirect('navigation:createpurchase')


def view_purchase(request, id):
    pi = purchesinvoice.objects.get(pk=id)
    form=purchesinvoice.objects.get(pk=id)
    viw=purchesinvoice.objects.filter(itemcode='ICODE00032')
    print(viw)
    return render(request, 'viewpurchase.html', {'form': form})        
def update_purchase(request, id):
    if request.method=='POST':
        pi = purchesinvoice.objects.get(pk=id)
        form = purchesForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            return redirect('navigation:createpurchase')
    else:
        pi = purchesinvoice.objects.get(pk=id)
        #form = purchesForm(instance=pi)
        form=purchesinvoice.objects.get(pk=id)

    return render(request, 'updatepurchase.html', {'form':form})

def loadvcode(request):
    print(request)
    vcodee=request.GET.get('vcode')
    vrow=vendor.objects.filter(vcode=vcodee)
    print(list(vrow))
    return JsonResponse(list(vrow.values('id', 'vname','vadd','gstn')), safe=False)
def loaditemcode(request):
    print(request)
    icodee=request.GET.get('itemcode')
    print("itemcode  ---------------------    ",icodee)
    irow=item.objects.filter(itemcode=icodee)
    #print(list(irow))
    data=list(irow.values('id','desc','uom'))
    itemcocode_batchno=list(purchesinvoice.objects.filter(itemcode=icodee).values('id','batchno'))
    itemd=[x['batchno'] for x in itemcocode_batchno]
   
    sals=list(salseinvoice.objects.filter(itemcode=icodee).values('batchno'))
    salsd=[x['batchno'] for x in sals]
    finaldata=[x for x in itemd if x not in salsd]
    data.append(finaldata)
    print("fgh",finaldata)
    #print(data)
    return JsonResponse(data, safe=False)  
#loaditem code for salse
def loaditemcodes(request):
    print(request)
    icodee=request.GET.get('itemcode')
    print("itemcode  ---------------------    ",icodee)
    irow=item.objects.filter(itemcode=icodee)
    #print(list(irow))
    data=list(irow.values('id','desc','uom'))
    itemcocode_batchno=list(purchesinvoice.objects.filter(itemcode=icodee).values('id','batchno'))
    print("fgh",list(salseinvoice.objects.filter(itemcode=icodee).values('batchno'))[1])
    data.append(itemcocode_batchno)
    #print(data)
    return JsonResponse(data, safe=False)    

#Stock Report
def stock(request):
    res=list(purchesinvoice.objects.values('itemcode'))
    itemcodedata=[]
    for i in res:
        if i["itemcode"] not in itemcodedata:
            itemcodedata.append(i["itemcode"])
    
    datadict={}
    resdata={} 
    salsedatadict={}
    salseprim={}
    ressalse={}
    for itm in itemcodedata:
        data=list(purchesinvoice.objects.filter(itemcode=itm).values('id','batchno','quantity','uom','amount','totalamount','unitprice'))
        for temp in data:
            temp['tax']=temp['totalamount']-temp['amount']
            temp['salsetax']=0
            temp['salseamount']=0
            temp['salseuom']=''
            temp['salsequantity']=0
            datadict[temp['batchno']]=temp
        print(itm) 
        resdata[itm]=copy.deepcopy(datadict)
        
        datadict.clear()   
    for itm in itemcodedata:
            salsedata=list(salseinvoice.objects.filter(itemcode=itm).values('id','batchno','quantity','uom','amount','totalamount'))
            for temp in salsedata:
                salseprim['salsetax']=temp['totalamount']-temp['amount']
                salseprim['salseamount']=temp['amount']
                salseprim['salseuom']=temp['uom']
                salseprim['salsequantity']=temp['quantity']
                salsedatadict[temp['batchno']]=copy.deepcopy(salseprim)
            ressalse[itm]=copy.deepcopy(salsedatadict) 
            print(salsedatadict)
            salsedatadict.clear()       
    totalstockq=0
    totalstockv=0
    for key,value in resdata.items():
        for ke,val in value.items():
            try:
                val.update(ressalse[key][ke])
                value[ke]['stockqua']=value[ke]['quantity']-value[ke]['salsequantity']
                value[ke]['stockval']=(value[ke]['quantity']-value[ke]['salsequantity'])*value[ke]['unitprice']
                totalstockq=totalstockq+value[ke]['stockqua']
                totalstockv=totalstockv+value[ke]['stockval']
            except:
                value[ke]['stockqua']=value[ke]['quantity'] 
                value[ke]['stockval']=(value[ke]['quantity'])*value[ke]['unitprice'] 
                totalstockq=totalstockq+value[ke]['stockqua']  
                totalstockv=totalstockv+value[ke]['stockval']
        value['Total Stock Qty']=totalstockq
        value['Total Stock Value']=totalstockv
        totalstockq=0  
        totalstockv=0      
                    

    # for key,value in resdata.items():
    #     print(key)
    #     print(value)
    #print(ressalse)
    global globaldict
    globaldict = copy.deepcopy(resdata)
    
    return render(request, 'stock.html',{"resdata":resdata})

def payment(request):
    return render(request, 'payments.html')

#customer
def customer_something(request):
    form = customerForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            
            idd=customer.objects.last().id
            formm=customer.objects.get(pk=idd)
            formm.cust_code="CUS000"+str(idd)
            #formm.batchno="BTN-00"+str(idd)
            formm.save()
            return redirect('navigation:customer')
        else:
            print(form.errors)

    cs= customer.objects.all()
    print(cs)
    context = {'form':form, 'cus':cs}
    print('GET', form.data)
    return render(request, 'customer.html', context)



#customer list crud view
def createcustomer(request):
    customers = customer.objects.all()
    print(customers)
    return render(request,'createcustomer.html', {'customers': customers})

#customer update
def update_customer(request, id):
    if request.method=='POST':
        pi = customer.objects.get(pk=id)
        form = customerForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            return redirect('navigation:createcustomer')
    else:
        pi = customer.objects.get(pk=id)
        form = customerForm(instance=pi)

    return render(request, 'updatecustomer.html', {'form':form})

#customer view
def view_customer(request, id):
    if request.method == 'POST':
        pi = customer.objects.get(pk=id)
        form = customerForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            return redirect('navigation:createcustomer')
    else:
        pi = customer.objects.get(pk=id)
        form = customerForm(instance=pi)



    return render(request, 'viewcustomer.html', {'form': form})




#customer delete
def delete_customer(request, id):
    if request.method=='POST':
        pi = customer.objects.get(pk=id)
        pi.delete()
        return redirect('navigation:createcustomer')



# Pricing Page
def pricing(request):
    pricing=pricingshemeForm()
    form=pricingshemeForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('navigation:createcustomer')
        else:
            print(form.errors)
    return render(request, 'pricing.html')
def createpricing(request):
    pricing=pricingscheme.objects.all()
    return render(request,'createpricingscheme.html', {'pricing': pricing})


def delete_pricing(request, id):
    if request.method=='POST':
        pi = pricingscheme.objects.get(pk=id)
        pi.delete()
        return redirect('navigation:createpricing')


def view_pricing(request, id):
    pi = pricingscheme.objects.get(pk=id)
    form=pricingscheme.objects.get(pk=id)
    return render(request, 'viewpricing.html', {'form': form})



def update_pricing(request, id):
    if request.method=='POST':
        pi = pricingscheme.objects.get(pk=id)
        form = pricingshemeForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            return redirect('navigation:createpricing')
    else:
        pi =pricingscheme.objects.get(pk=id)
        #form = purchesForm(instance=pi)
        form=pricingscheme.objects.get(pk=id)

    return render(request, 'updatepricing.html', {'form':form})  

def sales(request):
    
    res=list(purchesinvoice.objects.values('itemcode'))
    cnmdata=customer.objects.all()
    itemcodedata=[]
    for i in res:
        if i["itemcode"] not in itemcodedata:
            itemcodedata.append(i["itemcode"])

    
    form =salseForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            print(form)
            print("----___------")
            print(salseinvoice.objects.all())
            form.save()

            idd=salseinvoice.objects.last().id
            formm=salseinvoice.objects.get(pk=idd)
            formm.invoiceno="SIV00"+str(idd)
            formm.save()

            return redirect('navigation:createsalse')
        else:
            print(form.errors)
    return render(request, 'sales.html',{"itemcodedata":itemcodedata,"cnmdata":cnmdata})
def createsalse(request):
    salse=salseinvoice.objects.all()
    return render(request,'createsalse.html', {'salse':salse})
def delete_salse(request, id):
    if request.method=='POST':
        pi = salseinvoice.objects.get(pk=id)
        pi.delete()
        return redirect('navigation:createsalse')

def view_salse(request, id):
    pi = salseinvoice.objects.get(pk=id)
    form=salseinvoice.objects.get(pk=id)
    viw=salseinvoice.objects.filter(itemcode='ICODE00032')
    print(viw)
    return render(request, 'viewsalse.html', {'form': form}) 

def update_salse(request, id):
    if request.method=='POST':
        pi = salseinvoice.objects.get(pk=id)
        form = salseForm(request.POST, instance=pi)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('navigation:createsalse')
    else:
        pi = salseinvoice.objects.get(pk=id)
        #form = purchesForm(instance=pi)
        form=salseinvoice.objects.get(pk=id)

    return render(request, 'updatesalse.html', {'form':form})

def loadcustomerid(request):
    print(request)
    idd=request.GET.get('idd')
    #print("itemcode  ---------------------    ",icodee)
    irow=customer.objects.filter(id=idd)
    print(list(irow))
    return JsonResponse(list(irow.values('id','cust_name','cust_ad','gstn')), safe=False) 

def loadbatcno(request):
    print(request)
    idd=request.GET.get('idd')
    #print("itemcode  ---------------------    ",icodee)
    irow=purchesinvoice.objects.filter(batchno=idd)
    print(list(irow))
    return JsonResponse(list(irow.values('id','unitprice','uom','quantity')), safe=False)     
def loadpricingscheme(request):
    print(request)
    idd=request.GET.get('idd')
    irow=pricingscheme.objects.filter(id=idd)
    print(idd)
    return JsonResponse(list(irow.values('id','purchaseprice')), safe=False) 
def gst(request):
    purchasein=list(purchesinvoice.objects.all().values('invoiceno','cgstamount','sgstamount','igstamount'))
    salsein=list(salseinvoice.objects.all().values('invoiceno','cgstamount','sgstamount','igstamount'))
    #print(purchasein)
    totalCP=0
    totalSP=0
    totalIP=0
    totalCS=0
    totalSS=0
    totalIS=0
    for cisgst in purchasein:
        totalCP +=cisgst['cgstamount']
        totalSP +=cisgst['sgstamount']
        totalIP +=cisgst['igstamount']
    for cisgst in salsein:
        totalCS +=cisgst['cgstamount']
        totalSS +=cisgst['sgstamount']
        totalIS +=cisgst['igstamount']
    global lastdata
    lastdata=[len(purchasein),totalCP,totalSP,totalIP,len(salsein),totalCS,totalSS,totalIS]        
    #print(totalCP)
    global Pgst
    global Sgst
    Pgst=copy.deepcopy(purchasein)
    Sgst=copy.deepcopy(salsein)
    resdata=itertools.zip_longest(purchasein, salsein, fillvalue=-1)
    
    return render(request, 'gst.html',{"resdata":resdata})


def pamentvoucher(request):
    vcodedata=vendor.objects.all()
    itemcodedata=item.objects.all()

    form = paymentvoucherForm(request.POST or None)
    if request.method == 'POST':
       
        if form.is_valid():
            print(form)
            print("-----_ _ _------")
            print(paymentvoucher.objects.all())
            form.save()
            idd=paymentvoucher.objects.last().id
            formm=paymentvoucher.objects.get(pk=idd)
            formm.invoiceno="PVC00"+str(idd)
            formm.save()
            return redirect('navigation:createpayment')
    else:
        print("hhg")
    return render(request, 'payment.html',{"vcodedata":vcodedata,"itemcodedata":itemcodedata,"form":form})

def createpayment(request):
    items = paymentvoucher.objects.all()
    print(items)
    print("itemviewpuches")
    return render(request,'createpament.html', {'items': items})

def delete_paymentvoucher(request, id):
    if request.method=='POST':
        pi = paymentvoucher.objects.get(pk=id)
        pi.delete()
        return redirect('navigation:createpayment')


def view_paymentvoucher(request, id):
    pi = paymentvoucher.objects.get(pk=id)
    form=paymentvoucher.objects.get(pk=id)
    return render(request, 'viewpaymentvoucher.html', {'form': form})        
def update_paymentvoucher(request, id):
    if request.method=='POST':
        pi = paymentvoucher.objects.get(pk=id)
        form = paymentvoucherForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            return redirect('navigation:createpayment')
    else:
        pi = paymentvoucher.objects.get(pk=id)
        #form = purchesForm(instance=pi)
        form=paymentvoucher.objects.get(pk=id)

    return render(request, 'updatepaymentvoucher.html', {'form':form})    



def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users Data', cell_overwrite_ok=True) # this will make a sheet named Users Data
    print(a)
    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    lastcel_style=xlwt.XFStyle()
    columns = ['Item Code', 'Batch No', 'Stock Qty', 'UOM','Current Value','Tax','Transaction History','Stock Qty(current)','Stock Value ' ]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 
    font_style = xlwt.XFStyle()
    print(globaldict)
    aligment = xlwt.Alignment()
    aligment.horz = aligment.HORZ_CENTER    #  horizontal alignment 
    aligment.vert = aligment.VERT_CENTER    #  perpendicular to its way 
    font_style.alignment = aligment
    lastaligment = xlwt.Alignment()
    lastaligment.horz=aligment.HORZ_RIGHT
    lastcel_style.alignment=lastaligment
    rows=1
    columns=0
    for key,value in globaldict.items():
        ws.write_merge(rows,(rows+len(value)*2)-5,columns,columns,key,font_style)
        brow=0
        bcolum=1
        for ke,val in value.items():
            ws.write_merge(rows,rows+1,bcolum,bcolum,ke,font_style)
            # v=8
            # v=val['id']
            try:
                ws.write(rows,bcolum+1,val['quantity'],font_style)
                ws.write(rows,bcolum+2,val['uom'],font_style)
                ws.write(rows,bcolum+3,val['amount'],font_style)
                ws.write(rows,bcolum+4,val['tax'],font_style)
                ws.write(rows,bcolum+5,"Dr",font_style)
                rows +=1
                ws.write(rows,bcolum+1,val['salsequantity'],font_style)
                ws.write(rows,bcolum+2,val['salseuom'],font_style)
                ws.write(rows,bcolum+3,val['salseamount'],font_style)
                ws.write(rows,bcolum+4,val['salsetax'],font_style)
                ws.write(rows,bcolum+5,"Cr",font_style)
                ws.write_merge(rows-1,rows,bcolum+6,bcolum+6,val['stockqua'])
                ws.write_merge(rows-1,rows,bcolum+7,bcolum+7,val['stockval'])
            except:
                if(ke=="Total Stock Value"):
                    ws.write_merge(rows,rows+1,bcolum+1,bcolum+7,str(val),lastcel_style)
                else:
                    ws.write_merge(rows,rows+1,bcolum+1,bcolum+6,str(val),lastcel_style)
                rows +=1
            rows +=1     
        rows +=1
    wb.save(response)
    return response    



#gstreport
def export_gst_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users Data', cell_overwrite_ok=True) # this will make a sheet named Users Data
    print(a)
    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    lastcel_style=xlwt.XFStyle()
    columns = ['Purchase Invoice', 'CGST','SGST','IGST','salse Invoice', 'CGST','SGST','IGST']
    colmd=['invoiceno','cgstamount','sgstamount','igstamount']
    lastrow=['Total Count of Purchasing Invoice','Total Input CGST','Total Input SGST','Total Input IGST','Total Count of salse Invoice','Total Output CGST','Total Output SGST','Total Output IGST']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 
    font_style = xlwt.XFStyle()
    print(globaldict)
    aligment = xlwt.Alignment()
    aligment.horz = aligment.HORZ_CENTER    #  horizontal alignment 
    aligment.vert = aligment.VERT_CENTER    #  perpendicular to its way 
    font_style.alignment = aligment
    lastaligment = xlwt.Alignment()
    lastaligment.horz=aligment.HORZ_RIGHT
    lastcel_style.alignment=lastaligment
    st = xlwt.easyxf('pattern: pattern solid, fore_colour gray25;' 'font: colour black, bold True;')
    rows=1
    columns=0
    for data in Pgst:
        columns=0
        for i in colmd:
            ws.write(rows,columns,data[i])
            columns+=1
        rows+=1
    rowss=1    
    for data in Sgst:
        columns=4
        for i in colmd:
            ws.write(rowss,columns,data[i])
            columns+=1
        rowss+=1
    row_num=max(rows,rowss)    
    for col_num in range(len(lastrow)):
        ws.write(row_num, col_num, lastrow[col_num], st)
        ws.write(row_num+1, col_num, lastdata[col_num], font_style)
    print(Pgst)
    wb.save(response)

    return response        