#!/bin/sh

repoHome=/OVS/Repositories/

vDiskList=`find $repoHome -name *.img`
vmCfgList=`find $repoHome -name vm.cfg`

orphanflag=0

for vDisk in $vDiskList
do
  diskflag=0
  for vmCfg in $vmCfgList
  do
    grep $vDisk $vmCfg &> /dev/null
    if [ $? -eq 0 ]; then 
      diskflag=1
      break
    fi
  done
#    echo $vDisk $diskflag
    if [ $diskflag -eq 0 ]; then
      echo "$vDisk is not used by any VM or Template"
      orphanflag=1      
    fi
done

if [ $orphanflag -eq 0 ]; then
  echo "No orphan disk"
fi
