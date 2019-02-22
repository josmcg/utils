from yaml_reader.yaml_reader import YAMLReader
import unittest

class TestConfig(unittest.TestCase):
    def setUp(self):
        self.fp = "model_config.yaml"

    def test_init(self):
        cfg = YAMLReader(self.fp)
        self.assertIsNotNone(cfg.instance)

    def test_multi_init(self):
        cfg = YAMLReader(self.fp)
        cfg1 = YAMLReader()
        self.assertEqual(cfg.instance, cfg1.instance)

    def test_access(self):
        cfg = YAMLReader(self.fp)
        img_size = cfg.IMAGE_SIZE
        self.assertEqual(img_size, 1920)

    def test_access_nested(self):
        cfg = YAMLReader(self.fp)
        intermediate = cfg.HEAD.INTERMEDIATE
        self.assertEqual(intermediate, 1024)

    def test_update(self):
        cfg = YAMLReader(self.fp)
        img_size_1 = cfg.IMAGE_SIZE
        cfg.IMAGE_SIZE = img_size_1 + 2
        self.assertEqual(cfg.IMAGE_SIZE, img_size_1 + 2)

    def test_update_propogation(self):
        cfg = YAMLReader(self.fp)
        cfg1 = YAMLReader()
        cfg1.IMAGE_SIZE = 12
        self.assertEqual(cfg.IMAGE_SIZE, 12)