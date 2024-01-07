# Generated by Django 4.2.3 on 2024-01-04 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0004_bank_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='aadhar_file',
            field=models.FileField(blank=True, default=None, null=True, upload_to='aadhar_card/'),
        ),
        migrations.AddField(
            model_name='employee',
            name='bank_passbook_file',
            field=models.FileField(blank=True, default=None, null=True, upload_to='bank_passbook/'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_local_address',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_permante_address',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_permante_state',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
