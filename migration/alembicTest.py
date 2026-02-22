"""Adiciona coluna stripe_id

Revision ID: 4fbc22a1
Revisão Anterior: 3eab11b2
Data: 2025-05-10
"""
from alembic import op
import sqlalchemy as sa

# Identificadores da versão (gerados automaticamente pelo Alembic)
revision = '4fbc22a1'
down_revision = '3eab11b2'

def upgrade():
    """O que acontece ao subir de versão (Adicionar a coluna)"""
    op.add_column('utilizadores', 
        sa.Column('stripe_customer_id', sa.String(length=50), nullable=True)
    )

def downgrade():
    """O que acontece se precisarmos de voltar atrás (Remover a coluna)"""
    op.drop_column('utilizadores', 'stripe_customer_id')
