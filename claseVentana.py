class Ventana:
    def __init__(self, titulo, x=0, y=0, alto=100, ancho=200):
        self.titulo = titulo
        self.x = x
        self.y = y
        self.alto = alto
        self.ancho = ancho

    def mostrar(self):
        print('Mostrando ventana "{}" en la posición ({}, {}) con altura {} y ancho {}'.format(
            self.titulo, self.x, self.y, self.alto, self.ancho))

    def moverDerecha(self, dx):
        self.x += dx

    def moverIzquierda(self, dx):
        self.x -= dx

    def bajar(self, dy=10):
        self.y += dy

    def subir(self, dy=10):
        self.y -= dy

    def getTitulo(self):
        return self.titulo

    def alto(self):
        return self.alto

    def ancho(self):
        return self.ancho

            