let messages = {
  NET_ERR_403: '403 接口请求被拒绝，请重新登录',
  NET_ERR_404: '404 接口请求不存在',
  NET_ERR_405: '405 接口请求操作类型不存在',
  NET_ERR_500: '500 服务端错误',
  NET_ERR_DEFAULT: '网络错误'
};

function rspStatusHandler(namespace, errCode) {
  let result = '';
  switch (namespace) {
    case 'NET':
      switch (errCode) {
        case 403:
          result = messages.NET_ERR_403;
          break;
        case 404:
          result = messages.NET_ERR_404;
          break;
        case 405:
          result = messages.NET_ERR_405;
          break;
        case 500:
          result = messages.NET_ERR_500;
          break;
        default:
          result = messages.NET_ERR_DEFAULT;
          break;
      }
      break;
    case 'APP':
      break;
  }
  return result;
}

export {messages, rspStatusHandler};
