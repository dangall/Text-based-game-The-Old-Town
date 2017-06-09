import gamemodule
import time
import random

evacugo = 0
introchat = 0
editspoken = 0
engspoken = 0
stevespoken = 0
sharspoken = 0
steveadmitfish = 0
mayorfestival = 0
engcctv = 0
fishinrod = 0
foundrod = 0
steveadmitall = 0
usecrane = 0
badpress = 0
sitefix = 0
baronsort = 0
editmission = 0
hallannounce = 0
hallempty = 0
damchecked = 0
onthepapers = 0
damlooked = 0
damtalked = 0
barondeal = 0

play1 = 0
play2 = 0
play3 = 0

class Person(object):
	def __init__(self, name, startplace):
		self.name = name
		self.location = startplace

#===========================================================
class House(object):
	def __init__(self, name, coord):
		self.name = name
		self.coord = coord
		self.arrivmessage = "You are back in your home. The usual silence prevails."
		self.chat = "There is no one else in the house."
		self.description = "\nThe house is completely void of people."
		
	def arrive(self):
		print self.arrivmessage
    
	def inspect(self):
		print self.description
		
	def talk(self):
		print self.chat
		
#===========================================================
class Steve(object):
	def __init__(self, name, coord):
		self.name = name
		self.coord = coord
		self.arrivmessage = "A man greets you at the door, looking wary and annoyed."
		self.chat = """He demands to know who you are, and whether you're a lawyer.
Without properly listening to your answers, he mutters to
himself that he hates his ex-wife Sharon, and slams the door 
on you. He doesn't come back out."""
		self.description = "Under careful inspection, the man seems to not have slept much and appears very nervous and stressed."
		
	def arrive(self):
		print self.arrivmessage
    
	def inspect(self):
		if fishinrod==1:
			self.description = """Steve sounds very vague about his descriptions. You notice a rusty old disused 
fishing pole on his porch"""
			print self.description
			global foundrod
			foundrod = 1
		else:
			print self.description
    
	def talk(self):
		if steveadmitall==1 and sharspoken==1 and editmission==1:
			self.chat = """You tell Steve that the engineers looked at the CCTV footage and there was nothing suspicious.
Steve breaks into sobbing and admits that he stole Sharon's car, taking the keys from the secret place in the shed.
He then drove the car into the lake by the dam, and he thinks the strong current sucked it into the dam."""
			print self.chat
			global usecrane
			usecrane = 1
		else:
			if steveadmitfish==1 and foundrod==0:
				self.chat = """Steve says that it's true he was fishing there yesterday, but he didn't catch much.
He says he saw something suspicious there around 6pm, some people doing suspicious 
stuff outside the control room."""
				global fishinrod
				global engcctv
				fishinrod = 1
				engcctv = 1
				print self.chat
			elif steveadmitfish==1 and foundrod==1:
				self.chat = """You point out that his fishing pole seems very disused. He gets really defensive, and 
tells you that if you don't believe him, you should go to the dam and confirm his story with the engineers.
He then slams the door on you."""
				print self.chat
			else:
				global stevespoken
				if sharspoken==1 and stevespoken==1:
					self.chat = """You say you've met Sharon. He says that she stole his kids from him and
she deserves having lost her car. He'll make her life as hard as he can over this divorce. 
Then he slams the door and doesn't come back out."""
					print self.chat
				elif sharspoken==0 and stevespoken==1:
					self.chat = "Steve says he doesn't want to talk to you now, and closes the door in your face."
					print self.chat
				else:
					print self.chat
					stevespoken = 1
					self.arrivmessage = "Steve greets you at the door, still looking wary and annoyed."
		
