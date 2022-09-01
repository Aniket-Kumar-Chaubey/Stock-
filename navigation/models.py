from django.db import models

# Create your models here.
class item(models.Model):
    itemcode=models.CharField(max_length=30,blank=True)
    desc = models.CharField(max_length=122)
    uom = models.CharField(max_length=122)
    manufac = models.CharField(max_length=122, blank=True)
    PSCHEME = (('1','PS1'), ('2','PS2'), ('3','PS3'),)
    pscheme = models.CharField(max_length=1, choices=PSCHEME)
    puchaseprice=models.DecimalField(max_digits=20,decimal_places=2)




    def __str__(self):
        return self.desc

class vendor(models.Model):
    vcode = models.CharField(max_length=100000,blank=True)
    vname = models.CharField(max_length=122)
    vadd = models.CharField(max_length=122)
    STATE = (('1','Jammu & Kashmir'), ('2','Himachal Pradesh'), ('3','Punjab'), ('4','Chandigarh'), ('5','Uttarakhand'), ('6','Haryana'), ('7','Delhi'), ('8','Rajasthan'), ('9','Uttar Pradesh'), ('10','Bihar'), ('11','Sikkim'), ('12','Arunachal Pradesh'), ('13','Nagaland'), ('14','Manipur'), ('15','Mizoram'), ('16','Tripura'), ('17','Meghalaya'), ('18','Assam'), ('19','West Bengal'),('20','Jharkhand'), ('21','Odisha'), ('22','Chattisgarh'), ('23','Madhya Pradesh'), ('24','Gujarat'), ('25','Daman & Diu'), ('26','Dadra & Nagar Haveli'))
    state = models.CharField(max_length=2, choices=STATE, auto_created=True, null= True)
    city = models.CharField(max_length=122)
    pin = models.CharField(max_length=50, null=True)
    gstn=models.CharField(max_length=50, null=True)
    pan=models.CharField(max_length=50, null=True)
    contact=models.CharField(max_length=50, null=True)


    def __str__(self):
        return self.vname


class customer(models.Model):
    cust_name = models.CharField(max_length=122)
    cust_code=models.CharField(max_length=100000,blank=True)
    cust_ad = models.CharField(max_length=122)
    country = models.CharField(max_length=122)
    STATE = (('1','Jammu & Kashmir'), ('2','Himachal Pradesh'), ('3','Punjab'), ('4','Chandigarh'), ('5','Uttarakhand'), ('6','Haryana'), ('7','Delhi'), ('8','Rajasthan'), ('9','Uttar Pradesh'), ('10','Bihar'), ('11','Sikkim'), ('12','Arunachal Pradesh'), ('13','Nagaland'), ('14','Manipur'), ('15','Mizoram'), ('16','Tripura'), ('17','Meghalaya'), ('18','Assam'), ('19','West Bengal'),('20','Jharkhand'), ('21','Odisha'), ('22','Chattisgarh'), ('23','Madhya Pradesh'), ('24','Gujarat'), ('25','Daman & Diu'), ('26','Dadra & Nagar Haveli'))
    state = models.CharField(max_length=2, choices=STATE, default=None)
    district = models.CharField(max_length=122)
    city = models.CharField(max_length=122)
    pin = models.CharField(max_length=122)
    gstn = models.CharField(max_length=122, blank=True)
    pan = models.CharField(max_length=122, blank=True)
    contact = models.CharField(max_length=122, blank=True)

    def __str__(self):
        return self.cust_name
