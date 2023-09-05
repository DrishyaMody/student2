---
layout: post
title: Emoji Print
type: hacks
description: emojis
courses: {"csp": {"week": 2}}
permalink: /emoji-print
---


```python
pip install emoji

```

    Collecting emoji
      Downloading emoji-2.8.0-py2.py3-none-any.whl (358 kB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m358.9/358.9 kB[0m [31m9.7 MB/s[0m eta [36m0:00:00[0m
    [?25hInstalling collected packages: emoji
    Successfully installed emoji-2.8.0
    
    [1m[[0m[34;49mnotice[0m[1;39;49m][0m[39;49m A new release of pip is available: [0m[31;49m23.1.2[0m[39;49m -> [0m[32;49m23.2.1[0m
    [1m[[0m[34;49mnotice[0m[1;39;49m][0m[39;49m To update, run: [0m[32;49mpip3 install --upgrade pip[0m
    Note: you may need to restart the kernel to use updated packages.



```python
from emoji import emojize 
print(emojize(":thumbs_up: Python is awesome! :grinning_face:"))
```

    👍 Python is awesome! 😀

