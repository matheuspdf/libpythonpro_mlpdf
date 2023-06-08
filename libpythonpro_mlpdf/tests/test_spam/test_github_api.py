from unittest.mock import Mock

from libpythonpro_mlpdf import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        "login": "matheuspdf", "id": 96511087,
        "avatar_url": "https://avatars.githubusercontent.com/u/96511087?v=4",
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('matheuspdf')
    assert 'https://avatars.githubusercontent.com/u/96511087?v=4' == url
