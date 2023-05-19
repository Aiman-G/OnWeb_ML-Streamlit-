
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
    menu_vis = st.sidebar.radio('Visulaize', ['categories', 'combination'])
    summary_menu = st.sidebar.radio("Summary & Reports",['summary', 'Profiling'] )
    #profiling_button = st.sidebar.radio("Profiling","profiling_button")
   #delete_localFile_button =  st.sidebar.button("Delete uploded profile","delete_localFile_button")
    #summary_button = st.sidebar.radio("summary","summary_button")
    #clustring_button = st.sidebar.button("Clusters", "clustring_button")
    ML_radios = st.sidebar.radio('ML', ['clusting', 'something'])

 
 #if os.path.exists("uplodedFile.csv"):
   # app_path = os.path.dirname(os.path.abspath(__file__))
  #  file_path = os.path.join(app_path, "uploadedFile.csv")
  #  df = pd.read_csv(file_path, index_col=None) 
    


# Read csv
if menu_file == 'Choose CSV File':
    #st.title("Upload your data here")
    csv_file = st.file_uploader("Upload your CSV file", type=["csv"])
    if csv_file:
        df = pd.read_csv(csv_file, index_col=None)

        #df.to_csv(file_path, index=None)
        st.dataframe(df)
       # st.success(f"File saved at: {file_path}")
    else:
        #df = pd.read_csv(file_path, index_col=None)
        pass

   
if summary_menu == 'summary' :
    st.write("Summary")
    with st.expander("Summary"):
        if 'df' in globals() and not df.empty:
            # Display the DataFrame description in Streamlit
            st.dataframe(df.describe())
elif summary_menu == 'Profiling':
    #st.write('You selected profiling')
    st.title("EDA")
    with st.expander(" Profiling Report"):
            
        if  'df' in globals() and not df.empty:
            profile_report = df.profile_report()
    
            st_profile_report(profile_report)
        else:
            st.write("No data")


if menu_vis == 'categories':
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
            # Example code to use the selected column names
            if selected_cat_col and selected_x_col and selected_y_col:
                plotting.plotCat(df, selected_cat_col, selected_x_col,selected_y_col )
                #st.write(f"You selected {selected_cat_col} and {selected_x_col}")

       


if menu_file == 'Save CSV':
    st.write('You selected Save CSV, not implemented yet')

if menu_vis == 'combination':
    st.write("Work in progress..")
    
   




if ML_radios == 'clusting':
    if  'df' in globals() and not df.empty:
        
         st.subheader('Setup data befor clustring ')
         with st.expander("Setup Summery"):
           

            #st.subheader('Setup data befor clustring Categorical Columns for Clustering')
            execlud_cols = st.multiselect('Choose columns to execlude ', options=df.columns)
            setup_button = st.button('Setup Data', "setup_button")
            if setup_button:
                setup_experiment = setup(df, normalize = True, ignore_features = execlud_cols, session_id = 123)
                setup_summary = setup_experiment.pull()
                st.write(setup_summary)
                st.write("processing is done!")
                
                kmeans = create_model('kmeans')
                st.write("kmeans parameters")
                st.write(kmeans)
                kmean_results = assign_model(kmeans)
                st.write("kmeans result")
                st.write(kmean_results)
                plot_model(kmeans,display_format='streamlit')
                
               