class purchesinvoice(models.Model):
    invoiceno=models.CharField(max_length=100000)
    invoicedate=models.DateField()
    vcode = models.CharField(max_length=100000,blank=True)
    vname = models.CharField(max_length=122)
    vadd = models.CharField(max_length=122)
    vengstin=models.CharField(max_length=30,blank=True)
    itemcode=models.CharField(max_length=30,blank=True)
    desc = models.CharField(max_length=122)
    uom = models.CharField(max_length=122)
    quantity=models.DecimalField(max_digits=20,decimal_places=2)
    unitprice=models.DecimalField(max_digits=20,decimal_places=2)
    amount=models.DecimalField(max_digits=20,decimal_places=2)
    batchno=models.CharField(max_length=100000)
    cgst=models.DecimalField(max_digits=20,decimal_places=2)
    igst=models.DecimalField(max_digits=20,decimal_places=2)
    sgst=models.DecimalField(max_digits=20,decimal_places=2)
    cgstamount=models.DecimalField(max_digits=20,decimal_places=2)
    sgstamount=models.DecimalField(max_digits=20,decimal_places=2)
    igstamount=models.DecimalField(max_digits=20,decimal_places=2)
    totalamount=models.DecimalField(max_digits=20,decimal_places=2)

class salseinvoice(models.Model):
    invoiceno=models.CharField(max_length=100000,blank=True)
    invoicedate=models.DateField()
    custmercode= models.CharField(max_length=100000,blank=True)
    #vname = models.CharField(max_length=122)
    customeraddress= models.CharField(max_length=122)
    customergstin=models.CharField(max_length=30,blank=True)
    itemcode=models.CharField(max_length=30,blank=True)
    desc = models.CharField(max_length=122)
    uom = models.CharField(max_length=122)
    quantity=models.DecimalField(max_digits=20,decimal_places=2)
    unitprice=models.DecimalField(max_digits=20,decimal_places=2)
    amount=models.DecimalField(max_digits=20,decimal_places=2)
    batchno=models.CharField(max_length=100000)
    cgst=models.DecimalField(max_digits=20,decimal_places=2)
    igst=models.DecimalField(max_digits=20,decimal_places=2)
    sgst=models.DecimalField(max_digits=20,decimal_places=2)
    cgstamount=models.DecimalField(max_digits=20,decimal_places=2)
    sgstamount=models.DecimalField(max_digits=20,decimal_places=2)
    igstamount=models.DecimalField(max_digits=20,decimal_places=2)
    totalamount=models.DecimalField(max_digits=20,decimal_places=2)

class pricingscheme(models.Model):
    pricingscheme=models.CharField(max_length=20)
    lowerlimit=models.DecimalField(max_digits=20,decimal_places=2)
    uperlimit=models.DecimalField(max_digits=20,decimal_places=2)
    purchaseprice=models.DecimalField(max_digits=20,decimal_places=2)
    profit=models.DecimalField(max_digits=20,decimal_places=3,default=0)
    profitmarginfactor=models.DecimalField(max_digits=20,decimal_places=3)
    salseprice=models.DecimalField(max_digits=20,decimal_places=2)
class paymentvoucher(models.Model):
    invoiceno=models.CharField(max_length=100000)
    vcode = models.CharField(max_length=100000,blank=True)
    vname = models.CharField(max_length=122)
    vadd = models.CharField(max_length=122)
    vengstin=models.CharField(max_length=30,blank=True)
    itemcode=models.CharField(max_length=30,blank=True)
    desc = models.CharField(max_length=122)
    uom = models.CharField(max_length=122)
    quantity=models.DecimalField(max_digits=20,decimal_places=2)
    unitprice=models.DecimalField(max_digits=20,decimal_places=5)
    amount=models.DecimalField(max_digits=20,decimal_places=5)
    cgst=models.DecimalField(max_digits=20,decimal_places=2)
    igst=models.DecimalField(max_digits=20,decimal_places=2)
    sgst=models.DecimalField(max_digits=20,decimal_places=2)
    cgstamount=models.DecimalField(max_digits=20,decimal_places=2)
    sgstamount=models.DecimalField(max_digits=20,decimal_places=2)
    igstamount=models.DecimalField(max_digits=20,decimal_places=2)
    totalamount=models.DecimalField(max_digits=20,decimal_places=2)