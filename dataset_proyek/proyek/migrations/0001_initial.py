# Generated by Django 5.2.3 on 2025-06-15 07:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('target', models.CharField(max_length=255)),
                ('data_type', models.CharField(max_length=255)),
                ('aktivitas_pemrosesan', models.CharField(max_length=255)),
                ('jumlah_fitur', models.IntegerField()),
                ('ukuran_dataset', models.CharField(max_length=100)),
                ('format_file', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.CharField(max_length=100)),
                ('sender', models.CharField(blank=True, max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('file_format', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='dataset_images/')),
                ('dataset_file', models.FileField(blank=True, null=True, upload_to='dataset_files/')),
                ('creator_name', models.CharField(max_length=100)),
                ('verifier_name', models.CharField(max_length=100)),
                ('num_rows', models.IntegerField()),
                ('num_features', models.IntegerField()),
                ('keywords', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_public', models.BooleanField(default=False)),
                ('click_count', models.PositiveIntegerField(default=0, verbose_name='Jumlah Dilihat')),
                ('download_count', models.PositiveIntegerField(default=0, verbose_name='Jumlah Diunduh')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DownloadLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='download_logs', to='proyek.dataset')),
            ],
        ),
    ]
