# Critical Path for Planning Events
```
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
```

This is a tool that automates the CPM method, receiving as input a table of activities in ```.csv``` format to calculate the critical path, critical activities and minimum project / event duration.
```
Index, Activity, Description, Duration, Dependencies
```


### Reach Method (UCS-Dijkstra)
```
['1', '3', '5', '6', '8', '11', '22', '23', '25', '27', '29']
>>> 61

```

```
29  8   27  29  8   26
27  3   25  26  5   25          --  2   ++
25  8   23  25  5   24
23  3   22  24  5   22          --  2   ++
22  8   11  22  8   13 
11  1   8   13  12  8           --  11   ++
                                    61+15 = 76 -> 76>61

```
## Install

``` bash

$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install --upgrade pip
$ pip3 install -r requeriments.txt


```
## CLI

``` bash

$ python3 command.py < <TEST_FILE>


```


## Build

Generated on ``` ./dist/```

```
$ ./build_mac.sh
```


