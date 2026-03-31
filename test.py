import pickle

with open("encoder_mappings.pkl", "rb") as f:
    mappings = pickle.load(f)

print(type(mappings))