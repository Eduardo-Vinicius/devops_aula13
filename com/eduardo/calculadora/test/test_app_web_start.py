# pylint: disable=invalid-name

from com.eduardo.calculadora import app_web_start

def test_root_status():
    '''
    Testa a rota do root
    '''
    instancia_app = app_web_start.app.test_client()
    response = instancia_app.get('/')
    assert response.status_code == 200, 'Deveria existir essa rota'

def test_root_url():
    '''
    Função que testa a URL do root
    '''
    instancia_app = app_web_start.app.test_client()
    response = instancia_app.get('/')
    assert response.data.decode('utf-8') == 'Index Page!', 'Deveria ser Index Page'

