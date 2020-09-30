
import os, json, argparse, sys, datetime, time
import pronto, six

"""
GO has relationship: capable_of (-->activity) and relationship: capable_of_part_of (--> process) on cell component entries. These can be made to the resp.
molfunc and process statemens. 
"""
# Initiate the parser
parser = argparse.ArgumentParser()
#parser.add_argument("-q", "--query", help="perform SPARQL query",
#        action="store_true")

# Read arguments from the command line
args = parser.parse_args()

# Check for --version or -V
#QS = args.output_qs
#dontquery = not args.query
script = os.path.basename(sys.argv[0])[:-3]

print('Reading GO')
ont = pronto.Ontology('/home/ralf/wikidata/go.obo')

for term in ont.terms():
    goid = term.id
    if not goid.startswith('GO:'):
        continue
    for syn in term.synonyms:
        if any(x.id.startswith('EC:') for x in syn.xrefs):
            j = {"id": goid, "name": term.name, "synonym": syn.description,
                    "scope": syn.scope, "xrefs": [x.id for x in syn.xrefs] }
            print(json.dumps(j))
