"""Another way to run the app"""

from src import create_app

app = create_app()


@app.route('/')
def home():
    return "Welcome to the Home Page!"


if __name__ == "__main__":
    app.run()
