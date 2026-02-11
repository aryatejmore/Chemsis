import numpy as np
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances

class MoleculeSimilarity:
    def __init__(self, molecules):
        self.molecules = molecules

    def calculate_similarity(self, query_molecule):
        similarities = {}
        for molecule in self.molecules:
            # Calculate cosine similarity
            cos_sim = cosine_similarity(query_molecule.reshape(1, -1), molecule.reshape(1, -1))[0][0]
            # Calculate Euclidean distance
            euc_dist = euclidean_distances(query_molecule.reshape(1, -1), molecule.reshape(1, -1))[0][0]
            similarities[molecule] = (cos_sim, euc_dist)
        return similarities

    def find_closest_molecule(self, query_molecule):
        similarities = self.calculate_similarity(query_molecule)
        # Finding the closest molecule based on cosine similarity and minimum Euclidean distance
        closest_by_cosine = max(similarities, key=lambda x: similarities[x][0])
        closest_by_euclidean = min(similarities, key=lambda x: similarities[x][1])
        return closest_by_cosine, closest_by_euclidean

if __name__ == '__main__':
    # Example usage
    molecules_data = [
        np.array([0.1, 0.2, 0.3]),
        np.array([0.3, 0.2, 0.1]),
        np.array([0.2, 0.3, 0.4])
    ]
    query = np.array([0.2, 0.2, 0.2])
    similarity_calculator = MoleculeSimilarity(molecules_data)
    closest_cosine, closest_euclidean = similarity_calculator.find_closest_molecule(query)
    print(f'Closest by Cosine Similarity: {closest_cosine}')
    print(f'Closest by Euclidean Distance: {closest_euclidean}')