import ahoCorasick
import compareLists
import argparse
import sys
import os

def checkFile(targetFile):
    if not os.path.isfile(targetFile):
        raise argparse.ArgumentTypeError(targetFile+' is not a file')
    if os.access(targetFile, os.R_OK):
        return targetFile
    else:
        raise argparse.ArgumentTypeError(targetFile+' is not readable')

def patternFileToSearchTree(targetFile):
    tree = ahoCorasick.searchTree()
    with open(targetFile, 'r') as f:
        for line in f:
            line=line.replace('\r','').replace('\n','').replace(' ','')
            tree.add(line)
    tree.make()
    return tree

def readDna(targetFile):
    with open(targetFile, 'r') as f:
        dna=f.read()
    dna=dna.replace('\r','').replace('\n','').replace(' ','')
    return dna


def main(argv):
    parser = argparse.ArgumentParser(description="Python program to primer location pairs in a DNA sequence")
    parser.add_argument("-v","--verbose", help="increase output verbosity", action="store_true")
    parser.add_argument("-i","--inputFile", help="file to find primers in (assumes the file contains only DNA sequence, i.e. no headers, and that newlines are not significant)",type=checkFile,required=True)
    parser.add_argument("-p","--patternFile", help="primer file with one primer per line all 5' to 3'",type=checkFile,required=True)
    parser.add_argument("-o","--outFile", help="file to write to ",default="out.csv")
    args=parser.parse_args()
        
    if args.verbose:
        print("Arguments: ")
        for key, value in vars(args).items():
            print("   ",key,": ",value)

        
    if args.verbose: print('Reading patterns')
    tree=patternFileToSearchTree(args.patternFile)
    if args.verbose: print('Read',len(tree.terms),'patterns')
    revCompTree=tree.reverseComplimentTree()
    if args.verbose: print('Reading DNA')
    dna=readDna(args.inputFile)
    if args.verbose: print('Read',len(dna),'length DNA string')

    
    if args.verbose: print('Searching')
    pos=tree.search(dna,findStart=False,verbose=args.verbose) #last base of primer
    revCompPos=revCompTree.search(dna,verbose=args.verbose)   #first base of primer
    if args.verbose: print('Done searching')

    #do smarter things here with storing the positions and subsetting among the various primers

    if args.verbose: print('Combining primer lists')
    allFivePrime=compareLists.mergeMultipleArrays(pos.values())
    allThreePrime=compareLists.mergeMultipleArrays(revCompPos.values())
    if args.verbose: print('Done combining primer lists')

    if args.verbose: print('Finding nearest neighbors')
    minFragmentSizes=compareLists.findDistanceToClosest(allFivePrime,allThreePrime) 
    if args.verbose: print('Done finding nearest neighbors')
    
    with open(args.outFile, 'w') as f:
        for pos,dist in zip(allFivePrime,minFragmentSizes):
            f.write("%d,%d\n" % (pos,dist))

    if args.verbose: print('All done. Thanks')

if __name__ == '__main__':
    main(sys.argv)


