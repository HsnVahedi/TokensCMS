# Generated by Django 3.2.8 on 2021-11-22 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('tokens', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EthereumNetwork',
            fields=[
                ('name', models.TextField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Ethereum Network',
                'verbose_name_plural': 'Ethereum Networks',
            },
        ),
        migrations.CreateModel(
            name='TronNetwork',
            fields=[
                ('name', models.TextField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Tron Network',
                'verbose_name_plural': 'Tron Networks',
            },
        ),
        migrations.CreateModel(
            name='TRC20Token',
            fields=[
                ('symbol', models.TextField(primary_key=True, serialize=False)),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('network', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trc20_tokens', to='tokens.tronnetwork')),
            ],
            options={
                'verbose_name': 'TRC20 Token',
                'verbose_name_plural': 'TRC20 Tokens',
            },
        ),
        migrations.CreateModel(
            name='TRC20DefaultToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': 'TRC20 Default Token',
                'verbose_name_plural': 'TRC20 Default Tokens',
            },
        ),
        migrations.AddField(
            model_name='erc20token',
            name='network',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='erc20_tokens', to='tokens.ethereumnetwork'),
        ),
        migrations.AddField(
            model_name='erc721token',
            name='network',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='erc721_tokens', to='tokens.ethereumnetwork'),
        ),
    ]
