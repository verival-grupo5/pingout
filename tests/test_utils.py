import pingout.utils
import unittest.mock as mock

import pandas

JSON = '''
{
  "pingout": {
    "pings": [
      {
        "count": 1, 
        "date": "Fri, 02 Nov 2018 19:29:00 GMT"
      }
    ], 
    "uuid": "171bc80181884c23a6d27ccf8193815f"
  }
}
'''


def test_validate_valid_uuid():
    returned_data = pingout.utils.validate_uuid('171bc80181884c23a6d27ccf8193815f')

    assert returned_data == True

# case where the informed UUID is invalid
def test_validate_invalid_uuid():
    returned_data = pingout.utils.validate_uuid('')

    assert returned_data == False

def test_convert_json_to_csv():
    with mock.patch('pingout.utils.pandas') as mock_pandas:
        # mock da conversao do json para csv
        mock_pandas = mock.Mock(wraps=pandas)

        pingout.utils.from_json_to_csv(JSON, 'arquivo')