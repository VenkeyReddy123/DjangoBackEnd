# Generated by Django 5.0.2 on 2024-06-30 11:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='product_images/')),
                ('ImageUrl', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('P_Images', models.ImageField(upload_to='product_images/')),
                ('ImageUrl', models.URLField(default='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')),
                ('List_Urls', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Custamer_Name', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('Mobile_Number', models.IntegerField()),
                ('JoinDate', models.DateTimeField(null=True)),
                ('Profile_Pic', models.ImageField(null=True, upload_to='')),
                ('P_Url', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CupenCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code_Name', models.CharField(max_length=100, unique=True)),
                ('Discount_Type', models.CharField(max_length=20)),
                ('Code_Off', models.IntegerField()),
                ('ExpireDate', models.DateTimeField()),
                ('Limit', models.IntegerField()),
                ('description', models.CharField(max_length=1000, null=True)),
                ('Condtion', models.CharField(max_length=1000, null=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CheckCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Times', models.IntegerField()),
                ('Code_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.cupencode')),
                ('Custamer_Name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.login')),
            ],
        ),
        migrations.CreateModel(
            name='AdressList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Adrss_List', models.TextField()),
                ('Custamer_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.login')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('Order_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Delivary_Type', models.CharField(max_length=100)),
                ('Payment_Status', models.CharField(max_length=100)),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('Selling_Price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('Code_Using', models.IntegerField(null=True)),
                ('Delivary', models.CharField(default='No', max_length=100)),
                ('OrderCancel', models.TextField(default='No', max_length=100)),
                ('CancelDate', models.DateTimeField(null=True)),
                ('Delivary_Date', models.DateTimeField(null=True)),
                ('AdminWrite', models.CharField(max_length=100, null=True)),
                ('Size', models.TextField(default='No')),
                ('Note', models.TextField(null=True)),
                ('refund_id', models.TextField(null=True)),
                ('process', models.TextField(null=True)),
                ('Custamer_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.login')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExchangeOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('Note', models.TextField(default='yes')),
                ('Delivary', models.TextField(default='No')),
                ('Delivary_Date', models.DateTimeField(null=True)),
                ('Custamer_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.login')),
                ('Order_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.orders')),
            ],
        ),
        migrations.CreateModel(
            name='Custamer_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('Total_Amount', models.IntegerField()),
                ('City', models.CharField(max_length=100)),
                ('Adress', models.TextField()),
                ('Full_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('ImageUrl', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.image')),
                ('Custamer_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.login')),
                ('Order_Id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app1.orders')),
            ],
        ),
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Adresss', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.custamer_details')),
                ('Custamer_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.login')),
                ('Order_Id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app1.orders')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Order_Id', models.TextField()),
                ('Payment_Id', models.TextField()),
                ('Product_Name', models.TextField()),
                ('Product_Id', models.IntegerField(default=0)),
                ('Order_Id2', models.IntegerField(default=0)),
                ('Custamer_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.login')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.TextField(blank=True, null=True)),
                ('Product_Name', models.CharField(max_length=1000)),
                ('Category', models.CharField(max_length=100)),
                ('Category_Name', models.CharField(max_length=100)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Stack', models.IntegerField()),
                ('Out_Of_Stack', models.BooleanField(default=False)),
                ('Discount', models.IntegerField(null=True)),
                ('Rating', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('How_Many', models.IntegerField(default=0)),
                ('Hightlet', models.TextField(null=True)),
                ('Delivary_Charges', models.IntegerField(default=0)),
                ('Brand', models.CharField(max_length=1000, null=True)),
                ('Color', models.CharField(max_length=1000, null=True)),
                ('Specifications', models.TextField(null=True)),
                ('Size_Of_Product', models.TextField(default='No')),
                ('Size_Price', models.TextField(default='No')),
                ('ReplaceMentDays', models.IntegerField(default=7)),
                ('returnForDays', models.IntegerField(default=7)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='orders',
            name='Product_Name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.products'),
        ),
        migrations.AddField(
            model_name='image',
            name='Product_Name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='app1.products'),
        ),
        migrations.CreateModel(
            name='Add_TO_Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Size', models.TextField(default='No')),
                ('Custamer_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.login')),
                ('Product_Name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app1.products')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mobile_Number', models.IntegerField(null=True)),
                ('Profile_Pic', models.ImageField(upload_to='')),
                ('P_Url', models.TextField(default='Not Sucess')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('Rating_Lable', models.TextField(null=True)),
                ('Custamer_Name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.login')),
                ('Product_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.products')),
            ],
        ),
        migrations.CreateModel(
            name='RefoundData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PaymentProcess', models.TextField()),
                ('Payment_Id', models.TextField()),
                ('Price', models.IntegerField()),
                ('Custamer_Name', models.IntegerField()),
                ('Note', models.TextField(default='No')),
                ('RefundDate', models.DateTimeField(null=True)),
                ('Order_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.orders')),
            ],
        ),
        migrations.CreateModel(
            name='Sugget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ImageUrl', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.image')),
                ('Product_Name', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.products')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TopDeals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ImageUrl', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.image')),
                ('Product_Name', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.products')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
