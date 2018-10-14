import sqlite3
conn = sqlite3.connect('IoT.db')
c = conn.cursor()

#a = c.fetchall()



def take_data(data):
	conn = sqlite3.connect('IoT.db')
	c = conn.cursor()
	c.execute("SELECT * FROM DHT22_Humidity_Data LIMIT 20")
	humidity_data = c.fetchall()
	c.execute("SELECT * FROM DHT22_Temperature_Data LIMIT 20")
	temperature_data = c.fetchall()
	conn.close()
	return temperature_data, humidity_data



def parse(data_name):
	conn = sqlite3.connect('IoT.db')
	c = conn.cursor()
	if (data_name == 'humidity'):
		c.execute("SELECT * FROM DHT22_Humidity_Data ORDER BY id DESC LIMIT 20")
		data = c.fetchall()
	elif (data_name == 'temperature'):
		c.execute("SELECT * FROM DHT22_Temperature_Data ORDER BY id DESC LIMIT 20 " )
		data = c.fetchall()
	conn.close()
	return data
'''
	parsed = {}
	for i in data:
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
#	print(type(parsed))
#	print(parsed)
'''

#print(parse(humidity_data))



from flask import Flask, jsonify, g, request, render_template
app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

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
	return jsonify(parse('humidity'))

@app.route('/temperature')
def tempi():
	return jsonify(parse('temperature'))


if __name__ == '__main__' : app.run(debug=True, host='0.0.0.0', port=3003 )
