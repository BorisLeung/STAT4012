# STAT4012

STAT4012 Project - Movie Genre Classification

<strong>\*Important note: Please create a new branch when developing a new feature/model for the sake of good practices!!!</strong>

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

A python file that hosts an array of utility of functions to facilitate data io with the poster images. Image plotting functions are also available!

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

## Some Useful Git Commands for Beginners

### Login

Upon first dealing with `git push`, one may encounter error from VSCode requiring you to sign in. Simply type the following two commands and replace the variables enclosed in \<\> with your own identifications:

```
git config --global user.name <myusername>
git config --global user.email <myemail>
```

### Push Error due to outdated local version

When attempting to push your commits to the remote repository, one may encounter an error that states your push was unsuccessful. This happens as the remote repository is in a newer state than your local repository. But what happens now? You have already committed and it is stuck midway. Fear not, follow these steps:

1. Revert your last commit:

```
git reset HEAD~1
```

2. Stash (i.e. temporarily take away) your changes

```
git stash
```

3. Pull the updated version from remote

```
git pull
```

4. Pop your stashed changes and solve any conflicts

```
git stash pop
```

5. Try push to the remote repository again

```
git commit -m "<your commit message>"
git push
```

Again, replace anything inside \<\> with your own. It is also highly encourage to periodically run `git fetch`(This is also available in VSCode).

### Branching

Branching is an important factor in version control. It allows isolated yet parallel development. As aforementioned, all is advised to work on separate branches for each feature/model. One can create a branch and switch to it via:

```
git checkout -b <branch name>
```

To switch between branches, do:

```
git checkout <branch name>
```

Here, \<branch name\> is any name of your own choice. Be sure to make it concise and intuitive so that everybody else can understand it immediately.

If you deem any source from another branch useful and would like to incorporate it into your own branch, one can achieve so with:

```
git pull <branch name>
```

Be sure to switch to your own branch first, after that will you be able to pull from other branches!
