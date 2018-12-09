import unittest
from the_simpliest_dict import LinearArray


class TestSimpleDict(unittest.TestCase):
    def test_init(self):
        dic = LinearArray()
        self.assertIsInstance(dic._data, list)

    def test_add(self):
        dic = LinearArray()
        dic.add('key1', 1)
        dic.add('key2', 2)
        dic.add('key1', 3)
        self.assertEqual(dic._data, [('key2', 2), ('key1', 3)])

    def test_get(self):
        dic = LinearArray()
        dic.add('key1', 1)
        dic.add('key2', 2)
        result = dic.get('key1')
        self.assertEqual(result, 1)

    def test_get_none(self):
        dic = LinearArray()
        dic.add('key1', 1)
        dic.add('key2', 2)
        result = dic.get('key')
        self.assertIsNone(result)

    def test_values(self):
        dic = LinearArray()
        dic.add('key1', 1)
        dic.add('key2', 2)
        result = dic.values()
        self.assertEqual(result, [1, 2])

    def test_items(self):
        dic = LinearArray()
        dic.add('key1', 1)
        dic.add('key2', 2)
        result = dic.items()
        self.assertEqual(result, [('key1', 1), ('key2', 2)])

    def test_keys(self):
        dic = LinearArray()
        dic.add('key1', 1)
        dic.add('key2', 2)
        result = dic.keys()
        self.assertEqual(result, ['key1', 'key2'])

    def test_pop(self):
        dic = LinearArray()
        dic.add('key1', 1)
        dic.add('key2', 2)
        result = dic.pop('key1')
        self.assertEqual(result, 1)
        self.assertIsNone(dic.get('key1'))

    def test_pop_error(self):
        dic = LinearArray()
        dic.add('key1', 1)
        dic.add('key2', 2)
        try:
            dic.pop('key3')
        except KeyError as error:
            self.assertRaises(Exception, error)

    def test_clear(self):
        dic = LinearArray()
        dic.add('key1', 1)
        dic.add('key2', 2)
        dic.clear()
        self.assertEqual(dic._data, [])

    def test_copy(self):
        dic = LinearArray()
        dic.add('key1', 1)
        dic.add('key2', 2)
        result = dic.copy()
        self.assertEqual(result._data, dic._data)


if __name__ == '__main__':
    unittest.main()
