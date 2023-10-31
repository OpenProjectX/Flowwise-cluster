import autogen
import openai

# openai.proxy = {
#     "http": "http://127.0.0.1:10809",
#     "https": "http://127.0.0.1:10809"
# }


def start_chatbot():
    # import OpenAI API key
    config_list = autogen.config_list_from_json(env_or_file="OAI_CONFIG_LIST")

    # create the assistant agent
    assistant = autogen.AssistantAgent(
        name="assistant", llm_config={"config_list": config_list}
    )

    # Create the user proxy agent
    user_proxy = autogen.UserProxyAgent(
        name="UserProxy", code_execution_config={"work_dir": "results"}
    )

    # Start the conversation
    user_proxy.initiate_chat(
        assistant, message="Write a code to print odd numbers from 2 to 100."
    )


if __name__ == "__main__":
    start_chatbot()
