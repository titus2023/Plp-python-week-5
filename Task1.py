class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery = battery  # in mAh

    def make_call(self, number):
        return f"Calling {number} from {self.brand} {self.model}..."

    def charge(self):
        return f"{self.brand} {self.model} is charging."

    def get_info(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage and {self.battery}mAh battery."

class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery = battery  # in mAh

    def make_call(self, number):
        return f"Calling {number} from {self.brand} {self.model}..."

    def charge(self):
        return f"{self.brand} {self.model} is charging."

    def get_info(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage and {self.battery}mAh battery."


class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, storage, battery, camera_megapixels):
        super().__init__(brand, model, storage, battery)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        return f"Taking a photo with {self.camera_megapixels}MP camera."

    # Polymorphism: 
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} It also has a {self.camera_megapixels}MP camera."
      
