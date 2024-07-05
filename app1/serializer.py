from rest_framework import serializers
from app1.models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User 
        fields=['username','firstname','lastname','email','password']
class UserSerializer2(serializers.ModelSerializer):
    class Meta:
        model=User 
        fields=['username','email','id']

class ProfileDisSerilizer(serializers.ModelSerializer):
    username=UserSerializer2()
    class Meta:
         model=Profile
         fields=['id','username','Profile_Pic','P_Url','Mobile_Number']


#Login Seializer
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model =Login
        fields = ['Email','Custamer_Name','Password','Mobile_Number','JoinDate','id','P_Url',"Profile_Pic"]
class LoginImageSerializer(serializers.ModelSerializer):
    class Meta:
        model =Login
        fields = ['pk',"Profile_Pic","P_Url"]

#Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=['username','Description','Product_Name','Category','Category_Name','Price','Stack','Out_Of_Stack','Discount',
                'Rating','How_Many','Hightlet','Delivary_Charges','Brand','Color','Specifications','id','Size_Of_Product','ReplaceMentDays','returnForDays']


#Orders Serializer
class CancelOrderSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Orders
        fields=['username','Delivary_Type','Payment_Status','Product_Name',"CancelDate",'Custamer_Name','Selling_Price','Code_Using','Delivary','Date',"OrderCancel",'refund_id','Note','process']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Orders
        fields='__all__'

#Custemor Serializer


from rest_framework import serializers
from .models import Custamer_Details

class CustamerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custamer_Details
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields='__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Image
        fields=["id","Product_Name","P_Images","ImageUrl","List_Urls"]

#User Model Serializer
class AddCardSerializer(serializers.ModelSerializer):
    class Meta:
        model=Add_TO_Card
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'first_name', 'last_name', 'email','password',]

#ProfileSerializer

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields ='__all__'

class UserChekSerilizer(serializers.ModelSerializer):
    class Meta:
        model=User 
        fields=['username','password']

class ProductDisplaySerilizer(serializers.ModelSerializer):
    Product_Name = ProductSerializer()
    class Meta:
        model = Image 
        fields = ['id','P_Images', 'ImageUrl','Product_Name','List_Urls']  # Include 'Product_Name' in the fields list


class LoginM(serializers.ModelSerializer):
    class Meta:
        model=Login 
        fields=['Email','Custamer_Name']
# class AdressSerilizer(serializers.ModelSerializer):
#     class Meta:
#         model=Adress 
#         fields='__all__'


class AddCardDisplySerializer(serializers.ModelSerializer):
    Custamer_Name=LoginM()
    class Meta:
        model=Add_TO_Card 
        fields = ['Product_Name', 'Custamer_Name','Size'] 
class CuponCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model=CupenCode 
        fields='__all__'
class CheckCuponCodeSerilizer(serializers.ModelSerializer):
    class Meta:
        model=CheckCode 
        fields='__all__'

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model =Products  # Assuming Product is the name of your product model
        fields = ['Product_Name', 'Price','id','Rating',"Price","Discount","Delivary_Charges","Category","Category_Name",'Stack','Size_Of_Product','ReplaceMentDays','returnForDays']

class LoginsSerializer(serializers.ModelSerializer):
    class Meta:
        model =Login # Assuming Customer is the name of your customer model
        fields = ['Custamer_Name', 'Email']  
class ImgeLSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Image 
        fields=['ImageUrl']
class OrderLSerilizer(serializers.ModelSerializer):
    Product_Name=ProductsSerializer()
    class Meta:
        model=Orders 
        fields=["Product_Name",'Order_Id','Delivary_Type','Payment_Status','Date','username',"Delivary",'Selling_Price','Code_Using',"OrderCancel","CancelDate","Delivary_Date","AdminWrite","Size",'refund_id','Note','process']

class LCOserilizer(serializers.ModelSerializer):
    ImageUrl=ImgeLSerilizer()
    Order_Id=OrderLSerilizer()
    Custamer_Name=LoginsSerializer()
    # 
    class Meta:
        model=Custamer_Details 
        # fields=['username','Product_Name','Custamer_Name','Order_Id','Delivary_Type','Payment_Status','Date']
        fields=['ImageUrl',"Order_Id","Custamer_Name",'Adress','Quantity','Total_Amount']
        fields='__all__'
class LSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ['Custamer_Name', 'id','Email']


