import streamlit as st



left, cent, right = st.columns(3)
with right:
   st.image('C:\Users\Gustavo\OneDrive\Documentos\MVP\LOGO.png')
    
st.title('O projeto')
st.markdown(
    '''
        <div style="text-align: justify;">
            <p>
                Este projeto tem por objetivo o desenvolvimento de um dashboard interativo capaz de gerar insights relevantes para tomada de decisão no que diz respeito ao negócio do petróleo brent, o que inclui a implementação de um modelo de Machine Learning que traga o forecasting dos preços.
            </p>
            <p>
                Esta aplicação é um MVP. O projeto completo está disponível em <b><a style='text-decoration:none', href='add link do repositorio'>repositório</a></b> GitHub.
            </p>
    ''',
    unsafe_allow_html=True
)