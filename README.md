# Jupyter Notebooks - Python básico
Neste repo, eu organizo meus estudos de Python básico em notebooks jupyter,
com o intuito de consulta e revisão de conceitos como:
- funcoes
- listas
- dicionarios
- inputs de dados
- tuplas
etc...

06/07/2022
- Adicionado projeto prático do capítulo de Dicionários do livro 'Automatize tarefas maçantes com Python'
  - projeto_pratico_dicionarios.py

09/07/2022
- Adicionado projeto 'Automatize tarefas maçantes com Python': Removendo o cabeçalho de arquivos CSV 
  - projeto1_csv.py

10/07/2022
- Adicionado projeto para consumir uma API (openweathermap.org) que retorna dados como
  temperatura, humidade, condição das nuvens. A entrada de dados dar-se a partir da chamada 
  do script, onde a localização é capturada através do sysargv.
  - quickWeather.org
- Adicionado notebook python_json.org que mostra exemplos do módujo json e seus métodos: json.loads(entrada: json, retorno: python) e json.dumps(entrada: python, retorno: json)

11/07/2022
- Terminado o estudo básico do módulo json (json.loads / json.dumps) no notebook python_json.ipynb
  - Exemplo de arquivo json que poderá ser importado para scripts em python: pessoa.json
- Iniciado estudos de erros, tratamentos de exceções e testes no notebook erros_testes_tratamentos.ipynb

14/07/2022
- Continuando estudos de debbuging no código, introdução a testes unitários (unittests), programação defensiva, raise, asserts (imperativos)
  - script com introdução a unittest: test_operacoes.py
  - operacoes.py pra ser usado como módulo na importação em test_operacoes.py
  - operacoes.py contem diversas funções que simulam uma calculadora