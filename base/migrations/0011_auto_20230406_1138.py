# Generated by Django 3.2.18 on 2023-04-06 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_auto_20230326_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='requestStatus',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Completed', 'Completed'), ('Request cancelled', 'Request cancelled'), ('Order cancelled', 'Order cancelled'), ('Disabled', 'Disabled')], default='Accepted', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='sellrequest',
            name='requestStatus',
            field=models.CharField(choices=[('Requested', 'Requested'), ('Accepted', 'Accepted'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('Disabled', 'Disabled')], default='Requested', max_length=10, null=True),
        ),
    ]
