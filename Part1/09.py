import random

target = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind."

rand_str = lambda s: "".join(random.sample(s, len(s)))
inner_rand_str = lambda s: s[0] + rand_str(s[1:len(s)-1]) + s[-1] if len(s) > 4 else s

print " ".join([inner_rand_str(target) for target in target.split(" ")])
