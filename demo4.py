def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'application/json')])
    return [b'{"name":"my_name","age":23,"year":2018,"nickName":"zhejiang"}']