#===========================================================
class Townhall(object):
	def __init__(self, name, coord):
		self.name = name
		self.coord = coord
		self.arrivmessage = "The town hall is jammed full of people. There is a heated discussion going on. The Mayor is there."
		self.chat = """You go up to the Mayor. He is extremely worried. He says that there 
seems to be some problem with the old Dam and the water level is rising
beyond the safe levels. He mutters 'regular inspection wasn't so regular'. 
It's looking bad, really bad."""
		self.description = """Everyone seems to be talking about the dam. They are saying that
there is some problem with it and that it might explode.
The Mayor seems to be silent and avoiding the discussion. You can probably approach him."""
		
	def arrive(self):
		print self.arrivmessage
    
	def inspect(self):
		print self.description
    
	def talk(self):
		global hallempty
		if hallempty==1:
			self.chat = "There is no one left to talk to here."
			print self.chat
		else:
			if hallannounce==1:
				self.chat = """You shout over the voices, announcing that the evacuation has started.
Everybody scrambles out of the hall, presumably to their things and their cars."""
				print self.chat
				self.chat = "The hall is empty."
				self.arrivmessage = "The town hall is completely void of people."
				self.description = "The hall is filled with silence. After the day's events, it's very messy."
				hallempty = 1
			else:
				print self.chat
				global introchat
				introchat = 1
				# Now the Mayor goes back to his office.
				self.arrivmessage = "The town hall is still jammed full of people. The Mayor isn't here."
				self.chat = "There is a terrible commotion still. Everyone seems panicky and no one is willing to talk."
				self.description = """Everyone seems to be talking about the dam. They are saying that
there is some problem with it and that it might explode."""
		
#===========================================================
class Park(object):
	def __init__(self, name, coord):
		self.name = name
		self.coord = coord
		self.arrivmessage = "The park is completely empty. No one is jogging, no one is walking their dog."
		self.chat = "There is no one to talk to."
		self.description = """After looking around it carefully, you notice signs of people having left quickly.
There are several forgotten bags and personal items in the park."""
		
	def arrive(self):
		if evacugo==1:
			self.arrivmessage = """The park is full of panicky people. You see that everyone is there.
Large buses come and pick everyone up, driving fast out of town. The town is
successfully evacuated! 
\nUnfortunately, the dam burst, completely destroying the town and everything in it,
except for the Baron's mansion."""
			print self.arrivmessage
			time.sleep(5)
			print "\nYOU WON! (THOUGH AT A HIGH COST...)\n"
			exit(0)
		else:
			print self.arrivmessage
    
	def inspect(self):
		print self.description
    
	def talk(self):
		print self.chat
		
#===========================================================
class Sharon(object):
	def __init__(self, name, coord):
		self.name = name
		self.coord = coord
		self.arrivmessage = "A woman answers the door, not letting you in."
		self.chat = """She tells you that she is furious that someone stole her car. She has been looking all
over for it. She says that on top of the divorce with Steve, this is way too much for her.
There is a shout from inside the house and she retreats back into her home, closing the door behind her."""
		self.description = "She seems honest, but very unkempt. You can hear children's voices from upstairs."
		
	def arrive(self):
		print self.arrivmessage
    
	def inspect(self):
		if sharspoken==1 and stevespoken==1:
			self.description = "She seems honest, but very unkempt. You can hear children's voices from inside the house."
			print self.description
		else:
			print self.description
    
	def talk(self):
		global sharspoken
		if sharspoken==1 and stevespoken==1:
			self.chat = """You tell her you spoke to Steve.
She just tells you again that she is furious that someone stole her car. She noticed today that the keys
are missing from the secret place in the outdoor shed. She mentions how difficult this is, and 
how stressed she is from her divorce with Steve, what with her getting to keep the children 
and all. There is another shout from inside the house and she retreats back into her home, closing 
the door behind her."""
			print self.chat
		elif sharspoken==1 and stevespoken==0:
			self.chat = "Sharon can't hear your knocking at the door, and doesn't come out."
			print self.chat
		else:	
			print self.chat
			sharspoken = 1
			self.arrivmessage = "Sharon answers the door again, not letting you in."
					
#===========================================================
class Baron(object):
	def __init__(self, name, coord):
		self.name = name
		self.coord = coord
		self.arrivmessage = """The butler greets you at the door. He tells you that you're
not expected, and closes the door on you."""
		self.chat = "There is no one here to talk to."
		self.description = """The mansion is very beautiful and lies above the lake."""
		
	def arrive(self):
		if baronsort==1 and evacugo==0:
			self.arrivmessage = "The butler greets you at the door. You are allowed inside, where the Baron lazily dignifies you with his gaze."
			print self.arrivmessage
		else:
			self.arrivmessage = """The butler greets you at the door. He tells you that you're
not expected, and closes the door on you."""
			print self.arrivmessage
    
	def inspect(self):
		if baronsort==1 and evacugo==0:
			self.description = """The house is beautifully constructed. Fine art hangs on the walls, 
and a small dog is lying on the rug, growling to himself."""
			print self.description
		else:
			self.description = """The mansion is very beautiful and lies above the lake."""
			print self.description
    
	def talk(self):
		global barondeal
		global evacugo
		if baronsort==1 and evacugo==0:
			self.chat = """The Baron listens to the situation. He says he can make the evacuation happen,
without having to 'jump through all those hoops'. All you need to do is
tell the Mayor that his daughter has high aspirations, in particular when
it comes to the next election, and that the Mayor will only receive help
if his daughter is guaranteed not to be disappointed."""
			print self.chat
			barondeal = 1
			self.arrivmessage = """The butler greets you at the door. He tells you that you're
not expected, and closes the door on you."""
		else:
			self.chat = "There is no one here to talk to."
			print self.chat
		
