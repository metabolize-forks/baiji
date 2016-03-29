import os
import unittest
import uuid
from test.test_support import EnvironmentVarGuard
from baiji.util import tempfile

class TestTempfile(unittest.TestCase):

    def test_that_NamedTemporaryFile_honors_TMP_env_var(self):
        self.env = EnvironmentVarGuard()
        self.env.set('BAIJI_TMP', '.')
        with self.env:
            with tempfile.NamedTemporaryFile('w') as tf:
                self.assertEquals(os.path.dirname(tf.name), os.getcwd())
