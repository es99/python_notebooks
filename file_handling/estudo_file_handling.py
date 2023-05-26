import os

def remove_arquivo(arquivo):
    if os.path.exists(arquivo):
        os.remove(arquivo)
        print("O arquivo foi removido")
    else:
        print("O arquivo não existe")

def remove_dir(diretorio):
    if os.path.exists(diretorio):
        os.rmdir(diretorio)
        print("O diretorio foi removido")
    else:
        print("O diretorio n existe")

