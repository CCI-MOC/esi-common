# esi-common

esi-common is a library containing specialized OpenStack code for use by the ESI project.

### Installation

```
    $ git clone https://github.com/CCI-MOC/esi-common
    $ cd esi-common
    $ sudo python setup.py install
```

### Custom Nova Filter for ESI

The code in [esi_common/scheduler/filters/esi_filter.py](https://github.com/CCI-MOC/esi-common/blob/master/esi_common/scheduler/filters/esi_filter.py) provides an additional Nova filter that allows Nova to filter baremetal hosts based on additional Ironic properties set by ESI workflows. To use this filter, configure Nova by modifying `/etc/conf/nova/nova.com` by uncommenting, adding, or modifying these lines:


```
available_filters=nova.scheduler.filters.all_filters
available_filters=esi_common.scheduler.filters.esi_filter.ESIFilter

enabled_filters=RetryFilter,AvailabilityZoneFilter,ComputeFilter,ComputeCapabilitiesFilter,ImagePropertiesFilter,ServerGroupAntiAffinityFilter,ServerGroupAffinityFilter,ESIFilter

```