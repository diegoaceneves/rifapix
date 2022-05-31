import rifapix.core
import rifapix.models


DATA=[
    {
        "user":"admin",
        "password":"admin",
        "email":"admin@rifapix.com"
    },
    {
        "user":"user",
        "password":"user",
        "email":"user@rifapix.com"
    },
    {
        "user":"user2",
        "password":"user2",
        "email":"user2@rifapix.com"
    }    
]

for d in DATA:
    rifapix.core.add_user_to_database(
        user=d['user'],
        password=d['password'],
        email=d['email']
    )

print(rifapix.core.get_users_from_database())

# print(rifapix.core.del_users_from_database(id=2))