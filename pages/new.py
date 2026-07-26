import streamlit as st
import streamlit.components.v1 as components

st.title("New Page")

st.write("counting app")

st.write("This is a simple counting app. You can increase or decrease the count using the buttons below.")

if "count" not in st.session_state:
    st.session_state.count = 0

col1, col2, col3 = st.columns(3)

if col1.button("Increase"):
    st.session_state.count += 1

if col2.button("Decrease"):
    st.session_state.count -= 1

if col3.button("Reset"):
    st.session_state.count = 0

st.write(f"Count: {st.session_state.count}")

st.divider()

components.html("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>test</title>
        <style>
            #demo {
                font-size: 30px;
                color:#aaaaff;
            }
        </style>
    </head>
    <body>
        <p id="demo"></p>
        <button onclick="aa()">click</button>
        <script>
        function aa() {
            name = prompt("hi " + name + ", enter your name");
            document.getElementById('demo').innerHTML = "Made Using html and streamlit"; 
        }
        </script>
    </body>
    </html>
""")
st.divider()
st.header("Radio section")
radio = st.radio("What you want", ["nothing", "absolutely nothing", "nothing at all"])
st.write(f"I want {radio}")
st.code("st.radio()", language="python")

st.divider()
st.header("selectbox section")
select = st.selectbox("What you want", ["nothing", "absolutely nothing", "nothing at all"])
st.write(f"I want {select}")
st.code("st.selectbox()", language="python")

st.header("multiselect section")
multi = st.multiselect("What you want", ["nothing", "absolutely nothing", "nothing at all"])
st.write(f"I want {multi}")
st.code("st.multiselect()", language="python")

st.divider()
st.header("slider section")
slider = st.slider("What is your age?", 0, 100, 25)
st.write(f"My age is {slider}")
age = st.empty()
st.code("st.slider()", language="python")

if slider <= 18:
    age.write("young coder")
elif slider < 25:
    age.write("Unc")
else:
    age.write(" ")

st.divider()

st.header("text_input section")
text = st.text_input("What is your name?","the best Coder")
st.write(f"Hello, {text}!")
st.code("st.text_input()", language="python")

st.header("text_area section")
ta = st.text_area("write something here","its just an simple example")
st.write(f"You wrote: {ta}")
st.code("st.text_area()", language="python") and

st.header("number_input section")
num = st.number_input("enter a number", -100, 100, 0)
st.write(f"You entered: {num}")
st.code("st.number_input()", language="python")
st.divider()

st.header("")