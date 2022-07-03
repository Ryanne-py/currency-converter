import requests
from bs4 import BeautifulSoup
import lxml


class CurrencyNameError(Exception):
    pass


class Conversion:
    """
    parser currency converter in site https://minfin.com.ua
        """

    def __init__(self):
        pass

    def conversion(self, start_currency: str,
                   quantity_currency: int,
                   end_currency: str) -> float:
        """
        input:(str(start_currency), int(quantity), str(end_currency))
        output:final quantity
            """

        try:
            start_currency = start_currency.lower()
            end_currency = end_currency.lower()

            url = f'https://minfin.com.ua/ua/currency/converter/' \
                  f'{quantity_currency}-{start_currency}-to-{end_currency}/' \
                  f'?converter-type=auction'

            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            result = soup.find_all('input', class_='sc-1xh0v1v-1 jwqFnq')

            return result[1].get('value')

        except AttributeError:
            raise TypeError('Wrong data types in passed arguments')

        except IndexError:
            raise CurrencyNameError('Wrong currency name')
