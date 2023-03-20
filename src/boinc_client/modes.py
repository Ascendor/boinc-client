import xmltodict

from boinc_client.clients.rpc_client import RpcClient

def run_mode(client: RpcClient, mode: str = "auto") -> dict:
    """Set run mode."""
    rpc_resp = client.make_request("<set_run_mode><" + mode + "/></set_run_mode>")
    rpc_json = xmltodict.parse(rpc_resp)
    return rpc_json
