from flask import Flask, jsonify, request, json

app = Flask(__name__)
todos = [
  { "label": "Sample todo 1", "done": True },
  { "label": "Sample todo 2", "done": True }
]




@app.route('/todos', methods=['GET'])
def hello_world():
  text = jsonify(todos)
  return text



@app.route('/todos', methods=['POST'])
def add_new_todo():
  body = request.data
  object = json.loads(body)
  todos.append(object)
  text = jsonify(todos)
  print("Incoming request with the following body", body)
  return text

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
  todos.pop(position)
  text = jsonify(todos)
  print("This is the position to delete: ",position)
  return text

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)