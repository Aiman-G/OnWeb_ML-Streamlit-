
import plotting
import streamlit as st
from PIL import Image
import pandas as pd
import os
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
from pycaret.clustering import *
import plotting
import ML_tools

st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        width: 250px;
        background-color: #f8f9fa;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add photo to the sidebar
image = Image.open('D:\cSharp_dataVisu\Thabab\ploticon22.png')
st.sidebar.image(image, use_column_width=True)
with st.sidebar:
    # Add menu options to the sidebar
    st.title("Build is in Progress")
    menu_file = st.sidebar.radio('File', ['Choose CSV File'])
    menu_vis = st.sidebar.radio('Visulaize', ['categories',"PairPlot","Pair Plot(category)", 'combination' ])
    summary_menu = st.sidebar.radio("Summary & Reports",['summary', 'Profiling'] )
    ML_radios = st.sidebar.radio('ML', ['clusting', 'something'])

 
 

# Read csv
if menu_file == 'Choose CSV File':
    #st.title("Upload your data here")
    csv_file = st.file_uploader("Upload your CSV file", type=["csv"])
    if csv_file:
        df = pd.read_csv(csv_file, index_col=None)
        st.dataframe(df)
       
    else:
        pass


# ------------- Data Summarization ---------------------------------------------

content_placeholder = st.empty()  
if summary_menu == 'summary' :
    
    st.title("Summary")
    with st.expander("Summary"):
        content_placeholder.empty()  # Clear previous content
        if 'df' in globals() and not df.empty:
            # Display the DataFrame description in Streamlit
            st.dataframe(df.describe())
elif summary_menu == 'Profiling':
    st.title("EDA")
    with st.expander(" Profiling Report"):
            
        if  'df' in globals() and not df.empty:
            profile_report = df.profile_report()
            st_profile_report(profile_report)
        else:
            st.write("No data")

# ------------------------ Plotting ----------------------------------
if menu_vis == 'categories':
    content_placeholder.empty()  # Clear previous content
    st.title("Plot Categories ")
    if 'df' in globals() and not df.empty:
        # Get column names from df
       column_names = df.columns.tolist()
       with st.expander("Expand to see selction variables"):
        
        # Create combo boxes and populate them with column names
        selected_cat_col = st.selectbox("Select Cate. ", column_names)
        selected_x_col = st.selectbox("Select X column ", column_names)
        selected_y_col = st.selectbox("Select Y column ", column_names)
        plot_cat_button = st.button("Plot","plot_cat_button" )

       if plot_cat_button:
            
            if selected_cat_col and selected_x_col and selected_y_col:
                plotting.plotCat(df, selected_cat_col, selected_x_col,selected_y_col )
                #st.write(f"You selected {selected_cat_col} and {selected_x_col}")
elif menu_vis == 'PairPlot':
    content_placeholder.empty()  # Clear previous content
    st.title("Pair Plots")
    if 'df' in globals() and not df.empty:
        with st.expander("Piar Plots"):
             content_placeholder.empty()  # Clear previous content
             with st.spinner("Ploting in progress.."):
                 plotting.Pair_plots(df)
                 
elif menu_vis == "Pair Plot(category)":
    content_placeholder.empty()  # Clear previous content
    st.title("Pair Plots by category")
    if 'df' in globals() and not df.empty:
        
        with st.expander("Piar Plots"):
             
             selected_hue_col = st.selectbox("Select Cate. ", df.columns)
             plot_pair_button = st.button("Plot","plot_pair_button" )
             if plot_pair_button:
                 with st.spinner("Ploting in Progress.. "):
                     plotting.Pair_plots_hue(df,selected_hue_col)
                   

elif menu_vis == 'combination':
    st.write("Work in progress..")
                            

# ----------------------  ML -----------------------------------

if ML_radios == 'clusting':
    if  'df' in globals() and not df.empty:
        
         st.title('Setup data & show clustring information ')
         with st.expander("Setup Summery"):
           

            #st.subheader('Setup data befor clustring Categorical Columns for Clustering')
            execlud_cols = st.multiselect('Choose columns to execlude ', options=df.columns)
            setup_button = st.button('Setup Data', "setup_button")
            if setup_button:
                with st.spinner("Processing & producing summary .."):
                    setup_experiment = setup(df, normalize = True, ignore_features = execlud_cols, session_id = 123)
                    setup_summary = setup_experiment.pull()
                    st.write(setup_summary)
                    kmeans = create_model('kmeans')
                    st.write("kmeans parameters")
                    st.write(kmeans)
                st.write("processing is done!")
                                
                with st.spinner("Clustring & plotting..."):
                                     
                    kmean_results = assign_model(kmeans)
                    st.write("kmeans result")
                    st.write(kmean_results)
                    plot_model(kmeans,display_format='streamlit')
                
               
