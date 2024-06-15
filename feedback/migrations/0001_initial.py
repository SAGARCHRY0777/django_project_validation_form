# Generated by Django 5.0.6 on 2024-06-15 16:20

import feedback.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(choices=[('general', 'General'), ('bug', 'Bug Report'), ('feature', 'Feature Request')], max_length=20)),
                ('message', models.TextField(validators=[feedback.models.validate_message_length])),
                ('sender', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
