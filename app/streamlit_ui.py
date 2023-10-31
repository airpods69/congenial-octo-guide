from re import split
from typing import List
import streamlit as st
import random
import time
from llm_interface import generate_reply
from document_reader import get_content
from template import chat_script, AI_NAME, USER_NAME

st.title("Simple chat")

default_messages = [
        {"role": "user", "content": f"Hello {AI_NAME}"},
        {
            "role": "assistant",
            "content": f"Hello {USER_NAME}! How may I help you today?",
        },
        {"role": "user", "content": f"What is a cat?"},
        {
            "role": "assistant",
            "content": "A cat is a domestic species of small carnivorous mammal. It is the only domesticated species in the family Felidae.",
        },
    ]

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = default_messages.copy()


def generate_chat_script(messages: List[dict]):
    chat_script = ""
    for message in messages[-9:]:
        chat_script += (
            (f"{AI_NAME}: " if message["role"] == "assistant" else f"{USER_NAME}: ")
            + message["content"]
            + "\n"
        )

    return chat_script

uploaded_file = st.file_uploader("Choose file to summarize")
content = ""
if uploaded_file is not None:
    st.session_state.messages = default_messages.copy()
    pdf_bytes = uploaded_file.getvalue()
    content = "The contents of the given document is:\n\n" + get_content(pdf_bytes)
    # st.write(content)
    with st.chat_message("assistant"):
        st.markdown(content)

    # st.session_state.messages.append({"role": "assistant", "content": content})
    # prompt = "\nSummarize the contents of the emails in the given document."
    # n = 2046
    summary = ""

    summary = generate_reply(content)
    st.session_state.messages.append({"role": "assistant", "content": summary})
    

# Display chat messages from history on app rerun
for message in st.session_state.messages[4:]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])




# assistant_response = generate_reply(
#     prompt, generate_chat_script(st.session_state.messages)
# )


# # Accept user input
# if prompt := st.chat_input("What is up?"):
#     # Add user message to chat history
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     # Display user message in chat message container
#     with st.chat_message("user"):
#         st.markdown(prompt)
#
#     # Display assistant response in chat message container
#     with st.chat_message("assistant"):
#         message_placeholder = st.empty()
#         full_response = ""
#         # assistant_response = random.choice(
#         #     [
#         #         "Hello there! How can I assist you today?",
#         #         "Hi, human! Is there anything I can help you with?",
#         #         "Do you need help?",
#         #     ]
#         # )
#         assistant_response = generate_reply(
#             prompt, generate_chat_script(st.session_state.messages)
#         )
#         # Simulate stream of response with milliseconds delay
#         for chunk in assistant_response.split():
#             full_response += chunk + " "
#             time.sleep(0.05)
#             # Add a blinking cursor to simulate typing
#             message_placeholder.markdown(full_response + "▌")
#         message_placeholder.markdown(full_response)
#     # Add assistant response to chat history
#     st.session_state.messages.append({"role": "assistant", "content": full_response})
