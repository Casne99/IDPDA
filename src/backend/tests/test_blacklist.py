import bcrypt
import pytest
from app.models import Blacklist, Credentials
from sqlalchemy.orm import Session


@pytest.fixture(autouse=True)
def setup_db(db_session):
    db_session.query(Blacklist).delete()
    db_session.query(Credentials).delete()
    db_session.commit()
    password_hash = bcrypt.hashpw("password".encode(), bcrypt.gensalt()).decode()
    user = Credentials(user="admin", password=password_hash)
    db_session.add(user)
    db_session.commit()


def test_user_not_in_blacklist(db_session: Session):
    result = db_session.query(Blacklist).filter(Blacklist.user == "admin").first()
    assert result is None


def test_user_in_blacklist(db_session: Session):
    entry = Blacklist(user="admin")
    db_session.add(entry)
    db_session.commit()

    result = db_session.query(Blacklist).filter(Blacklist.user == "admin").first()
    assert result is not None
    assert result.user == "admin"


def test_blacklist_requires_existing_user(db_session: Session):
    entry = Blacklist(user="nonexistent")
    db_session.add(entry)
    with pytest.raises(Exception):
        db_session.commit()
    db_session.rollback()
