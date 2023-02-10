# Generated by Django 4.1.5 on 2023-02-09 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Acteur",
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
                ("code_acteur", models.CharField(max_length=50)),
                ("coordonnee", models.CharField(max_length=50)),
                ("picture", models.FileField(upload_to="acteur_img")),
                ("description", models.TextField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Filiere",
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
                ("code_filiere", models.CharField(max_length=50)),
                ("nom_filiere", models.CharField(max_length=50)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="TypeActeur",
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
                ("code_type_acteur", models.CharField(max_length=150)),
                ("libele", models.CharField(max_length=50)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="TypeFilier",
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
                ("code_type_filiere", models.CharField(max_length=50)),
                ("nom_type_filiere", models.CharField(max_length=250)),
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
        migrations.CreateModel(
            name="Produit",
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
                ("nom_produit", models.CharField(max_length=250)),
                ("code_produit", models.CharField(max_length=50)),
                ("forme_produit", models.CharField(max_length=50)),
                ("maillon_produit", models.CharField(max_length=50)),
                ("photo", models.FileField(upload_to="img_produit")),
                ("description", models.TextField()),
                (
                    "code_filier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="web.filiere"
                    ),
                ),
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
                ("code_marche", models.CharField(max_length=50)),
                ("locaclite", models.CharField(max_length=250)),
                ("jour_marche", models.CharField(max_length=50)),
                ("code_superviseur", models.CharField(max_length=50)),
                ("coordonnee_geo", models.CharField(max_length=250)),
                ("superficie", models.CharField(max_length=250)),
                ("caracteristique", models.CharField(max_length=250)),
                ("photo", models.FileField(upload_to="img_marche")),
                (
                    "code_type_marche",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="web.typemarche"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
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
                ("localite_magasin", models.CharField(max_length=250)),
                ("coordonnee_geo", models.CharField(max_length=250)),
                ("volume", models.IntegerField()),
                ("caracteristique", models.TextField()),
                ("photo", models.FileField(upload_to="img_magasin")),
                (
                    "code_acteur",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="web.acteur"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="acteur",
            name="type_acteur",
            field=models.ManyToManyField(to="web.typeacteur"),
        ),
    ]
