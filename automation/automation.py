import shutil
from faker import Faker
import re

fake = Faker('en_US')

content = ""

for _ in range(100):
    content += fake.paragraph()
    content += fake.email()
    content += fake.address()
    content += fake.phone_number()
    content += fake.word()

with open('automation/assest/potential-contacts.txt', 'w+') as file:
    file.write(content)

with open("automation/assest/potential-contacts.txt","r") as f:
    file_content=f.read()


match = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', file_content)
match=set(match)


with open("automation/assest/Email.txt", "w") as f:
    for element in match:
        f.write(element + "\n")

phone = re.findall(r'\d{3}-\d{3}-\d{4}|\d{3}-\d{4}', file_content)

with open("automation/assest/phone.txt", "w") as f:
    for element in phone:
        if len(element)==12:
         f.write( element + "\n")

        if len(element)==8:
          f.write( "206-"+ element + "\n")








