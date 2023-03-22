r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Media
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Optional
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class MediaRecordingInstance(InstanceResource):
    class Format(object):
        MP4 = "mp4"
        WEBM = "webm"

    class Order(object):
        ASC = "asc"
        DESC = "desc"

    class Status(object):
        PROCESSING = "processing"
        COMPLETED = "completed"
        DELETED = "deleted"
        FAILED = "failed"

    def __init__(self, version, payload, sid: Optional[str] = None):
        """
        Initialize the MediaRecordingInstance

        :returns: twilio.rest.media.v1.media_recording.MediaRecordingInstance
        :rtype: twilio.rest.media.v1.media_recording.MediaRecordingInstance
        """
        super().__init__(version)

        self._properties = {
            "account_sid": payload.get("account_sid"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "duration": deserialize.integer(payload.get("duration")),
            "format": payload.get("format"),
            "links": payload.get("links"),
            "processor_sid": payload.get("processor_sid"),
            "resolution": payload.get("resolution"),
            "source_sid": payload.get("source_sid"),
            "sid": payload.get("sid"),
            "media_size": payload.get("media_size"),
            "status": payload.get("status"),
            "status_callback": payload.get("status_callback"),
            "status_callback_method": payload.get("status_callback_method"),
            "url": payload.get("url"),
        }

        self._solution = {
            "sid": sid or self._properties["sid"],
        }
        self._context: Optional[MediaRecordingContext] = None

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: MediaRecordingContext for this MediaRecordingInstance
        :rtype: twilio.rest.media.v1.media_recording.MediaRecordingContext
        """
        if self._context is None:
            self._context = MediaRecordingContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the MediaRecording resource.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties["date_created"]

    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties["date_updated"]

    @property
    def duration(self):
        """
        :returns: The duration of the MediaRecording in seconds.
        :rtype: int
        """
        return self._properties["duration"]

    @property
    def format(self):
        """
        :returns:
        :rtype: MediaRecordingInstance.Format
        """
        return self._properties["format"]

    @property
    def links(self):
        """
        :returns: The URLs of related resources.
        :rtype: dict
        """
        return self._properties["links"]

    @property
    def processor_sid(self):
        """
        :returns: The SID of the MediaProcessor resource which produced the MediaRecording.
        :rtype: str
        """
        return self._properties["processor_sid"]

    @property
    def resolution(self):
        """
        :returns: The dimensions of the video image in pixels expressed as columns (width) and rows (height).
        :rtype: str
        """
        return self._properties["resolution"]

    @property
    def source_sid(self):
        """
        :returns: The SID of the resource that generated the original media track(s) of the MediaRecording.
        :rtype: str
        """
        return self._properties["source_sid"]

    @property
    def sid(self):
        """
        :returns: The unique string generated to identify the MediaRecording resource.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def media_size(self):
        """
        :returns: The size of the recording media in bytes.
        :rtype: int
        """
        return self._properties["media_size"]

    @property
    def status(self):
        """
        :returns:
        :rtype: MediaRecordingInstance.Status
        """
        return self._properties["status"]

    @property
    def status_callback(self):
        """
        :returns: The URL to which Twilio will send asynchronous webhook requests for every MediaRecording event. See [Status Callbacks](/docs/live/status-callbacks) for more details.
        :rtype: str
        """
        return self._properties["status_callback"]

    @property
    def status_callback_method(self):
        """
        :returns: The HTTP method Twilio should use to call the `status_callback` URL. Can be `POST` or `GET` and the default is `POST`.
        :rtype: str
        """
        return self._properties["status_callback_method"]

    @property
    def url(self):
        """
        :returns: The absolute URL of the resource.
        :rtype: str
        """
        return self._properties["url"]

    def delete(self):
        """
        Deletes the MediaRecordingInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the MediaRecordingInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._proxy.delete_async()

    def fetch(self):
        """
        Fetch the MediaRecordingInstance


        :returns: The fetched MediaRecordingInstance
        :rtype: twilio.rest.media.v1.media_recording.MediaRecordingInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the MediaRecordingInstance


        :returns: The fetched MediaRecordingInstance
        :rtype: twilio.rest.media.v1.media_recording.MediaRecordingInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Media.V1.MediaRecordingInstance {}>".format(context)


class MediaRecordingContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the MediaRecordingContext

        :param Version version: Version that contains the resource
        :param sid: The SID of the MediaRecording resource to fetch.

        :returns: twilio.rest.media.v1.media_recording.MediaRecordingContext
        :rtype: twilio.rest.media.v1.media_recording.MediaRecordingContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/MediaRecordings/{sid}".format(**self._solution)

    def delete(self):
        """
        Deletes the MediaRecordingInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the MediaRecordingInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self):
        """
        Fetch the MediaRecordingInstance


        :returns: The fetched MediaRecordingInstance
        :rtype: twilio.rest.media.v1.media_recording.MediaRecordingInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return MediaRecordingInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the MediaRecordingInstance


        :returns: The fetched MediaRecordingInstance
        :rtype: twilio.rest.media.v1.media_recording.MediaRecordingInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return MediaRecordingInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Media.V1.MediaRecordingContext {}>".format(context)


class MediaRecordingPage(Page):
    def get_instance(self, payload):
        """
        Build an instance of MediaRecordingInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.media.v1.media_recording.MediaRecordingInstance
        :rtype: twilio.rest.media.v1.media_recording.MediaRecordingInstance
        """
        return MediaRecordingInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Media.V1.MediaRecordingPage>"


class MediaRecordingList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the MediaRecordingList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.media.v1.media_recording.MediaRecordingList
        :rtype: twilio.rest.media.v1.media_recording.MediaRecordingList
        """
        super().__init__(version)

        self._uri = "/MediaRecordings"

    def stream(
        self,
        order=values.unset,
        status=values.unset,
        processor_sid=values.unset,
        source_sid=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Streams MediaRecordingInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param MediaRecordingInstance.Order order: The sort order of the list by `date_created`. Can be: `asc` (ascending) or `desc` (descending) with `desc` as the default.
        :param MediaRecordingInstance.Status status: Status to filter by, with possible values `processing`, `completed`, `deleted`, or `failed`.
        :param str processor_sid: SID of a MediaProcessor to filter by.
        :param str source_sid: SID of a MediaRecording source to filter by.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.media.v1.media_recording.MediaRecordingInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            order=order,
            status=status,
            processor_sid=processor_sid,
            source_sid=source_sid,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        order=values.unset,
        status=values.unset,
        processor_sid=values.unset,
        source_sid=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Asynchronously streams MediaRecordingInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param MediaRecordingInstance.Order order: The sort order of the list by `date_created`. Can be: `asc` (ascending) or `desc` (descending) with `desc` as the default.
        :param MediaRecordingInstance.Status status: Status to filter by, with possible values `processing`, `completed`, `deleted`, or `failed`.
        :param str processor_sid: SID of a MediaProcessor to filter by.
        :param str source_sid: SID of a MediaRecording source to filter by.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.media.v1.media_recording.MediaRecordingInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            order=order,
            status=status,
            processor_sid=processor_sid,
            source_sid=source_sid,
            page_size=limits["page_size"],
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        order=values.unset,
        status=values.unset,
        processor_sid=values.unset,
        source_sid=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Lists MediaRecordingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param MediaRecordingInstance.Order order: The sort order of the list by `date_created`. Can be: `asc` (ascending) or `desc` (descending) with `desc` as the default.
        :param MediaRecordingInstance.Status status: Status to filter by, with possible values `processing`, `completed`, `deleted`, or `failed`.
        :param str processor_sid: SID of a MediaProcessor to filter by.
        :param str source_sid: SID of a MediaRecording source to filter by.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.media.v1.media_recording.MediaRecordingInstance]
        """
        return list(
            self.stream(
                order=order,
                status=status,
                processor_sid=processor_sid,
                source_sid=source_sid,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        order=values.unset,
        status=values.unset,
        processor_sid=values.unset,
        source_sid=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Asynchronously lists MediaRecordingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param MediaRecordingInstance.Order order: The sort order of the list by `date_created`. Can be: `asc` (ascending) or `desc` (descending) with `desc` as the default.
        :param MediaRecordingInstance.Status status: Status to filter by, with possible values `processing`, `completed`, `deleted`, or `failed`.
        :param str processor_sid: SID of a MediaProcessor to filter by.
        :param str source_sid: SID of a MediaRecording source to filter by.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.media.v1.media_recording.MediaRecordingInstance]
        """
        return list(
            await self.stream_async(
                order=order,
                status=status,
                processor_sid=processor_sid,
                source_sid=source_sid,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        order=values.unset,
        status=values.unset,
        processor_sid=values.unset,
        source_sid=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Retrieve a single page of MediaRecordingInstance records from the API.
        Request is executed immediately

        :param MediaRecordingInstance.Order order: The sort order of the list by `date_created`. Can be: `asc` (ascending) or `desc` (descending) with `desc` as the default.
        :param MediaRecordingInstance.Status status: Status to filter by, with possible values `processing`, `completed`, `deleted`, or `failed`.
        :param str processor_sid: SID of a MediaProcessor to filter by.
        :param str source_sid: SID of a MediaRecording source to filter by.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of MediaRecordingInstance
        :rtype: twilio.rest.media.v1.media_recording.MediaRecordingPage
        """
        data = values.of(
            {
                "Order": order,
                "Status": status,
                "ProcessorSid": processor_sid,
                "SourceSid": source_sid,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return MediaRecordingPage(self._version, response)

    async def page_async(
        self,
        order=values.unset,
        status=values.unset,
        processor_sid=values.unset,
        source_sid=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Asynchronously retrieve a single page of MediaRecordingInstance records from the API.
        Request is executed immediately

        :param MediaRecordingInstance.Order order: The sort order of the list by `date_created`. Can be: `asc` (ascending) or `desc` (descending) with `desc` as the default.
        :param MediaRecordingInstance.Status status: Status to filter by, with possible values `processing`, `completed`, `deleted`, or `failed`.
        :param str processor_sid: SID of a MediaProcessor to filter by.
        :param str source_sid: SID of a MediaRecording source to filter by.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of MediaRecordingInstance
        :rtype: twilio.rest.media.v1.media_recording.MediaRecordingPage
        """
        data = values.of(
            {
                "Order": order,
                "Status": status,
                "ProcessorSid": processor_sid,
                "SourceSid": source_sid,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return MediaRecordingPage(self._version, response)

    def get_page(self, target_url):
        """
        Retrieve a specific page of MediaRecordingInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of MediaRecordingInstance
        :rtype: twilio.rest.media.v1.media_recording.MediaRecordingPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return MediaRecordingPage(self._version, response)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of MediaRecordingInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of MediaRecordingInstance
        :rtype: twilio.rest.media.v1.media_recording.MediaRecordingPage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return MediaRecordingPage(self._version, response)

    def get(self, sid):
        """
        Constructs a MediaRecordingContext

        :param sid: The SID of the MediaRecording resource to fetch.

        :returns: twilio.rest.media.v1.media_recording.MediaRecordingContext
        :rtype: twilio.rest.media.v1.media_recording.MediaRecordingContext
        """
        return MediaRecordingContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a MediaRecordingContext

        :param sid: The SID of the MediaRecording resource to fetch.

        :returns: twilio.rest.media.v1.media_recording.MediaRecordingContext
        :rtype: twilio.rest.media.v1.media_recording.MediaRecordingContext
        """
        return MediaRecordingContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Media.V1.MediaRecordingList>"