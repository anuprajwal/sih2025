# sih2025

ellaruku vanakkam 🙏🙏




PROJECT FLOW

=> extract the source files from the website https://data-argo.ifremer.fr/dac/

=> reed all the data from the cycle files and meta files

=> save these 2 files in 2 different formats:
        1. sql structured data
        2. save embidings of the data extracted

=> embed the user query and make the search from the rag database and sql database.

=> send these 2 data to the llm for a cleaner and meaningfull output

=> send raw sql data to frontend for the data visualisation






EXISTING FILES

1900121_prof.nc => metadata about the floats in scientific format
D1900121_001.nc => actual scientific data about the ocean recordings

meta_data.py => to see the data in the *_prof.nc files
cycle_test.py => to see all the needed data in the cucle files like D1900121_001.nc, the file also saves the data to the sql db

explain.txt => is the file which summarises the numerical data into redable text so that embidings are made

save_rag.py => file created chunks from the explain.txt file, creates embidings and saves that embidins to the chroma db (vector db)

work_over_data.py => file where we can test the rag chunks retrival.

requirements.txt => dependencies

install dependencies with          pip install -r requirements.txt



