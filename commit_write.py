from git import Repo
import openai
repo = Repo('./')
diff_output = repo.git.diff('./')


prompt_for_GPT="  Here is a git diff, it has information about what lines have been changed, could you write a simple an concise git commit message such that anyone reading can get a rough idea of what this git commit was about?. Also please just return the value as a String with no qoutation marks. \n " + diff_output
print(prompt_for_GPT)
openai.api_key = "InsertKey"

# list models
models = openai.Model.list()

# print the first model's id
print(models.data[0].id)

# create a completion
completion = openai.Completion.create(model="text-davinci-003", prompt=prompt_for_GPT)

# print the completion
print(completion.choices[0].text)
