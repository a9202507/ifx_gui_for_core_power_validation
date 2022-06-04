import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


def dict_to_df(dict):
    pass
    # input one dict and re
    return None


def plt_vmax(filename):

    df = pd.read_excel(filename, sheet_name="Sheet1")

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Make data.
    X = pd.Series(df['item1'])
    Y = pd.Series(df['item2'])
    Z = pd.Series(df['item3'])
    # Plot the surface.
    surf = ax.plot_trisurf(X, Y, Z, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)

    # Customize the z axis.
    #ax.set_zlim(1.75, 1.85)
    ax.set_xlabel("item1")
    ax.set_ylabel("item2")
    ax.set_zlabel("item3")

    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()


def plt_vmin(filename):

    df = pd.read_excel(filename, sheet_name="Sheet1")

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Make data.
    X = pd.Series(df['item1'])
    Y = pd.Series(df['item2'])
    Z = pd.Series(df['item4'])
    # Plot the surface.
    surf = ax.plot_trisurf(X, Y, Z, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)

    # Customize the z axis.
    #ax.set_zlim(1.75, 1.85)
    ax.set_xlabel("item1")
    ax.set_ylabel("item2")
    ax.set_zlabel("item4")

    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()


if __name__ == "__main__":
    print(1)
    plt_vmax("30.0A_10.0.xls")
