import pytest

from libpythonpro_mlpdf.spam.enviador_de_email import Enviador
from libpythonpro_mlpdf.spam.main import EnviadorDeSpam
from libpythonpro_mlpdf.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Matheus', email='matheuslopes.pdf@gmail.com'),
            Usuario(nome='Gabriel', email='matheuslopes.pdf@gmail.com')
        ],
        [
            Usuario(nome='Gabriel', email='matheuslopes.pdf@gmail.com')
        ]
    ]
)
def test_qte_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'matheuslopes.pdf@gmail.com',
        'Curso Python Pro',
        'Corpo'
    )
    assert len(usuarios) == enviador.qtd_email_enviados