#===========================================================
class Mayorplace(object):
	def __init__(self, name, coord):
		self.name = name
		self.coord = coord
		self.arrivmessage = "You enter in an empty hall, normally full of secretaries. The big desk at the back, where the Mayor sits, is also empty."
		self.chat = "There is no one else in the house."
		self.description = """The desk still has this morning's breakfast on it. People must have left together. 
There is a memo on the Mayor's desk asking for a statement on the dam situation."""
		
	def arrive(self):
		if evacugo==1:
			self.arrivmessage = "You enter in an empty hall, normally full of secretaries. The big desk at the back, where the Mayor sits, is also empty."
			print self.arrivmessage
		elif introchat==1:
			self.arrivmessage = "The hall has a large desk at the back, where the Mayor is sitting, looking at his computer."
			print self.arrivmessage
		else:
			print self.arrivmessage
    
	def inspect(self):
		if introchat==1:
			self.description = """There are papers everywhere. Some of them look like engineering reports, 
police reports, and preparations for the upcoming May festival."""
			print self.description
		else:
			print self.description
    
	def talk(self):
		global evacugo
		if evacugo==1:
			self.chat = "The room is empty."
			print self.chat
		elif sitefix==1 and hallempty==1 and onthepapers==1:
			self.chat = """You tell the Mayor you've done all the tasks he required for the evacuation.
He looks a little scared and disappointed, and says that it's all over then.
We must all evacuate quickly from the park! He rushes out of the office,
leaving the room in silence."""
			print self.chat
			evacugo = 1
		elif barondeal==1:
			self.chat = """You tell the Mayor about your conversation with the Baron. He says
he was expecting this. He makes a quick call to the Baron and tells you 
it's all sorted, the evacuation of the town will now be under way. 
We must all evacuate quickly from the park! He rushes out of the office,
leaving the room in silence."""
			print self.chat
			evacugo = 1
		elif introchat==1:
			global steveadmitfish
			global mayorfestival
			global badpress
			if badpress==1:
				self.chat = """The Mayor looks worried to hear about the editor's bad press.
He says that if you can manage to cancel the festival, he'll evacuate the
town. But he firmly insists for the following things to have been done:
 - The news about the festival cancellation to be on the town's website
 - The news also be put in the papers
 - The evacuationbe announced in the town hall
Then an assistant comes in and he vaguely points to where the webmaster's office is."""
				print self.chat
				global baronsort 
				baronsort = 1
				global editmission 
				editmission = 1
				global hallannounce
				hallannounce = 1
				global placedict
				global allplaces
				global placelist
				global placearray
				placedict = {'website': websiteoffice, 'administrator': websiteoffice, "administrator's": websiteoffice, "Administrator's": websiteoffice, 'home': myhouse, 'park': park, 'baron': baronhouse, "baron's": baronhouse, "Baron's": baronhouse, 'mansion': baronhouse, 'mayor': mayoroffice, "mayor's": mayoroffice, "Mayor's": mayoroffice, 'dam': dam, 'town':townhall, 'printing': newspaper, 'press': newspaper, 'steve': stevehouse, "steve's": stevehouse, 'Steve': stevehouse, "Steve's": stevehouse, 'sharon': sharonhouse, "sharon's": sharonhouse, 'Sharon': sharonhouse, "Sharon's": sharonhouse}
				allplaces = [websiteoffice, myhouse, stevehouse, townhall, park, sharonhouse, baronhouse, mayoroffice, websiteoffice, dam, newspaper]
				placelist = websiteoffice.name + ", " + myhouse.name + ", " + townhall.name + ", " + park.name + ", " + baronhouse.name + ", " + mayoroffice.name + ", " + dam.name + ", " + newspaper.name + ", " + stevehouse.name + ", " + sharonhouse.name + "."
				placearray = ['website', 'administrator', "administrator's", "Administrator's", 'home', 'park', 'baron', "baron's", "Baron's", 'mayor', "mayor's", "Mayor's", 'dam', 'town', 'printing', 'press', 'steve', "steve's", 'Steve', "Steve's", 'sharon', "sharon's", 'Sharon', "Sharon's"]
				#placedict = {websiteoffice.name: websiteoffice, myhouse.name: myhouse, townhall.name: townhall, park.name: park, baronhouse.name: baronhouse, mayoroffice.name: mayoroffice, dam.name: dam, newspaper.name: newspaper, stevehouse.name: stevehouse, sharonhouse.name: sharonhouse}
				#allplaces = [websiteoffice, myhouse, stevehouse, townhall, park, sharonhouse, baronhouse, mayoroffice, websiteoffice, dam, newspaper]
				#placelist = websiteoffice.name + ", " + myhouse.name + ", " + townhall.name + ", " + park.name + ", " + baronhouse.name + ", " + mayoroffice.name + ", " + dam.name + ", " + newspaper.name + ", " + stevehouse.name + ", " + sharonhouse.name + "."
				#placearray = [websiteoffice.name, myhouse.name, townhall.name, park.name, baronhouse.name, mayoroffice.name, dam.name, newspaper.name, stevehouse.name, sharonhouse.name]
			else:
				if stevespoken==0 and editspoken==0:
					self.chat = "The Mayor is too preoccupied to speak right now. He says to go away."
					print self.chat
				elif stevespoken==1 and editspoken==0:
					self.chat = """You mention that you spoke to Steve. The Mayor says that Steve was seen by the Dam yesterday fishing.
They questioned him to find out if he saw or noticed anything, but he was really unhelpful. 
They think he was possibly fishing up endangered fish."""
					steveadmitfish = 1
					print self.chat
				elif stevespoken==0 and editspoken==1:
					self.chat = """You tell him that the editor was pushing for full evacuation. The Mayor gets very irritated, pointing
out that the town is about to have the famous May festival, and everything is paid for already, and that 
he's not going to panic over the first sign of trouble. """
					print self.chat
					mayorfestival = 1
				elif stevespoken==1 and editspoken==1:
					self.chat = """You mention that you spoke to Steve. The Mayor says that Steve was seen by the
Dam yesterday fishing. They questioned him to find out if he saw or noticed 
anything, but he was really unhelpful. They think he was possibly fishing up 
endangered fish. 
\nYou tell him that the editor was pushing for full evacuation. The Mayor 
gets very irritated, pointing out that the town is about to have the famous 
May festival, and everything is paid for already, and that he's not going
to panic over the first sign of trouble."""
					print self.chat
					steveadmitfish = 1
					mayorfestival = 1
		else:
			print self.chat
		
