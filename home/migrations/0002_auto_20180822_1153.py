# Generated by Django 2.0.6 on 2018-08-22 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
