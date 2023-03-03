# Generated by Django 4.1.1 on 2023-03-03 02:27

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Magasin",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_add", models.DateTimeField(auto_now_add=True)),
                ("date_update", models.DateTimeField(auto_now=True)),
                ("publish", models.BooleanField(default=False)),
                ("code_magasin", models.CharField(max_length=50)),
                ("coordonnee_geo", models.CharField(max_length=250)),
                ("volume", models.IntegerField()),
                ("caracteristique", models.TextField()),
                ("photo", models.FileField(upload_to="img_magasin")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Marche",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_add", models.DateTimeField(auto_now_add=True)),
                ("date_update", models.DateTimeField(auto_now=True)),
                ("publish", models.BooleanField(default=False)),
                (
                    "nom_marche",
                    models.CharField(default="marché mamiAdjoua", max_length=250),
                ),
                ("code_marche", models.CharField(max_length=50)),
                ("coordonnee_geo", models.CharField(max_length=250)),
                ("superficie", models.CharField(max_length=250)),
                ("caracteristique", models.CharField(max_length=250)),
                ("photo", models.FileField(upload_to="img_marche")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="TypeMarche",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_add", models.DateTimeField(auto_now_add=True)),
                ("date_update", models.DateTimeField(auto_now=True)),
                ("publish", models.BooleanField(default=False)),
                ("code_type_marche", models.CharField(max_length=50)),
                ("nom_type_marche", models.CharField(max_length=250)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]