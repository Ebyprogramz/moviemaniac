# Generated by Django 3.2.6 on 2021-09-02 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='MXPLAYER', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
