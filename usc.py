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
from Node import Node

class UniformCostSearch:
    def __init__(self, start, goal):
        self.goal = start
        self.start = goal
        self.graph = {}
        self.fields = None

    def parse_file(self, filepath):
        f=open(filepath, 'r')
        for index, line in enumerate(f):
            line = line.strip()
            if index == 0:
                self.fields = line.split(',')
            else:
                elements = line.split(',')
                if elements[0] not in self.graph:
                    self.graph[elements[0]] = Node(
                        elements[0], elements[1], elements[2], elements[3])
        f.close()

    def solve(self):
       
        q = PriorityQueue()
        q.put((self.graph[self.start].duracion, (self.graph[self.start], [])))
        visited = set()
        while q:
            len_node, x = q.get()
            node, path = x[0], x[1]
            if node is self.graph[self.goal]:
                path.append(node.id)
                path = path[::-1]
                print('reach')

                print(path)
                pr = 0
                for r in path:
                    # print(graph[r].duracion)
                    pr += self.graph[r].duracion
                print('>>>', pr, len_node)

                paco = "1,3,5,6,8,13,22,24,25,26,29".split(',')
                print(paco)
                pc = 0
                for i in paco:
                    # print(graph[i].duracion)
                    pc += self.graph[i].duracion
                print('>>>', pc)
                return path, len_node
                #break
            else:
                for dependencia in node.dependencias:
                    if dependencia in self.graph and dependencia not in visited:
                        aux = path[:]
                        aux.append(node.id)
                        visited.add(node.id)
                        a = len_node+self.graph[dependencia].duracion
                        q.put((a, (self.graph[dependencia], aux)))
