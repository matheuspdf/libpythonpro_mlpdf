from libpythonpro_mlpdf.spam.enviador_de_email import Enviador
from libpythonpro_mlpdf.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao=None):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'matheuslopes.pdf@gmail.com',
        'Curso Python Pro',
        'Corpo'
    )
