from address import Address
from mailing import Mailing

to_address = Address("775475848", "Екатеринбург", "Латвийская", "56", "38")
from_address = Address("78737483", "Санкт-Петербург", "Лиговский проспект", "30", "10")

mail = Mailing(to_address, from_address, 1000, "5874857487Y")

print(f"Отправление {mail.track} из {mail.from_address.index}, {mail.from_address.city}, {mail.from_address.street}, {mail.from_address.house} - {mail.from_address.apartment} в {mail.to_address.index}, {mail.to_address.city}, {mail.to_address.street}, {mail.to_address.house} - {mail.to_address.apartment}. Стоимость {mail.cost} рублей.")