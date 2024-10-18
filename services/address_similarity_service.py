from fuzzywuzzy import fuzz


class AddressSimilarityService:
    def __init__(self, address_list):
        self.address_list = address_list

    def find_similar_addresses(self, target_address, threshold=80):
        similar_addresses = []

        for address in self.address_list:
            similarity_score = fuzz.ratio(
                target_address.lower(), address.lower())
            if similarity_score >= threshold:
                similar_addresses.append((address, similarity_score))

        return similar_addresses
