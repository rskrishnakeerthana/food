# Generated by Django 4.1 on 2022-09-30 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sub_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subfood_name', models.CharField(default='', max_length=150)),
                ('subfood_price', models.FloatField(default='', max_length=50)),
                ('subfood_image', models.ImageField(null=True, upload_to='sub_categories')),
                ('foodcate_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.food_categories')),
            ],
        ),
    ]
