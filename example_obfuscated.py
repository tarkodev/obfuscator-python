def _obf_decode(s):
    import base64
    return base64.b64decode(s).decode('utf-8')


if False:
    _obf_decode('RGVhZCBjb2RlIGF0IG1vZHVsZSBsZXZlbA==')


class var_wwavt_1:

    def var_oriag_2(var_qkzxh_3, var_qnsid_4: int) ->int:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_2546():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        if var_qnsid_4 < 2:
            return var_qnsid_4
        return var_qkzxh_3.var_oriag_2(var_qnsid_4 - 1
            ) + var_qkzxh_3.var_oriag_2(var_qnsid_4 - 2)

    def var_nbjom_5(var_qkzxh_3, var_aidku_6: int) ->list:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_1507():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        return [var_qkzxh_3.var_oriag_2(var_tykrp_7) for var_tykrp_7 in
            range(var_aidku_6)]


class var_nxivt_8:

    def __init__(var_qkzxh_3, var_zjhmk_9: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_1017():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        var_qkzxh_3.var_zjhmk_9 = var_zjhmk_9

    def var_bkpzk_10(var_qkzxh_3, var_odqae_11: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_8330():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        print(
            f"{_obf_decode('Ww==')}{var_qkzxh_3.var_zjhmk_9}{_obf_decode('XTog')}{var_odqae_11}"
            )


def var_rrsnz_12():
    if False:
        print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

    def unused_function_6923():
        _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
        return 42
    var_xdfug_13 = var_wwavt_1()
    var_jgmks_14 = var_nxivt_8(_obf_decode('Rmlib25hY2NpIFByb2dyYW0='))
    var_aidku_6 = 10
    var_kacah_15 = var_xdfug_13.var_nbjom_5(var_aidku_6)
    var_jgmks_14.var_bkpzk_10(
        f"{_obf_decode('Rmlib25hY2NpIHNlcXVlbmNlIG9mIGxlbmd0aCA=')}{var_aidku_6}{_obf_decode('ID0+IA==')}{var_kacah_15}"
        )


if __name__ == _obf_decode('X19tYWluX18='):
    var_rrsnz_12()
