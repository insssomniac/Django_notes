# Generated by Django 5.1.7 on 2025-03-27 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_alter_notes_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]
