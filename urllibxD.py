import urllib.request

meu_sitio = urllib.request.urlopen("https://www.tribalwars.com.pt/")
meus_bytes = meu_sitio.read()
minha_cadeia = meus_bytes.decode("utf8")
meu_sitio.close()

