# Generated by Django 4.2.5 on 2023-09-26 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gemukyu_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('game_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Developers',
            fields=[
                ('developer_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('website', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('order_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField()),
                ('game_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('item_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('order_date', models.DateTimeField()),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Publishers',
            fields=[
                ('publisher_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('website', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('game_id', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
                ('review_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password_hash', models.CharField(max_length=255)),
                ('date_registered', models.DateTimeField()),
                ('last_login', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('wishlist_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('game_id', models.IntegerField()),
                ('added_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('game_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
                ('genre', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('publisher_id', models.IntegerField()),
                ('developer_id', models.IntegerField()),
            ],
        ),
    ]
