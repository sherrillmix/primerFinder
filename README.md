# primerFinder
Rought test of concept to find primer fragment length relatively quickly. 

```
usage: primerFinder.py [-h] [-v] -i INPUTFILE -p PATTERNFILE [-o OUTFILE]

Python program to primer location pairs in a DNA sequence

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         increase output verbosity
  -i INPUTFILE, --inputFile INPUTFILE
                        file to find primers in (assumes the file contains
                        only DNA sequence, i.e. no headers, and that newlines
                        are not significant)
  -p PATTERNFILE, --patternFile PATTERNFILE
                        primer file with one primer per line all 5' to 3'
  -o OUTFILE, --outFile OUTFILE
                        file to write to
```

Example usage:
```
./primerFinder.py -i inputExample.txt -p primersExample.txt -v
```
The commands generates a csv file of position,fragmentLength in output.csv (use `-o` or `--output` to change).
