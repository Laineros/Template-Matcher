import unittest
from app import check_type, match_template, add_template, load_templates

class TestFormMatcher(unittest.TestCase):

    def test_add_template_success(self):
        template = {"name": "New Template", "field1": "text"}
        add_template(template)
        templates = load_templates()
        self.assertIn(template, templates)

    def test_add_template_without_name_error(self):
        template = {"field1": "text"}
        with self.assertRaises(ValueError):
            add_template(template)

    def test_calculate_value_templates(self):
        templates = load_templates()
        self.assertGreaterEqual(len(templates), 6)

    def test_check_type_success(self):
        self.assertEqual(check_type('27.05.2025'), 'date')
        self.assertEqual(check_type('2025-05-27'), 'date')
        self.assertEqual(check_type('+7 999 888 77 66'), 'phone')
        self.assertEqual(check_type('aaa@bbb.com'), 'email')
        self.assertEqual(check_type('foo bar'), 'text')

    def test_existing_template(self):
        args = {'f_name1': 'aaa@bbb.com', 'f_name2': '2025-05-27'}
        self.assertEqual(match_template(args), 'Test')

    def test_non_existing_template(self):
        args = {'unknown1': '27.05.2025', 'unknown2': '+7 666 666 66 66'}
        result = match_template(args)
        self.assertIn('"unknown1": "date"', result)
        self.assertIn('"unknown2": "phone"', result)

if __name__ == '__main__':
    unittest.main()