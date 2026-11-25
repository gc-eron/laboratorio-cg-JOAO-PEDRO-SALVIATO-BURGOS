import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Trabalho de Computação Gráfica")

st.header("8. Negativo")
foto = Image.open("imagens/foto.jpg")
img = np.array(foto)
negativo = 255 - img
st.image(negativo, caption="negativo")

st.header("9. Recorte")
foto = Image.open("imagens/foto.jpg")
img = np.array(foto)
altura, largura = img.shape[0], img.shape[1]
y = st.slider("y", 0, altura - 1, altura // 4)
x = st.slider("x", 0, largura - 1, largura // 4)
t = st.slider("tamanho", 10, largura, largura // 3)
recorte = img[y:y + t, x:x + t]
st.image(recorte, caption="recorte")

st.header("11. Espelhamento")
foto = Image.open("imagens/foto.jpg")
img = np.array(foto)
st.image(img[:, ::-1], caption="horizontal")
st.image(img[::-1, :], caption="vertical")

st.header("12. Simetria")
foto = Image.open("imagens/foto.jpg")
img = np.array(foto)
largura = img.shape[1]
meio = largura // 2
esquerda = img[:, :meio]
nova = img.copy()
nova[:, largura - meio:] = esquerda[:, ::-1]
st.image(nova, caption="simetria")

st.header("20. Pixel art")
foto = Image.open("imagens/foto.jpg")
img = np.array(foto)
passo = st.slider("Passo", 1, 40, 10)
pequena = img[::passo, ::passo]
grande = pequena.repeat(passo, axis=0).repeat(passo, axis=1)
st.image(grande, caption="pixel art")