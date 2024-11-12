import copernicusmarine as cop
from yaml import Loader, load as yml_load

import argparse

prefix = 'samplesNSEW_'
parser = argparse.ArgumentParser(description="function that downloads files from copernicus marine client using a "
                                             "configuration file to specify variables, spatiotemporal extent etc.")
parser.add_argument("file", help="filename")
args = parser.parse_args()
configuration_file = './' + args.file

class File:
    def __init__(self, namelist):
        breakpoint()
        self.start_date = 0


def download_set(self):
    print(" ##################### ")
    print("Preparing to download dataset")
    print("filename = " + self.outfile)
    print(" ##################### ")
    cop.subset(dataset_id=self.data_id,
               variables=self.var,
               start_datetime=self.start_date,
               end_datetime=self.end_date,
               minimum_longitude=self.min_lon,
               maximum_longitude=self.max_lon,
               minimum_latitude=self.min_lat,
               maximum_latitude=self.max_lat,
               minimum_depth=self.min_depth,
               maximum_depth=self.max_depth,
               output_filename=self.outfile,
               output_directory=self.outfile_path,
               credentials_file=self.config_path + ".copernicusmarine-credentials",
               force_download=True
               )
    return


def main(configuration_file):
    # load namelist:
    stream = open(configuration_file, "r")
    namelist = yml_load(stream, Loader)
    File(namelist)

if __name__ == '__main__':
    main(configuration_file)