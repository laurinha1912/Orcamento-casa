import streamlit as st

st.title("Orçamento Casa Completo")

st.write("Preencha as informações para cada etapa da construção:")
categorias = ["Fundação", "Estrutura", "Cobertura", "Revestimentos", "Enquadrias"]

if "custos" not in st.session_state:
    st.session_state.custos = {categoria: [] for categoria in categorias}


for categoria in categorias:
    with st.expander(f"Categoria: {categoria}"):       
        if categoria == "Fundação":
            st.image("https://www.mapadaobra.com.br/wp-content/uploads/2016/10/Novo_Layout-3.jpg", caption="Fundação exemplo", use_container_width=True)
            item = st.selectbox("Escolha o material:", ["Blocos de concreto", "Areia", "Cimento", "Brita", "Ferro"], key=f"item_{categoria}")
        elif categoria == "Estrutura":
            st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdUgPrs2-0D6wAvW5IUVbx_uARt_XUTXQyTQ&s", caption="Estrutura exemplo", use_container_width=True)
            item = st.selectbox("Escolha o material:", ["Tijolos", "Blocos Cerâmicos", "Cimento", "Aço", "Madeira"], key=f"item_{categoria}")
        elif categoria == "Cobertura":
            st.image("https://casadoconstrutor.com.br/sites/default/files/styles/blog_extra_grande_816x304/public/2024-11/fase-da-obra-cobertura-tudo-que-voce-precisa-saber.jpg.webp?itok=HzixqY5h", caption="Cobertura exemplo", use_container_width=True)
            item = st.selectbox("Escolha o material:", ["Telhas", "Estrutura"], key=f"item_{categoria}")
            if item == "Telhas":
                item += f" ({st.selectbox('Tipo de Telha:', ['Cerâmica', 'Metálica'], key=f'tipo_{categoria}')})"
            else:
                item += f" ({st.selectbox('Tipo de Estrutura:', ['Madeira', 'Metálica'], key=f'tipo_{categoria}')})"
        elif categoria == "Revestimentos":
            st.image("https://reformweb.com.br/img/reboco_04.jpg", caption="Revestimento exemplo", use_container_width=True)
            item = st.selectbox("Escolha o material:", ["Piso", "Pintura"], key=f"item_{categoria}")
        elif categoria == "Enquadrias":
            st.image("https://www.tudoconstrucao.com/wp-content/uploads/2020/01/35cef589cc8d9fa8818db5fe79ce6831.jpg", caption="Enquadria exemplo", use_container_width=True)
            item = st.selectbox("Escolha o material:", ["Portas", "Janelas"], key=f"item_{categoria}")

        
        valor = st.text_input(f"Digite o preço do(a) {item}:", key=f"valor_{categoria}")
        quantidade = st.text_input(f"Quantidade de {item}:", key=f"quantidade_{categoria}")

        
        if st.button(f"Adicionar {item} à categoria {categoria}", key=f"adicionar_{categoria}"):
            if valor and quantidade:
                try:
                    custo_total_item = float(valor) * float(quantidade)
                    st.session_state.custos[categoria].append({"item": item, "quantidade": quantidade, "valor": valor, "custo_total": custo_total_item})
                    st.success(f"Adicionado: {item} - Quantidade: {quantidade}, Preço Unitário: R$ {valor}, Total: R$ {custo_total_item:.2f}")
                except ValueError:
                    st.error("Por favor, insira valores numéricos válidos para preço e quantidade.")
            else:
                st.warning("Preencha todos os campos antes de adicionar.")


if st.button("Calcular Orçamento Total"):
    total_geral = sum(item["custo_total"] for categoria in st.session_state.custos.values() for item in categoria)
    if total_geral > 0:
        st.success(f"O custo total estimado é R$ {total_geral:.2f}")
        for categoria, itens in st.session_state.custos.items():
            if itens:
                st.subheader(f"Categoria: {categoria}")
                for item in itens:
                    st.write(f"{item['item']}: Quantidade {item['quantidade']}, Preço Unitário {item['valor']} reais, Total {item['custo_total']:.2f} reais")
    else:
        st.warning("Nenhum item foi adicionado para calcular o orçamento.")
