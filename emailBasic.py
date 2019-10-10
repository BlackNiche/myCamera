import smtplib
from datetime import datetime
email = 'goodshepherdiot@gmail.com'                    #Email account the file is sent to
password = 'P@ssword#1'                                #Email's password
sendToEmail = 'jl.Niche02@gmail.com'                   #Email address the file is sent to
message = str('Hi', str(datetime.now()))               #The Message of the email
server = smtplib.SMTP('smtp.gmail.com', 587)           #connect to the gmail server
server.starttls()                                      #use TLS (Transport Layer Security)
server.login(email, password)                          #logs into the email
server.sendmail(email, sendToEmail, message)           #sends mail from the email, to the SendTo, as the message
server.quit()