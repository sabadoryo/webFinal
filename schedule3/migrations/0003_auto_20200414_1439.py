# Generated by Django 3.0.5 on 2020-04-14 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule3', '0002_auto_20200414_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='room',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='start',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='subject',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='schedule3.Subjects'),
        ),
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.CharField(choices=[('0', 'Lecture'), ('1', 'Practice'), ('2', 'Laboratory')], max_length=20, null=True),
        ),
    ]
