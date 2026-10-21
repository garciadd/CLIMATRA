"""Initial package smoke tests; add behavioral tests with each new feature."""


def test_package_imports():
    import climatra

    assert "CLIMATRA" in climatra.__doc__
