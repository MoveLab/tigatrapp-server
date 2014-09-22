from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import mixins
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings


from serializers import UserSerializer, ReportSerializer, MissionSerializer, PhotoSerializer, FixSerializer, \
    ConfigurationSerializer
from models import TigaUser, Mission, Report, Photo, \
    Fix, Configuration


class ReadOnlyModelViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    A viewset that provides `retrieve`, and 'list` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """
    pass


class WriteOnlyModelViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    A viewset that provides`create` action.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """
    pass


class ReadWriteOnlyModelViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    A viewset that provides `retrieve`, 'list`, and `create` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """
    pass


@api_view(['GET'])
def get_current_configuration(request):
    """
API endpoint for getting most recent app configuration created by Movelab.

**Fields**

* id: Auto-incremented primary key record ID.
* samples_per_day: Number of randomly-timed location samples to take per day.
* creation_time: Date and time when this configuration was created by MoveLab. Automatically generated when
record is saved.
    """
    if request.method == 'GET':
        current_config = Configuration.objects.order_by('creation_time').last()
        serializer = ConfigurationSerializer(current_config)
        return Response(serializer.data)


@api_view(['GET'])
def get_new_missions(request):
    """
API endpoint for getting most missions that have not yet been downloaded.

**Fields**

* id: Unique identifier of the mission. Automatically generated by server when mission created.
* title_catalan: Title of mission in Catalan.
* title_spanish: Title of mission in Spanish.
* title_english: Title of mission in English.
* short_description_catalan: Catalan text to be displayed in mission list.
* short_description_spanish: Spanish text to be displayed in mission list.
* short_description_english: English text to be displayed in mission list.
* long_description_catalan: Catalan text that fully explains mission to user.
* long_description_spanish: Spanish text that fully explains mission to user.
* long_description_english: English text that fully explains mission to user.
* help_text_catalan: Catalan text to be displayed when user taps mission help button.
* help_text_spanish: Spanish text to be displayed when user taps mission help button.
* help_text_english: English text to be displayed when user taps mission help button.
* platform: What type of device is this mission is intended for? It will be sent only to these devices.
* creation_time: Date and time mission was created by MoveLab. Automatically generated when mission saved.
* expiration_time: Optional date and time when mission should expire (if ever). Mission will no longer be displayed to users after this date-time.
* photo_mission: Should this mission allow users to attach photos to their responses? (True/False).
* url: Optional URL that wll be displayed to user for this mission. (The entire mission can consist of user going to that URL and performing some action there. For security reasons, this URL must be within a MoveLab domain.
* mission_version: Optional integer that can be used to ensure that new mission parameters that we may create in the
future do not cause problems on older versions of the app. The Android app is currently set to respond only to
missions with mission_version=1 or null.
* triggers:
    * lat_lower_bound:Optional lower-bound latitude for triggering mission to appear to user. Given in decimal degrees.
    * lat_upper_bound: Optional upper-bound latitude for triggering mission to appear to user. Given in decimal degrees.
    * lon_lower_bound: Optional lower-bound longitude for triggering mission to appear to user. Given in decimal
    degrees.
    * lon_upper_bound: Optional upper-bound longitude for triggering mission to appear to user. Given in decimal degrees.
    * time_lowerbound: Lower bound of optional time-of-day window for triggering mission. If location trigger also is specified, mission will be triggered only if user is found in that location within the window; if location is not specified, the mission will be triggered for all users who have their phones on during the time window. Given as time without date, formatted as [ISO 8601](http://www.w3.org/TR/NOTE-datetime) time string (e.g. "12:34:00") with no time zone specified (trigger is always based on local time zone of user.)
    * time_upperbound: Lower bound of optional time-of-day window for triggering mission. If location trigger also is specified, mission will be triggered only if user is found in that location within the window; if location is not specified, the mission will be triggered for all users who have their phones on during the time window. Given as time without date, formatted as [ISO 8601](http://www.w3.org/TR/NOTE-datetime) time string (e.g. "12:34:00") with no time zone specified (trigger is always based on local time zone of user.)
* items:
    * question_catalan: Question displayed to user in Catalan.
    * question_spanish: Question displayed to user in Spanish.
    * question_english: Question displayed to user in English.
    * answer_choices_catalan: Response choices, with each choice surrounded by square brackets (e.g. _[Yes][No]_).
    * answer_choices_spanish: Response choices, with each choice surrounded by square brackets (e.g. _[Yes][No]_).
    * answer_choices_english: Response choices, with each choice surrounded by square brackets (e.g. _[Yes][No]_).
    * help_text_catalan: Help text displayed to user for this item.
    * help_text_spanish: Help text displayed to user for this item.
    * help_text_english: Help text displayed to user for this item.
    * prepositioned_image_reference: Optional image displayed to user within the help message. Integer reference to image prepositioned on device.')
    * attached_image: Optional Image displayed to user within the help message. File.

**Query Parameters**

* id_gt: Returns records with id greater than the specified value. Use this for getting only those missions that have not yet been downloaded. Default is 0.
* platform: Returns records matching exactly the platform code or those with 'all' or null. Default is 'all'.
* version_lte: returns records with mission_version less than or equal to the value specified or those with
mission_version null. Defaults to 100.
    """
    if request.method == 'GET':
        these_missions = Mission.objects.filter(Q(id__gt=request.QUERY_PARAMS.get('id_gt', 0)),
                                                Q(platform__exact=request.QUERY_PARAMS.get('platform', 'all')) | Q(
                                                    platform__isnull=True) | Q(platform__exact='all'),
                                                Q(mission_version__lte=request.QUERY_PARAMS.get(
                                                    'version_lte',
                                                                                               100)) | Q(mission_version__isnull=True))
        serializer = MissionSerializer(these_missions)
        return Response(serializer.data)



