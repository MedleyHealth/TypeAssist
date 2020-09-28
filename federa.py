from exceptions import ProtectionError

class Assembly:
    """ A collection of Component objects """


class ComponentType(type):
    """ A type for pipeline components """

    def __new__(mcs, name, bases, dict_):

        instance = super().__new__(mcs, name, bases, dict_)

        return instance


class Intake(metaclass=ComponentType):
    """
    An intake component for loading data. Can only connect to a ProtectedTank
    instance.


    """

    def __init__(self):
        pass


class Pipe(metaclass=ComponentType):
    """
    A pipe component for moving data from Point A to Point B

    :param point_a: str - Path for the data source
    :param point_b: str - Path for the data destination
    """

    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def check_integrity(self):
        """ Checks the data integrity of a data flow """


class Fitting(metaclass=ComponentType):
    """
    A fitting component for connecting two or more pipes. Will randomly split
    data flowing out into "pipes_out" pieces

    :param pipes_in: int - The number of pipes coming in
    :param pipes_out: int - The number of pipes coming out
    """

    def __init__(self, pipes_in, pipes_out=1):
        self.pipes_in = pipes_in
        self.pipes_out = pipes_out


class Valve(metaclass=ComponentType):
    """ A valve component for controlling the flow of data """


class Queue(Valve):
    """ A queue component for queueing a data flow"""


class Filter(metaclass=ComponentType):
    """ A filter component for removing data from the pipeline """


class Tank(metaclass=ComponentType):
    """ A tank component for storing data at a location """


class ProtectedTank(Tank):
    """
    A protected tank component for data that cannot leave the tank

    :param protected_names: list - The names of variables that cannot be sent
    """

    def __init__(self, protected_ids):
        self.protected_ids = protected_ids

    def __call__(self, model, instructions):
        pass

    def pump_data(self, dataset_id, location):
        """
        Selects a dataset by ID and sends it to a location.

        :param dataset_id: int - ID of the dataset
        :param location: str - Path to the data receiver
        """

        if self.dataset_id in self.protected_ids:
            raise ProtectionError


class Screen(metaclass=ComponentType):
    """ A screen component for viewing the state of a component """


class Pump(metaclass=ComponentType):
    """ A pump component for  """


class Hose(metaclass=ComponentType):
    """ A hose component for portable and flexible data moving """


class Processor(metaclass=ComponentType):
    """ A processor component for running computations on data """


class Controller(metaclass=ComponentType):
    """ A controller component for controlling a collection of components """


class MainController(Controller):
    """
    A controller component for controlling a federated network """

    def add_host(self, host):
        self.hosts.append(host)


class Host:
    """
    A machine with zero or more datasets and/or models

    :param ip_address: str - The IP address of the host machine with data / models
    :param port: int - The port for inbound communication
    """

    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port
        self.datasets = []
        self.models = []

    def add_dataset(self):
        pass

    def remove_dataset(self):
        pass

    def add_model(self):
        pass

    def remove_model(self):
        pass