# Generated by Django 4.0.3 on 2022-03-15 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requirement', models.CharField(max_length=100, null=True)),
                ('submit_date', models.DateTimeField(auto_now_add=True)),
                ('processing_date', models.DateTimeField(null=True)),
                ('processing_status', models.CharField(blank=True, max_length=75, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Renter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('identity_proof_document', models.CharField(max_length=100)),
                ('identity_proof_id', models.CharField(max_length=100)),
                ('permenant_address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('staff_role', models.CharField(max_length=50)),
                ('employment_start_date', models.DateField()),
                ('employment_end_date', models.DateField(null=True)),
                ('staff_notes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unit_Lease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lease_tenure_in_months', models.IntegerField(default=10)),
                ('monthly_rent', models.DecimalField(decimal_places=2, max_digits=20)),
                ('discount_in_rent', models.DecimalField(decimal_places=2, max_digits=20)),
                ('lease_starting_from', models.DateField(null=True)),
                ('lease_ending_on', models.DateField(null=True)),
            ],
        ),
    ]
