# as3_inventory

## Overview

as3_inventory is a simple script that grabs a list of all application services deployed via BIG-IQ and details around each. 

This script can be run on a local BIG-IQ or remotely. To run locally, set the destination address to 127.0.0.1 in the script itself. Also make sure you set a valid username and password.

This script uses token authentication for the BIG-IQ; basic auth is not required to be enabled.

To run the script, issue the "python as3_inventory.py" command on the BIG-IQ.

## Sample Output

```
Name: tcp_testing_tenant_tcp_testing_app_svc
    Tenant: tcp_testing_tenant
    ID: af1a2b7a-fd5a-3238-b468-644d69b53fbe
    Status: DEPLOYED
    Application: tcp_testing_app
    Application Service Type: TCP
    Device: 10.0.0.6
    App Svcs Template: AS3-F5-TCP-lb-template-big-iq-default-v2
    Last Configured: 2020-07-16T18:03:56.060Z
    Last Deployment: 2020-07-16T18:03:56.060Z
Name: udptesting_greg_udp
    Tenant: udptesting
    ID: cbc01f53-eb51-3c69-b90f-0a6988eb0069
    Status: DEPLOYED
    Application: udp_testing
    Application Service Type: TCP
    Device: 10.0.0.6
    App Svcs Template: AS3-F5-UDP-lb-template-big-iq-default-v1
    Last Configured: 2020-07-16T18:01:20.371Z
    Last Deployment: 2020-07-16T18:01:20.371Z
Name: greg_testing
    Tenant: greg
    ID: e3459326-b520-3795-954a-80ecccf2fe23
    Status: DEPLOYED
    Application: gregtest
    Application Service Type: HTTP
    Device: 10.0.0.6
    App Svcs Template: AS3-F5-HTTP-lb-template-big-iq-default-v1
    Last Configured: 2020-07-16T17:55:55.865Z
    Last Deployment: 2020-07-16T17:55:55.865Z
```
