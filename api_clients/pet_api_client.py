from api_clients.abstract_api_client import AbstractApiClient


class PetApiClient(AbstractApiClient):
    def find_by_status(self, status_value):
        return self._get_pet_store('pet/findByStatus', status=status_value)

    def pet(self, pet_data: dict):
        return self.post("pet", pet_data)

    def update_pet(self, pet_data: dict):
        return self.put("pet", pet_data)

    def find_by_id(self, pet_id):
        return self.get("pet/" + str(pet_id))

    def find_by_tags(self, pet_tags):
        return self._get_pet_store('pet/findByTags', tags=pet_tags)



