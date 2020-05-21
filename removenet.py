import sys

net_found = False
search_name = "(name {})".format(sys.argv[3])

with open(sys.argv[1]) as search:
    with open(sys.argv[2],'w') as output:
        for line in search:
            tmpline = line.lstrip()  # remove '\n' at end of line
            if tmpline.startswith("(net") and search_name in tmpline:
                net_found = True
            if tmpline.startswith("(net") and not search_name in tmpline:
                net_found = False
            if not net_found:
                output.write(line)
