from collect_files.collect_files import collect
import os
import shutil
import unittest

class TestCollector(unittest.TestCase):
    def setUp(self):
        self.parent = "data"
        self.out = "out"
        self.nfiles = 1

    def test_run(self):
        collect(self.parent, self.out, self.nfiles)
        struct1 = os.listdir(self.parent)
        struct2 = os.listdir(self.out)
        nfiles = len(os.listdir(os.path.join(self.out, struct1[0])))
        self.assertEqual(struct1, struct2)
        self.assertEqual(self.nfiles, nfiles)

    def test_already_there(self):
        os.mkdir(self.out)
        with self.assertRaises(ValueError):
            collect(self.parent, self.out, self.nfiles)

    def tearDown(self):
        shutil.rmtree(self.out)

