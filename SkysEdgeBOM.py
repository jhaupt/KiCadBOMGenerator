"""
    @package
    Output: CSV (comma-separated)
    Grouped By: Value, Footprint
    Sorted By: Ref
    Fields: Ref, Qnty, Value, Cmp name, Footprint, Description, Vendor

    Command line:
    python "pathToFile/bom_csv_grouped_by_value_with_fp.py" "%I" "%O.csv"
"""

# Import the KiCad python helper module and the csv formatter
import kicad_netlist_reader
import kicad_utils
import csv
import sys

# A helper function to convert a UTF8/Unicode/locale string read in netlist
# for python2 or python3
def fromNetlistText( aText ):
    if sys.platform.startswith('win32'):
        try:
            return aText.encode('utf-8').decode('cp1252')
        except UnicodeDecodeError:
            return aText
    else:
        return aText

# Generate an instance of a generic netlist, and load the netlist tree from
# the command line option. If the file doesn't exist, execution will stop
net = kicad_netlist_reader.netlist(sys.argv[1])

# Open a file to write to, if the file cannot be opened output to stdout
# instead
try:
    f = kicad_utils.open_file_write(sys.argv[2], 'w')
except IOError:
    e = "Can't open output file for writing: " + sys.argv[2]
    print(__file__, ":", e, sys.stderr)
    f = sys.stdout

# Create a new csv writer object to use as the output formatter
out = csv.writer(f, delimiter=',', quotechar='\"', quoting=csv.QUOTE_ALL)

# Column titles
out.writerow(['Qty', 'Stock', 'Description', 'Ref Des', 'Manufacturer', 'Part No.', 'Cost Each', 'Cost per ASM', ' ','Footprint'])


# Get all of the components in groups of matching parts + values
# (see ky_generic_netlist_reader.py)
grouped = net.groupComponents()

# Output all of the component information
n=2
for group in grouped:
    refs = ""
    # Add the reference of every component in the group and keep a reference
    # to the component so that the other data can be filled in once per group
    for component in group:
        refs += fromNetlistText( component.getRef() ) + ", "
        c = component

    # Fill in the component groups common data
    out.writerow([
        len(group), 
        0, 
        fromNetlistText( c.getValue() ),
        refs, 
        fromNetlistText( c.getField("Mfg. Name") ),
        fromNetlistText( c.getField("Mfg. Part No.") ),
        0,
        "=A%d*G%d" %(n,n),
        " ",
        fromNetlistText( c.getFootprint() )
    ])
    n=n+1
# Write a final output row totaling the component prices
out.writerow([
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    "TOTAL:",
    "=SUM(H3:H%d)" %(n-1)       #Give column total
])
