def _obf_decode(s):
    import base64
    return base64.b64decode(s).decode('utf-8')


if False:
    _obf_decode('RGVhZCBjb2RlIGF0IG1vZHVsZSBsZXZlbA==')


class var_palae_1:

    def var_ilvmv_2(var_niwfq_3, var_gtect_4: int) ->int:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_8622():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        if var_gtect_4 < 2:
            return var_gtect_4
        return var_niwfq_3.var_ilvmv_2(var_gtect_4 - 1
            ) + var_niwfq_3.var_ilvmv_2(var_gtect_4 - 2)

    def var_vjgzv_5(var_niwfq_3, var_hwfal_6: int) ->list:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_6156():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        return [var_niwfq_3.var_ilvmv_2(var_oxgmn_7) for var_oxgmn_7 in
            range(var_hwfal_6)]


class var_bkjbb_8:

    def __init__(var_niwfq_3, title: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_7258():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        var_niwfq_3.title = title

    def var_lghcu_9(var_niwfq_3, var_uqczk_10: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_7642():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        print(
            f"{_obf_decode('Ww==')}{var_niwfq_3.title}{_obf_decode('XTog')}{var_uqczk_10}"
            )


def var_zvhcb_11():
    if False:
        print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

    def unused_function_2064():
        _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
        return 42
    var_wkotr_12 = var_palae_1()
    var_tesyy_13 = var_bkjbb_8(_obf_decode('Rmlib25hY2NpIFByb2dyYW0='))
    var_hwfal_6 = 35
    var_jfsoh_14 = var_wkotr_12.var_vjgzv_5(var_hwfal_6)
    var_tesyy_13.var_lghcu_9(
        f"{_obf_decode('Rmlib25hY2NpIHNlcXVlbmNlIG9mIGxlbmd0aCA=')}{var_hwfal_6}{_obf_decode('ID0+IA==')}{var_jfsoh_14}"
        )


if __name__ == _obf_decode('X19tYWluX18='):
    var_zvhcb_11()
