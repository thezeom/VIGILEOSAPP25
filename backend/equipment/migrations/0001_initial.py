# Generated by Django 4.2.10 on 2025-03-18 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nom')),
                ('type', models.CharField(choices=[('camera', 'Caméra'), ('video-recorder', 'Enregistreur vidéo'), ('switch', 'Switch'), ('server', 'Serveur'), ('access_point', "Point d'accès WiFi"), ('router', 'Routeur'), ('pc', 'PC'), ('other', 'Autre')], max_length=20, verbose_name='Type')),
                ('status', models.CharField(choices=[('online', 'En ligne'), ('offline', 'Hors ligne'), ('warning', 'Attention')], default='online', max_length=20, verbose_name='Statut')),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True, verbose_name='Adresse IP')),
                ('last_maintenance', models.DateField(blank=True, null=True, verbose_name='Dernière maintenance')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Créé le')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Mis à jour le')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipment', to='sites.site', verbose_name='Site')),
            ],
            options={
                'verbose_name': 'Équipement',
                'verbose_name_plural': 'Équipements',
            },
        ),
    ]
