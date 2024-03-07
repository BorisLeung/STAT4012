# STAT4012

STAT4012 Project - Movie Genre Classification

## Quick Start

### Data

Create a folder named `data` under the same directory as this readme file and move all the data within. The folder should holds the same structure as presented in our [Kaggle source](https://www.kaggle.com/datasets/gsimonx37/letterboxd)

### Python Environment

#### Mac Users

Conda environment is used as of the date of writing this section(The author of this section also happens to have a device with the M2Pro Chip). The `mac.yaml` should be present within under the same directory as this readme file should be able to create a new conda environment. Simply use:

```
conda create -f mac.yaml
```

However, most of the times this is not going to work. Below details the steps taken to generate the aforementioned environment.

```
conda create -n <env_name> python=3.11 anaconda
conda install pytorch::pytorch torchvision torchaudio -c pytorch
```

-   Note: replace \<env_name\> with your own name for your local environment. `stat4012proj` was chosen for `mac.yaml`.
-   Note: The second line above is to install PyTorch. The line was generated from the official [PyTorch docs](https://pytorch.org/get-started/locally/)

## Files

### const.py

A python file that contains only constant variables that are expected to be shared amongst different python files and jupyter notebooks. Should only contains <strong>all-capital</strong> variables that are meant to be used globally, for example, column names.

### poster_sizes.csv

A csv file containing all poster images and their corresponding image sizes. Note that here some images cannot be opened and are ignored. Below is the file's columns, their types and descriptions:

| Column name | Type                 | Description                                |
| ----------- | -------------------- | ------------------------------------------ |
|             | int                  | The index column                           |
| movie_id    | int                  | The movie ID of the poster                 |
| size        | str, holding a tuple | The image size of the corresponding poster |

### valid_movies.csv

A csv file containing movie_id's that are considered valid, of which can be opened and has its image size of the most common type amongst all poster images (i.e., `(345, 230, 3)`). This file contains only 2 columns: index, and movie_id.
