def _obf_decode(s):
    import base64
    return base64.b64decode(s).decode('utf-8')


if False:
    _obf_decode('RGVhZCBjb2RlIGF0IG1vZHVsZSBsZXZlbA==')


class var_mzhok_1:

    def var_svdmh_2(var_anseh_3, var_hrapt_4: int) ->int:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_4434():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        if var_hrapt_4 < 2:
            return var_hrapt_4
        return var_anseh_3.var_svdmh_2(var_hrapt_4 - 1
            ) + var_anseh_3.var_svdmh_2(var_hrapt_4 - 2)

    def var_qjwwb_5(var_anseh_3, var_yfqhw_6: int) ->list:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_4723():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        return [var_anseh_3.var_svdmh_2(var_vkqjm_7) for var_vkqjm_7 in
            range(var_yfqhw_6)]


class var_baqtd_8:

    def __init__(var_anseh_3, title: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_8763():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        var_anseh_3.title = title

    def var_cdawp_9(var_anseh_3, var_wkxyg_10: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_1619():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        print(
            f"{_obf_decode('Ww==')}{var_anseh_3.title}{_obf_decode('XTog')}{var_wkxyg_10}"
            )


def var_mypqv_11():
    if False:
        print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

    def unused_function_5115():
        _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
        return 42
    var_jfqeu_12 = var_mzhok_1()
    var_uzxfx_13 = var_baqtd_8(_obf_decode('Rmlib25hY2NpIFByb2dyYW0='))
    var_yfqhw_6 = 35
    var_tfvkd_14 = var_jfqeu_12.var_qjwwb_5(var_yfqhw_6)
    var_uzxfx_13.var_cdawp_9(
        f"{_obf_decode('Rmlib25hY2NpIHNlcXVlbmNlIG9mIGxlbmd0aCA=')}{var_yfqhw_6}{_obf_decode('ID0+IA==')}{var_tfvkd_14}"
        )


if __name__ == _obf_decode('X19tYWluX18='):
    var_mypqv_11()
