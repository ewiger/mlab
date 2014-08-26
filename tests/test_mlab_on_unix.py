import sys
sys.path = ['../src/'] + sys.path
import unittest
from mlab.mlabwrap import MatlabReleaseNotFound


class TestMlabUnix(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_version_discovery(self):
        import mlab
        instances = mlab.releases.MatlabVersions(globals())
        assert len(instances.pick_latest_release()) > 0
        with self.assertRaises(MatlabReleaseNotFound):
            mlab_inst = instances.get_mlab_instance('R2010c')

    def test_latest_release(self):
        from mlab.releases import latest_release
        from matlab import matlabroot
        self.assertTrue(len(matlabroot())>0)
        matlabroot()


if __name__ == '__main__':
    unittest.main()
