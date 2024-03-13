dial_codes = [
    (880, 'Bangladesh'),
    (55, 'Brazil'),
    (86, 'China'),
    (91, 'India'),
    (62, 'Indonesia'),
    (81, 'Japan'),
    (234, 'Nigeria'),
    (92, 'Pakistan'),
    (7, 'Russia'),
    (1, 'United States'),
]

dial_codes_dict = {code: country for (code, country) in dial_codes}
print(dial_codes_dict)
dial_codes_dict_upper = {code: country.upper() for (code, country) in dial_codes_dict.items() if code < 70}
print(dial_codes_dict_upper)