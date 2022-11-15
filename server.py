from flask import Flask, render_template, request, flash, session, redirect 
from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined 



if __name__ == "__main__":
    connect_to_db(app)
    app.run(port=8000, debug=True)