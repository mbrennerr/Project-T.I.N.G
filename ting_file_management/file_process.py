import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file = txt_importer(path_file)
    labels = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }
    if instance.data.count(labels) == 0:
        instance.enqueue(labels)
        print(labels)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos")
    else:
        removed = instance.dequeue()
        print(f"Arquivo {removed['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        instance_position = instance.data[position]
        if instance_position:
            print(instance.data[position], file=sys.stdout)
    except IndexError:
        return sys.stderr.write("Posição inválida")
