import cImage
import tkinter

def cria_janela(nome, largura, altura):
    """ Cria uma janela de nome = nome, com dimensoes: largura*altura """
    janela = cImage.ImageWin(nome, largura, altura)
    janela.exitOnClick()

def cria_janela_cor(nome, largura, altura, cor):
    """ Cria uma janela de nome = nome, com dimensoes largura*altura e cor de fundo = cor """
    janela = cImage.ImageWin(nome, largura, altura)
    janela.getMouse()
    janela.exitOnClick()


def cria_imagem_vazia(largura, altura):
    imagem = cImage.EmptyImage(largura, altura)
    return imagem

def mostra_imagem_simples(imagem):
    largura = imagem.getWidth()
    altura  = imagem.getHeight()

    janela = cImage.ImageWin("Imagem" , largura, altura)
    imagem.draw(janela)

    janela.exitOnClick()


if __name__ == '__main__':
    largura = 300
    altura = 200
    imagem = cImage.EmptyImage(largura, altura)
    mostra_imagem_simples(imagem)