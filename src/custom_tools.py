import os
from time import sleep
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ast


class Tools:

    def retry(func: object):
        i = 0
        while i < 5:
            sleep(2)
            try:
                func
                break
            except:
                pass

            i += 1

    def getOsName():
        return os.name

    def sendSms():
        pass

    def sendWhatsApp():
        pass

    def sendEmail(self, password, to_email, body, _from, _to):

        economy_seats = body[0]['ECONOMY']
        str_economy = ""
        for seatE in economy_seats:
            for key, val in seatE.items():
                str_economy += key+" -> "+val + "\n"

        business_seats = body[0]['BUSINESS']
        str_business = ""
        for seatB in business_seats:
            for key, val in seatB.items():
                str_business += key+" -> "+val + "\n"

        email_body = f"""
                        Hello,

                        I hope everything is going well for you. I wanted to provide you with information about the tickets. 

                        Here are the details from {_from} to {_to}:
                        
                        ECONOMY CLASS:
                        {str_economy}

                        BUSINESS CLASS:
                        {str_business}

                        I will continue to improve the application. If you have any questions or requests, please feel free to contact me.

                        Best regards,

                        aftekardic
                        """

        msg = MIMEMultipart()
        msg['From'] = to_email
        password = password
        msg['To'] = to_email
        msg['Subject'] = "AVAILABLE SEATS"
        msg.attach(MIMEText(email_body, 'plain'))

        with smtplib.SMTP('smtp-mail.outlook.com', 587) as server:
            server.starttls()
            server.login(to_email, password)
            server.send_message(msg)

        server.close()
