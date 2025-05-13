# The function below converts the given string from base64-encoded bytes to a UTF-8 decoded string.
def _obf_decode(s):
    import base64
    return base64.b64decode(s).decode('utf-8')

# This block is never executed (if False).
if False:
    _obf_decode('RGVhZCBjb2RlIGF0IG1vZHVsZSBsZXZlbA==')

# This class contains methods related to prime number checking and listing.
class var_cgote_1:

    # This method checks if a given integer (var_mjart_4) is prime.
    def var_xlreh_2(var_cchlu_3, var_mjart_4: int) -> bool:
        # This block is never executed (if False).
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        # This nested function is never called.
        def unused_function_5513():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42

        if var_mjart_4 <= 1:
            return False
        if var_mjart_4 == 2:
            return True
        if var_mjart_4 % 2 == 0:
            return False

        var_zvyrl_5 = 3
        while var_zvyrl_5 < int(var_mjart_4 ** 0.5) + 1:
            if var_mjart_4 % var_zvyrl_5 == 0:
                return False
            var_zvyrl_5 += 2
        return True

    # This method returns a list of prime numbers up to var_fzqif_7.
    def var_bnjeb_6(var_cchlu_3, var_fzqif_7: int) -> list:
        # This block is never executed (if False).
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        # This nested function is never called.
        def unused_function_6104():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42

        return [var_zvyrl_5 for var_zvyrl_5 in range(var_fzqif_7) if var_cchlu_3.var_xlreh_2(var_zvyrl_5)]

# This class demonstrates how to print messages with a title.
class var_ujnky_8:

    # The constructor saves the title.
    def __init__(var_cchlu_3, title: str):
        # This block is never executed (if False).
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        # This nested function is never called.
        def unused_function_3741():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        var_cchlu_3.title = title

    # This method prints a message with the stored title.
    def var_ihbmm_9(var_cchlu_3, var_oqfhe_10: str):
        # This block is never executed (if False).
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

        # This nested function is never called.
        def unused_function_2638():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42

        print(f"{_obf_decode('Ww==')}{var_cchlu_3.title}{_obf_decode('XTog')}{var_oqfhe_10}")

# This function ties everything together by instantiating the classes and printing prime numbers.
def var_lmogo_11():
    # This block is never executed (if False).
    if False:
        print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))

    # This nested function is never called.
    def unused_function_7667():
        _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
        return 42

    var_mgquc_12 = var_cgote_1()
    var_kgawu_13 = var_ujnky_8(_obf_decode('UHJpbWUgQ2hlY2tlcg=='))
    var_fzqif_7 = 1000000
    var_cglnt_14 = var_mgquc_12.var_bnjeb_6(var_fzqif_7)
    var_kgawu_13.var_ihbmm_9(f"{_obf_decode('UHJpbWUgbnVtYmVycyBiZWxvdyA=')}{var_fzqif_7}{_obf_decode('ID0+IA==')}{var_cglnt_14}")

# This block runs the function if this file is the main entry point.
if __name__ == _obf_decode('X19tYWluX18='):
    var_lmogo_11()