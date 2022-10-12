"""Test of the command line interface."""

import pytest

from nt_users_tool import cli


def test_main():
    """Test the main function."""
    with pytest.raises(NotImplementedError):
        cli.main()
