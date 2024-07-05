from django.shortcuts import render
import random
import datetime

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from app1.models import *
from django.http import HttpResponse
from rest_framework import viewsets

from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
from app1.serializer import *
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from rest_framework import serializers
from django.template.loader import render_to_string



# views.py



import razorpay 
from django.conf import settings 
from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt
import json 

@csrf_exempt
def Check(request):
    if(request.method=='GET'):
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        try:
            refund_requests = client.refund.all()
            refund_details = []
            for refund in refund_requests['items']:
                refund_details.append({
                    'id': refund['id'],
                    'amount_refunded': refund['amount_refunded'],
                    'status': refund['status'],
                    'created_at': refund['created_at']
                })
                print(refund_details)
            return JsonResponse({'refund_details': refund_details})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def create_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        amount = data.get('amount')
        currency = data.get('currency', 'INR')
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        payment_data = {
            'amount': amount,
            'currency': currency,
            'payment_capture': 1
        }
        
        order = client.order.create(data=payment_data)
        return JsonResponse(order)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
from razorpay import Client
@csrf_exempt
def get_refund_status(request, refund_id):
    try:
        client = Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        refund = client.refund.fetch(refund_id)
        refund_status = refund.get('status')
        return JsonResponse({'status': refund_status})
    except Exception as e:
        return JsonResponse({'error': 'Error fetching refund details'}, status=500)
    
@csrf_exempt
def initiate_refund(request):
    if request.method == 'POST':
        data=json.loads(request.body)
        payment_id = data.get('paymentId')
        refund_amount = data.get('refundAmount')
        # upi_id = data.get('upiId')
        refund_reason = data.get('note')
        email=data.get('email')
        name=data.get('name')
        oid=data.get('id')
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        try:
            # Initiate refund using Razorpay API
            refund_data = {
            'amount': refund_amount * 100,  # Razorpay expects amount in paisa
            # 'upi_id': upi_id,  # UPI ID of the customer
            'notes': {
                'refund_reason': refund_reason  # Additional note for the refund
                 }
            }
            refund = client.payment.refund(payment_id, refund_data)
            # refund = client.payment.refund(payment_id, {'amount': refund_amount * 100})
            refund_status = refund['status']
            refund_id = refund.get('id')
            email_content = render_to_string('Refund.html', {'refund_id':refund_id,'refund_amount':refund_amount,'name':name,'oid':oid})
            send_mail(
               'Refund Process Accepted',
                 '',
                     'venkateswarlureddy647@gmail.com',
            [email],
            html_message=email_content
            )
            return JsonResponse({'status': refund_status, 'refund_id': refund_id})
        except Exception as e:
            print('Error initiating refund:', e)
            return JsonResponse({'status': 'error'})

@api_view(['GET','POST','PATCH','PUT','DELETE'])
def LoginDetails(request):
    if(request.method=='GET'):
        Data=Login.objects.all()
        Serializer_Data=LoginSerializer(Data,many=True)
        return Response(Serializer_Data.data,status=status.HTTP_201_CREATED)
    elif(request.method=='POST'):
        data=request.data 
        serializer=LoginSerializer(data=data)
        print(request.data['Email'])
        email_content = render_to_string('LoginTemplate.html', {'recipient_name':request.data['Custamer_Name']})
        if(serializer.is_valid()):
            serializer.save()
            send_mail(
        'Creating Account',
        '',
        'venkateswarlureddy647@gmail.com',
        [request.data['Email']],
        html_message=email_content
    )
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        data = request.data
        custamer_name = data.get('pk')  
        obj = Login.objects.get(pk=custamer_name)
        serializer = LoginSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','POST','PATCH'])
def LoginImageDetails(request):
    if request.method == 'PATCH':
        data = request.data
        custamer_name = data.get('pk')  
        obj = Login.objects.get(pk=custamer_name)
        request.data['P_Url']=request.build_absolute_uri(request.data['Profile_Pic'])
        serializer = LoginSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','POST','PATCH'])
def LoginImageDetails2(request):
    if request.method == 'PATCH':
        data = request.data
        custamer_name = data.get('pk')  
        obj = Login.objects.get(pk=custamer_name)
        request.data['P_Url']=request.build_absolute_uri(request.data['Profile_Pic'])
        request.data.pop('Profile_Pic')
        serializer = LoginSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



           

# from django.http import HttpResponseRedirect


# #Product Details

