import requests
import json
import urllib3

bigiq_ip = '54.163.99.90'
username = 'admin'
password = 'f5c0nfig123!'

urllib3.disable_warnings()

# Get an auth token from BIG-IQ
credentials_dict = {"username": username, "password": password}
headers = {'content-type': 'application/json'}
token_auth_response = requests.post('https://' + bigiq_ip + '/mgmt/shared/authn/login', verify=False,data=json.dumps(credentials_dict), headers=headers)
auth_token = json.loads(token_auth_response.text)['token']['token']

# Get a list of all of the applications deployed on the BIG-IQ
headers = {'content-type': 'application/json', 'X-F5-Auth-Token': auth_token}
global_config_sets_response = requests.get('https://' + bigiq_ip + '/mgmt/cm/global/config-sets', verify=False,headers=headers)
# print(global_config_sets_response.content)
global_config_sets = json.loads(global_config_sets_response.content)['items']
for current_config_set in global_config_sets:
    # Template for attributes
    # if current_config_set.has_key('status'):
    #     current_config_set_status = current_config_set['status']
    #     print('    Status: ' + current_config_set_status)
    if current_config_set.has_key('configSetName'):
        current_config_set_name = current_config_set['configSetName']
        print('Name: ' + current_config_set_name)
    if current_config_set.has_key('partition'):
        current_config_set_id = current_config_set['partition']
        print('    Partition: ' + current_config_set_id)
    if current_config_set.has_key('id'):
        current_config_set_id = current_config_set['id']
        print('    ID: ' + current_config_set_id)
    if current_config_set.has_key('status'):
        current_config_set_status = current_config_set['status']
        print('    Status: ' + current_config_set_status)
    if current_config_set.has_key('applicationServiceType'):
        current_config_set_last_deployment_time = current_config_set['applicationServiceType']
        print('    Application Service Type: ' + current_config_set_last_deployment_time)
    if current_config_set.has_key('analyticsMode'):
        current_config_set_last_deployment_time = current_config_set['analyticsMode']
        print('    Analytics Mode: ' + current_config_set_last_deployment_time)
    if current_config_set.has_key('protectionMode'):
        current_config_set_last_deployment_time = current_config_set['protectionMode']
        print('    Protection Mode: ' + current_config_set_last_deployment_time)
    if current_config_set.has_key('applicationReference'):
        current_config_set_application_reference = current_config_set['applicationReference']['link']
        current_config_set_application = requests.get(current_config_set_application_reference.replace('localhost', bigiq_ip), verify=False, headers=headers)
        current_config_set_application_name = json.loads(current_config_set_application.content)['name']
        print('    Application: ' + current_config_set_application_name)
    if current_config_set.has_key('tenantReference'):
        current_config_set_tenant_reference = current_config_set['tenantReference']['link']
        current_config_set_tenant = requests.get(current_config_set_tenant_reference.replace('localhost', bigiq_ip),verify=False, headers=headers)
        current_config_set_tenant_name = json.loads(current_config_set_tenant.content)['name']
        print('    Tenant: ' + current_config_set_tenant_name)
    if current_config_set.has_key('appSvcsTemplateReference'):
        current_config_set_app_svcs_template_reference = current_config_set['appSvcsTemplateReference']['link']
        current_config_set_app_svcs_template = requests.get(current_config_set_app_svcs_template_reference.replace('localhost', bigiq_ip), verify=False,headers=headers)
        current_config_set_app_svcs_template_name = json.loads(current_config_set_app_svcs_template.content)['name']
        print('    Application Services (AS3) Template: ' + current_config_set_app_svcs_template_name)
    if current_config_set.has_key('templateReference'):
        current_config_set_template_reference = current_config_set['templateReference']['link']
        current_config_set_template = requests.get(current_config_set_template_reference.replace('localhost', bigiq_ip), verify=False,headers=headers)
        current_config_set_template_name = json.loads(current_config_set_template.content)['name']
        print('    BIG-IQ Application Template: ' + current_config_set_app_svcs_template_name)
    if current_config_set.has_key('deviceReference'):
        current_config_set_device_reference = current_config_set['deviceReference']['link']
        current_config_set_device = requests.get(current_config_set_device_reference.replace('localhost', bigiq_ip),verify=False, headers=headers)
        current_config_set_device_name = json.loads(current_config_set_device.content)['address']
        print('    Device: ' + current_config_set_device_name)
    if current_config_set.has_key('selfLink'):
        current_config_self_link = current_config_set['selfLink']
        current_config_self_link = current_config_self_link.replace('localhost', bigiq_ip)
        print('    Link: ' + current_config_self_link)
    if current_config_set.has_key('subPath'):
        current_config_sub_path = current_config_set['subPath']
        print('    Sub-Path: ' + current_config_sub_path)
    if current_config_set.has_key('createDateTime'):
        current_config_set_last_config_time = current_config_set['createDateTime']
        print('    Created: ' + current_config_set_last_config_time)
    if current_config_set.has_key('lastConfigTime'):
        current_config_set_last_config_time = current_config_set['lastConfigTime']
        print('    Last Configured: ' + current_config_set_last_config_time)
    if current_config_set.has_key('lastDeploymentTime'):
        current_config_set_last_deployment_time = current_config_set['lastDeploymentTime']
        print('    Last Deployment: ' + current_config_set_last_deployment_time)