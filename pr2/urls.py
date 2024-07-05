"""
URL configuration for pr2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import *
from django.conf.urls.static import static 
from django.conf import settings


# CheckUserName
urlpatterns = [
    path('admin/', admin.site.urls),
    path('LoginDetails/',LoginDetails,name='LoginDetails'),
    path('ProductDetails/',ProductDetails,name='ProductDetails'),
    path('OrderDetails/',OrderDetails,name='OrderDetails'),
    path('ProfileDetails/',ProfileDetails,name='ProfileDeatils'),
    # path('RatingSerializer/',RatingDetails,name='RatingDetails'),
    path('CustamerDetails/',CustamerDetails,name='CustamerDetails'),
    path('AddCardDetails/',AddCardDetails,name='AddCardDetails'),
    path('UserDetails/', UserDetails,name=' UserDetails'),
    path('ImageDetails/',ImageDetails,name='ImageDetails'),
    path('UserCheckDetails/',UserCheckDetails,name='UserCheckDetails'),
    path('UserCheck/',UserCheckDetails,name='UserCHeck'),
    path('ProductDispalyView/',ProductDispalyView,name='ProductDispalyView'),
    path('upload_image/',upload_image,name='upload_image'),
    path('UpdateDetails/',UpdateDetails,name='UpdateDetails'),
    path('CuponCodeDetails/',CuponCodeDetails,name='CupondCodeDetails'),
    path('CheckCodeDetails/',CheckCodeDetails,name='CheckCOdeDetails'),
    path('LCODetails/',LCODetails,name='LCODetails'),
    path('OtpDetails/',OtpDetails,name='OtpDetails'),
    path("ForgetDetails/",ForgetDetails,name='ForgetDetails'),
    path('CDDetails/',CDDetails,name='CDDetails'),
    path('LoginOtpDetails/',LoginOtpDetails,name='LoginOtpDetails'),
    path('LoginPasswordChange/',LoginPasswordChange,name='LoginPasswordChange'),
    path('OrderDispalyDetails/', OrderDisplayDetails,name='OrderDispalyDetails'),
    path('TopDealsDetails/',TopDealsDetails,name='TopDealsDetails'),
    path('SuggestDetails/',SuggetsDetails,name='SuggetsDetails'),
    path('CheckDetails/',CheckDetails,name='CheckDetails'),
    path('RatingDetails/',RatingDetails,name='RatingDetails'),
    path('RatingDetails2/',RatingDetails2,name='RatingDetails2'),
    path('Check2CuponDetails/',Check2CuponDetails,name='Check2CuponDetails'),
    path('RatingAddProductDetails/',RatingAddProductDetails,name='RatingAddProductDetails'),
    path("HandleDeleteOrder/",HandleDeleteOrder,name='HandleDeleteOrder'),
    path('SendOrderDetails/',SendOrderDetails,name='SendOrderDetails'),
    path('ImageCheckDetails/',ImageCheckDetails,name='ImageCheckDetails'),
    path("SendingEmailDelivaried/",SendingEmailDelivaried,name='SendingEmailDelivaried'),
    path('Image2Details/',Image2Details,name='Image2Details'),
    path('RemoveImages/',RemoveImages,name='RemoveImages'),
    path('Image3Details/',Image3Details,name='Image3Details'),
    path('AdressListDetails/',AdressListDetails,name='AdressListDetails'),
    path('RemoveAdress/',RemoveAdress,name='RemoveAdress'),
    path("CancelOrderDetails/",CancelOrderDetails,name='CancelOrderDetails'),
    path('ProfileImageDetails/',ProfileImageDetails,name='ProfileImageDetails'),
    path('ProfileNumberDetails/',ProfileNumberDetails,name='ProfileNumberDetails'),
    path('CheckUserName/',CheckUserName,name='CheckUserName'),
    path("LoginImageDetails/",LoginImageDetails,name='LoginImageDetails'),
    path("LoginImageDetails2/",LoginImageDetails2,name='LoginImageDetails2'),
    path('UserOtpDetails/',UserOtpDetails,name='UserOtpDetails'),
    path('AdminCuponCheckDetails/',AdminCuponCheckDetails,name='AdminCuponCheckDetails'),
    path('CardCheck/',CardCheck,name='CardCheck'),
    path('create_order/',create_order,name='create_order'),
    path('PaymentDetailsView/',PaymentDetailsView,name='PaymentDetailsView'),
    path('initiate_refund/',initiate_refund,name='initiate_refund'),
    path('Check/',Check,name='Check'),
    path('RefoundDetailsView/',RefoundDetailsView,name='RefoundDetailsView'),
    path('get_refund_status/<str:refund_id>/',get_refund_status,name='get_refund_status'),
    path('ExchangeDetailsView/',ExchangeDetailsView,name='ExchangeDetailsView'),
    path('ExchangeDetailsView2/',ExchangeDetailsView2,name='ExchangeDetailsView2'),
    path('RefoundDetailsView2/',RefoundDetailsView2,name='RefoundDetailsView2'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
