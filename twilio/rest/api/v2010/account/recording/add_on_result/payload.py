"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
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


class PayloadList(ListResource):

    def __init__(self, version: Version, account_sid: str, reference_sid: str, add_on_result_sid: str):
        """
        Initialize the PayloadList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult Payload resources to read.
        :param reference_sid: The SID of the recording to which the AddOnResult resource that contains the payloads to read belongs.
        :param add_on_result_sid: The SID of the AddOnResult to which the payloads to read belongs.
        
        :returns: twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadList
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid, 'reference_sid': reference_sid, 'add_on_result_sid': add_on_result_sid,  }
        self._uri = '/Accounts/${account_sid}/Recordings/${reference_sid}/AddOnResults/${add_on_result_sid}/Payloads.json'.format(**self._solution)
        
        
    
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams PayloadInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists PayloadInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of PayloadInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of PayloadInstance
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return PayloadPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of PayloadInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of PayloadInstance
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return PayloadPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a PayloadContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Recording AddOnResult Payload resource to fetch.
        
        :returns: twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadContext
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadContext
        """
        return PayloadContext(self._version, account_sid=self._solution['account_sid'], reference_sid=self._solution['reference_sid'], add_on_result_sid=self._solution['add_on_result_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a PayloadContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Recording AddOnResult Payload resource to fetch.
        
        :returns: twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadContext
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadContext
        """
        return PayloadContext(self._version, account_sid=self._solution['account_sid'], reference_sid=self._solution['reference_sid'], add_on_result_sid=self._solution['add_on_result_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.PayloadList>'






class PayloadPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the PayloadPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadPage
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of PayloadInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadInstance
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadInstance
        """
        return PayloadInstance(self._version, payload, account_sid=self._solution['account_sid'], reference_sid=self._solution['reference_sid'], add_on_result_sid=self._solution['add_on_result_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.PayloadPage>'





class PayloadContext(InstanceContext):
    def __init__(self, version: Version, account_sid: str, reference_sid: str, add_on_result_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid, 'reference_sid': reference_sid, 'add_on_result_sid': add_on_result_sid, 'sid': sid,  }
        self._uri = '/Accounts/${account_sid}/Recordings/${reference_sid}/AddOnResults/${add_on_result_sid}/Payloads/${sid}.json'
        
    
    def delete(self):
        
        

        """
        Deletes the PayloadInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the PayloadInstance

        :returns: The fetched PayloadInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return PayloadInstance(self._version, payload, account_sid=self._solution['account_sid'], reference_sid=self._solution['reference_sid'], add_on_result_sid=self._solution['add_on_result_sid'], sid=self._solution['sid'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.PayloadContext>'



class PayloadInstance(InstanceResource):
    def __init__(self, version, payload, account_sid: str, reference_sid: str, add_on_result_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'add_on_result_sid' : payload.get('add_on_result_sid'),
            'account_sid' : payload.get('account_sid'),
            'label' : payload.get('label'),
            'add_on_sid' : payload.get('add_on_sid'),
            'add_on_configuration_sid' : payload.get('add_on_configuration_sid'),
            'content_type' : payload.get('content_type'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'reference_sid' : payload.get('reference_sid'),
            'subresource_uris' : payload.get('subresource_uris'),
        }

        self._context = None
        self._solution = {
            'account_sid': account_sid or self._properties['account_sid'],'reference_sid': reference_sid or self._properties['reference_sid'],'add_on_result_sid': add_on_result_sid or self._properties['add_on_result_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = PayloadContext(
                self._version,
                account_sid=self._solution['account_sid'],reference_sid=self._solution['reference_sid'],add_on_result_sid=self._solution['add_on_result_sid'],sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.PayloadInstance {}>'.format(context)


