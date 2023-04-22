"""
import ezgmail, os
#ezgmail.send('lucas.murphy31@outlook.com', 'A computer is emailing you', 'Hi Lucas, I am emailing you from my code!')
unreadThreads = ezgmail.unread()
resultThreads = ezgmail.search('stocking')


import smtplib
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('mpetry14@gmail.com', 'Youaremysunshine1')
smtpObj.sendmail('mpetry14@gmail.com', 'katie.m.murphy@outlook.com', 'Subject: Test 2\n Hi Katie, hope you are well !')
smtpObj.quit()
"""
import imapclient

imapObj = imapclient.IMAPClient("imap.gmail.com", ssl=True)
imapObj.login("mpetry14@gmail.com", "Youaremysunshine1")
