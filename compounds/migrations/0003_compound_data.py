# Generated by Django 4.0.2 on 2022-03-07 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('compounds', '0002_computed_molecular_weight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compound_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IUPAC_name', models.TextField()),
                ('molecular_weight', models.TextField()),
                ('boiling_point', models.TextField()),
                ('melting_point', models.TextField()),
                ('solubility', models.TextField()),
                ('density', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
