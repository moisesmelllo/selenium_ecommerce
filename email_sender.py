from email.message import EmailMessage
import smtplib


class Emailer:
    def __init__(self, email_origem, senha_email):
        self.email_origem = email_origem
        self.senha_email = senha_email

    def __enter__(self):
        # Lógica para configurar a conexão ou qualquer inicialização necessária
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    # Lógica para fechar a conexão ou lidar com erros e limpar recursos

    # Outros métodos da classe

    def definir_conteudo(self, topico, email_remetente, destinatario, conteudo_email):
        self.mail = EmailMessage()
        self.mail['Subject'] = topico
        self.mensagem = conteudo_email
        self.mail['From'] = email_remetente
        self.mail['To'] = destinatario
        self.mail.add_header('Content-Type', 'text/html')
        self.mail.set_payload(self.mensagem.encode('utf-8'))

    def anexar_arquivos(self):
        with open('dados.csv', 'rb') as a:
            dados = a.read()
        self.mail.add_attachment(dados, maintype='application', subtype='octet-stream', filename='dados.csv')

    def enviar_email(self):
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(user=self.email_origem, password=self.senha_email)
            smtp.send_message(self.mail)
