class veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def frear(self):
        print(f"A {self.marca} já freio")
    def acelerar(self):
        print(f"A {self.marca} está acelerando")

class carro(veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor

    def abrir_porta(self):
        print(f"O {self.modelo} está abrindo a porta")

class moto(veiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def empinar(self):
        print(f"A {self.modelo} está empinando")

veiculo_geral = veiculo("BMW", "depende do veículo")
carro1 = carro("Fiat", "Pálio", "Branco")
moto1 = moto("Yamaha", "Factor", "125")

veiculo_geral.frear()
veiculo_geral.acelerar()
carro1.abrir_porta()
moto1.empinar()