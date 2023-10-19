import streamlit as st
import random
import time
from llm_interface import generate_reply
from document_reader import get_content
from template import chat_script, AI_NAME
chat_script = chat_script

st.title("Simple chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hey there!"}]

uploaded_file = st.file_uploader("Choose file to summarize")
content = ""
if uploaded_file is not None:
    pdf_bytes = uploaded_file.getvalue()
    content = "The contents of the given document is:\n\n" + get_content(pdf_bytes)
    # st.write(content)
    with st.chat_message("assistant"):
        st.markdown(content)


# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        # assistant_response = random.choice(
        #     [
        #         "Hello there! How can I assist you today?",
        #         "Hi, human! Is there anything I can help you with?",
        #         "Do you need help?",
        #     ]
        # )
        assistant_response = generate_reply(
            f"\n{content}\n"
            + prompt, chat_script
        )
        chat_script += f"{AI_NAME}: {assistant_response.split(f'{AI_NAME}')[-1]}"
        # Simulate stream of response with milliseconds delay
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
