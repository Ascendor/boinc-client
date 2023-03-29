import xmltodict

from boinc_client.clients.rpc_client import RpcClient

def set_global_prefs_override(client: RpcClient, mode: str = "") -> dict:    
    """Set global preference override."""
    rpc_resp = client.make_request("<set_global_prefs_override><global_preferences><cpu_usage_limit>50</cpu_usage_limit></global_preferences></set_global_prefs_override>")
    rpc_json = xmltodict.parse(rpc_resp)
    return rpc_json
