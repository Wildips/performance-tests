from faker import Faker

fake = Faker('ru_RU')

print(fake.name())
print(fake.address())
print(fake.email(domain="gmail.com"))

user_data = {
    "name": fake.name(),
    "email": fake.email(),
    "address": fake.address()
}
