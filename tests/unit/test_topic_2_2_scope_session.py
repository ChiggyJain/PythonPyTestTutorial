import pytest


# scope=session means shared generated fixture for all tets-file including all defined test-function-cases
# Fixture created once for entire test run
@pytest.fixture(scope="session")
def app_config():
    return {
        "env": "test",
        "debug": True
    }


def test_config_env(app_config):
    assert app_config["env"] == "test"


def test_config_debug(app_config):
    assert app_config["debug"] is True
