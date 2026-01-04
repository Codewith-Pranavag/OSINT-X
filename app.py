import requests

def check_my_email():
    print("--- OSINT-X Email Breach Checker ---")
    email = input("Enter the email you want to check: ")
    
    # This sends the email to the XposedOrNot website
    url = f"https://api.xposedornot.com/v1/check-email/{email}"
    
    response = requests.get(url)

    if response.status_code == 200:
        print(f"⚠️ ALERT! This email was found in data breaches.")
        print(response.json()) # This prints the list of hacks
    elif response.status_code == 404:
        print("✅ Good news! This email was not found in any known breaches.")
    else:
        print("❌ Something went wrong. Try again later.")

# Run the tool
check_my_email()