@api_view(['POST'])
def post_photo(request):
    """
API endpoint for uploading photos associated with a report. Data must be posted as multipart form,
with with _photo_ used as the form key for the file itself, and _report_ used as the key for the report
version_UUID linking this photo to a specific report version.

**Fields**

* photo: The photo's binary image data
* report: The version_UUID of the report to which this photo is attached.
    """
    if request.method == 'POST':
        this_report = Report.objects.get(version_UUID=request.DATA['report'])
        instance = Photo(photo=request.FILES['photo'], report=this_report)
        instance.save()
        return Response('uploaded')


# For production version, substitute WriteOnlyModelViewSet
class UserViewSet(ReadWriteOnlyModelViewSet):
    """
API endpoint for getting and posting user registration. The only information required is a 36 digit UUID generated on
user's
device. (Registration time is also added by server automatically and included in the database, but is not accessible
through the API.)

**Fields**

* user_UUID: UUID randomly generated on phone to identify each unique user. Must be exactly 36 characters (32 hex digits plus 4 hyphens).
    """
    queryset = TigaUser.objects.all()
    serializer_class = UserSerializer


class CustomBrowsableAPIRenderer(BrowsableAPIRenderer):
    def get_default_renderer(self, view):
        return JSONRenderer()


# For production version, substitute WriteOnlyModelViewSet
class ReportViewSet(ReadWriteOnlyModelViewSet):
    """
API endpoint for getting and posting new reports and report versions. (Every time a user edits a report,
a new version is
posted; user keeps only most recent version on phone but server retains all versions.) Note that photos attached to the
report must be uploaded separately through the [photo](/api/photos/) endpoint. (Also note that the HTML form, below,
for testing posts does not work for including responses in posted reports; use the raw/JSON format instead.)

**Fields**

* version_UUID: UUID randomly generated on phone to identify each unique report version. Must be exactly 36 characters (32 hex digits plus 4 hyphens).
* version_number: The report version number. Should be an integer that increments by 1 for each repor version. Note
that the user keeps only the most recent version on the device, but all versions are stored on the server. To
delete a report, submit a version with version_number = -1. This will cause the report to no longer be displated on
the server map (although it will still be retained internally).
* user: user_UUID for the user sending this report. Must be exactly 36 characters (32 hex digits plus 4 hyphens) and user must have already registered this ID.
* report_id: 4-digit alpha-numeric code generated on user phone to identify each unique report from that user. Digits should lbe randomly drawn from the set of all lowercase and uppercase alphabetic characters and 0-9, but excluding 0, o, and O to avoid confusion if we ever need user to be able to refer to a report ID in correspondence with MoveLab (as was previously the case when we had them sending samples).
* phone_upload_time: Date and time on phone when it uploaded fix. Format as [ECMA 262](http://ecma-international.org/ecma-262/5.1/#sec-15.9.1.15) date time string (e.g. "2014-05-17T12:34:56.123+01:00".
* creation_time:Date and time on phone when first version of report was created. Format as [ECMA 262](http://ecma-international.org/ecma-262/5.1/#sec-15.9.1.15) date time string
(e.g. "2014-05-17T12:34:56.123+01:00".
* version_time:Date and time on phone when this version of report was created. Format as [ECMA 262](http://ecma-international.org/ecma-262/5.1/#sec-15.9.1.15) date time string (e
.g. "2014-05-17T12:34:56.123+01:00".
* type: Type of report: 'adult', 'site', or 'mission'.
* mission: If this report was a response to a mission, the unique id field of that mission.
* location_choice: Did user indicate that report relates to current location of phone ("current") or to a location selected manually on the map ("selected")?
* current_location_lon: Longitude of user's current location. In decimal degrees.
* current_location_lat: Latitude of user's current location. In decimal degrees.
* selected_location_lon: Latitude of location selected by user on map. In decimal degrees.
* selected_location_lat: Longitude of location selected by user on map. In decimal degrees.
* note: Note user attached to report.
* package_name: Name of tigatrapp package from which this report was submitted.
* package_version: Version number of tigatrapp package from which this report was submitted.
* device_manufacturer: Manufacturer of device from which this report was submitted.
* device_model: Model of device from which this report was submitted.
* os:  Operating system of device from which this report was submitted.
* os_version: Operating system version of device from which this report was submitted.
* os_language: Language setting of operating system on device from which this report was submitted. 2-digit [ISO 639-1](http://www.iso.org/iso/home/standards/language_codes.htm) language code.
* app_language:Language setting, within tigatrapp, of device from which this report was submitted. 2-digit [ISO 639-1](http://www.iso.org/iso/home/standards/language_codes.htm) language code.
* responses:
    * question: Question that the user responded to.
    * answer: Answer that user selected.

**Query Parameters**

* user_UUID: The user_UUID for a particular user.
* version_number: The report version number.
* report_id: The 4-digit report ID.
* type: The report type (adult, site, or mission).
    """
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    filter_fields = ('user', 'version_number', 'report_id', 'type')


