# This is to publish data to splunk through Python. This is still in the works

import logging
from splunk_hec_handler import SplunkHecHandler
logger = logging.getLogger('SplunkHecHandlerExample')
logger.setLevel(logging.DEBUG)

# If using self-signed certificate, set ssl_verify to False
# If using http, set proto to http
splunk_handler = SplunkHecHandler('splunkfw.domain.tld',
                    '697c573a-9371-4c71-a036-cb9998803a66',
                    port=8088, proto='http', ssl_verify=False,
                    source="HEC_example")
logger.addHandler(splunk_handler)