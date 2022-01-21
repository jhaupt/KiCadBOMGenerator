# KiCadBOMGenerator
A simple BOM generator script for KiCad that organizes parts intuitively in a CSV file, with space for inventory and price tracking.
Includes spreadsheet (LibreOffice or Excel) cell calculations to get total component line price from "price each" and quantity, as well as sheet Total. 

It expects part fields called "Mfg. Name" and "Mfg. Part No.", which I add to all parts in my projects. You can easily add these (or any) fields to all parts in a project using the "Edit Schematic Setup Button" by adding Field Name Templates with the little red gear in KiCad6. Just add the names of the fields you want included. 

Installation:
It only works for me if I put it in /usr/share/kicad/plugins. Just stick the script there, then in KiCad go to the BOM tool (from the schematic editor, Tools > Generae BOM...), click the "plus" button to add a new script, navigate to the place where you stuck the script, give it a name, and voila. Generated BOM CSV files will get generated right in your project's workign directory. 

~Justine
