countries = ['POL', 'ENG', 'GER', 'USA', 'ITA']
is_italy = 'ITA' in countries

assert is_italy # OK

countries = ['POL', 'ENG', 'GER', 'USA', 'ITA']
is_canada = 'CAN' in countries

assert is_canada # AssertionError