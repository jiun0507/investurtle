# Generated by Django 3.2.1 on 2021-06-12 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20210612_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='log',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='works', to='post.log'),
        ),
    ]
