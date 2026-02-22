# Ficheiro gerado: 2025_05_10_add_coluna_stripe_id.py

def upgrade():
    # O que acontece ao subir de versão
    op.add_column('utilizadores', sa.Column('stripe_customer_id', sa.String(50)))

def downgrade():
    # O que acontece se precisarmos de voltar atrás
    op.drop_column('utilizadores', 'stripe_customer_id')
