# Generated by Django 3.0.3 on 2020-04-09 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Performer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('nationality', models.CharField(max_length=20)),
                ('masterpiece', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('weight', models.CharField(default='191g', max_length=20)),
                ('size', models.CharField(default='161mm*76mm', max_length=20)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Type')),
            ],
        ),
        migrations.CreateModel(
            name='Performer_info',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('birth', models.CharField(max_length=20)),
                ('elapse', models.CharField(max_length=20)),
                ('performer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='index.Performer')),
            ],
        ),
    ]
