import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import pandas as pd
import spacy

# spacy.download("en")
nlp = spacy.load("en_core_web_md")

df = pd.read_csv("B00CHTPGIS.csv")
reviews = str(df["reviews"].iloc[4])

lem = WordNetLemmatizer()

text_tokens = word_tokenize(reviews)
all_stopwords = stopwords.words('english')
all_stopwords.append([",", ".", "//", ":", ";", "'"])
list2 = [word for word in text_tokens if not word in all_stopwords]
filtered_sentence = " ".join(list2)

size_keywords_string = "Size, small, tiny, petite, slim, compact, large, big, giant,\
huge, enormous, gigantic, bulky, colossal, massive, sizable, weight, heavy, lightweight, cumbersome"

quality_keywords_string = "Build, built, quality,durability, sturdy, sturdiness, durable, tough, scratch, scratch,\
coating, solid, cheaply, aluminum, steel, titanium, brass, copper,\
material, metal, rubber, plastic, nylon, bent, broke, faulty, shatter,\
waterproof, dustproof, corrosion, ingress, drop, shock, impact, resistance,\
screws, threads, knurling, anodized, flicker, housing, indestructible,\
wet, temperature, hot, heat, overheat, cold,  well"

battery_keywords_string = "Battery, batteries, rechargeable, charge, charging,\
recharge, USB, solar, runtime, hours, lifetime, dies, died, dead"

design_keywords_string = "Features, design, setting, settings, mode, modes,\
interface, programmable, memory, dim, roll, design, roll, upright, stand, tailstanding, \
strobe, sos, float, warranty, grip, rotate, rotating, head, hang, lantern, eco, adjustable,\
zoom, clip, lanyard, holster, indicator, easy to use, versatile, switch, twist,\
activation, clicky, click, magnetize, accessories, bezel"

beam_keywords_string = "Power, project, projects, far, illuminate, shine,\
focus, distance, range, feet, meters, beam, distance, visibility, throw, \
flood, lumens, bright, brightness, lens, optics, frosted, reflector, mule, LED, tint, \
colour, color, hotspot, spill, corona, lux, candelas, intensity, lights"

price_keywords_string = "Price, cost, costly, pricey, pricy, expensive, overpriced, reasonable,\
unreasonable, value, affordable, cheap, $, bargain, budget, cash, discount, money, sale"

list1 = "size durable battery beam price"
# size_keywords = size_keywords_string.lower().replace(" ","").split(",")
# quality_keywords = quality_keywords_string.lower().replace(" ","").split(",")
# battery_keywords = battery_keywords_string.lower().replace(" ","").split(",")
# design_keywords = design_keywords_string.lower().replace(" ","").split(",")
# beam_keywords = beam_keywords_string.lower().replace(" ","").split(",")
# price_keywords = price_keywords_string.lower().replace(" ","").split(",")

# list1 = size_keywords + quality_keywords + battery_keywords + design_keywords + beam_keywords + price_keywords

tokens = nlp(filtered_sentence)
tokens1 = nlp(list1)
for token in tokens:
    for tkn in tokens1:
        if (token and token.vector_norm) and (tkn and tkn.vector_norm):
            if round(token.similarity(tkn), 2) >= 0.40:
                print(token.text, tkn.text, token.similarity(tkn))
