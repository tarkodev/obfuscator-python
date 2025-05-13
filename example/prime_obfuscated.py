def _obf_decode(s):
    import base64
    return base64.b64decode(s).decode('utf-8')


if False:
    _obf_decode('RGVhZCBjb2RlIGF0IG1vZHVsZSBsZXZlbA==')


class var_zdyyf_1:

    def var_ixoyq_2(var_uqxdn_3, var_xlivw_4: int) ->bool:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_8167():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        if var_xlivw_4 <= 1:
            return False
        if var_xlivw_4 == 2:
            return True
        if var_xlivw_4 % 2 == 0:
            return False
        var_lqdow_5 = 3
        while var_lqdow_5 < int(var_xlivw_4 ** 0.5) + 1:
            if var_xlivw_4 % var_lqdow_5 == 0:
                return False
            var_lqdow_5 += 2
        return True

    def var_axfao_6(var_uqxdn_3, var_rssjs_7: int) ->list:
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_8313():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        return [var_lqdow_5 for var_lqdow_5 in range(var_rssjs_7) if
            var_uqxdn_3.var_ixoyq_2(var_lqdow_5)]


class var_jdgwm_8:

    def __init__(var_uqxdn_3, title: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_9856():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        var_uqxdn_3.title = title

    def var_serbj_9(var_uqxdn_3, var_sfxog_10: str):
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        def unused_function_4246():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        print(
            f"{_obf_decode('Ww==')}{var_uqxdn_3.title}{_obf_decode('XTog')}{var_sfxog_10}"
            )


def var_hcjtp_11():
    if False:
        print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

    def unused_function_8324():
        _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
        return 42
    var_frurx_12 = var_zdyyf_1()
    var_abbvp_13 = var_jdgwm_8(_obf_decode('UHJpbWUgQ2hlY2tlcg=='))
    var_rssjs_7 = 1000000
    var_kcwwq_14 = var_frurx_12.var_axfao_6(var_rssjs_7)
    var_abbvp_13.var_serbj_9(
        f"{_obf_decode('UHJpbWUgbnVtYmVycyBiZWxvdyA=')}{var_rssjs_7}{_obf_decode('ID0+IA==')}{var_kcwwq_14}"
        )


if __name__ == _obf_decode('X19tYWluX18='):
    var_hcjtp_11()
