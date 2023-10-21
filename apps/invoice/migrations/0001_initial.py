# Generated by Django 4.2.1 on 2023-10-21 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Invoice",
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
                (
                    "title",
                    models.CharField(
                        blank=True, default="Invoice", max_length=100, null=True
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "logo",
                    models.ImageField(blank=True, null=True, upload_to="static/images"),
                ),
                ("invoice_number", models.CharField(max_length=100)),
                ("invoice_date", models.DateField()),
                ("paymnet_due", models.DateField()),
                ("footer_text", models.TextField(blank=True, null=True)),
                ("is_draft", models.BooleanField(default=True)),
                ("is_send", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Item",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                ("quantity", models.IntegerField()),
                ("price", models.IntegerField()),
                ("amout", models.IntegerField()),
                (
                    "invoice",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="invoice.invoice",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("phone", models.CharField(blank=True, max_length=20, null=True)),
                ("first_name", models.CharField(blank=True, max_length=100, null=True)),
                ("last_name", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "invoice",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="invoice.invoice",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Business",
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
                ("name", models.CharField(max_length=100)),
                ("address1", models.CharField(blank=True, max_length=100, null=True)),
                ("address2", models.CharField(blank=True, max_length=100, null=True)),
                ("city", models.CharField(blank=True, max_length=100, null=True)),
                ("zip_code", models.CharField(blank=True, max_length=100, null=True)),
                ("country", models.CharField(blank=True, max_length=100, null=True)),
                ("state", models.CharField(blank=True, max_length=100, null=True)),
                ("phone", models.CharField(blank=True, max_length=100, null=True)),
                ("fax", models.CharField(blank=True, max_length=100, null=True)),
                ("mobile", models.CharField(blank=True, max_length=100, null=True)),
                ("toll_free", models.CharField(blank=True, max_length=100, null=True)),
                ("website", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "invoice",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="invoice.invoice",
                    ),
                ),
            ],
        ),
    ]