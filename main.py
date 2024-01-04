# Printing the welcome intro in the output
print("Welcome to Smart Contract Generator!!\n")
print("Let's build an ERC-20 Smart Contract!!!!\n")

# Ask the user for the smart contract inputs for the application to generate a correct smart contract
user_pragma_version = input("Input the smart contract version:\n")
user_token_name = input("What is the name of your token?\n")
user_token_symbol = input("What is the ticker symbol for your token?\n")
user_initial_supply = input("What is the total supply of your token going to be? (Please refer to the extra 0's)\n")
name_solidity_creation_file = input("What name do you want your smart contract file to be when generated? (Be sure to"
                                    "add a .sol in you input)")


# Reading the erc20.sol template
def read_template(file_path):
    with open(file_path, 'r') as file:
        return file.read()


# filling the brackets in the template from the user inputs
def fill_template(contract_template, values):
    for key, value in values.items():
        contract_template = contract_template.replace(f'{{{key}}}', value)
    return contract_template


# Writing to a new sol file based on the template and user inputs
def write_to_file(content, filename):
    with open(filename, 'w') as file:
        file.write(content)


# user inputs and names of the brackets in template
user_inputs = {
    'contract_version': user_pragma_version,
    'token_name': user_token_name,
    'token_symbol': user_token_symbol,
    'initial_supply': user_initial_supply
}

template_content = read_template('erc20.sol')
final_contract = fill_template(template_content, user_inputs)
write_to_file(final_contract, name_solidity_creation_file)
