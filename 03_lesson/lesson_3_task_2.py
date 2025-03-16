from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 13", "+79126583054"),
    Smartphone("Apple", "Realme 10", "+79126573856"),
    Smartphone("Apple", "OnePlus 13", "+791946577396"),
    Smartphone("Apple", "Xiaomi RedmeNote 11S", "+79126549874"),
    Smartphone("Apple", "Samsung Galaxy A23", "+79196503123"),

]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")