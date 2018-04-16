from pyactor.context import set_context, create_host, Host, sleep, shutdown, serve_forever
from time import time
import collections, re, urllib, os, commands, sys

#Reducer: This class joins the result of the mappers into a single dictionary and orders it alphabetically
class Joiner(object):
	_tell = ['start','send','result','syncEnd','syncStart']
	_ask = []
	_ref = ['start','send','syncEnd']

	#Reducer.initialize: initializes the necessary parameters for the reducer class
		#-maps: number of mappers created.
	def start(self ,maps):
		self.timer = time()
		self.dictionary = {}
		self.contMaps = maps
	
	#Reducer.send: this function adds a dictionary from a mapper to the reducer's dictionary, reduces by 1 the counter of how many dictionaries 		are left to be received and calls the result() function when no more dictionaries are expected
		#-mapDictionary: a dictionary created by a mapper from a fragment of the total text
	def send(self, mapDictionary):
		for word in mapDictionary:
			if word not in self.dictionary:
				self.dictionary[word] = 0
			self.dictionary[word] += mapDictionary[word]
		self.contMaps -= 1
		if self.contMaps == 0:
			self.result()
	
	#Reducer.result: this function orders the reducer's dictionary and prints it, calculates the total time the countWords and mapReduce has 		taken and prints them and kills all processes from previous mappers
	def result(self):
		resultado = collections.OrderedDict(sorted(self.dictionary.items()))
		totalT = time() - self.timer
		print resultado
		print"\nElapsed time: %s" % totalT
		sleep(1)
		os.system("kill -9 $(ps -a|grep python|cut -f2 -d"+"'"+" "+"')")
	

#Mapper: Reads a fragment of the text and adds the words to a dictionary.
class Actor(object):
	_tell = ['countWords','start','map']
    	_ask = []
	_ref = ['start']

	#Mapper.readFile: function that reads the corresponding fragment of the file
		#-fName: string used to identify the name of the file to be read
		#-reducer: reducer class used to send the results of the execution
		#-ip: the ip from the master needed by the "wget" function to download the text file from the master
	def start(self, fName, reducer,ip):
		self.name = "xa"+chr(fName)
		self.reducer = reducer
		os.system("wget 'http://"+ip+":8000/"+self.name+"'")
		self.reducer=reducer
		self.text =open(self.name,'r').read()
		self.countWords()
	
	#Mapper.countWords: cleans the text fragment out of textual punctuations, special symbols and numbers, counts the total number of words in 		the fragment and calls the map() function
	def countWords(self):
		for char in "?![]{}()+*-=_\#.:,;<>/|~$%1234567890'":
			self.text=self.text.replace(char, ' ')
		self.text = self.text.lower()				#Changes all Caps to lowerCaps
		self.text = self.text.split()
		self.map()
	
	#Mapper.map: creates a dictionary out of all the words from the text fragment and sends it to the reducer with send(mapDictionary) 
	def map(self):
		self.dict = {}
		for word in self.text:
			if word not in self.dict:
				self.dict[word] = 0
			self.dict[word] += 1
		self.reducer.send(self.dict)
