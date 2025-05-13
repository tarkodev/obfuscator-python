def _obf_decode(s):
    import base64
    return base64.b64decode(s).decode('utf-8')


if False:
    _obf_decode('RGVhZCBjb2RlIGF0IG1vZHVsZSBsZXZlbA==')


class var_qisjc_1:

    def var_wwxfd_2(var_apfsa_3, var_qzwkb_4: int) ->int:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_9580():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        if var_qzwkb_4 < 2:
            return var_qzwkb_4
        return var_apfsa_3.var_wwxfd_2(var_qzwkb_4 - 1
            ) + var_apfsa_3.var_wwxfd_2(var_qzwkb_4 - 2)

    def var_ovyzn_5(var_apfsa_3, var_kblth_6: int) ->list:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_3730():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        return [var_apfsa_3.var_wwxfd_2(var_buygy_7) for var_buygy_7 in
            range(var_kblth_6)]


class var_ojgqb_8:

    def __init__(var_apfsa_3, title: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_7026():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        var_apfsa_3.title = title

    def var_hfwft_9(var_apfsa_3, var_jbbxy_10: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_8216():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        print(
            f"{_obf_decode('Ww==')}{var_apfsa_3.title}{_obf_decode('XTog')}{var_jbbxy_10}"
            )


def var_fxkmj_11():
    if False:
        print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

    def unused_function_3885():
        _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
        return 42
    var_tmyen_12 = var_qisjc_1()
    var_wgtht_13 = var_ojgqb_8(_obf_decode('Rmlib25hY2NpIFByb2dyYW0='))
    var_kblth_6 = 35
    var_dozpr_14 = var_tmyen_12.var_ovyzn_5(var_kblth_6)
    var_wgtht_13.var_hfwft_9(
        f"{_obf_decode('Rmlib25hY2NpIHNlcXVlbmNlIG9mIGxlbmd0aCA=')}{var_kblth_6}{_obf_decode('ID0+IA==')}{var_dozpr_14}"
        )


if __name__ == _obf_decode('X19tYWluX18='):
    var_fxkmj_11()
