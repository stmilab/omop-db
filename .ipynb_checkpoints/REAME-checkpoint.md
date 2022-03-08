
## How to run

Set your environment variables:

```
export OMOP_USER='the postgres username'
export OMOP_USER='the DB password'
```

## Requirements
PySpark >+ 3.2.1

## Build OMOP DB
If the mimic postgres DB doesn't exist, build it. The data can be found here: /olddata/datasets/mimic/mimic-csv. Follow the instructions here: 

Follow instruction for building schema: https://github.com/MIT-LCP/mimic-omop/tree/master/omop/build-omop/postgresql

*	Once you get to the vocabulary part. 
	*	create an account here: https://www.ohdsi.org/analytic-tools/athena-standardized-vocabularies/
	*	download the vocabulary
	*	Get an API key for vocabulary extraction here: https://uts.nlm.nih.gov/uts/signUp
	*	Symlink didn't work for me (just copy the vocab from data/vocab to extras/athena)

When you run the ETL, don't worry about the errors saying that the tables don't exist. this happens the first time you run it. If you look at the code, it says to drop if it doesn't exist anyways

To connect your spark session to the postresql database, you will need to download the PostgreSQL JDBC Driver from https://jdbc.postgresql.org/download.html. *Note: we have JAVA JDK 11. This will determine which version of the driver you should download. Currently the driver version is 42.3.3.*