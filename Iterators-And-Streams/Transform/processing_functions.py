def upper_case(input_filename, output_filename=None):
    with open(input_filename, 'r') as infile:
        lines = infile.readlines()

    output_filename = output_filename or input_filename + '.processed'
    with open(output_filename, 'w') as outfile:
        for line in lines:
            outfile.write(line.upper())

def remove_stop_words(text):
    stop_words = {'a', 'an', 'the', 'and', 'or'}
    words = text.split()
    return ' '.join([word for word in words if word not in stop_words])

def capitalize(text):
    return text.title()

def fetch_geo_ip(ip):
    import requests
    response = requests.get(f"https://ipinfo.io/{ip}/geo")
    geo_data = response.json()
    return f"{geo_data['city']}, {geo_data['region']}, {geo_data['country']}"

def lower_case(text):
    return text.lower()

def uk_to_us(text):
    import re
    return re.sub(r'sation$', 'zation', text.lower())
