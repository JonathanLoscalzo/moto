import json
import sure  # noqa # pylint: disable=unused-import

import moto.server as server


def test_appsync_list_tags_for_resource():
    backend = server.create_backend_app("appsync")
    test_client = backend.test_client()

    resp = test_client.get(
        "/v1/tags/arn%3Aaws%3Aappsync%3Aus-east-1%3A123456789012%3Aapis%2Ff405dd93-855e-451d-ab00-7325b8e439c6?tagKeys=Description"
    )
    resp.status_code.should.equal(200)
    json.loads(resp.data).should.equals({"tags": {}})
