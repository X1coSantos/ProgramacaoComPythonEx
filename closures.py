# "Ola", "ahoy", hello

def externa(idioma):
    dic = {'pt': 'Olá', 'pi': 'ahrr', 'dg': 'AOOA', 'en': 'hello'}

    def interna(nome):
        print(f"{nome} - {dic[idioma]}")
    return interna

func = externa('pt')
func('Pedro')

func = externa('en')
func('Pedro')
