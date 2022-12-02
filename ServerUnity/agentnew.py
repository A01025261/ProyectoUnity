"""
Modelación de Agentes Inteligentes: Car, Traffic_Lights.
Objetos: Destination (Cajon de estacionamiento), Obstacle, Road.
"""

"""
Autores:
    Equipo 5
    Alberto Jashua Rodriguez Villegas 	A01752023
    Jeovani Hernandez Bastida 			A01749164
    Maximiliano Benítez Ahumada 		A01752791
    Maximiliano Carrasco Rojas 		    A01025261
"""
from mesa import Agent
from math import sqrt, pow


class Car(Agent):
    """
    Agente Car: busca lugar de estacionamiento.
    """
    def __init__(self, unique_id, model):
        """
        Crea al carro.
        Argumentos:
            unique_id: el id del agente.
            model: referencia del modelo.
        """
        super().__init__(unique_id, model)
        self.prevSentido = ""
        self.tipo = "car"
        self.nexCord = ()
        self.destino = None
        self.prevCord = ()
        self.parado = False
        self.mePuedoMover = True
        self.entrada = None
        self.NoDestino = True
        self.NoEntrada = True


    def move(self):
        """
        Desplazamiento del carro por el estacionamiento.
        """
        possibleSteps = self.model.grid.get_neighborhood(
            self.pos,
            moore=False,
            include_center=False,
            radius=1)

        cord = list(self.pos)
        cordstr = str(cord)

        for e in possibleSteps:
            actualE = list(e)
            if actualE == self.entrada and self.NoEntrada == True:
                print(f'Coche en: {self.pos}')
                print(f'Encontraste entrada {actualE} == {self.entrada}')
                print(" ")
                self.nexCord = e
                self.NoEntrada = False
            destinoE = list(e)
            if destinoE == self.destino:
                print(f'Coche en: {self.pos}')
                print(f'Encontraste destino {destinoE} == {self.destino}')
                print(" ")
                self.nexCord = e
                self.NoDestino = False

        if self.NoDestino and self.NoEntrada:
            for i in possibleSteps:
                cellmates = self.model.grid.get_cell_list_contents(i)
                for j in cellmates:
                    if j.tipo == "semaforo" and j.state is False:
                        if self.prevSentido == ">":
                            if self.pos == j.pos or self.pos[0] < j.pos[0]\
                                and self.pos[1] == j.pos[1]:
                                self.nexCord = self.pos
                        elif self.prevSentido == "<":
                            if self.pos == j.pos or self.pos[0] > j.pos[0]\
                                and self.pos[1] == j.pos[1]:
                                self.nexCord = self.pos
                        elif self.prevSentido == "^":
                            if self.pos == j.pos or self.pos[1] < j.pos[1]\
                                and self.pos[0] == j.pos[0]:
                                self.nexCord = self.pos
                        elif self.prevSentido == "v":
                            if self.pos == j.pos or self.pos[1] > j.pos[1]\
                                and self.pos[0] == j.pos[0]:
                                self.nexCord = self.pos

                    elif j.tipo == "semaforo" and j.state is True:
                        self.parado = False
                        if self.prevSentido == "<":
                            self.nexCord = ((cord[0] - 1), cord[1])
                        elif self.prevSentido == ">":
                            self.nexCord = ((cord[0] + 1), cord[1])
                        elif self.prevSentido == "v":
                            self.nexCord = (cord[0], (cord[1] - 1))
                        elif self.prevSentido == "^":
                            self.nexCord = (cord[0], (cord[1] + 1))

                    elif j.tipo == "calle":
                        if cordstr in self.model.dicSentido:
                            sentido = self.model.dicSentido[cordstr]
                            if sentido == "<":
                                self.nexCord = ((cord[0] - 1), cord[1])
                                self.prevSentido = sentido
                            elif sentido == ">":
                                self.nexCord = ((cord[0] + 1), cord[1])
                                self.prevSentido = sentido
                            elif sentido == "v":
                                self.nexCord = (cord[0], (cord[1] - 1))
                                self.prevSentido = sentido
                            elif sentido == "^":
                                self.nexCord = (cord[0], (cord[1] + 1))
                                self.prevSentido = sentido

                            # Se hace analisis de seleccion de camino en cruce.
                            elif sentido == "c":
                                if (self.pos == (17, 12) or self.pos == (17, 11))\
                                    and  self.destino[0] < 13\
                                        and self.destino[1] > 11:
                                    self.nexCord = (cord[0], (cord[1] + 1))
                                elif (self.pos == (14, 18) or self.pos == (13, 18))\
                                    and  self.destino[0] < 13\
                                        and self.destino[1] > 11:
                                    self.nexCord = (cord[0], (cord[1] - 1))
                                elif (self.pos == (22, 11) or self.pos == (23, 11))\
                                    and self.destino[0] == 18:
                                    self.nexCord = ((cord[0] - 1), cord[1])
                                elif (self.pos == (22, 11) or self.pos == (23, 11))\
                                    and self.destino[1] > 20:
                                    self.nexCord = (cord[0], (cord[1] + 1))
                                elif (self.pos == (16, 1) or self.pos == (16, 0))\
                                    and self.destino[0] > 18:
                                    self.nexCord = ((cord[0] + 1), cord[1])
                                elif (self.pos == (13, 8) or self.pos == (13, 9))\
                                    and self.destino[1] < 11:
                                    self.nexCord = (cord[0], (cord[1] - 1))
                                elif (self.pos == (7, 11) or self.pos == (7, 12))\
                                    and self.destino[1] > 11:
                                    self.nexCord = (cord[0], (cord[1] + 1))
                                elif (self.pos == (14, 24) or self.pos == (14, 23))\
                                    and self.destino == [5, 15]:
                                    self.nexCord = (cord[0], (cord[1] - 1))
                                elif (self.pos == (14, 24) or self.pos == (14, 23))\
                                    and self.destino == [3, 19]:
                                    self.nexCord = (cord[0], (cord[1] - 1))
                                elif (self.pos == (14, 18) or self.pos == (13, 18))\
                                    and self.destino == [5, 15]:
                                    self.nexCord = (cord[0], (cord[1] - 1))
                                else:
                                    distanciaActual = 10000000000000000
                                    for k in possibleSteps:
                                        # Evaluo que no sea la posición pasada
                                        if k != self.prevCord:
                                            cellmates = self.model.grid.\
                                                get_cell_list_contents(k)
                                            for n in cellmates:
                                                if n.tipo == "calle" or\
                                                    n.tipo == "semaforo":
                                                    disobjetivo = self.\
                                                        euclidiana(self.entrada, k)
                                                    if distanciaActual > disobjetivo:
                                                        sentido2 = self.model.\
                                                            dicSentido[str(list
                                                                    (n.pos))]
                                                        val = self.\
                                                            validarmov(sentido2,
                                                                    list(n.pos),
                                                                    cord)
                                                        if val:
                                                            distanciaActual =\
                                                                disobjetivo
                                                            Ncord = list(n.pos)
                                                            self.nexCord = (Ncord[0], Ncord[1])
            self.prevCord = self.pos


    def euclidiana(self, eDestino: list, eK: list) -> float:
        '''
        Calcula distancia de un punto a otro para poder comparar caminos.
        Argumentos:
            eDestino: punto destino.
            eK: punto a analizar.
        '''
        return sqrt(pow(eDestino[0] - eK[0], 2) +
                    pow((eDestino[1] - eK[1]), 2))


    def validarmov(self, sCasilla: str, objetivo: list, origen: list) -> bool:
        '''
        Determina movimientos correctos, evitando regresar a posiciones para
        no generar ciclos.
        Argumentos:
            sCasilla: casilla a revisar.
            objetivo: objetivo establecido.
            origen: punto de referencia.
        '''
        xOrigen = origen[0]
        yOrigen = origen[1]
        xObjetivo = objetivo[0]
        yObjetivo = objetivo[1]

        if sCasilla == "<":
            if xObjetivo < xOrigen:
                return True
            else:
                return False

        elif sCasilla == ">":
            if xObjetivo > xOrigen:
                return True
            else:
                return False

        elif sCasilla == "v":
            if yOrigen > yObjetivo:
                return True
            else:
                False

        elif sCasilla == "^":
            if yOrigen < yObjetivo:
                return True
            else:
                False

        elif sCasilla == "c":
            return True
        return False


    def step(self):
        """
        Representa un paso en el que se movera el carro.
        """
        self.move()


    def advance(self) -> None:
        '''
        Determina las restricciones al moverse a una celda
        para evitar choques.
        '''
        contador = 0
        self.mePuedoMover = True

        agente = [agent for agent in self.model.schedule.agents
                  if agent.tipo == "car" and
                  agent.unique_id != self.unique_id and
                  agent.nexCord == self.nexCord]

        if len(agente) != 0:
            contador = contador + 1

        if contador == 0:
            self.model.grid.move_agent(self, self.nexCord)
        else:
            ...
            if self.parado:
                self.mePuedoMover = False
                ...
            else:
                if self.unique_id > agente[0].unique_id:
                    self.parado = False
                    self.model.grid.move_agent(self, self.nexCord)
                else:
                    self.parado = True


