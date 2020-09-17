class ValidateName:
    def __init__(self, valid_names):
        self.valid_names = valid_names

    def __set_name__(self, _, property_name):
        self.property_name = property_name

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return getattr(instance, self.property_name, None)

    def __set__(self, instance, value):
        if value not in self.valid_names:
            raise ValueError(f'Invalid {self.property_name}={value} for class={type(instance)}. Please choose from {self.valid_names}!')
        setattr(instance, self.property_name, value)
