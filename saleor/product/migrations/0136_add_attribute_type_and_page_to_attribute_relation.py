# Generated by Django 3.1 on 2020-10-09 10:17

import django.db.models.deletion
from django.db import migrations, models


def set_product_type_to_all_existing_attributes(apps, schema_editor):
    Attribute = apps.get_model("product", "Attribute")
    Attribute.objects.all().update(type="product-type")


class Migration(migrations.Migration):

    dependencies = [
        ("page", "0017_pagetype"),
        ("product", "0135_collection_channel_listing"),
    ]

    operations = [
        migrations.AddField(
            model_name="attribute",
            name="type",
            field=models.CharField(
                choices=[("product-type", "Product type"), ("page-type", "Page type")],
                max_length=50,
                null=True,
            ),
        ),
        migrations.RunPython(
            set_product_type_to_all_existing_attributes,
            migrations.RunPython.noop,
        ),
        migrations.AlterField(
            model_name="attribute",
            name="type",
            field=models.CharField(
                choices=[("product-type", "Product type"), ("page-type", "Page type")],
                max_length=50,
            ),
        ),
        migrations.CreateModel(
            name="AssignedPageAttribute",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="AttributePage",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(db_index=True, editable=False, null=True),
                ),
                (
                    "assigned_pages",
                    models.ManyToManyField(
                        blank=True,
                        related_name="attributesrelated",
                        through="product.AssignedPageAttribute",
                        to="page.Page",
                    ),
                ),
                (
                    "attribute",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attributepage",
                        to="product.attribute",
                    ),
                ),
                (
                    "page_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attributepage",
                        to="page.pagetype",
                    ),
                ),
            ],
            options={
                "ordering": ("sort_order", "pk"),
                "unique_together": {("attribute", "page_type")},
            },
        ),
        migrations.AddField(
            model_name="assignedpageattribute",
            name="assignment",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pageassignments",
                to="product.attributepage",
            ),
        ),
        migrations.AddField(
            model_name="assignedpageattribute",
            name="page",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="attributes",
                to="page.page",
            ),
        ),
        migrations.AddField(
            model_name="assignedpageattribute",
            name="values",
            field=models.ManyToManyField(to="product.AttributeValue"),
        ),
        migrations.AddField(
            model_name="attribute",
            name="page_types",
            field=models.ManyToManyField(
                blank=True,
                related_name="page_attributes",
                through="product.AttributePage",
                to="page.PageType",
            ),
        ),
    ]