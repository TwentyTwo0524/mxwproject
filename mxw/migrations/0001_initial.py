# Generated by Django 2.1.7 on 2019-03-18 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('isselect', models.BooleanField(default=True)),
                ('isdelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'mxw_cart',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=10)),
                ('productimg', models.CharField(max_length=100)),
                ('productname', models.CharField(max_length=100)),
                ('productlongname', models.CharField(max_length=256)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('storenums', models.IntegerField()),
                ('productnum', models.IntegerField()),
            ],
            options={
                'db_table': 'mxw_goods',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=40, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=100)),
                ('img', models.CharField(default='mxw.png', max_length=40)),
            ],
            options={
                'db_table': 'mxw_user',
            },
        ),
        migrations.CreateModel(
            name='wheel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'mxw_wheel',
            },
        ),
        migrations.AddField(
            model_name='cart',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mxw.Goods'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mxw.User'),
        ),
    ]
