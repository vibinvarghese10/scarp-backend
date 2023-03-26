# Generated by Django 3.2.18 on 2023-03-26 12:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_address_order_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='sellRequest',
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sellrequest',
            name='pickupAddress',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.address'),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(null=True)),
                ('price', models.IntegerField(null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.order')),
            ],
        ),
    ]