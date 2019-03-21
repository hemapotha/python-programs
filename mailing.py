#sending mail through python


import smtplib
import getpass

s=smtplib.SMTP('smtp.gmail.com','587')
s.starttls()
sender='pothahemareddy@gmail.com'
receiver='pothahemareddy@gmail.com'
msg="hii"
p=getpass.getpass()
s.login(sender,p)
s.sendmail(sender,receiver,msg)
print("msg sent successfully")
s.quit()