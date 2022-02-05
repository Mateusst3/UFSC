class SpecialExceptions:

    @staticmethod
    def captura_exception(e):
        if 'invalid literal for int()' in e:
            exception = 'Somente é possível passar numeros!'

        elif 'list index out of range' in e:
            exception = 'Opção inválida! Selecione uma opção válida'

        else:
            exception = 'Selecione uma opção válida!'

        return exception
