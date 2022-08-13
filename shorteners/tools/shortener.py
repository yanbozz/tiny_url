from random import randint


def shorten(domain, protocol='http', reverse=True) -> str:
    """
    return: generate a short url that has a seven-chars length code as its path
    using alphabet(both uppercase and lowercase) and numbers
    param: protocol: protocol used for current url, default 'http'
    param: reverse: return reversed url or not , default True
    """
    code = ''
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for _ in range(7):
        code += chars[randint(0, 61)]

    res = '{protocol}://{domain}/{code}'.format(protocol=protocol, domain=domain, code=code)
    if reverse:
        return res[::-1]
    return res


def get_url_by_code(code, http='http') -> str:
    return '{http}://127.0.0.1:8000/{code}'.format(http=http, code=code)


