import pytest

from tests.conftest import setup


@pytest.mark.usefixtures("setup")

class BaseTest:
    pass