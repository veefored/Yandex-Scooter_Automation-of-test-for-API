# Данила Ерофеев, 11-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import requests

def test_get_track_name():
    response = sender_stand_request.get_new_order_track("body")
    assert response.status_code == 200
