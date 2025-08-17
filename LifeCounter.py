from datetime import datetime, date

birth_str = input("تاریخ تولد (YYYY-MM-DD)")
birth_date = datetime.strptime(birth_str,"%Y-%m-%d").date()

today = date.today()

age_days = (today - birth_date).days
age_years = age_days // 365
age_months = (age_days % 365) // 30
age_days_left = (age_days % 365) % 30

next_birthday = birth_date.replace(year=today.year)
if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)

days_to_birthday = (next_birthday - today).days

weekdays = ["شنبه", "یکشنبه", "دوشنبه", "سه شنبه", "چهارشنبه", "پنجشنبه", "جمعه"]
born_day = weekdays[birth_date.weekday()]

print("نتیجه:")
print(f"سن شما: {age_years}سال و {age_months} ماه و {age_days_left} روز")
print(f"تولد بعدی شما در {days_to_birthday} روز اینده است")
print(f"روز تولد شما: {born_day}")
