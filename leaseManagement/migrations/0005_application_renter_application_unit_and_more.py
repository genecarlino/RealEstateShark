# Generated by Django 4.0.3 on 2022-03-19 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unitManagement', '0004_remove_community_address_id_remove_unit_address_id_and_more'),
        ('leaseManagement', '0004_delete_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='renter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='leaseManagement.renter'),
        ),
        migrations.AddField(
            model_name='application',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='unitManagement.unit'),
        ),
        migrations.AddField(
            model_name='unit_lease',
            name='application',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='leaseManagement.application'),
        ),
        migrations.AddField(
            model_name='unit_lease',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='unitManagement.unit'),
        ),
    ]
