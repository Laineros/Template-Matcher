import argparse
import re
import json
from tinydb import TinyDB

DB_FILE = 'db.json'

def check_type(value):
    date_patterns = [r'^\d{2}\.\d{2}\.\d{4}$', r'^\d{4}-\d{2}-\d{2}$']
    phone_pattern = r'^\+7 \d{3} \d{3} \d{2} \d{2}$'
    email_pattern = r'^[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$'

    for pattern in date_patterns:
        if re.match(pattern, value):
            return 'date'
    if re.match(phone_pattern, value):
        return 'phone'
    if re.match(email_pattern, value):
        return 'email'
    return 'text'

def load_templates():
    db = TinyDB(DB_FILE)
    return db.all()

def add_template(template):
    if 'name' not in template:
        raise ValueError("The 'name' key is required, the template can't be without a name")
    db = TinyDB(DB_FILE)
    db.insert(template)

def match_template(suggested_template):
    templates = load_templates()
    for template in templates:
        template_fields = {k: v for k, v in template.items() if k != 'name'}
        if all(field in suggested_template and check_type(suggested_template[field]) == field_type
               for field, field_type in template_fields.items()):
            return template['name']
    result = {k: check_type(v) for k, v in suggested_template.items()}
    return json.dumps(result, ensure_ascii=False, indent=2)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['get_tpl'])
    known_args, unknown_args = parser.parse_known_args()

    arg_dict = {}
    for arg in unknown_args:
        if arg.startswith('--'):
            key, val = arg[2:].split('=', 1)
            arg_dict[key] = val

    if known_args.command == 'get_tpl':
        result = match_template(arg_dict)
        print(result)

if __name__ == '__main__':
    main()