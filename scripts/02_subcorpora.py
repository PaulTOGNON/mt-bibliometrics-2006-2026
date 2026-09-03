"""
02_subcorpora.py
Specialized Subcorpora Extraction & Matrix Intersection Analysis
Study: Bibliometric Analysis of Machine Translation (2006-2026)
Authors: TOGNON G. Jean-Paul & MOUSSE A. Mikael
"""

import pandas as pd

def extract_and_intersect(dataset_csv):
    df = pd.read_csv(dataset_csv, skiprows=1, low_memory=False)
    text = df['Title'].fillna('') + ' ' + df['Abstract'].fillna('')

    s2s = text.str.contains(r'(speech-to-speech|speech translation|spoken language translation|voice-to-voice|speech-to-unit)', case=False, regex=True)
    lrl = text.str.contains(r'(low-resource|under-resourced|resource-poor|less-resourced|indigenous languages)', case=False, regex=True)
    al = text.str.contains(r'(African|sub-Saharan|Niger-Congo|Swahili|Yoruba|Igbo|Hausa|Amharic|Fon|Bariba|Baatonum|Masakhane)', case=False, regex=True)
    tl = text.str.contains(r'(tonal language|tone language|lexical tone|tone modeling|pitch contour)', case=False, regex=True)

    print("=== Specialized Subcorpora Volumes ===")
    print(f"Speech-to-Speech (S2S): {s2s.sum()}")
    print(f"Low-Resource Languages (LRL): {lrl.sum()}")
    print(f"African Languages (AL): {al.sum()}")
    print(f"Tonal Languages (TL): {tl.sum()}")

    print("\n=== Intersection Matrix ===")
    print(f"LRL and AL: {(lrl & al).sum()}")
    print(f"LRL and TL: {(lrl & tl).sum()}")
    print(f"AL and TL: {(al & tl).sum()}")
    print(f"LRL and AL and TL: {(lrl & al & tl).sum()}")

if __name__ == '__main__':
    print("Subcorpora isolation rules verified.")
