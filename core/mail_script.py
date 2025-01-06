from django.core.mail import send_mail
def send_email(name, email, phone, subject, message):
    try:
        full_message = f"""
        Name: {name}
        Email: {email}
        Phone: {phone if phone else 'N/A'}
        Message: {message}
        """
        send_mail(
            subject=f"Contact Us Form Submission: {subject}",
            message=full_message,
            from_email=email,  # You can use EMAIL_HOST_USER here if desired
            recipient_list=['wasimranjhaa@gmail.com'],  # Replace with the recipient's email
        )
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")