class Traffic_Light(Agent):
    """
    Agente Semaforo inteligente. Se comunica con semaforos adyacentes.
    """
    def __init__(self, unique_id, model, state=False, timeToChange=10):
        super().__init__(unique_id, model)
        """
        Crea un semaforo.
        Args:
            unique_id: ID del agente
            model: referencia del modelo.
            state: determina color de semaforo, rojo falso y verde true
        """
        self.state = state
        self.timeToChange = timeToChange
        self.tipo = "semaforo"
        self.semaforosMaster = None
        self.dicCalles = None
        self.dicHermano = None
        self.dicContrario = None
        self.cuenta = 0


    def avisarHermano(self, agenteHermano):
        '''
        Avisa a celda de semaforo de al lado que
        tenga el mismo color.
        Args:
            agenteHermano: referencia a agente semaforo hermano.
        '''
        if self.state == True:
            agenteHermano.state = True
        elif self.state == False:
            agenteHermano.state = False


    def contarCoches(self):
        '''
        Cuenta los coches en su calle, teniendo un alcance
        de 3 celdas, de ambos carriles y tambien
        toma en cuenta su propia celda y la de su hermano.
        Return:
            contadorCarros: numero de carros en sus celdas de calle.
        '''
        contadorCarros = 0
        posicion = str(list(self.pos))
        vecinos = self.dicCalles[posicion]
        for i in vecinos:
            agentes = self.model.grid.get_cell_list_contents(i)
            for k in agentes:
                if k.tipo == "car":
                    contadorCarros += 1
        return contadorCarros


    def compararContrario(self, agenteContrario, hermanoContrario):
        '''
        Revisa contador propio y de contrario para determinar
        sincronizacion.
        Ya que esta funcion solo la correran los prioritaros
        si los cont son iguales, el prioritario sera el verde.
        Args:
            agenteContrario: referncia a agente semaforo contrario.
            heramnoContrario: referencia a agente semaforo hermano de contrario.
        '''
        if self.cuenta < agenteContrario.cuenta:
            self.state = False
            agenteContrario.state = True
            hermanoContrario.state = True
        elif self.cuenta > agenteContrario.cuenta:
            self.state = True
            agenteContrario.state = False
            hermanoContrario.state = False
        else:
            self.state = True
            agenteContrario.state = False
            hermanoContrario.state = False


    def step(self):
        '''
        Representa un paso en donde el semaforo cuenta, le avisa a su hermano
        y compara contrario.
        '''
        if self.pos in self.semaforosMaster:
            self.cuenta = self.contarCoches()
            posicion = str(list(self.pos))
            hermano = self.dicHermano[posicion]
            agenteHermano = self.model.grid.get_cell_list_contents(hermano)

            if posicion in self.dicContrario:
                contrario = self.dicContrario[posicion]
                agenteContrario = self.model.grid.get_cell_list_contents(contrario)
                hermanoContrario = self.dicHermano[str(list(agenteContrario[0].pos))]
                agenteHermanoContrario = self.model.grid.get_cell_list_contents(hermanoContrario)
                self.compararContrario(agenteContrario[0], agenteHermanoContrario[0])
                self.avisarHermano(agenteHermano[0])


