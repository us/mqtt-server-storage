from flask import Flask, jsonify, g, request, render_template
import sqlite3


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


app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

@app.route('/')
def hello():
	return """ <div align="center">
		<H1>Hello Motherfuckers<H1>
			<a>What do you want ? </a><br>
		<a href="/temperature">Temperature</a>
		<a href="/humidity">Humidity</a></div>
	"""

@app.route('/humidity')
def humi():
	#return jsonify(hello='world')
	return jsonify(parse('humidity'))

@app.route('/temperature')
def tempi():
	return jsonify(parse('temperature'))


if __name__ == '__main__' : app.run(debug=True, host='0.0.0.0', port=3003 )
