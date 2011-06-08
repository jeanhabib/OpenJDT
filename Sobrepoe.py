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
#TODO: Sortear o premio
act.scene = escolhePremio()
controller.activate(act)

#Troca Cena
#act = controller.actuators["remove"]
#controller.activate(act)

act = controller.actuators["adiciona"]
act.scene=escolheScene()
controller.activate(act)