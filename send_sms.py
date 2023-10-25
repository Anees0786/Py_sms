

from twilio.rest import Client

def send_twilio_message(account_SID, account_token, twillios_phn, my_phn, msg):
    client = Client(account_SID, account_token)

    try:
        message = client.messages.create(
            body=msg,
            from_=twillios_phn,
            to=my_phn
        )
        return message
    except Exception as e:
        return f"Error: {e}"

def main():
    print("Send Message using Twilio")

    # Replace these values with your Twilio account SID, account token, and phone numbers
    account_SID = "YOUR ACCOUNT SID"
    account_token = "YOUR ACCOUNT TOKEN"
    twillios_phn = "+17624754370"
    my_phn = "+YOUR PHONE NUMBER"

    msg = input("Enter the message to send: ")

    result = send_twilio_message(account_SID, account_token, twillios_phn, my_phn, msg)

    print("<pre>")
    print(result)
    print("</pre>")

if __name__ == "__main__":
    main()
