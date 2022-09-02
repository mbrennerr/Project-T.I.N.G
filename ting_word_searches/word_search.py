from assets.utils import Utils


def exists_word(word, instance):
    data = list()
    occurrences = list()

    for index in range(len(instance)):
        file = instance.search(index)
        for index, line in enumerate(file["linhas_do_arquivo"]):
            if word in line.lower():
                occurrences.append({"linha": index + 1})

        if len(occurrences) > 0:
            data.append(
                {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )

        return data


def search_by_word(word, instance):
    result = []
    for index in range(len(instance)):
        result.append(instance.search(index))
    for notice in result:
        return Utils.search_engine(notice, word)
