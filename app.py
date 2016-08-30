
import os
from app import create_app, db
from app.models import Student


app = create_app('production')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
