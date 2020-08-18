from smtplib import SMTP

servidor = SMTP('')
remitente = ''
texto = 'Estimado =S =A: \n\n'
texto += 'Por la presente le informamos de que nos debe usted la candidad de =E euros.'
texto += ' Si no abona dicha cantidad antes de 3 dias, su nombre pasará a nuestra lista de morosos.'

seguir = 's'
while seguir == 's':
    destinatario = input('Dirección del destinatario: ')
    tratamiento = input('Tratamiento: ')
    apellido = input('Apellido: ')
    euros = input('Deuda (en euros): ')

    mensaje = 'From: {0}\n To: {1}\n\n'.format(remitente, destinatario)
    personalizado = ''
    i = 0
    while i < len(texto):
        if texto[i] != '=':
            personalizado +=texto[i]
        else:
            if texto[i+1]=='A':
                personalizado+=apellido
                i+=1
            elif texto[i+1]=='E':
                personalizado += euros
                i+=1
            elif texto[i+1]=='S':
                personalizado += tratamiento
                i+=1
            else:
                personalizado+='='
        i+=1
    mensaje += personalizado
    servidor.sendmail(remitente, destinatario, mensaje)
    seguir = input('Si desea enviar otro correo pulse "s": ')