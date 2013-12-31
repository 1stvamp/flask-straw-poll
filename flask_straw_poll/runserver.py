import sys, os
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from flask_straw_poll import app

if __name__ == '__main__':
    app.run()


