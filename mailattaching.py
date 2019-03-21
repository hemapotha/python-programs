import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
   
fromaddr = "pothahemalathareddy@gmail.com"
toaddr = "hemsareddy@gmail.com"
   
msg = MIMEMultipart() 
    
msg['From'] = fromaddr 
    
msg['To'] = toaddr 
  
msg['Subject'] = "requirement of notes"
  
body = "send me important notes"
  
msg.attach(MIMEText(body, 'plain')) 
  
filename = "mailing.py"
attachment = open("/home/bl119/Desktop/hemapy/mailing.py", "rb") 
  
p = MIMEBase('application', 'octet-stream') 
  
p.set_payload((attachment).read()) 
  
encoders.encode_base64(p) 
   
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
  
msg.attach(p) 

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