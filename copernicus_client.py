import copernicusmarine as cop
from yaml import Loader, load as yml_load
import argparse

parser = argparse.ArgumentParser(
    description="function that downloads files from copernicus marine client using a "
    "configuration file to specify variables, spatiotemporal extent etc."
)
parser.add_argument("file", help="filename")
args = parser.parse_args()
configuration_file = "./" + args.file


class File:
    def __init__(self, namelist):
        self.config_path = "./"
        self.outfile_path = "./"
        self.file_prefix = "eddy_test"
        self.start_date = namelist["datetime_start"] + "T00:00:00"
        self.end_date = namelist["datetime_end"] + "T23:59:59"
        self.data_id = namelist["data_id"]
        self.var = namelist["variables"]
        self.min_depth = namelist["min_depth"]
        self.max_depth = namelist["max_depth"]
        self.domain = namelist["domain"]
        self.min_lon = namelist[self.domain]["min_lon"]
        self.min_lat = namelist[self.domain]["min_lat"]
        self.max_lon = namelist[self.domain]["max_lon"]
        self.max_lat = namelist[self.domain]["max_lat"]
        self.outfile = (
            self.outfile_path + self.file_prefix + "_" + self.start_date[:4] + ".nc"
        )
        return

    def download(self):
        self.download_set()
        return

    def download_set(self):
        print(" ##################### ")
        print("Preparing to download dataset")
        print("filename = " + self.outfile)
        print("domain = " + self.domain)
        print(" ##################### ")
        cop.subset(
            dataset_id=self.data_id,
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
            force_download=True,
        )
        return


def main(configuration_file):
    # load namelist:
    stream = open(configuration_file, "r")
    namelist = yml_load(stream, Loader)
    f = File(namelist)
    f.download_set()


if __name__ == "__main__":
    main(configuration_file)
