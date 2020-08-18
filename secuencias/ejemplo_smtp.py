from smtplib import SMTP

servidor = SMTP('gmail.com')
remitente = 'nicolas123alejandro@gmail.com'
destinatario = 'nicolas_ale123@hotmail.com'
mensaje = 'From: {0}\nTo: {1}\n\n'.format(remitente, destinatario)
mensaje +='Hola. \n'
mensaje += 'Hasta luego.\n'

servidor.sendmail(remitente, destinatario, mensaje)
