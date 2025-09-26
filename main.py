import csv
import re

def convert_to_csv(input_file, output_file):
    pattern = re.compile(r"([\d.]+)\s*cm\s*at\s*([\d.]+)\s*seconds")

    with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["cm", "seconds"])  # header row

        for line in infile:
            match = pattern.search(line)
            if match:
                cm, seconds = match.groups()
                writer.writerow([cm, seconds])

if __name__ == "__main__":
    # Change these to your filenames
    convert_to_csv("output.log", "measurements.csv")
