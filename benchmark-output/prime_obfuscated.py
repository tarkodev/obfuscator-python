def _obf_decode(s):
    import base64
    return base64.b64decode(s).decode('utf-8')


if False:
    _obf_decode('RGVhZCBjb2RlIGF0IG1vZHVsZSBsZXZlbA==')


class var_haugy_1:

    def var_ktfsr_2(var_osnwi_3, var_tiaho_4: int) ->bool:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_5586():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        if var_tiaho_4 <= 1:
            return False
        if var_tiaho_4 == 2:
            return True
        if var_tiaho_4 % 2 == 0:
            return False
        var_jiehu_5 = 3
        while var_jiehu_5 < int(var_tiaho_4 ** 0.5) + 1:
            if var_tiaho_4 % var_jiehu_5 == 0:
                return False
            var_jiehu_5 += 2
        return True

    def var_howsv_6(var_osnwi_3, var_ukypd_7: int) ->list:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_8120():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        return [var_jiehu_5 for var_jiehu_5 in range(var_ukypd_7) if
            var_osnwi_3.var_ktfsr_2(var_jiehu_5)]


class var_ksijp_8:

    def __init__(var_osnwi_3, title: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_2687():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        var_osnwi_3.title = title

    def var_nlbzj_9(var_osnwi_3, var_nzgry_10: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_6474():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        print(
            f"{_obf_decode('Ww==')}{var_osnwi_3.title}{_obf_decode('XTog')}{var_nzgry_10}"
            )


def var_zasko_11():
    if False:
        print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

    def unused_function_1113():
        _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
        return 42
    var_khskt_12 = var_haugy_1()
    var_sacdl_13 = var_ksijp_8(_obf_decode('UHJpbWUgQ2hlY2tlcg=='))
    var_ukypd_7 = 1000000
    var_paxuz_14 = var_khskt_12.var_howsv_6(var_ukypd_7)
    var_sacdl_13.var_nlbzj_9(
        f"{_obf_decode('UHJpbWUgbnVtYmVycyBiZWxvdyA=')}{var_ukypd_7}{_obf_decode('ID0+IA==')}{var_paxuz_14}"
        )


if __name__ == _obf_decode('X19tYWluX18='):
    var_zasko_11()
