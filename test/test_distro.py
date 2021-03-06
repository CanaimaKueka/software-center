#!/usr/bin/python


import sys
sys.path.insert(0,"../")

import unittest

from softwarecenter.distro import get_distro

class TestDistro(unittest.TestCase):
    """ tests the distro class """

    def test_get_distro(self):
        distro = get_distro()
        self.assertNotEqual(distro, None)
        
    def test_distro_functions(self):
        distro = get_distro()
        codename = distro.get_codename()
        self.assertNotEqual(codename, None)
        myname = distro.get_app_name()
        self.assertTrue(len(myname) > 0)
        arch = distro.get_architecture()
        self.assertNotEqual(arch, None)


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
