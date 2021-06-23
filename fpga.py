import urllib
import json
import subprocess
import sys

def countMyAFIs():
    cmd='aws ec2 describe-fpga-images --filters Name=owner-id,Values=438680689039'
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,   stderr=subprocess.PIPE)
    out, err = p.communicate()
    out = json.loads(out)
    print ("There are %d AFIs"%(len(out['FpgaImages'])))


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Utilities to use AWS FPGAs")
    # parser.add_argument('--choice', action='store_true')
    parser.add_argument('-c', '--choice', type=int, help="choice")
    args = parser.parse_args()

    if (args.choice == 0):
        countMyAFIs()
    else:
        print("Undefined choice!")
        sys.exit(0)

