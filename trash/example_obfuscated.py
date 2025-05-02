def _obf_decode(s):
    import base64
    return base64.b64decode(s).decode('utf-8')


if False:
    _obf_decode('RGVhZCBjb2RlIGF0IG1vZHVsZSBsZXZlbA==')


class var_xknxd_1:

    def var_bhbpz_2(var_tsfqu_3, var_chxjb_4: int) ->int:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_6359():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        if var_chxjb_4 < 2:
            return var_chxjb_4
        return var_tsfqu_3.var_bhbpz_2(var_chxjb_4 - 1
            ) + var_tsfqu_3.var_bhbpz_2(var_chxjb_4 - 2)

    def var_adsvs_5(var_tsfqu_3, var_etqcm_6: int) ->list:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_2067():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        return [var_tsfqu_3.var_bhbpz_2(var_pwgym_7) for var_pwgym_7 in
            range(var_etqcm_6)]


class var_pmvnf_8:

    def __init__(var_tsfqu_3, var_jlzxf_9: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_7429():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        var_tsfqu_3.var_jlzxf_9 = var_jlzxf_9

    def var_nkhif_10(var_tsfqu_3, var_qthex_11: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_6914():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        print(
            f"{_obf_decode('Ww==')}{var_tsfqu_3.var_jlzxf_9}{_obf_decode('XTog')}{var_qthex_11}"
            )


def var_gfqxy_12():
    if False:
        print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

    def unused_function_6708():
        _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
        return 42
    var_dkmic_13 = var_xknxd_1()
    var_klqor_14 = var_pmvnf_8(_obf_decode('Rmlib25hY2NpIFByb2dyYW0='))
    var_etqcm_6 = 10
    var_rhpmg_15 = var_dkmic_13.var_adsvs_5(var_etqcm_6)
    var_klqor_14.var_nkhif_10(
        f"{_obf_decode('Rmlib25hY2NpIHNlcXVlbmNlIG9mIGxlbmd0aCA=')}{var_etqcm_6}{_obf_decode('ID0+IA==')}{var_rhpmg_15}"
        )


if __name__ == _obf_decode('X19tYWluX18='):
    var_gfqxy_12()