#===========================================================
class Website(object):
	def __init__(self, name, coord):
		self.name = name
		self.coord = coord
		self.arrivmessage = "A pale man in round glasses looks up from a messy office full of computer components."
		self.chat = """The man is the webmaster. He says he can change the website as you request,
but first he needs the password. The Mayor has forgotten it, but he needs it.
He reads out the password hint:
\n'It travels around the world while staying in one corner.'"""
		self.description = "The place smells musty and a feels a bit claustrophobic."
		
	def arrive(self):
		print self.arrivmessage
    
	def inspect(self):
		print self.description
    
	def talk(self):
		global sitefix
		if sitefix==1:
			self.chat = "The webmaster is too busy to talk to you."
			print self.chat
		else:
			print self.chat
			secfound = 0
			cont=0
			while cont==0:
				print "\nThe password he typed in doesn't work. Do you want to try and guess the password?\n"
				yesno = gamemodule.asktoget(['yes','Yes','No','no'])
				if gamemodule.intersect(yesno,['yes','Yes'])!=[]:
					print "\nWhat is the password?\n"
					secpass = raw_input("> ")
					secpass = secpass.split()
					if gamemodule.intersect(secpass,['stamp'])!=[]:
						time.sleep(3)
						print "\nThe password is correct!"
						time.sleep(1)
						secfound = 1
						cont = 1
				elif gamemodule.intersect(yesno,['No','no'])!=[]:
					cont = 1
			if secfound==1:
				print """\nThe webmaster enters into the website code, and says he'll fix it.
He looks annoyed at you still standing there, and says that you can leave."""
				sitefix = 1
			else:
				print """\nHe looks annoyed at you, and says that if you don't give him the
password, he's clearly not going to log in and fix the site for
you. He turns to his computer and ignores you."""
		
