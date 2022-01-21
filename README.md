# KiCadBOMGenerator
A simple BOM generator script for KiCad that organizes parts intuitively in a CSV file, with space for inventory and price tracking.
Includes spreadsheet (LibreOffice or Excel) cell calculations to get total component line price from "price each" and quantity, as well as sheet Total. 

Installation:
It only works for me if I put it in /usr/share/kicad/plugins. Just stick the script there, then in KiCad go to the BOM tool (from the schematic editor, Tools > Generae BOM...), click the "plus" button to add a new script, navigate to the place where you stuck the script, give it a name, and voila.
