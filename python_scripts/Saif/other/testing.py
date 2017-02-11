#imports
import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle
import numpy as np
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA
from flask import Flask
from flask_restful import Resource, Api, reqparse, request
from flask import render_template
from operator import itemgetter 


