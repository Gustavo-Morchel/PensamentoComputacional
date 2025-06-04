import re

def validar_email(email):
    padrao = r'^[a-z]+\.[a-z]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    email2_0 = padrao = r'^[a-z0-9]+\.[a-z0-9]+@(gmail|hotmail|outlook)\.com$'#só pode esses 3 dominios
    return bool(re.match(padrao, email))


emails = ['usuario@gmail.com', 'usuario.o2@gmail.com','usuario3@Gmail.com', 'aaa0.gmailcom', 'gustavo.morchel@g.c']

for email in emails:
    print(f'{email}: {'é válido' if validar_email(email) else "não é válido"}')


