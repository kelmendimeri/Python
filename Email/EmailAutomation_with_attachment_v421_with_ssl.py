import smtplib
import csv
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_server = 'postausgang.mail-connect.net'
port = 465
sender = "kelmend.test@inacon.de"
password = "Kelmend001"
with smtplib.SMTP_SSL(smtp_server, port) as server:
    with open('Teilnehmerliste-Fake-Kelmend.csv') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        attch = input("Will you attach a file [y/n]: ")
        for First_Name, Last_Name, email, User_Id, Passwort, MD5_Hash in reader:
            msg = MIMEMultipart()
            server.connect(smtp_server, port)
            server.ehlo()
            server.login(sender, password)
            if attch == 'y':
                filename = f"{First_Name}_{Last_Name}.pdf"
                with open(filename, 'rb') as attchfile:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attchfile.read())
                    encoders.encode_base64(part)
                    part.add_header("Content-Disposition", f"attacment; filename= {filename}", )
                    msg.attach(part)
            msg['Subject'] = "Subject" # you Subject goes heres
            body = f"""Hallo {First_Name} {Last_Name},

            danke für Deine Beiträge während des Kurses! Ich hoffe, daß es dir viel
            gebracht hat und, wie gesagt, nutz einfach die bald folgende "Ask
            Question" Option, um weiterführende Fragen an mich zu stellen.

            Jetzt erstmal Deine Zugangsdaten für Dich, die Kurs-Plattform ist ab
            jetzt PW-geschützt:

            

            UserId: {User_Id}

            Passwort: {Passwort}


            Hab schon wieder neue Inhalte drin und eure ganzen Whiteboard Images und
            die Ask Question Funktion folgen auf dem Fuße.

            Liebe Grüße!"""
            msg.attach(MIMEText(body, "plain"))
            server.sendmail(sender, email, msg.as_string())
            print(f"Successfully sent to {email}")
            server.close()
            del msg
