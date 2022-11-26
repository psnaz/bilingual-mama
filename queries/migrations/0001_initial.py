# Generated by Django 3.2.16 on 2022-11-26 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('status', models.CharField(choices=[('PARENT', 'I am a parent'), ('EXPECTING', 'I am or we are expecting a baby'), ('BLOGGER', 'I am a blogger'), ('OTHER', 'I am just someone who wants to get in touch')], max_length=50)),
                ('subject', models.TextField(max_length=50)),
                ('message', models.TextField()),
                ('submitted', models.DateField(auto_now_add=True)),
                ('answerdate', models.DateField(blank=True, null=True)),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
