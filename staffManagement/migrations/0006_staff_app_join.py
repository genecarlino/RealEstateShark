# Generated by Django 4.0.3 on 2022-03-19 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leaseManagement', '0005_application_renter_application_unit_and_more'),
        ('staffManagement', '0005_rent_payment_log_staff_service_request_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff_APP_Join',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='leaseManagement.application')),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='staffManagement.staff')),
            ],
        ),
    ]