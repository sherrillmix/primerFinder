# primerFinder
A python program to find the smallest fragments (i.e. the most likely to be amplified) from a set of primers in a target DNA sequence. The command generates a csv file (default: output.csv, use `-o` or `--output` to change) with 2 columns; 5' position of primer hit and length of fragment generated by the closest 3' primer site. The 5' position is the *last* base of the 5' primer. The length of fragment excludes the lengths of the two primers.

```
usage: primerFinder.py [-h] [-v] -i INPUTFILE -p PATTERNFILE [-o OUTFILE]

A program to find the smallest fragments (i.e. the most likely to be
amplified) from a set of primers in a target DNA sequence. The command
generates a csv file (default: output.csv, use `-o` or `--output` to change)
with 2 columns; 5' position of primer hit and length of fragment generated by
the closest 3' primer site. The 5' position is the _last_ base of the 5'
primer. The length of fragment excludes the lengths of the two primers.

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

