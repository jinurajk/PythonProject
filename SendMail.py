import smtplib

#sender = 'from@fromdomain.com'
#receivers = "shindeamitv8@gmail.com"

#message = """From: From Person <from@fromdomain.com>

try:
   smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
   smtpObj.starttls()
   smtpObj.login("k.jinuraj@gmail.com", "123kottackal@")
   smtpObj.sendmail("k.jinuraj@gmail.com", "k.jinuraj@gmail.com", "Hello Amit, how are you?")         
   print ("Successfully sent email")
except SMTPException:
   print ("Error: unable to send email")