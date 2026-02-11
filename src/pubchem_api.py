import requests

class PubChemAPI:
    BASE_URL = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug'

    @staticmethod
    def search_drug(drug_name):
        """Search for a drug by name and return its CID."""
        response = requests.get(f'{PubChemAPI.BASE_URL}/compound/name/{drug_name}/cids')
        if response.status_code == 200:
            return response.json()['IdentifierList']['CID']
        else:
            raise Exception(f'Error fetching data: {response.status_code}')

    @staticmethod
    def get_molecular_properties(cid):
        """Fetch molecular properties for a given Compound ID (CID)."""
        response = requests.get(f'{PubChemAPI.BASE_URL}/compound/cid/{cid}/property/MolecularWeight,HeavyAtomCount,AromaticAtomCount/JSON')
        if response.status_code == 200:
            return response.json()['PropertyTable']['Properties'][0]
        else:
            raise Exception(f'Error fetching data: {response.status_code}')

    @staticmethod
    def handle_api_request(request):
        """A generic handler for processing API requests and responses."""
        try:
            return request.json()
        except ValueError:
            raise Exception('Invalid JSON response')  

# Example usage:
# cid = PubChemAPI.search_drug('Aspirin')
# properties = PubChemAPI.get_molecular_properties(cid)