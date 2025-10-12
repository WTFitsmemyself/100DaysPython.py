import smtplib
from email.message import EmailMessage
from email.utils import make_msgid
import mimetypes
import os

# Email credentials and addresses
sender_email = "itshosyn@gmail.com"
receiver_email = "h.nouri.taksatsp@gmail.com"
password = "------------------"  # Use Gmail app password

# Create the email message
msg = EmailMessage()
msg['Subject'] = "New Version of a message"
msg['From'] = sender_email
msg['To'] = receiver_email

# Embed image into HTML
image_cid = make_msgid(domain='xyz.com')  # Unique content ID

# HTML content (use image_cid[1:-1] to remove angle brackets)
html_content = f"""
<html>
  <body>
    <h1>Hello from Python!</h1>
    <p>This email contains an <b>HTML message</b>, an inline image, and a file attachment.</p>
    <img src="cid:{image_cid[1:-1]}" alt="Certificate" width="300" />
  </body>
</html>
"""

msg.set_content("This is the fallback plain text.")
msg.add_alternative(html_content, subtype='html')

# Add the image as an attachment (inline)
with open("image.jpg", 'rb') as img:
    img_data = img.read()
    msg.get_payload()[1].add_related(img_data, 'image', 'jpg', cid=image_cid)

# Add a file attachment
attachment_path = "CV.pdf"
filename = os.path.basename(attachment_path)

# Guess MIME type
mime_type, _ = mimetypes.guess_type(attachment_path)
mime_type = mime_type or 'application/octet-stream'
maintype, subtype = mime_type.split('/')

with open(attachment_path, 'rb') as file:
    file_data = file.read()
    msg.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=filename)

# Send the email using Gmail's SMTP server
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, password)
        smtp.send_message(msg)
        print("Email sent successfully!")
except Exception as e:
    print("Error sending email:", e)