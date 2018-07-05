def exp_genes(adn):
    """ A partir da sequencia de ADN determina as proteinas. """
    arn = transcreve(adn)
    amino = traduz(arn)
    return amino

def transcreve(adn):
    """ Substitui T por U no ADN. """
    adn = adn.upper()
    arn = adn.replace('T', 'U')
    return arn

def traduz(arn):
    """ A partir do ARN devolve a lista de proteínas """
    l_cod = codoes(arn)
    # l_amino = amino(l_cod)

def codoes(arn):
    pass