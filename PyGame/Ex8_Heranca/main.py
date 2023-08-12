from Mota import Mota
from Bicicleta import Bicicleta

moto = Mota(
	marca="Kawasaki",
	cor="verde",
	peso=500
)

moto.andar()
moto.receber_combustivel()

bike = Bicicleta(
	marca="Shimano",
	cor="azul",
	tipo="BTT",
	material="alumínio"
)

bike.andar()
