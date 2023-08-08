from app import create_app
import sys
import os

print("PYTHONPATH:", sys.path)
print("Current Directory:", os.getcwd())


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
