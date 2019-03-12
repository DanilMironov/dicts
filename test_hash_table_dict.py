import unittest
from hash_table_dict import HashTableDict


class TestHashTableDict(unittest.TestCase):
    def test_init(self):
        hash_dict = HashTableDict()
        self.assertIsInstance(hash_dict.hash_table, list)
        self.assertEqual(hash_dict.size_of_table, 16)
        self.assertEqual(hash_dict.degree_of_occupancy, 0)

    def test_enlarge(self):
        hash_dict = HashTableDict()
        hash_dict.add('sample_key', 1)
        hash_dict._enlarge()
        self.assertEqual(hash_dict.degree_of_occupancy, 1)
        self.assertEqual(hash_dict.size_of_table, 32)

    def test_add(self):
        h_dict = HashTableDict()
        h_dict.add('key', 1)
        self.assertEqual(h_dict.degree_of_occupancy, 1)

    def test_get(self):
        h_dict = HashTableDict()
        h_dict.add('key', 1)
        res = h_dict.get('key')
        expectation = 1
        self.assertEqual(expectation, res)

    def test_get_none(self):
        h_dict = HashTableDict()
        res = h_dict.get(1)
        self.assertIsNone(res)

    def test_items(self):
        hash_dict = HashTableDict()
        hash_dict.add('key1', 1)
        hash_dict.add('key2', 2)
        hash_dict.add('key3', 3)
        res = hash_dict.items()
        self.assertEqual(len(res), 3)
        self.assertTrue(set(res).intersection(
            [('key1', 1),
             ('key2', 2),
             ('key3', 3)]) == {('key1', 1), ('key2', 2), ('key3', 3)})

    def test_keys(self):
        hash_dict = HashTableDict()
        hash_dict.add('key1', 1)
        hash_dict.add('key2', 2)
        hash_dict.add('key3', 3)
        res = hash_dict.keys()
        self.assertTrue(set(res).intersection(
            ['key1', 'key2', 'key3']) == {'key1', 'key2', 'key3'})

    def test_values(self):
        hash_dict = HashTableDict()
        hash_dict.add('key1', 1)
        hash_dict.add('key2', 2)
        hash_dict.add('key3', 3)
        res = hash_dict.values()
        self.assertEqual(len(res), 3)
        self.assertTrue(set(res).intersection([1, 2, 3]) == {1, 2, 3})

    def test_pop(self):
        hash_dict = HashTableDict()
        hash_dict.add('key1', 1)
        hash_dict.add('key2', 2)
        hash_dict.add('key3', 3)
        res = hash_dict.pop('key1')
        self.assertEqual(res, 1)
        self.assertTrue(set(hash_dict.keys()).intersection(
            ['key1', 'key2', 'key3']) == {'key2', 'key3'})


if __name__ == '__main__':
    unittest.main()
