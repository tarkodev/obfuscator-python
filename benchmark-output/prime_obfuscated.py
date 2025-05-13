def _obf_decode(s):
    import base64
    return base64.b64decode(s).decode('utf-8')


if False:
    _obf_decode('RGVhZCBjb2RlIGF0IG1vZHVsZSBsZXZlbA==')


class var_kjaki_1:

    def var_ehvbl_2(var_pleuf_3, var_kdgtj_4: int) ->bool:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_7702():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        if var_kdgtj_4 <= 1:
            return False
        if var_kdgtj_4 == 2:
            return True
        if var_kdgtj_4 % 2 == 0:
            return False
        var_psosa_5 = 3
        while var_psosa_5 < int(var_kdgtj_4 ** 0.5) + 1:
            if var_kdgtj_4 % var_psosa_5 == 0:
                return False
            var_psosa_5 += 2
        return True

    def var_prqdd_6(var_pleuf_3, var_rsiqv_7: int) ->list:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_4156():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        return [var_psosa_5 for var_psosa_5 in range(var_rsiqv_7) if
            var_pleuf_3.var_ehvbl_2(var_psosa_5)]


class var_wjskd_8:

    def __init__(var_pleuf_3, title: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_1315():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        var_pleuf_3.title = title

    def var_exxuv_9(var_pleuf_3, var_glduh_10: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_7392():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        print(
            f"{_obf_decode('Ww==')}{var_pleuf_3.title}{_obf_decode('XTog')}{var_glduh_10}"
            )


def var_tcrin_11():
    if False:
        print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

    def unused_function_6522():
        _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
        return 42
    var_qvyde_12 = var_kjaki_1()
    var_hhgke_13 = var_wjskd_8(_obf_decode('UHJpbWUgQ2hlY2tlcg=='))
    var_rsiqv_7 = 1000000
    var_rinaj_14 = var_qvyde_12.var_prqdd_6(var_rsiqv_7)
    var_hhgke_13.var_exxuv_9(
        f"{_obf_decode('UHJpbWUgbnVtYmVycyBiZWxvdyA=')}{var_rsiqv_7}{_obf_decode('ID0+IA==')}{var_rinaj_14}"
        )


if __name__ == _obf_decode('X19tYWluX18='):
    var_tcrin_11()
