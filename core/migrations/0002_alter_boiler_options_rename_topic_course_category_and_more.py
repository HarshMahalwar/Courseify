# Generated by Django 4.0.4 on 2022-05-24 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='boiler',
            options={},
        ),
        migrations.RenameField(
            model_name='course',
            old_name='topic',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]