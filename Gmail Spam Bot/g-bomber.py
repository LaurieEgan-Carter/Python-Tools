import os 
import sys
import getpass
import smtplib


semail = input(' Enter sender Email Address : ')
pswd = getpass.getpass(' Enter sender Password : ')
vemail = input(' Enter Vicitm Email Address : ')
message = input(' Enter Your Message Here : ')
count = int(input(' How Many Time You Want To Send : '))

print()
print('Loading...')
print()


try:
    smtp_server = 'smtp.gmail.com'
    port = 587
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(semail,pswd)
    i = 0
    print(' Sending is in Progress \n')
    while i < count:
        i+=1
        server.sendmail(semail,vemail,message)
        if i == 1:
            print ('Email has been sent successfully ')
        elif i == 2:
            print ('Email has been sent successfully ')
        elif i == 3:
            print ('Email has been sent successfully ')
        else:
            print ('Email has been sent successfully ' %(i))
        sys.stdout.flush()
    server.quit()
    print('All done')

except KeyboardInterrupt:
    print(" ")
    print (' Canceled')
    sys.exit()
    
except smtplib.SMTPAuthenticationError:
    print(" ")
    print(' The username or password you entered is incorrect.')
    print (' Check if the option of "Allow less secure apps" is enabled on the email you want to send the message from.')
    sys.exit()
