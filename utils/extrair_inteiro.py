def extrair_inteiro(texto):
    try:
        i = texto.rindex(' ')
        sem_unidade = texto[:i]

        # Às vezes, esse valor pode iniciar pelo ano...
        i = sem_unidade.find(' ')
        if i >= 0:
            sem_unidade = sem_unidade[(i + 1):]

        sem_virgula = sem_unidade.replace(',', '')

        return int(sem_virgula)
    except:
        return 0
