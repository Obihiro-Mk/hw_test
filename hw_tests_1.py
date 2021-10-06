import unittest
from unittest.mock import patch
import app


class TestApp(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("method setUp")

    def tearDown(self):
        print("method tearDown")

    @patch("builtins.input", return_value="10006")
    def test_get_doc_owner_name(self, mock_input):
        print("test_get_doc_owner_name")
        self.assertEqual(app.get_doc_owner_name(), "Аристарх Павлов")

    def test_get_all_doc_owners_names(self):
        users_list = []
        for current_document in app.documents:
            doc_owner_name = current_document['name']
            users_list.append(doc_owner_name)
        result = set(users_list)
        print("test_get_all_doc_owners_names")
        self.assertEqual(app.get_all_doc_owners_names(), result)

    @patch("builtins.input")
    @patch("builtins.input")
    @patch("builtins.input")
    @patch("builtins.input")
    def test_add_new_doc(self, parm1,  parm2, parm3, parm4):
        parm1.return_value = "4505"
        parm2.return_value = "passport"
        parm3.return_value = "Roman"
        parm4.return_value = "2207"
        self.assertEqual(app.add_new_doc(), "2207")

    @patch("builtins.input", return_value="2207 876234")
    def test_delete_doc(self, mock_input):
        print("test_delete_doc")
        self.assertEqual(app.get_doc_owner_name(), "Василий Гупкин")


if __name__ == '__main__':
    unittest.main()
