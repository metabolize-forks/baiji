import unittest
import os

from test.test_support import EnvironmentVarGuard

class TestAWS(unittest.TestCase):

    def test_settings_set_aws_keys_and_default_region(self):
        from baiji.config import settings
        from baiji.util import yaml
        bodylabs_file_path = os.getenv('BODYLABS_CREDENTIAL_FILE', os.path.expanduser('~/.bodylabs'))
        if not os.path.exists(bodylabs_file_path):
            raise unittest.SkipTest("Skipping test_credentials because ~/.bodylabs doesn't exist.")
        truth = yaml.load(bodylabs_file_path)
        if 'AWS_ACCESS_KEY' not in truth or 'AWS_SECRET' not in truth:
            raise unittest.SkipTest("Skipping test_credentials because ~/.bodylabs doesn't contain credentials.")
        self.assertEqual(settings.key, truth['AWS_ACCESS_KEY'])
        self.assertEqual(settings.secret, truth['AWS_SECRET'])
        self.assertEqual(settings.region, 'us-east-1')


    def test_settings_set_region_from_env(self):
        from baiji.config import settings
        env = EnvironmentVarGuard()
        env.set('AWS_DEFAULT_REGION', 'ap-northeast-1')

        with env:
            self.assertEqual(settings.region, 'ap-northeast-1')