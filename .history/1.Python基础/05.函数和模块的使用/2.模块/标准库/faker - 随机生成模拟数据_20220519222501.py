from faker import Faker

fake = Faker(locale='zh_CN')

for _ in range(20):
    print(fake.name())
