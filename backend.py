from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("frontpage.html")

@app.route("/send", methods=["POST"])
def send_text():
    data = request.get_json()
    message = data.get("message", "")
    return jsonify({"received": message})

if __name__ == "__main__":
    app.run(debug=True)
