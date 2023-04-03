import xmltodict

from boinc_client.clients.rpc_client import RpcClient

def set_global_prefs_override(client: RpcClient, pref: str = "") -> dict:    
    """Set global preference override."""
    rpc_resp = client.make_request("<set_global_prefs_override><global_preferences>" + pref + "</global_preferences></set_global_prefs_override>")
    rpc_json = xmltodict.parse(rpc_resp)
    read_global_prefs_override(client=client)   #prefs have to be read to activate them
    return rpc_json

def read_global_prefs_override(client: RpcClient) -> dict:    
    """Read and activate global preference override."""
    rpc_resp = client.make_request("<read_global_prefs_override/>")
    rpc_json = xmltodict.parse(rpc_resp)
    return rpc_json




