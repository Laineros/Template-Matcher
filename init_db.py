from app import add_template

templates = [
    {
        "name": "User Info",
        "login": "email",
        "tel": "phone"
    },
    {
        "name": "Driver Order Form",
        "employee": "text",
        "order_date": "date",
        "contact": "phone"
    },
    {
        "name": "User Order Form",
        "customer": "text",
        "order_date": "date",
        "contact": "phone",
        "mail": "email"
    },
    {
        "name": "Admin Order Form",
        "customer": "text",
        "order_id": "text",
        "order_date": "date",
        "contact": "phone"
    },
    {
        "name": "SuperUser Order Form",
        "driver_id": "text",
        "order_id": "text",
        "order_date": "date",
        "contact": "phone"
    },
    {
        "name": "Test",
        "f_name1": "email",
        "f_name2": "date"
    }
]

for template in templates:
    add_template(template)

print("Database initialized!")