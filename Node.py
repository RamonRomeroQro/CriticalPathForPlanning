# Copyright 2019 
# © Ramon Romero   @RamonRomeroQro

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

class Node:
    ''' Data structure for graph generation'''

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