@api_view(['GET','POST','PATCH','PUT','DELETE'])
def ProductDetails(request):
    if(request.method=='GET'):
        Data=Products.objects.all()
        Serializer_Data=ProductSerializer(Data,many=True)
        return Response(Serializer_Data.data,status=status.HTTP_201_CREATED)
    elif request.method == 'POST':
        username = request.data.get('username')
        user = User.objects.get(username=username)
        request.data['username'] = user.pk
        serializer = ProductSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            print('sss')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='PATCH':
        PO=Products.objects.get(pk=request.data['pk'])
        serializer=ProductSerializer(PO,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:       
        PO=Products.objects.filter(pk=request.data['pk'])[0]
        serializer=ProductSerializer(PO,data=request.data,partial=True)
        if serializer.is_valid():
            PO.delete()
            return Response({"Message":"Success"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
#-----------------------------------------------------------------------------------
#------------------------------------------------------------------------
#---------------------------------------------------------------- 
    

# # OrderDetails
    
@api_view(['GET','POST','PATCH','PUT','DELETE'])
def OrderDetails(request):
    if(request.method=='GET'):
        Data=Orders.objects.all()
        Serializer_Data=OrderSerializer(Data,many=True)
        return Response(Serializer_Data.data,status=status.HTTP_201_CREATED)
    elif(request.method=='POST'):
        email=request.data['Custamer_Name']
        CO=Login.objects.get(Email=email)
        request.data['Custamer_Name']=CO.pk
        serializer = OrderSerializer(data=request.data)
        print(request.data)
        if(serializer.is_valid()):
            serializer.save()
            ADO=Add_TO_Card.objects.filter(Product_Name=request.data['Product_Name'],Custamer_Name=request.data['Custamer_Name'])
            if(len(ADO)>0):
                for obj in ADO:
                    obj.delete()      
            return Response(serializer.data,status=status.HTTP_201_CREATED)   
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    elif(request.method=='PATCH'):
        Oid=request.data['Order_Id']
        OObj=Orders.objects.get(Order_Id=Oid)
        serilizer=OrderLSerilizer(OObj,data=request.data,partial=True)
        if(serilizer.is_valid()):
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_201_CREATED)   
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)  

        
       
 
# custemar Details
@api_view(['GET','POST','PATCH','PUT','DELETE'])    
def CustamerDetails(request):
    if(request.method=='GET'):
        Data=Custamer_Details.objects.all()
        Serializer_Data=CustamerSerializer(Data,many=True)
        return Response(Serializer_Data.data,status=status.HTTP_201_CREATED)
    elif request.method == 'POST':
        LO=Login.objects.get(pk=request.data['Custamer_Name'])
        IOL=Image.objects.filter(ImageUrl=request.data['ImageUrl'])
        UO=User.objects.get(pk=request.data['username'])
        PO=Products.objects.get(pk=request.data['Product_Name'])
        OOL=Orders.objects.filter(Custamer_Name=LO,username=UO,Product_Name=PO)
        request.data.pop('username')
        request.data.pop('Product_Name')
        print(request.data)
        IO=IOL[len(IOL)-1]
        OO=OOL[len(OOL)-1]
        request.data['Order_Id']=OO.Order_Id
        request.data["ImageUrl"]=IO.pk
        print(OO.Order_Id)
        serializer = CustamerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email_content = render_to_string('OrderConformation.html', {'Orders':OO.Order_Id,'Date':OO.Date,'Quantity':request.data['Quantity'],'Total':request.data['Total_Amount']})
            send_mail(
            'Order Comformation',
            '',
             'venkateswarlureddy647@gmail.com',
             [LO.Email],
            html_message=email_content
            )
            return Response({"Message":"Yes"}, status=status.HTTP_201_CREATED)
            
        return Response({"Message":"Yes"}, status=status.HTTP_201_CREATED)

@api_view(['GET','POST','PATCH','PUT','DELETE'])
def HandleDeleteOrder(request):
    if(request.method=='GET'):
        return Response({"Message":"Yes"}, status=status.HTTP_201_CREATED)
    elif(request.method=='POST'):
        OOBJ=Orders.objects.filter(Product_Name=request.data['pk'])
        for obj in OOBJ:
            print(obj.Delivary)
            print('---------')
            if(obj.Delivary=='No'):
                return Response({"Message":"No"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"Message":"Yes"}, status=status.HTTP_201_CREATED)
    elif(request.method=='DELETE'):
        return Response({"Message":"Success"},status=status.HTTP_201_CREATED)
#ProfileDetails
@api_view(['GET','POST','PATCH','PUT','DELETE'])
def ProfileDetails(request):
    if(request.method=='GET'):
        Data=Profile.objects.all()
        Serializer_Data=ProfileDisSerilizer(Data,many=True)
        return Response(Serializer_Data.data,status=status.HTTP_201_CREATED)
    elif(request.method=='POST'):
        P_url=request.build_absolute_uri(request.data['Profile_Pic'])
        request.data['P_Url']=P_url
        serializer=ProfileSerializer(data=request.data)
        if(serializer.is_valid()):
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif(request.method=='PATCH'):
        Po=Profile.objects.get(pk=request.data['pk'])
        P_url=request.build_absolute_uri(request.data['Profile_Pic'])
        request.data.pop('Profile_Pic')
        request.data['P_Url']=P_url
        serializer=ProfileSerializer(Po,data=request.data,partial=True)
        if(serializer.is_valid()):
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST','PATCH','PUT','DELETE'])
def ProfileImageDetails(request):
    if(request.method=='PATCH'):
        Po=Profile.objects.get(pk=request.data['pk'])
        P_url=request.build_absolute_uri(request.data['Profile_Pic'])
        request.data['P_Url']=P_url
        serializer=ProfileSerializer(Po,data=request.data,partial=True)
        if(serializer.is_valid()):
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','POST','PATCH','PUT','DELETE'])
def ProfileNumberDetails(request):
    if(request.method=='PATCH'):
        Po=Profile.objects.get(pk=request.data['pk'])
        serializer=ProfileSerializer(Po,data=request.data,partial=True)
        if(serializer.is_valid()):
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





        
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','POST','PATCH','PUT','DELETE'])
def  UserDetails(request):
    if(request.method=='GET'):
        Data=User.objects.all()
        Serializer_Data=UserSerializer(Data,many=True)
        return Response(Serializer_Data.data,status=status.HTTP_201_CREATED)
    elif request.method == 'POST':
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()
            send_mail('Registration',
            'Thanku For Registration',
            'venkateswarlureddy647@gmail.com',
             [data['email']],
            fail_silently=True,
             )
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif(request.method=='PATCH'):
        Uo=User.objects.get(pk=request.data['pk'])
        serializer=UserSerializer(Uo,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def UserOtpDetails(request):
    if request.method == 'POST':
        CheckUserName = request.data.get('username')  # Get email from request data 
        user_exists = User.objects.filter(username=CheckUserName).exists()
        if user_exists:
            LO=User.objects.get(username=CheckUserName)
            otp = get_random_string(length=4, allowed_chars='0123456789')  # Generate OTP
            email_content = render_to_string('UserForget.html',{"Otp":otp,"Name":LO.username})
            send_mail(
            'Forget Password',
            '',
             'venkateswarlureddy647@gmail.com',
             [LO.email],
            html_message=email_content
            )
            return JsonResponse({"Message": otp}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({"Message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    else:
        return JsonResponse({"Message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
       


@api_view(['GET','POST','PATCH','PUT','DELETE'])
def ImageDetails(request):
    if(request.method=='GET'):
        Data=Image.objects.all()
        Serializer_Data=ImageSerializer(Data,many=True)
        return Response(Serializer_Data.data,status=status.HTTP_201_CREATED)
    elif request.method == 'POST':
        request.data['ImageUrl'] = request.build_absolute_uri(request.data.get('P_Images'))
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
        # Save the serializer
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        # If any serializer is not valid, return error response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        image_pk = request.data.get('pk')  # Get the primary key from request data
        image_obj = Image.objects.get(pk=image_pk)  # Get the image object

        if(int(request.data['Ind'])==0):
            request.data.pop("Ind")
            url=request.build_absolute_uri(request.data.get('P_Images'))
            request.data['ImageUrl']=url 
            request.data.pop('P_Images') 
            arr=[url]
            request.data['List_Urls']=' '.join(arr)
            serializer = ImageSerializer(image_obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            request.data.pop("Ind")
            url=request.build_absolute_uri(request.data.get('P_Images'))
            request.data['ImageUrl']=url 
            request.data.pop('P_Images') 
            arr=[]
            if(image_obj.List_Urls):
                arr=[image_obj.List_Urls]
            arr.append(url)
            request.data['List_Urls']=" ".join(arr)

            serializer = ImageSerializer(image_obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        imo=Image.objects.get(pk=request.data['pk'])
        imo.delete()
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PATCH'])
def UpdateDetails(request):
    if(request.method=='PATCH'):
        image_obj = Image.objects.get(pk=request.data['pk'] )
        request.data['ImageUrl'] = request.build_absolute_uri(request.data['P_Images'])
        request.data.pop('P_Images') 
        print(request.data['ImageUrl'])
        serializer = ImageSerializer(image_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      
from django.contrib.auth import authenticate
@api_view(['POST'])
def UserCheckDetails(request):
    if(request.method=='POST'):
        un=request.data.get('username')
        pw=request.data.get('password')
       
        AUO=authenticate(username=un,password=pw)
        if(AUO):
            UO=User.objects.get(username=un)
            return Response({"Message":UO.pk},status=status.HTTP_201_CREATED)
        else:
            return Response({"Message":False},status=status.HTTP_201_CREATED)
@api_view(['POST'])
def CheckUserName(request):
    if(request.method=='POST'):
        un=request.data.get('username')
        UO=User.objects.filter(username=un)
        if(len(UO)>0):
            return Response({"Message":True},status=status.HTTP_201_CREATED)
        else:
            print(False)
            return Response({"Message":False},status=status.HTTP_400_BAD_REQUEST)

           
@api_view(['GET','POST','PATCH','PUT','DELETE'])
def ProductDispalyView(request):
    if(request.method=='GET'):
        Data=Image.objects.all()
        Serializer_Data=ProductDisplaySerilizer(Data,many=True)
        return Response(Serializer_Data.data,status=status.HTTP_201_CREATED)
    

@api_view(['GET','POST','PATCH','PUT','DELETE'])
def AddCardDetails(request):
    if(request.method=='GET'):
        Data=Add_TO_Card.objects.all()
        Serializer_Data=AddCardDisplySerializer(Data,many=True)
        return Response(Serializer_Data.data,status=status.HTTP_201_CREATED)
    elif(request.method=='POST'):
        email=request.data['Custamer_Name']
        print(email)
        CO=Login.objects.get(Email=email)
        request.data['Custamer_Name']=CO.pk
        print(CO.pk)
        serializer=AddCardSerializer(data=request.data)
        if(serializer.is_valid()):
             print('bye')
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response({"Message":'Success'},status=status.HTTP_201_CREATED)
    elif(request.method=='DELETE'):
        try:
            customer_id = request.data.get('Custamer_Name')
            Product_id=Products.objects.get(pk=request.data['Product_Name'])
            customer = Login.objects.get(Email=customer_id)
            cart_item = Add_TO_Card.objects.get(Custamer_Name=customer.pk, Product_Name=Product_id.pk)   
        except Add_TO_Card.DoesNotExist:
            return Response({"Message": "Error: Cart item not found"}, status=status.HTTP_404_NOT_FOUND)

        # Initialize serializer with instance to delete
        serializer = AddCardSerializer(instance=cart_item)
        # Perform deletion
       
        cart_item.delete()
        return Response({"Message": "Success"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST','PATCH','PUT','DELETE'])
def CuponCodeDetails(request):
    if(request.method=='GET'):
        Data=CupenCode.objects.all()
        Serializer_Data=CuponCodeSerializer(Data,many=True)
        return Response(Serializer_Data.data,status=status.HTTP_201_CREATED)
    elif(request.method=='POST'):
        serializers=CuponCodeSerializer(data=request.data)
        if(serializers.is_valid()):
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    elif(request.method=='PATCH'):
        CO=CupenCode.objects.get(pk=request.data['pk'])
        serializer =CuponCodeSerializer(CO,data=request.data,partial=True)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    elif(request.method=='DELETE'):
         CO=CupenCode.objects.get(pk=request.data['pk'])
         CO.delete()
         return Response({'Message':'Success'},status=status.HTTP_201_CREATED)


@api_view(['GET','POST','PATCH','PUT','DELETE'])
def CheckCodeDetails(request):
    if(request.method=='GET'):
        print(request.data)
        print('---------')
        Data=CheckCode.objects.all()
        Serializer_Data=CheckCuponCodeSerilizer(Data,many=True)
        return Response(Serializer_Data.data,status=status.HTTP_201_CREATED)
    elif(request.method=='POST'):
        CO=CupenCode.objects.get(Code_Name=request.data['Code_Name'])
        CCO=CheckCode.objects.filter(Code_Name=CO.pk)
        if(True):
            request.data['Times']=len(CCO)+1
            request.data['Code_Name']=CO.pk
            serializers=CheckCuponCodeSerilizer(data=request.data)
            if(serializers.is_valid()):
                serializers.save()
                return Response({"Message":True},status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"Message":False},status=status.HTTP_201_CREATED)
@api_view(['GET','POST','PATCH','PUT','DELETE'])
def Check2CuponDetails(request):
    if(request.method=='GET'):
        Data=CheckCode.objects.all()
        Serializer_Data=CheckCuponCodeSerilizer(Data,many=True)
        return Response(Serializer_Data.data,status=status.HTTP_201_CREATED)
    elif(request.method=='POST'):
        Code=request.data['Code_Name']
        CPO=CupenCode.objects.filter(Code_Name=Code)
        if(CPO):
            CO=CPO[0]
            Check=CheckCode.objects.filter(Code_Name=CO.pk)
            if(CO.Limit>len(Check)):
                CodeCheck=CheckCode.objects.filter(Code_Name=CO.pk,Custamer_Name=request.data['Custamer_Name'])
                if(len(CodeCheck)==0):
                    return Response({"Message":'All Done'},status=status.HTTP_201_CREATED)
                return Response({"Message":'This Code You Alredy Used'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"Message":'Code is Reched limit'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"Message":'You Entered Wrong Code Name'}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def LCODetails(request):
    if request.method == 'GET':
        Data=Custamer_Details.objects.all()
        Serializer_Data=LCOserilizer(Data,many=True)
        return Response(Serializer_Data.data,status=status.HTTP_201_CREATED)

from random import randint
@api_view(['GET','POST'])
def OtpDetails(request):
    if(request.method=='POST'):
        UO=User.objects.filter(username=request.data['username'])
        if(len(UO)>0):
            otp=randint(1000,9999)
            email_content = render_to_string('ForgetPassword.html',{"Otp":otp,"Name":'Admin'})
            send_mail(
            'Forget Password',
            '',
             'venkateswarlureddy647@gmail.com',
             [UO[0].email],
            html_message=email_content
            )
            return Response({"Message":otp},status=status.HTTP_201_CREATED)   
        return Response({"Message":"UserName Not Valid"}, status=status.HTTP_400_BAD_REQUEST)
@api_view(['PATCH'])
def ForgetDetails(request):
    if(request.method=='PATCH'):
        UO=User.objects.get(username=request.data['username'])
        serializer=UserSerializer(UO,data=request.data,partial=True)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()
            email_content = render_to_string('PassWordSucc.html',{"New":request.data['password'],"Name":UO.username})
            send_mail(
            'Password Change Successful',
            '',
             'venkateswarlureddy647@gmail.com',
            [UO.email],
            html_message=email_content
             )
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def CDDetails(request):
    if(request.method=='GET'):
        Data=Custamer_Details.objects.all()
        Serializer_Data=CDSerilizer(Data,many=True)
        return Response(Serializer_Data.data,status=status.HTTP_201_CREATED)
# from django.core.mail import send_mail
from django.http import JsonResponse
from django.utils.crypto import get_random_string

@api_view(['POST'])
def LoginOtpDetails(request):
    if request.method == 'POST':
        email = request.data.get('Email')  # Get email from request data 
        user_exists = Login.objects.filter(Email=email).exists()
        if user_exists:
            LO=Login.objects.get(Email=email)
        
            LOj=Login.objects.filter(Email=email)
            otp = get_random_string(length=4, allowed_chars='0123456789')  # Generate OTP
            email_content = render_to_string('ForgetPassword.html',{"Otp":otp,"Name":LO.Custamer_Name})
            send_mail(
            'Forget Password',
            '',
             'venkateswarlureddy647@gmail.com',
             [email],
            html_message=email_content
            )
            return JsonResponse({"Message": otp}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({"Message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    else:
        return JsonResponse({"Message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
@api_view(['PATCH'])
def LoginPasswordChange(request):
    LE=Login.objects.get(Email=request.data['Email'])
    email_content = render_to_string('PassWordSucc.html',{"New":request.data['Password'],"Name":LE.Custamer_Name})
    send_mail(
            'Password Change Successful',
            '',
             'venkateswarlureddy647@gmail.com',
             [LE.Email],
    html_message=email_content
    )
    serializer=LoginSerializer(LE,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"Message":'Success'},status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def OrderDisplayDetails(request):
    Data = Custamer_Details.objects.all()
    Serializer_Data = CDSerializer(Data, many=True)
    return Response(Serializer_Data.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def TopDealsDetails(request):
    if request.method == 'GET':
        TDO = TopDeals.objects.all()
        serializer = TopDealsProductsSerilizer(TDO, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer =TopDealsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            print(request.data.get('id'))
            top_deal = TopDeals.objects.get(ImageUrl=request.data.get('id'))
        except TopDeals.DoesNotExist:
            return Response({"message": "Top deal not found."}, status=status.HTTP_404_NOT_FOUND)
        
        # Delete the TopDeals object
        top_deal.delete()
        return Response({"message": "Top deal deleted."}, status=status.HTTP_204_NO_CONTENT)
@api_view(['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def SuggetsDetails(request):
    if request.method == 'GET':
        TDO = Sugget.objects.all()
        serializer =SuggestProductSerializer(TDO, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer =SuggetsSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            print(request.data.get('id'))
            top_deal = Sugget.objects.get(ImageUrl=request.data.get('id'))
        except TopDeals.DoesNotExist:
            return Response({"message": "Top deal not found."}, status=status.HTTP_404_NOT_FOUND)
        top_deal.delete()
        return Response({"message": "Top deal deleted."}, status=status.HTTP_204_NO_CONTENT)
@api_view(['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def CheckDetails(request):
    if request.method == 'GET':
        # TDO =Check.objects.all()
        # serializer =Check(TDO, many=True)
        return Response({}, status=status.HTTP_200_OK)
@api_view(['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def RatingDetails(request):
    if(request.method=='GET'):
        TDO =Rating.objects.all()
        serializer =RatingDisplySerilizer(TDO, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif(request.method=='POST'):
        LO=Login.objects.get(Email=request.data['Custamer_Name'])
        request.data['Custamer_Name']=LO.pk
        serilizer=RatingSerilizer(data=request.data)
        print(request.data)
        if(serilizer.is_valid()):
            serilizer.save()
            return Response(serilizer.data, status=status.HTTP_200_OK)
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)   
@api_view(['GET','PATCH'])
def RatingAddProductDetails(request):
    if(request.method=="GET"):
        return Response({'Message':"Success"}, status=status.HTTP_200_OK)
    elif(request.method=='PATCH'):
        UO=User.objects.get(pk=request.data['username'])
        PO=Products.objects.filter(pk=request.data['pk'],username=request.data['username'])[0]
        if(PO):
            request.data.pop('username')
            if(PO.How_Many>0):                                          
                C_R=request.data['Rating']
                P_R=PO.Rating   
                P_How_Many=PO.How_Many
                request.data["How_Many"]=P_How_Many+1
                request.data['Rating']=(C_R+P_R)/2
                serializer=ProductSerializer(PO,data=request.data,partial=True)
                if serializer.is_valid():   
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
            else:
                request.data["How_Many"]=1
                serializer=ProductSerializer(PO,data=request.data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from django.http import JsonResponse    
def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        print('POST')
        image_instance = Image.objects.create(image_url=image.url)
        image_instance.save()
        return JsonResponse({'url': image_instance.request.build_absolute_uri(image.url)})
    return JsonResponse({'error': 'No image provided'}, status=400)
@api_view(['GET','POST'])
def SendOrderDetails(request):
    if(request.method=='POST'):
        
        Order_Ids=[]
        Datess=[]
        Quantities=[]
        Total=[]
        Length=request.data['Arr']
        OObj=Orders.objects.all()[0:int(Length)]
        for obj in OObj:
            Order_Ids.append(obj.Order_Id)
            Dates=obj.Date.date()  
            Str=str(Dates)
            Str2= Str.replace('datetime.date','')
            Datess.append(Str2)
            print(Datess)
            POBJ=Custamer_Details.objects.filter(Order_Id=obj.Order_Id)[0]
            Quantities.append(POBJ.Quantity)
            Total.append(POBJ.Total_Amount)
        email_content = render_to_string('OrderConformation.html', {'Orders':Order_Ids,'Date':Datess,'Quantity':Quantities,'Total':Total})
            
        send_mail(
            'Order Comformation',
            '',
             'venkateswarlureddy647@gmail.com',
             ['lawrencevenky12345@gmail.com'],
            html_message=email_content
        )
        return Response({'error': 'No image provided'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'error': 'No imagess provided'}, status=status.HTTP_201_CREATED)

   
    
    # return render(request,'LoginTemplate.html',d)
@api_view(['GET','POST'])
def ImageCheckDetails(request):
    if(request.method=='GET'):
       TDO =CheckImages.objects.all()
       serializer =ImageCheckSerilizer(TDO, many=True)
       return Response(serializer.data, status=status.HTTP_200_OK)
    elif(request.method=='POST'):
        # print(request.FILES['Image'])
        # print('POOOOO')
       
        request.data['ImageUrl']=request.build_absolute_uri(request.data['Image'])
        print(request.data['Image'])
        print(request.data['ImageUrl'])
       
        serializers=ImageCheckSerilizer(data=request.data)
        if(serializers.is_valid()):
            data_instance=serializers.save()
            # if 'ImageUrl' in serializers.data and request:
            #     print(request.build_absolute_uri(data_instance.ImageUrl))
            #     print('-------------------')
            #     data_instance.ImageUrl = request.build_absolute_uri(data_instance.Image)
            
            # data_instance.ImageUrl=request.build_absolute_uri(data_instance.Image)
            
            # data_instance2=data_instance.save()
            # print(data_instance2.ImageUrl)
        
            # request.data['ImageUr']=request.build_absolute_uri(Data['Image'])
            return Response({"Message":"Success"},status=status.HTTP_201_CREATED)
        return Response({'error': 'No imagess provided'}, status=status.HTTP_201_CREATED)
@api_view(['GET','POST'])
def SendingEmailDelivaried(request):
    if(request.method=='GET'):
        return Response({"Message":"Success"},status=status.HTTP_201_CREATED)
    elif(request.method=='POST'):
        Oid=request.data['Orderid']
        ODate=request.data['ODate']
        DDate=request.data['DDate']
        Qun=request.data['Quant']
        email_content = render_to_string('DelivaryProduct.html', {"Id":Oid,"od":ODate,'dd':DDate,'quan':Qun}) 
        send_mail(
            'Your Order Has Been Delivered!',
            '',
             'venkateswarlureddy647@gmail.com',
             [request.data['Email']],
            html_message=email_content
        )
        return Response({"Message":"Success"},status=status.HTTP_201_CREATED)
@api_view(['PATCH',"GET"])
def Image2Details(request):
    if(request.method=='PATCH'):
        image_pk = request.data.get('pk')  # Get the primary key from request data
        image_obj = Image.objects.all().last()
        print(image_obj.pk)
        url=request.build_absolute_uri(request.data.get('P_Images'))
        request.data['ImageUrl']=url
        print(request.data)
        serializer = ImageSerializer(image_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"Message":"Success"},status=status.HTTP_200_OK)



@api_view(['PATCH',"GET"])
def Image3Details(request):
    if(request.method=='PATCH'):
        image_pk = request.data.get('pk')  # Get the primary key from request data
        image_obj = Image.objects.get(pk=image_pk)
        url=request.build_absolute_uri(request.data.get('P_Images'))
        request.data['ImageUrl']=url
        serializer = ImageSerializer(image_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"Message":"Success"},status=status.HTTP_200_OK)

@api_view(['PATCH',"GET"])
def RemoveImages(request):
    if(request.method=='GET'):
         return Response({"Message":"Success"},status=status.HTTP_200_OK)
    elif(request.method=='PATCH'):
        image_pk = request.data.get('pk')  # Get the primary key from request data
        image_obj = Image.objects.get(pk=image_pk)
        UrlList=request.data.get('List_Urls')
        UrlList2=' '.join(UrlList)
        request.data['List_Urls']=UrlList2
        print(request.data)
        serializer = ImageSerializer(image_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','POST','PATCH','DELETE'])    
def AdressListDetails(request):
    if(request.method=='GET'):
        TDO =AdressList.objects.all()
        serializer =AdressListSerilizer(TDO, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif(request.method=='POST'):
        LO=Login.objects.get(pk=request.data['Custamer_Name'])
        request.data['Custamer_Name']=LO.pk
        Adress=[request.data['Adrss_List']]
        request.data['Adrss_List']=(request.data['Adrss_List'])
        print(request.data)
        serializer =AdressListSerilizer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif(request.method=='PATCH'):
        AdressObject=AdressList.objects.get(Custamer_Name=request.data['Custamer_Name'])
        Adress=[AdressObject.Adrss_List,request.data['Adrss_List']]
        request.data['Adrss_List']='@'.join(Adress)
        serializer=AdressListSerilizer(AdressObject, data=request.data, partial=True)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','POST','PATCH','DELETE'])    
def RemoveAdress(request):
    if(request.method=='GET'):
        return Response({"Message":"Success"},status=status.HTTP_200_OK)
    elif(request.method=='PATCH'):
        AO=AdressList.objects.get(Custamer_Name=request.data['Custamer_Name']) 
        serializer=AdressListSerilizer(AO, data=request.data, partial=True)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif(request.method=='DELETE'):
        print(request.data)
        AO=AdressList.objects.get(Custamer_Name=request.data['Custamer_Name']) 
        AO.delete()
        return Response({"Message": "Success"}, status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET','POST','PATCH','DELETE'])
def CancelOrderDetails(request):
    if(request.method=='GET'):
        TDO =Orders.objects.all()
        serializer =OrderSerializer(TDO, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif(request.method=='PATCH'):
        AO=Orders.objects.get(Order_Id=request.data["Order_Id"]) 
        serializer=CancelOrderSerilizer(AO, data=request.data, partial=True)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
       

@api_view(['GET',])
def RatingDetails2(request):
    if(request.method=='GET'):
        TDO =Rating.objects.all()
        serializer =RatingDisplySerilizer2(TDO, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
@api_view(['GET','POST'])
def AdminCuponCheckDetails(request):
    if(request.method=='POST'):
        cname=request.data['cname']
        CO=CupenCode.objects.filter(Code_Name=cname)
        if(len(CO)==0):
            return Response({'Message':'True'}, status=status.HTTP_200_OK)
        return Response({'Message':'false'}, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','POST'])
def CardCheck(request):
    if(request.method=='POST'):
        CO=Add_TO_Card.objects.filter(Custamer_Name=request.data['Custamer_Name'],Product_Name=request.data['Product_Name'])
        if(len(CO)==0):
            return Response({'Message':'True'}, status=status.HTTP_200_OK)
        return Response({'Message':'false'}, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','POST'])
def PaymentDetailsView(request):
    if(request.method=='POST'):
        data=request.data 
        serializers=PaymentDetailsSerilizer(data=data)
        if(serializers.is_valid()):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    elif(request.method=='GET'):
        DOS=PaymentDetails.objects.all()
        serializers=PaymentDetailsSerilizer(DOS,many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
@api_view(['GET','POST','PATCH'])
def RefoundDetailsView(request):
    if(request.method=='POST'):
        data=request.data 
        serializers=RefoundSerilizer(data=data)
        if(serializers.is_valid()):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    elif(request.method=='GET'):
        DOS=RefoundData.objects.all()
        serializers=RefoundSerilizer(DOS,many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    elif(request.method=='PATCH'):
        oid=request.data['Order_Id']
        EXO=RefoundData.objects.get(Order_Id=oid)
        request.data['pk']=EXO.pk
        print(request.data)
        serializer= RefoundSerilizer(EXO, data=request.data, partial=True)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','PATCH'])
def ExchangeDetailsView(request):
    if(request.method=='POST'):
        data=request.data 
        serializers=ExchangeSerilizer(data=data)
        # LO=Login.objects.get(pk=request.data['Custamer_Name'])
        if(serializers.is_valid()):
            serializers.save()
            # email_content = render_to_string('Exchamge.html', {'oid':request.data['Order_Id'],'qty':request.data['Quantity'],'name':LO.Custamer_Name,})
            # send_mail(
            #    'Exchange Process Accepted',
            #      '',
            #          'venkateswarlureddy647@gmail.com',
            # [LO.Email],
            # html_message=email_content
            # )
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    elif(request.method=='GET'):
        DOS=ExchangeOrder.objects.all()
        serializers=ExchangeSerilizer(DOS,many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    elif(request.method=='PATCH'):
        oid=request.data['pk']
        EXO=ExchangeOrder.objects.get(pk=oid)
        serializer=ExchangeSerilizer(EXO, data=request.data, partial=True)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def ExchangeDetailsView2(request):
    if(request.method=='GET'):
        DOS=ExchangeOrder.objects.all()
        serializers=ExchangeDisplySerializer(DOS,many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def RefoundDetailsView2(request):
    if(request.method=='GET'):
        DOS=RefoundData.objects.all()
        serializers=ReturnDisplySerilizer(DOS,many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

             























