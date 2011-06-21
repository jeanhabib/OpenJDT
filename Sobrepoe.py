""" 
Copyright (C) <2011>  <Jean Habib & Thiago Lechuga>
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

#Sorteia uma cena - local que o premio ira sair -
def escolhe_scene():
	cenas=["Scene", "Scene.002", "Scene.003", "Scene.004"]
	from random import seed,choice
	seed()
	sorteado=choice(cenas)
	
	print "Cena sorteada:"+sorteado
		
	return sorteado

def monta_lista_premios():
	import ConfigParser

	#Pega as confs do arquivo
	config = ConfigParser.RawConfigParser()
	config.read('configs.cfg')

 	premios=["broche"] * config.getint('premios', 'broche')
	premios+=["camiseta"] * config.getint('premios', 'camiseta')
	premios+=["tuxP"] * config.getint('premios', 'tuxP')
	premios+=["curso"] * config.getint('premios', 'curso')
	
	return premios

def remove_premio_lista(premio):
	import ConfigParser

	#Carrega conf do arquivo
	config = ConfigParser.RawConfigParser()
	config.read('configs.cfg')

	valor = config.getint('premios', premio) - 1
	config.set('premios', premio, str(valor))


	# Writing our configuration file to 'example.cfg'
	with open('configs.cfg', 'wb') as configfile:
	    config.write(configfile)

#Sorteia um premio
def escolhe_premio():
	premios=monta_lista_premios()
	print premios

	from random import seed,choice,shuffle
	seed()
	shuffle(premios)
	sorteado=choice(premios)
	
	print "Premio sorteado:"+sorteado
		
	remove_premio_lista(sorteado);
	

	return sorteado	


# get controller
controller = GameLogic.getCurrentController()

##Executa Premio

# get actuator attached to the controller named switchScene
act = controller.actuators["premio"]

# set scene name
#TODO: Sortear o premio
act.scene = escolhe_premio()
controller.activate(act)

#Troca Cena
#act = controller.actuators["remove"]
#controller.activate(act)

act = controller.actuators["adiciona"]
act.scene=escolhe_scene()
controller.activate(act)
