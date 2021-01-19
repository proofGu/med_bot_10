import requests
TG_API = 'https://api.telegram.org/bot1547796385:AAFFx559T0VHzkETZ0e5tTDawN2a9ozFAO4/'
last_update_id = 0

while True:
    result = requests.get(TG_API + 'getUpdates', params={'offset':last_update_id + 1})
    data = result.json()
    for update in data['result']:
        last_update_id = update['update_id']
        chat_id = update['message']['chat']['id']
        name = update['message']['from']['first_name']
        user_input = update['message']['text']
        print(name, '->', user_input)

        if user_input[0] == 'Q':
            x = float(user_input[1:]) * 18
            answer = f'Ответ = {x}'
            send_result = requests.get(TG_API + 'sendMessage', params={'chat_id': chat_id, 'text': answer})
            continue
        elif user_input[0] == 'P':
            x = float(user_input[1:]) / 18
            answer = f'Ответ = {x}'
            send_result = requests.get(TG_API + 'sendMessage', params={'chat_id': chat_id, 'text': answer})
            continue
        else:
            greeting = 'Для того, чтобы перевести ммоль/л в мг/дл: введите Q"число" \nДля того, чтобы перевести мг/дл в ммоль/л: введите P"число"'
            send_result = requests.get(TG_API + 'sendMessage', params={'chat_id': chat_id, 'text': greeting})

        # answer = name
