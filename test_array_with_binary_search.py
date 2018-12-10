import unittest
from array_with_binary_search import BinaryArray


class TestBinaryArray(unittest.TestCase):
    def test_init(self):
        dic = BinaryArray()
        self.assertIsInstance(dic._data, list)

    def test_add(self):
        dic = BinaryArray()
        dic.add('key1', 1)
        dic.add('key2', 2)
        dic.add('key1', 3)
        self.assertEqual(dic._data, [('key2', 2), ('key1', 3)])

    def test_add2(self):
        dic = BinaryArray()
        dic.add(1, 1)
        dic.add(2, 1)
        dic.add(3, 1)
        dic.add(4, 1)
        dic.add(5, 1)
        dic.add(4, 2)
        self.assertTrue((4, 2) in dic._data)

    def test_get2(self):
        dic = BinaryArray()
        dic.add(1, 'data')
        dic.add(2, 'data2')
        dic.add(3, 'data3')
        dic.add(4, 'data4')
        dic.add(5, 'data5')
        res_1 = dic.get(2)
        res_2 = dic.get(5)
        res_none = dic.get(3003)
        self.assertEqual(res_1, 'data2')
        self.assertEqual(res_2, 'data5')
        self.assertIsNone(res_none)

    def test_values(self):
        dic = BinaryArray()
        dic.add('key1', 1)
        dic.add('key2', 2)
        dic.add('key3', 3)
        result = dic.values()
        self.assertEqual(result, [1, 2, 3])

    def test_items(self):
        dic = BinaryArray()
        dic.add('key1', 1)
        dic.add('key2', 2)
        dic.add('key3', 3)
        result = dic.items()
        self.assertEqual(result, [('key1', 1), ('key2', 2), ('key3', 3)])

    def test_keys(self):
        dic = BinaryArray()
        dic.add('key1', 1)
        dic.add('key2', 2)
        dic.add('key3', 3)
        result = dic.keys()
        self.assertEqual(result, ['key1', 'key2', 'key3'])

    def test_pop(self):
        dic = BinaryArray()
        dic.add('key1', 1)
        dic.add('key2', 2)
        dic.add('key3', 3)
        dic.add('key4', 4)
        dic.add('key5', 5)
        dic.add('key6', 6)
        res_1 = dic.pop('key2')
        self.assertEqual(res_1, 2)
        res_2 = dic.pop('key6')
        self.assertEqual(res_2, 6)
        try:
            dic.pop('ckkk')
        except KeyError as error:
            self.assertRaises(Exception, error)

    def test_clear(self):
        dic = BinaryArray()
        dic.add('key1', 1)
        dic.add('key2', 2)
        dic.add('key3', 3)
        dic.clear()
        self.assertEqual(dic._data, [])

    def test_copy(self):
        dic = BinaryArray()
        dic.add('key1', 1)
        dic.add('key2', 2)
        dic.add('key3', 3)
        new = dic.copy()
        self.assertEqual(new._data, dic._data)


if __name__ == '__main__':
    unittest.main()
