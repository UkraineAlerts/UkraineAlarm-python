# coding: utf-8

"""
    Ukraine Alert API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0
    Contact: support@stfalcon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import UkraineAlarm
from UkraineAlarm.api.web_hook_api import WebHookApi  # noqa: E501
from UkraineAlarm.rest import ApiException


class TestWebHookApi(unittest.TestCase):
    """WebHookApi unit test stubs"""

    def setUp(self):
        self.api = WebHookApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v3_webhook_delete(self):
        """Test case for api_v3_webhook_delete

        Відписка на WebHook про нові сирени та їх відбій  # noqa: E501
        """
        pass

    def test_api_v3_webhook_patch(self):
        """Test case for api_v3_webhook_patch

        Оновлення WebHook посилання про нові сирени та їх відбій  # noqa: E501
        """
        pass

    def test_api_v3_webhook_post(self):
        """Test case for api_v3_webhook_post

        Підписка на WebHook про нові сирени та їх відбій. У вебхукі відпрявляється подія тривоги/відбою (приклад в відповіді \"200\")  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
