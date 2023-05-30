
import plotting
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import pandas as pd
import os

os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")
GTK_FOLDER = r'C:\Program Files\GTK3-Runtime Win64\bin'
os.environ['PATH'] = GTK_FOLDER + os.pathsep + os.environ.get('PATH', '')

from pandas_profiling import ProfileReport
#import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
from pycaret.clustering import *
#from ydata_profiling import ProfileReport
import weasyprint
from selenium import webdriver
import pdfkit
import io
import base64
from bs4  import BeautifulSoup
import tempfile
from io import BytesIO
# Our Modules
import plotting
#import ML_tools



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
# with st.sidebar:
#     # Add menu options to the sidebar
#     st.title("Build is in Progress")
#     menu_file = st.sidebar.radio('File', ['Choose CSV File'])
#     with st.expander("Data Visualization"):
#         menu_vis = st.sidebar.radio('Visulaize', ['categories',"PairPlot","Pair Plot(category)", 'combination' ])
#     summary_menu = st.sidebar.radio("Summary & Reports",['summary', 'Profiling'] )
#     ML_radios = st.sidebar.radio('ML', ['clusting', 'something'])
# Add menu options to the sidebar
# Add menu options to the sidebar
# Add menu options to the sidebar
st.sidebar.title("aymen.omg@gmail.com")

menu_file = st.sidebar.radio('File', ['Choose CSV File'])

expander_vis = st.sidebar.expander("Data Visualization")
with expander_vis:
    menu_vis = st.radio('Visualize', ['categories', 'PairPlot', 'Pair Plot (category)', 'combination'])

expander_summary = st.sidebar.expander("Summary & Reports")
with expander_summary:
    summary_menu = st.radio('Summary & Reports', ['summary', 'Profiling'])


expander_ml = st.sidebar.expander("ML")
with expander_ml:
    ML_radios = st.radio('ML', ['clustering', 'something'])
 

 # ---------------------------------- Reading data ----------------------------------------

# Read csv
if menu_file == 'Choose CSV File':
    #st.title("Upload your data here")
    csv_file = st.file_uploader("Upload your CSV file", type=["csv"])
    if csv_file:
        df = pd.read_csv(csv_file, index_col=None)
        st.dataframe(df)
       
    else:
        pass



# --------------------------------------Data Summarization ---------------------------------------------

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
    with st.expander("Dataset Report"):
        generateReport_button = st.button("Generate")

        if generateReport_button:
            if 'df' in globals() and not df.empty:
                profile_report = ProfileReport(df, title="Dataset EDA Report")
                st_profile_report(profile_report)
                st.session_state['profile_report'] = profile_report
            else:
                st.warning("No data")
            
           

            # if 'profile_report' in st.session_state:
            #     profile_report = st.session_state['profile_report']
            #     with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as tmp_file:
            #         tmp_filename = tmp_file.name
            #         profile_report.to_file(tmp_filename)

            #     # Allow user to choose file location and name
            #     file_name = st.text_input("Enter file name", value="report.pdf")

            #     # Render the HTML with WeasyPrint and save as PDF
            #     pdf = weasyprint.HTML(tmp_filename).write_pdf()

            #     # Save the PDF file
            #     with open(file_name, "wb") as file:
            #         file.write(pdf)

            #     # Display the download link
            #     pdf_file = open(file_name, "rb").read()
            #     b64_pdf = base64.b64encode(pdf_file).decode('utf-8')
            #     href = f'<a href="data:application/pdf;base64,{b64_pdf}" download="{file_name}">Click here to download the PDF file</a>'
            #     st.markdown(href, unsafe_allow_html=True)

            #     st.success("Report exported to PDF successfully!")
            # else:
            #     st.warning("No report generated yet")
                 

   

             
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
                 
elif menu_vis == 'Pair Plot (category)':
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
    st.write("Not implemented yet...")
                            

# ----------------------  ML -----------------------------------

if ML_radios == 'clustering':
    if  'df' in globals() and not df.empty:
        
         st.title('Setup data & show clustring information ')
         with st.expander("Setup Summery"):
           
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
                
               
