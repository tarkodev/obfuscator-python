def _obf_decode(s):
    import base64
    return base64.b64decode(s).decode('utf-8')


if False:
    _obf_decode('RGVhZCBjb2RlIGF0IG1vZHVsZSBsZXZlbA==')


class var_tckls_1:

    def var_aqkdk_2(var_nkmbu_3, var_ijfkh_4: str) ->bool:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_2924():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        var_erlbk_5 = _obf_decode('').join(var_jcyif_6.lower() for
            var_jcyif_6 in var_ijfkh_4 if var_jcyif_6.isalnum())
        return var_erlbk_5 == var_erlbk_5[::-1]

    def var_qdaxf_7(var_nkmbu_3, var_fessn_8: list) ->dict:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_1298():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        return {var_ijfkh_4: var_nkmbu_3.var_aqkdk_2(var_ijfkh_4) for
            var_ijfkh_4 in var_fessn_8}


class var_vnppo_9:

    def __init__(var_nkmbu_3, title: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_7214():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        var_nkmbu_3.title = title

    def var_aeqhb_10(var_nkmbu_3, var_atojy_11: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_7821():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        print(
            f"{_obf_decode('Ww==')}{var_nkmbu_3.title}{_obf_decode('XTog')}{var_atojy_11}"
            )


def var_lourf_12():
    if False:
        print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

    def unused_function_3318():
        _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
        return 42
    var_cbfhj_13 = var_tckls_1()
    var_jykbt_14 = var_vnppo_9(_obf_decode('UGFsaW5kcm9tZSBDaGVja2Vy'))
    var_fessn_8 = [_obf_decode('cmFkYXI='), _obf_decode('aGVsbG8='),
        _obf_decode('QSBtYW4gYSBwbGFuIGEgY2FuYWwgUGFuYW1h'), _obf_decode(
        'MTIzMjE='), _obf_decode('UHl0aG9u'), _obf_decode('a2F5YWs='),
        _obf_decode('eWFrYWs=')]
    var_kbedl_15 = var_cbfhj_13.var_qdaxf_7(var_fessn_8)
    for var_ijfkh_4, var_nwcee_16 in var_kbedl_15.items():
        var_ylfwb_17 = _obf_decode('aXM=') if var_nwcee_16 else _obf_decode(
            'aXMgbm90')
        var_jykbt_14.var_aeqhb_10(
            f"{_obf_decode('Jw==')}{var_ijfkh_4}{_obf_decode('JyA=')}{var_ylfwb_17}{_obf_decode('IGEgcGFsaW5kcm9tZS4=')}"
            )


if __name__ == _obf_decode('X19tYWluX18='):
    var_lourf_12()
