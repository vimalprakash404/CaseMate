# Generated by Django 4.1.6 on 2023-04-26 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_user', '0012_remove_notary_address_judgement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Judgement_files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='judgement')),
                ('judgement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin_user.judgement')),
            ],
        ),
    ]
