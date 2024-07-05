from django.db import models
from django.contrib.auth.models import User


# Get the current date and time



# Create your models here.
#Profile Model
class Profile(models.Model):
    Mobile_Number=models.IntegerField(null=True)
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    Profile_Pic=models.ImageField()
    P_Url=models.TextField(default='Not Sucess')


# #Login Custemor Details
class Login(models.Model):
    Email=models.EmailField(unique=True)
    Custamer_Name=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    Mobile_Number=models.IntegerField()
    JoinDate=models.DateTimeField(null=True)
    Profile_Pic=models.ImageField(null=True)
    P_Url=models.URLField(null=True)
    def __str__(self):
        return self.Custamer_Name


# #Store Products
class Products(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE,)
    Description=models.TextField(null=True,blank=True)
    Product_Name=models.CharField(max_length=1000)
    Category=models.CharField(max_length=100)
    Category_Name=models.CharField(max_length=100)
    Price=models.DecimalField(max_digits=10, decimal_places=2)
    Stack=models.IntegerField()
    Out_Of_Stack=models.BooleanField(default=False)
    Discount=models.IntegerField(null=True  )
    Rating=models.DecimalField(max_digits=3, decimal_places=2,default=0 )
    How_Many=models.IntegerField(default=0)
    Hightlet=models.TextField(null=True)
    Delivary_Charges=models.IntegerField(default=0) 
    Brand=models.CharField(max_length=1000,null=True)
    Color=models.CharField(max_length=1000,null=True)
    Specifications=models.TextField(null=True)
    Size_Of_Product=models.TextField(default='No')
    Size_Price=models.TextField(default='No')
    ReplaceMentDays=models.IntegerField(default=7)
    returnForDays=models.IntegerField(default=7)
    def __str__(self):  
        return self.Product_Name
Img="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"
# #Stroe Multiple Images
class Image(models.Model):
    Product_Name = models.ForeignKey(Products, related_name='images', on_delete=models.CASCADE)
    P_Images = models.ImageField(upload_to='product_images/')
    ImageUrl=models.URLField(default=Img)
    List_Urls=models.TextField(null=True)
    # List_Urls=models.TextField(null=True)
    def save(self, *args, **kwargs):
        # Generate the URL based on the image file
        if not self.ImageUrl:
            self.ImageUrl = self.P_Images.url
        super().save(*args, **kwargs)
    def __str__(self):
        return (self.ImageUrl)
#Orders Storing
class Orders(models.Model): 
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    Custamer_Name=models.ForeignKey(Login,on_delete=models.CASCADE) 
    Order_Id=models.AutoField(primary_key=True) 
    Delivary_Type=models.CharField(max_length=100)
    Payment_Status=models.CharField(max_length=100)
    Product_Name=models.ForeignKey(Products,on_delete=models.CASCADE)
    Date=models.DateTimeField(auto_now_add=True)
    Selling_Price=models.DecimalField(max_digits=10, decimal_places=2,null=True)
    Code_Using=models.IntegerField(null=True)
    Delivary=models.CharField(max_length=100,default='No')
    OrderCancel=models.TextField(max_length=100,default='No')
    CancelDate=models.DateTimeField(null=True)
    Delivary_Date=models.DateTimeField(null=True)
    AdminWrite=models.CharField(max_length=100,null=True)
    Size=models.TextField(default='No')
    Note=models.TextField(null=True)
    refund_id=models.TextField(null=True)
    process=models.TextField(null=True)
   
    def __str__(self) :
        return str(self.Order_Id)
class Custamer_Details(models.Model):
    ImageUrl=models.ForeignKey(Image,on_delete=models.CASCADE,null=True) 
    Quantity=models.IntegerField()
    Custamer_Name=models.ForeignKey(Login,on_delete=models.CASCADE) 
    Order_Id=models.OneToOneField(Orders,on_delete=models.CASCADE)
    Total_Amount=models.IntegerField()
    City=models.CharField(max_length=100)
    Adress = models.TextField()
    Full_Name=models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.City
class Add_TO_Card(models.Model):
    Custamer_Name=models.ForeignKey(Login,on_delete=models.CASCADE)
    Product_Name=models.OneToOneField(Products,on_delete=models.CASCADE,unique=True)
    Size=models.TextField(default='No')
class Adress(models.Model):
    Custamer_Name=models.ForeignKey(Login,on_delete=models.CASCADE)
    Order_Id=models.OneToOneField(Orders,on_delete=models.CASCADE)
    Adresss=models.ForeignKey(Custamer_Details,on_delete=models.CASCADE)
class CupenCode(models.Model):
    Code_Name=models.CharField(max_length=100,unique=True)
    Discount_Type=models.CharField(max_length=20)
    Code_Off=models.IntegerField()
    ExpireDate=models.DateTimeField()
    Limit=models.IntegerField()
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.CharField(max_length=1000,null=True)
    Condtion=models.CharField(max_length=1000,null=True)
    def __str__(self):
        return self.Code_Name

class CheckCode(models.Model):
    Custamer_Name=models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    Code_Name=models.ForeignKey(CupenCode,on_delete=models.CASCADE)
    Times=models.IntegerField()


class TopDeals(models.Model):
    ImageUrl=models.OneToOneField(Image,on_delete=models.CASCADE,null=True)
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    Product_Name=models.OneToOneField(Products,on_delete=models.CASCADE,null=True)

class Sugget(models.Model):
    ImageUrl=models.OneToOneField(Image,on_delete=models.CASCADE,null=True)
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    Product_Name=models.OneToOneField(Products,on_delete=models.CASCADE,null=True)
class Rating(models.Model):
    Product_Name=models.ForeignKey(Products,on_delete=models.CASCADE)
    Rating=models.DecimalField(max_digits=3, decimal_places=2)
    Rating_Lable=models.TextField(null=True)
    Custamer_Name=models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
class CheckImages(models.Model):
    Image=models.ImageField(upload_to='product_images/')
    ImageUrl=models.URLField()
    def __str__(self):
        return str(Image)
    
class AdressList(models.Model):
    Custamer_Name=models.ForeignKey(Login,on_delete=models.CASCADE)
    Adrss_List=models.TextField()
class PaymentDetails(models.Model):
    Order_Id=models.TextField()
    Payment_Id=models.TextField()
    Custamer_Name=models.ForeignKey(Login,on_delete=models.CASCADE)
    Product_Name=models.TextField()
    Product_Id=models.IntegerField(default=0)
    Order_Id2=models.IntegerField(default=0)

class RefoundData(models.Model):
    Order_Id=models.ForeignKey(Orders,on_delete=models.CASCADE)
    PaymentProcess=models.TextField()
    Payment_Id=models.TextField()
    Price=models.IntegerField()
    Custamer_Name=models.IntegerField()
    Note=models.TextField(default='No')
    RefundDate=models.DateTimeField(null=True)
class ExchangeOrder(models.Model):
    Order_Id=models.ForeignKey(Orders,on_delete=models.CASCADE)
    Custamer_Name=models.ForeignKey(Login,on_delete=models.CASCADE)
    Quantity=models.IntegerField()
    Note=models.TextField(default='yes')
    Delivary=models.TextField(default='No')
    Delivary_Date=models.DateTimeField(null=True)

    




    
