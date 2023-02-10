# Generated by Django 4.1.5 on 2023-02-08 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("farmacia", "0002_remove_medicamento_desconto_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="preco",
            options={"verbose_name": "Preços", "verbose_name_plural": "Preços"},
        ),
        migrations.RemoveField(model_name="feedback", name="feedback_negativos",),
        migrations.RemoveField(model_name="feedback", name="feedback_positivos",),
        migrations.AddField(
            model_name="feedback",
            name="negativos",
            field=models.IntegerField(blank=True, null=True, verbose_name="Negativos"),
        ),
        migrations.AddField(
            model_name="feedback",
            name="positivos",
            field=models.IntegerField(blank=True, null=True, verbose_name="Positivos"),
        ),
    ]