
import subprocess
import os

from base_test import BaseTest

# we reuse a bit of pytest's own testing machinery, this should eventually come
# from a separatedly installable pytest-cli plugin.
pytest_plugins = ['pytester']


class TestKeyCurrent(BaseTest):

    expected_response = {'api_key': '111', 'auth_level': 100, 'auth_level_name': 'default'}

    def get_action_name(self):
        return 'key_get_current'

    def init_request_scenario(self):
        os.environ['TEST_SCENARIO'] = 'key.key_current'

    def test_base_query(self, run_command):
        self.init_request_scenario()

        run_command(self.get_action_name())
        self.see_response(self.expected_response)

    def test_verbose_query(self, run_command):
        self.init_request_scenario()

        run_command(self.get_action_name(), '-v')
        self.see_headers()
        self.see_sent_params('GET', {})
        self.see_response(self.expected_response)