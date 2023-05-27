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

def test_var_args(first_arg, *args, **kwargs):
    print("primeiro argumento: ", first_arg)

    for outros_args in args:
        print("outros argumentos: ", outros_args)

    for key, value in kwargs.items():
        print(f"{key}: {value}")


def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print(f"{key}: {value}")

def test_args_kwargs(arg1, arg2, arg3):
    print("arg1: ", arg1)
    print("arg2: ", arg2)
    print("arg3: ", arg3)

def escreve_mensagem(**kwargs):
    msg = f"""
    Olá {kwargs['nome']},

    sabemos que vc tem {kwargs['idade']} e vc é do sexo {kwargs['sexo']}
    """
    return msg

dicionario = {'nome': 'Engels', 'idade': 36, 'sexo': 'Masculino'}

print(escreve_mensagem(**dicionario))

