import unittest
from client import parse_parameters


class TestClient(unittest.TestCase):

    def test_parse_params_default(self):
        default_port_settings = 7777
        default_host_settings = 'localhost'
        result = parse_parameters(default_host_settings, default_port_settings)
        self.assertEqual(result, ('localhost', 7777))


if __name__ == '__main__':
    unittest.main()
