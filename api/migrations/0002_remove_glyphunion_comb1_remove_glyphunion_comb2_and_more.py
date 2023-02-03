# Generated by Django 4.0 on 2023-02-01 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='glyphunion',
            name='comb1',
        ),
        migrations.RemoveField(
            model_name='glyphunion',
            name='comb2',
        ),
        migrations.AddField(
            model_name='glyphunion',
            name='back',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='glyphunion',
            name='slot1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='glyphunion',
            name='slot2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='glyphunion',
            name='attack',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='glyphunion',
            name='attribute',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='glyphunion',
            name='notes',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='attributes',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='statistics',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]