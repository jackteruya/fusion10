from django import forms
from django.core.mail.message import EmailMessage

from services.send_grid import SendGridServic


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.CharField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=100)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'<p>Nome: {nome} <br>E-mail: {email} <br>Assunto: {assunto} <br>Mensagem: {mensagem}<\p>'

        # Estas configurações são para servidores de e-mail
        # mail = EmailMessage(
        #     subject=assunto,
        #     body=conteudo,
        #     from_email='contato@fusion.com.br',
        #     to=['contato@fusion.com.br',],
        #     headers={'Reply-To': email}
        # )
        # mail.send()

        # API Send Grid
        mail = SendGridServic(subject=assunto, content=conteudo, email=email)
        mail.send_email()
