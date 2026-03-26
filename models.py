from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import ChoiceType

#criar o banco
db =  create_engine("sqlite:///banco.db")

#base do banco de dados
base = declarative_base()

#classes/tabelas

class Usuario(base):
    __tablename__ = "usuarios"
    id = Column("id", Integer, primary_key=True,autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean, default=False)

    def __init__(self,nome,email,senha,ativo = True,admin = False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin


class Pedido(base):
    __tablename__ = "pedidos"

    #Status_pedidos =(
    #    ("PENDENTE","PENDENTE"),
    #    ("CANCELADO", "CANCELADO"),
    #    ("FINALIZADO", "FINALIZADO")
    #    )
    
    id = Column("id", Integer, primary_key=True,autoincrement=True)
    status = Column("status", String)
    usuario = Column("usuario",ForeignKey("usuarios.id"))
    preco = Column("preco", Integer)
    
    def __init__(self,usuario, status="PENDENTE", preco = 0):
        self.status = status
        self.usuario = usuario
        self.preco = preco
        

class ItensPedido(base):
    __tablename__ = "item_pedidos"
    
    id = Column("id", Integer, primary_key=True,autoincrement=True)
    quantidade = Column("quantidade", Integer)
    sabor = Column("sabor", String)
    tamanho = Column("tamanho", String)
    valor_unitario = Column("valor_unitario",Float)
    pedido = Column("pedidos", ForeignKey("pedidos.id"))

    def __init__(self,quantidade,sabor,tamanho,valor_unitario,pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.valor_unitario = valor_unitario
        self.pedido = pedido

   
