def _obf_decode(s):
    import base64
    return base64.b64decode(s).decode('utf-8')


if False:
    _obf_decode('RGVhZCBjb2RlIGF0IG1vZHVsZSBsZXZlbA==')


class var_bvdwe_1:

    def var_xrkny_2(var_letvl_3, var_hsiaz_4: str) ->bool:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_6826():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        var_glchv_5 = _obf_decode('').join(var_qskyd_6.lower() for
            var_qskyd_6 in var_hsiaz_4 if var_qskyd_6.isalnum())
        return var_glchv_5 == var_glchv_5[::-1]

    def var_swjhd_7(var_letvl_3, var_tqkbf_8: list) ->dict:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_6774():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        return {var_hsiaz_4: var_letvl_3.var_xrkny_2(var_hsiaz_4) for
            var_hsiaz_4 in var_tqkbf_8}


class var_psyjs_9:

    def __init__(var_letvl_3, title: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_6774():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        var_letvl_3.title = title

    def var_ouhzj_10(var_letvl_3, var_ipzii_11: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_3533():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        print(
            f"{_obf_decode('Ww==')}{var_letvl_3.title}{_obf_decode('XTog')}{var_ipzii_11}"
            )


def var_gjprq_12():
    if False:
        print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

    def unused_function_7627():
        _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
        return 42
    var_zpinl_13 = var_bvdwe_1()
    var_pnzkr_14 = var_psyjs_9(_obf_decode('UGFsaW5kcm9tZSBDaGVja2Vy'))
    var_tqkbf_8 = [_obf_decode('cmFkYXI='), _obf_decode('aGVsbG8='),
        _obf_decode('QSBtYW4gYSBwbGFuIGEgY2FuYWwgUGFuYW1h'), _obf_decode(
        'MTIzMjE='), _obf_decode('UHl0aG9u'), _obf_decode('a2F5YWs='),
        _obf_decode('eWFrYWs=')]
    var_tzprr_15 = var_zpinl_13.var_swjhd_7(var_tqkbf_8)
    for var_hsiaz_4, var_qrdlp_16 in var_tzprr_15.items():
        var_gulhk_17 = _obf_decode('aXM=') if var_qrdlp_16 else _obf_decode(
            'aXMgbm90')
        var_pnzkr_14.var_ouhzj_10(
            f"{_obf_decode('Jw==')}{var_hsiaz_4}{_obf_decode('JyA=')}{var_gulhk_17}{_obf_decode('IGEgcGFsaW5kcm9tZS4=')}"
            )


if __name__ == _obf_decode('X19tYWluX18='):
    var_gjprq_12()
