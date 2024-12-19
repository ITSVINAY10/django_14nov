import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'modelproject33.settings')
import django
django.setup()

from testapp.models import Student
from faker import Faker
from random import randint

faker = Faker()

# Function to generate random phone numbers
def phonenumbergen():
    d1 = randint(6, 9)  # Ensures the first digit is 6-9
    num = str(d1)
    for i in range(9):  # Generates the remaining 9 digits
        num += str(randint(0, 9))
    return int(num)

# Function to populate the database
def populate(n):
    for i in range(n):
        frollno = faker.random_int(min=1, max=999)
        fname = faker.name()
        fdob = faker.date()
        fmarks = faker.random_int(min=1, max=99)
        femail = faker.email()
        fphonenumber = phonenumbergen()  # Corrected function call
        faddress = faker.address()
        # Insert record into the database
        Student.objects.get_or_create(
            rollno=frollno,
            name=fname,
            dob=fdob,
            marks=fmarks,
            email=femail,
            phonenumber=fphonenumber,
            address=faddress,
        )

# Input and execution
n = int(input('Enter number of records: '))
populate(n)
print(f'{n} Records inserted successfully...')
