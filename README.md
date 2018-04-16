Map-reduce implementation with Pyactor

This code use a simple map reduce function in distributed system. Allows to split the problem in pieces and solve it with diferent computers with actors. This code is implemented as a framework. You can use your own function map-reduce following a standard code implementation:

      function.py:
      class Joiner(object):
         def start(nActors):
         ...
      class Actor(object):
         def start(textFragment, Joiner, ip):
         ...
    
The class actor will be used to be spawned in a empty host. This class will make all the distributed work in a diferent computers.
The class Joiner will be spawned in the master. It will be used to join all the results of the mappers inside the master computer.
 
 INSTRUCTIONS:
 1. cd ~/ (you must have all the code in the same directory, including the txt files)
 2. execute "python master.py <name of the function> <ip of the master> <port>  *name of the function will be the name of the                      
    code(without .py) for execute. example: mapreduce
 3. Introduce the number of actors.
 4. In a new console (or computer) execute "python spawner.py <ip_host> <ip+port_master> <number of actors>"
 5. Introduce the name of the file in the master console.
  *If the last step worked you will be noticed in the console with the registry of the hosts joined.
 6. Wait for the result of the execution and DONE!
 *Optional: to spawn actors in a different computer, execute spawner.py with your own public ip and the public ip of the master.
            You can use 'ip a' or 'ifconfig' to check your local ip. Otherwise, use the local ip 127.0.0.1/24
  
 EXAMPLE:
 
        cd Desktop/sd/
        python master.py countwords 127.0.0.1 7777
        /*inside the console of the master*/
        number of mappers: 4
        /*in another console*/
        python master.py 127.0.0.2 127.0.0.1:7777 4
        /*back to master console*/
        name of the text file: sherlock
        ...
        /*result:
        number of words:3640322
        elapsed time: 0,09362943167
        */


Autors: Daniel Díez Sánchez & Raúl Almenara Peñaranda
