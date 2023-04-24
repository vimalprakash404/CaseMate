# Generated by Django 4.1.6 on 2023-04-24 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_user', '0011_remove_caseregister_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notary',
            name='Address',
        ),
        migrations.CreateModel(
            name='Judgement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('details', models.CharField(max_length=50)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin_user.caseregister')),
            ],
        ),
    ]
