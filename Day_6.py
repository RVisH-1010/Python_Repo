print("day 6 of py tut...")
# 1.cmmd line utility argpass
import argparse
import requests

def download_file(url, local_filenmae):
    if local_filename == "None":
        local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename

parser = argparse.ArgumentParser()
# add cmmd line
parser.add_argument("url", help="url of the file to dowload")
# parser.add_argument("output" , help="nmae of file to save ")
parser.add_argument("-o","--output", help="name of the file", default=None)

# parse the  argument
args = parser.parse_args()
# use arguments in the code
print(args.url)
print(args.output)
