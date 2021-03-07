from ansible_collections.community.mysql.plugins.module_utils.mysql import get_server_version
from distutils.version import LooseVersion


def uses_replica_terminology(cursor):
    """Checks if REPLICA must be used instead of SLAVE"""
    return LooseVersion(get_server_version(cursor)) >= LooseVersion('10.5.1')
