__author__ = '@mjjacko'
import polib,csv,sys,getopt


def main(argv):
    inputfile = ''
    outputfile = ''
    isConvertPo = False
    isConvertCsv = False
    try:
        opts, args = getopt.getopt(argv,"cphi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-p"):
            isConvertPo = True
        elif opt in ("-c"):
            isConvertCsv = True

    if (isConvertPo):
        convertPo(inputfile, outputfile)

    if (isConvertCsv):
        convertCsv(inputfile, outputfile)
    print 'Converted "', inputfile,'" to "', outputfile, '"'




def convertPo(inputpo, outputcsv):
    po = polib.pofile(inputpo)
    mdata = po.ordered_metadata()
    language = 'en-US'
    for name, value in mdata:
        if (name=='Language'):
            language = value
    with open(outputcsv, 'wb') as csvfile:
        fieldnames = ['Title','Default language','Default text',language+' text','Variant status','Placeholder']
        csvwriter = csv.DictWriter(csvfile, delimiter=',',quotechar='"',quoting=csv.QUOTE_ALL,fieldnames=fieldnames)
        csvwriter.writeheader()

        for entry in po:
            arr = entry.comment.split('||' )
            csvwriter.writerow({'Title':arr[1].encode('utf-8'),'Default language':arr[2].encode('utf-8'),
                            'Default text':arr[3].encode('utf-8'),language+' text':entry.msgstr.encode('utf-8'),
                            'Variant status':arr[5].encode('utf-8'),'Placeholder':arr[6].encode('utf-8')})


def convertCsv(inputcsv, outputpo):
    po = polib.POFile()
    po.metadata = {
        'Project-Id-Version': '1.0',
        'Report-Msgid-Bugs-To': 'you@example.com',
        'POT-Creation-Date': '2007-10-18 14:00+0100',
        'PO-Revision-Date': '2007-10-18 14:00+0100',
        'Last-Translator': 'you <you@example.com>',
        'Language-Team': 'English <yourteam@example.com>',
        'MIME-Version': '1.0',
        'Content-Type': 'text/plain; charset=utf-8',
        'Content-Transfer-Encoding': '8bit',
    }

    cd = '||'

    with open(inputcsv, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for (i,row) in enumerate(csvreader):
            comment = str(i)+cd+row['Title']+cd+row['Default language']+cd+row['Default text']+cd+row['en-US text']\
                      +cd+row['Variant status']+cd+row['Placeholder']
            msgid = row['Default text']
            entry = polib.POEntry(
                encoding='utf-8',
                comment=comment.decode('utf-8'),
                msgid=msgid.decode('utf-8')
    )
            po.append(entry)

    po.save(outputpo)

if __name__ == "__main__":
   main(sys.argv[1:])

