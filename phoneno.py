import phonenumbers
from phonenumbers import geocoder, carrier, timezone

number = input("Enter Number: ")

number_det = phonenumbers.parse(f"+91{number}", None)
country = geocoder.description_for_number(number_det, "en")
ro_number = carrier.name_for_number(number_det, "en")
name=timezone.time_zones_for_number(number_det)

print(f"number:{number} \nCountry:{country} \nCarrier:{ro_number}\nName:{name}")