#===========================================================
class Dam(object):
	def __init__(self, name, coord):
		self.name = name
		self.coord = coord
		self.arrivmessage = """The huge dam only has water flowing out of one of the two outlets, where
the water seems to be coming out with unusual strength. Near the top of 
the dam you see the usual junk yard with a large magnet-crane in it."""
		self.chat = "There is no one here."
		self.description = """The dam is very old. It has a control room, which appears to be locked. The road to the dam 
ends in a muddy field, which eventually leads into the lake. On the one side you can gain
access to the dam, and on the other is the access to the junk yard, which is positioned 
right by the water. The junk yard is filled with heaps of discarded items, and has a large
crane with a magnet to pick up the metal."""
		
	def arrive(self):
		if usecrane==1:
			self.arrivmessage = """The dam looks deserted. The water level is almost to the brim of the dam, and is almost
in the junk yard, where the magnetic crane is."""
			print self.arrivmessage
		else:
			print self.arrivmessage
    
	def inspect(self):
		global damlooked
		damlooked = 1
		if damtalked==1:
			global damchecked
			damchecked = 1
		if introchat==1:
			if engcctv==1:
				self.description = """You see that in the mud field next to the dam, there are car
tracks leading straight into the lake."""
				print self.description
			else:
				self.description = """The dam is very old. Engineers are standing smoking outside the control room. 
The road to the dam ends in a muddy field, which eventually leads into the lake. 
On the one side you can gain access to the dam, and on the other is the 
access to the junk yard, which is positioned right by the water. The junk 
yard is filled with heaps of discarded items, and has large crane with a magnet 
to pick up the metal."""
				print self.description
		else:
			print self.description 
    
	def talk(self):
		global damtalked
		damtalked = 1
		if damlooked==1:
			global damchecked
			damchecked = 1
		if usecrane==1:
			self.chat = "There is no one around to talk to."
			print self.chat
		else:
			if engcctv==1:
				self.chat = """You ask about Steve and the CCTV footage. They say they looked through the whole thing and didn't
see anything suspicious at any point. They don't have any footage between 1.00am and 1.05am, 
which is when the system was changing tapes."""
				print self.chat
				global steveadmitall
				steveadmitall = 1
			else:
				if introchat==1:
					self.chat = """You go up to speak to the engineers. The say they don't understand what is going on at all:
everything seems to be working with the dam in theory, but there doesn't seem to be any water
going through. The rising water is putting too much pressure on the old dam, and it probably 
will collapse."""
					print self.chat
					global engspoken
					engspoken = 1
				else:
					print self.chat
		
#===========================================================
class Newspaper(object):
	def __init__(self, name, coord):
		self.name = name
		self.coord = coord
		self.arrivmessage = """The printing press is usually full of activity. Now the room stands eerily empty."""
		self.chat = "There is no one here to talk to."
		self.description = """The room is fully of messy desks, coffee cups, notepads and photographs."""
