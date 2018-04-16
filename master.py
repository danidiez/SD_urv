'''

'''

from pyactor.context import set_context, create_host, Host, sleep, shutdown, serve_forever
from time import time
import collections, re, urllib, os, commands, sys

#Registry: the Registry class allows to save all the actors that will be needed by the joinRemoteActors() function into a dictionary
class Registry(object):
    	_ask = ['getN','getAll']
	_tell = ['bind']
	_async = []
	_ref = ['bind','getAll']

	def __init__(self):
        	self.actors = {}
        	self.n = 0

	#Registry.bind: grants an incremental name (actor0, actor1, etc.) to an actor an adds it to the "actors" dictionary
		#-actor: the actor to be added to the "actors" dictionary
	def bind(self, actor):
		name = "actor%s" % self.n
		print "server registred", name
		self.actors[name] = actor
		self.n+=1
	
	#Registry.getN: returns the number of actors in the "actors" dictionary
	def getN(self):
		return self.n
	
	#Registry.getAll: returns all actors from a dictionary
	def getAll(self):
		return self.actors.values()


#joinRemoteActors: removes all the text fragment files and gets all actors from the Registry "actors" dictionary into a "remote" dictionary
def joinRemoteActors():
	remote= {}
	os.system("rm x*")
	print "waiting for Actors..."
	while registry.getN() < nActors:
		sleep(1)
    	remote= registry.getAll()
	return remote

#splitText: receives a file name from input, counts the number of lines in it, initializes the simpleHTTPServer and divides the original file in various files depending on the number of Actors
def splitText():
	text =raw_input("introduce the name of the text: ")
	nLines = int(commands.getoutput("wc -l "+text+" |cut -f1 -d' '"))
	nLines = nLines/nActors
	os.system("split -l %s %s" % (nLines, text))
	
#startActors: initializes the Joiner and the Actors
def startActors():
	char = 97
	joiner.start(nActors)
	for i in range(nActors):
		Actor = remote_Actors[i].spawn("Actor%s" % i, '%s/Actor' % sys.argv[1])	#create a Actor
		Actor.start(char, joiner, ip)			#start the Actor
		char += 1


if __name__ == "__main__":
	set_context()
	ip= sys.argv[2]	
	port = sys.argv[3]
	master = create_host('http://%s:%s/' % (ip, port))	#creates a host with the master's IP with a chosen port
	joiner = master.spawn('joiner', '%s/Joiner'% sys.argv[1])
	nActors = input("\nIntroduce the number of Actors: ")	#nActors: number of Actors introduced
	registry = master.spawn('regis', Registry)
	os.system("python -m SimpleHTTPServer &")	
	remote_Actors = joinRemoteActors()
	splitText()
	startActors()
	sleep(3)
	serve_forever()
