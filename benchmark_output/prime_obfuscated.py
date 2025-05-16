def _obf_decode(s):
    import base64
    return base64.b64decode(s).decode('utf-8')


if False:
    _obf_decode('RGVhZCBjb2RlIGF0IG1vZHVsZSBsZXZlbA==')


class var_ppqjp_1:

    def var_zkoca_2(var_uahzc_3, var_eexfr_4: int) ->bool:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_7524():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        if var_eexfr_4 <= 1:
            return False
        if var_eexfr_4 == 2:
            return True
        if var_eexfr_4 % 2 == 0:
            return False
        var_jmukq_5 = 3
        while var_jmukq_5 < int(var_eexfr_4 ** 0.5) + 1:
            if var_eexfr_4 % var_jmukq_5 == 0:
                return False
            var_jmukq_5 += 2
        return True

    def var_qympc_6(var_uahzc_3, var_sdtnk_7: int) ->list:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_8980():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        return [var_jmukq_5 for var_jmukq_5 in range(var_sdtnk_7) if
            var_uahzc_3.var_zkoca_2(var_jmukq_5)]


class var_pxdfr_8:

    def __init__(var_uahzc_3, title: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_2239():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        var_uahzc_3.title = title

    def var_cvlgk_9(var_uahzc_3, var_sfcfn_10: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_4155():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        print(
            f"{_obf_decode('Ww==')}{var_uahzc_3.title}{_obf_decode('XTog')}{var_sfcfn_10}"
            )


def var_uarez_11():
    if False:
        print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

    def unused_function_5347():
        _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
        return 42
    var_hxxsi_12 = var_ppqjp_1()
    var_mqpwa_13 = var_pxdfr_8(_obf_decode('UHJpbWUgQ2hlY2tlcg=='))
    var_sdtnk_7 = 1000000
    var_mpjbk_14 = var_hxxsi_12.var_qympc_6(var_sdtnk_7)
    var_mqpwa_13.var_cvlgk_9(
        f"{_obf_decode('UHJpbWUgbnVtYmVycyBiZWxvdyA=')}{var_sdtnk_7}{_obf_decode('ID0+IA==')}{var_mpjbk_14}"
        )


if __name__ == _obf_decode('X19tYWluX18='):
    var_uarez_11()
