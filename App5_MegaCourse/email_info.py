import smtplib, ssl

def send_email(message):
    host = 'smtp.gmail.com'
    port = 465

    username = 'abhadi027@gmail.com'
    password = 'kztoeqizxeimfkjm'

    
    receiver = 'abhadi027@gmail.com'
    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.set_debuglevel(1)  # Enable debug output
            server.login(username, password)
            server.sendmail(username, receiver, message)
            print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        print("Authentication error. Please check your username or password.")
    except Exception as e:
        print(f"Error: {e}")

send_email()
