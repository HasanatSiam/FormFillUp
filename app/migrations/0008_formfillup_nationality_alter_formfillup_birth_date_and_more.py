# Generated by Django 4.1.3 on 2022-11-07 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_formfillup_passing_year_formfillup_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='formfillup',
            name='nationality',
            field=models.CharField(default='', max_length=200, verbose_name='nationality'),
        ),
        migrations.AlterField(
            model_name='formfillup',
            name='birth_date',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='birth_date'),
        ),
        migrations.AlterField(
            model_name='formfillup',
            name='father',
            field=models.CharField(default='', max_length=200, verbose_name='father'),
        ),
        migrations.AlterField(
            model_name='formfillup',
            name='guardian',
            field=models.CharField(default='', max_length=200, verbose_name='guardian'),
        ),
        migrations.AlterField(
            model_name='formfillup',
            name='mother',
            field=models.CharField(default='', max_length=200, verbose_name='mother'),
        ),
        migrations.AlterField(
            model_name='formfillup',
            name='phone',
            field=models.CharField(default=' ', max_length=50, verbose_name='phone'),
        ),
    ]
