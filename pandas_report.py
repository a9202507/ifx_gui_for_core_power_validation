import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.offline as pyo
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

def plt_2d(filename, autosave=False,sheet_name="row",vmin_spec=0,vmax_spec=1.5):
    # Read the data
    df = pd.read_excel(filename,sheet_name=sheet_name)

    # Create figure
    fig = go.Figure()

    # Get unique duty cycles
    duty_cycles = sorted(df['duty'].unique())

    # Color scale
    colors = [
        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
        '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'
    ]

    # Add traces for each duty cycle
    for i, duty in enumerate(duty_cycles):
        mask = df['duty'] == duty
        # Add Vmax (solid line)
        fig.add_trace(
            go.Scatter(
                x=df[mask]['Freq'],
                y=df[mask]['Vmax'],
                name=f'Duty {duty}% (Vmax)',
                mode='lines+markers',
                line=dict(
                    color=colors[i % len(colors)],
                    dash='solid'
                ),
                marker=dict(
                    size=6,
                    symbol='circle'
                ),
                legendgroup=f'duty_{duty}'
            )
        )
        
        # Add Vmin (dashed line)
        fig.add_trace(
            go.Scatter(
                x=df[mask]['Freq'],
                y=df[mask]['Vmin'],
                name=f'Duty {duty}% (Vmin)',
                mode='lines+markers',
                line=dict(
                    color=colors[i % len(colors)],
                    dash='dash'
                ),
                marker=dict(
                    size=6,
                    symbol='square'
                ),
                legendgroup=f'duty_{duty}'
            )
        )

    # Add horizontal lines for Vmax_spec and Vmin_spec
    fig.add_shape(
        type='line',
        x0=df['Freq'].min(), 
        x1=df['Freq'].max(), 
        y0=vmax_spec, 
        y1=vmax_spec,
        line=dict(
            color='Green',
            width=2,
            dash='dashdot'
        ),
        name='Vmax_spec'
    )

    fig.add_shape(
        type='line',
        x0=df['Freq'].min(), 
        x1=df['Freq'].max(), 
        y0=vmin_spec, 
        y1=vmin_spec,
        line=dict(
            color='Red',
            width=2,
            dash='dashdot'
        ),
        name='Vmin_spec'
    )

    # Update layout
    fig.update_layout(
        title='Voltage vs Frequency for Different Duty Cycles',
        xaxis_title='Frequency (KHz)',
        yaxis_title='Voltage (V)',
        hovermode='x unified',
        showlegend=True,        
        legend=dict(
            groupclick="toggleitem"
        )
    )

    # Display the plot
    #fig.show()
    # Display the plot using offline mode
    pyo.plot(fig, filename='voltage_vs_frequency.html')

def plt_3d(filename, autosave=False,sheet_name="row"):
    # Load the data
    df = pd.read_excel(filename,sheet_name=sheet_name)

    # Assume there are corresponding 'Vmax' and 'Vmin' values for each pair of 'Freq' and 'duty'
    # Transform the data into a 2D matrix form, assuming df has been gridified by (Freq, duty)
    # Need to ensure the unique values and their sorting corresponding to Freq and duty
    freq_unique = df['Freq'].unique()
    duty_unique = df['duty'].unique()
    freq_unique.sort()
    duty_unique.sort()

    # Create the grid
    freq_grid, duty_grid = np.meshgrid(freq_unique, duty_unique)

    # Corresponding 'Vmax' and 'Vmin' for each grid point
    vmax_grid = df.pivot(index='duty', columns='Freq', values='Vmax').values
    vmin_grid = df.pivot(index='duty', columns='Freq', values='Vmin').values

    # Create subplots containing two 3D surfaces
    fig = make_subplots(
        rows=1, cols=2,
        specs=[[{'type': 'surface'}, {'type': 'surface'}]],
        subplot_titles=('3D Surface Plot of Vmax', '3D Surface Plot of Vmin'),
        horizontal_spacing=0  # Set horizontal spacing between subplots to 0
    )

    # Define the color range for Vmax and Vmin
    colorscale_vmax = [[0, 'rgb(255,255,255)'], [1, 'rgb(255,0,0)']]  # White to red
    colorscale_vmin = [[0, 'rgb(255,255,255)'], [1, 'rgb(0,0,255)']]  # White to blue

    # Add the first surface plot (Vmax)
    fig.add_trace(
        go.Surface(x=freq_grid, y=duty_grid, z=vmax_grid, colorscale='Inferno',
                   hovertemplate='freq=%{x} Khz<br>duty=%{y} Pct<br>Vmax=%{z} Vol<extra></extra>',
                   colorbar=dict(title='Vmax', thickness=20, len=0.6, x=0.01)),  # Adjust the position of the color axis
        row=1, col=1
    )

    # Add the second surface plot (Vmin)
    fig.add_trace(
        go.Surface(x=freq_grid, y=duty_grid, z=vmin_grid, colorscale='Viridis',
                   hovertemplate='freq=%{x} Khz<br>duty=%{y} Pct<br>Vmin=%{z} Vol<extra></extra>',
                   colorbar=dict(title='Vmin', thickness=20, len=0.6, x=0.99)),  # Adjust the position of the color axis
        row=1, col=2
    )

    # Update the layout
    fig.update_layout(
        title_text="3D Surface Plots of Vmax and Vmin",
        title_x=0.5,
        xaxis_title="Freq (Hz)",
        yaxis_title="Duty (%)",
        scene=dict(
            xaxis_title_text="Freq (Hz)",
            yaxis_title_text="Duty (%)",
            zaxis_title_text="Value"
        )
    )

    # Manually set the x-axis, y-axis, and z-axis titles for the left plot
    fig.update_scenes(
        row=1, col=1,
        xaxis_title="Freq (Hz)",
        yaxis_title="Duty (%)",
        zaxis_title="Vmax"
    )

    # Manually set the x-axis, y-axis, and z-axis titles for the right plot
    fig.update_scenes(
        row=1, col=2,
        xaxis_title="Freq (Hz)",
        yaxis_title="Duty (%)",
        zaxis_title="Vmin"
    )

    # Display the plot
    #fig.show()
    pyo.plot(fig, filename='voltage_vs_frequency_3D.html')


if __name__ == "__main__":

    plt_vmax("./report/IFX_DB425_Don_100.0A_0.0A_report_2022_0609_1131.xls")
