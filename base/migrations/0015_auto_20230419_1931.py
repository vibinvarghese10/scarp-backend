# Generated by Django 3.2.18 on 2023-04-19 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_alter_customuser_usertype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='requestStatus',
            field=models.CharField(blank=True, choices=[('Accepted', 'Accepted'), ('Completed', 'Completed'), ('Request cancelled', 'Request cancelled'), ('Order cancelled', 'Order cancelled'), ('Disabled', 'Disabled')], default='Accepted', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='sellrequest',
            name='requestStatus',
            field=models.CharField(blank=True, choices=[('Requested', 'Requested'), ('Accepted', 'Accepted'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('Disabled', 'Disabled')], default='Requested', max_length=10, null=True),
        ),
    ]