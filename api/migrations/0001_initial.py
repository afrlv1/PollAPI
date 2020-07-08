# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 06:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('choice_text', models.TextField()),
                ('votes', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ('created', 'updated'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('question_text', models.TextField()),
            ],
            options={
                'ordering': ('created', 'updated'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionSet', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created', 'updated'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('destroyed', models.BooleanField(default=False)),
                ('public', models.BooleanField()),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roomOwner', to=settings.AUTH_USER_MODEL)),
                ('question_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room', to='api.QuestionSet')),
                ('users', models.ManyToManyField(blank=True, related_name='roomUser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created', 'updated'),
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='question',
            name='set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='api.QuestionSet'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice', to='api.Question'),
        ),
        migrations.AddField(
            model_name='choice',
            name='users',
            field=models.ManyToManyField(related_name='choiceVoted', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='questionset',
            unique_together=set([('name', 'owner')]),
        ),
    ]
