# Generated by Django 4.2.10 on 2024-05-01 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='catering_company',
        ),
        migrations.RemoveField(
            model_name='event',
            name='cleaning_company',
        ),
        migrations.RemoveField(
            model_name='event',
            name='decorations_company',
        ),
        migrations.RemoveField(
            model_name='event',
            name='entertainment_company',
        ),
        migrations.RemoveField(
            model_name='event',
            name='furniture_company',
        ),
        migrations.RemoveField(
            model_name='event',
            name='suppliers',
        ),
        migrations.AddField(
            model_name='event',
            name='caterer',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='events.caterer'),
        ),
        migrations.AlterField(
            model_name='event',
            name='client',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='events.client'),
        ),
        migrations.AlterField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='events.venue'),
        ),
        migrations.DeleteModel(
            name='CateringCompany',
        ),
        migrations.DeleteModel(
            name='CleaningCompany',
        ),
        migrations.DeleteModel(
            name='DecorationsCompany',
        ),
        migrations.DeleteModel(
            name='EntertainmentCompany',
        ),
        migrations.DeleteModel(
            name='FurnitureSupplyCompany',
        ),
        migrations.DeleteModel(
            name='Supplier',
        ),
    ]