import unittest
import json
from server import parse_params, form_response, resp_presence, resp_incorrect_request


class TestServer(unittest.TestCase):

    def test_parse_params(self):
        default_port_settings = 7777
        default_addr_settings = ''
        result = parse_params(default_port_settings, default_addr_settings)
        self.assertEqual(result, ('', 7777))

    def test_form_response_presence(self):
        request_presence = {"action": "presence", "time": 1624884233, "type": "status",
                            "user": {"account_name": "client_001", "status": "client_001 present"}}

        resp_presence_encoded = json.dumps(resp_presence).encode('utf-8')

        result_presence = form_response(request_presence)
        self.assertEqual(result_presence, resp_presence_encoded)

    def test_form_response_incorrect(self):
        request_incorrect = {"action": "something", "time": 1624884233, "type": "status",
                             "user": {"account_name": "client_001", "status": "client_001 present"}}

        resp_incorrect_encoded = json.dumps(resp_incorrect_request).encode('utf-8')

        result_incorrect = form_response(request_incorrect)
        self.assertEqual(result_incorrect, resp_incorrect_encoded)


if __name__ == '__main__':
    unittest.main()
