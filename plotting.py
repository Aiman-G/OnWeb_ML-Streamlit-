import matplotlib.pyplot as plt
import mplcursors
import streamlit as st
import seaborn as sns

def plotCat(df, cat_col, x_col,y_col):
    # Clear previous plot
    plt.clf()
    groups = df.groupby(cat_col)

    #plt.clf()
    # Create a subplot for each unique device
    num_of_values = len(groups)
    fig, axs = plt.subplots(num_of_values, 1, figsize=(10, 5*num_of_values))

    # Loop over each temp group and create plots for each combination of categorical variables
    for i, (temp_value, device_data) in enumerate(groups):
        # Group the data by remaining categorical variables
        subgroups = device_data.groupby(cat_col)
        # Create a plot for each subgroup
        
            
        for j, ( group_name, group_data) in enumerate(subgroups):
            
            axs[i].plot(group_data[x_col], group_data[y_col], label=group_name)
        # Set the title and legend for the subplot
        
        axs[i].set_title(f' Col: {cat_col}, Value: {temp_value} ')
        #axs[i].legend(prop={"size": 6})
        axs[i].set_xlabel(x_col)
        axs[i].set_ylabel(y_col)
        
        # Use mplcursors to show the legend when the mouse hovers over the plot
        mplcursors.cursor(axs[i].get_lines(), hover=True).connect("add", lambda sel: sel.annotation.set_text(sel.artist.get_label()))
     
     
    
    # Set the overall title for the figure
    #fig.suptitle("Interactive plot: Plots for each test temprature and categorical variable combination")
    # Add space between subplots
    #fig.subplots_adjust(hspace=0.5)

    # Show the figure
    #plt.show() 
    st.pyplot(plt.gcf())

def Pair_plots(df):
    sns.pairplot(df)
    st.pyplot(plt.gcf())

def Pair_plots_hue(df , col_name):
    sns.pairplot(df , hue=col_name)
    st.pyplot(plt.gcf())
