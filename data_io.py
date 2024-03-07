"""
A module that facilitates the reading and writing of data to and from files.
"""

import os

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import pandas as pd

from const import *


def get_poster(movie_id: str | int) -> np.ndarray:
    """
    Retrieves the poster image for a given movie.

    Parameters:
        movie_id (str | int): The ID of the movie.

    Returns:
        np.ndarray: The image data as a NumPy array.

    Example:
        >>> get_poster(1000005) # get the poster for the movie with ID 1000005
        array([[[ 5,  7, 19],
                [ 5,  7, 19],
                [ 5,  7, 19],
                ...,
                [ 6,  5, 13],
                [ 6,  5, 13],
                [ 6,  5, 13]],

               [[ 4,  6, 18],
                [ 4,  6, 18],
                [ 4,  6, 18],
                ...,
                [ 6,  5, 11],
                [ 6,  5, 11],
                [ 6,  5, 11]],

               [[ 4,  6, 18],
                [ 4,  6, 18],
                [ 4,  6, 18],
                ...,
                [ 6,  5, 11],
                [ 6,  5, 11],
                [ 6,  5, 11]],

                ...,

               [[21, 18, 25],
                [20, 17, 24],
                [20, 17, 24],
                ...,
                [ 1,  4, 13],
                [ 2,  5, 14],
                [ 3,  6, 15]],

               [[20, 18, 23],
                [19, 17, 22],
                [19, 16, 23],
                ...,
                [ 1,  4, 13],
                [ 2,  5, 14],
                [ 3,  6, 15]],

               [[22, 17, 23],
                [20, 15, 21],
                [20, 18, 23],
                ...,
                [ 1,  4, 13],
                [ 1,  4, 13],
                [ 2,  5, 14]]], dtype=uint8)
    """
    poster_path = os.path.join(POSTER_DIR, f"{movie_id}.jpg")
    img = mpimg.imread(poster_path)
    return img


encoded_genres_df = pd.read_csv("encoded_genres.csv", index_col=0).drop(
    columns=[GENRE_COUNT]
)


def plot_poster(
    movie_id: str | int,
    reveal_genre: bool = False,
    no_ticks: bool = True,
    show: bool = True,
) -> mpimg.AxesImage:
    """
    Plot the poster of a movie based on its ID.

    Parameters:
        movie_id (str | int): The ID of the movie.
        reveal_genre (bool, optional): Whether to reveal the genre of the movie. Defaults to False.
        no_ticks (bool, optional): Whether to hide the ticks on the plot. Defaults to True.
        show (bool, optional): Whether to display the plot. Defaults to True.

    Returns:
        mpimg.AxesImage: The AxesImage object representing the plot.

    Example:
        >>> plot_poster(1000005, True) # movie with ID 1000005 plotted with its genres revealed

    """
    movie_id = int(movie_id)
    ax = plt.imshow(get_poster(movie_id))
    plt.title(f"Movie ID: {movie_id}")
    if no_ticks:
        plt.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
    if reveal_genre:
        movie_genres = encoded_genres_df.columns[
            encoded_genres_df.loc[movie_id, encoded_genres_df.any()]
        ]

        plt.text(
            0,
            380 - 20 * int(no_ticks),
            f"Genre{'s' if len(movie_genres) > 1 else ''}: {', '.join(genre[1:] for genre in movie_genres)}",
            fontsize=8,
        )
    if show:
        plt.show()
    return ax
