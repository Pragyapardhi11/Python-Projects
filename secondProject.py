import phonenumbers
from phonenumbers import timezone , geocoder,carrier

number = input("enter the phone number:-")
# phoneNumber = phonenumbers.parse("+916268086288")
phoneNumber = phonenumbers.parse(number)
timeZone = timezone.time_zones_for_number(phoneNumber)
Carrier=carrier.name_for_number(phoneNumber,'en')
Geocoder = geocoder.description_for_number(phoneNumber,'en')
print(phoneNumber)
print(timeZone)
print(Carrier)
print(Geocoder)
