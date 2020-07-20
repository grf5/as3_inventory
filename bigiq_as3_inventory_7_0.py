import requests
import json

bigiq_ip = '54.163.99.90'
username = 'admin'
password = 'f5c0nfig123!'

# Get an auth token from BIG-IQ
credentials_dict = {"username":username,"password":password}
headers = {'content-type':'application/json'}
token_auth_response = requests.post('https://' + bigiq_ip + '/mgmt/shared/authn/login', verify=False, data=json.dumps(credentials_dict), headers=headers)
auth_token = json.loads(token_auth_response.text)['token']['token']

# Get a list of all of the applications deployed on the BIG-IQ
headers = {'content-type':'application/json','X-F5-Auth-Token':auth_token}
global_config_sets_response = requests.get('https://' + bigiq_ip + '/mgmt/cm/global/config-sets', verify=False, headers=headers)
print(global_config_sets_response.content)
global_config_sets = json.loads(global_config_sets_response.content)['items']
for current_config_set in global_config_sets:
    current_config_set_name = current_config_set['configSetName']
    current_config_set_id = current_config_set['id']
    current_config_set_status = current_config_set['status']
    current_config_set_last_config_time = current_config_set['lastConfigTime']
    current_config_set_last_deployment_time = current_config_set['lastDeploymentTime']
    current_config_set_app_svcs_template_reference = current_config_set['appSvcsTemplateReference']['link']
    current_config_set_app_svcs_template = requests.get(current_config_set_app_svcs_template_reference.replace('localhost',bigiq_ip), verify=False, headers=headers)
    current_config_set_app_svcs_template_name = json.loads(current_config_set_app_svcs_template.content)['name']
    current_config_set_application_reference = current_config_set['applicationReference']['link']
    current_config_set_application = requests.get(current_config_set_application_reference.replace('localhost',bigiq_ip), verify=False, headers=headers)
    current_config_set_application_name = json.loads(current_config_set_application.content)['name']
    current_config_set_tenant_reference = current_config_set['tenantReference']['link']
    current_config_set_tenant = requests.get(current_config_set_tenant_reference.replace('localhost',bigiq_ip), verify=False, headers=headers)
    current_config_set_tenant_name = json.loads(current_config_set_tenant.content)['name']
    current_config_set_device_reference = current_config_set['deviceReference']['link']
    current_config_set_device = requests.get(current_config_set_device_reference.replace('localhost',bigiq_ip), verify=False, headers=headers)
    current_config_set_device_name = json.loads(current_config_set_device.content)['address']
    print('Name: ' + current_config_set_name)
    print('    Tenant: ' + current_config_set_tenant_name)
    print('    ID: ' + current_config_set_id)
    print('    Status: ' + current_config_set_status)
    print('    Application: ' + current_config_set_application_name)
    print('    Device: ' + current_config_set_device_name)
    print('    App Svcs Template: ' + current_config_set_app_svcs_template_name)
    print('    Last Configured: ' + current_config_set_last_config_time)
    print('    Last Deployment: ' + current_config_set_last_deployment_time)
    