import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def dict_to_df(dict):
    pass
    # input one dict and re
    return None


def plt_vmax(filename, autosave=False):

    df = pd.read_excel(filename, sheet_name="Sheet1")

    # Get the unique values and counts
    unique_freqs = df['Freq'].unique()
    unique_duties = df['duty'].unique()
    n_freqs = len(unique_freqs)
    n_duties = len(unique_duties)

    # Reshape Vmax and Vmin into 2D arrays
    vmax_2d = df['Vmax'].values.reshape(n_freqs, n_duties)
    vmin_2d = df['Vmin'].values.reshape(n_freqs, n_duties)

    # Create a figure with two 3D surface plots side by side
    fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'surface'}, {'type': 'surface'}]])

    # Add the first surface plot (freq/vmax/duty)
    fig.add_trace(go.Surface(z=vmax_2d, x=unique_freqs, y=unique_duties), row=1, col=1)
    fig.update_scenes(xaxis_title='Frequency', yaxis_title='Duty Cycle', zaxis_title='Vmax', row=1, col=1)

    # Add the second surface plot (freq/vmin/duty)
    fig.add_trace(go.Surface(z=vmin_2d, x=unique_freqs, y=unique_duties), row=1, col=2)
    fig.update_scenes(xaxis_title='Frequency', yaxis_title='Duty Cycle', zaxis_title='Vmin', row=1, col=2)

    # Customize plot layout
    fig.update_layout(
        title='Interactive 3D Surface Plots',
        margin=dict(l=65, r=50, b=65, t=90),
        scene_camera=dict(eye=dict(x=1.5, y=1.5, z=1.5))  # Adjust the camera view
    )

    # Display the plot
    fig.show()



def plt_vmin(filename):

    df = pd.read_excel(filename, sheet_name="Sheet1")

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Make data.
    X = pd.Series(df['Freq'])
    Y = pd.Series(df['duty'])
    Z = pd.Series(df['Vmin'])
    # Plot the surface.
    surf = ax.plot_trisurf(X, Y, Z, cmap=plt.cm.coolwarm,
                           linewidth=0, antialiased=False)

    # Customize the z axis.
    #ax.set_zlim(1.75, 1.85)
    ax.set_xlabel("Freq")
    ax.set_ylabel("duty")
    ax.set_zlabel("Vmin")

    ax.zaxis.set_major_locator(plt.LinearLocator(10))
    ax.zaxis.set_major_formatter(plt.FormatStrFormatter('%.02f'))

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()


if __name__ == "__main__":

    plt_vmax("./report/IFX_DB425_Don_100.0A_0.0A_report_2022_0609_1131.xls")
