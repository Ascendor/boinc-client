import xmltodict

from boinc_client.clients.rpc_client import RpcClient

def set_global_prefs_override(client: RpcClient, mode: str = "") -> dict:    
    """Set global preference override."""
    rpc_resp = client.make_request("<set_global_prefs_override><cpu_usage_limit>0.5</cpu_usage_limit></set_global_prefs_override>")
    rpc_json = xmltodict.parse(rpc_resp)
    return rpc_json
