"""
Simulación de un estacionamiento con máxima capacidad de 50 carros.
Los carros buscarán y se estacionarán en el lugar más conveniente.
"""

"""
Autores:
    Equipo 5
    Alberto Jashua Rodriguez Villegas 	A01752023
    Jeovani Hernandez Bastida 			A01749164
    Maximiliano Benítez Ahumada 		A01752791
    Maximiliano Carrasco Rojas 		    A01025261
"""
from mesa import Model
from mesa.time import SimultaneousActivation
from mesa.space import MultiGrid
from agentnew import *
import json


class RandomModel(Model):
    """
    Creates a new model with random agents.
    Args:
        N: Number of agents in the simulation
    """
    def __init__(self, N):

        dataDictionary = json.load(open("mapDictionary.json"))
        initCar = []
        self.destino = []
        self.salidas = []
        self.traffic_lights = []
        self.dicSentido = {}
        
        # Diccionario que contiene las coordenadas del grid en donde estarán los cajones disponibles.
        # Key = Celda del cajón, VALUE = Calle adyacente que el carró encontrará para estacionarse.

        self.cajones = {

                    #PRIMER CUADRANTE

                        #I
                           '[2, 22]': [2, 23],
                           '[3, 22]': [3, 23],
                           '[5, 22]': [5, 23],
                           '[6, 22]': [6, 23],
                           '[7, 22]': [7, 23],
                           '[8, 22]': [8, 23],
                           '[9, 22]': [9, 23],
                           '[11, 22]': [11, 23],
                           '[12, 22]': [12, 23],

                        #J
                           '[2, 21]': [1, 21],
                           '[2, 20]': [1, 20],

                        #L

                           '[12, 21]': [13, 21],
                           '[12, 20]': [13, 20],

                        #K

                           #'[2, 19]': [2, 18], Causa error
                           '[3, 19]': [3, 18],
                           #'[7, 19]': [7, 18], Causa error.
                           #'[8, 19]': [8, 18], Causa error.
                           #'[11, 19]': [11, 18] Causa error, al estar presente, algunos carros no encuentran lugar.

                    #SEGUNDO CUADRANTE - 1

                        #J
                           '[2, 15]': [1, 15],
                           '[2, 14]': [1, 14],

                        #K

                           #'[4, 13]': [4, 12], Causa error, al estar presente, algunos carros no encuentran lugar.

                        #L

                           '[5, 15]': [6, 15],
                           '[5, 14]': [6, 14],


                    
                    #SEGUNDO CUADRANTE - 2

                        #L

                            '[12, 15]': [13, 15],
                            '[12, 14]': [13, 14],

                    #TERCER CUADRANTE

                        #J

                           '[18, 20]': [17, 20],
                           '[18, 19]': [17, 19],
                           '[18, 18]': [17, 18],
                           '[18, 17]': [17, 17],
                           '[18, 16]': [17, 16],
                           '[18, 15]': [17, 15],
                           '[18, 14]': [17, 14],

                        #L

                           '[21, 22]': [21, 22],
                           '[21, 21]': [21, 21],
                           '[21, 20]': [21, 20],
                           '[21, 19]': [21, 19],
                           '[21, 18]': [21, 18],
                           '[21, 17]': [21, 17],
                           '[21, 16]': [21, 16],
                           '[21, 15]': [21, 15],
                           '[21, 14]': [22, 14],
                    
                    #CUARTO CUADRANTE - 1

                        #I
                            '[3, 7]': [3, 8],
                            #'[4, 7]': [4, 8],

                        #J
                            #'[2, 4]': [1, 4], Causa error

                        
                        #L
                            '[5, 4]': [6, 4],
                    
                    #CUARTO CUADRANTE - 2

                        #I
                            '[10, 7]': [10, 8],
                            '[11, 7]': [11, 8],

                        #J
                            '[8, 6]': [7, 6],
                            '[8, 5]': [7, 5],
                            '[8, 4]': [7, 4],

                        #L
                            '[12, 6]': [13, 6],
                            '[12, 5]': [13, 5],
                            '[12, 4]': [13, 4],
                    
                    #QUINTO CUADRANTE 
                        #J
                            #'[18, 5]': [18, 5], Causa Error
                            #'[18, 4]': [18, 4], Causa Error
                            #'[18, 3]': [18, 3], Causa Error

                        #L
                            '[21, 5]': [22, 5],
                            '[21, 4]': [22, 4],
                            '[21, 3]': [22, 3],

                        #K

                            '[19, 2]': [19, 1],

                           }

        # Se elige una celda de cada agente semáforo, puesto que son representados con 2 celdas.

        self.semaforosMaster = [(0, 13), (2, 11), (5, 0), (7, 2), (7, 16), (8, 18),
                                      (12, 0), (14, 2), (16, 22), (18, 24), (21, 9), (23, 7)]

        # Una celda semaforo desiganda como contadora puede sensar hasta 8 celdas, debido a que revisa
        # las 3 celdas de ambos carriles de su calle (6) y tambien su propia celda y la de su hermano (2).

        self.dicSensorSemaforo = {'[0, 13]': [(0, 13),(0, 14),(0, 15),(0, 16),(1, 13),(1, 14),(1, 15),(1, 16)],
                                 '[2, 11]': [(2, 11),(3, 11),(4, 11),(5, 11),(2, 12),(3, 12),(4, 12),(5, 12)],
                                 '[5, 0]': [(2, 0),(3, 0),(4, 0),(5, 0),(2, 1),(3, 1),(4, 1),(5, 1)],
                                 '[7, 2]': [(6, 2),(6, 3),(6, 4),(6, 5),(7, 2),(7, 3),(7, 4),(7, 5)],
                                 '[7, 16]': [(6, 13),(6, 14),(6, 15),(6, 16),(7, 13),(7, 14),(7, 15),(7, 16)],
                                 '[8, 18]': [(8, 17),(9, 17),(10, 17),(11, 17),(8, 18),(9, 18),(10, 18),(11, 18)],
                                 '[12, 0]': [(9, 0),(10, 0),(11, 0),(12, 0),(9, 1),(10, 1),(11, 1),(12, 1)],
                                 '[14, 2]': [(13, 2),(13, 3),(13, 4),(13, 5),(14, 2),(14, 3),(14, 4),(14, 5)],
                                 '[16, 22]': [(16, 19),(16, 20),(16, 21),(16, 22),(17, 19),(17, 20),(17, 21),(17, 22)],
                                 '[18, 24]': [(18, 23),(19, 23),(20, 23),(21, 23),(18, 24),(19, 24),(20, 24),(21, 24)],
                                 '[21, 9]': [(18, 8),(19, 8),(20, 8),(21, 8),(18, 9),(19, 9),(20, 9),(21, 9)],
                                 '[23, 7]': [(22, 4),(22, 5),(22, 6),(22, 7),(23, 4),(23, 5),(23, 6),(23, 7)]}

        # Diccionario que contiene como llave al semáforo reactivo, y como valor su hermano,
        # el cual imita su comportamiento.
        self.dicSemaforoHermano = {'[0, 13]': (1, 13),
                                   '[2, 11]': (2, 12),
                                   '[5, 0]': (5, 1),
                                   '[7, 2]': (6, 2),
                                   '[7, 16]': (6, 16),
                                   '[8, 18]': (8, 17),
                                   '[12, 0]': (12, 1),
                                   '[14, 2]': (13, 2),
                                   '[16, 22]': (17, 22),
                                   '[18, 24]': (18, 23),
                                   '[21, 9]': (21, 8),
                                   '[23, 7]': (22, 7)}

        # Se determinan las celdas semaforo que haran la comparacion con su contrario,
        # para no verificar los contadores mas de una vez. 

        self.dicSemaforoAdyacente = {'[0, 13]': (2, 11),
                                     '[5, 0]': (7, 2),
                                     '[8, 18]': (7, 16),
                                     '[12, 0]': (14, 2),
                                     '[18, 24]': (16, 22),
                                     '[23, 7]': (21, 9)}

        with open('2022_base.txt') as baseFile:
            lines = baseFile.readlines()
            self.width = len(lines[0])-1
            self.height = len(lines)

            self.grid = MultiGrid(self.width, self.height, torus=False)
            self.schedule = SimultaneousActivation(self)

            # Este for lee el archivo txt para dibujar el mapa
            for r, row in enumerate(lines):
                for c, col in enumerate(row):
                    # Sentido de la calle
                    if col in ["v", "^", ">", "<", "c"]:
                        # DataDictionary tiene el sentido de la calle
                        agent = Road(f"r_{r*self.width+c}", self,
                                     dataDictionary[col])
                        self.grid.place_agent(agent, (c, self.height - r - 1))
                        initCar.append([c, self.height - r - 1])
                        key = str([c, self.height - r - 1])
                        self.dicSentido[key] = col

                    # Genera los Semáforos
                    elif col in ["S", "s"]:
                        agent = Traffic_Light(f"tl_{r*self.width+c}",
                                              self,
                                              False if col == "S"
                                              else True,
                                              int(dataDictionary[col]))
                        self.grid.place_agent(agent, (c, self.height - r - 1))
                        self.schedule.add(agent)
                        agent.semaforosMaster = self.semaforosMaster
                        agent.dicCalles = self.dicSensorSemaforo
                        agent.dicHermano = self.dicSemaforoHermano
                        agent.dicContrario = self.dicSemaforoAdyacente
                        self.traffic_lights.append(agent)

                    # Genera los edificios
                    elif col == "#":
                        agent = Obstacle(f"ob_{r*self.width+c}", self)
                        self.grid.place_agent(agent, (c, self.height - r - 1))

                    # Genera los puentos de destino
                    elif col == "D":
                        agent = Destination(f"d_{r*self.width+c}", self)
                        self.grid.place_agent(agent, (c, self.height - r - 1))
                        self.destino.append([c, self.height - r - 1])


        
        #if N <= len(self.destino):
        
        # Generar Carros
        for i in range(N):
            ran = self.random.choice(initCar)
            car = Car(i, self)
            self.grid.place_agent(car, (ran[0], ran[1]))
            self.schedule.add(car)
            car.destino = self.random.choice(self.destino)
            self.destino.remove(car.destino)
            car.entrada = self.cajones[str(car.destino)]
            print(f'Destino {car.destino} del carro iniciado en {car.pos}')
            print(f'Entrada {car.entrada} del carro iniciado en {car.pos}')
            print(" ")
        
        #elif N >= len(self.destino):

            # disponibles = len(self.destino)
            # carrosRestantes = N - len(self.destino)

            # for j in range (carrosRestantes + 1, N):
            #     ran = self.random.choice(initCar)
            #     car = Car(j, self)
            #     self.grid.place_agent(car, (ran[0], ran[1]))
            #     self.schedule.add(car)
            #     car.destino = None 

            # for i in range(disponibles):
            #     ran = self.random.choice(initCar)
            #     car = Car(i, self)
            #     self.grid.place_agent(car, (ran[0], ran[1]))
            #     self.schedule.add(car)
            #     car.destino = self.random.choice(self.destino)
            #     self.destino.remove(car.destino)
            #     car.entrada = self.cajones[str(car.destino)]
            #     print(f'Destino {car.destino} del carro iniciado en {car.pos}')
            #     print(f'Entrada {car.entrada} del carro iniciado en {car.pos}')
            #     print(" ")
            


        self.num_agents = N
        self.running = True

    def step(self):
        '''Avanza el modelo por un paso.'''
        self.schedule.step()