#The sound of the editor's muttering oddly echoes off the walls of this otherwise deserted room.		
		
	def arrive(self):
		if introchat==1 and evacugo==0:
			self.arrivmessage = """The printing press, usually a busy room, only has a few journalists
typing furiously at their computers, and the editor, looking concerned 
and staring into empty space, muttering to himself."""
			print self.arrivmessage
		else:
			self.arrivmessage = """The printing press is usually full of activity. Now the room stands eerily empty."""
			print self.arrivmessage
    
	def inspect(self):
		if introchat==1 and evacugo==0:
			self.description = """The room is fully of messy desks, coffee cups, notepads and photographs. 
The sound of the editor's muttering oddly echoes off the walls."""
			print self.description
		else:
			print self.description
    
	def talk(self):
		if evacugo==1:
			self.chat = "There is no one here to talk to."
			print self.chat
		else:
			if introchat==1:
				if editmission==1 and damchecked==0:
					self.chat = """You tell the editor that the Mayor has agreed to evacuate,
as long as the news of the cancellation of the May festival and
the evacuation is put on the newspaper. The editor agrees to do it, 
if you give him news on the dam, since his journalists don't have time
to go there now."""
					print self.chat
				elif editmission==1 and damchecked==1:
					self.chat = """You give news about the dam to the editor. He's pleased to hear
that the Mayor has agreed to evacuate, and with the dam update you gave him,
he's very willing to put everything in the newspaper as you request."""
					print self.chat
					global onthepapers
					onthepapers = 1
				else:
					if mayorfestival==1:
						self.chat = """You tell the editor that the Mayor is unwilling to evacuate the town,
for fear of ruining the May festival. The editor shouts that if
the Mayor doesn't decide to evacuate immediately, he'll give him
the worse press a Mayor has ever had, and that his articles will
absolutely destroy him."""
						print self.chat
						global badpress
						badpress = 1
					else:
						global editspoken
						if editspoken==1:
							self.chat = "The editor is still talking on the phone."
							print self.chat
						else:
							self.chat = """The editor asks if you've spoken to the Mayor. He's quick
at expressing his opinion: he think the town should evacuate, 
as quickly as possible. 'But the Mayor's thick skull doesn't 
seem understand how urgent this is'. He then picks up a call and 
waves you out."""
							print self.chat 
							editspoken = 1
			else:
				print self.chat
		
myhouse = House("home",(0,0))
stevehouse = Steve("steve",(1,-2)) #This is the guy
townhall = Townhall("town hall",(0,-2))
park = Park("park",(-2,2))
sharonhouse = Sharon("sharon",(4,0)) #This is the guy's ex wife
baronhouse = Baron("the baron's mansion",(8,4))
mayoroffice = Mayorplace("mayor's office",(-2,3))
websiteoffice = Website("website administrator's office",(-3,3))
dam = Dam("dam",(4,6))
newspaper = Newspaper("printing press",(0,3))


placedict = {'home': myhouse, 'park': park, 'baron': baronhouse, "baron's": baronhouse, "Baron's": baronhouse, 'mansion': baronhouse, 'mayor': mayoroffice, "mayor's": mayoroffice, "Mayor's": mayoroffice, 'office': mayoroffice, 'dam': dam, 'town':townhall, 'printing': newspaper, 'press': newspaper, 'steve': stevehouse, "steve's": stevehouse, 'Steve': stevehouse, "Steve's": stevehouse, 'sharon': sharonhouse, "sharon's": sharonhouse, 'Sharon': sharonhouse, "Sharon's": sharonhouse}
allplaces = [myhouse, stevehouse, townhall, park, sharonhouse, baronhouse, mayoroffice, websiteoffice, dam, newspaper]

# These are the places that are currently accessible to you
placelist = myhouse.name + ", " + park.name + ", " + baronhouse.name + ", " + mayoroffice.name + ", " + dam.name + ", " + newspaper.name + ", " + townhall.name + ", " + stevehouse.name + ", " + sharonhouse.name + "."
placearray = ['home', 'park', 'baron', "baron's", "Baron's", 'mayor', "mayor's", "Mayor's", 'office', 'dam', 'town', 'printing', 'press', 'steve', "steve's", 'Steve', "Steve's", 'sharon', "sharon's", 'Sharon', "Sharon's"]




# I could even have a thing which determines the difficulty level?
timeleft = 130 #turn this to 100!!!
initialtime = timeleft

#------------------------------I HAVE FINISHED SETTING UP THE WORLD--------------------------

def goout():
	print "\nEverywhere is completely empty."
	print "\nWhere would you like to go? You may go to: \n"
	print placelist
	print ""
	global nextplace 
	nextplace = gamemodule.asktoget(placearray)
	
def moveto(locname):
	global me
	global timeleft
	timeleft = gamemodule.walk(me, locname, timeleft)
	global play1
	global play2
	global play3
	if timeleft <= 0:
		time.sleep(3)
		print """\nYou hear an almighty crack from the Dam. It completely breaks apart, 
letting the entire lake flood over the town. Everything goes under."""
		time.sleep(5)
		print "\n \nTHE END"
		time.sleep(1)
		exit(0)
	elif timeleft < initialtime/10 and play1==0:
		print "\n(The Dam is looks like it will soon break apart!)"
		play1 = 1
	elif timeleft < initialtime/4 and play2==0:
		print "\n(The Dam is looking in a bad shape -- there are big cracks on it)"
		play2 = 1
	elif timeleft < initialtime/2 and play3==0:
		print "\n(You hear some ominous sounds from the Dam...)"
		print "(Time is ticking...)"
		play3 = 1
	
