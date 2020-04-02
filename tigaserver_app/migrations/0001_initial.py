# Generated by Django 2.2.7 on 2020-04-01 14:50

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import tigaserver_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(help_text='Auto-incremented primary key record ID.', primary_key=True, serialize=False)),
                ('samples_per_day', models.IntegerField(help_text='Number of randomly-timed location samples to take per day.')),
                ('creation_time', models.DateTimeField(auto_now_add=True, help_text='Date and time when this configuration was created by MoveLab. Automatically generated when record is saved.')),
            ],
        ),
        migrations.CreateModel(
            name='EuropeCountry',
            fields=[
                ('gid', models.IntegerField(primary_key=True, serialize=False)),
                ('cntr_id', models.CharField(blank=True, max_length=2)),
                ('name_engl', models.CharField(blank=True, max_length=44)),
                ('iso3_code', models.CharField(blank=True, max_length=3)),
                ('fid', models.CharField(blank=True, max_length=2)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
                ('x_min', models.FloatField(blank=True, null=True)),
                ('x_max', models.FloatField(blank=True, null=True)),
                ('y_min', models.FloatField(blank=True, null=True)),
                ('y_max', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'europe_countries',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Fix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_coverage_uuid', models.CharField(blank=True, help_text='UUID randomly generated on phone to identify each unique user, but only within the coverage data so that privacy issues are not raised by linking this to the report data.. Must be exactly 36 characters (32 hex digits plus 4 hyphens).', max_length=36, null=True)),
                ('fix_time', models.DateTimeField(help_text='Date and time when fix was recorded on phone. Format as ECMA 262 date time string (e.g. "2014-05-17T12:34:56.123+01:00".')),
                ('server_upload_time', models.DateTimeField(auto_now_add=True, help_text='Date and time registered by server when it received fix upload. Automatically generated by server.')),
                ('phone_upload_time', models.DateTimeField(help_text='Date and time on phone when it uploaded fix. Format as ECMA 262 date time string (e.g. "2014-05-17T12:34:56.123+01:00".')),
                ('masked_lon', models.FloatField(help_text='Longitude rounded down to nearest 0.5 decimal degree (floor(lon/.5)*.5).')),
                ('masked_lat', models.FloatField(help_text='Latitude rounded down to nearest 0.5 decimal degree (floor(lat/.5)*.5).')),
                ('power', models.FloatField(blank=True, help_text='Power level of phone at time fix recorded, expressed as proportion of full charge. Range: 0-1.', null=True)),
            ],
            options={
                'verbose_name': 'fix',
                'verbose_name_plural': 'fixes',
            },
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(help_text='Unique identifier of the mission. Automatically generated by server when mission created.', primary_key=True, serialize=False)),
                ('title_catalan', models.CharField(help_text='Title of mission in Catalan', max_length=200)),
                ('title_spanish', models.CharField(help_text='Title of mission in Spanish', max_length=200)),
                ('title_english', models.CharField(help_text='Title of mission in English', max_length=200)),
                ('short_description_catalan', models.CharField(help_text='Catalan text to be displayed in mission list.', max_length=200)),
                ('short_description_spanish', models.CharField(help_text='Spanish text to be displayed in mission list.', max_length=200)),
                ('short_description_english', models.CharField(help_text='English text to be displayed in mission list.', max_length=200)),
                ('long_description_catalan', models.CharField(blank=True, help_text='Catalan text that fully explains mission to user', max_length=1000)),
                ('long_description_spanish', models.CharField(blank=True, help_text='Spanish text that fully explains mission to user', max_length=1000)),
                ('long_description_english', models.CharField(blank=True, help_text='English text that fully explains mission to user', max_length=1000)),
                ('help_text_catalan', models.TextField(blank=True, help_text='Catalan text to be displayed when user taps mission help button.')),
                ('help_text_spanish', models.TextField(blank=True, help_text='Spanish text to be displayed when user taps mission help button.')),
                ('help_text_english', models.TextField(blank=True, help_text='English text to be displayed when user taps mission help button.')),
                ('platform', models.CharField(choices=[('none', 'No platforms (for drafts)'), ('and', 'Android'), ('ios', 'iOS'), ('html', 'HTML5'), ('beta', 'beta versions only'), ('all', 'All platforms')], help_text='What type of device is this mission is intended for? It will be sent only to these devices', max_length=4)),
                ('creation_time', models.DateTimeField(auto_now=True, help_text='Date and time mission was created by MoveLab. Automatically generated when mission saved.')),
                ('expiration_time', models.DateTimeField(blank=True, help_text='Optional date and time when mission should expire (if ever). Mission will no longer be displayed to users after this date-time.', null=True)),
                ('photo_mission', models.BooleanField(help_text='Should this mission allow users to attach photos to their responses? (True/False).')),
                ('url', models.URLField(blank=True, help_text='Optional URL that wll be displayed to user for this mission. (The entire mission can consist of user going to that URL and performing some action there. For security reasons, this URL must be within a MoveLab domain.')),
                ('mission_version', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NotificationContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_html_es', models.TextField(help_text='Expert comment, expanded and allows html, in spanish')),
                ('body_html_ca', models.TextField(blank=True, default=None, help_text='Expert comment, expanded and allows html, in catalan', null=True)),
                ('body_html_en', models.TextField(blank=True, default=None, help_text='Expert comment, expanded and allows html, in english', null=True)),
                ('title_es', models.TextField(help_text='Title of the comment, shown in non-detail view, in spanish')),
                ('title_ca', models.TextField(blank=True, default=None, help_text='Title of the comment, shown in non-detail view, in catalan', null=True)),
                ('title_en', models.TextField(blank=True, default=None, help_text='Title of the comment, shown in non-detail view, in english', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('version_UUID', models.CharField(help_text='UUID randomly generated on phone to identify each unique report version. Must be exactly 36 characters (32 hex digits plus 4 hyphens).', max_length=36, primary_key=True, serialize=False)),
                ('version_number', models.IntegerField(db_index=True, help_text='The report version number. Should be an integer that increments by 1 for each repor version. Note that the user keeps only the most recent version on the device, but all versions are stored on the server.')),
                ('report_id', models.CharField(db_index=True, help_text='4-digit alpha-numeric code generated on user phone to identify each unique report from that user. Digits should lbe randomly drawn from the set of all lowercase and uppercase alphabetic characters and 0-9, but excluding 0, o, and O to avoid confusion if we ever need user to be able to refer to a report ID in correspondence with MoveLab (as was previously the case when we had them sending samples).', max_length=4)),
                ('server_upload_time', models.DateTimeField(auto_now_add=True, help_text='Date and time on server when report uploaded. (Automatically generated by server.)')),
                ('phone_upload_time', models.DateTimeField(help_text='Date and time on phone when it uploaded fix. Format as ECMA 262 date time string (e.g. "2014-05-17T12:34:56.123+01:00".')),
                ('creation_time', models.DateTimeField(help_text='Date and time on phone when first version of report was created. Format as ECMA 262 date time string (e.g. "2014-05-17T12:34:56.123+01:00".')),
                ('version_time', models.DateTimeField(help_text='Date and time on phone when this version of report was created. Format as ECMA 262 date time string (e.g. "2014-05-17T12:34:56.123+01:00".')),
                ('type', models.CharField(choices=[('adult', 'Adult'), ('site', 'Breeding Site'), ('mission', 'Mission')], help_text="Type of report: 'adult', 'site', or 'mission'.", max_length=7)),
                ('location_choice', models.CharField(choices=[('current', "Current location detected by user's device"), ('selected', 'Location selected by user from map'), ('missing', 'No location choice submitted - should be used only for missions')], help_text='Did user indicate that report relates to current location of phone ("current") or to a location selected manually on the map ("selected")? Or is the choice missing ("missing")', max_length=8)),
                ('current_location_lon', models.FloatField(blank=True, help_text="Longitude of user's current location. In decimal degrees.", null=True)),
                ('current_location_lat', models.FloatField(blank=True, help_text="Latitude of user's current location. In decimal degrees.", null=True)),
                ('selected_location_lon', models.FloatField(blank=True, help_text='Latitude of location selected by user on map. In decimal degrees.', null=True)),
                ('selected_location_lat', models.FloatField(blank=True, help_text='Longitude of location selected by user on map. In decimal degrees.', null=True)),
                ('note', models.TextField(blank=True, help_text='Note user attached to report.')),
                ('package_name', models.CharField(blank=True, db_index=True, help_text='Name of tigatrapp package from which this report was submitted.', max_length=400)),
                ('package_version', models.IntegerField(blank=True, db_index=True, help_text='Version number of tigatrapp package from which this report was submitted.', null=True)),
                ('device_manufacturer', models.CharField(blank=True, help_text='Manufacturer of device from which this report was submitted.', max_length=200)),
                ('device_model', models.CharField(blank=True, help_text='Model of device from which this report was submitted.', max_length=200)),
                ('os', models.CharField(blank=True, help_text='Operating system of device from which this report was submitted.', max_length=200)),
                ('os_version', models.CharField(blank=True, help_text='Operating system version of device from which this report was submitted.', max_length=200)),
                ('os_language', models.CharField(blank=True, help_text='Language setting of operating system on device from which this report was submitted. 2-digit ISO-639-1 language code.', max_length=10)),
                ('app_language', models.CharField(blank=True, help_text='Language setting, within tigatrapp, of device from which this report was submitted. 2-digit ISO-639-1 language code.', max_length=10)),
                ('hide', models.BooleanField(default=False, help_text='Hide this report from public views?')),
                ('cached_visible', models.IntegerField(blank=True, help_text='Precalculated value of show_on_map_function', null=True)),
                ('point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tigaserver_app.EuropeCountry')),
                ('mission', models.ForeignKey(blank=True, help_text='If this report was a response to a mission, the unique id field of that mission.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tigaserver_app.Mission')),
            ],
        ),
        migrations.CreateModel(
            name='TigaProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firebase_token', models.TextField(blank=True, help_text='Firebase token supplied by firebase, suuplied by an registration service (Google, Facebook,etc)', null=True, unique=True, verbose_name='Firebase token associated with the profile')),
                ('score', models.IntegerField(default=0, help_text='Score associated with profile. This is the score associated with the account')),
            ],
        ),
        migrations.CreateModel(
            name='TigaUser',
            fields=[
                ('user_UUID', models.CharField(help_text='UUID randomly generated on phone to identify each unique user. Must be exactly 36 characters (32 hex digits plus 4 hyphens).', max_length=36, primary_key=True, serialize=False)),
                ('registration_time', models.DateTimeField(auto_now_add=True, help_text='The date and time when user registered and consented to sharing data. Automatically set by server when user uploads registration.')),
                ('device_token', models.TextField(blank=True, help_text='Device token, used in messaging. Must be supplied by the client', null=True, verbose_name='Url to picture that originated the comment')),
                ('score', models.IntegerField(default=0, help_text='Score associated with user. This field is used only if the user does not have a profile')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='profile_devices', to='tigaserver_app.TigaProfile')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'ordering': ('user_UUID',),
            },
        ),
        migrations.CreateModel(
            name='ReportResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(help_text='Question that the user responded to.', max_length=1000)),
                ('answer', models.CharField(help_text='Answer that user selected.', max_length=1000)),
                ('report', models.ForeignKey(help_text='Report to which this response is associated.', on_delete=django.db.models.deletion.DO_NOTHING, related_name='responses', to='tigaserver_app.Report')),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='user',
            field=models.ForeignKey(help_text='user_UUID for the user sending this report. Must be exactly 36 characters (32 hex digits plus 4 hyphens) and user must have already registered this ID.', on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_reports', to='tigaserver_app.TigaUser'),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(help_text='Photo uploaded by user.', upload_to=tigaserver_app.models.MakeImageUUID('tigapics'))),
                ('hide', models.BooleanField(default=False, help_text='Hide this photo from public views?')),
                ('uuid', models.CharField(default=tigaserver_app.models.make_uuid, max_length=36)),
                ('report', models.ForeignKey(help_text='Report and version to which this photo is associated (36-digit report_UUID).', on_delete=django.db.models.deletion.DO_NOTHING, related_name='photos', to='tigaserver_app.Report')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_comment', models.DateTimeField(auto_now_add=True)),
                ('expert_comment', models.TextField(help_text='Text message sent to user', verbose_name='Expert comment')),
                ('expert_html', models.TextField(help_text='Expanded message information goes here. This field can contain HTML', verbose_name='Expert comment, expanded and allows html')),
                ('photo_url', models.TextField(blank=True, help_text='Relative url to the public report photo', null=True, verbose_name='Url to picture that originated the comment')),
                ('acknowledged', models.BooleanField(default=False, help_text='This is set to True through the public API, when the user signals that the message has been received')),
                ('public', models.BooleanField(default=False, help_text='Whether the notification is shown in the public map or not')),
                ('expert', models.ForeignKey(blank=True, help_text='Expert sending the notification', on_delete=django.db.models.deletion.DO_NOTHING, related_name='expert_notifications', to=settings.AUTH_USER_MODEL)),
                ('notification_content', models.ForeignKey(blank=True, help_text='Multi language content of the notification', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='notification_content', to='tigaserver_app.NotificationContent')),
                ('report', models.ForeignKey(blank=True, help_text='Report regarding the current notification', on_delete=django.db.models.deletion.DO_NOTHING, related_name='report_notifications', to='tigaserver_app.Report')),
                ('user', models.ForeignKey(help_text='User to which the notification will be sent', on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_notifications', to='tigaserver_app.TigaUser')),
            ],
        ),
        migrations.CreateModel(
            name='MissionTrigger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat_lower_bound', models.FloatField(blank=True, help_text='Optional lower-bound latitude for triggering mission to appear to user. Given in decimal degrees.', null=True)),
                ('lat_upper_bound', models.FloatField(blank=True, help_text='Optional upper-bound latitude for triggering mission to appear to user. Given in decimal degrees.', null=True)),
                ('lon_lower_bound', models.FloatField(blank=True, help_text='Optional lower-bound longitude for triggering mission to appear to user. Given in decimal degrees.', null=True)),
                ('lon_upper_bound', models.FloatField(blank=True, help_text='Optional upper-bound longitude for triggering mission to appear to user. Given in decimal degrees.', null=True)),
                ('time_lowerbound', models.TimeField(blank=True, help_text='Lower bound of optional time-of-day window for triggering mission. If location trigger also is specified, mission will be triggered only if user is found in that location within the window; if location is not specified, the mission will be triggered for all users who have their phones on during the time window. Given as time without date, formatted as ISO 8601 time string (e.g. "12:34:00") with no time zone specified (trigger is always based on local time zone of user.)', null=True)),
                ('time_upperbound', models.TimeField(blank=True, help_text='Lower bound of optional time-of-day window for triggering mission. If location trigger also is specified, mission will be triggered only if user is found in that location within the window; if location is not specified, the mission will be triggered for all users who have their phones on during the time window. Given as time without date, formatted as ISO 8601 time string (e.g. "12:34:00") with no time zone specified (trigger is always based on local time zone of user.)', null=True)),
                ('mission', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='triggers', to='tigaserver_app.Mission')),
            ],
        ),
        migrations.CreateModel(
            name='MissionItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_catalan', models.CharField(help_text='Question displayed to user in Catalan.', max_length=1000)),
                ('question_spanish', models.CharField(help_text='Question displayed to user in Spanish.', max_length=1000)),
                ('question_english', models.CharField(help_text='Question displayed to user in English.', max_length=1000)),
                ('answer_choices_catalan', models.CharField(help_text='Response choices in Catalan, wrapped in quotes, comma separated and in square brackets (e.g., ["yes", "no"]).', max_length=1000)),
                ('answer_choices_spanish', models.CharField(help_text='Response choices in Catalan, wrapped in quotes, comma separated and in square brackets (e.g., ["yes", "no"]).', max_length=1000)),
                ('answer_choices_english', models.CharField(help_text='Response choices in Catalan, wrapped in quotes, comma separated and in square brackets (e.g., ["yes", "no"]).', max_length=1000)),
                ('help_text_catalan', models.TextField(blank=True, help_text='Catalan help text displayed to user for this item.')),
                ('help_text_spanish', models.TextField(blank=True, help_text='Spanish help text displayed to user for this item.')),
                ('help_text_english', models.TextField(blank=True, help_text='English help text displayed to user for this item.')),
                ('prepositioned_image_reference', models.IntegerField(blank=True, help_text='Optional image displayed to user within the help message. Integer reference to image prepositioned on device.', null=True)),
                ('attached_image', models.ImageField(blank=True, help_text='Optional Image displayed to user within the help message. File.', null=True, upload_to='tigaserver_mission_images')),
                ('mission', models.ForeignKey(help_text='Mission to which this item is associated.', on_delete=django.db.models.deletion.DO_NOTHING, related_name='items', to='tigaserver_app.Mission')),
            ],
        ),
        migrations.CreateModel(
            name='CoverageAreaMonth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('n_fixes', models.PositiveIntegerField()),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('latest_report_server_upload_time', models.DateTimeField()),
                ('latest_fix_id', models.PositiveIntegerField()),
            ],
            options={
                'unique_together': {('lat', 'lon', 'year', 'month')},
            },
        ),
        migrations.CreateModel(
            name='CoverageArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('n_fixes', models.PositiveIntegerField()),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('latest_report_server_upload_time', models.DateTimeField()),
                ('latest_fix_id', models.PositiveIntegerField()),
            ],
            options={
                'unique_together': {('lat', 'lon')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='report',
            unique_together={('user', 'version_UUID')},
        ),
    ]
