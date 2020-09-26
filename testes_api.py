import requests


class TestSolicitacoes:
    headers = {'Authorization': 'Token 342c2544c0ed2481b318eac1fde01c6a0f625ed2'}
    url_base_solicitacoes = 'http://localhost:8000/api/v2/solicitacoes/'

    def test_get_solicitacoes(self):
        solicitacoes = requests.get(url=self.url_base_solicitacoes, headers=self.headers)

        assert solicitacoes.status_code == 200

    def test_get_solicitacao(self):
        solicitacao = requests.get(url=f'{self.url_base_solicitacoes}1/', headers=self.headers)

        assert solicitacao.status_code == 200

    def test_post_solicitacao(self):
        novo = {
            "nome": "Testador",
            "renda": 3500,
            "score": "",
            "limit": ""

        }
        resposta = requests.post(url=self.url_base_solicitacoes, headers=self.headers, data=novo)

        assert resposta.status_code == 201

    def test_delete_solicitacao(self):
        resposta = requests.delete(url=f'{self.url_base_solicitacoes}/1', headers = self.headers)

        assert resposta.status_code == 204