from funcoes import *
from email_sender import *
from senhas import *

with Ecommerce() as bot:
    bot.land_first_page()
    while True:
        bot.crawling_products()
        try:
            bot.next_page()
        except:
            bot.save_to_excel()
            break

with Emailer(EMAIL, SENHA) as sender:
    conteudo = '''Ola, tudo bem?
Segue em anexo seu arquivo de hoje com os ultimos preços de celulares!    '''
    to = input('digite o email onde sera enviado sua planilha: ')
    sender.definir_conteudo(topico='eccomerce',
                            conteudo_email=conteudo,
                            destinatario=to,
                            email_remetente=EMAIL
                            )
    sender.anexar_arquivos()
    sender.enviar_email()
