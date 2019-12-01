# CPM_Automated
Esta es una herramienta que automatiza el método CPM, recibiendo como entrada una tabla de actividades en formato .csv para calcular el camino crítico, actividades críticas y duración mínima del proyecto/evento



29  8   27  29  8   26
27  3   25  26  5   25          --  2   ++
25  8   23  25  5   24
23  3   22  24  5   22          --  2   ++
22  8   11  22  8   13 
11  1   8   13  12  8           --  11   ++
                                    61+15 = 76 -> 76>61

reach (UCS-Dijkstra)
['1', '3', '5', '6', '8', '11', '22', '23', '25', '27', '29']
>>> 61

Refuting https://github.com/pacomonroy/CPM_Automated
['1', '3', '5', '6', '8', '13', '22', '24', '25', '26', '29']

>>> 76