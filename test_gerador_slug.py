# test_gerador_slug.py
import pytest
from gerador_slug import slugify

def test_string_simples():
    assert slugify("Hello World") == "hello-world"

def test_com_acentos():
    assert slugify("Criação de código e teste") == "criacao-de-codigo-e-teste"

def test_com_caracteres_especiais():
    assert slugify("Meu Post Incrível! (Novo)") == "meu-post-incrivel-novo"

def test_com_espacos_multiplos():
    assert slugify("Um   título  com    muitos espaços") == "um-titulo-com-muitos-espacos"

def test_com_hifens_no_texto():
    assert slugify("Testando um-hífen-no-meio") == "testando-um-hifen-no-meio"

def test_string_vazia():
    assert slugify("") == ""

def test_com_numeros():
    assert slugify("Meu post número 1 de 2025") == "meu-post-numero-1-de-2025"

def test_apenas_caracteres_especiais():
    assert slugify("!!! @#$%¨&*() ???") == ""

def test_hifens_inicio_e_fim():
    assert slugify("---Meu Post---") == "meu-post"