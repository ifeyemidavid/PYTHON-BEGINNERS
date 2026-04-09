import phonenumbers
from phonenumbers import geocoder, carrier
import requests

def phone_info():
    input_number = input("Enter the phone number (with country code): ")
    try:
        parsed_number = phonenumbers.parse(input_number)
        print(f"Country: {geocoder.description_for_number(parsed_number, 'en')}")
        print(f"Carrier: {carrier.name_for_number(parsed_number, 'en')}")
    except Exception as e:
        print(f"Error parsing phone number: {e}")

def ip_info():
    input_ip = input("Enter the IP address: ")
    try:
        response = requests.get(f"https://ipinfo.io/{input_ip}/json")
        data = response.json()
        print(f"IP: {data.get('ip', 'N/A')}")
        print(f"City: {data.get('city', 'N/A')}")
        print(f"Region: {data.get('region', 'N/A')}")
        print(f"Country: {data.get('country', 'N/A')}")
        print(f"Location: {data.get('loc', 'N/A')}")
        print(f"Organization: {data.get('org', 'N/A')}")
    except Exception as e:
        print(f"Error fetching IP information: {e}")
    


def main():
    while True:
        print("\nChoose an option:")
        print("1. Get phone number information")
        print("2. Get IP address information")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            phone_info()
        elif choice == '2':
            ip_info()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()