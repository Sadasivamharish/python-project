
import smtplib
import csv

def send_bulk_emails(sender_email, sender_password, subject, message, recipient_file):
    # Read recipient details from CSV file
    with open(recipient_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        recipients = [row[0] for row in reader]  # Assuming email addresses are in the first column

    # Prepare the email message
    email_message = f"Subject: {subject}\n\n{message}"

    # Connect to SMTP server
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)  # Replace with your email provider's SMTP server
    smtp_server.starttls()
    smtp_server.login(sender_email, sender_password)

    try:
        # Send email to each recipient
        for recipient in recipients:
            smtp_server.sendmail(sender_email, recipient, email_message)
            print(f"Email sent to {recipient}")

        print("All emails sent successfully!")
    except smtplib.SMTPException as e:
        print(f"Error sending emails: {str(e)}")
    finally:
        # Disconnect from the SMTP server
        smtp_server.quit()

# Example usage
sender_email = 'your_email@example.com'  # Replace with your email address
sender_password = 'your_password'  # Replace with your email password
subject = 'Hello'
message = 'This is a test email sent using Python.'
recipient_file = 'recipients.csv'  # Replace with the path to your CSV file

send_bulk_emails(sender_email, sender_password, subject, message, recipient_file)

