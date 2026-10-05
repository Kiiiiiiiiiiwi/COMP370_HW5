import argparse
import csv
from datetime import datetime
import sys

# python3 src/complaint_borough.py -i data/311_clean_records.csv -s 2024-01-12 -e 2024-01-15

def main():

# borough_complaints.py -i <the input csv file> -s <start date> -e <end date> [-o <output file>]
# If the output argument isn’t specified, then just print the results (to stdout).
    parser = argparse.ArgumentParser(
        description="Count complaints by borough within a specified date range."
    )
    parser.add_argument('-i', '--input', required=True,type=str, help='the input csv file')
    parser.add_argument('-s', '--start', required=True, type=str, help='start date')
    parser.add_argument('-e', '--end', required=True, type=str, help='end date')
    parser.add_argument('-o', '--output', type=str, help='output file') #optional

    args = parser.parse_args()

    start_date = datetime.strptime(args.start, "%Y-%m-%d").date()
    end_date = datetime.strptime(args.end, "%Y-%m-%d").date()

    counts = {}

    with open(args.input, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            created = datetime.strptime(
                row["Created Date"], 
                "%m/%d/%Y %I:%M:%S %p"
            ).date() # a cleaner approach is to compare only the date

            if start_date <= created <= end_date:
                complaint = row["Complaint Type"]
                borough = row["Borough"]

                key = (complaint, borough)

                if key not in counts:
                    counts[key] = 0

                counts[key] += 1

    # stdout if -o isn't provided
    if args.output:
        output = open(args.output, "w", newline="", encoding="utf-8")
    else:
        output = sys.stdout

    writer = csv.writer(output)

    writer.writerow(["complaint type", "borough", "count"])

    for (complaint, borough), count in counts.items():
        writer.writerow([complaint, borough, count])

    if args.output:
        output.close()

if __name__ == '__main__':
    main()