# Generated by Django 4.2.16 on 2024-12-20 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deposits', to='user.useraccount')),
            ],
        ),
    ]
