import smtplib
from email.mime.text import MIMEText
import getpass

intento=100
contador=0
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
# Ayuda a encriptar mejor los correo y utulizar mejor los el smtp
server.ehlo()

server.login('','')

while contador < intento:
   
    message=MIMEText('Hola, esto es un mensaje para prueba')
    message['From']=""
    message['To']=""
    message['Subject'] = f"Prueba de correo, intento {contador + 1}"
    server.sendmail(message['From'],message['To'],message.as_string())
    contador+=1
    print(contador)
server.quit()





