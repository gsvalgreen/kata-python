import pytest
import requests

from calculadora import calcular


def test_deve_retornar_zero():
    assert calcular("") == 0


def test_deve_retornar_tres():
    assert calcular("3") == 3


def test_deve_retornar_cinco():
    assert calcular("2,3") == 5


def test_deve_retornar_nove():
    assert calcular("2,3,4") == 9


def test_deve_retornar_tres_tambem():
    assert calcular("1\n2") == 3


def test_deve_retornar_seis():
    assert calcular("1\n2,3") == 6


def test_deve_lancar_excecao_numero_negativo():
    with pytest.raises(Exception) as e_info:
        calcular("2,-1")
    assert str(e_info.value) == "numeros negativos nao permitidos: -1"


def test_deve_lancar_excecao_mais_numeros_negativo():
    with pytest.raises(Exception) as e_info:
        calcular("2,-1,-2")
    assert str(e_info.value) == "numeros negativos nao permitidos: -1, -2"


def test_deve_aceitar_ponto_e_virgula_e_espaco():
    assert calcular("3;4 5") == 12


def test_deve_dizer_ola_e_retornar_200():
    response = requests.get('http://192.168.15.9:81/')
    assert response.text == "Ola Mundo!"


def test_deve_calcular_e_retornar_200():
    response = requests.get('http://192.168.15.9:81/calcular/1,2,3')
    assert response.text == "calculei: 6"


def test_deve_calcular_com_json_e_retornar_200():
    entrada = {
        "texto": "1,2,3,4"
    }

    response = requests.post('http://192.168.15.9:81/calcular/', json=entrada)

    resposta = response.json()
    assert resposta == {
        "calculei": 10
    }
    assert response.status_code == 200


def test_deve_dar_erro_quando_houver_negativo():
    entrada = {
        "texto": "1,2,3,-4"
    }

    response = requests.post('http://192.168.15.9:81/calcular/', json=entrada)

    assert response.status_code == 500
