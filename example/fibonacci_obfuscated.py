def _obf_decode(s):
    import base64
    return base64.b64decode(s).decode('utf-8')


if False:
    _obf_decode('RGVhZCBjb2RlIGF0IG1vZHVsZSBsZXZlbA==')


class var_vcesi_1:

    def var_pzlsd_2(var_wriek_3, var_warcd_4: int) ->int:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_8034():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        if var_warcd_4 < 2:
            return var_warcd_4
        return var_wriek_3.var_pzlsd_2(var_warcd_4 - 1
            ) + var_wriek_3.var_pzlsd_2(var_warcd_4 - 2)

    def var_rxlbr_5(var_wriek_3, var_xersm_6: int) ->list:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_1327():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        return [var_wriek_3.var_pzlsd_2(var_ctqmj_7) for var_ctqmj_7 in
            range(var_xersm_6)]


class var_bxerh_8:

    def __init__(var_wriek_3, title: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_6913():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        var_wriek_3.title = title

    def var_xxpwe_9(var_wriek_3, var_ksfaz_10: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_2130():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        print(
            f"{_obf_decode('Ww==')}{var_wriek_3.title}{_obf_decode('XTog')}{var_ksfaz_10}"
            )


def var_vhrmw_11():
    if False:
        print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

    def unused_function_2399():
        _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
        return 42
    var_ynkbr_12 = var_vcesi_1()
    var_zwyct_13 = var_bxerh_8(_obf_decode('Rmlib25hY2NpIFByb2dyYW0='))
    var_xersm_6 = 35
    var_wyqnx_14 = var_ynkbr_12.var_rxlbr_5(var_xersm_6)
    var_zwyct_13.var_xxpwe_9(
        f"{_obf_decode('Rmlib25hY2NpIHNlcXVlbmNlIG9mIGxlbmd0aCA=')}{var_xersm_6}{_obf_decode('ID0+IA==')}{var_wyqnx_14}"
        )


if __name__ == _obf_decode('X19tYWluX18='):
    var_vhrmw_11()
