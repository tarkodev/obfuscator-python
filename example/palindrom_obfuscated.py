def _obf_decode(s):
    import base64
    return base64.b64decode(s).decode('utf-8')


if False:
    _obf_decode('RGVhZCBjb2RlIGF0IG1vZHVsZSBsZXZlbA==')


class var_innfb_1:

    def var_prryb_2(var_bbzlh_3, var_xqnro_4: str) ->bool:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_3131():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        var_ujmqa_5 = _obf_decode('').join(var_qpzkz_6.lower() for
            var_qpzkz_6 in var_xqnro_4 if var_qpzkz_6.isalnum())
        return var_ujmqa_5 == var_ujmqa_5[::-1]

    def var_tdzgq_7(var_bbzlh_3, var_zqzhc_8: list) ->dict:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_5835():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        return {var_xqnro_4: var_bbzlh_3.var_prryb_2(var_xqnro_4) for
            var_xqnro_4 in var_zqzhc_8}


class var_jrxjc_9:

    def __init__(var_bbzlh_3, title: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_8540():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        var_bbzlh_3.title = title

    def var_xjdxn_10(var_bbzlh_3, var_ibick_11: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_8058():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        print(
            f"{_obf_decode('Ww==')}{var_bbzlh_3.title}{_obf_decode('XTog')}{var_ibick_11}"
            )


def var_pakor_12():
    if False:
        print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

    def unused_function_2746():
        _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
        return 42
    var_cbqlu_13 = var_innfb_1()
    var_yfbfi_14 = var_jrxjc_9(_obf_decode('UGFsaW5kcm9tZSBDaGVja2Vy'))
    var_zqzhc_8 = [_obf_decode('cmFkYXI='), _obf_decode('aGVsbG8='),
        _obf_decode('QSBtYW4gYSBwbGFuIGEgY2FuYWwgUGFuYW1h'), _obf_decode(
        'MTIzMjE='), _obf_decode('UHl0aG9u'), _obf_decode('a2F5YWs='),
        _obf_decode('eWFrYWs=')]
    var_xhppx_15 = var_cbqlu_13.var_tdzgq_7(var_zqzhc_8)
    for var_xqnro_4, var_oqdfh_16 in var_xhppx_15.items():
        var_nsfef_17 = _obf_decode('aXM=') if var_oqdfh_16 else _obf_decode(
            'aXMgbm90')
        var_yfbfi_14.var_xjdxn_10(
            f"{_obf_decode('Jw==')}{var_xqnro_4}{_obf_decode('JyA=')}{var_nsfef_17}{_obf_decode('IGEgcGFsaW5kcm9tZS4=')}"
            )


if __name__ == _obf_decode('X19tYWluX18='):
    var_pakor_12()
