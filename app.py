from flask import Flask, render_template
from main import InventoryManager

app = Flask(__name__)
manager = InventoryManager()

@app.route('/')
def index():
    return render_template('index.html', inventory=manager.inventory)

if __name__ == '__main__':
    app.run(debug=True)