def _obf_decode(s):
    import base64
    return base64.b64decode(s).decode('utf-8')


if False:
    _obf_decode('RGVhZCBjb2RlIGF0IG1vZHVsZSBsZXZlbA==')


class var_lqxme_1:

    def var_cqcel_2(var_vsmvt_3, var_otcnt_4: int) ->int:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_9576():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        if var_otcnt_4 < 2:
            return var_otcnt_4
        return var_vsmvt_3.var_cqcel_2(var_otcnt_4 - 1
            ) + var_vsmvt_3.var_cqcel_2(var_otcnt_4 - 2)

    def var_srixs_5(var_vsmvt_3, var_ycvlu_6: int) ->list:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_5791():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        return [var_vsmvt_3.var_cqcel_2(var_nfous_7) for var_nfous_7 in
            range(var_ycvlu_6)]


class var_fteqw_8:

    def __init__(var_vsmvt_3, title: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_4525():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        var_vsmvt_3.title = title

    def var_yaald_9(var_vsmvt_3, var_waerk_10: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_4915():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        print(
            f"{_obf_decode('Ww==')}{var_vsmvt_3.title}{_obf_decode('XTog')}{var_waerk_10}"
            )


def var_albdr_11():
    if False:
        print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

    def unused_function_8536():
        _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
        return 42
    var_xdrrw_12 = var_lqxme_1()
    var_mawkd_13 = var_fteqw_8(_obf_decode('Rmlib25hY2NpIFByb2dyYW0='))
    var_ycvlu_6 = 35
    var_zhslk_14 = var_xdrrw_12.var_srixs_5(var_ycvlu_6)
    var_mawkd_13.var_yaald_9(
        f"{_obf_decode('Rmlib25hY2NpIHNlcXVlbmNlIG9mIGxlbmd0aCA=')}{var_ycvlu_6}{_obf_decode('ID0+IA==')}{var_zhslk_14}"
        )


if __name__ == _obf_decode('X19tYWluX18='):
    var_albdr_11()
