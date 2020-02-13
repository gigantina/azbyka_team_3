import coding
import decode


def main():
    print('Привет, пользователь! Мы - команда престарелых разработчиков, создавших этот проект.')
    print('Если хочешь закодировать сообщение, то пиши code, а если наоборот, то decode')
    message = input()
    if message == 'code':
        print('Отлично! Пиши сообщение на латинице:')
        print(coding.encode_to_morse(input()))
    elif message == 'decode':
        print('Пиши, американский шпион...')
        print(decode.decode_from_morse(input()))


main()
