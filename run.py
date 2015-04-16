# !/usr/bin/env python
# -*- coding: utf-8 -*-

from src import app
from src.controllers import controllers
from src.services import services

app.register_blueprint(controllers)
app.register_blueprint(services)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
    #app.run()
    
