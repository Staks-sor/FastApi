import pytest
from sqlalchemy import insert, select

from auth.models import role
from conftest import async_session_maker


def test_register():
    assert 1 == 1
