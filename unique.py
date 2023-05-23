from utils import Colors, float_input


def vector_multiply():
    var_list = {
        'x1': None,
        'y1': None,
        'z1': None,
        'x2': None,
        'y2': None,
        'z2': None
    }

    var_list = float_input(var_list)

    x = var_list['y1']*var_list['z2']-var_list['z1']*var_list['y2']
    y = var_list['z1']*var_list['x2']-var_list['x1']*var_list['z2']
    z = var_list['x1']*var_list['y2']-var_list['y1']*var_list['x1']

    print(f'{Colors.OKGREEN}Векторний добуток: [{x}; {y}; {z}]')


def nod_nok():
    var_list = {
        'n1': None,
        'n2': None
    }

    var_list = float_input(var_list)

    x = var_list['n1']
    y = var_list['n2']

    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1
    if x > y:
        smaller = int(y)
    else:
        smaller = int(x)
    for i in range(1, smaller + 1):
        if(x % i == 0) and (y % i == 0):
            hcf = i

def distance_from_dot_to_line():


    print(f'{Colors.OKGREEN}НСД: {lcm}, НСК: {hcf}')