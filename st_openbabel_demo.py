import streamlit as st
import pandas as pd
import tempfile

#from openbabel import pybel
from openbabel import openbabel
from st_table_select_cell import st_table_select_cell

st.header("Openbabel test")
st.write("Select a molecul to visualize:")

# Open data in sdf format:
#molecules = pybel.readfile("sdf","demo.sdf")

# Convert to a list of molecules:
#moleculeList = []
#for item in molecules:
#    moleculeList.append(item)
    
# Prepare a dataframe:
#data = pd.DataFrame({'Molecules':["molecule "+str(i) for i in range(len(moleculeList))]})

#col1, col2 = st.columns(2)

#with col1:
#    # Show table and get user selected cell:
#    selectedCell = st_table_select_cell(data)
#    if selectedCell != False:
#        
#        # Visualize a molecule using a temporary file:
#        file = tempfile.NamedTemporaryFile(suffix = ".png", delete = True)
#        
#        st.write(str("temporary file name is " + file.name))
#        
#        moleculeList[int(selectedCell["rowId"])].draw(show = False, filename = file.name)
#        
#        st.image(file.name, caption="Visualization")
#        
#with col2:
#    st.write("Select a subgraph:")
#    
#    st.write("To be done.")
