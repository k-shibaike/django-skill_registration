# Generated by Django 4.2 on 2023-11-02 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("introduction_app", "0002_alter_product_image_alter_skill_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(null=True, upload_to="images"),
        ),
        migrations.AlterField(
            model_name="skill",
            name="image",
            field=models.ImageField(null=True, upload_to="images"),
        ),
    ]