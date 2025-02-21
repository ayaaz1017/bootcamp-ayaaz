import requests

# API URL for ExchangeRate-API
API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

def convert_currency(amount, target_currency):
    try:
        # Fetch currency rates
        response = requests.get(API_URL)
        
        if response.status_code == 200:
            data = response.json()
            rates = data.get("rates", {})

            # Check if target currency exists in response
            if target_currency in rates:
                conversion_rate = rates[target_currency]
                converted_amount = amount * conversion_rate

                print(f"💵 Currency Conversion 💵")
                print(f"1 USD = {conversion_rate} {target_currency}")
                print(f"{amount} USD = {converted_amount:.2f} {target_currency}")
            else:
                print(f"❌ Error: Unsupported currency code '{target_currency}'")
        else:
            print(f"❌ Error: Failed to fetch exchange rates. Status code: {response.status_code}")

    except Exception as e:
        print(f"❌ Error: {e}")

# Example usage
amount = float(input("Enter amount in USD: "))
target_currency = input("Enter target currency (e.g., EUR, INR, GBP): ").upper()

convert_currency(amount, target_currency)
