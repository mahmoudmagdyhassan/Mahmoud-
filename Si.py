import streamlit as st
st.code("st.text()", language='python')
st.text('Neptune AI Blog')
st.code("st.markdown()", language='python')
st.markdown('# This is Heading 1 in Markdown')
st.code("st.title()", language='python')
st.title('This is a title')
st.code("st.header()", language='python')
st.header('Header')
st.code("st.subheader()", language='python')
st.subheader('Sub Header')
st.code("st.latex()", language='python')
st.latex(r'''
...     a + ar + a r^2 + a r^3 + cdots + a r^{n-1} =
...     sum_{k=0}^{n-1} ar^k =
...     a left(frac{1-r^{n}}{1-r}right)
...     ''')
st.code("st.write()", language='python')
st.write('Can display many things')
st.button('Click here')
st.checkbox('Check')
st.radio('Radio', [1,2,3])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiple selection', [21,85,53])
st.slider('Slide', min_value=10, max_value=20)
st.select_slider('Slide to select', options=[1,2,3,4])
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Text area')
st.date_input('Date input')
st.time_input('Time input')
st.file_uploader('File uploader')
st.color_picker('Color Picker')
PASSWORD = config('PASSWORD')

session_state = SessionState.get(username='', password='')

if (session_state.password == PASSWORD):

    your_function()

elif ( session_state.password != PASSWORD):

    password_placeholder = st.empty()

    password = password_placeholder.text_input("Enter Password:", type="password")

    session_state.password = password

    if (password and session_state.password == PASSWORD):

        password_placeholder.empty()

        st.success("Logged in successfully")

        your_function()

    elif(password and session_state.password != PASSWORD):

        st.error("Wrong password")
