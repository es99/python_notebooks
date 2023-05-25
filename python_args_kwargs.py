def copa_titulos(country, *args):
    print('Country: ', country)

    for title in args:
        print('ano: ', title)

def lista_supermercado(*args):
    print("lista de itens: ")
    
    for item in args:
        print('item: ', item)

def calculate_price(valor, **kwargs):
    taxa_imposto = kwargs.get('imposto')
    desconto = kwargs.get('desconto')

    if taxa_imposto:
        valor += valor * (taxa_imposto / 100)
    if desconto:
        valor -= desconto

    return valor 

def test_var_args(first_arg, *args):
    print("primeiro argumento: ", first_arg)

    for outros_args in args:
        print("outros argumentos: ", outros_args)

def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print(f"{key}: {value}")

def test_args_kwargs(arg1, arg2, arg3):
    print("arg1: ", arg1)
    print("arg2: ", arg2)
    print("arg3: ", arg3)

args = ("two", 3, 2)
kwargs = {'arg1': 'two', 'arg2': 3, 'arg3': 2}

test_args_kwargs(**kwargs)