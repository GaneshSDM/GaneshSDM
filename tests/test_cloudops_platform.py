from cloudops.connectors.aws import AWSConnector
from cloudops.connectors.azure import AzureConnector
from cloudops.connectors.gcp import GCPConnector
from cloudops.platform import CloudOpsPlatform


def test_collect_posture_snapshot_includes_all_resources():
    platform = CloudOpsPlatform([AWSConnector(), AzureConnector(), GCPConnector()])
    snapshot = platform.collect_posture_snapshot()
    assert len(snapshot.resources) == 6
    providers = {resource.provider for resource in snapshot.resources}
    assert providers == {"aws", "azure", "gcp"}


def test_cost_summary_matches_snapshot():
    platform = CloudOpsPlatform([AWSConnector(), AzureConnector(), GCPConnector()])
    snapshot = platform.collect_posture_snapshot()
    totals = platform.summarize_costs(snapshot)

    assert totals["aws"] == 4270.5
    assert totals["azure"] == 3139.0
    assert totals["gcp"] == 2445.5
    assert totals["total"] == totals["aws"] + totals["azure"] + totals["gcp"]
