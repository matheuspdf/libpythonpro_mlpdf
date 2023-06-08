from libpythonpro_mlpdf.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Matheus', email='matheuslopes.pdf@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Matheus', email='matheuslopes.pdf@gmail.com'),
                Usuario(nome='Gabriel', email='matheuslopes.pdf@gmail.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
