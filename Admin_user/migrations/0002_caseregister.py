# Generated by Django 4.1.6 on 2023-02-09 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('case_number', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('advocate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin_user.advocate')),
            ],
        ),
    ]
