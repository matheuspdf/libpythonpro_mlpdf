import pytest


from libpythonpro_mlpdf.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['mathsoad@gmail.com', 'violoncelopes@gmail.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'matheuslopes.pdf@gmail.com',
        'Assunto teste',
        'corpo teste'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'violoncelopes']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'matheuslopes.pdf@gmail.com',
            'Assunto teste',
            'corpo teste'
        )
