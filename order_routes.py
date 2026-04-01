from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends
from dependencies import pegar_sessao, verificar_token
from schemas import PedidoSchema
from models import Pedido,Usuario


order_router = APIRouter(prefix="/order", tags=["order"], dependencies=[Depends(verificar_token)])

@order_router.get("/")
async def pedidos():
    """
    Essa é a rota padrão de pedidos do nosso sistema
    """
    return {"mensagem : Você acessou a lista de pedidos"}

@order_router.post("/pedidos")
async def criar_pedido(pedido_schema: PedidoSchema, session: Session = Depends(pegar_sessao)):
    novo_pedido = Pedido(usuario = pedido_schema.id_usuario)
    session.add(novo_pedido)
    session.commit()
    return{"mensagem":f"Pedido criado com sucesso. Id do pedido: {novo_pedido.id}" }

@order_router.post("/pedidos/cancelar/{id_pedido}")
async def cancelar_pedido(id_pedido:int,session: Session = Depends(pegar_sessao),usuario: Usuario = Depends(verificar_token)):
    #usuario_admin = true
    #usuario_id = pedido usuario
    pedido = session.query(Pedido).filter(Pedido.id==id_pedido).first()
    if not pedido:
        raise HTTPException(status_code = 400, detail="Pedido não encontrado")
    if not usuario.admin and usuario.id != pedido.usuario:
        raise HTTPException(status_code=401, detail="Você não tem autorização para essa modificação")
    pedido.status = "CANCELADO"
    session.commit()
    return {
        "mensagem" : f"Pedido número: {id_pedido} cancelado com sucesso",
        "pedido" : pedido
    }