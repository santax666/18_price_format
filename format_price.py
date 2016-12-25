import argparse
import re


def create_parser():
    parser = argparse.ArgumentParser(usage='%(prog)s [аргументы]',
                                     description='Форматирование цены'
                                                 ' с помощью %(prog)s')
    parser.add_argument('-p', '--price', help='Цена товара')
    return parser


def has_letter(value):
    return bool(re.search(r'[А-Яа-яA-Za-zЁё]', value))


def has_spec_char(value):
    return bool(re.search(r'[^А-Яа-яA-Za-zЁё0-9.,]', value))


def is_negative_number(price):
    return bool(price[0] == '-')


def get_whole_and_fractional(price):
    whole_str, fract_str = '{:,.2f}'.format(price).split('.')
    return whole_str.replace(',', ' '), fract_str


def format_price(price):
    if has_letter(price):
        return 'Цена содержит буквы!', None
    elif is_negative_number(price):
        return 'Цена отрицательная!', None
    elif has_spec_char(price):
        return 'Цена содержит спецсимволы!', None
    else:
        price = price.replace(',', '.')
        if price.count('.') == 1:
            return get_whole_and_fractional(float(price))
        else:
            return 'Цена некорректная!', None


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    price = namespace.price
    if price is None:
        price = input('Введите цену товара для форматирования: ')
    price_formated = format_price(price)
    print('.'.join(filter(None, price_formated)))
