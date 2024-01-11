import pytest

# Am creata aceasta clasa pentru optimizarea codului, sa nu mai scriem de fiecare data,
# @pytest.usefixture("setup_browser), iar in functie sa introducem numele fixture-ului

@pytest.mark.usefixtures("setup_browser")
class BaseClass:
    pass