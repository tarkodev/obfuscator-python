def _obf_decode(s):
    import base64
    return base64.b64decode(s).decode('utf-8')


if False:
    _obf_decode('RGVhZCBjb2RlIGF0IG1vZHVsZSBsZXZlbA==')


class var_bzksb_1:

    def var_psppy_2(var_susxy_3, var_yqmpu_4: str) ->bool:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_7888():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        var_decev_5 = _obf_decode('').join(var_bqrjs_6.lower() for
            var_bqrjs_6 in var_yqmpu_4 if var_bqrjs_6.isalnum())
        return var_decev_5 == var_decev_5[::-1]

    def var_oqmwv_7(var_susxy_3, var_usgei_8: list) ->dict:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_1297():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        return {var_yqmpu_4: var_susxy_3.var_psppy_2(var_yqmpu_4) for
            var_yqmpu_4 in var_usgei_8}


class var_fsdox_9:

    def __init__(var_susxy_3, title: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_8443():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        var_susxy_3.title = title

    def var_ijubv_10(var_susxy_3, var_xvllh_11: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_6313():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        print(
            f"{_obf_decode('Ww==')}{var_susxy_3.title}{_obf_decode('XTog')}{var_xvllh_11}"
            )


def var_qrjqq_12():
    if False:
        print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

    def unused_function_9586():
        _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
        return 42
    var_onuvm_13 = var_bzksb_1()
    var_tothe_14 = var_fsdox_9(_obf_decode('UGFsaW5kcm9tZSBDaGVja2Vy'))
    var_usgei_8 = [_obf_decode('cmFkYXI='), _obf_decode('aGVsbG8='),
        _obf_decode('QSBtYW4gYSBwbGFuIGEgY2FuYWwgUGFuYW1h'), _obf_decode(
        'MTIzMjE='), _obf_decode('UHl0aG9u'), _obf_decode('a2F5YWs='),
        _obf_decode('eWFrYWs=')]
    var_rimav_15 = var_onuvm_13.var_oqmwv_7(var_usgei_8)
    for var_yqmpu_4, var_jthmi_16 in var_rimav_15.items():
        var_uwpqu_17 = _obf_decode('aXM=') if var_jthmi_16 else _obf_decode(
            'aXMgbm90')
        var_tothe_14.var_ijubv_10(
            f"{_obf_decode('Jw==')}{var_yqmpu_4}{_obf_decode('JyA=')}{var_uwpqu_17}{_obf_decode('IGEgcGFsaW5kcm9tZS4=')}"
            )


if __name__ == _obf_decode('X19tYWluX18='):
    var_qrjqq_12()
