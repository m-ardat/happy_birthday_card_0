# ИМПОРТ БИБЛИОТЕК
import streamlit as st
import streamlit_antd_components as sac
from streamlit_lottie import st_lottie
import json

# КОНФИГУРАЦИЯ ПРИЛОЖЕНИЯ
st.set_page_config(
    page_title="Happy Birthday Card",
    page_icon=":material/featured_seasonal_and_gifts:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None
)

# ОФОРМЛЕНИЕ
st.markdown(
    """
    <style>    
    /* НАСТРОЙКИ ШРИФТА */
    /* Изменение цвета текста и шрифта в label */
    [data-testid="stWidgetLabel"] {
        font-size: 14px;                        /* Размер текста */
        font-family: 'Helvetica', sans-serif;   /* Шрифт текста */
    }

    /* Изменение шрифта */
    bodybody, h1, h2, h3, h4, h5, h6, p, div, span, li, a, blockquote, pre, code {
        font-family: 'Helvetica', sans-serif;
    }
    .st-emotion-cache-16tyu1 h1, 
    .st-emotion-cache-16tyu1 h2, 
    .st-emotion-cache-16tyu1 h3, 
    .st-emotion-cache-16tyu1 h4, 
    .st-emotion-cache-16tyu1 h5, 
    .st-emotion-cache-16tyu1 h6, 
    .st-emotion-cache-102y9h7 h1, 
    .st-emotion-cache-102y9h7 h2, 
    .st-emotion-cache-102y9h7 h3, 
    .st-emotion-cache-102y9h7 h4, 
    .st-emotion-cache-102y9h7 h5, 
    .st-emotion-cache-102y9h7 h6,
    .st-emotion-cache-16tyu1 td {
        font-family: 'Helvetica', sans-serif;
    }   

    /* Скрыть кнопку увеличение изображения */
    .st-emotion-cache-z56u96 {
        display: none;
    }
    
    /* Скрыть якорь заголовка */
    .st-emotion-cache-gi0tri {
        display: none !important;
    }
    
    </style>
    """,
    unsafe_allow_html=True
)

# ФУНКЦИИ
# Загрузка Lottie-анимации из локального файла
def load_lottie_file(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

#ФРОНТ
# Заголовок
st.markdown("""
<h1 style="text-align: center; 
           margin: -81px 0 15px 0;   /* top, right, bottom, left */
           color: #2e2e2e; 
           font-family: 'Helvetica', sans-serif; 
           font-size: 4rem;
           font-weight: bold;">
    С Днём Рождения! 🎉
</h1>
""", unsafe_allow_html=True)

# Пожелания
text0 = """Саша, поздравляем тебя С Днём Рождения!
Пусть твоя деятельность приносит не только стабильный доход, но и настоящее удовольствие - ты создаёшь что-то важное. 
Больше свободного времени для любимых увлечений/хобби, чтобы ты мог по-настоящему отдохнуть и зарядиться энергией. 
И, конечно, крепкого здоровья — оно важнее всего, чтобы и трудиться, и наслаждаться жизнью было в радость!
P.S.: В этом году без примеров.
"""
text1 = """Тридцатник уже ближе, чем молодецкие 25, потому желаю не костенеть, пробовать новое и обрастать интересными увлечениями, дабы новые кризисы проходили мягко и почти незаметно.
"""
text2 = """Сан Сергеич! 
Ты – человек, с которым всегда легко (правда правда) и весело (не соскучишься точно), и я очень рад (по факту) иметь такого друга. 
Пусть коленки не скрипят, тараканы – разбегаются, а тусан – черный.
С новым годом!
"""

# Словарь с данными
dict_options = {
    "Максим и Алина": ("files/image0.jpg", text0),
    "Алексей": ("files/image1.jpg", text1),
    "Михаил": ("files/image2.jpg", text2)
}

with st.sidebar.container():
    selected_brach = sac.menu(
        items=[
            sac.MenuItem(label="С Днём Рождения!"),
            *[sac.MenuItem(label=name_k, icon="gift") for name_k in dict_options.keys()]
        ],
        variant="filled",
        color="#4285b4",
        indent=30
    )

if selected_brach == "С Днём Рождения!":
    lottie_animation = load_lottie_file("files/congratulation.json")
    st_lottie(lottie_animation, height=300, key="birthday")

else:
    col1, col2 = st.columns([1,1], vertical_alignment="top")
    with st.container():
        with col1:
            st.image(image=dict_options[selected_brach][0], use_container_width=True)

    with col2:
        st.markdown(f"""
        <div 
            style="background-color: #FFFAFA; 
            padding: 20px; 
            border-radius: 8px; 
            text-align: left; 
            font-style: italic; 
            color: #2E2E2E;
            white-space: pre-line;
            margin: 0;">
            {dict_options[selected_brach][1]}
        """, unsafe_allow_html=True)