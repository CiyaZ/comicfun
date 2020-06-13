from rest_framework.response import Response


class APIResponse(Response):
    """定制Response"""

    def __init__(self, data=None, api_code='0', api_msg='操作成功',
                 status=None, template_name=None, headers=None,
                 exception=False, content_type=None):
        api_data = {
            'rspCode': api_code,
            'rspMsg': api_msg,
            'data': data
        }
        super().__init__(api_data, status,
                         template_name, headers,
                         exception, content_type)

    @staticmethod
    def success(data=None, status=None, template_name=None, headers=None,
                exception=False, content_type=None):
        return APIResponse(data, '0', '操作成功', status, template_name,
                           headers, exception,
                           content_type)

    @staticmethod
    def failure(data=None, api_code='5000', api_msg='操作失败',
                status=None, template_name=None, headers=None,
                exception=False, content_type=None):
        return APIResponse(data, api_code, api_msg,
                           status, template_name,
                           headers, exception,
                           content_type)
