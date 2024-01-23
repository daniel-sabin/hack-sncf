from flask import Flask, jsonify, redirect


FRONTEND_URL = "http://localhost:3000"

def create_app() -> Flask:
    app = Flask(__name__)
    #CORS(app)

    @app.route("/login")
    def login():
        return redirect(f"{FRONTEND_URL}?username=defacto")
        # redirect()
        # return jsonify({'username': 'defacto'})


    @app.route("/ping")
    def ping():
        print("ping requested")
        return "pong"

    @app.route("/")
    def home():
        print("home")
        return "home"


    return app


if __name__ == "__main__":
    create_app().run(debug=True, host="0.0.0.0", port=5000)
