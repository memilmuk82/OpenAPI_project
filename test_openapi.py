import os
import unittest
from unittest.mock import Mock, patch

from test import API_URL, get_service_key, request_path


class OpenApiTestCase(unittest.TestCase):
    def test_missing_service_key_is_rejected(self):
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaisesRegex(RuntimeError, 'SEOUL_OPENAPI_SERVICE_KEY'):
                get_service_key()

    def test_request_uses_timeout_and_coordinates(self):
        response = Mock()
        session = Mock()
        session.get.return_value = response

        result = request_path('test-value', session=session)

        self.assertIs(result, response)
        session.get.assert_called_once()
        url, = session.get.call_args.args
        self.assertEqual(url, API_URL)
        self.assertEqual(session.get.call_args.kwargs['timeout'], 30)
        self.assertIn('startX', session.get.call_args.kwargs['params'])
        response.raise_for_status.assert_called_once_with()


if __name__ == '__main__':
    unittest.main()
