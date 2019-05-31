FROM oraclelinux

# Variables para la instalación, no son necesarias para el sistema operativo
ARG DEFAULT_USER=oracle
ARG DEFAULT_GRP=oracle
ARG DEFAULT_PWD=oracle

COPY installer/jdk-6u45-linux-x64.bin /opt
COPY installer/wls1036_generic.jar /opt
COPY installer/ofm_osb_generic_11.1.1.7.0_disk1_1of1.zip /opt
COPY installer/ofm_soa_generic_11.1.1.7.0_disk1_1of2.zip /opt
COPY installer/ofm_soa_generic_11.1.1.7.0_disk1_2of2.zip /opt
COPY installer/ofm_rcu_linux_11.1.1.7.0_64_disk1_1of1.zip /opt
COPY installer/ojdbc6.jar /opt
COPY config/wl.xml /opt
COPY config/osb.rsp /opt
COPY config/soa.rsp /opt
COPY start/run.sh /opt
COPY start/script.py /opt
WORKDIR /opt

RUN yum install -y unzip

RUN echo -e "root\nroot" | passwd root &&\
	groupadd $DEFAULT_GRP &&\
	useradd -g $DEFAULT_GRP $DEFAULT_USER &&\
	echo -e "${DEFAULT_PWD}\n${DEFAULT_PWD}" | passwd $DEFAULT_USER &&\
	chmod +x jdk-6u45-linux-x64.bin &&\
	sh jdk-6u45-linux-x64.bin &&\
	rm jdk-6u45-linux-x64.bin &&\
	unzip ofm_osb_generic_11.1.1.7.0_disk1_1of1.zip -d osb &&\
	rm ofm_osb_generic_11.1.1.7.0_disk1_1of1.zip &&\
	unzip ofm_soa_generic_11.1.1.7.0_disk1_1of2.zip -d soa &&\
	rm ofm_soa_generic_11.1.1.7.0_disk1_1of2.zip &&\
	unzip ofm_soa_generic_11.1.1.7.0_disk1_2of2.zip -d soa &&\
	rm ofm_soa_generic_11.1.1.7.0_disk1_2of2.zip &&\
	unzip ofm_rcu_linux_11.1.1.7.0_64_disk1_1of1.zip -d rcu &&\
	rm ofm_rcu_linux_11.1.1.7.0_64_disk1_1of1.zip &&\
	chown $DEFAULT_USER:$DEFAULT_GRP /opt -R &&\
	chmod +x osb/Disk1/runInstaller &&\
	bash -c "sh osb/Disk1/stage/Response/createCentralInventory.sh /opt/orainv $DEFAULT_GRP" &&\
	bash -c "cp /opt/ojdbc6.jar /opt/rcu/rcuHome/jdbc/lib"

USER $DEFAULT_USER

RUN /opt/jdk1.6.0_45/bin/java -jar wls1036_generic.jar -mode=silent -silent_xml=/opt/wl.xml &&\
	bash -c "while kill -0 $(ps -a | pgrep java) 2> /dev/null; do sleep 1; done;"
RUN cd /opt/osb/Disk1/ && ./runInstaller -jreLoc /opt/jdk1.6.0_45 -silent -invPtrLoc /etc/oraInst.loc -response /opt/osb.rsp &&\
	bash -c "while kill -0 $(ps -a | pgrep java) 2> /dev/null; do sleep 1; done;"
RUN cd /opt/soa/Disk1/ && ./runInstaller -jreLoc /opt/jdk1.6.0_45 -silent -invPtrLoc /etc/oraInst.loc -response /opt/soa.rsp &&\
	bash -c "while kill -0 $(ps -a | pgrep java) 2> /dev/null; do sleep 1; done;"
RUN cd /opt && rm -rf osb soa && rm osb.rsp soa.rsp wl.xml wls1036_generic.jar

RUN bash -c "cp /opt/ojdbc6.jar /opt/Middleware/oracle_common/inventory/Scripts/ext/jlib"
RUN bash -c "cp /opt/ojdbc6.jar /opt/Middleware/wlserver_10.3/server/lib"
RUN bash -c "cp /opt/ojdbc6.jar /opt/Middleware/wlserver_10.3/server/adr"
RUN bash -c "cp /opt/ojdbc6.jar /opt/Middleware/Oracle_SOA1/inventory/Scripts/ext/jlib"
RUN bash -c "rm /opt/ojdbc6.jar"

CMD bash run.sh
