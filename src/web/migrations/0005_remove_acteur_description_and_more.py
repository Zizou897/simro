# Generated by Django 4.1.5 on 2023-02-10 23:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("web", "0004_forme_maillon_alter_produit_code_filier_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="acteur",
            name="description",
        ),
        migrations.AlterField(
            model_name="marche",
            name="code_superviseur",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
