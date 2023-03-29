from pytest import fixture


@fixture
def success_xml() -> str:
    return """<boinc_gui_rpc_reply>
    <success/>
</boinc_gui_rpc_reply>"""

@fixture
def success_dict() -> dict:
    return {
        "boinc_gui_rpc_reply": 
            {
                "success": None
            }        
    }