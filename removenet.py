import sys

net_found = False

with open(sys.argv[1]) as search:
    with open(sys.argv[2],'w') as output:
        for line in search:
            tmpline = line.lstrip()  # remove '\n' at end of line
            if tmpline.startswith("(net") and sys.argv[3] in tmpline:
                net_found = True
            if tmpline.startswith("(net") and not sys.argv[3] in tmpline:
                net_found = False
            if not net_found:
                output.write(line)