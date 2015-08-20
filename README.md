# zendesk-csv-converter
Simple Python script to convert to/from Zendesk CSV and PO Files for translations

Quick example usage:
Need either -c for CSV->PO or -p for PO->CSV 
-i <inputfile> 
-o <outputfile>

Examples:
To convert from CSV to PO
python convert.py -c -i ./csv_files/en-US.csv -o ./po_files/en-US.pot

To convert from PO to CSV
python convert.py -p -i ./po_files/for_use_zendesk-csv-1_en-uspot-1_de.po -o ./csv_files/de.csv

returns what was converted
Converted " ./po_files/for_use_zendesk-csv-1_en-uspot-1_de.po " to " ./csv_files/de.csv "
