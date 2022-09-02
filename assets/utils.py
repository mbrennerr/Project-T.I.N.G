class Utils:
    @staticmethod
    def search_engine(notice, word):
        data = list()
        occurrences = list()
        for index, line in enumerate(notice["linhas_do_arquivo"]):
            if word in line.lower():
                occurrences.append({"linha": index + 1, "conteudo": line})
            if len(occurrences) > 0:
                data.append(
                    {
                        "palavra": word,
                        "arquivo": notice["nome_do_arquivo"],
                        "ocorrencias": occurrences,
                    }
                )
        return data
