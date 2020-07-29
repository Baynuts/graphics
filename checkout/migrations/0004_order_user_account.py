# Generated by Django 3.0.7 on 2020-07-29 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('checkout', '0003_auto_20200729_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='accounts.UserAccount'),
        ),
    ]
