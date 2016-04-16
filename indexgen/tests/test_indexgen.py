from os import path

from fixtures import TempDir
from testtools import TestCase

from indexgen.indexgen import read_index_data


class IndexGenTestCase(TestCase):

    indices = ['borovik', 'grub', 'holy family',
               'inky', 'pine', 'raw', 'toadstools']

    def setUp(self):
        super(IndexGenTestCase, self).setUp()
        self.tmpdir = self.useFixture(TempDir()).path

    def test_read_data(self):
        # make temp file with test indices
        index_path = path.join(self.tmpdir, 'index')
        indices = '\n'.join(self.indices) + '\n'
        with open(index_path, 'w') as f:
            f.write(indices)
        results = read_index_data(index_path)
        self.assertItemsEqual(self.indices, results)

    def skip_existing_anchors(self):
        # source text matches with existing anchors should be skipped
        pass
