from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.orm import Session

from models.member import Member


class MemberService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, name: str, email: str, member_id: Optional[int] = None) -> Member:
        obj = Member(
            member_id=member_id,
            name=name,
            email=email,
        )
        self.db.add(obj)
        self.db.flush()
        self.db.refresh(obj)
        return obj

    def list(self) -> List[Member]:
        return self.db.execute(select(Member)).scalars().all()

    def get(self, member_id: int) -> Optional[Member]:
        return self.db.get(Member, member_id)


    def update(self, member_id: int, name: Optional[str] = None, email: Optional[str] = None) -> Optional[Member]:
        obj = self.db.get(Member, member_id)
        if not obj:
            return None
        if name is not None:
            obj.name = name
        if email is not None:
            obj.email = email
        self.db.flush()
        self.db.refresh(obj)
        return obj

    def delete(self, member_id: int) -> bool:
        obj = self.db.get(Member, member_id)
        if not obj:
            return False
        self.db.delete(obj)
        return True
