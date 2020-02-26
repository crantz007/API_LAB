import unittest
from unittest import TestCase
from unittest.mock import patch
import bitcoin


class TestBitCoin(TestCase):
    @patch('bitcoin.get_bitcoin_rate')
    def test_get_price_in_us_dollar(self, mock_rates):
        mock_rate = 12345.67
        api_response = {'rate': mock_rate}
        mock_rates.side_effect = [api_response]
        bitcoins = 10
        formatting = bitcoins * mock_rate
        conversion = bitcoin.convert(mock_rate, bitcoins)
        self.assertEqual(formatting, conversion)


if __name__ == '__main__':
    unittest.main()
