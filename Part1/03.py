str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

for ele in str.split(" "):
    print '%d' % len(ele if ele[-1].isalpha() else ele[0:len(ele)-1]),
