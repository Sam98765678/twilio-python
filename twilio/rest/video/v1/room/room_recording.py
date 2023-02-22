"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Video
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class RoomRecordingList(ListResource):

    def __init__(self, version: Version, room_sid: str):
        """
        Initialize the RoomRecordingList

        :param Version version: Version that contains the resource
        :param room_sid: The SID of the room with the RoomRecording resources to read.
        
        :returns: twilio.rest.video.v1.room.room_recording.RoomRecordingList
        :rtype: twilio.rest.video.v1.room.room_recording.RoomRecordingList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'room_sid': room_sid,  }
        self._uri = '/Rooms/${room_sid}/Recordings'.format(**self._solution)
        
        
    
    
    
    def stream(self, status=values.unset, source_sid=values.unset, date_created_after=values.unset, date_created_before=values.unset, limit=None, page_size=None):
        """
        Streams RoomRecordingInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param RoomRecordingStatus status: Read only the recordings with this status. Can be: `processing`, `completed`, or `deleted`.
        :param str source_sid: Read only the recordings that have this `source_sid`.
        :param datetime date_created_after: Read only recordings that started on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone.
        :param datetime date_created_before: Read only Recordings that started before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.video.v1.room.room_recording.RoomRecordingInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            status=status,
            source_sid=source_sid,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, status=values.unset, source_sid=values.unset, date_created_after=values.unset, date_created_before=values.unset, limit=None, page_size=None):
        """
        Lists RoomRecordingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param RoomRecordingStatus status: Read only the recordings with this status. Can be: `processing`, `completed`, or `deleted`.
        :param str source_sid: Read only the recordings that have this `source_sid`.
        :param datetime date_created_after: Read only recordings that started on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone.
        :param datetime date_created_before: Read only Recordings that started before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.video.v1.room.room_recording.RoomRecordingInstance]
        """
        return list(self.stream(
            status=status,
            source_sid=source_sid,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, status=values.unset, source_sid=values.unset, date_created_after=values.unset, date_created_before=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of RoomRecordingInstance records from the API.
        Request is executed immediately
        
        :param RoomRecordingStatus status: Read only the recordings with this status. Can be: `processing`, `completed`, or `deleted`.
        :param str source_sid: Read only the recordings that have this `source_sid`.
        :param datetime date_created_after: Read only recordings that started on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone.
        :param datetime date_created_before: Read only Recordings that started before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of RoomRecordingInstance
        :rtype: twilio.rest.video.v1.room.room_recording.RoomRecordingPage
        """
        data = values.of({ 
            'Status': status,
            'SourceSid': source_sid,
            'DateCreatedAfter': serialize.iso8601_datetime(date_created_after),
            'DateCreatedBefore': serialize.iso8601_datetime(date_created_before),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return RoomRecordingPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of RoomRecordingInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of RoomRecordingInstance
        :rtype: twilio.rest.video.v1.room.room_recording.RoomRecordingPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return RoomRecordingPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a RoomRecordingContext
        
        :param sid: The SID of the RoomRecording resource to fetch.
        
        :returns: twilio.rest.video.v1.room.room_recording.RoomRecordingContext
        :rtype: twilio.rest.video.v1.room.room_recording.RoomRecordingContext
        """
        return RoomRecordingContext(self._version, room_sid=self._solution['room_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a RoomRecordingContext
        
        :param sid: The SID of the RoomRecording resource to fetch.
        
        :returns: twilio.rest.video.v1.room.room_recording.RoomRecordingContext
        :rtype: twilio.rest.video.v1.room.room_recording.RoomRecordingContext
        """
        return RoomRecordingContext(self._version, room_sid=self._solution['room_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.RoomRecordingList>'






class RoomRecordingPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the RoomRecordingPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.video.v1.room.room_recording.RoomRecordingPage
        :rtype: twilio.rest.video.v1.room.room_recording.RoomRecordingPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of RoomRecordingInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.video.v1.room.room_recording.RoomRecordingInstance
        :rtype: twilio.rest.video.v1.room.room_recording.RoomRecordingInstance
        """
        return RoomRecordingInstance(self._version, payload, room_sid=self._solution['room_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.RoomRecordingPage>'





class RoomRecordingContext(InstanceContext):
    def __init__(self, version: Version, room_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'room_sid': room_sid, 'sid': sid,  }
        self._uri = '/Rooms/${room_sid}/Recordings/${sid}'
        
    
    def delete(self):
        
        

        """
        Deletes the RoomRecordingInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the RoomRecordingInstance

        :returns: The fetched RoomRecordingInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return RoomRecordingInstance(self._version, payload, room_sid=self._solution['room_sid'], sid=self._solution['sid'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.RoomRecordingContext>'



class RoomRecordingInstance(InstanceResource):
    def __init__(self, version, payload, room_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'status' : payload.get('status'),
            'date_created' : payload.get('date_created'),
            'sid' : payload.get('sid'),
            'source_sid' : payload.get('source_sid'),
            'size' : payload.get('size'),
            'url' : payload.get('url'),
            'type' : payload.get('type'),
            'duration' : payload.get('duration'),
            'container_format' : payload.get('container_format'),
            'codec' : payload.get('codec'),
            'grouping_sids' : payload.get('grouping_sids'),
            'track_name' : payload.get('track_name'),
            'offset' : payload.get('offset'),
            'media_external_location' : payload.get('media_external_location'),
            'room_sid' : payload.get('room_sid'),
            'links' : payload.get('links'),
        }

        self._context = None
        self._solution = {
            'room_sid': room_sid or self._properties['room_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = RoomRecordingContext(
                self._version,
                room_sid=self._solution['room_sid'],sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Video.V1.RoomRecordingInstance {}>'.format(context)


