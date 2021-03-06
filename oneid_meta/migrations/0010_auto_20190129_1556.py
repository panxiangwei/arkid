# Generated by Django 2.0.7 on 2019-01-29 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneid_meta', '0009_dinggroup_is_role_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dinggroup',
            name='is_role_group',
        ),
        migrations.AddField(
            model_name='dinggroup',
            name='is_group',
            field=models.BooleanField(default=False, verbose_name='区分角色组与角色，标签与标签组'),
        ),
        migrations.AddField(
            model_name='dinggroup',
            name='subject',
            field=models.CharField(choices=[('role', '角色与角色组（内部人员）'), ('label', '标签与标签组（外部人员）')], default='role', max_length=128, verbose_name='组类型'),
        ),
    ]
