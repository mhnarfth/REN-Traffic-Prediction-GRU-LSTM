# Data is located in this folder in my Macbook:

'/Users/maushariff/Downloads/Local Disk E/Byrav/Internet2 Data'

# (In the HCC server)The data was copied to my directory using the following command and then downloaded to local machine.

# For Atlanta
# cmd 1:

for day in {08..31}; do cp "/common/ramamurthy/saisuman/internet2-netflow/2021-10-${day}/2021-10-${day}-rtsw_atla.gz" "/common/ramamurthy/mhnarfth/temp/"; done

# cmd 2: 

for day in {01..08}; do cp "/common/ramamurthy/saisuman/internet2-netflow/2021-11-${day}/2021-11-${day}-rtsw_atla.gz" "/common/ramamurthy/mhnarfth/temp/"; done


# For Dallas
# cmd 1:

for day in {08..31}; do cp "/common/ramamurthy/saisuman/internet2-netflow/2021-10-${day}/2021-10-${day}-rtsw_dall.gz" "/common/ramamurthy/mhnarfth/temp/"; done

# cmd 2: 

for day in {01..08}; do cp "/common/ramamurthy/saisuman/internet2-netflow/2021-11-${day}/2021-11-${day}-rtsw_dall.gz" "/common/ramamurthy/mhnarfth/temp/"; done


# Then to unzip all the files using a single command

# cmd:

for file in *.gz; do gunzip "$file"; done


