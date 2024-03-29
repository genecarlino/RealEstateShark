# Generated by Django 4.0.3 on 2022-03-15 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unitManagement', '0003_initial'),
        ('leaseManagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='renter_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='leaseManagement.renter'),
        ),
        migrations.AddField(
            model_name='application',
            name='staff_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='leaseManagement.staff'),
        ),
        migrations.AddField(
            model_name='application',
            name='unit_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='unitManagement.unit'),
        ),
        migrations.AddField(
            model_name='unit_lease',
            name='application_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='leaseManagement.application'),
        ),
        migrations.AddField(
            model_name='unit_lease',
            name='unit_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='unitManagement.unit'),
        ),
    ]
