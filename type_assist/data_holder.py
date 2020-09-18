from type_assist.config import config
from type_assist.data_validate import ValidateName


class Dataset:
    """ A dataset from a single source """

    valid_names = config['valid_datasets']
    dataset_name = ValidateName(valid_names)

    def __init__(self, dataset_name):
        self.dataset_name = dataset_name
        self._build_dataset()

    def _build_dataset(self):
        ds = ...
        return ds


class CompositeDataset:
    """ A collection of Dataset objects into one DataFrame """

    def __init__(self, dataset_names=config['dataset_names']):
        self.dataset_names = dataset_names
        self.datasets = [Dataset(name) for name in dataset_names]


class FederatedDataset(Dataset):
    """ A dataset with federated learning capabilities and protections """

    def __init__(self, name):
        super().__init__(name)

