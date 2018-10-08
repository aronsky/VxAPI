# content of test_pyconv.py

import subprocess
import os

from base_test import BaseTest

# we reuse a bit of pytest's own testing machinery, this should eventually come
# from a separatedly installable pytest-cli plugin.
pytest_plugins = ["pytester"]


class TestReportDroppedFiles(BaseTest):

    expected_hash = '8b585baa0b8f4bea3af85f93eda4c164d3c577b34856e6ca9d923a676e95a8e9'

    def get_action_name(self):
        return 'report_get_dropped_files'

    def init_request_scenario(self):
        os.environ['TEST_SCENARIO'] = 'report.report_dropped_files'

    def test_base_query(self, run_command):
        self.init_request_scenario()

        run_command(self.get_action_name(), 'test')
        print(self.output)
        self.see_file_response('output/report_get_dropped_files-test-archive-file.zip', self.expected_hash)

    def test_verbose_query(self, run_command):
        self.init_request_scenario()

        run_command(self.get_action_name(), 'test', '-v')
        self.see_headers()
        self.see_file_response('output/report_get_dropped_files-test-archive-file.zip', self.expected_hash)