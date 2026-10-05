wc -l
- 11369941 311_Service_Requests_from_2010_to_Present_20250928.csv

1. For some rows the closed date is before the open date resulting in a negative response time. How to handle those rows? - _These rows should be removed. You can use some filter._
	- `chmod +x compare_dates.sh`
	- `./compare_dates.sh 311_service_records_2024_zipcode_ClosedDate.csv 311_clean_records.csv` -> no header, why?
	- 3339826 311_clean_records.csv

2. If the start date is in Jan and close date in Feb, which month does it belong to? - _Feb. Since that is when the issue was resolved._

3. Do rows with missing zip codes be included in the overall average? - _These should be removed. At the beginning when you trim the data, you should only choose the rows with zipcode._
	- `awk -F',' '$9 != ""'`
	- `-F','` → columns are separated by commas
	- `'$9 != ""'`  → keep the row if column 9 is **not blank**
	- 3402730 311_service_records_2024_zipcode.csv
	
4. Do we include cases based on "open in 2024" or "closed in 2024"? - _Open in 2024._
	- `grep -E '^[^,]*,[0-9]{2}/[0-9]{2}/2024 ' `
		- -E = Basic Regular Expressions (BRE)
		- `^` -> Start of the row
		- `[^,]*`-> Everything in column 1, until a comma
		- `,`-> End of column 1
		- `[0-9]{2}`->Two-digit month
		- `/`-> Separator
		- `/2024` -> Year must be 2024
	- `grep '^[^,]*,[0-9]\{2\}/[0-9]\{2\}/2024 ' `
	- 3458320 311_service_records_2024.csv

5. Should we calculate duration by day or by hour? - _In hours._

6. What if there is no end date for a zipcode event? - _Remove it._
	- `awk -F',' '$3 != ""'`
	- 3340652 311_service_records_2024_zipcode_ClosedDate.csv





