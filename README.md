
## How to run

Install PySpark using conda. To connect your spark session to the postresql database, you will need to download the PostgreSQL JDBC Driver from https://jdbc.postgresql.org/download.html. *Note: we have JAVA JDK 11. This will determine which version of the driver you should download. Currently the driver version is 42.3.3.* I downloaded this file to my root directory. More information about the configuration can be found in the example script named `omop_connect.py`. If everything is setup correctly, this script will print the schema of the death table.

## Requirements
PySpark >= 3.2.1

## Build OMOP DB

The OMOP Postgres DB has already been built so you don't need this section. However, if we do need to rebuild it or build in on a new system, I've included some instructions and notes below:

If the mimic postgres DB doesn't exist, build it. Use this repo to build it: https://github.com/MIT-LCP/mimic-omop. The script to build it can be found in `mimic-omop/mimic/build-mimic/build-mimiciii.sql`. You will need to change line 6 where it says `postgres_load_data_gz.sql` to `postgres_load_data.sql`. You will also need to set the mimic_data_dir or you can change line 12 in `postgres_load_data.sql` to be the location of the MIMIC-III CSVs. Those can be found here: /olddata/datasets/mimic/mimic-csv.

After the MIMIC-III DB has been built follow instruction for building the OMOP schema: https://github.com/MIT-LCP/mimic-omop/tree/master/omop/build-omop/postgresql

*	Once you get to the vocabulary part. 
	*	create an account here: https://www.ohdsi.org/analytic-tools/athena-standardized-vocabularies/
	*	download the vocabulary
	*	Get an API key for vocabulary extraction here: https://uts.nlm.nih.gov/uts/signUp
	*	Symlink didn't work for me (just copy the vocab from data/vocab to extras/athena)

After the schema is built, follow the instructions here: https://github.com/MIT-LCP/mimic-omop/blob/fa5113c3f0777e74d2a6b302322477e6fe666910/README-run-etl.md

When you run the ETL, don't worry about the errors saying that the tables don't exist. this happens the first time you run it. If you look at the code, it says to drop if it doesn't exist anyways
