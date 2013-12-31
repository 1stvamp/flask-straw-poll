import sys, os
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from flask_straw_poll import app

def main():
    app.run()
    return 0

if __name__ == '__main__':
    sys.exit(main())
