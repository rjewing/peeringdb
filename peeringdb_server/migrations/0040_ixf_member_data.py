# Generated by Django 2.2.13 on 2020-07-09 14:39

import django.db.models.deletion
import django.db.models.manager
import django_handleref.models
import django_inet.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("peeringdb_server", "0039_delete_duplicateipnetworkixlan"),
    ]

    operations = [
        migrations.CreateModel(
            name="IXFMemberData",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "status",
                    models.CharField(blank=True, max_length=255, verbose_name="Status"),
                ),
                (
                    "created",
                    django_handleref.models.CreatedDateTimeField(
                        auto_now_add=True, verbose_name="Created"
                    ),
                ),
                (
                    "updated",
                    django_handleref.models.UpdatedDateTimeField(
                        auto_now=True, verbose_name="Updated"
                    ),
                ),
                ("version", models.IntegerField(default=0)),
                ("asn", django_inet.models.ASNField()),
                (
                    "ipaddr4",
                    django_inet.models.IPAddressField(
                        blank=True, max_length=39, null=True
                    ),
                ),
                (
                    "ipaddr6",
                    django_inet.models.IPAddressField(
                        blank=True, max_length=39, null=True
                    ),
                ),
                ("is_rs_peer", models.BooleanField(default=False)),
                ("notes", models.CharField(blank=True, max_length=255)),
                ("speed", models.PositiveIntegerField()),
                ("operational", models.BooleanField(default=True)),
                (
                    "data",
                    models.TextField(
                        default="{}",
                        help_text="JSON snapshot of the ix-f member data that created this entry",
                    ),
                ),
                (
                    "log",
                    models.TextField(blank=True, help_text="Activity for this entry"),
                ),
                (
                    "dismissed",
                    models.BooleanField(
                        default=False,
                        help_text="Network's dismissal of this proposed change, which will hide it until from the customer facing network view",
                    ),
                ),
                (
                    "error",
                    models.TextField(
                        blank=True,
                        help_text="Trying to apply data to peeringdb raised an issue",
                        null=True,
                    ),
                ),
                ("reason", models.CharField(default="", max_length=255)),
                ("fetched", models.DateTimeField(verbose_name="Last Fetched")),
                (
                    "ixlan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ixf_set",
                        to="peeringdb_server.IXLan",
                    ),
                ),
            ],
            options={
                "verbose_name": "IXF Member Data",
                "verbose_name_plural": "IXF Member Data",
                "db_table": "peeringdb_ixf_member_data",
            },
            managers=[
                ("handleref", django.db.models.manager.Manager()),
            ],
        ),
    ]
