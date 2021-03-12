# Generated by Django 3.1.5 on 2021-03-04 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_order', '0004_auto_20210304_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completeorderuser',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop_order.city', verbose_name='شهر'),
        ),
        migrations.AlterField(
            model_name='completeorderuser',
            name='family',
            field=models.CharField(max_length=50, verbose_name=' نام\u200cخانوادگی'),
        ),
        migrations.AlterField(
            model_name='completeorderuser',
            name='name',
            field=models.CharField(max_length=50, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='completeorderuser',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='eshop_order.order', verbose_name='سبد خرید'),
        ),
        migrations.AlterField(
            model_name='completeorderuser',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop_order.province', verbose_name='استان'),
        ),
    ]
