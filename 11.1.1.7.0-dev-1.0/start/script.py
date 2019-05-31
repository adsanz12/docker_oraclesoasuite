import sys

DB_URL = 'jdbc:oracle:thin:@' + sys.argv[1];
DBUSER_PREFIX = sys.argv[2];
DBUSER_PWD = sys.argv[3];
DBDRIVER = sys.argv[4];
DBDRIVER_XA = sys.argv[5];
WLUSER_PWD = sys.argv[6];
WLDOMAIN = sys.argv[7];

# Read template for WL Server
readTemplate('/opt/Middleware/wlserver_10.3/common/templates/domains/wls.jar');
# Create user
cd('/Security/base_domain/User/weblogic');
# Set password
cmo.setPassword(WLUSER_PWD);
# Close template
closeTemplate();
# Create domain
createDomain('/opt/Middleware/wlserver_10.3/common/templates/domains/wls.jar','/opt/Middleware/user_projects/domains/'+WLDOMAIN,'weblogic',WLUSER_PWD);
# Read domain
readDomain('/opt/Middleware/user_projects/domains/'+WLDOMAIN);

print('WebLogic Advanced Web Services for JAX-WS Extension');
addTemplate('/opt/Middleware/wlserver_10.3/common/templates/applications/wls_webservice_jaxws.jar');

print('Oracle SOA Suite for developers');
addTemplate('/opt/Middleware/Oracle_SOA1/common/templates/applications/oracle.soa_template_developer_11.1.1.jar');

print('Oracle Service Bus for developers');
addTemplate('/opt/Middleware/Oracle_OSB1/common/templates/applications/wlsb_single_server.jar');

print('Oracle Service Bus OWSM Extension');
addTemplate('/opt/Middleware/Oracle_OSB1/common/templates/applications/wlsb_owsm.jar');

print('Oracle Enterprise Manager');
addTemplate('/opt/Middleware/oracle_common/common/templates/applications/oracle.em_11_1_1_0_0_template.jar');

print('Oracle Business Activity Monitoring');
addTemplate('/opt/Middleware/Oracle_SOA1/common/templates/applications/oracle.bam_template_11.1.1.jar');

print('Oracle BI Composer Runtime');
addTemplate('/opt/Middleware/oracle_common/common/templates/applications/oracle.applcore.model.stub.11.1.1_template.jar');

# Create admin server
cd('/Servers/AdminServer');
set('ListenPort', 7001);
# Create BAM datasource
cd('/JDBCSystemResources/BAMDataSource/JdbcResource/BAMDataSource/JDBCDriverParams/NO_NAME_0');
set('URL',DB_URL);
cmo.setDriverName(DBDRIVER);
cmo.setPasswordEncrypted(DBUSER_PWD);
cd('Properties/NO_NAME_0/Property/user');
set('Value',DBUSER_PREFIX+'_ORABAM');
# Create EDN datasource
cd('/JDBCSystemResources/EDNDataSource/JdbcResource/EDNDataSource/JDBCDriverParams/NO_NAME_0');
set('URL',DB_URL);
cmo.setDriverName(DBDRIVER);
cmo.setPasswordEncrypted(DBUSER_PWD);
cd('Properties/NO_NAME_0/Property/user');
set('Value',DBUSER_PREFIX+'_SOAINFRA');
# Create EDN local datasource
cd('/JDBCSystemResources/EDNLocalTxDataSource/JdbcResource/EDNLocalTxDataSource/JDBCDriverParams/NO_NAME_0');
set('URL',DB_URL);
cmo.setDriverName(DBDRIVER);
cmo.setPasswordEncrypted(DBUSER_PWD);
cd('Properties/NO_NAME_0/Property/user');
set('Value',DBUSER_PREFIX+'_SOAINFRA');
# Create SDPM datasource
cd('/JDBCSystemResources/OraSDPMDataSource/JdbcResource/OraSDPMDataSource/JDBCDriverParams/NO_NAME_0');
set('URL',DB_URL);
cmo.setDriverName(DBDRIVER);
cmo.setPasswordEncrypted(DBUSER_PWD);
cd('Properties/NO_NAME_0/Property/user');
set('Value',DBUSER_PREFIX+'_ORASDPM');
# Create SOA datasource
cd('/JDBCSystemResources/SOADataSource/JdbcResource/SOADataSource/JDBCDriverParams/NO_NAME_0');
set('URL',DB_URL);
cmo.setDriverName(DBDRIVER);
cmo.setPasswordEncrypted(DBUSER_PWD);
cd('Properties/NO_NAME_0/Property/user');
set('Value',DBUSER_PREFIX+'_SOAINFRA');
# Create SOA Local datasource
cd('/JDBCSystemResources/SOALocalTxDataSource/JdbcResource/SOALocalTxDataSource/JDBCDriverParams/NO_NAME_0');
set('URL',DB_URL);
cmo.setDriverName(DBDRIVER);
cmo.setPasswordEncrypted(DBUSER_PWD);
cd('Properties/NO_NAME_0/Property/user');
set('Value',DBUSER_PREFIX+'_SOAINFRA');
### OSB ###
# Create wlsbjmsrp
cd('/JDBCSystemResource/wlsbjmsrpDataSource/JdbcResource/wlsbjmsrpDataSource/JDBCDriverParams/NO_NAME_0') 
set('URL',DB_URL);
cmo.setDriverName(DBDRIVER);
cmo.setPasswordEncrypted(DBUSER_PWD);
cd('Properties/NO_NAME_0/Property/user');
set('Value',DBUSER_PREFIX+'_SOAINFRA');
### SOA ###
# Create mds-owsm
cd('/JDBCSystemResources/mds-owsm/JdbcResource/mds-owsm/JDBCDriverParams/NO_NAME_0');
set('URL',DB_URL);
cmo.setDriverName(DBDRIVER);
cmo.setPasswordEncrypted(DBUSER_PWD);
cd('Properties/NO_NAME_0/Property/user');
set('Value',DBUSER_PREFIX+'_MDS');
# Create mds-soa
cd('/JDBCSystemResources/mds-soa/JdbcResource/mds-soa/JDBCDriverParams/NO_NAME_0');
set('URL',DB_URL);
cmo.setDriverName(DBDRIVER);
cmo.setPasswordEncrypted(DBUSER_PWD);
cd('Properties/NO_NAME_0/Property/user');
set('Value',DBUSER_PREFIX+'_MDS');
updateDomain();
exit();
