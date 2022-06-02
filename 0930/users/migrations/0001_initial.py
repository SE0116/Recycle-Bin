# Generated by Django 3.2.7 on 2021-10-02 20:03

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
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_img', models.ImageField(blank=True, upload_to='user_img')),
                ('nickname', models.CharField(blank=True, max_length=20)),
                ('intro', models.TextField(blank=True)),
                ('user_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_name', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]