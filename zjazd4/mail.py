import smtplib

userr="przemo"
passwordd="hasło"

sent_from="przemo@x.pl"
to=["zdzichu@x.pl"]
subject="temat"
body="treść"

email_txt=f"""
From: {sent_from}
To: {', '.join(to)}
Subject: {subject}

{body}
"""

try:
    server=smtplib.SMTP_SSL("smtp.wp.pl", 465)
    server.ehlo()
    server.login(userr, passwordd)
    server.sendmail(sent_from, to, email_txt)
    server.close()
except Exception as e:
    print(e)
    print("Coś pękło - może gumcia")
