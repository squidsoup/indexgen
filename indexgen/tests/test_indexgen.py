from os import path
from testtools import TestCase

from indexgen.indexgen import read_index_data


class IndexGenTestCase(TestCase):

    def test_read_data(self):
        # make temp file with keywords instead
        data_path = path.join('indexgen', 'testing', 'data.txt')
        keywords = read_index_data(data_path)
        self.assertIn('foo\n', keywords)

    def skip_existing_anchors(self):
        # source text matches with existing anchors should be skipped
        pass
