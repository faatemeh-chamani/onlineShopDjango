# Generated by Django 3.1.5 on 2021-01-17 15:51

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0005_comment_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='content',
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='نظر'),
        ),
    ]
