from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 13", "+79126583054"),
    Smartphone("Apple", "iPhone 16", "+79126573856"),
    Smartphone("Apple", "iPhone X", "+791946577396"),

]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")