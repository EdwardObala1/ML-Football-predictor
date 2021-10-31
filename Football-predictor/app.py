import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("r_regressor.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Hello Welcome to kelvins page"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(Reactions,Composure,Aggression,BallControl, Skill_Moves, ShortPassing, ShotPower, FKAccuracy, LongPassing):
   
    prediction=classifier.predict([[Reactions,Composure,Aggression,BallControl, Skill_Moves, ShortPassing, ShotPower, FKAccuracy, LongPassing]])
    print(prediction)
    return prediction

'Reactions','Composure','Aggression','BallControl','Skill_Moves','ShortPassing','ShotPower','FKAccuracy','LongPassing'

def main():
    st.title("Fifa player predictor")
    html_temp = """
    <div style="background-color:#033923;padding:10px">
    <h2 style="color:white;text-align:center;">Machine learning class project app </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Age = st.slider("Age", 0, 100)
    Nationality = st.input("Nationality", 0, 100)
    Club = st.text_input("Club", 0, 100)
    Value = st.text_input('Value', 0, 100)
    Wage = st.text_input('ShortPassing', 0, 100)
    Special = st.slider('ShotPower', 0, 100)
    PrefferdFoot = st.text_input('FKAccuracy', 0, 100)
    InternationalReputation = st.slider('LongPassing', 0, 100)
    SkillMoves = st.slider("Reactions", 0, 100)
    WorkRate = st.slider("Composure", 0, 10)
    Position = st.slider("Aggression", 0, 200)
    LS = st.slider("BallControl", 0, 100)
    ST = st.slider('Skill_Moves', 0, 100)
    RS = st.slider('ShortPassing', 0, 100)
    LW = st.slider('ShotPower', 0, 100)
    LF = st.slider('FKAccuracy', 0, 100)
    CF = st.slider('LongPassing', 0, 100)
    RF = st.slider("BallControl", 0, 100)
    RW = st.slider('Skill_Moves', 0, 100)
    LAM = st.slider('ShortPassing', 0, 100)
    LCM = st.slider('ShotPower', 0, 100)
    CM = st.slider('FKAccuracy', 0, 100)
    RCM = st.slider('LongPassing', 0, 100)
    RM = st.slider("BallControl", 0, 100)
    LWB = st.slider('Skill_Moves', 0, 100)
    LDM = st.slider('ShortPassing', 0, 100)
    CDM = st.slider('ShotPower', 0, 100)
    RDM = st.slider('FKAccuracy', 0, 100)
    RWB = st.slider('LongPassing', 0, 100)
    LB = st.slider("BallControl", 0, 100)
    LCB = st.slider('Skill_Moves', 0, 100)
    CB = st.slider('ShortPassing', 0, 100)
    RCB = st.slider('ShotPower', 0, 100)
    RB = st.slider('FKAccuracy', 0, 100)
    Crossing = st.slider('Skill_Moves', 0, 100)
    LDM = st.slider('ShortPassing', 0, 100)
    CDM = st.slider('ShotPower', 0, 100)
    RDM = st.slider('FKAccuracy', 0, 100)
    RWB = st.slider('LongPassing', 0, 100)
    LB = st.slider("BallControl", 0, 100)
    LCB = st.slider('Skill_Moves', 0, 100)
    CB = st.slider('ShortPassing', 0, 100)
    RCB = st.slider('ShotPower', 0, 100)
    RB = st.slider('FKAccuracy', 0, 100)
   
   'Crossing',
 'Finishing',
 'HeadingAccuracy',
 'ShortPassing',
 'Volleys',
 'Dribbling',
 'Curve',
 'FKAccuracy',
 'LongPassing',
 'BallControl',
 'Reactions',
 'ShotPower',
 'Strength',
 'Aggression',
 'Interceptions',
 'Positioning',
 'Vision',
 'Penalties',
 'Composure',
 'Release Clause']


    result=""
    if st.button("Predict"):
        result=predict_note_authentication(Reactions,Composure,Aggression,BallControl, 
                                          Skill_Moves, ShortPassing, ShotPower, FKAccuracy, LongPassing)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()

# small change

	['Age',
 'Nationality',
 'Club',
 'Value',
 'Wage',
 'Special',
 'Preferred Foot',
 'International Reputation',
 'Skill Moves',
 'Work Rate',
 'Body Type',
 'Position',
 'Joined',
 'Contract Valid Until',
 'LS',
 'ST',
 'RS',
 'LW',
 'LF',
 'CF',
 'RF',
 'RW',
 'LAM',
 'CAM',
 'RAM',
 'LM',
 'LCM',
 'CM',
 'RCM',
 'RM',
 'LWB',
 'LDM',
 'CDM',
 'RDM',
 'RWB',
 'LB',
 'RB',
 'Crossing',
 'Finishing',
 'HeadingAccuracy',
 'ShortPassing',
 'Volleys',
 'Dribbling',
 'Curve',
 'FKAccuracy',
 'LongPassing',
 'BallControl',
 'Reactions',
 'ShotPower',
 'Strength',
 'Aggression',
 'Interceptions',
 'Positioning',
 'Vision',
 'Penalties',
 'Composure',
 'Release Clause']