# Generated by Django 3.2.4 on 2021-06-10 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpostapp', '0004_remove_comment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
