import pandas as pd

def predict(filename):
#your dataset
    df = pd.read_csv("product.csv")
#IDs you should find their corresponding brands
    brand = df[]
    prod_id = read_input(filename)
#write your code here



##############################
    return brand, brandUniq, categUniq, BrCat


def read_input(filename):
    contents = []
    f = open(filename, "r")
    for line in f:
        contents.append(int(line))
    return contents
