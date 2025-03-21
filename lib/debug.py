from models import Company, Dev, Freebie, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///freebie_tracker.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

company1 = Company(name="TechCorp", founding_year=2000)
company2 = Company(name="CodeMaster", founding_year=1995)
dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")

session.add_all([company1, company2, dev1, dev2])
session.commit()

freebie1 = Freebie(item_name="T-shirt", value=20, dev=dev1, company=company1)
freebie2 = Freebie(item_name="Sticker", value=5, dev=dev2, company=company2)

session.add_all([freebie1, freebie2])
session.commit()

print("Dev1's freebies:", dev1.freebies)
print("Company1's devs:", company1.devs)

print("Freebie1 details:", freebie1.print_details())

new_freebie = company1.give_freebie(dev2, "Mug", 10)
print("New freebie details:", new_freebie.print_details())

oldest = Company.oldest_company()
print("Oldest company:", oldest.name)

print("Does Dev1 have a T-shirt?", dev1.received_one("T-shirt"))
print("Does Dev1 have a Mug?", dev1.received_one("Mug"))

print("Before give_away - Freebie1 dev:", freebie1.dev.name)
dev1.give_away(dev2, freebie1)
print("After give_away - Freebie1 dev:", freebie1.dev.name)

session.commit()