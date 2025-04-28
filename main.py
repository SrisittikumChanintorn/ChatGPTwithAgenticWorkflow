import os
from openai import OpenAI
from agentic_workflow import *

# Set the API key for Anthropic 
CHATGPT_API_KEY = 'YOUR_API_KEY'  # Replace with your actual API key

# Get the permission from the owner of the API key to use it.
llm1 = OpenAI(api_key=CHATGPT_API_KEY) 

# Define the prompt for the first model ( as a root of tree of thought)
query = "What is the potential impact of Chinese price war on Thailand economy?"

# Define the model and max token for the models
slm_model = "gpt-3.5-turbo-16k"




# Branching the query into sub-branches
response_domestic_market_competition = domestic_market_competition(query, llm1, slm_model)

# reflection
reflection_response_domestic_market_competition = reflection(response_domestic_market_competition, llm1, slm_model)

# Sub-branches of domestic market competition
reflection_response_price_undercutting = price_undercutting(reflection_response_domestic_market_competition, llm1, slm_model)
reflection_response_market_share_losses = market_share_losses(reflection_response_domestic_market_competition, llm1, slm_model)
reflection_response_response_domestic_market_competition = innovation_and_quality_improvement(reflection_response_domestic_market_competition, llm1, slm_model)



# Branching the query into sub-branches
response_consumer_behavior = consumer_behavior(query, llm1, slm_model)

# reflection
reflection_response_consumer_behavior = reflection(response_consumer_behavior, llm1, slm_model)

# Sub-branches of consumer behavior
reflection_response_demand_for_cheaper_goods = demand_for_cheaper_goods(reflection_response_consumer_behavior, llm1, slm_model)
reflection_response_disposable_income_and_spending_patterns = disposable_income_and_spending_patterns(reflection_response_consumer_behavior, llm1, slm_model)
reflection_response_brand_layalty_and_perception = brand_layalty_and_perception(reflection_response_consumer_behavior, llm1, slm_model)


# If the Developer consider any of the Sub-branches answer not good enough, they decide to manually remove the Sub-branches.
final_query = reflection_response_price_undercutting + \
              reflection_response_market_share_losses + \
              reflection_response_response_domestic_market_competition + \
              reflection_response_demand_for_cheaper_goods + \
              reflection_response_disposable_income_and_spending_patterns + \
              reflection_response_brand_layalty_and_perception


# Make the final conclusion based on the sub-branches
final_response = make_conclusion(final_query, llm1, slm_model)

# Print the final response
print(final_response)