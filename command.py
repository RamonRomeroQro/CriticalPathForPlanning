'''
Copyright 2019 
© Ramon Romero   @RamonRomeroQro

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

from queue import PriorityQueue


class Node:
    def __init__(self, a0, a1, a2, a3):
        self.id = a0
        self.descripcion = a1
        self.duracion = int(a2)
        self.dependencias = a3.split(' ')

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id

    def __eq__(self, other):
        return self.id == other.id

    def __repr__(self):
        return "node: "+str(self.id)


graph = {}
fields = None
index = 0

while True:
    try:
        line = str(input()).strip()
        if index == 0:
            fields = line.split(',')
        else:
            elements = line.split(',')
            if elements[0] not in graph:
                graph[elements[0]] = Node(
                    elements[0], elements[1], elements[2], elements[3])
        index += 1
    except EOFError:
        break

# setting goals
goal = str('1')
start = str(index-1)


q = PriorityQueue()

current = 0
q.put((graph[start].duracion, (graph[start], [])))
visited = set()

while q:
    len_node, x = q.get()
    node, path = x[0], x[1]
    if node is graph[goal]:
        path.append(node.id)
        path = path[::-1]
        print('reach')

        print(path)
        pr = 0
        for r in path:
            # print(graph[r].duracion)
            pr += graph[r].duracion
        print('>>>', pr, len_node)

        paco = "1,3,5,6,8,13,22,24,25,26,29".split(',')
        print(paco)
        pc = 0
        for i in paco:
            # print(graph[i].duracion)
            pc += graph[i].duracion
        print('>>>', pc)
        break
    else:
        for dependencia in node.dependencias:
            if dependencia in graph and dependencia not in visited:
                aux = path[:]
                aux.append(node.id)
                visited.add(node.id)
                a = len_node+graph[dependencia].duracion
                q.put((a, (graph[dependencia], aux)))