#----------------------------I HAVE FINISHED SETTING UP THE FUNCTIONS------------------------

print "\n \nWelcome to \nTHE OLD TOWN\n \n"
time.sleep(3) 

print """\n \nThere are no rules to the game. However, in most situation the options on
what you can do involve studying the place / looking around, talking
to whoever is present, and exiting the place to go somewhere else.\n \n"""

print "What is your name?\n"
nam = raw_input("> ")
me = Person(nam, myhouse)

print """\nYou wake up one morning in your house. The small town in which
you live is normally bustling with activity, but today it's
unusually silent.\n"""

print "What would you like to do?\n"
todowords = gamemodule.asktoget(['exit','out','look','study','look around','inspect','listen'])

done=0
while done==0:
	if gamemodule.intersect(todowords,['look','study','look around','inspect'])!=[]:
		me.location.inspect()
		print ""
		print "\nWhat would you like to do?\n"
		todowords = gamemodule.asktoget(['exit','out','look','study','look around','listen'])
	elif gamemodule.intersect(todowords,['exit','out'])!=[]:
		goout()
		done = 1
	elif gamemodule.intersect(todowords,['listen'])!=[]:
		print "\nYou hear absolutely nothing -- none of the usual sounds from the town."
		print "\nWhat would you like to do?\n"
		todowords = gamemodule.asktoget(['exit','out','look','study','look around','listen'])

#print "You want to go to:"
#print nextplace[0]

moveto(placedict[nextplace[-1]])

print "\nWhat would you like to do?\n"
todowords = gamemodule.asktoget(['exit','out','look','study','look around','inspect','talk','speak','chat'])

#print todowords


while True:
	#if usecrane==1 and me.location.name==dam.name and gamemodule.intersect(todowords,['crane'])!=[]:
			#print """You find the magnetic crane to still be operable. After jumping in it, you manage to manoeuvre
#it to the area of the dam where the car is presumably blocking the flow. After sinking the crane 
#under the water and activating the magnet, you hear a loud clunk. The crane works hard to tug up, 
#and eventually manages to lift up Sharon's car!"""
			#print """\nThe water is now flowing from both holes in the dam, with huge pressure. It looks like the dam will be OK after all!"""
			#time.sleep(5)		
			#print "\nYOU WON!!! WELL DONE!\n"
			#exit(0)
			
	done=0
	while done==0:
		if usecrane==1 and me.location.name==dam.name and gamemodule.intersect(todowords,['crane'])!=[]:
			print """\nYou find the magnetic crane to still be operable. After jumping in it, you manage to manoeuvre
it to the area of the dam where the car is presumably blocking the flow. After sinking the crane 
under the water and activating the magnet, you hear a loud clunk. The crane works hard to tug up, 
and eventually manages to lift up Sharon's car!"""
			print """\nThe water is now flowing from both holes in the dam, with huge pressure. It looks like the dam will be OK after all!"""
			time.sleep(5)		
			print "\nYOU WON!!! WELL DONE!\n"
			exit(0)
		elif gamemodule.intersect(todowords,['look','study','look around','inspect'])!=[]:
			print ""
			me.location.inspect()
			print "\nWhat would you like to do?\n"
			todowords = gamemodule.asktoget(['exit','out','look','study','look around','inspect','talk','speak','chat','crane'])
		elif gamemodule.intersect(todowords,['exit','out'])!=[]:
			goout()
			done = 1
		elif gamemodule.intersect(todowords,['talk','speak','chat'])!=[]:
			print ""
			me.location.talk()
			print "\nWhat would you like to do?\n"
			todowords = gamemodule.asktoget(['exit','out','look','study','look around','inspect','talk','speak','chat','crane'])
		
	#print "You want to go to:"
	#print nextplace[0]
	
	moveto(placedict[nextplace[-1]])
	
	print "\nWhat would you like to do?\n"
	todowords = gamemodule.asktoget(['exit','out','look','study','look around','inspect','talk','speak','chat','crane'])
			
	
	

	




