FROM cnfldemos/cp-server-connect-datagen:0.5.0-6.2.0
USER root:root
COPY ./plugins/ /opt/kafka/plugins/
ENV CONNECT_PLUGIN_PATH="/opt/kafka/plugins"
USER 1001