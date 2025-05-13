def _obf_decode(s):
    import base64
    return base64.b64decode(s).decode('utf-8')


if False:
    _obf_decode('RGVhZCBjb2RlIGF0IG1vZHVsZSBsZXZlbA==')


class var_ostat_1:

    def var_ecgqz_2(var_iuwkp_3, var_vugyf_4: str) ->bool:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_7036():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        var_mrztp_5 = _obf_decode('').join(var_wsugu_6.lower() for
            var_wsugu_6 in var_vugyf_4 if var_wsugu_6.isalnum())
        return var_mrztp_5 == var_mrztp_5[::-1]

    def var_uryuy_7(var_iuwkp_3, var_qkbpw_8: list) ->dict:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_1528():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        return {var_vugyf_4: var_iuwkp_3.var_ecgqz_2(var_vugyf_4) for
            var_vugyf_4 in var_qkbpw_8}


class var_qupkl_9:

    def __init__(var_iuwkp_3, title: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_9984():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        var_iuwkp_3.title = title

    def var_prssg_10(var_iuwkp_3, var_qebfm_11: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_7603():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        print(
            f"{_obf_decode('Ww==')}{var_iuwkp_3.title}{_obf_decode('XTog')}{var_qebfm_11}"
            )


def var_yfvrn_12():
    if False:
        print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

    def unused_function_7891():
        _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
        return 42
    var_axxom_13 = var_ostat_1()
    var_qgmop_14 = var_qupkl_9(_obf_decode('UGFsaW5kcm9tZSBDaGVja2Vy'))
    var_qkbpw_8 = [_obf_decode('cmFkYXI='), _obf_decode('aGVsbG8='),
        _obf_decode('QSBtYW4gYSBwbGFuIGEgY2FuYWwgUGFuYW1h'), _obf_decode(
        'MTIzMjE='), _obf_decode('UHl0aG9u'), _obf_decode('a2F5YWs='),
        _obf_decode('eWFrYWs=')]
    var_pizcc_15 = var_axxom_13.var_uryuy_7(var_qkbpw_8)
    for var_vugyf_4, var_migif_16 in var_pizcc_15.items():
        var_kzita_17 = _obf_decode('aXM=') if var_migif_16 else _obf_decode(
            'aXMgbm90')
        var_qgmop_14.var_prssg_10(
            f"{_obf_decode('Jw==')}{var_vugyf_4}{_obf_decode('JyA=')}{var_kzita_17}{_obf_decode('IGEgcGFsaW5kcm9tZS4=')}"
            )


if __name__ == _obf_decode('X19tYWluX18='):
    var_yfvrn_12()
