# Generated by Django 3.0.4 on 2020-04-15 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_auto_20200415_1339'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name_of_category',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='categories',
        ),
        migrations.AddField(
            model_name='category',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.Product'),
        ),
    ]