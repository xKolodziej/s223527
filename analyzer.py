import os
import pandas as pd

print("[filename.split(". ")[0] for filename in os.listdir("./revievs")], sep="\n")
product_id = input("Podaj identyfikator produktu")
      
opinions = pd.read_json("reviews/"+product_id+".json")
      
opinions_count = len(opinions)
pros_count = opinions.pros["pros"].astype(bool).sum()
cons_count = opinions.pros["pros"].astype(bool).sum()  
average_score = opinions["stars"].mean().round(2)
      
recommendations = opinions["recommendation"].
print(pros_count)
