import sqlite3
conn = sqlite3.connect('IoT.db')
c = conn.cursor()

#a = c.fetchall()

c.execute("SELECT * FROM DHT22_Humidity_Data")
humidity_data = c.fetchall()
c.execute("SELECT * FROM DHT22_Temperature_Data")
temperature_data = c.fetchall()
#>>> a[1]
#(2, 'Dummy-1', '13-Aug-2018 20:20:28:342326', '68.44')
conn.close()

def parse(data, data_name):
	parsed = {}
	print("numberi bu haci ", len(data))
	for i in data[::-1]:
		i_d = i[0]
		SensorID = i[1]
		date = i[2]
		data1 = i[3]
		
		parsed[i_d] = []
		parsed[i_d].append({
			"SensorID" : SensorID,
			"date" : date,
			data_name : data1
			})
	print(type(parsed))
	return parsed

#print(parse(humidity_data))



from flask import Flask, jsonify, g, request, render_template

app = Flask(__name__)

app.config["JSON_SORT_KEYS"] = True
@app.route('/')
def hello():
	return """ 
		<H1>Hello Motherfuckers<H1>
<a href="/temperature">Temperature</a>
<a href="/humidity">Humidity</a>

	"""

@app.route('/humidity')
def humi():
	#return jsonify(hello='world')
	return jsonify(parse(humidity_data, 'humidity'))

@app.route('/temperature')
def tempi():
	return jsonify(parse(temperature_data,'temperature'))


app.config["JSON_SORT_KEYS"] = False
if __name__ == '__main__' : app.run(debug=True, host='0.0.0.0', port=3003)
