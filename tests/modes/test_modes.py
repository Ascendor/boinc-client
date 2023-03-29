from boinc_client.modes import run_mode


def test_successfull(
    mocker,
    mock_rpc_client,
    success_xml,
    success_dict,
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=success_xml,
    )
    assert run_mode(client=mock_rpc_client, mode="always") == success_dict