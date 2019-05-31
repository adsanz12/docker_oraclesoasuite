#!/bin/bash

if [ "$WL_DOMAIN" == "" ]
then
	echo "No name provided for the WebLogic Domain (env WL_DOMAIN)"
else
	if [ -e /opt/done_rcu.txt ]
	then
		echo "RCU already executed"
	else
		if [ "$START_RCU" == "true" ]
		then
			# Default sys user
			if [ "$SYS_USER" == "" ]
			then
				SYS_USER="SYS"
			fi
			if [[ ( "$SYS_PASSWORD" == "" ) || ( "$SOAINFRA_PASSWORD" == "") ]]
			then
					echo "Mandatory SYS_PASSWORD and SOAINFRA_PASSWORD not present"
			else
				if [[ ( "$CONNECT_STRING" == "" ) || ( "$SCHEMA_PREFIX" == "") ]]
				then
					echo "Mandatory CONNECT_STRING and SCHEMA_PREFIX not present"
				else
					echo "Running RCU"
					# Create password file
					echo $SYS_PASSWORD >> /opt/passwordFile.txt
					echo $SOAINFRA_PASSWORD >> /opt/passwordFile.txt
					echo $SOAINFRA_PASSWORD >> /opt/passwordFile.txt
					echo $SOAINFRA_PASSWORD >> /opt/passwordFile.txt
					echo $SOAINFRA_PASSWORD >> /opt/passwordFile.txt
					# RCU Command
					echo "-connectString: "$CONNECT_STRING
					echo "-dbUser: "$SYS_USER
					echo "-schemaPrefix"$SCHEMA_PREFIX
					echo "/opt/passwordFile:"
					cat /opt/passwordFile.txt
					sh /opt/rcu/rcuHome/bin/rcu -silent -createRepository -connectString $CONNECT_STRING -dbUser $SYS_USER -dbRole SYSDBA -schemaPrefix $SCHEMA_PREFIX -component MDS -component SOAINFRA -component BAM -component ORASDPM -f < /opt/passwordFile.txt
					touch /opt/done_rcu.txt
					# Clean password file
					rm /opt/passwordFile.txt
				fi
			fi
		fi
	fi
	if [ -e /opt/done_soa_domain.txt ]
	then
		echo "Starting WL Domain"
		sh /opt/Middleware/user_projects/domains/${WL_DOMAIN}/startWebLogic.sh
	else
		echo "Creating WL Domain"
		if [ "$WL_DOMAIN_PWD" == "" ]
		then
			WL_DOMAIN_PWD=welcome1
		fi
		sh /opt/Middleware/wlserver_10.3/common/bin/wlst.sh /opt/script.py $CONNECT_STRING $SCHEMA_PREFIX $SOAINFRA_PASSWORD oracle.jdbc.OracleDriver oracle.jdbc.xa.client.OracleXADataSource $WL_DOMAIN_PWD $WL_DOMAIN
		echo "Fixing classpath"
		echo 'CLASSPATH="${CLASSPATH}${CLASSPATHSEP}${COMMON_COMPONENTS_HOME}/modules/com.oracle.weblogic.sca.engine.jar"' >> /opt/Middleware/user_projects/domains/${WL_DOMAIN}/bin/setDomainEnv.sh
		echo 'export CLASSPATH' >> /opt/Middleware/user_projects/domains/{$WL_DOMAIN}/bin/setDomainEnv.sh
		echo "Starting WL Domain"
		touch /opt/done_soa_domain.txt
		sh /opt/Middleware/user_projects/domains/${WL_DOMAIN}/startWebLogic.sh
	fi
fi