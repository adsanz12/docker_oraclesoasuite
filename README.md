# docker_oraclesoasuite

This repository contains the required files to build the docker image in https://hub.docker.com/r/adsanz12/oraclesoasuite

The docker image allows you to quickly setup an Oracle SOA Suite environment. It contains the required libraries to connect to an Oracle Database 12c, but you may use the Oracle Database 11g as well. Within the image you can find Oracle Service Bus, Oracle SOA Suite, Oracle Enterprise Manager and Oracle BAM.

To run a container for a development use the images with the "dev" tag.

# Setting a SOA 11g development environment:

docker run -d --name $wlname -p 7001:7001 -e WL_DOMAIN=devdomain -e START_RCU=true -e SYS_USER=sys -e SYS_PASSWORD=Oradoc_db1 -e SOAINFRA_PASSWORD=welcome1 -e CONNECT_STRING=localhost:1521/ORCLPDB1.localdomain -e SCHEMA_PREFIX=DEV -e WL_DOMAIN_PWD=welcome1 adsanz12/oraclesoasuite:11.1.1.7.0-dev-1.0
