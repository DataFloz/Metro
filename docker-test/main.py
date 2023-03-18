import sys
import json
def main(arg1):
    js = json.loads(arg1)
    print(js)
    # print(f"final result: arg1 {arg1} arg2{arg2}")
    sys.exit(js)

main(arg1=sys.argv[3])