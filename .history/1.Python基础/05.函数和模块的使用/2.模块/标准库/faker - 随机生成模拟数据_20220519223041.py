from faker import Faker

fake = Faker(locale='zh_CN')

print(fake.name())
print(fake.address())
print(fake.text())
print(fake.phone_number())
print(fake.email())
print(fake.company())
print(fake.credit_card_number())
print(fake.credit_card_expire())
print(fake.credit_card_provider())
print(fake.password())

print(fake.mac_address())
print(fake.city())
