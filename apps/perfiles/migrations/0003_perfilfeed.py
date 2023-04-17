# Generated by Django 4.1.7 on 2023-04-16 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0002_rename_staff_usuario_is_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilFeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_text', models.CharField(max_length=200)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('usuaro_perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]