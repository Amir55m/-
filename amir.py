import phonenumbers
from phonenumbers import geocoder, carrier

def get_phone_number_info(phone_number):
    try:
      
        parsed_phone_number = phonenumbers.parse(phone_number, "IR")
        
        # دریافت اطلاعات مربوط به موقعیت جغرافیایی
        location = geocoder.description_for_number(parsed_phone_number, "fa")
        
        # دریافت اطلاعات مربوط به اپراتور
        operator = carrier.name_for_number(parsed_phone_number, "fa")
        
        # بازگشت اطلاعات به ترتیب مطلوب
        return (phone_number, parsed_phone_number.country_code, parsed_phone_number.national_number, location, operator)
    except phonenumbers.NumberParseException as e:
        return (phone_number, None, None, None, None)

# شماره موبایل مورد نظر
phone_number = "+98**"  # شماره موبایل مورد نظر خود را اینجا قرار دهید

# دریافت اطلاعات شماره موبایل
phone_number_info = get_phone_number_info(phone_number)

# چاپ اطلاعات شماره موبایل به ترتیب مطلوب
print("شماره موبایل:", phone_number_info[0])
print("کد کشور:", phone_number_info[1])
print("شماره ملی:", phone_number_info[2])
print("موقعیت جغرافیایی:", phone_number_info[3])
print("اپراتور:", phone_number_info[4])

سورس پایتون به دست اوردن اطلاعات شماره موبایل😉
سازنده امیر حسین شاکری