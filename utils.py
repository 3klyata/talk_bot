class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def float_input(var_list):
    for var in var_list:
        var_not_decimal = True
        print(f'{Colors.OKGREEN}Введіть перемінну {var}: ')
        while var_not_decimal:
            val = input(f'{Colors.OKCYAN}')
            try:
                val = float(val)
            except ValueError:
                print(f'{Colors.OKGREEN}Введіть число!')
                continue
            var_not_decimal = False

        var_list[var] = val

    return var_list
