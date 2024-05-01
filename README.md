# STAT4012

STAT4012 Project - Movie Genre Classification

<strong>\*Important note: Please create a new branch when developing a new feature/model for the sake of good practices!!!</strong>

## Table of Content

1. [Quick Start](#quick-start)
2. [Important Files](#important-files)
3. [Some Useful Git Commands for Beginner](#some-useful-git-commands-for-beginners)

## Quick Start

### Data

Create a folder named `data` under the same directory as this readme file and move all the data within. The folder should holds the same structure as presented in our [Kaggle source](https://www.kaggle.com/datasets/gsimonx37/letterboxd).

<strong>\*Or, one can simply unzip the data and move the folder under the same directory as this readme file and rename the folder name to `data`.</strong> As long as the poster images exists under the relative path: `./data/posters/`, you are good to go.

_Side Note: Opening the `posters` directory is highly discouraged as it is going to take forever unless you have a supercomputer._

### Python Environment (Optional)

#### Mac Users

Conda environment is used as of the date of writing this section(The author of this section also happens to have a device with the M2Pro Chip). The `mac.yaml` should be present under the same directory as this readme file should be able to create a new conda environment. Simply use:

```
conda create -f mac.yaml
```

However, most of the times this is not going to work. Below details the steps taken to generate the aforementioned environment.

```
conda create -n <env_name> python=3.11 anaconda
conda activate <env_name>
conda install pytorch::pytorch torchvision torchaudio -c pytorch
```

-   Note: replace \<env_name\> with your own name for your local environment. `stat4012proj` was chosen for `mac.yaml`.
-   Note: The last line above is to install PyTorch. The line was generated from the official [PyTorch docs](https://pytorch.org/get-started/locally/). One can ignore this line if PyTorch is not necessary.

## Important Files

### const.py

A python file that contains only constant variables that are expected to be shared amongst different python files and jupyter notebooks. Should only contains <strong>all-capital</strong> variables that are meant to be used globally, for example, column names.

### data_io.py

A python file that hosts an array of utility of functions to facilitate data io with the poster images. Image plotting functions are also available, namely:

```python
from data_io import plot_poster

plot_poster(1000005, True) # movie with ID 1000005 plotted with its genres revealed
```

This will generate:

![an example of a plotted movie poster](./img/example_movie.png)

### encoded_genres.csv

The main dish of our project, with movie ID's serving as its index column. The rest of the columns are one-hot encoded genres of each movie. There is also an additional column at the end counting up the number of genres present. Note that this file has already been cleaned, so that the maximum number of genres of a movie will be 4.

### poster_sizes.csv

A csv file containing all poster images and their corresponding image sizes. Note that here some images cannot be opened and are ignored. Below is the file's columns, their types and descriptions:

| Column name | Type                 | Description                                |
| ----------- | -------------------- | ------------------------------------------ |
|             | int                  | The index column                           |
| movie_id    | int                  | The movie ID of the poster                 |
| size        | str, holding a tuple | The image size of the corresponding poster |

### valid_movies.csv

A csv file containing movie_id's that are considered valid, of which can be opened and has its image size of the most common type amongst all poster images (i.e., `(345, 230, 3)`). This file contains only 2 columns: index, and movie_id.
