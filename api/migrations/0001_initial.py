# Generated by Django 4.1 on 2022-08-19 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GUnion",
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
                ("name", models.CharField(max_length=200)),
                ("attk", models.CharField(max_length=200)),
                ("attribute", models.CharField(max_length=200)),
                ("consume", models.CharField(max_length=200)),
                ("effect", models.CharField(max_length=200)),
                ("notes", models.CharField(max_length=200)),
                ("comb_1", models.CharField(max_length=200)),
                ("comb_2", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Weapon",
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
                ("name", models.CharField(max_length=200)),
                ("description", models.CharField(max_length=200)),
                ("type", models.CharField(max_length=200)),
                ("attribute", models.CharField(max_length=200)),
                ("statistic", models.CharField(max_length=200)),
                ("found", models.CharField(max_length=200)),
                ("consume", models.CharField(max_length=200)),
                ("notes", models.CharField(max_length=200)),
            ],
        ),
    ]