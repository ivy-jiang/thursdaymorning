#!/usr/bin/env python3
import os
## read in text File and get each line --> get each word--> string
## remove duplicates
###TODO #TODO space turn into hyphen (e.g. The Doorbell=The Doorbell)
def gettext():
    ## if running from setup
    with open("testtext.txt", "r") as textfile:
        next(textfile) ##IF HAS HEADER
        counterkey=0
        worddict={}
        for line in textfile:
            cline= str(line.strip())
            cleaned=cline.replace("-", "_")
            cleanez=cleaned.replace(" ", "_")
            # print(cline)
            # cline= str(line.rstrip('\n'))
            if cleanez in worddict.values(): ## NO DUPLICATES
                pass
            else:
                counterkey+=1
                worddict[cline]=cleanez
    # print(worddict)
    filenamezlistz=[]
    filelistz=[]
    for numkey in worddict:
        orignamez= (worddict[numkey])
        filelistz.append(orignamez)
    # print (worddict)
    return(worddict)


imavariable=gettext()
# print(imavariable, type(imavariable))
messylist=list(imavariable.values())
# print (messylist)

pathin=os.path.join('..', 'run','core','controllers','cleanlist.py')
with open(pathin, 'w') as melist:
    melist.write("#!/usr/bin/env python3")
    melist.write("\n")
    melist.write("melisty={}".format(messylist))


## Iterate over dictionary
# for key, value in d.items():


def createpycontroller(filelist):
    for filename, dirt in filelist.items():
        pathy=os.path.join('..', 'run','core','controllers','{}mez.py'.format(dirt))
        with open(pathy, 'w') as fmez:
        # with open("{}mez.py".format(filename), 'w') as fmez:
            fmez.write("#!/usr/bin/env python3\n")
            fmez.write("from flask import Blueprint, render_template")
            fmez.write("\n")
            fmez.write("{dirz}mez = Blueprint('{dirz}mez', __name__, url_prefix='/{hihi}')".format(dirz=dirt, hihi=filename))
            fmez.write("\n")
            fmez.write("@{}mez.route('/', methods=['GET'])".format(dirt))
            fmez.write("\n")
            fmez.write("def show_{}():".format(dirt))
            fmez.write("\n")
            fmez.write("\treturn render_template('"+"{}".format(dirt)+"mez.html')")

# createpycontroller(["hihi", "meao", "return"])
createpycontroller(imavariable)



##TODO for each WORD (e.g. dict value), create meowWORD.html in folder templates
def createhtml(filelist):
    for filename,dirt in filelist.items():
        pathy=os.path.join('..', 'run','core','templates','{}mez.html'.format(dirt))
        with open(pathy, 'w') as fmez:
        # with open("{}mez.py".format(filename), 'w') as fmez:
            fmez.write("{% extends \"layout.html\" %}")
            fmez.write("\n")
            fmez.write("{% block content %}")
            fmez.write("\n")
            fmez.write("{{super()}}")
            fmez.write("\n")
            fmez.write("<b>{namey}</b>".format(namey=filename))
            fmez.write("\n")
            fmez.write("{{message2}}")
            fmez.write("\n")
            fmez.write("{% endblock %}")
# createhtml(["hihi", "meao", "return"])
createhtml(imavariable)


def allwordssite(listofwords):
    messylist=list(listofwords.values())
    pathpyth=os.path.join('..', 'run','core','controllers','all_listed.py')
    pathhtm=os.path.join('..', 'run','core','templates','all_listed.html')
    with open(pathpyth, 'w') as allpyth:
        allpyth.write("#!/usr/bin/env python3")
        allpyth.write("\n")
        allpyth.write("from flask import Blueprint, render_template, redirect, url_for")
        allpyth.write("\n")
        allpyth.write("{hihi}mez = Blueprint('{hihi}mez', __name__, url_prefix='/{hihi}')".format(hihi='all_listed'))
        allpyth.write("\n")
        allpyth.write("@{}mez.route('/', methods=['GET'])".format('all_listed'))
        allpyth.write("\n")
        allpyth.write("def show_{}():".format('all_listed'))
        allpyth.write("\n")
        allpyth.write("\treturn render_template('"+"{}".format('all_listed')+".html')")

    with open(pathhtm, 'w') as alllisthtm:
        alllisthtm.write("{% extends \"layout.html\" %}")
        alllisthtm.write("\n")
        alllisthtm.write("{% block content %}")
        alllisthtm.write("\n")
        alllisthtm.write("{{super()}}")
        for filename, dirt in listofwords.items():
            alllisthtm.write("\n <br>")
            alllisthtm.write("  <a href=\"{{{{ url_for(\'{dirz}mez.show_{dirz}\') }}}}\">  {namey}</a>".format(dirz=dirt, namey=filename))
            alllisthtm.write("\n")
        alllisthtm.write("{{message2}}")
        alllisthtm.write("\n")
        alllisthtm.write("{% endblock %}")
allwordssite(imavariable)
