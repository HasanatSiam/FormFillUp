# Generated by Django 4.1.3 on 2022-11-07 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_formfillup_code1_formfillup_code2_formfillup_code3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='formfillup',
            name='last_semester',
            field=models.CharField(default='', max_length=50, verbose_name='last_semester'),
        ),
    ]
