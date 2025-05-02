def _obf_decode(s):
    import base64
    return base64.b64decode(s).decode('utf-8')


if False:
    _obf_decode('RGVhZCBjb2RlIGF0IG1vZHVsZSBsZXZlbA==')


class var_ieyso_1:

    def var_pjufb_2(var_uctzd_3, var_ihlaf_4: int) ->bool:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_3980():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        if var_ihlaf_4 <= 1:
            return False
        if var_ihlaf_4 == 2:
            return True
        if var_ihlaf_4 % 2 == 0:
            return False
        var_dewup_5 = 3
        while var_dewup_5 < int(var_ihlaf_4 ** 0.5) + 1:
            if var_ihlaf_4 % var_dewup_5 == 0:
                return False
            var_dewup_5 += 2
        return True

    def var_qomiv_6(var_uctzd_3, var_usjja_7: int) ->list:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_4486():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        return [var_dewup_5 for var_dewup_5 in range(var_usjja_7) if
            var_uctzd_3.var_pjufb_2(var_dewup_5)]


class var_nesam_8:

    def __init__(var_uctzd_3, title: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_1212():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        var_uctzd_3.title = title

    def var_ocbfa_9(var_uctzd_3, var_ubggu_10: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_9059():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        print(
            f"{_obf_decode('Ww==')}{var_uctzd_3.title}{_obf_decode('XTog')}{var_ubggu_10}"
            )


def var_racmg_11():
    if False:
        print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

    def unused_function_7275():
        _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
        return 42
    var_okgyn_12 = var_ieyso_1()
    var_cpuyk_13 = var_nesam_8(_obf_decode('UHJpbWUgQ2hlY2tlcg=='))
    var_usjja_7 = 1000000
    var_boyni_14 = var_okgyn_12.var_qomiv_6(var_usjja_7)
    var_cpuyk_13.var_ocbfa_9(
        f"{_obf_decode('UHJpbWUgbnVtYmVycyBiZWxvdyA=')}{var_usjja_7}{_obf_decode('ID0+IA==')}{var_boyni_14}"
        )


if __name__ == _obf_decode('X19tYWluX18='):
    var_racmg_11()
