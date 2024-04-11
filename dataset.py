import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from torch.utils.data import Dataset
from torchvision import transforms


from data_io import get_poster


class PosterDataset(Dataset):
    csv_file = "encoded_genres.csv"
    IMG_SIZE = [224, 224]

    @classmethod
    def get_default_transform(cls):
        return transforms.Compose(
            [
                transforms.ToPILImage(),
                transforms.Resize(cls.IMG_SIZE),
                transforms.ToTensor(),
                transforms.Normalize(
                    mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
                ),
            ]
        )

    def __init__(self, indices=None, transform_=None):
        """
        Initializes the PosterDataset class.

        Args:
            indices (list or None): List of indices to select from the dataset. If None, all indices will be used.
            transform_ (torchvision.transforms.Compose or None): Custom transformation to apply to the data. If None, a default transformation will be used.

        Attributes:
            data (pandas.DataFrame): The dataset loaded from a CSV file.
            transform (torchvision.transforms.Compose): The transformation to apply to the data.

        """
        self.data = pd.read_csv(self.csv_file)
        if indices is not None:
            self.data = self.data.iloc[indices, :]

        if transform_ is not None:
            self.transform = transform_
        else:
            self.transform = self.get_default_transform()

    def __len__(self):
        """
        Returns the length of the dataset.

        Returns:
            int: The length of the dataset.

        """
        return len(self.data)

    def __getitem__(self, idx):
        """
        Retrieves a sample from the dataset at the given index.

        Args:
            idx (int): The index of the sample to retrieve.

        Returns:
            tuple: A tuple containing the transformed image sample and the array of features.

        """
        movie_id, *features, genre_count = self.data.iloc[idx, :]
        img = get_poster(movie_id)
        if self.transform:
            sample = self.transform(img)
        return sample, np.array(features).astype(np.float32)


def get_datasets(test_size: float = 0.2, random_state: int = 42, **kwargs):
    """
    Load the dataset and split it into train and test datasets.

    Parameters:
    - test_size (float): The proportion of the dataset to include in the test split.
    - random_state (int): The seed used by the random number generator.
    - **kwargs: Additional keyword arguments to be passed to the PosterDataset constructor.

    Returns:
    - train_dataset (PosterDataset): The training dataset.
    - test_dataset (PosterDataset): The test dataset.
    """
    data = pd.read_csv(PosterDataset.csv_file)
    train_indices, test_indices = train_test_split(
        data.index, test_size=test_size, random_state=random_state
    )

    train_dataset = PosterDataset(indices=train_indices, **kwargs)
    test_dataset = PosterDataset(indices=test_indices, **kwargs)
    return train_dataset, test_dataset
