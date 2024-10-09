#! /bin/bash
# --------------------------------------------
# Options that must be configured by app owner
# --------------------------------------------
APP_NAME="kibana"  # name of app-sre "application" folder this component lives in
COMPONENT_NAME="es-cleanup"  # name of app-sre "resourceTemplate" in deploy.yaml for this component
IMAGE="quay.io/cloudservices/es-cleanup"  

IQE_PLUGINS="kibana"
IQE_MARKER_EXPRESSION="smoke"
IQE_FILTER_EXPRESSION=""

# Install bonfire repo/initialize
CICD_URL_SCRIPT=https://raw.githubusercontent.com/RedHatInsights/cicd-tools/main/bootstrap.sh
curl -sL "$CICD_URL_SCRIPT" > .cicd_bootstrap.sh && source .cicd_bootstrap.sh
source $CICD_ROOT/build.sh

mkdir artifacts
cat << EOF > artifacts/junit-dummy.xml
<testsuite tests="1">
    <testcase classname="dummy" name="dummytest"/>
</testsuite>
EOF