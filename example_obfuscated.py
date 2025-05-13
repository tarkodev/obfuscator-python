def _obf_decode(s):
    import base64
    return base64.b64decode(s).decode('utf-8')


if False:
    _obf_decode('RGVhZCBjb2RlIGF0IG1vZHVsZSBsZXZlbA==')


class var_mnmyf_1:

    def var_pbrat_2(var_prsti_3, var_ahgti_4: str) ->bool:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_4655():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        var_tyoba_5 = _obf_decode('').join(var_kjvxc_6.lower() for
            var_kjvxc_6 in var_ahgti_4 if var_kjvxc_6.isalnum())
        return var_tyoba_5 == var_tyoba_5[::-1]

    def var_sbzzq_7(var_prsti_3, var_oqrtc_8: list) ->dict:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_1682():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        return {var_ahgti_4: var_prsti_3.var_pbrat_2(var_ahgti_4) for
            var_ahgti_4 in var_oqrtc_8}


class var_fnslh_9:

    def __init__(var_prsti_3, title: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_2826():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        var_prsti_3.title = title

    def var_perra_10(var_prsti_3, var_hkhox_11: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_6122():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        print(
            f"{_obf_decode('Ww==')}{var_prsti_3.title}{_obf_decode('XTog')}{var_hkhox_11}"
            )


def var_jlhem_12():
    if False:
        print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

    def unused_function_7462():
        _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
        return 42
    var_wsfkg_13 = var_mnmyf_1()
    var_sftxo_14 = var_fnslh_9(_obf_decode('UGFsaW5kcm9tZSBDaGVja2Vy'))
    var_oqrtc_8 = [_obf_decode('cmFkYXI='), _obf_decode('aGVsbG8='),
        _obf_decode('QSBtYW4gYSBwbGFuIGEgY2FuYWwgUGFuYW1h'), _obf_decode(
        'MTIzMjE='), _obf_decode('UHl0aG9u'), _obf_decode('a2F5YWs='),
        _obf_decode('eWFrYWs=')]
    var_wrxzk_15 = var_wsfkg_13.var_sbzzq_7(var_oqrtc_8)
    for var_ahgti_4, var_azrlw_16 in var_wrxzk_15.items():
        var_ikhvv_17 = _obf_decode('aXM=') if var_azrlw_16 else _obf_decode(
            'aXMgbm90')
        var_sftxo_14.var_perra_10(
            f"{_obf_decode('Jw==')}{var_ahgti_4}{_obf_decode('JyA=')}{var_ikhvv_17}{_obf_decode('IGEgcGFsaW5kcm9tZS4=')}"
            )


if __name__ == _obf_decode('X19tYWluX18='):
    var_jlhem_12()
