#!/bin/sh

EXECUTION_ID=`openstack workflow execution create "$@" -f value -c ID`

echo "Workflow execution starting with execution ID $EXECUTION_ID"

EXECUTION_STATUS=''
while [ "${EXECUTION_STATUS}" != "SUCCESS" ] && [ "${EXECUTION_STATUS}" != "ERROR" ]; do
  EXECUTION_STATUS=`openstack workflow execution show $EXECUTION_ID -f value -c State`
  if [ "${EXECUTION_STATUS}" != "SUCCESS" ] && [ "${EXECUTION_STATUS}" != "ERROR" ]; then
    echo "..$EXECUTION_STATUS.."
  fi
  sleep 2
done

if [ "${EXECUTION_STATUS}" == "SUCCESS" ]; then
  echo "$EXECUTION_STATUS! :)"
elif [ "${EXECUTION_STATUS}" == "ERROR" ]; then
  echo "$EXECUTION_STATUS! :("
fi

openstack workflow execution output show $EXECUTION_ID
