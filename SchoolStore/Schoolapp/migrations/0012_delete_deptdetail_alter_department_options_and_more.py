# Generated by Django 4.1.7 on 2023-02-21 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Schoolapp', '0011_remove_deptdetail_department_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DeptDetail',
        ),
        migrations.AlterModelOptions(
            name='department',
            options={},
        ),
        migrations.RemoveField(
            model_name='department',
            name='slug',
        ),
    ]
