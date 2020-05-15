# Generated by Django 3.0.6 on 2020-05-16 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GBranch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=128, verbose_name='Name')),
                ('description', models.TextField(blank=True, default='', verbose_name='Description')),
                ('weight', models.IntegerField(default=0, help_text='Weight of the relation', verbose_name='Weight')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GTree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('public', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('description', models.TextField(blank=True, default='', verbose_name='Description')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('public', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('description', models.TextField(blank=True, default='', verbose_name='Description')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('relations', models.ManyToManyField(through='mind.GBranch', to='mind.GNode')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('kind', models.CharField(choices=[('TEXT', 'Text'), ('IMAGE', 'Image'), ('VIDEO', 'Video'), ('SOUND', 'Sound')], max_length=32)),
                ('value', models.TextField()),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='mind.GNode')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='gbranch',
            name='inbound',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outbound_branches', to='mind.GNode'),
        ),
        migrations.AddField(
            model_name='gbranch',
            name='outbound',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inbound_branches', to='mind.GNode'),
        ),
        migrations.AddField(
            model_name='gbranch',
            name='tree',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='mind.GTree'),
        ),
    ]
