from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convert', methods=['GET'])
def convert_temperature():
    temperature = request.args.get('temperature', type=float)
    unit = request.args.get('unit', default='celsius')
    
    if unit == 'celsius':
        converted = (temperature * 9/5) + 32
        new_unit = 'fahrenheit'
    else:
        converted = (temperature - 32) * 5/9
        new_unit = 'celsius'
    
    return jsonify({'original_temperature': temperature, 'original_unit': unit, 'converted_temperature': converted, 'new_unit': new_unit})

if __name__ == '__main__':
    app.run(debug=True)