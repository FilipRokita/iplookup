import sys
import requests
import json

# API_CONFIG contains URLs for various IP geolocation services.
# The placeholders '{}' in the URLs will be replaced with the target IP address.
# Feel free to add more services if needed or adjust the existing ones.
API_CONFIG = {
    "ipinfo": "https://ipinfo.io/{}/json",
    "ip-api": "http://ip-api.com/json/{}",
    "ipapi": "https://api.ipapi.is/?q={}",
    "iplocation": "https://api.iplocation.net/?ip={}",
    "ipwhois": "https://ipwhois.app/json/{}",
    "freeipapi": "https://freeipapi.com/api/json/{}"
}

def fetch_ip_info(api_name, ip):
    url = API_CONFIG[api_name].format(ip) if api_name != "ipgeolocation" else f"{API_CONFIG[api_name]}&ip={ip}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as http_err:
        return {"error": f"HTTP error occurred: {http_err}"}
    except requests.RequestException as req_err:
        return {"error": f"Request error occurred: {req_err}"}
    except Exception as err:
        return {"error": f"An error occurred: {err}"}

def print_usage_and_exit():
    print(json.dumps({"error": "Usage: python iplookup.py [-s] <ip-address>"}))
    sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print_usage_and_exit()

    save_to_file = False
    ip_address = None
    
    if sys.argv[1] == '-s':
        if len(sys.argv) < 3:
            print_usage_and_exit()
        save_to_file = True
        ip_address = sys.argv[2]
    else:
        ip_address = sys.argv[1]

    if not ip_address:
        print_usage_and_exit()

    results = {}
    for api_name in API_CONFIG:
        data = fetch_ip_info(api_name, ip_address)
        results[api_name] = data

    output = json.dumps(results, indent=4)
    print(output)
    
    if save_to_file:
        with open("ip_lookup_result.json", "w") as file:
            file.write(output)
        print("Data saved to ip_lookup_result.json")

if __name__ == "__main__":
    main()
