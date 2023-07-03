import streamlit as st
import random
from matplotlib import pyplot as plt
from PIL import Image

st.markdown("<h1 style='text-align: center;font-size: 62px; color: Blue;'>Dice Roller</h1>", unsafe_allow_html=True)

def make_grid(cols,rows):
    grid = [0]*cols
    for i in range(cols):
        with st.container():
            grid[i] = st.columns(rows)
    return grid
    
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #1BAF14;
    color:#ffffff;
    }
</style>""", unsafe_allow_html=True)

mygrid = make_grid(3,3)  




no=1 

mygrid_1 = make_grid(3,5) 
submitted = mygrid_1[2][2].button("Roll the Dice!") 
if submitted:
	# Generates a random number
    # between 1 and 6 (including both 1 and 6)
    no = random.randint(1,6)
  
    
    
     
if no == 1:
	img = Image.open(r"C:\Users\INVASEE\Downloads\dice_images\dice_images\dice_1.png")
	mygrid[1][1].image(img)	
	
if no == 2:
	img = Image.open(r"C:\Users\INVASEE\Downloads\dice_images\dice_images\dice_2.png")
	mygrid[1][1].image(img)
	
if no == 3:
	img = Image.open(r"C:\Users\INVASEE\Downloads\dice_images\dice_images\dice_3.png")
	mygrid[1][1].image(img)
	
if no == 4:
	img = Image.open(r"C:\Users\INVASEE\Downloads\dice_images\dice_images\dice_4.png")
	mygrid[1][1].image(img)
	
if no == 5:
	img = Image.open(r"C:\Users\INVASEE\Downloads\dice_images\dice_images\dice_5.png")
	mygrid[1][1].image(img)
	
if no == 6:
	img = Image.open(r"C:\Users\INVASEE\Downloads\dice_images\dice_images\dice_6.png")
	mygrid[1][1].image(img)	

