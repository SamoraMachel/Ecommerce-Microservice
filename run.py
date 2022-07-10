from run import get_app, get_db
import os

app = get_app()
db = get_db()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)