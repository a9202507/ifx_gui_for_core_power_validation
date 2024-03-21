import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def dict_to_df(dict):
    pass
    # input one dict and re
    return None


def plt_vmax(filename, autosave=False):

    df = pd.read_excel(filename, sheet_name="Sheet1")

    matplotlib.use('pdf') # needed for pyinstaller to collect the pdf backend
    matplotlib.use('qtagg') # needed for pyinstaller to collect the qtagg backend
    plt.rcParams.update({'font.size': 8})
    plt.ion()
    fig = plt.figure(figsize=(6.5,10))

    #ax = fig.gca(projection='3d')
    ax = fig.add_subplot(2, 1, 1, projection='3d')
    # Make data.
    X = pd.Series(df['Freq'])
    Y = pd.Series(df['duty'])
    Z = pd.Series(df['Vmax'])
    # Plot the surface.
    surf = ax.plot_trisurf(X, Y, Z, cmap=plt.cm.coolwarm,
                           linewidth=0, antialiased=False)

    # Customize the z axis.
    #ax.set_zlim(1.75, 1.85)
    ax.set_xlabel("Frequency")
    ax.set_ylabel("Duty-Cycle")
    ax.set_zlabel("Vmax", rotation=90)

    ax.zaxis.set_major_locator(plt.LinearLocator(10))
    ax.zaxis.set_major_formatter(plt.FormatStrFormatter('%.02f'))

    # add notice for Vmax point
    highest_point_index = np.argmax(Z)
    highest_point = (X[highest_point_index], Y[highest_point_index], Z[highest_point_index])
    ax.text(X[highest_point_index], Y[highest_point_index], Z[highest_point_index], f'Highest: {highest_point[0]}Khz,{highest_point[1]}Duty,{highest_point[2]} Vol', color='red')

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5, orientation='vertical', pad=0.2)

    plt.title("Vmax vs Frequency/Duty-Cycle")

    ax = fig.add_subplot(2, 1, 2, projection='3d')
    # Make data.
    X = pd.Series(df['Freq'])
    Y = pd.Series(df['duty'])
    Z = pd.Series(df['Vmin'])
    # Plot the surface.
    surf = ax.plot_trisurf(X, Y, Z, cmap=plt.cm.coolwarm,
                           linewidth=0, antialiased=False)

    # Customize the z axis.    
    #ax.set_zlim(1.75, 1.85)
    ax.set_xlabel("Frequency")
    ax.set_ylabel("Duty-Cycle")
    ax.set_zlabel("Vmin", rotation=90)

    ax.zaxis.set_major_locator(plt.LinearLocator(10))
    ax.zaxis.set_major_formatter(plt.FormatStrFormatter('%.02f'))


    # add notice for Vmin point
    lowest_point_index = np.argmin(Z)
    lowest_point = (X[lowest_point_index], Y[lowest_point_index], Z[lowest_point_index])
    ax.text(X[lowest_point_index], Y[lowest_point_index], Z[lowest_point_index], f'Lowest: {lowest_point[0]}Khz,{lowest_point[1]}Duty,{lowest_point[2]} Vol', color='red',zorder=1)

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5, orientation='vertical', pad=0.2)
    plt.title("Vmin vs Frequency/Duty-Cycle")

    if autosave == True:
        plt.savefig(filename.replace(".xlsx", ".pdf").replace(".xls", ".pdf"), bbox_inches='tight')
    plt.show()


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
