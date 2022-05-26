# Generated by Django 4.0.4 on 2022-05-23 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('prodotto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCarrello',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodotti', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prodotto.prodotto')),
                ('utente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
