# Generated by Django 4.1.7 on 2023-02-21 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Schoolapp', '0010_alter_student_materials'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deptdetail',
            name='department',
        ),
        migrations.RemoveField(
            model_name='deptdetail',
            name='mission',
        ),
        migrations.RemoveField(
            model_name='deptdetail',
            name='overview',
        ),
        migrations.RemoveField(
            model_name='deptdetail',
            name='vision',
        ),
        migrations.AddField(
            model_name='department',
            name='mission',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='department',
            name='overview',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='department',
            name='vision',
            field=models.TextField(blank=True),
        ),
    ]
