print(



'''

 /$$$$$$$  /$$$$$$$$  /$$$$$$  /$$$$$$$$        /$$$$$$  /$$$$$$$  /$$$$$$      
| $$__  $$| $$_____/ /$$__  $$|__  $$__/       /$$__  $$| $$__  $$|_  $$_/      
| $$  \ $$| $$      | $$  \__/   | $$         | $$  \ $$| $$  \ $$  | $$        
| $$$$$$$/| $$$$$   |  $$$$$$    | $$         | $$$$$$$$| $$$$$$$/  | $$        
| $$__  $$| $$__/    \____  $$   | $$         | $$__  $$| $$____/   | $$        
| $$  \ $$| $$       /$$  \ $$   | $$         | $$  | $$| $$        | $$        
| $$  | $$| $$$$$$$$|  $$$$$$/   | $$         | $$  | $$| $$       /$$$$$$      
|__/  |__/|________/ \______/    |__/         |__/  |__/|__/      |______/      
                                                                                
                                                                                
                                                                                
             ############ Coded By Ahmed^_^Mahmoud ############



'''











	)

from flask import Flask,render_template,request

app = Flask(__name__)


gpsinfo = [

	{

	
	'items': [

		{
			
			'lng':'any number for lng','lat':'number for lat','speed':'number for speed m/s'

		}

			]

		}

	]



@app.route('/location',methods=['GET','POST']) #GET  info for location

def get_gpsinfo():
	
	arg1 = request.args['arg1']
	arg2 = request.args['arg2']
	x = gpsinfo
	return render_template('index.html',data=x,Arg1=arg1,Arg2=arg2)
	return 'Arg1 : '+ arg1 + 'Arg2 : ' + arg2



app.run(port=4000)



'''
to run it open the terminal and type 

python3 test_restapi.py

then open your browser and put this link

http://127.0.0.1:4000/location?arg1=hi&arg2=hello

you can change values of parameters when you rander it 

'''
