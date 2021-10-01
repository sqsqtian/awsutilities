import urllib
import json
import subprocess
import sys
import operator

def printList(l):
    for e in l:
        print(e)

def countMyAFIs():
    cmd='aws ec2 describe-fpga-images --filters Name=owner-id,Values=438680689039'
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,   stderr=subprocess.PIPE)
    out, err = p.communicate()
    out = json.loads(out)
    print ("There are %d AFIs"%(len(out['FpgaImages'])))

def cleanMyAFIs():
    cmd='aws ec2 describe-fpga-images --filters Name=owner-id,Values=438680689039'
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,   stderr=subprocess.PIPE)
    out, err = p.communicate()
    out = json.loads(out)
    print (len(out['FpgaImages']))
    for i in range(len(out['FpgaImages'])):
        # print (out['FpgaImages'][i]['Name'], out['FpgaImages'][i]['Public'], out['FpgaImages'][i]['CreateTime'], out['FpgaImages'][i]['State']['Code'])
        # print ("Name: %s\t\tPublic: %s\t\tState: %s"%(out['FpgaImages'][i]['Name'], out['FpgaImages'][i]['Public'], out['FpgaImages'][i]['State']['Code']))
        if (out['FpgaImages'][i]['State']['Code'] == 'failed'):
            print (out['FpgaImages'][i])
            cmd='aws ec2 delete-fpga-image --fpga-image-id %s'%(out['FpgaImages'][i]['FpgaImageId'])
            p = subprocess.call(cmd, shell=True)


def printMyAFIs():
    cmd='aws ec2 describe-fpga-images --filters Name=owner-id,Values=438680689039'
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,   stderr=subprocess.PIPE)
    out, err = p.communicate()
    out = json.loads(out)
    l = out['FpgaImages']
    # print (type(l), type(l[0]), type(l[0]['CreateTime']), l[0].keys())
    # print (l[0])
    # print (l[0].values())
    
    for i in range(len(l)):
        if (type(list(l[i].values())[-5]) is not str):
            print (l[i])
            print (list(l[i].values())[-5])
            sys.exit(0)
    l.sort( key=lambda k: list(k.values())[-5], reverse=True)
    # l.sort(key=operator.itemgetter('CreateTime'))
    with open ("allAFIs.txt", "w") as f: 
        for e in l:
            f.write("%s\n"%(str(e)))


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Utilities to use AWS FPGAs")
    # parser.add_argument('--choice', action='store_true')
    parser.add_argument('-c', '--choice', type=int, help="choice 0: countMyAFIs and save AFIs to file; choice 1: clean AFIs; ")
    args = parser.parse_args()

    if (args.choice == 0):
        countMyAFIs()
        printMyAFIs()
    elif (args.choice == 1):
        cleanMyAFIs()
    else:
        print("Undefined choice!")
        sys.exit(0)

