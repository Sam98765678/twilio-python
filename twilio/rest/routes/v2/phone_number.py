"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Routes
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



class PhoneNumberList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the PhoneNumberList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.routes.v2.phone_number.PhoneNumberList
        :rtype: twilio.rest.routes.v2.phone_number.PhoneNumberList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        
        
        
    
    

    def get(self, phone_number):
        """
        Constructs a PhoneNumberContext
        
        :param phone_number: The phone number in E.164 format
        
        :returns: twilio.rest.routes.v2.phone_number.PhoneNumberContext
        :rtype: twilio.rest.routes.v2.phone_number.PhoneNumberContext
        """
        return PhoneNumberContext(self._version, phone_number=phone_number)

    def __call__(self, phone_number):
        """
        Constructs a PhoneNumberContext
        
        :param phone_number: The phone number in E.164 format
        
        :returns: twilio.rest.routes.v2.phone_number.PhoneNumberContext
        :rtype: twilio.rest.routes.v2.phone_number.PhoneNumberContext
        """
        return PhoneNumberContext(self._version, phone_number=phone_number)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Routes.V2.PhoneNumberList>'


class PhoneNumberContext(InstanceContext):
    def __init__(self, version: Version, phone_number: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'phone_number': phone_number,  }
        self._uri = '/PhoneNumbers/${phone_number}'
        
    
    def fetch(self):
        
        """
        Fetch the PhoneNumberInstance

        :returns: The fetched PhoneNumberInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return PhoneNumberInstance(self._version, payload, phone_number=self._solution['phone_number'], )
        

        
    
    def update(self, voice_region, friendly_name):
        data = values.of({
            'voice_region': voice_region,'friendly_name': friendly_name,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return PhoneNumberInstance(self._version, payload, phone_number=self._solution['phone_number'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Routes.V2.PhoneNumberContext>'



class PhoneNumberInstance(InstanceResource):
    def __init__(self, version, payload, phone_number: str):
        super().__init__(version)
        self._properties = { 
            'phone_number' : payload.get('phone_number'),
            'url' : payload.get('url'),
            'sid' : payload.get('sid'),
            'account_sid' : payload.get('account_sid'),
            'friendly_name' : payload.get('friendly_name'),
            'voice_region' : payload.get('voice_region'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
        }

        self._context = None
        self._solution = {
            'phone_number': phone_number or self._properties['phone_number'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = PhoneNumberContext(
                self._version,
                phone_number=self._solution['phone_number'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Routes.V2.PhoneNumberInstance {}>'.format(context)


