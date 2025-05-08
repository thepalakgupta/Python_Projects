# Hardcoded currency exchange rates (base: 1 unit of source)
exchange_rates = {
    'USD': {'INR': 83.12, 'EUR': 0.93},
    'INR': {'USD': 0.012, 'EUR': 0.011},
    'EUR': {'USD': 1.07, 'INR': 89.12}
}

def convert_currency(from_currency, to_currency, amount):
    try:
        rate = exchange_rates[from_currency][to_currency]
        return amount * rate
    except KeyError:
        return None

def main():
    print("💱 Currency Converter")
    print("Supported currencies: USD, INR, EUR")

    while True:
        from_curr = input("From currency (e.g., USD): ").upper()
        to_curr = input("To currency (e.g., INR): ").upper()
        
        try:
            amount = float(input(f"Amount in {from_curr}: "))
        except ValueError:
            print("Invalid amount. Try again.")
            continue

        result = convert_currency(from_curr, to_curr, amount)

        if result is not None:
            print(f"{amount:.2f} {from_curr} = {result:.2f} {to_curr}")
        else:
            print("Conversion not supported or currency code invalid.")

        again = input("Do you want to convert another amount? (y/n): ").lower()
        if again != 'y':
            print("Thank you for using the Currency Converter!")
            break

# Run the converter
main()
