# Generated by Django 2.1.3 on 2019-09-01 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('picture', models.ImageField(upload_to='product_pics')),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField(default=1)),
            ],
        ),
    ]