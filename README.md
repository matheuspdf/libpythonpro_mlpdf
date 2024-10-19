# libpythonpro-mlpdf
Este README tem como propósito registrar e documentar os conceitos aprendidos durante o Curso Pytools da comunidade DevPro.

[![Lib Python](https://github.com/matheuspdf/libpythonpro_mlpdf/actions/workflows/python.yaml/badge.svg)](https://github.com/matheuspdf/libpythonpro_mlpdf/actions/workflows/python.yaml) [![codecov](https://codecov.io/gh/matheuspdf/libpythonpro_mlpdf/branch/main/graph/badge.svg?token=0TT2NUN8W0)](https://codecov.io/gh/matheuspdf/libpythonpro_mlpdf)

![Version](https://img.shields.io/pypi/v/libpythonpro-mlpdf)
![License](https://img.shields.io/badge/license-MIT-blue)


**libpythonpro-mlpdf** é uma biblioteca Python disponível no [PyPI](https://pypi.org/), projetada para facilitar a busca e recuperação do avatar de qualquer usuário do GitHub. Com esta biblioteca, você pode acessar rapidamente as imagens de perfil dos usuários do GitHub utilizando apenas o nome de usuário.

## Instalação

Instale a biblioteca usando o gerenciador de pacotes `pip`:

```bash
pip install libpythonpro-mlpdf
```

## Como Usar

Siga estes passos simples:

1. **Criar um Ambiente Virtual**:

   ```bash
   python -m venv venv
   ```

2. **Ativar o Ambiente Virtual**:

   - **Windows**:

     ```bash
     venv\Scripts\activate
     ```

   - **macOS e Linux**:

     ```bash
     source venv/bin/activate
     ```

3. **Instalar a Biblioteca**:

   ```bash
   pip install libpythonpro-mlpdf
   ```

4. **Iniciar o Console do Python**:

   ```bash
   python
   ```

5. **Buscar o Avatar**:

   Execute os seguintes comandos:

   ```python
   from libpythonpro_mlpdf.github_api import buscar_avatar
   avatar_url = buscar_avatar("matheuspdf")  # Exemplo com meu usuário
   ```

### Exemplo de Saída

O comando acima retorna um link para o seu avatar:

**Saída:** 
['https://avatars.githubusercontent.com/u/96511087?v=4'](https://avatars.githubusercontent.com/u/96511087?v=4)

[![Avatar do GitHub](https://avatars.githubusercontent.com/u/96511087?v=4)](https://avatars.githubusercontent.com/u/96511087?v=4)

Clique na imagem ou no link para visualizar o seu avatar.

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).