class MissionViewSet(ReadOnlyModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer


# For production version, substitute WriteOnlyModelViewSet
class PhotoViewSet(ReadWriteOnlyModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


# For production version, substitute WriteOnlyModelViewSet
class FixViewSet(ReadWriteOnlyModelViewSet):
    """
API endpoint for getting and posting masked location fixes.

**Fields**

* user: The 36-digit user_UUID for the user sending this location fix.
* fix_time: Date and time when fix was recorded on phone. Format as [ECMA 262](http://ecma-international.org/ecma-262/5.1/#sec-15.9.1.15) date time string (e.g. "2014-05-17T12:34:56'
                                              '.123+01:00".
* server_upload_time: Date and time registered by server when it received fix upload. Automatically generated by server.'
* phone_upload_time: Date and time on phone when it uploaded fix. Format as [ECMA 262](http://ecma-international.org/ecma-262/5.1/#sec-15.9.1.15) date time string (e.g. "2014-05-17T12:34:56.123+01:00".
* masked_lon: Longitude rounded down to nearest 0.05 decimal degree (floor(lon/.05)*.05).
* masked_lat: Latitude rounded down to nearest 0.05 decimal degree (floor(lat/.05)*.05).
* power: Power level of phone at time fix recorded, expressed as proportion of full charge. Range: 0-1.

**Query Parameters**

* user_UUID: The UUID of the user sending this fix.
    """
    queryset = Fix.objects.all()
    serializer_class = FixSerializer
    filter_fields = ('user_coverage_uuid', )


class ConfigurationViewSet(ReadOnlyModelViewSet):
    """
API endpoint for downloading app configurations created by Movelab. Only the most recent configuration is downloaded.

**Fields**

* id: Auto-incremented primary key record ID.
* samples_per_day: Number of randomly-timed location samples to take per day.
* creation_time: Date and time when this configuration was created by MoveLab. Automatically generated when
record is saved.
    """
    queryset = Configuration.objects.all()
    serializer_class = ConfigurationSerializer


def lookup_photo(request, token, photo_uuid, size):
    if token == settings.PHOTO_SECRET_KEY: # and request.get_host() in 'crowdcrafting.org':
        this_photo = Photo.objects.get(uuid=photo_uuid)
        if size == 'small':
            url = this_photo.get_small_url()
        elif size == 'medium':
            url = this_photo.get_medium_url()
        else:
            url = this_photo.photo.url
        return HttpResponseRedirect(url)