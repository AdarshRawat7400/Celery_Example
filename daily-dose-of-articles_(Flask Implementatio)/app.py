from articleapp import app
from articleapp.routes import celery

if __name__ == '__main__':
    app.run(debug=True)


 
