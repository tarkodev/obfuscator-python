def _obf_decode(s):
    import base64
    return base64.b64decode(s).decode('utf-8')


if False:
    _obf_decode('RGVhZCBjb2RlIGF0IG1vZHVsZSBsZXZlbA==')


class var_fsgqx_1:

    def var_sbyiy_2(var_zikqm_3, var_ashjq_4: int) ->int:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_1314():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        if var_ashjq_4 < 2:
            return var_ashjq_4
        return var_zikqm_3.var_sbyiy_2(var_ashjq_4 - 1
            ) + var_zikqm_3.var_sbyiy_2(var_ashjq_4 - 2)

    def var_hyzer_5(var_zikqm_3, var_ltsxn_6: int) ->list:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_1138():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        return [var_zikqm_3.var_sbyiy_2(var_zhdsz_7) for var_zhdsz_7 in
            range(var_ltsxn_6)]


class var_qfykn_8:

    def __init__(var_zikqm_3, title: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_7790():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        var_zikqm_3.title = title

    def var_bpvdy_9(var_zikqm_3, var_virnn_10: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_7850():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        print(
            f"{_obf_decode('Ww==')}{var_zikqm_3.title}{_obf_decode('XTog')}{var_virnn_10}"
            )


def var_ynuik_11():
    if False:
        print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

    def unused_function_8912():
        _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
        return 42
    var_dqdly_12 = var_fsgqx_1()
    var_ufcwg_13 = var_qfykn_8(_obf_decode('Rmlib25hY2NpIFByb2dyYW0='))
    var_ltsxn_6 = 35
    var_pmcrk_14 = var_dqdly_12.var_hyzer_5(var_ltsxn_6)
    var_ufcwg_13.var_bpvdy_9(
        f"{_obf_decode('Rmlib25hY2NpIHNlcXVlbmNlIG9mIGxlbmd0aCA=')}{var_ltsxn_6}{_obf_decode('ID0+IA==')}{var_pmcrk_14}"
        )


if __name__ == _obf_decode('X19tYWluX18='):
    var_ynuik_11()
