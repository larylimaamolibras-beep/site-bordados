import streamlit as st
import urllib.parse
import os

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Flávia Confecção", page_icon="🪡", layout="wide")

# --- 2. ESTILO CSS ATUALIZADO (AVISO AMARELO ESCURO) ---
st.markdown("""
<style>
/* 1. FUNDO GERAL VERDE CLARINHO */
[data-testid="stAppViewContainer"] {
    background-color: #C1F0C1 !important;
}

/* 2. BARRA LATERAL BRANCA */
[data-testid="stSidebar"] {
    background-color: #FFFFFF !important;
}

/* 3. CAIXA DE AVISO AMARELO ESCURO (O que faltou!) */
[data-testid="stNotification"] {
    background-color: #FFD700 !important; /* Amarelo Ouro bem vivo */
    color: #000000 !important; /* Letra preta */
    border: 2px solid #B8860B !important; /* Borda dourada escura para destacar */
}

/* 4. EXPANDERS (AMOSTRAS) EM BRANCO */
.stExpander {
    background-color: #FFFFFF !important;
    border: 1px solid #000000 !important;
}

/* 5. FONTES GERAIS EM PRETO */
h1, h2, h3, p, span, label {
    color: #000000 !important;
    font-weight: 600 !important;
}

/* 6. CAIXA DE NAVEGAÇÃO NA LATERAL */
div[data-testid="stRadio"] {
    background-color: #C1F0C1 !important;
    padding: 15px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)
# --- 3. LÓGICA DE NAVEGAÇÃO ---
if "aba_home" not in st.session_state:
    st.session_state.aba_home = "Vitrine de Amostras"

def mudar_para_pedido():
    st.session_state.aba_home = "Fazer Pedido"

# --- 4. BARRA LATERAL ---
with st.sidebar:
    st.markdown("### Bem-vinda(o)!")
    caminho_logo = "logo.jpg" 
    if os.path.exists(caminho_logo): st.image(caminho_logo, width=300)
    elif os.path.exists("logo.jpg.jpeg"): st.image("logo.jpg.jpeg", width=300)
    
    st.markdown("Olá, sou a Flavia! Ofereço serviços de bordado, kits de maternidade e jogos de cama sob medida.")
    st.write("---")
    escolha = st.radio("Navegação", ["Vitrine de Amostras", "Fazer Pedido"], key="aba_home")

# --- 5. CONTEÚDO PRINCIPAL ---
meu_whatsapp = "5581981262102"
st.title("Flávia Confecção")

if escolha == "Vitrine de Amostras":
    st.subheader("✨ Minhas Amostras")

    # TEMA SAFARI - TAMANHO 100
    with st.expander("🦁 Tema: Safari"):
        col_img, col_txt = st.columns([0.5, 1]) # Coluna da foto menor
        with col_img:
            if os.path.exists("Foto Safari.jpg"): 
                st.image("Foto Safari.jpg", width=198) # Tamanho 100 aqui
            else: 
                st.info("Foto Safari")
        with col_txt:
            st.write("**Turminha e com nomes*")
            st.write("R$ 25,00",)
    
    # TEMA BAILARINA - FOTOS SEPARADAS
    with st.expander("🩰 Tema: Bailarina"):
        b_col1, b_col2 = st.columns(2)
        
        # Modelo 1
        with b_col1:
            img_c, txt_c = st.columns([0.5, 1])
            with img_c:
                if os.path.exists("bailarina1.jpg"): 
                    st.image("bailarina1.jpg", width=100)
                else: 
                    st.info("Foto Bailarina 1")
            with txt_c:
                st.write("**Bailarina Mod. 1**")
                st.write("R$ 15,00")
        
        # Modelo 2
        with b_col2:
            img_c, txt_c = st.columns([0.5, 1])
            with img_c:
                if os.path.exists("bailarina2.jpg"): 
                    st.image("bailarina2.jpg", width=100)
                else: 
                    st.info("Foto Bailarina 2")
            with txt_c:
                st.write("**Bailarina Mod. 2**")
                st.write("R$ 15,00")

                # Modelo 3
        with b_col2:
            img_c, txt_c = st.columns([0.5, 1])
            with img_c:
                if os.path.exists("bailarina3.jpg"): 
                    st.image("bailarina3.jpg", width=100)
                else: 
                    st.info("Foto Bailarina 3")
            with txt_c:
                st.write("**Bailarina Mod. com nomes 3**")
                st.write("R$ 25,00")

    # TEMA SOBREPOSTO 1 NOME
    with st.expander("🔠 Tema: Sobreposto (1 Nome)"):
        col_img, col_txt = st.columns([0.5, 1])
        with col_img:
            if os.path.exists("sobreposto1.jpg"): 
                st.image("sobreposto1.jpg", width=100)
            else: 
                st.info("Foto 1 Nome")
        with col_txt:
            st.write("**Sobreposto: 1 Nome**")
            st.write("R$ 15,00")

    # TEMA SOBREPOSTO 2 NOMES
    with st.expander("🔡 Tema: Sobreposto (2 Nomes)"):
        col_img, col_txt = st.columns([0.5, 1])
        with col_img:
            if os.path.exists("sobreposto2.jpg"): 
                st.image("sobreposto2.jpg", width=100)
            else: 
                st.info("Foto 2 Nomes")
        with col_txt:
            st.write("**Sobreposto: 2 Nomes**")
            st.write("R$ 20,00")

    st.write("---")
    st.warning("### 💡 Não encontrou o que gostou?")
    st.button("✨ Se não gostou, peça outro", on_click=mudar_para_pedido)

elif escolha == "Fazer Pedido":
    st.subheader("📝 Detalhes do seu Pedido")
    
    col1, col2 = st.columns(2)
    with col1:
        cliente = st.text_input("Seu Nome:", placeholder="Como podemos te chamar?")
        nome_bordar = st.text_input("Nome para Bordar:", placeholder="Ex: Arthur, Helena...")
    with col2:
        tipo_prod = st.selectbox("Tipo de Produto:", ["Fralda", "Toalha", "Kit Maternidade", "Outro"])
        tema_opcoes = ["Safari", "Bailarina", "Sobreposto 1 Nome", "Sobreposto 2 Nomes", "Personalizado"]
        tema_escolhido = st.selectbox("Escolha do Tema:", tema_opcoes)

    detalhes = st.text_area("Descreva outros detalhes:")
    
    if st.button("Finalizar Pedido"):
        if cliente and nome_bordar:
            msg = (f"Olá Flávia! Pedido de {cliente}:\n"
                   f"- Produto: {tipo_prod}\n"
                   f"- Tema: {tema_escolhido}\n"
                   f"- Nome para Bordar: {nome_bordar}\n"
                   f"- Detalhes: {detalhes}")
            link = f"https://wa.me/{meu_whatsapp}?text={urllib.parse.quote(msg)}"
            st.markdown(f'[✅ Enviar no WhatsApp]({link})')
            st.balloons()
        else:
            st.error("⚠️ Preencha seu nome e o nome para o bordado!")