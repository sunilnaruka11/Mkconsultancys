# Generated by Django 4.2.3 on 2024-01-06 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0006_employee_emp_designation_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_dob',
            field=models.DateField(blank=True, max_length=20, null=True),
        ),
    ]