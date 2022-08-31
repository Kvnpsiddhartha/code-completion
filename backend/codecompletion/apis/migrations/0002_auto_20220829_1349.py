# Generated by Django 3.2.9 on 2022-08-29 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='code',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='folder',
            name='parent_folder',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_folders', to='apis.folder'),
        ),
    ]
