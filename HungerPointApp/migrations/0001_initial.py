# Generated by Django 5.0.2 on 2024-02-09 13:38

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
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(blank=True, max_length=250, null=True)),
                ('c_c_timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Create_TimeStamp')),
                ('c_u_timestamp', models.DateTimeField(auto_now=True, null=True, verbose_name='Update_TimeStamp')),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryDriver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=250, null=True)),
                ('dd_c_timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Create_TimeStamp')),
                ('dd_u_timestamp', models.DateTimeField(auto_now=True, null=True, verbose_name='Update_TimeStamp')),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryPartners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dp_name', models.CharField(blank=True, max_length=250, null=True)),
                ('dp_img_path', models.CharField(blank=True, max_length=250, null=True)),
                ('dp_ph_number', models.CharField(blank=True, max_length=250, null=True)),
                ('dp_charges', models.CharField(blank=True, max_length=250, null=True)),
                ('dp_c_timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Create_TimeStamp')),
                ('dp_u_timestamp', models.DateTimeField(auto_now=True, null=True, verbose_name='Update_TimeStamp')),
            ],
        ),
        migrations.CreateModel(
            name='FoodCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=250, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=250, null=True)),
                ('fc_c_timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Create_TimeStamp')),
                ('fc_u_timestamp', models.DateTimeField(auto_now=True, null=True, verbose_name='Update_TimeStamp')),
            ],
        ),
        migrations.CreateModel(
            name='Toppings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('price', models.CharField(blank=True, max_length=250, null=True)),
                ('t_c_timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Create_TimeStamp')),
                ('t_u_timestamp', models.DateTimeField(auto_now=True, null=True, verbose_name='Update_TimeStamp')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(blank=True, max_length=250, null=True)),
                ('l_name', models.CharField(blank=True, max_length=250, null=True)),
                ('address_tag', models.CharField(blank=True, max_length=250, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=250, null=True)),
                ('flat', models.CharField(blank=True, max_length=250, null=True)),
                ('area', models.CharField(blank=True, max_length=250, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=250, null=True)),
                ('city', models.CharField(blank=True, max_length=250, null=True)),
                ('google_map_link', models.CharField(blank=True, max_length=250, null=True)),
                ('a_c_timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Create_TimeStamp')),
                ('a_u_timestamp', models.DateTimeField(auto_now=True, null=True, verbose_name='Update_TimeStamp')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HungerPointApp.country')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=250, null=True)),
                ('email_id', models.CharField(blank=True, max_length=250, null=True)),
                ('password', models.CharField(blank=True, max_length=250, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=250, null=True)),
                ('facebook_id', models.CharField(blank=True, max_length=250, null=True)),
                ('customer_c_timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Create_TimeStamp')),
                ('customer_u_timestamp', models.DateTimeField(auto_now=True, null=True, verbose_name='Update_TimeStamp')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HungerPointApp.address')),
                ('super_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FoodItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('tag_list', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('price', models.CharField(blank=True, max_length=250, null=True)),
                ('image_path', models.CharField(blank=True, max_length=250, null=True)),
                ('f_c_timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Create_TimeStamp')),
                ('f_u_timestamp', models.DateTimeField(auto_now=True, null=True, verbose_name='Update_TimeStamp')),
                ('food_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HungerPointApp.foodcategories')),
            ],
        ),
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(blank=True, max_length=250, null=True)),
                ('c_c_timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Create_TimeStamp')),
                ('c_u_timestamp', models.DateTimeField(auto_now=True, null=True, verbose_name='Update_TimeStamp')),
                ('customer_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HungerPointApp.customuser')),
                ('food_items', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HungerPointApp.fooditems')),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_c_timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Create_TimeStamp')),
                ('l_u_timestamp', models.DateTimeField(auto_now=True, null=True, verbose_name='Update_TimeStamp')),
                ('customer_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HungerPointApp.customuser')),
                ('food_items', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HungerPointApp.fooditems')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.CharField(blank=True, max_length=250, null=True)),
                ('order_time', models.CharField(blank=True, max_length=250, null=True)),
                ('total_amount', models.CharField(blank=True, max_length=250, null=True)),
                ('order_status', models.CharField(blank=True, max_length=250, null=True)),
                ('payment_method', models.CharField(blank=True, max_length=250, null=True)),
                ('transaction_id', models.CharField(blank=True, max_length=250, null=True)),
                ('devlivery_method', models.CharField(blank=True, max_length=250, null=True)),
                ('delivery_fee', models.CharField(blank=True, max_length=250, null=True)),
                ('requested_delivery_time', models.CharField(blank=True, max_length=250, null=True)),
                ('driver_rating', models.CharField(blank=True, max_length=250, null=True)),
                ('restaurent_rating', models.CharField(blank=True, max_length=250, null=True)),
                ('o_c_timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Create_TimeStamp')),
                ('o_u_timestamp', models.DateTimeField(auto_now=True, null=True, verbose_name='Update_TimeStamp')),
                ('customer_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HungerPointApp.customuser')),
                ('delivery_driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HungerPointApp.deliverydriver')),
                ('delivery_partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HungerPointApp.deliverypartners')),
            ],
        ),
        migrations.CreateModel(
            name='OrdersItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toppings_id_list', models.JSONField(blank=True, null=True)),
                ('complete_order_item', models.JSONField(blank=True, null=True)),
                ('quantity', models.CharField(blank=True, max_length=250, null=True)),
                ('ot_c_timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Create_TimeStamp')),
                ('ot_u_timestamp', models.DateTimeField(auto_now=True, null=True, verbose_name='Update_TimeStamp')),
                ('food_items', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HungerPointApp.fooditems')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HungerPointApp.orders')),
            ],
        ),
        migrations.CreateModel(
            name='OrderTracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=250, null=True)),
                ('time_stamp', models.CharField(blank=True, max_length=250, null=True)),
                ('ot_c_timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Create_TimeStamp')),
                ('ot_u_timestamp', models.DateTimeField(auto_now=True, null=True, verbose_name='Update_TimeStamp')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HungerPointApp.orders')),
            ],
        ),
        migrations.CreateModel(
            name='PromoCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=250, null=True)),
                ('discount_amount', models.CharField(blank=True, max_length=250, null=True)),
                ('valid_from', models.CharField(blank=True, max_length=250, null=True)),
                ('valid_to', models.CharField(blank=True, max_length=250, null=True)),
                ('pc_c_timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Create_TimeStamp')),
                ('pc_u_timestamp', models.DateTimeField(auto_now=True, null=True, verbose_name='Update_TimeStamp')),
                ('customer_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HungerPointApp.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurent_name', models.CharField(blank=True, max_length=250, null=True)),
                ('dp_list', models.CharField(blank=True, max_length=250, null=True)),
                ('leave_list', models.CharField(blank=True, max_length=250, null=True)),
                ('every_day_time_list', models.CharField(blank=True, max_length=250, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=250, null=True)),
                ('branch', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('logo_path', models.CharField(blank=True, max_length=250, null=True)),
                ('r_c_timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Create_TimeStamp')),
                ('r_u_timestamp', models.DateTimeField(auto_now=True, null=True, verbose_name='Update_TimeStamp')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HungerPointApp.address')),
            ],
        ),
        migrations.AddField(
            model_name='orders',
            name='restaurent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HungerPointApp.restaurent'),
        ),
        migrations.AddField(
            model_name='foodcategories',
            name='restaurent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HungerPointApp.restaurent'),
        ),
        migrations.CreateModel(
            name='ToppingsItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toppings_id_list', models.JSONField(blank=True, null=True)),
                ('ti_c_timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Create_TimeStamp')),
                ('ti_u_timestamp', models.DateTimeField(auto_now=True, null=True, verbose_name='Update_TimeStamp')),
                ('food_items', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HungerPointApp.fooditems')),
            ],
        ),
        migrations.CreateModel(
            name='UserActionTracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_type', models.CharField(blank=True, max_length=250, null=True)),
                ('action_time_stamp', models.CharField(blank=True, max_length=250, null=True)),
                ('uat_c_timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Create_TimeStamp')),
                ('uat_u_timestamp', models.DateTimeField(auto_now=True, null=True, verbose_name='Update_TimeStamp')),
                ('customer_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HungerPointApp.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='UserPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(blank=True, max_length=250, null=True)),
                ('payment_date', models.CharField(blank=True, max_length=250, null=True)),
                ('payment_status', models.CharField(blank=True, max_length=250, null=True)),
                ('transaction_id', models.CharField(blank=True, max_length=250, null=True)),
                ('payment_gateway_response', models.CharField(blank=True, max_length=250, null=True)),
                ('up_c_timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Create_TimeStamp')),
                ('up_u_timestamp', models.DateTimeField(auto_now=True, null=True, verbose_name='Update_TimeStamp')),
                ('customer_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HungerPointApp.customuser')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HungerPointApp.orders')),
            ],
        ),
    ]
