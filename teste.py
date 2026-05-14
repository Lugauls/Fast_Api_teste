from models import db, base, Usuario
from sqlalchemy.orm import Session
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

with Session(db) as session:
    admin = Usuario(
        nome="Admin2",
        email="admin2@admin.com",
        senha=pwd_context.hash("123456"),  # senha criptografada
        ativo=True,
        admin=True
    )
    session.add(admin)
    session.commit()
    print("Usuário admin criado com sucesso!")