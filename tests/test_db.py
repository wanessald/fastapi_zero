from dataclasses import asdict

import pytest
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_zero.models import Todo, User


@pytest.mark.asyncio
async def test_create_user(session: AsyncSession, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(username='test', email='test@test', password='secret')

        # pattern: unit of work
        # Realiza várias op na sessão e uma única op com o db
        session.add(new_user)
        await session.commit()

        user = await session.scalar(
            select(User).where(User.username == 'test')
        )

    assert asdict(user) == {
        'id': 1,
        'username': 'test',
        'email': 'test@test',
        'password': 'secret',
        'created_at': time,
        'updated_at': time,
        'todos': [],
    }


@pytest.mark.asyncio
async def test_create_user_error(session: AsyncSession, user: User):
    todo = Todo(
        title='Test todo',
        description='Test todo description',
        state='test',
        user_id=user.id,
    )

    session.add(todo)
    await session.commit()

    with pytest.raises(LookupError):
        await session.scalar(select(Todo))
