import pyrebase
import time
import timeago
from threading import Thread
import datetime
from collections import defaultdict
keyword = ['tweet', '40']


screen_names =['Minrt11', 'bot97959606']

following_list =defaultdict(list)
list_check = defaultdict(list)
config1 = {
	"apiKey": "AIzaSyC3XCuSCDITwKIxKGCUakvibog64wgDFA0",
    "authDomain": "hello-2cf3b.firebaseapp.com",
    "databaseURL": "https://hello-2cf3b.firebaseio.com",
    "projectId": "hello-2cf3b",
    "storageBucket": "hello-2cf3b.appspot.com",
    "messagingSenderId": "527985104277",
    "appId": "1:527985104277:web:910b5310c58ff573db929c",
    "measurementId": "G-45F53VFCJB"
}
config2 = {
    "apiKey": "AIzaSyDmaWg580Z_E3_-yNfs7uamHNQc9SvqQ-o",
    "authDomain": "twitter-12d3d.firebaseapp.com",
    "databaseURL": "https://twitter-12d3d-default-rtdb.firebaseio.com",
    "projectId": "twitter-12d3d",
    "storageBucket": "twitter-12d3d.appspot.com",
    "messagingSenderId": "822417634193",
    "appId": "1:822417634193:web:ecf25704a1a5a72f7b6030",
    "measurementId": "G-Z1E5B9Q14Q"
}

firebase1 = pyrebase.initialize_app(config1)
firebase2 = pyrebase.initialize_app(config2)

db = firebase1.database()
ds = firebase2.database()
from flask import *


app = Flask(__name__)



@app.route('/' , methods=['GET' , 'POST'])
def basic():
	if request.method == 'POST':
		username = request.form['name']
		if(username != ""):
			db.push(username)
			
	h1 = db.get()
	r = h1.val()
	if(r!=None):
		t= r.values()
	else:
		t = {}
		

	return render_template('index.html', t = t)



@app.route('/real' , methods=['GET' , 'POST'])
def real():


	my_dict = {}
	todo = ds.get()
	to = todo.val()
	# print(to)
	zee = list(to)
	value = to.values()
	name = list(value)
	# print(name)

	for a in range(len(zee)):
		my_dict[zee[a]] = {}

		for key, value in name[a].items():

			for key1 in (name[a])[key]:

				my_dict[zee[a]][key] = (((name[a])[key])[key1])


	main = {}
	for a in my_dict:
		for keys in my_dict[a]:
			my_dict[a][keys] = datetime.datetime.strptime(my_dict[a][keys], '%Y-%m-%d %H:%M:%S.%f')
		sorted_dict = {}
		sorted_keys = sorted(my_dict[a], key=my_dict[a].get)  # [1, 3, 2]

		for w in sorted_keys:
			sorted_dict[w] = my_dict[a][w]
		res = dict(reversed(list(sorted_dict.items())))
		main[a] = res
	t = main
	for l in t:
		for k in t[l]:
			string = (str(t[l][k]))
			gg = str(datetime.datetime.now())
			mod_string = ""
			time = ""
			for i in range(len(string) - 7):
				mod_string = mod_string + string[i]
			for i in range(len(gg) - 7):
				time = time + gg[i]				

			t[l][k] = timeago.format(mod_string, time)	
	return render_template('real.html' , t= t)


if __name__ == '__main__' :

	app.run(host="127.0.0.1", port=8080,debug  = True)
