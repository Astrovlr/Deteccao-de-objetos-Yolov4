import cv2

# Verificar a versão do OpenCV
print(cv2.__version__)

# Teste simples para exibir uma imagem
image = cv2.imread('')  # Substitua pelo caminho da sua imagem
cv2.imshow('horro.png', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
