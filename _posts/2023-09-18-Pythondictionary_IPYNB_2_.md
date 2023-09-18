---
toc: True
comments: True
layout: post
title: Python Dictionary
courses: {'csp': {'week': 5}}
type: hacks
---

```python
pip install PyDictionary
```

    Collecting PyDictionary
      Downloading PyDictionary-2.0.1-py3-none-any.whl (6.1 kB)
    Collecting bs4 (from PyDictionary)
      Downloading bs4-0.0.1.tar.gz (1.1 kB)
      Installing build dependencies ... [?25ldone
    [?25h  Getting requirements to build wheel ... [?25ldone
    [?25h  Preparing metadata (pyproject.toml) ... [?25ldone
    [?25hCollecting click (from PyDictionary)
      Using cached click-8.1.7-py3-none-any.whl (97 kB)
    Collecting goslate (from PyDictionary)
      Downloading goslate-1.5.4.tar.gz (14 kB)
      Installing build dependencies ... [?25ldone
    [?25h  Getting requirements to build wheel ... [?25ldone
    [?25h  Preparing metadata (pyproject.toml) ... [?25ldone
    [?25hCollecting requests (from PyDictionary)
      Using cached requests-2.31.0-py3-none-any.whl (62 kB)
    Collecting beautifulsoup4 (from bs4->PyDictionary)
      Using cached beautifulsoup4-4.12.2-py3-none-any.whl (142 kB)
    Collecting futures (from goslate->PyDictionary)
      Downloading futures-3.0.5.tar.gz (25 kB)
      Installing build dependencies ... [?25ldone
    [?25h  Getting requirements to build wheel ... [?25ldone
    [?25h  Preparing metadata (pyproject.toml) ... [?25ldone
    [?25hCollecting charset-normalizer<4,>=2 (from requests->PyDictionary)
      Using cached charset_normalizer-3.2.0-cp311-cp311-macosx_11_0_arm64.whl (122 kB)
    Collecting idna<4,>=2.5 (from requests->PyDictionary)
      Using cached idna-3.4-py3-none-any.whl (61 kB)
    Collecting urllib3<3,>=1.21.1 (from requests->PyDictionary)
      Using cached urllib3-2.0.4-py3-none-any.whl (123 kB)
    Collecting certifi>=2017.4.17 (from requests->PyDictionary)
      Downloading certifi-2023.7.22-py3-none-any.whl (158 kB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m158.3/158.3 kB[0m [31m6.6 MB/s[0m eta [36m0:00:00[0m
    [?25hCollecting soupsieve>1.2 (from beautifulsoup4->bs4->PyDictionary)
      Downloading soupsieve-2.5-py3-none-any.whl (36 kB)
    Building wheels for collected packages: bs4, goslate, futures
      Building wheel for bs4 (pyproject.toml) ... [?25ldone
    [?25h  Created wheel for bs4: filename=bs4-0.0.1-py3-none-any.whl size=1256 sha256=7d2a9cc578dfa52a6dbd5fcbfd8acd9058e2156d2be1e35d220a877df0b6b33a
      Stored in directory: /Users/drishyamody/Library/Caches/pip/wheels/d4/c8/5b/b5be9c20e5e4503d04a6eac8a3cd5c2393505c29f02bea0960
      Building wheel for goslate (pyproject.toml) ... [?25ldone
    [?25h  Created wheel for goslate: filename=goslate-1.5.4-py3-none-any.whl size=11579 sha256=83dc8971c96e2a42eede982c704ecab941313f5b1be48f1c52f50978f6fcbc57
      Stored in directory: /Users/drishyamody/Library/Caches/pip/wheels/b6/48/7a/e7458e7a110a5525687dd17a52d3e42c157a8d22a2c4d5e840
      Building wheel for futures (pyproject.toml) ... [?25ldone
    [?25h  Created wheel for futures: filename=futures-3.0.5-py3-none-any.whl size=14068 sha256=1484927bba137556ea489204afae6509ad2114703c1bc8ad166aaa838c6010a2
      Stored in directory: /Users/drishyamody/Library/Caches/pip/wheels/66/cb/37/51fe32ecb9068869196ce81111bdfe82e6ecb53c889362f81b
    Successfully built bs4 goslate futures
    Installing collected packages: futures, urllib3, soupsieve, idna, goslate, click, charset-normalizer, certifi, requests, beautifulsoup4, bs4, PyDictionary
    Successfully installed PyDictionary-2.0.1 beautifulsoup4-4.12.2 bs4-0.0.1 certifi-2023.7.22 charset-normalizer-3.2.0 click-8.1.7 futures-3.0.5 goslate-1.5.4 idna-3.4 requests-2.31.0 soupsieve-2.5 urllib3-2.0.4
    
    [1m[[0m[34;49mnotice[0m[1;39;49m][0m[39;49m A new release of pip is available: [0m[31;49m23.1.2[0m[39;49m -> [0m[32;49m23.2.1[0m
    [1m[[0m[34;49mnotice[0m[1;39;49m][0m[39;49m To update, run: [0m[32;49mpip3 install --upgrade pip[0m
    Note: you may need to restart the kernel to use updated packages.



```python
from PyDictionary import PyDictionary

#Initialize the PyDictionary
dictionary = PyDictionary()

#Function to fetch the meaning of a word
def fetch_meaning(word):
    try:
        meanings = dictionary.meaning(word)
        if meanings:
            for part_of_speech, definition_list in meanings.items():
                print(f"{part_of_speech}:")
                for definition in definition_list:
                    print(f"  - {definition}")
        else:
            print(f"Meaning not found for '{word}'")
    except Exception as e:
        print(f"An error occurred: {e}")

#Simple CLI interface for word lookup
while True:
    user_input = input("Enter a word to lookup (or 'exit' to quit): ").strip()

    if user_input.lower() == 'exit':
        break

    fetch_meaning(user_input)
```

    Noun:
      - an expression of greeting
      - a state in the United States in the central Pacific on the Hawaiian Islands
      - Czechoslovakian religious reformer who anticipated the Reformation; he questioned the infallibility of the Catholic Church was excommunicated (1409
      - 1372-1415