class Oserilizer(serializers.ModelSerializer):
    Custamer_Name=LoginsSerializer()
    Product_Name=ProductsSerializer()
    class Meta:
        model = Orders 
        fields = ['Order_Id','Custamer_Name','Product_Name','username','Delivary_Type','Payment_Status','Date',"Size"]

class CDSerilizer(serializers.ModelSerializer):
    Order_Id = Oserilizer()
    # Custamer_Name = LSerilizer()
    
    class Meta:
        model = Custamer_Details 
        fields = ['Order_Id', 'Quantity', 'Total_Amount', 'City', 'Adress', 'Full_Name',"Size" ]



class Oderserilizer(serializers.ModelSerializer):
    Custamer_Name=LoginsSerializer()
    ImageUrl=ProductDisplaySerilizer()
    class Meta:
        model = Orders 
        fields = ['Order_Id','Custamer_Name','ImageUrl','username','Delivary_Type','Payment_Status','Date',"Size"]
class CDSerializer(serializers.ModelSerializer):
    Custamer_Name=LoginsSerializer()
    Order_Id=Oserilizer()
    class Meta:
        model=Custamer_Details 
        fields=['id','City','Total_Amount','Custamer_Name','Order_Id','Quantity','Adress','Full_Name']
class TopDealsSerializer(serializers.ModelSerializer):
    class Meta:
        model=TopDeals 
        fields=['username','ImageUrl','Product_Name']

class TopDealsProductsSerilizer(serializers.ModelSerializer):
    Product_Name=ProductsSerializer()
    ImageUrl=ProductDisplaySerilizer()
    class Meta:
        model=TopDeals      
        fields=['id','ImageUrl','username','Product_Name']
class SuggetsSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Sugget 
        fields=['id','ImageUrl','username','Product_Name']
class SuggestProductSerializer(serializers.ModelSerializer):
    Product_Name=ProductsSerializer()
    ImageUrl=ProductDisplaySerilizer()
    class Meta:
        model=Sugget
        fields=['id','ImageUrl','username','Product_Name']
class CheckSerilizer(serializers.ModelSerializer):
    class Meta:
        model=TopDeals
        fields='__all__'
class RatingSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Rating 
        fields=['Product_Name','Rating','Rating_Lable','Custamer_Name']
class RatingDisplySerilizer(serializers.ModelSerializer):
    Custamer_Name=LSerilizer()
    class Meta:
        model=Rating
        fields=['Rating','Rating_Lable','Custamer_Name',"Product_Name"]
class ImageCheckSerilizer(serializers.ModelSerializer):
    class Meta:
        model=CheckImages
        fields='__all__'

class ProductsSerializer2(serializers.ModelSerializer):
    class Meta:
        model =Products  # Assuming Product is the name of your product model
        fields = ['Product_Name']



class RatingDisplySerilizer2(serializers.ModelSerializer):
    Custamer_Name=LSerilizer()
    Product_Name=ProductsSerializer2()
    class Meta:
        model=Rating
        fields=['Rating','Rating_Lable','Custamer_Name',"Product_Name"]
class PaymentDetailsSerilizer(serializers.ModelSerializer):
    class Meta:
        model=PaymentDetails
        fields='__all__'



#Product Image
        


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Image
        fielsd='__all__'


# class AddCardSerializer(serializers.Serializer):
#     class Meta:
#         model=Add_TO_Card
#         fields='__all__'
class AdressListSerilizer(serializers.ModelSerializer):
    class Meta:
        model=AdressList 
        fields='__all__'

class RefoundSerilizer(serializers.ModelSerializer):
    class Meta:
        model=RefoundData
        fields='__all__'

class ExchangeSerilizer(serializers.ModelSerializer):
    class Meta:
        model=ExchangeOrder
        fields=['pk','Order_Id','Quantity','Note','Delivary','Custamer_Name','Delivary_Date']
        
class ExchangeDisplySerializer(serializers.ModelSerializer):
    Order_Id=Oserilizer()
    class Meta:
        model=ExchangeOrder 
        fields=['pk','Order_Id','Quantity','Note','Delivary']
        
class ReturnDisplySerilizer(serializers.ModelSerializer):
     Order_Id=Oserilizer()
     class Meta:
        model=RefoundData
        fields=['pk','Order_Id','PaymentProcess','Payment_Id','Price','Note','Payment_Id']
class ReturnPatchData(serializers.ModelSerializer):
    class Meta:
        model=RefoundData
        fields=['pk','Order_Id','PaymentProcess','Payment_Id','Price','Note','Payment_Id','RefundDate']
    



