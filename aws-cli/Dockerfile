FROM amazon/aws-cli:2.2.43

RUN curl https://s3.amazonaws.com/session-manager-downloads/plugin/latest/linux_64bit/session-manager-plugin.rpm -o session-manager-plugin.rpm
RUN yum install -y session-manager-plugin.rpm