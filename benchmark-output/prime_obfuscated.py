def _obf_decode(s):
    import base64
    return base64.b64decode(s).decode('utf-8')


if False:
    _obf_decode('RGVhZCBjb2RlIGF0IG1vZHVsZSBsZXZlbA==')


class var_ntspi_1:

    def var_jvetp_2(var_tlafw_3, var_kgfvv_4: int) ->bool:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_2257():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        if var_kgfvv_4 <= 1:
            return False
        if var_kgfvv_4 == 2:
            return True
        if var_kgfvv_4 % 2 == 0:
            return False
        var_mvwic_5 = 3
        while var_mvwic_5 < int(var_kgfvv_4 ** 0.5) + 1:
            if var_kgfvv_4 % var_mvwic_5 == 0:
                return False
            var_mvwic_5 += 2
        return True

    def var_gcxet_6(var_tlafw_3, var_hrkem_7: int) ->list:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_6287():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        return [var_mvwic_5 for var_mvwic_5 in range(var_hrkem_7) if
            var_tlafw_3.var_jvetp_2(var_mvwic_5)]


class var_blvjx_8:

    def __init__(var_tlafw_3, title: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_3688():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        var_tlafw_3.title = title

    def var_cqctm_9(var_tlafw_3, var_fwlxt_10: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_8933():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        print(
            f"{_obf_decode('Ww==')}{var_tlafw_3.title}{_obf_decode('XTog')}{var_fwlxt_10}"
            )


def var_masyt_11():
    if False:
        print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

    def unused_function_3312():
        _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
        return 42
    var_pbxjn_12 = var_ntspi_1()
    var_pxubp_13 = var_blvjx_8(_obf_decode('UHJpbWUgQ2hlY2tlcg=='))
    var_hrkem_7 = 1000000
    var_sonuj_14 = var_pbxjn_12.var_gcxet_6(var_hrkem_7)
    var_pxubp_13.var_cqctm_9(
        f"{_obf_decode('UHJpbWUgbnVtYmVycyBiZWxvdyA=')}{var_hrkem_7}{_obf_decode('ID0+IA==')}{var_sonuj_14}"
        )


if __name__ == _obf_decode('X19tYWluX18='):
    var_masyt_11()
