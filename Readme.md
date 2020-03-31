# KiCad Net Remover
Extremely simple and probably largely improvable tool to remove a specific net from KiCad's netlist file *.net that you use between Eeschema and PCBNew.

I mainly use this tool to remove the GND net while routing in PCBNew and then I add it back in the end.

## How to use it
It's a little python script called `removenet.py` and you use it like this

```
python removenet.py <FileIn> <FileOut> <NETNAME>

## so as an actual example you can write
python removenet.py test.net test-gnd.net GNDD
```
This will effectively create a new file (or overwrite it) and remove the given net from it. So in the example above it takes test.net and generates a new file test-gnd.net that has the net GNDD removed from it.