class Destination(Agent):
    """
    Agente destino: un cajon de estacionamiento al cual debe llegar un carro.
    (OBJETO).
    """
    def __init__(self, unique_id, model):
        """
        Crea un destino.
        Args:
            unique_id: ID del agente.
            model: referencia al modelo.
        """
        super().__init__(unique_id, model)
        self.tipo = "destino"


    def step(self):
        '''
        Un paso en el que no hara nada por ser un objeto.
        '''
        pass


class Obstacle(Agent):
    """
    Agente obstaculo que representa edificios.
    (OBJETO).
    """
    def __init__(self, unique_id, model):
        """
        Crea un obstaculo.
        Args:
            unique_id: ID del agente.
            model: referencia al modelo.
        """
        super().__init__(unique_id, model)
        self.tipo = "edificio"


    def step(self):
        '''
        Un paso en el que no hara nada por ser un objeto.
        '''
        pass


class Road(Agent):
    """
    Agente donde se desplaza el agente car.
    (OBJETO).
    """
    def __init__(self, unique_id, model, direction="Left"):
        """
        Crea una calle.
        Args:
            unique_id: ID del agente.
            model: referencia al modelo.
            direction: direccion donde pueden moverse los carros.
        """
        super().__init__(unique_id, model)
        self.direction = direction
        self.tipo = "calle"
        self.parada = False


    def step(self):
        '''
        Un paso en el que no hara nada por ser un objeto.
        '''
        pass
