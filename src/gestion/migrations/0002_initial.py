# Generated by Django 4.1.1 on 2023-03-03 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("produit", "0001_initial"),
        ("users", "0001_initial"),
        ("gestion", "0001_initial"),
        ("marche", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="stock",
            name="code_acteur",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="users.acteur",
            ),
        ),
        migrations.AddField(
            model_name="stock",
            name="code_enqueteur",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="users.enqueteur",
            ),
        ),
        migrations.AddField(
            model_name="stock",
            name="code_magasin",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="marche.magasin",
            ),
        ),
        migrations.AddField(
            model_name="stock",
            name="code_produit",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="produit.produit",
            ),
        ),
        migrations.AddField(
            model_name="stock",
            name="code_unite_produit",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="produit.uniteproduit",
            ),
        ),
        migrations.AddField(
            model_name="sortiestock",
            name="code_acteur_destinateur",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="users.acteur",
            ),
        ),
        migrations.AddField(
            model_name="sortiestock",
            name="code_enqueteur",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="users.enqueteur",
            ),
        ),
        migrations.AddField(
            model_name="sortiestock",
            name="code_stock",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="gestion.stock"
            ),
        ),
        migrations.AddField(
            model_name="commande",
            name="code_acteur_acheteur",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="customer",
                to="users.acteur",
            ),
        ),
        migrations.AddField(
            model_name="commande",
            name="code_acteur_vendeur",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="seller",
                to="users.acteur",
            ),
        ),
    ]
