import unittest
import ya_api


class TestYaFolder(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("method setUp")

    def tearDown(self):
        print("method tearDown")

    def test_requests_put(self):
        print("создание папки")
        if ya_api.result.status_code != 409:
            self.assertEqual(ya_api.result.status_code, 201)
        else:
            self.assertEqual(ya_api.result.status_code, 409)
            print("папка с таким именем существует")

    def test_add_folder(self):
        print("папка появилась в списке файлов")
        self.assertEqual(ya_api.result_get.status_code, 200)


if __name__ == '__main__':
    unittest.main()