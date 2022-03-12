from datetime import date

# run: python -m unittest 26_message-class-mock.py
def get_today_name():
    return date.today().strftime('%A')

def get_message():
    return f'Hello {get_today_name()}!'