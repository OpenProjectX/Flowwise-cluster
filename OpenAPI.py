import os, yaml
import openai

from langchain.llms.openai import OpenAI
from langchain.agents.agent_toolkits.openapi import planner
from langchain.agents.agent_toolkits.openapi.spec import reduce_openapi_spec
from langchain.requests import RequestsWrapper

openai.proxy = {
    "http": "http://127.0.0.1:10809",
    "https": "http://127.0.0.1:10809"
}

llm = OpenAI(temperature=0, verbose=True, openai_api_key='replace withh your key')

with open("trino.yaml") as f:
    raw_spotify_api_spec = yaml.load(f, Loader=yaml.Loader)
spotify_api_spec = reduce_openapi_spec(raw_spotify_api_spec)

requests_wrapper = RequestsWrapper()

trino_agent = planner.create_openapi_agent(spotify_api_spec, requests_wrapper, llm)
user_query = (
    "make me a playlist with the first song from kind of blue. call it machine blues."
)
trino_agent.run(user_query)
