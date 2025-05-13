def _obf_decode(s):
    import base64
    return base64.b64decode(s).decode('utf-8')


if False:
    _obf_decode('RGVhZCBjb2RlIGF0IG1vZHVsZSBsZXZlbA==')


class var_ptkiv_1:

    def var_ofbgc_2(var_ahozc_3, var_iiryn_4: str) ->bool:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_4275():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        var_ralay_5 = _obf_decode('').join(var_xfrqr_6.lower() for
            var_xfrqr_6 in var_iiryn_4 if var_xfrqr_6.isalnum())
        return var_ralay_5 == var_ralay_5[::-1]

    def var_mdqsz_7(var_ahozc_3, var_lapcn_8: list) ->dict:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_1426():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        return {var_iiryn_4: var_ahozc_3.var_ofbgc_2(var_iiryn_4) for
            var_iiryn_4 in var_lapcn_8}


class var_nfpii_9:

    def __init__(var_ahozc_3, title: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_8105():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        var_ahozc_3.title = title

    def var_fpjlj_10(var_ahozc_3, var_zzybb_11: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_7096():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        print(
            f"{_obf_decode('Ww==')}{var_ahozc_3.title}{_obf_decode('XTog')}{var_zzybb_11}"
            )


def var_pnnwl_12():
    if False:
        print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

    def unused_function_5085():
        _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
        return 42
    var_wywbf_13 = var_ptkiv_1()
    var_sljfc_14 = var_nfpii_9(_obf_decode('UGFsaW5kcm9tZSBDaGVja2Vy'))
    var_lapcn_8 = [_obf_decode('cmFkYXI='), _obf_decode('aGVsbG8='),
        _obf_decode('QSBtYW4gYSBwbGFuIGEgY2FuYWwgUGFuYW1h'), _obf_decode(
        'MTIzMjE='), _obf_decode('UHl0aG9u'), _obf_decode('a2F5YWs='),
        _obf_decode('eWFrYWs=')]
    var_cruip_15 = var_wywbf_13.var_mdqsz_7(var_lapcn_8)
    for var_iiryn_4, var_czcie_16 in var_cruip_15.items():
        var_twxxr_17 = _obf_decode('aXM=') if var_czcie_16 else _obf_decode(
            'aXMgbm90')
        var_sljfc_14.var_fpjlj_10(
            f"{_obf_decode('Jw==')}{var_iiryn_4}{_obf_decode('JyA=')}{var_twxxr_17}{_obf_decode('IGEgcGFsaW5kcm9tZS4=')}"
            )


if __name__ == _obf_decode('X19tYWluX18='):
    var_pnnwl_12()
