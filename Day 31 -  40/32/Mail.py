import smtplib

myemail = 'itshosyn@gmail.com'
password = '-----------------'

with smtplib.SMTP('smtp.gmail.com', 587) as s:
    s.starttls()
    s.login(myemail, password)
    message = "Subject:This is Test subject\n\nThis is the body of message"

    s.sendmail(myemail,
               'abolfazlkhanzade8744@gmail.com',
               message)