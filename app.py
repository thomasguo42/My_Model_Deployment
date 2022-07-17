import numpy as np
import pandas as pd
import pickle
from flask import Flask, request, render_template
import detectron2

app = Flask(__name__)


@app.route('/')
def home():
    print('this is home')
    print ('hello world')
    return render_template('index.html')
