import ssl
import socket
from datetime import datetime

def check_ssl_expiry(domain):
    """
    Retrieves the SSL certificate expiration date of a website.
    :param domain: Example: 'google.com'
    """
    context = ssl.create_default_context()
    
    try:
        # Establish a connection to the domain on port 443
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Retrieve certificate data
                cert = ssock.getpeercert()
                # Extract the expiration date (notAfter)
                exp_date_str = cert['notAfter']
                expiry_date = datetime.strptime(exp_date_str, '%b %d %H:%M:%S %Y %Z')
                
                # Calculate remaining days
                days_left = (expiry_date - datetime.utcnow()).days
                print(f"🔒 Domain: {domain}")
                print(f"📅 Expires on: {expiry_date}")
                print(f"⏳ Days remaining: {days_left}")

    except Exception as e:
        print(f"❌ Error checking SSL for {domain}: {e}")

# Testing
check_ssl_expiry("github.com")
