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
def escolheScene():
	cenas=["Scene", "Scene.002", "Scene.003", "Scene.004"]
	from random import seed,choice
	seed()
	sorteado=choice(cenas)
	
	print "Cena sorteada:"+sorteado
		
	return sorteado

#Sorteia um premio
def escolhePremio():
	premios=["broche"] * 12
	premios+=["Camiseta"] * 4
	premios+=["tuxP"] * 2
	premios+=["JavaEaD"] * 1
	
	from random import seed,choice,shuffle
	seed()
	shuffle(premios)
	sorteado=choice(premios)
	
	print "Premio sorteado:"+sorteado
		
	return sorteado	


# get controller
controller = GameLogic.getCurrentController()

##Executa Premio

# get actuator attached to the controller named switchScene
act = controller.actuators["premio"]

# set scene name
act.scene = escolhePremio()
controller.activate(act)

#Troca Cena
#act = controller.actuators["remove"]
#controller.activate(act)

act = controller.actuators["adiciona"]
act.scene=escolheScene()
controller.activate(act)
