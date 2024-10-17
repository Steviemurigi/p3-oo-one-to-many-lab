class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if not isinstance(name, str):
            raise Exception("Name must be a string.")
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type '{pet_type}'. Must be one of {Pet.PET_TYPES}.")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        
        Pet.all.append(self)
        
        if owner:
            owner.add_pet(self)

    @property
    def pet(self):
        return self.pet_type
    
    @pet.setter
    def pet(self, value):
        if value not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type '{value}'. Must be one of {Pet.PET_TYPES}.")
        self.pet_type = value

class Owner:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string.")
        
        self.name = name
        self.pets_list = []

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Only objects of type 'Pet' can be added.")
        
        pet.owner = self
        self.pets_list.append(pet)

    def pets(self):
        return self.pets_list

    def get_sorted_pets(self):
        return sorted(self.pets_list, key=lambda pet: pet.name)


