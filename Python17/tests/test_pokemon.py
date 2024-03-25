import requests
import pytest
host = 'https://api.pokemonbattle.me:9104'
token = 'e111d7746f6527e1f02f32d483fc7d88'

def test_status():
    response = requests.get(f'{host}/trainers', params={'trainer_id' : 4689})
    assert response.status_code == 200

def test_answer():
    response = requests.get(f'{host}/trainers', params={'trainer_id' : 4689})
    assert response.json()['trainer_name'] == 'Алек'