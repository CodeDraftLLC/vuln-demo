from flask import Flask, request, render_template_string
import yaml

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to the vulnerable app!"

@app.route("/unsafe", methods=["POST"])
def unsafe_yaml():
    data = request.data.decode("utf-8")
    loaded = yaml.load(data, Loader=yaml.FullLoader)  # Unsafe: allows code execution!
    return str(loaded)

if __name__ == "__main__":
    app.run(debug=True)
