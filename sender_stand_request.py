import configuration
import requests
import data

# Создать новый заказ
def post_new_order (body):
    return requests.post(configuration.URL_SERVICE + configuration.GET_ORDER_TRACK,
                         json=data.user_body)
response = post_new_order (data.user_body);

# Сохранить № трэка из заказа
def get_track ():
    track_body = create_new_order.json()
    data.order_body["track"] = str(response.json())

 # Поличить данные о заказе по трэку
def get_new_order_track (body):
     return requests.get (configuration.URL_SERVICE + configuration.GET_ORDER_TRACK)
