# Generated by Django 4.2.4 on 2023-09-29 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cbvapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodprod',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='companies', to='cbvapp.company'),
            preserve_default=False,
        ),
    ]
