
#send mail using smtp

import smtplib
from getpass import getpass

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
sender = 'kushal.18bcs@cmr.edu.in'
reciever = 'kushalkp88@gmail.com'
message = "hii"
password = "kushalkp8998"
s.login(sender, password)
s.sendmail(sender, reciever, message)	
	
